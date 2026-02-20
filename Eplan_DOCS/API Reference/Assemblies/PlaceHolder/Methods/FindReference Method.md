# FindReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~FindReference.html

---

Finds an object in the list of object referenced by a PlaceHolder.

Syntax

**C#**



public virtual int FindReference( 

   StorableObject oObject

)

public:

virtual int FindReference( 

   StorableObject^ oObject

)


#### Parameters

*oObject*
:   The referenced object to search for.

#### Return Value

The index of the reference or -1, if the object was not found.
