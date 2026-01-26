# ARTICLE_CABLEDISPLAYFORM Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_CABLEDISPLAYFORM().html

---

Cable assignment diagram form # 22034.

Syntax

**C#**



public PropertyValue ARTICLE_CABLEDISPLAYFORM {get; set;}

public:

property PropertyValue^ ARTICLE_CABLEDISPLAYFORM {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Shows the form to be used for the cable assignment diagram. When selecting a part the contents of this property are transferred to the main function. For the report, only those cables are considered which are assigned a form in the property "Cable assignment diagram form". All other cables are ignored.
