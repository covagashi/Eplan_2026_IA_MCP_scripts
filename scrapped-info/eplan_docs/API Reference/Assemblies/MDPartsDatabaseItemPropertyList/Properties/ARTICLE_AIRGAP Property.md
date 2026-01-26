# ARTICLE_AIRGAP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_AIRGAP().html

---

Plugs: Clearance # 22096.

Syntax

**C#**



public MDPropertyValue ARTICLE_AIRGAP {get; set;}

public:

property MDPropertyValue^ ARTICLE_AIRGAP {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. The clearance is defined as the shortest distance through the air between two conductive parts. For the calculation of minimum clearance, besides the rated surge voltage, the degree of pollution is also needed.
