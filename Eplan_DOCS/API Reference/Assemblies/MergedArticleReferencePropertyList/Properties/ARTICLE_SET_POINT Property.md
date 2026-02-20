# ARTICLE_SET_POINT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_SET_POINT().html

---

Setpoint # 26567.

Syntax

**C#**



public PropertyValue ARTICLE_SET_POINT {get; set;}

public:

property PropertyValue^ ARTICLE_SET_POINT {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

In a closed loop control, this is the target value that the process value is to assume, expressed in units of the process value.
