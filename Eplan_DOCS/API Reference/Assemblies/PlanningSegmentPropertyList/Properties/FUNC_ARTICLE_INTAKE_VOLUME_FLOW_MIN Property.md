# FUNC_ARTICLE_INTAKE_VOLUME_FLOW_MIN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic949.html

---

Maintenance cycle # 26638.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MAINTENANCE_CYCLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MAINTENANCE_CYCLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Describes the entire sequence of maintenance activities that must be performed within a specific time period or after a specific number of hours of operation. A maintenance cycle can include multiple maintenance intervals and ensures that all necessary maintenance work is performed over time.
