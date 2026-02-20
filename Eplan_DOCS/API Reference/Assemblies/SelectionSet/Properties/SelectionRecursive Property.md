# SelectionRecursive Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~SelectionRecursive.html

---

Gets the complete selection on the active window. Property `LockProjectByDefault` should be set to `true` before any changes on any inside elements of obtained objects.

Syntax

**C#**



public StorableObject[] SelectionRecursive {get;}

public:

property array<StorableObject^>^ SelectionRecursive {

   array<StorableObject^>^ get();

}


#### Property Value

Array of objects casted to class [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html).

Remarks

When a node in tree view is selected, all nested elements will be returned .
