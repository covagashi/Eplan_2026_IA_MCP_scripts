# GetCurrentValue Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~GetCurrentValue.html

---

Gets current value for given object, property and index.

Syntax

**C#**



public virtual PropertyValue GetCurrentValue( 

   StorableObject oObject,

   AnyPropertyId oProperty,

   int oIndex

)

public:

virtual PropertyValue^ GetCurrentValue( 

   StorableObject^ oObject,

   AnyPropertyId^ oProperty,

   int oIndex

)


#### Parameters

*oObject*


*oProperty*


*oIndex*

#### Return Value

PropertyValue object or null.

Remarks

If the given object is not referenced in PlaceHolder, the method returns null. If property and/or index is not found for passed object in Placeholder, method returns new empty PropertyValue.
