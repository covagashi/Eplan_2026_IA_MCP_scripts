# ToInt Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Relation~ToInt.html

---

Relation-Id - identifies which type of navigation will be done.

Syntax

**C#**



public ushort ToInt()

public:

ushort ToInt();


#### Return Value

Id of navigation type.

Remarks

Possible ids are defined in internal file and they are starting with number 20000. Not every relation is possible for every object. The helper class which could get corresponding DataModel object from relation, is not implemented yet.
