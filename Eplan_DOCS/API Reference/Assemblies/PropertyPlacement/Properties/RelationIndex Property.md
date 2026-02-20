# RelationIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement~RelationIndex.html

---

Gets/Sets RelationIndex of PropertyPlacement.

Syntax

**C#**



public short RelationIndex {get; set;}

public:

property short RelationIndex {

   short get();

   void set (    short value);

}


#### Property Value

RelationIndex of Property placement.

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when property cannot be set/get. |
| [Eplan.EplApi.DataModel.ObjectNotCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectNotCreatedException.html) | Thrown when the PropertyPlacement object has not been initialized. |
| [Eplan.EplApi.DataModel.InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when the object handle that property value will be displayed is invalid. |

Remarks

RelationIndex is used when Relation property is set to RelationType associated with Articles (Article, MainFunctionArticle etc.). It allows to choose index of Article from which property will be displayed. RelationIndex corresponds to the Row number in Parts tab in Function Properties dialog in GUI. Setter does not check if the given RelationIndex value is valid for the object. If given value is not valid PropertyPlacement text will be empty.
