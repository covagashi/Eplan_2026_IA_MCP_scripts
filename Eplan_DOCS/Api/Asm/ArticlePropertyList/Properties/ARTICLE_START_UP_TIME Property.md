# ARTICLE_START_UP_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_START_UP_TIME().html

---

Switch-on time # 26192.

Syntax

**C#**



public PropertyValue ARTICLE_START_UP_TIME {get; set;}

public:

property PropertyValue^ ARTICLE_START_UP_TIME {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Time interval which has elapsed between the application of the control signal (electrical or pneumatic) and the pressure increase at the corresponding valve outlet until 10% of the specified working pressure is reached.
