# ARTICLE_DISASSEMBLE_ADDONPARTS4 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_DISASSEMBLE_ADDONPARTS4().html

---

Include supplemental parts (parts list / manufacturing data) # 22420.

Syntax

**C#**



public MDPropertyValue ARTICLE_DISASSEMBLE_ADDONPARTS4 {get; set;}

public:

property MDPropertyValue^ ARTICLE_DISASSEMBLE_ADDONPARTS4 {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Indicates whether supplemental parts are to be included when assemblies or modules are broken up.

0 = From settings

1 = Yes

2 = No
