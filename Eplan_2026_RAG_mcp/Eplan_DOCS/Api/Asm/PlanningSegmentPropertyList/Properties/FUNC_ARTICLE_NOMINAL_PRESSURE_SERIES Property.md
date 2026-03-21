# FUNC_ARTICLE_NOMINAL_PRESSURE_SERIES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic964.html

---

Nominal flow rate # 26507.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_VOLUME_FLOW( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_VOLUME_FLOW {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Flow rate measured under defined nominal conditions. These are the conditions for which a device was designed with regard to its application when it is not under load. The nominal flow rate indicates how many volumes of a medium (e.g., air, water) flow through a system or a component per unit of time. These are usually specified in cubic meters per hour (m³/h) or liters per minute (l/min).
