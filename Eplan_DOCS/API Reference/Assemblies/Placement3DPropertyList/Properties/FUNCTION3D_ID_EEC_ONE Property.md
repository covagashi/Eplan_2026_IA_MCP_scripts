# FUNCTION3D_ID_EEC_ONE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_ID_EEC_ONE().html

---

Variable for placeable functions (EEC One) # 36041.

Syntax

**C#**



public PropertyValue FUNCTION3D_ID_EEC_ONE {get; set;}

public:

property PropertyValue^ FUNCTION3D_ID_EEC_ONE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The property serves to identify 3D part placements in EEC One, so that specific other 3D part placements can be placed automatically on them during the automatic generation of a layout space.
