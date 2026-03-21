# ARTICLE_PLCAXIS_DEVICETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCAXIS_DEVICETYPE().html

---

Drive: Device type # 22340.

Syntax

**C#**



public MDPropertyValue ARTICLE_PLCAXIS_DEVICETYPE {get; set;}

public:

property MDPropertyValue^ ARTICLE_PLCAXIS_DEVICETYPE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

For devices that are assigned to a drive you specify the type of device, for example "Synchronous motor", "Converter", "Encoder", etc., more exactly. The values to be entered for the device type are usually specified by the device manufacturer.
