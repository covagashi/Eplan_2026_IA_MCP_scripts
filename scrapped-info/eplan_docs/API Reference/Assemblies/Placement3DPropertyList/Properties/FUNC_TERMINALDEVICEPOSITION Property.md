# FUNC_TERMINALDEVICEPOSITION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_TERMINALDEVICEPOSITION().html

---

Terminal: Device position # 20367.

Syntax

**C#**



public PropertyValue FUNC_TERMINALDEVICEPOSITION {get; set;}

public:

property PropertyValue^ FUNC_TERMINALDEVICEPOSITION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The device position specifies the position of the terminal device to which the terminal belongs within the terminal strip. All the terminals of a terminal device have the same device position. The sort code also specifies the order of the terminals within a terminal device.
