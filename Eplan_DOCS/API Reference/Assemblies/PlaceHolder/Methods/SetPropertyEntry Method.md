# SetPropertyEntry Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~SetPropertyEntry.html

---

Sets a value or variable on a property of an object referenced by a PlaceHolder. The reference of the object will be added to the PlaceHolder if necessary.

Syntax

**C#**



public virtual void SetPropertyEntry( 

   StorableObject oObject,

   AnyPropertyId oProperty,

   MultiLangString strValue

)

public:

virtual void SetPropertyEntry( 

   StorableObject^ oObject,

   AnyPropertyId^ oProperty,

   MultiLangString^ strValue

)


#### Parameters

*oObject*
:   Object on which the property will be set.

*oProperty*
:   Property

*strValue*
:   Value of the property
