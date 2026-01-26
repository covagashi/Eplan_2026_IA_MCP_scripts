# Create(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Topology.Segment~Create(Project).html

---

Creates new unplaced segment.

Syntax

**C#**



public void Create( 

   Project pProject

)

public:

void Create( 

   Project^ pProject

)


#### Parameters

*pProject*
:   Project to which this object will be assigned. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when parameter is `null`. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when the `Segment` cannot be created. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when internal error has occured. Please see the exception message for details. |
