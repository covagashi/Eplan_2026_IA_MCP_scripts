# isPrinted Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer~isPrinted.html

---

Specifies, if the layer is printed

Syntax

**C#**



public bool isPrinted {get; set;}

public:

property bool isPrinted {

   bool get();

   void set (    bool value);

}


Remarks

GraphicalLayerTable::Reload() has to be called after isPrinted is changed to take effect without closing and reopening the project.
