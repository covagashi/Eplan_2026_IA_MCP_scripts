# ExportPartsDatabaseItems(String,DataFormat,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1522.html

---

Exports parts and other parts management items such as addresses, constructions, terminals, accessory lists and accessory placements from the system's parts database.

Syntax

**C#**



public bool ExportPartsDatabaseItems( 

   string strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   bool bIncludeParts,

   bool bIncludeAddresses,

   bool bIncludeConstructions,

   bool bIncludeTerminals,

   bool bIncludeAccessoryLists,

   bool bIncludeAccessoryPlacements

)

public:

bool ExportPartsDatabaseItems( 

   String^ strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   bool bIncludeParts,

   bool bIncludeAddresses,

   bool bIncludeConstructions,

   bool bIncludeTerminals,

   bool bIncludeAccessoryLists,

   bool bIncludeAccessoryPlacements

)


#### Parameters

*strFilePath*
:   Full output file name. This parameter must not be NULL and must not be an empty string ("").

*dataFormat*
:   Format type of export (XML or EDZ).

*bIncludeParts*
:   Include parts.

*bIncludeAddresses*
:   Include manufacturers and customers.

*bIncludeConstructions*
:   Include drilling patterns.

*bIncludeTerminals*
:   Include connection point patterns.

*bIncludeAccessoryLists*
:   Include accessory lists.

*bIncludeAccessoryPlacements*
:   Include accessory placements.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the strFilePath parameter is NULL. |
| [System.ArgumentException](#) | Thrown if the strFilePath parameter is an empty string ("") or if the directory specified in the strFilePath parameter does not exist. |

Remarks

All items of the included parts management item types are exported.
