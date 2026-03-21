# StoreToObject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~StoreToObject.html

---

Stores changes into a project database.

Syntax

**C#**



public bool StoreToObject()

public:

bool StoreToObject();


#### Return Value

false : cannot store mate

true : all properties should be stored into parent Function3D

Remarks

Please mind that a Mate is an offline object, i.e. changes are not stored automatically into a project. In order to store them into Placement3D, please call StoreToObject at the end. Please check IsReadOnly property at first to make sure that a Mate could be changed.
