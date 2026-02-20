# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ContactImage~Create.html

---

Creates the ContactImage object for specified function.

Syntax

**C#**



public void Create( 

   Function pParent,

   bool bOnComponent

)

public:

void Create( 

   Function^ pParent,

   bool bOnComponent

)


#### Parameters

*pParent*
:   [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) object to which contact image will be assigned.

*bOnComponent*
:   If `true` created object will be displayed next to the parent.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `pParent` is `null` or `invalid`. |
| [Eplan.EplApi.DataModel.ObjectAlreadyCreatedException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectAlreadyCreatedException.html) | Thrown when object has already been created. |

Remarks

If parent object already contains contact image object then it is removed and new one is created.

Method sets value of `parent`s property UseLocalPropertyPlacements to true if it's set to false and the selected scheme to 'User-defined'.
