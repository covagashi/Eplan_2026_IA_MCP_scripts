# FUNC_ARTICLE_PLCAXIS_DEVICETYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_PLCAXIS_DEVICETYPE().html

---

Drive: Device type # 20577.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PLCAXIS_DEVICETYPE {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PLCAXIS_DEVICETYPE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

For devices that are assigned to a drive you specify the type of device, for example "Synchronous motor", "Converter", "Encoder", etc., more exactly. The values to be entered for the device type are usually specified by the device manufacturer. During a part selection or device selection the property is filled with the corresponding value from the parts management.
