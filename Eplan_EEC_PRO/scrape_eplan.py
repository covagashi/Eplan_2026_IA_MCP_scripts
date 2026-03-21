"""
Scraper for EPLAN EEC Pro 2026 documentation.
Downloads all help pages and converts them to Markdown for RAG.
"""
import os
import re
import json
import time
import requests
import html2text
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

BASE_URL = "https://www.eplan.help/en-us/infoportal/content/eecpro/2026"
CHUNK_URL = f"{BASE_URL}/Data/Tocs/main_Chunk{{i}}.js?t=639064803756181400"
NUM_CHUNKS = 6
OUTPUT_DIR = Path("docs_md")
MAX_WORKERS = 5  # Concurrent downloads (be respectful)
DELAY = 0.3  # Seconds between requests per thread

# Configure html2text
h2t = html2text.HTML2Text()
h2t.ignore_links = False
h2t.ignore_images = True
h2t.ignore_emphasis = False
h2t.body_width = 0  # No wrapping
h2t.unicode_snob = True


def fetch_chunk(i: int) -> dict:
    """Fetch a chunk JS file and parse the entries."""
    url = CHUNK_URL.format(i=i)
    print(f"  Fetching chunk {i}: {url}")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    text = resp.text

    # The JS is: define({...})
    # Extract the JSON-like object inside define(...)
    match = re.search(r'define\((\{.*\})\)', text, re.DOTALL)
    if not match:
        print(f"  WARNING: Could not parse chunk {i}")
        return {}

    js_obj = match.group(1)

    # Parse entries: '/Content/htm/xxx.htm': { i: [...], t: ['Title'], b: [''] }
    entries = {}
    # Use regex to extract path and title
    pattern = r"'(/Content/htm/[^']+\.htm)'\s*:\s*\{[^}]*t\s*:\s*\['([^']*)'\]"
    for m in re.finditer(pattern, js_obj):
        path = m.group(1)
        title = m.group(2)
        entries[path] = title

    print(f"  Chunk {i}: found {len(entries)} entries")
    return entries


def fetch_all_entries() -> dict:
    """Fetch all chunks and combine entries."""
    print("Fetching TOC chunks...")
    all_entries = {}
    for i in range(NUM_CHUNKS):
        try:
            entries = fetch_chunk(i)
            all_entries.update(entries)
        except Exception as e:
            print(f"  ERROR fetching chunk {i}: {e}")
    print(f"\nTotal entries found: {len(all_entries)}")
    return all_entries


def download_and_convert(path: str, title: str) -> tuple[str, bool, str]:
    """Download a single page and convert to markdown."""
    url = BASE_URL + path
    filename = Path(path).stem  # e.g., admin_h_backup
    # Determine category from filename prefix
    category = filename.split("_")[0] if "_" in filename else "general"

    out_dir = OUTPUT_DIR / category
    out_file = out_dir / f"{filename}.md"

    if out_file.exists():
        return path, True, "skipped (exists)"

    try:
        resp = requests.get(url, timeout=30, headers={
            "User-Agent": "Mozilla/5.0 (documentation-archiver)"
        })
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")

        # Remove navigation, header, footer elements
        for tag in soup.find_all(["nav", "header", "footer", "script", "style"]):
            tag.decompose()

        # Try to find main content area
        content = soup.find("div", class_="body-container") or \
                  soup.find("div", id="mc-main-content") or \
                  soup.find("div", class_="topic-layout") or \
                  soup.find("body")

        if content is None:
            content = soup

        html_content = str(content)

        # Convert to markdown
        markdown = h2t.handle(html_content)

        # Add frontmatter
        md_output = f"""---
title: "{title}"
source: "{url}"
file: "{filename}"
category: "{category}"
---

# {title}

{markdown.strip()}
"""

        out_dir.mkdir(parents=True, exist_ok=True)
        out_file.write_text(md_output, encoding="utf-8")

        time.sleep(DELAY)
        return path, True, "ok"

    except requests.exceptions.HTTPError as e:
        return path, False, f"HTTP {e.response.status_code}"
    except Exception as e:
        return path, False, str(e)


def main():
    print("=" * 60)
    print("EPLAN EEC Pro 2026 Documentation Scraper")
    print("=" * 60)

    # Step 1: Get all page entries from TOC chunks
    entries = fetch_all_entries()

    if not entries:
        print("No entries found! Exiting.")
        return

    # Save the index
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index_file = OUTPUT_DIR / "_index.json"
    with open(index_file, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print(f"Index saved to {index_file}")

    # Step 2: Download and convert all pages
    print(f"\nDownloading {len(entries)} pages with {MAX_WORKERS} workers...")
    print("-" * 60)

    success = 0
    failed = 0
    skipped = 0
    errors = []

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {
            executor.submit(download_and_convert, path, title): (path, title)
            for path, title in entries.items()
        }

        for i, future in enumerate(as_completed(futures), 1):
            path, ok, msg = future.result()
            if msg.startswith("skipped"):
                skipped += 1
            elif ok:
                success += 1
            else:
                failed += 1
                errors.append((path, msg))

            if i % 50 == 0 or i == len(entries):
                print(f"  Progress: {i}/{len(entries)} "
                      f"(ok={success}, skip={skipped}, fail={failed})")

    # Summary
    print("\n" + "=" * 60)
    print(f"DONE! Downloaded: {success}, Skipped: {skipped}, Failed: {failed}")
    print(f"Output directory: {OUTPUT_DIR.absolute()}")

    if errors:
        print(f"\nFailed pages ({len(errors)}):")
        for path, msg in errors[:20]:
            print(f"  {path}: {msg}")
        if len(errors) > 20:
            print(f"  ... and {len(errors) - 20} more")

        # Save error log
        with open(OUTPUT_DIR / "_errors.json", "w", encoding="utf-8") as f:
            json.dump(errors, f, indent=2)

    # Generate category summary
    categories = {}
    for path in entries:
        filename = Path(path).stem
        cat = filename.split("_")[0] if "_" in filename else "general"
        categories[cat] = categories.get(cat, 0) + 1

    print(f"\nCategories ({len(categories)}):")
    for cat, count in sorted(categories.items(), key=lambda x: -x[1]):
        print(f"  {cat}: {count} pages")


if __name__ == "__main__":
    main()
