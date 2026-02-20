# FUNC_PLCCHANNEL_DESIGNATION_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCCHANNEL_DESIGNATION_MANUAL().html

---

Channel designation # 20407.

Syntax

**C#**



public PropertyValue FUNC_PLCCHANNEL_DESIGNATION_MANUAL {get; set;}

public:

property PropertyValue^ FUNC_PLCCHANNEL_DESIGNATION_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

PLC channel designation for PLC connection points and channels. The channel designation can be manually or automatically assigned. A channel must be unique within a PLC card. For power supply connection points, the assignment is usually graphical.
