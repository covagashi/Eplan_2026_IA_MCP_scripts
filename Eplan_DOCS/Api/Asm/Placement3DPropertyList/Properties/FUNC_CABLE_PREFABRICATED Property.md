# FUNC_CABLE_PREFABRICATED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_CABLE_PREFABRICATED().html

---

Use connected devices as source and target # 20621.

Syntax

**C#**



public PropertyValue FUNC_CABLE_PREFABRICATED {get; set;}

public:

property PropertyValue^ FUNC_CABLE_PREFABRICATED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

If this property is activated, pins are skipped when determining the source and target of the cable or shield and instead the devices connected to the cable / shield are displayed as the source and target. This property only affects the display in the editing dialogs for cables, terminals, and plugs and the display in the reports. The cables and connections themselves are not changed. If the property is deactivated, the pins are output as the source and target of the cable or shield.
