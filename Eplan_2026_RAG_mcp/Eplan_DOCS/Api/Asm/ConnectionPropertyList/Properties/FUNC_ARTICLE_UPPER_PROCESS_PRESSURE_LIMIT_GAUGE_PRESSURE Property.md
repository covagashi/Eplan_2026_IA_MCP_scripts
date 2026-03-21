# FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic189.html

---

Process pressure (overpressure), max. # 26521.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_UPPER_PROCESS_PRESSURE_LIMIT_GAUGE_PRESSURE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Highest process overpressure to which parts of the device that are in contact with the media can be exposed without permanent limitation of the operating behavior. The process overpressure is measured relative to the atmospheric pressure and is the pressure which exceeds the normal atmospheric pressure.
