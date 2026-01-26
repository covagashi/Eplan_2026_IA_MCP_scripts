# FUNC_ARTICLE_RANGE_OF_APPLICATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1240.html

---

Rated apparent power # 26235.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_APPARENT_POWER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_APPARENT_POWER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Power specification of the manufacturer, which results from the root mean square values of the electric current and voltage and is composed of an active power component and a reactive power component and was determined under specified conditions and rules. It identifies the power to be supplied or to be output of an electrical device.
