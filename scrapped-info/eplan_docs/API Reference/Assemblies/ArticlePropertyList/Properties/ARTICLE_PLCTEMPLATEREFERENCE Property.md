# ARTICLE_PLCTEMPLATEREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCTEMPLATEREFERENCE().html

---

PLC device: TemplateIdentifier # 22338.

Syntax

**C#**



public PropertyValue ARTICLE_PLCTEMPLATEREFERENCE {get; set;}

public:

property PropertyValue^ ARTICLE_PLCTEMPLATEREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of a template that is used for the exchange of a device in the PLC configuration program with preset, user-defined part properties. The property is used during the PLC data exchange in AutomationML AR APC format. The name of this template is replaced, but not the contents.
