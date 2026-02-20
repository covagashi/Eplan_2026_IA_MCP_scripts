# FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV(Int32).html

---

Active power (general power supply), max. # 26644.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTIVE_POWER_MAX_ASV {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum active power that a generating system (general power supply) can achieve under certain conditions.
