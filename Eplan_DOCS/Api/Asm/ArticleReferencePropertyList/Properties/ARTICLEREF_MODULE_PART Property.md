# ARTICLEREF_MODULE_PART Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLEREF_MODULE_PART().html

---

Part is included in a module # 20493.

Syntax

**C#**



public PropertyValue ARTICLEREF_MODULE_PART {get; set;}

public:

property PropertyValue^ ARTICLEREF_MODULE_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

This property is read-only..

Specifies whether the part is a module. Modules are parts (assemblies) with several devices. The module has its own part number. It can contain assemblies and other modules.
