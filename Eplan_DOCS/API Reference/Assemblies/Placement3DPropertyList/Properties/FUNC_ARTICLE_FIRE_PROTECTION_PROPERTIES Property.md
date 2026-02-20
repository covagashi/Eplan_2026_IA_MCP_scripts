# FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic545.html

---

Fire protection properties # 26244.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_FIRE_PROTECTION_PROPERTIES {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Specifies which fire protection properties the object, for example a device or a cable bundling tube, fulfills.
