# ARTICLE_DISASSEMBLE_MODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_DISASSEMBLE_MODE().html

---

Break up in summarized parts list # 22292.

Syntax

**C#**



public PropertyValue ARTICLE_DISASSEMBLE_MODE {get; set;}

public:

property PropertyValue^ ARTICLE_DISASSEMBLE_MODE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Through this property the behavior during the breaking up of assemblies and modules in the summarized parts list is influences.

0 = From settings

1 = Always break up

2 = Never break up
