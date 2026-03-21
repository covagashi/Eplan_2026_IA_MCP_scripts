# ARTICLE_VISCOSITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReferencePropertyList~ARTICLE_VISCOSITY().html

---

Viscosity # 26627.

Syntax

**C#**



public PropertyValue ARTICLE_VISCOSITY {get; set;}

public:

property PropertyValue^ ARTICLE_VISCOSITY {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Measure for the viscosity of the fluid, the greater the viscosity, the more viscous (less flowable) the fluid is. This property is measured in Pascal-Seconds (Pa·s) or in the more common unit Millipascal-Seconds (mPa·s). Example: A lubricating oil has a viscosity of 100 mPa·s at 40 °C.
