# ARTICLE_PLCTEMPLATEREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_PLCTEMPLATEREFERENCE().html

---

PLC device: TemplateIdentifier # 22338.

Syntax

**C#**



public MDPropertyValue ARTICLE_PLCTEMPLATEREFERENCE {get; set;}

public:

property MDPropertyValue^ ARTICLE_PLCTEMPLATEREFERENCE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of a template that is used for the exchange of a device in the PLC configuration program with preset, user-defined part properties. The property is used during the PLC data exchange in AutomationML AR APC format. The name of this template is replaced, but not the contents.
