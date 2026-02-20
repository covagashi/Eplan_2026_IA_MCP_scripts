# FUNC_PLCPLUG_DESIGNATION_MANUAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCPLUG_DESIGNATION_MANUAL().html

---

Plug designation # 20406.

Syntax

**C#**



public PropertyValue FUNC_PLCPLUG_DESIGNATION_MANUAL {get; set;}

public:

property PropertyValue^ FUNC_PLCPLUG_DESIGNATION_MANUAL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The designation of the plug is connected to the PLC connection point / channel or device connection point. The plug designation can be transferred from the left (or above), as with terminals and supports the identification of PLC connection points or device connection points.
