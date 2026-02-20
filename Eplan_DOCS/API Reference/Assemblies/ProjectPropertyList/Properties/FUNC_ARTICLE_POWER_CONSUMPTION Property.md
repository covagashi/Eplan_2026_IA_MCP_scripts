# FUNC_ARTICLE_POWER_CONSUMPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_POWER_CONSUMPTION(Int32).html

---

Power consumption # 26418.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_POWER_CONSUMPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_POWER_CONSUMPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Quantity of electrical energy that a device or component consumes during operation. The power consumption describes the actual energy consumption.
