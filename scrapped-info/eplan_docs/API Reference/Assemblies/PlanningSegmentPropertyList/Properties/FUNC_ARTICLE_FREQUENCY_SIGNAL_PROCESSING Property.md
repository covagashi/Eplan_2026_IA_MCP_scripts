# FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic940.html

---

Frequency (signal processing), set # 26339.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING_SET( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FREQUENCY_SIGNAL_PROCESSING_SET {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specific frequency to which a device or system is set for signal processing.
