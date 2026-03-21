# ExportPartsDatabaseItems(String,DataFormat,IEnumerable<MDPartsDatabaseItem>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1521.html

---

Exports specified parts and other specified parts management items such as addresses, constructions, terminals, accessory lists and accessory placements from the system's parts database.

Syntax

**C#**



public bool ExportPartsDatabaseItems( 

   string strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   IEnumerable<MDPartsDatabaseItem> databaseItems

)

public:

bool ExportPartsDatabaseItems( 

   String^ strFilePath,

   MDPartsDatabase.DataFormat dataFormat,

   IEnumerable<MDPartsDatabaseItem^>^ databaseItems

)


#### Parameters

*strFilePath*
:   Full output file name. This parameter must not be NULL and must not be an empty string ("").

*dataFormat*
:   Format type of export (XML or EDZ).

*databaseItems*
:   List of parts (and other parts management items) to be exported. This parameter must not be NULL and must not be an empty list.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if the strFilePath parameter or if the databaseItems parameter is NULL. |
| [System.ArgumentException](#) | Thrown in the following cases:  1.) The strFilePath parameter is an empty string ("").  2.) The directory specified in the strFilePath parameter does not exist.  3.) The databaseItems parameter is an empty list. |

Remarks

This method only exports the parts (and other parts management items) sepcified in the databaseItems parameter.

To export all parts, use the ExportParts(String,DataFormat) method.

To export all parts and all other parts management items, use the ExportPartsDatabaseItems(String,DataFormat,Boolean,Boolean,Boolean,Boolean,Boolean,Boolean) method.
