# SetStaticCursor(StorableObject,PointD) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetStaticCursor(StorableObject,PointD).html

---

Sets [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html), that will be temporary drawn as Cursor Representation.

Syntax

**C#**



public virtual void SetStaticCursor( 

   StorableObject oStorableObject,

   PointD pntStartPos

)

public:

virtual void SetStaticCursor( 

   StorableObject^ oStorableObject,

   PointD pntStartPos

)


#### Parameters

*oStorableObject*
:   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) that will be temporary drawn as Cursor Representation.

*pntStartPos*
:   The beginning of the new coordinate system in which placement is been drawn.

Remarks

The Static Cursor will not change its shape, size or location relative to the mouse pointer a dynamic cursor can be defined (additionally) by override of OnDrawCursor() Object can be transient (not stored in database).
