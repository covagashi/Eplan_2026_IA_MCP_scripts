# Selection Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~Selection.html

---

Gets the complete selection on the active window. Property `LockProjectByDefault` should be set to `true` before any changes on any inside elements of obtained objects.

Syntax

**C#**



public StorableObject[] Selection {get;}

public:

property array<StorableObject^>^ Selection {

   array<StorableObject^>^ get();

}


#### Property Value

Array of selected objects casted to class [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html).

Remarks

When a node is selected, this is only the first element. The property can work only within one project.
