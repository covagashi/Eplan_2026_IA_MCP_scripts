# OnElementFound Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnElementFound.html

---

Is called, when the placement below the mouse pointer changes as result of mouse movement.

Syntax

**C#**



public virtual void OnElementFound( 

   Position oPosition,

   StorableObject oStorableObject

)

public:

virtual void OnElementFound( 

   Position^ oPosition,

   StorableObject^ oStorableObject

)


#### Parameters

*oPosition*
:   Current position of cad cursor.

*oStorableObject*
:   A placement below mouse. Will be null, if no placement is below the mouse pointer.
