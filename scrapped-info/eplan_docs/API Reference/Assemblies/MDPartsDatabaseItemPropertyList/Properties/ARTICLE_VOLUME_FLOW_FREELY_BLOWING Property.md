# ARTICLE_VOLUME_FLOW_FREELY_BLOWING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_VOLUME_FLOW_FREELY_BLOWING().html

---

Flow rate (free blowing) # 26175.

Syntax

**C#**



public MDPropertyValue ARTICLE_VOLUME_FLOW_FREELY_BLOWING {get; set;}

public:

property MDPropertyValue^ ARTICLE_VOLUME_FLOW_FREELY_BLOWING {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Flow rate of a ventilation device or fan if it is operated without connected piping or resistances. This means that the flow rate is measured under ideal conditions at which no additional pressure losses occur through piping or other impairments.
