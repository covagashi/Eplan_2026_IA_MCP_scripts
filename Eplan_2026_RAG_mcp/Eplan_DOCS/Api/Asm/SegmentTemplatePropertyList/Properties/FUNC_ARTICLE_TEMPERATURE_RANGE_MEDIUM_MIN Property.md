# FUNC_ARTICLE_TEMPERATURE_RANGE_MEDIUM_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1274.html

---

Torque (at max. rotation speed) # 26250.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_TORQUE_AT_MAX_SPEED( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_TORQUE_AT_MAX_SPEED {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Torque at the maximum permissible output speed of the drive engine.
