# ARTICLE_GROUPNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_GROUPNUMBER().html

---

Group number # 22044.

Syntax

**C#**



public MDPropertyValue ARTICLE_GROUPNUMBER {get; set;}

public:

property MDPropertyValue^ ARTICLE_GROUPNUMBER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Outputs the group number entered in parts management on the "Properties" tab > hierarchy level "Data". The group number is used to differentiate between individual parts groups.
