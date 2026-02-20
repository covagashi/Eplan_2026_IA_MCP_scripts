# FUNC_ARTICLE_FREQUENCY_RANGE_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_FREQUENCY_RANGE_MIN(Int32).html

---

Frequency range, min. # 26333.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FREQUENCY_RANGE_MIN( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FREQUENCY_RANGE_MIN {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Minimum frequency that a device or system can process or generate. This specification is made in Hertz (Hz) or Kilohertz (kHz) and specifies the lower limit of the frequency range in which the device can operate effectively.
