# ToString(Language,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToString(Language,String).html

---

Returns string value of this property. When type of property is MultiLangString then only the specified language is returned. In case of a transient PropertyValue object, the stored value is returned without any cast. When property can not be read, `default_value` is returned instead of throwing an `EmptyPropertyException` .

Syntax

**C#**



public string ToString( 

   ISOCode.Language language,

   string default_value

)

public:

String^ ToString( 

   ISOCode.Language language,

   String^ default_value

)


#### Parameters

*language*
:   Language to extract from MultiLangString value.

*default\_value*
:   Default value which is retuned when property cannot be read.

#### Return Value

Value of string or `default_value` when property can not be read from object or properties list.
