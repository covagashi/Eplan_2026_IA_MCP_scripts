# XEGActionInsertSymRef

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XEGActionInsertSymRef.html

---

```
 Standard action to find symbol references for inserting.

```

| Parameter | Description |
| --- | --- |
| ``` SymbolLibName
 ``` | ``` Name of the symbol library where the symbol is to find
 ``` |
| ``` SymbolId
 ``` | ``` Number of the symbol that should be inserted
 ``` |
| ``` VariantId
 ``` | ``` Number of the variant, if the symbol has one
 ``` |
| ``` FctDefTag
 ``` | ``` Identifier of the function definition tag to search the symbol that should be inserted
 ``` |
| ``` Placementmode
 ``` | ``` Identifier of placement mode to search the symbol that should be inserted.
  String which defines the placement type of the symbol.
  The placement mode depends on the DocumentType
 ``` |
| ``` SymbolType
 ``` | ``` Identifier of symbol type to search the symbol that should be inserted
 ``` |
| ``` CustomSymbols
 ``` | ``` This parameter should be used if a user-created symbol should be inserted.
  The parameter is the name of the setting which contains the identifiers of the custom symbol.
  If this parameter is NOT empty, the custom symbol is used and not the symbol referenced by "SymbolLibName", "SymbolId", "VariantId".
  The setting itself must contain these values and look like this:
  XSbGui.CustomSymbols.CustomSymbols.lib
  XSbGui.CustomSymbols.CustomSymbols.id
  XSbGui.CustomSymbols.CustomSymbols.var
 ``` |

**Remarks**

```
 This action only works correctly when the GUI is initialized. If the symbol is not found, a window with symbols is opened.

 Can be used with all types of symbol variants, function definition tags, symbol data and symbol references.

 The action can be used only interactively.

Used specialized calling context: DMBaseHandleContext

```

**Example**

```
 XEGActionInsertSymRef  /SymbolLibName:IEC_symbol /SymbolId:55 /VariantId:0

```