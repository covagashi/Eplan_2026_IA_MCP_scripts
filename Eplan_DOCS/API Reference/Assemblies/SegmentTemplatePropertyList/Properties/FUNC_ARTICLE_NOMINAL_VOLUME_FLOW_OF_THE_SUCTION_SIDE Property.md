# FUNC_ARTICLE_NOMINAL_VOLUME_FLOW_OF_THE_SUCTION_SIDE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1192.html

---

Nominal flow rate (compressed air) # 26511.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_NOMINAL_VOLUMETRIC_FLOW_OF_COMPRESSED_AIR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_NOMINAL_VOLUMETRIC_FLOW_OF_COMPRESSED_AIR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Quantity of compressed air that a system or device can deliver under defined nominal conditions. The value is usually measured in cubic meters per hour (m³/h) or liters per minute (l/min).
