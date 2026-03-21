# StorableObjects Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragment~StorableObjects.html

---

Returns all objects contained in the OptionFragment.

Syntax

**C#**



public StorableObject[] StorableObjects {get; set;}

public:

property array<StorableObject^>^ StorableObjects {

   array<StorableObject^>^ get();

   void set (    array<StorableObject^>^ value);

}


#### Property Value

[StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html).

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown while setting when collection contains objects from more then one project. |

Remarks

All sub placements from each group which will be assign to this option fragment will be also assign to it.
