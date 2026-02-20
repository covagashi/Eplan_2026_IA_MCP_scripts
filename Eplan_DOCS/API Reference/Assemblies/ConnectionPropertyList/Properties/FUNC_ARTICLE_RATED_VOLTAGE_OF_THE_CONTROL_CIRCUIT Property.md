# FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_CONTROL_CIRCUIT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic177.html

---

Nominal voltage (control circuit) # 26497.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_CONTROL_CIRCUIT( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_VOLTAGE_OF_THE_CONTROL_CIRCUIT {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specified voltage in volt, which is foreseen for the operation of an electrical control circuit.
