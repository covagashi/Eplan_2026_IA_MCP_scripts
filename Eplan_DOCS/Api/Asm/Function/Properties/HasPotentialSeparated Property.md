# HasPotentialSeparated Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function~HasPotentialSeparated.html

---

Gets/Sets, if the function separates potentials.

Syntax

**C#**



public bool HasPotentialSeparated {get; set;}

public:

property bool HasPotentialSeparated {

   bool get();

   void set (    bool value);

}


#### Property Value

true : Function separates potentials

false : Function does not separate potentials

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when the information cannot be retrieved from data model. |
| [DataModelException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DataModelException.html) | Thrown when the property cannot be set. |

Remarks

Property can be set only for Functions having Pins. For example ConnectionDefinitionPoint is excluded.
