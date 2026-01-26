# ARTICLE_WIRECROSSSECTION_AND_DIAMETER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_WIRECROSSSECTION_AND_DIAMETER().html

---

No. of connections and cross-section / diameter # 22069.

Syntax

**C#**



public PropertyValue ARTICLE_WIRECROSSSECTION_AND_DIAMETER {get; set;}

public:

property PropertyValue^ ARTICLE_WIRECROSSSECTION_AND_DIAMETER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Displays the number of connections multiplied by the cross-section (or diameter), separated by "x". For pipes and hoses in fluid power and process engineering the property refers to the inner diameter.
