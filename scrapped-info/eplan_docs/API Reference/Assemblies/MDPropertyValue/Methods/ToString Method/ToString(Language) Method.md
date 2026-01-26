# ToString(Language) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToString(Language).html

---

Returns string value of this property. When type of property is MultiLangString then only specified language is returned. In case of offline MDPropertyValue object, stored value is returned without any cast. When property can not be read, `NULL` is returned instead of throwing `MDEmptyPropertyException` .

Syntax

**C#**



public string ToString( 

   ISOCode.Language language

)

public:

String^ ToString( 

   ISOCode.Language language

)


#### Parameters

*language*
:   Language to extract from MultiLangString value.

#### Return Value

Value of string or NULL when property cannot be read.
