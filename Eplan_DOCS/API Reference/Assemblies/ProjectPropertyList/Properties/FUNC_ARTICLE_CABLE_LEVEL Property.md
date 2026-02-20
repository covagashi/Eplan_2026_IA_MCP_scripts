# FUNC_ARTICLE_CABLE_LEVEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~FUNC_ARTICLE_CABLE_LEVEL(Int32).html

---

Cable: Voltage level # 26401.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CABLE_LEVEL( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_LEVEL {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Voltage level of the cable.
