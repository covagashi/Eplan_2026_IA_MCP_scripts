# ChangeLocationName Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project~ChangeLocationName.html

---

Changes name of the given location. After that change a location object becomes invalid, to get this object once again, use the GetLocationObjects function.

Syntax

**C#**



public Location ChangeLocationName( 

   Location oLocation,

   string strName

)

public:

Location^ ChangeLocationName( 

   Location^ oLocation,

   String^ strName

)


#### Parameters

*oLocation*
:   Location object.

*strName*
:   New name of a location.

#### Return Value

[Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location.html) object.

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when a location is not created. |
| [IncorrectNameFormatException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IncorrectNameFormatException.html) | Thrown when a location name contains special '.' character. |

Remarks

The project must be opened in exclusive mode.
