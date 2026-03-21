# ExportParts(String,DataFormat) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportParts(String,DataFormat).html

---

Exports all parts from the system's parts database.

Syntax

**C#**



public bool ExportParts( 

   string strFilePath,

   MDPartsDatabase.DataFormat dataFormat

)

public:

bool ExportParts( 

   String^ strFilePath,

   MDPartsDatabase.DataFormat dataFormat

)


#### Parameters

*strFilePath*
:   Full output file name. This parameter must not be NULL and must not be an empty string ("").

*dataFormat*
:   Format type of export (XML or EDZ).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the strFilePath parameter is NULL. |
| [System.ArgumentException](#) | Thrown if the strFilePath parameter is an empty string ("") or if the directory specified in the strFilePath parameter does not exist. |

Remarks

Exports parts only. Does not export other parts management items like addresses, constructions, terminals, accessory lists and accessory placements.

To export all parts and all other parts management items, use the ExportPartsDatabaseItems(String,DataFormat,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean) method.
