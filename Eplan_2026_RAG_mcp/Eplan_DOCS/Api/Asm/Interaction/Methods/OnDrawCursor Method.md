# OnDrawCursor Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnDrawCursor.html

---

Is called to get drawable objects for the cursor representation.

Syntax

**C#**



public virtual StorableObject[] OnDrawCursor( 

   Position oPosition

)

public:

virtual array<StorableObject^>^ OnDrawCursor( 

   Position^ oPosition

)


#### Parameters

*oPosition*
:   Is the current position of cad cursor.

#### Return Value

Array of object drawn under the Cursor.

Remarks

This objects may be transient (not stored in the database).
