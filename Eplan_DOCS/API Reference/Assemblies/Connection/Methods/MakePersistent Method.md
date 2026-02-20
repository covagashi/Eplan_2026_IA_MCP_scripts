# MakePersistent Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Connection~MakePersistent.html

---

Allows to create non-placed connection from a connection template. In effect connection template becomes covered template.

Syntax

**C#**



public void MakePersistent()

public:

void MakePersistent();


Exceptions

| Exception | Description |
| --- | --- |
| [InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when internally used handle is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an internal error occured. Please refer to the error message. |
