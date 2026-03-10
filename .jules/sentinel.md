## 2026-03-10 - C# Code Injection in Dynamically Generated Scripts
**Vulnerability:** Arbitrary C# Code Execution via unescaped string interpolation.
**Learning:** When generating C# scripts dynamically using Python f-strings, direct string interpolation allows attackers to break out of string literals or inject arbitrary commands into unquoted identifier contexts.
**Prevention:** Use `json.dumps()` to safely encode C# string literals, and strictly validate any C# identifiers (e.g., property names) against a regex like `^[a-zA-Z_][a-zA-Z0-9_]*$` before interpolation.
