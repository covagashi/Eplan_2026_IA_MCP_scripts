# AddReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~AddReference.html

---

Adds the reference of a Placement object to the placeholder.

Syntax

**C#**



public virtual void AddReference( 

   StorableObject pObject

)

public:

virtual void AddReference( 

   StorableObject^ pObject

)


#### Parameters

*pObject*
:   Object to be referenced by the PlaceHolder.

Remarks

After adding new reference to a PlaceHolder, the property PlaceHolder.ReferencesActive is automatically set to true.
