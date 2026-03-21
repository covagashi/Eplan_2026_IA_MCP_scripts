# Unite Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Edit3D~Unite.html

---

Merges collection of layout space components in such a way that their are treated like `one` object.

Syntax

**C#**



public Placement3D Unite( 

   IEnumerable<Placement3D> colPlacements2Unite,

   PointD3D oPoint

)

public:

Placement3D^ Unite( 

   IEnumerable<Placement3D^>^ colPlacements2Unite,

   PointD3D oPoint

)


#### Parameters

*colPlacements2Unite*
:   Collection of objects which will be combined. Must have at least 2 elements.

*oPoint*
:   Absolute position of handle.

#### Return Value

New object which parent is an installation space of components from which it has been created. If value is `null` unite didn't end with success. For more information in this case please check system messages.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Is thrown in case of null collection is passed or number of valid items is less then 2. |
| [System.ApplicationException](#) | If this functionality is not avaiable. Please check exception message. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | If internal error has occured. Please check exception message. |

Remarks

Unite creates one new object by combining meshes of elements. After this method is called all objects passed as parameter become invalid.

The handle which location is a prameter is stored in a new object. If a 3D macro is generate from this object, then it is moved to this point on the cursor and placed.
