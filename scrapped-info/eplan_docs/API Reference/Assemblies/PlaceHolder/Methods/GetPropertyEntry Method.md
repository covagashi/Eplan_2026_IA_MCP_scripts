# GetPropertyEntry Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~GetPropertyEntry.html

---

Gets a value or variable on a property of an object referenced by a PlaceHolder.

Syntax

**C#**



public virtual MultiLangString GetPropertyEntry( 

   StorableObject oObject,

   AnyPropertyId oProperty

)

public:

virtual MultiLangString^ GetPropertyEntry( 

   StorableObject^ oObject,

   AnyPropertyId^ oProperty

)


#### Parameters

*oObject*
:   Object from which property will be read

*oProperty*
:   The property.

#### Return Value

Value of the variable.

Remarks

If you want to get the text content of a text object, oProperty must have the property id 0.
