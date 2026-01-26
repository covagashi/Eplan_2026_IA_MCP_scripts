# PartToProject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Synchronize~PartToProject.html

---

Synchronizes the specified parts inside the project with the parts in the parts master database. Updates parts inside project. Parts in the database are not changed. This method corresponds with the EPLAN functionality in the ribbon "Master data \> Parts \> Synchronize" for selected parts.

Syntax

**C#**



public void PartToProject( 

   Project oProject,

   ArrayList lParts

)

public:

void PartToProject( 

   Project^ oProject,

   ArrayList^ lParts

)


#### Parameters

*oProject*
:   Project for which the parts will be updated.

*lParts*
:   List of parts which will be updated.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentNullException** | Thrown if null was passed as an argument. |
| **ArgumentException** | Thrown in case of invalid arguments, e.g. the project is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | The synchronization finished with errors. |
