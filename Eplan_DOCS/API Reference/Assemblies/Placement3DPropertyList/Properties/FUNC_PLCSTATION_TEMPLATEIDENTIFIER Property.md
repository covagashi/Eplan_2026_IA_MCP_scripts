# FUNC_PLCSTATION_TEMPLATEIDENTIFIER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_PLCSTATION_TEMPLATEIDENTIFIER().html

---

PLC station: TemplateIdentifier # 20614.

Syntax

**C#**



public PropertyValue FUNC_PLCSTATION_TEMPLATEIDENTIFIER {get; set;}

public:

property PropertyValue^ FUNC_PLCSTATION_TEMPLATEIDENTIFIER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of a workstation-specific template that is used for the exchange of devices with user-defined part properties preset in the PLC configuration program. The property is used during the PLC data exchange in AutomationML AR APC format. The name of this template is replaced, but not the contents. The property should be filled in within the corresponding workstation at each PLC box that represents a CPU or a head station.
