# SetStaticCursor(StorableObject[],PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetStaticCursor(StorableObject[],PointD).html

---

Sets [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html), that will be temporary drawn as Cursor Representation.

Syntax

**C#**



public virtual void SetStaticCursor( 

   StorableObject[] arrStorableObjects,

   PointD pntStartPos

)

public:

virtual void SetStaticCursor( 

   array<StorableObject^>^ arrStorableObjects,

   PointD pntStartPos

)


#### Parameters

*arrStorableObjects*
:   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) that will be temporary drawn as Cursor Representation.

*pntStartPos*
:   The beginning of the new coordinate system in which placements are been drawn.

Remarks

The Static Cursor will not change its shape, size or location relative to the mouse pointer a dynamic cursor can be defined (additionally) by override of OnDrawCursor(). Objects can be transient (not stored in database).
