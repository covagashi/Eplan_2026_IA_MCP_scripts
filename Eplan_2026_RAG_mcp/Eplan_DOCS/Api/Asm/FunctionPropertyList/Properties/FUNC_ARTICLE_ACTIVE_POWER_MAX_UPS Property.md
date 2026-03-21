# FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS(Int32).html

---

Active power (uninterruptible power supply), max. # 26648.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTIVE_POWER_MAX_UPS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum active power that can be provided by an uninterruptible power supply under optimum conditions.
