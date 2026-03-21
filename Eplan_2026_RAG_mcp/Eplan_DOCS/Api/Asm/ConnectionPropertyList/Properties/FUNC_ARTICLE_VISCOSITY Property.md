# FUNC_ARTICLE_VISCOSITY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_VISCOSITY(Int32).html

---

Viscosity # 26628.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_VISCOSITY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_VISCOSITY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Measure for the viscosity of the fluid, the greater the viscosity, the more viscous (less flowable) the fluid is. This property is measured in Pascal-Seconds (Pa·s) or in the more common unit Millipascal-Seconds (mPa·s). Example: A lubricating oil has a viscosity of 100 mPa·s at 40 °C.
