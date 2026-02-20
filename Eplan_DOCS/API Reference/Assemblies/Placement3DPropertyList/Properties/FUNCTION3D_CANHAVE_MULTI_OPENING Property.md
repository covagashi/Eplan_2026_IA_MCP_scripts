# FUNCTION3D_CANHAVE_MULTI_OPENING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_CANHAVE_MULTI_OPENING().html

---

Multiple cut-out possible # 36036.

Syntax

**C#**



public PropertyValue FUNCTION3D_CANHAVE_MULTI_OPENING {get; set;}

public:

property PropertyValue^ FUNCTION3D_CANHAVE_MULTI_OPENING {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Indicates whether multiple cut-outs are possible for an item, and allows for the "inheriting" of cut-outs. This way, cut-outs can be carried over from a drilling pattern to another item.
