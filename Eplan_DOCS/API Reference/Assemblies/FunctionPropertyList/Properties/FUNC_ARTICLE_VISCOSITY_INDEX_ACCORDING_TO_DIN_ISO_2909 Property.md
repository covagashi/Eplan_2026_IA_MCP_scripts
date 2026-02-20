# FUNC_ARTICLE_VISCOSITY_INDEX_ACCORDING_TO_DIN_ISO_2909 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic249.html

---

Viscosity index (acc. to DIN ISO 2909) # 26630.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_VISCOSITY_INDEX_ACCORDING_TO_DIN_ISO_2909( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_VISCOSITY_INDEX_ACCORDING_TO_DIN_ISO_2909 {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Description of a temperature-related kinematic viscosity change of a base oil or a completely formulated oil, but not its actual viscosity. The viscosity index VI is used as a measure of the temperature dependence of the viscosity in lubricating oils in the field of application. This index is calculated from the kinematic viscosity at two reference temperatures, typically 40 °C and 100 °C.
