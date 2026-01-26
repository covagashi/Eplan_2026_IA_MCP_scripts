# FUNC_ARTICLE_RUN_UP_TIME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentTemplatePropertyList~FUNC_ARTICLE_RUN_UP_TIME(Int32).html

---

Start-up time # 26314.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RUN_UP_TIME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RUN_UP_TIME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Time required for the maximum permissible starting current to accelerate the rotor of a synchronous or asynchronous motor from standstill to the set rotation speed.
