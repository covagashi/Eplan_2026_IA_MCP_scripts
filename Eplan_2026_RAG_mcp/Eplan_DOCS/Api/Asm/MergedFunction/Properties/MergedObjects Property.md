# MergedObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedFunction~MergedObjects.html

---

Returns an array of [StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)s covered by this merged function.

Syntax

**C#**



public StorableObject[] MergedObjects {get;}

public:

property array<StorableObject^>^ MergedObjects {

   array<StorableObject^>^ get();

}


#### Property Value

An array of objects covered by this merged function

Exceptions

| Exception | Description |
| --- | --- |
| [ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object wasn't created. |
