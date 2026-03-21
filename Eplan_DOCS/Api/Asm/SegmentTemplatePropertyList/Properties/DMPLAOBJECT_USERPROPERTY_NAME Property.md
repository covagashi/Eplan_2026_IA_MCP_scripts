# DMPLAOBJECT_USERPROPERTY_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1092.html

---

User-defined property: Value # 44055.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_USERPROPERTY_VALUE( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_USERPROPERTY_VALUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

This property can be used in reports and displays the value of the associated user-defined property with the same index. Up to 100 properties can be differentiated by using the index.
