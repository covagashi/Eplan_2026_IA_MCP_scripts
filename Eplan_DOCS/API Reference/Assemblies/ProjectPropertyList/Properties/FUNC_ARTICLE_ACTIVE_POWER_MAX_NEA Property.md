# FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA(Int32).html

---

Active power (emergency power system), max. # 26646.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_ACTIVE_POWER_MAX_NEA {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum active power that a mains replacement system (such as an emergency power unit) can supply under optimum conditions.
