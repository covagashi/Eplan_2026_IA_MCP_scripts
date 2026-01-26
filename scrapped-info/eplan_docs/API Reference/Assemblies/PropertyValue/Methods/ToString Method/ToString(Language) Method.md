# ToString(Language) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToString(Language).html

---

Returns string value of this property. When type of property is MultiLangString then only the specified language is returned. In case of a transient PropertyValue object, the stored value is returned without any cast. When property can not be read, `null` is returned instead of throwing an `EmptyPropertyException` .

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

Value of string or null when property cannot be read.
