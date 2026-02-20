# ImportPropertyPlacementsSchemas Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ProjectManagement~ImportPropertyPlacementsSchemas.html

---

Imports property placements schemes.

Syntax

**C#**



public Tuple<string,string>[] ImportPropertyPlacementsSchemas( 

   Project oProject,

   string strFileName,

   bool bOverwrite

)

public:

array<Tuple<String^,String^>^>^ ImportPropertyPlacementsSchemas( 

   Project^ oProject,

   String^ strFileName,

   bool bOverwrite

)


#### Parameters

*oProject*
:   Project to which property placements schemes will be imported.

*strFileName*
:   Full name of input file.

*bOverwrite*
:   If the imported property placement scheme already exists, this parameter specifies whether it should be overwritten.

#### Return Value

Returns an array of tuples where the first item is the name of the imported property placement scheme and the second item is the symbol name to which this imported scheme is assigned.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown in case if invalid arguments, e.g. an invalid project is set. |
| **ApplicationException** | Thrown, if the \internal action could no be found. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown if an error occurs while executing the method. |
