# API Data Access (Parts Database, Properties)

Some `Eplan.EplApi.*` API namespaces work directly inside scripts (no separate add-in needed): notably `Eplan.EplApi.MasterData` for the parts database. Full project object-model work (placements, functions, connections via `Eplan.EplApi.DataModel`) requires an API license and usually a proper API project — verify signatures against the RAG.

## Parts database (`MDPartsManagement`)

```csharp
using Eplan.EplApi.MasterData;

MDPartsManagement pm = new MDPartsManagement();
MDPartsDatabase database = pm.OpenDatabase();   // currently configured parts DB
if (database == null) throw new Exception("Could not open parts database");

foreach (MDPart part in database.Parts)
{
    if (part == null || string.IsNullOrEmpty(part.PartNr)) continue;
    // part.PartNr, part.Variant, part.Properties...
}
```

## Part properties

Access via `part.Properties.<PROPERTY_NAME>`. Values are `MDPropertyValue`: check `IsEmpty` before converting.

```csharp
string manufacturer = part.Properties.ARTICLE_MANUFACTURER_NAME.IsEmpty
    ? "" : part.Properties.ARTICLE_MANUFACTURER_NAME.ToString();
string erp = part.Properties.ARTICLE_ERPNR.IsEmpty
    ? "" : part.Properties.ARTICLE_ERPNR.ToString();
bool hasCE = !part.Properties.ARTICLE_CERTIFICATE_CE.IsEmpty
    && part.Properties.ARTICLE_CERTIFICATE_CE.ToBool();
string ul = part.Properties.ARTICLE_CERTIFICATE_UL.IsEmpty
    ? "" : part.Properties.ARTICLE_CERTIFICATE_UL.ToString();
```

Useful article properties:
- `ARTICLE_DESCR1/2/3` — descriptions (multilang; parse with the multilang parser in core-classes.md)
- `ARTICLE_MANUFACTURER_NAME`, `ARTICLE_ERPNR`
- `ARTICLE_CERTIFICATE_CE` (bool), `ARTICLE_CERTIFICATE_UL`
- `ARTICLE_EXTERNAL_DOCUMENT_1` … `ARTICLE_EXTERNAL_DOCUMENT_20` — legacy doc links
- `ARTICLE_EXTERNAL_DOCUMENT_URL[i]` / `ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION[i]` — indexed doc links (newer)

### Indexed vs legacy external documents (fallback pattern)
Newer databases use the indexed `ARTICLE_EXTERNAL_DOCUMENT_URL[i]` properties; older ones the numbered `ARTICLE_EXTERNAL_DOCUMENT_n`. Robust code reads the indexed property and falls back to the numbered one when empty:

```csharp
for (int i = 1; i <= 20; i++)
{
    var pUrl = part.Properties.ARTICLE_EXTERNAL_DOCUMENT_URL[i];
    var pDesg = part.Properties.ARTICLE_EXTERNAL_DOCUMENT_DESIGNATION[i];
    if (pUrl.IsEmpty)
    {
        // fall back to ARTICLE_EXTERNAL_DOCUMENT_1 .. _20 by index
        switch (i)
        {
            case 1: pUrl = part.Properties.ARTICLE_EXTERNAL_DOCUMENT_1; break;
            case 2: pUrl = part.Properties.ARTICLE_EXTERNAL_DOCUMENT_2; break;
            // ... up to 20
        }
    }
    // document paths often contain $(MD_DOCUMENTS) -> resolve with PathMap.SubstitutePath
}
```

## User-defined properties on parts

User-defined properties live on the part as `UserDefinedPropertyPositions`; each position has `IdentifyingName` (e.g. `"MYCOMPANY.P001"`) and `Value` (multilang string):

```csharp
foreach (var pos in part.UserDefinedPropertyPositions)
{
    if (pos == null) continue;
    string ident = pos.IdentifyingName ?? "";
    if (ident.Equals("MYCOMPANY.P001", StringComparison.OrdinalIgnoreCase))
    {
        var v = pos.Value;
        if (v != null) myValue = ParseMultiLang(v.ToString());
    }
}
```

## Practical notes

- Wrap per-part processing in try/catch and continue the loop — a single corrupt part must not abort a full DB scan; log the part number.
- Materialize `database.Parts` into a `List<MDPart>` first if you need a count for a progress bar.
- Document paths from the parts DB frequently contain PathMap variables (`$(MD_DOCUMENTS)\...`) — always resolve with `PathMap.SubstitutePath` before using as a filesystem path, and skip `http(s)://` URLs when expecting files.
- Report progress/results with `new BaseException(msg, MessageLevel.Message).FixMessage()` so runs are traceable in EPLAN's message list.
- For project data (pages, devices, functions): prefer **actions** from scripts (`selectionset`, `edit`, property actions — see actions-reference.md). Reserve `Eplan.EplApi.DataModel` for licensed API projects, and check exact class/method names in the RAG before writing code.
