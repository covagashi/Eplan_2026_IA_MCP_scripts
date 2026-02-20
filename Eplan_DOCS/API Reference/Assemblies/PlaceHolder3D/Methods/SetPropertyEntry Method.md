# SetPropertyEntry Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~SetPropertyEntry.html

---

Sets a value or variable on a property of an object referenced by a Placeholder3D. The reference of the object will be added to the Placeholder3D if necessary.

Syntax

**C#**



public virtual void SetPropertyEntry( 

   Placement3D oObject,

   AnyPropertyId oProperty,

   MultiLangString strValue

)

public:

virtual void SetPropertyEntry( 

   Placement3D^ oObject,

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
