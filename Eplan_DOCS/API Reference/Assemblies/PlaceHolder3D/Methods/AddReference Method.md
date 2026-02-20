# AddReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.PlaceHolder3D~AddReference.html

---

Adds the reference of a Placement3D object to the Placeholder3D.

Syntax

**C#**



public virtual void AddReference( 

   Placement3D pObject

)

public:

virtual void AddReference( 

   Placement3D^ pObject

)


#### Parameters

*pObject*
:   Object (Placement3D) to be referenced by the Placeholder3D.

Remarks

After adding new reference to a Placeholder3D, the property Placeholder3D.ReferencesActive is automatically set to true.
