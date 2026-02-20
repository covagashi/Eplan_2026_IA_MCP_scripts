# ARTICLE_PLCDEVICE_INDEX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCDEVICE_INDEX().html

---

Device description: Index in file # 22283.

Syntax

**C#**



public PropertyValue ARTICLE_PLCDEVICE_INDEX {get; set;}

public:

property PropertyValue^ ARTICLE_PLCDEVICE_INDEX {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Index in the device description file of a PLC card. Through the index it is possible to select a device in a language-neutral form within such a file. The property is transferred to the main function at a part selection or device selection. The property is taken into consideration during the PLC data exchange in AutomationML AR APC format.
