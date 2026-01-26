# FUNC_ARTICLE_PLCTEMPLATEREFERENCE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_ARTICLE_PLCTEMPLATEREFERENCE().html

---

PLC device: TemplateIdentifier # 20580.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_PLCTEMPLATEREFERENCE {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_PLCTEMPLATEREFERENCE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of a template that is used for the exchange of a device in the PLC configuration program with preset, user-defined part properties. The property is used during the PLC data exchange in AutomationML AR APC format. The name of this template is replaced, but not the contents. During a part selection or device selection the property is filled with the corresponding value from the parts management.
