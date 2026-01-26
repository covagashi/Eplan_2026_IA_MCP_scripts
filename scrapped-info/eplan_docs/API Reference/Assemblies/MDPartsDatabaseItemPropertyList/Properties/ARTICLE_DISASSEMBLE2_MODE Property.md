# ARTICLE_DISASSEMBLE2_MODE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DISASSEMBLE2_MODE().html

---

Break up in parts list # 22380.

Syntax

**C#**



public MDPropertyValue ARTICLE_DISASSEMBLE2_MODE {get; set;}

public:

property MDPropertyValue^ ARTICLE_DISASSEMBLE2_MODE {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Through this property the behavior during the breaking up of assemblies and modules in the parts list can be influenced.

0 = From settings

1 = Always break up

2 = Never break up
