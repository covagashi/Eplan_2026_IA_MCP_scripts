# Import Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Import.html

---

Imports layers from an XML file.

Syntax

**C#**



public void Import( 

   string strImportFilePath

)

public:

void Import( 

   String^ strImportFilePath

)


#### Parameters

*strImportFilePath*
:   The name of the input file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid \arguments. |
| [System.ApplicationException](#) | The internal interface for layers import could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during import. See the exception message for details. |
