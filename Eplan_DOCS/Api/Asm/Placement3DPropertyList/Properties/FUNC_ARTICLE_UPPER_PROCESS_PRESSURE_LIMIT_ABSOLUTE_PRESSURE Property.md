# FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic597.html

---

Process pressure (absolute pressure), max. # 26519.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_ABSOLUTE_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Highest absolute process pressure to which the parts of the device that are in contact with the media can be exposed without permanent limitation of the operating behavior. The absolute process pressure is measured in comparison to the absolute vacuum and is composed of the atmospheric pressure and the process pressure.
