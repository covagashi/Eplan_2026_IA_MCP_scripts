# FUNC_ARTICLE_FLOW_RATE_OPERATING_NORMAL_VOLUME_FLOW Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1162.html

---

Frequency range # 26343.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FREQUENCY_RANGE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FREQUENCY_RANGE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Range of the frequencies in which a device or system works. The value is often specified in Hertz (Hz) or Kilohertz (kHz) and specifies the minimum and maximum frequencies that a device can process or generate.
