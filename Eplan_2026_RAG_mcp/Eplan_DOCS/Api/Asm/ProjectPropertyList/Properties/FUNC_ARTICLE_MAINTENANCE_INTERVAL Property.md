# FUNC_ARTICLE_MAINTENANCE_INTERVAL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_MAINTENANCE_INTERVAL(Int32).html

---

Maintenance interval # 26636.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_MAINTENANCE_INTERVAL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_MAINTENANCE_INTERVAL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies the period or operating hours between two maintenance tasks. Specification of how often a maintenance has to be carried out, for example every 6 months or every 500 operating hours.
