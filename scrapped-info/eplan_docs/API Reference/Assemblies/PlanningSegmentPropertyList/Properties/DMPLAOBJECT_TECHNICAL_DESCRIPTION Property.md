# DMPLAOBJECT_TECHNICAL_DESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic865.html

---

User-defined property: Name # 44054.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_USERPROPERTY_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_USERPROPERTY_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

This property can be used in reports and displays the name of a user-defined property. Up to 100 properties can be differentiated by using the index.
