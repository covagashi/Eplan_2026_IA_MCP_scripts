# ARTICLE_DISASSEMBLE4_MODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DISASSEMBLE4_MODE().html

---

Break up in parts list (manufacturing data) # 22418.

Syntax

**C#**



public MDPropertyValue ARTICLE_DISASSEMBLE4_MODE {get; set;}

public:

property MDPropertyValue^ ARTICLE_DISASSEMBLE4_MODE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Through this property the behavior during the breaking up of assemblies and modules in the parts list (manufacturing data export) can be influenced.

0 = From settings

1 = Always break up

2 = Never break up
