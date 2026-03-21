# FUNC_ARTICLE_SUCTION_VOLUME_FLOW_MAX Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1261.html

---

Suitable as monitoring device # 26356.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_SUITABLE_AS_MONITOR( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_SUITABLE_AS_MONITOR {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Component can be used for temperature monitoring.
