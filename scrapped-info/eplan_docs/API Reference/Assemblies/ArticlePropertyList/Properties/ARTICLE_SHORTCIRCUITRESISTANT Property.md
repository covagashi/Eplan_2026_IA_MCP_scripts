# ARTICLE_SHORTCIRCUITRESISTANT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_SHORTCIRCUITRESISTANT().html

---

Short-circuit proof # 22115.

Syntax

**C#**



public PropertyValue ARTICLE_SHORTCIRCUITRESISTANT {get; set;}

public:

property PropertyValue^ ARTICLE_SHORTCIRCUITRESISTANT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Property of a part variant. Shows whether a cable is short-circuit proof. In this case, it is guaranteed that the cable will not burn through between individual conductors in case of a short circuit.
