# Parent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.BusBar~Parent.html

---

Gets or Sets parent placement. Caution: The Change of the parent will also change the absolute position because Placement3D stores the position relative to his parent

Syntax

**C#**



public override Placement3D Parent {set;}

public:

property Placement3D^ Parent {

   void set (    Placement3D^ value) override;

}

