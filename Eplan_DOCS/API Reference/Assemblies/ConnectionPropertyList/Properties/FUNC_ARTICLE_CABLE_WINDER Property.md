# FUNC_ARTICLE_CABLE_WINDER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_CABLE_WINDER(Int32).html

---

Cable reel # 26394.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_CABLE_WINDER( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_CABLE_WINDER {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Type of cable reel. Example: An extension cable is supplied with an integrated cable drum.
