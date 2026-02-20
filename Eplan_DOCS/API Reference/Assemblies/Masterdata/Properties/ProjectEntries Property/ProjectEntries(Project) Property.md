# ProjectEntries(Project) Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Masterdata~ProjectEntries(Project).html

---

Returns the file names of all master data stored in the project.

Syntax

**C#**



public StringCollection ProjectEntries( 

   Project oProject

) {get;}

public:

property StringCollection^ ProjectEntries {

   StringCollection^ get(Project^ oProject);

}


#### Parameters

*oProject*
:   Project.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown in case of missing arguments. |
| **ArgumentException** | Thrown, if the project is invalid. |
| **ApplicationException** | \Internal interface for master data could not be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Project master data files could not be returned correctly. |
