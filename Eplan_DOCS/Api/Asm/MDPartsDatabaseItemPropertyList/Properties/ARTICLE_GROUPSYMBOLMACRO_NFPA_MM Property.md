# ARTICLE_GROUPSYMBOLMACRO_NFPA_MM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_GROUPSYMBOLMACRO_NFPA_MM().html

---

Schematic macro: NFPA mm # 22871.

Syntax

**C#**



public MDPropertyValue ARTICLE_GROUPSYMBOLMACRO_NFPA_MM {get; set;}

public:

property MDPropertyValue^ ARTICLE_GROUPSYMBOLMACRO_NFPA_MM {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

2D macro that is placed preferentially on schematic pages if the "NFPA mm" standard is specified as the preferred standard in the project settings. This macro is only used if no company standard is specified in the project settings or if no corresponding schematic macro for the company standard is stored at the part.
