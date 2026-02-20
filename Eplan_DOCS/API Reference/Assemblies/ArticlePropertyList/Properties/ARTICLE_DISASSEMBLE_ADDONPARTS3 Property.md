# ARTICLE_DISASSEMBLE_ADDONPARTS3 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS3().html

---

Include supplemental parts (summarized parts list / manufacturing data) # 22419.

Syntax

**C#**



public PropertyValue ARTICLE_DISASSEMBLE_ADDONPARTS3 {get; set;}

public:

property PropertyValue^ ARTICLE_DISASSEMBLE_ADDONPARTS3 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Indicates whether supplemental parts are to be included when assemblies or modules are broken up.

0 = From settings

1 = Yes

2 = No
