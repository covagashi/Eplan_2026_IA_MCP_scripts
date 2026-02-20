# ARTICLE_CABLELENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_CABLELENGTH().html

---

Length (prefabricated) # 22055.

Syntax

**C#**



public MDPropertyValue ARTICLE_CABLELENGTH {get; set;}

public:

property MDPropertyValue^ ARTICLE_CABLELENGTH {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Double.

Remarks

Property of a part variant. Length of cables, bundles, pipes, tubes and wires is stored internally in the unit "meter" and is converted to the unit selected for the display. What is meant here is the "unchangeable" length with which a part is to be used, not the delivery length.
