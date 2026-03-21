# OnSelect Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSelect.html

---

Is called after object selection in the graphical editor by user.

Syntax

**C#**



public virtual RequestCode OnSelect( 

   StorableObject[] arrSelectedObjects,

   SelectionContext oContext

)

public:

virtual RequestCode OnSelect( 

   array<StorableObject^>^ arrSelectedObjects,

   SelectionContext^ oContext

)


#### Parameters

*arrSelectedObjects*
:   Array containing the selected placements.

*oContext*
:   Information about the selection operation.

#### Return Value

Default [RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) for this function is `Success`.
