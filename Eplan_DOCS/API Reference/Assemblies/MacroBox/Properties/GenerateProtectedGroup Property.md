# GenerateProtectedGroup Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~GenerateProtectedGroup.html

---

Gets or sets generate protected group property.

Syntax

**C#**



public bool GenerateProtectedGroup {get; set;}

public:

property bool GenerateProtectedGroup {

   bool get();

   void set (    bool value);

}


Remarks

Property determines if protected group should be generated during insertion of macro. When set to true macro cannot be changed graphically.
