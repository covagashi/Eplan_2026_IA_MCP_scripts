# PrePlanningMacro Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~PrePlanningMacro.html

---

Inserts the pre-planning macros below the given structure segment.

Syntax

**C#**



public StorableObject[] PrePlanningMacro( 

   string strMacroPath,

   Project pProject,

   PlanningSegment pParent

)

public:

array<StorableObject^>^ PrePlanningMacro( 

   String^ strMacroPath,

   Project^ pProject,

   PlanningSegment^ pParent

)


#### Parameters

*strMacroPath*
:   Full file name of the pre-planning macro file (.emv) to be placed. Can't be `null` or `empty`

*pProject*
:   Project into which macro will be inserted. Can't be `null`.

*pParent*
:   Planning segment under which macro will be inserted.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown in case of invalid parameter. |
| [System.ArgumentNullException](#) | Null was set to a needed parameter. |

Remarks

If parent of macro is `null` then macro is inserted under project in pre-planning stucture.
