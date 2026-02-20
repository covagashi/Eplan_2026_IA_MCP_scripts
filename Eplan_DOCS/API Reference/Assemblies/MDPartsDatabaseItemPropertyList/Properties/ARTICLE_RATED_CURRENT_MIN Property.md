# ARTICLE_RATED_CURRENT_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsDatabaseItemPropertyList~ARTICLE_RATED_CURRENT_MIN().html

---

Nominal current, min. # 26502.

Syntax

**C#**



public MDPropertyValue ARTICLE_RATED_CURRENT_MIN {get; set;}

public:

property MDPropertyValue^ ARTICLE_RATED_CURRENT_MIN {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Minimum value of the current that an electrical device or a component requires to function properly. For example, sensors often require a minimum current in order to carry out precise measurements.
