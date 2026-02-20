# TransformObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~TransformObjects.html

---

Transforms all objects from source page to target page.

Syntax

**C#**



public Dictionary<StorableObject,StorableObject> TransformObjects( 

   ChangeOfStandard.RotationAndFlipping rotationAndFlipping,

   Page sourcePage,

   Page targetPage

)

public:

Dictionary<StorableObject^,StorableObject^>^ TransformObjects( 

   ChangeOfStandard.RotationAndFlipping rotationAndFlipping,

   Page^ sourcePage,

   Page^ targetPage

)


#### Parameters

*rotationAndFlipping*
:   Determines how objects should be transformed

*sourcePage*
:   Page from which all objects will be taken

*targetPage*
:   Page to which all object will be inserted after expected operations

#### Return Value

The dictionary with pairs of objects (source, transformed)

Exceptions

| Exception | Description |
| --- | --- |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurs during transform operation. |
| **ArgumentNullException** | `sourcePage` or `targetPage` is null. |

Remarks

All objects from source page should be copied into target page with given rotation and mirrored if expected. Note that for symbol rotation and mirroring first the correct scheme should be set by the [SetSchema:Eplan::EplApi::HEServices::ChangeOfStandards:](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.ChangeOfStandard~SetSchema.html) method. Please be aware that objects out of a plot frame are ignored by this method. It also does not work in case of pages without a plot frame.
