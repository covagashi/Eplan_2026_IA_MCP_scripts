# Parent Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Parent.html

---

Gets or Sets parent placement. Caution: The Change of the parent will also change the absolute position because Placement3D stores the position relative to his parent

Syntax

**C#**



public virtual Placement3D Parent {get; set;}

public:

virtual property Placement3D^ Parent {

   Placement3D^ get();

   void set (    Placement3D^ value);

}

