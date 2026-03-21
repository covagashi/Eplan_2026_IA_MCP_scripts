# FUNCTION3D_CABINET_TOTALWEIGHT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION3D_CABINET_TOTALWEIGHT().html

---

Total weight # 36108.

Syntax

**C#**



public PropertyValue FUNCTION3D_CABINET_TOTALWEIGHT {get; set;}

public:

property PropertyValue^ FUNCTION3D_CABINET_TOTALWEIGHT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property displays the result of the calculation of the total weight of an enclosure placed in the layout space. The actual total weight of an enclosure is calculated from the enclosure weight and the sum of the weights of all parts and routed connections placed in the enclosure.
