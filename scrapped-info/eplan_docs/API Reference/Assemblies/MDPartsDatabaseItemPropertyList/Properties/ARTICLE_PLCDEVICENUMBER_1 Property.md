# ARTICLE_PLCDEVICENUMBER_1 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCDEVICENUMBER_1().html

---

PLC subdevice 1: Position (slot / module) # 22305.

Syntax

**C#**



public MDPropertyValue ARTICLE_PLCDEVICENUMBER_1 {get; set;}

public:

property MDPropertyValue^ ARTICLE_PLCDEVICENUMBER_1 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. In this property you specify in which slot / at which position on the PLC card this PLC subdevice is located. PLC devices exist that consist of several integrated modules and that have several start addresses. Such a device can consist, for example, of an internal CPU module, an internal input-output module as well as internal counter module - however with only one part number. Such integrated modules within a PLC device can be displayed in Eplan with PLC subdevices. To this purpose up to twelve PLC subdevices are available.
