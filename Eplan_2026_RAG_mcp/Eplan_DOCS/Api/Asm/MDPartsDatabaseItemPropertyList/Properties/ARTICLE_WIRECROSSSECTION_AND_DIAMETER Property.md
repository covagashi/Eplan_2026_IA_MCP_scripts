# ARTICLE_WIRECROSSSECTION_AND_DIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1720.html

---

No. of connections and cross-section / diameter # 22069.

Syntax

**C#**



public MDPropertyValue ARTICLE_WIRECROSSSECTION_AND_DIAMETER {get; set;}

public:

property MDPropertyValue^ ARTICLE_WIRECROSSSECTION_AND_DIAMETER {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Displays the number of connections multiplied by the cross-section (or diameter), separated by "x". For pipes and hoses in fluid power and process engineering the property refers to the inner diameter.
