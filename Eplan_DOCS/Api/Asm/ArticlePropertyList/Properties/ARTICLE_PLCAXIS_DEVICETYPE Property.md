# ARTICLE_PLCAXIS_DEVICETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCAXIS_DEVICETYPE().html

---

Drive: Device type # 22340.

Syntax

**C#**



public PropertyValue ARTICLE_PLCAXIS_DEVICETYPE {get; set;}

public:

property PropertyValue^ ARTICLE_PLCAXIS_DEVICETYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

For devices that are assigned to a drive you specify the type of device, for example "Synchronous motor", "Converter", "Encoder", etc., more exactly. The values to be entered for the device type are usually specified by the device manufacturer.
