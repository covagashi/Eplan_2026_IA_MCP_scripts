# FUNC_ARTICLE_APPLICATION_AREA_OF_THE_CABLE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic145.html

---

Operating area: Cable # 26288.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_APPLICATION_AREA_OF_THE_CABLE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_APPLICATION_AREA_OF_THE_CABLE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Foreseen operating area of the cable.
