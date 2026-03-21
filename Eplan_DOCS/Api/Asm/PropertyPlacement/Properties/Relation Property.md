# Relation Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~Relation.html

---

Gets/Sets Relation of PropertyPlacement.

Syntax

**C#**



public PropertyPlacement.RelationType Relation {get; set;}

public:

property PropertyPlacement.RelationType Relation {

   PropertyPlacement.RelationType get();

   void set (    PropertyPlacement.RelationType value);

}


#### Property Value

RelationType of PropertyPlacement.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when property cannot be set/get. |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when the PropertyPlacement object has not been initialized. |
| [Eplan.EplApi.DataModel.InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when the object handle that property value will be displayed is invalid. |

Remarks

Relation allows to select the source object for a PropertyPlacement. List of possible source objects is declared in RelationType enum. Property corresponds to the Source object field in Dialog Property selection in GUI. Setter does not check if the given RelationType value is valid for the object. If given value is not valid PropertyPlacement text will be empty.
