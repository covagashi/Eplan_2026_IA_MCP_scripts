# FUNC_ARTICLE_FREQUENCY Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_FREQUENCY(Int32).html

---

Frequency # 26335.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FREQUENCY( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FREQUENCY {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Number of oscillations or cycles per second of a periodic signal or a wave. The value is measured in Hertz (Hz).
