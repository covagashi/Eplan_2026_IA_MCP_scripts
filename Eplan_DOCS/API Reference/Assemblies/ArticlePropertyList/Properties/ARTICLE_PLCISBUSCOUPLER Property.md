# ARTICLE_PLCISBUSCOUPLER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCISBUSCOUPLER().html

---

Bus coupler / head station # 22019.

Syntax

**C#**



public PropertyValue ARTICLE_PLCISBUSCOUPLER {get; set;}

public:

property PropertyValue^ ARTICLE_PLCISBUSCOUPLER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Property of a part variant. Identifies a device as a bus coupler or as a head station. In the case of a head station the Rack property has to be filled additionally for the respective PLC card.
