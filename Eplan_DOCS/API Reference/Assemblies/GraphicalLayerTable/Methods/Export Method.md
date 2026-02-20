# Export Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayerTable~Export.html

---

Exports the layers into an XML file.

Syntax

**C#**



public void Export( 

   string strExportFilePath

)

public:

void Export( 

   String^ strExportFilePath

)


#### Parameters

*strExportFilePath*
:   The name of the output file.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid \arguments. |
| [System.UnauthorizedAccessException](#) | No user rights to create files on the \file system. |
| [System.ApplicationException](#) | The internal interface for layers export could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Errors occurred during export. See the exception message for details. |
