# ExportParts(String,DataFormat,IEnumerable<MDPart>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabase~ExportParts(String,DataFormat,IEnumerable{MDPart}).html

---

Exports specified parts from the system's parts database.

Syntax

**C#**



public bool ExportParts( 

   string strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   IEnumerable<MDPart> parts

)

public:

bool ExportParts( 

   String^ strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   IEnumerable<MDPart^>^ parts

)


#### Parameters

*strFilePath*
:   Full output file name. This parameter must not be NULL and must not be an empty string ("").

*dataFormat*
:   Format type of export (XML or EDZ).

*parts*
:   List of parts to be exported. This parameter must not be NULL and must not be an empty list.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the strFilePath parameter is NULL or if the parts parameter is NULL. |
| [System.ArgumentException](#) | Thrown in the following cases:  1.) The strFilePath parameter is an empty string ("").  2.) The directory specified in the strFilePath parameter does not exist.  3.) The parts parameter is an empty list. |

Remarks

This method only exports the parts sepcified in the parts parameter.

To export all parts, use the ExportParts(String,DataFormat) method.

To export all parts and all other parts management items, use the ExportPartsDatabaseItems(String,DataFormat,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean) method.
