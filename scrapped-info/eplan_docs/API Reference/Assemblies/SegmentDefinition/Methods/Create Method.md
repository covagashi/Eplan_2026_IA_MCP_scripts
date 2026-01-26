# Create Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentDefinition~Create.html

---

Creates SegmentDefinition object.

Syntax

**C#**



public void Create( 

   string strIdentifyingName,

   SegmentDefinition pParent

)

public:

void Create( 

   String^ strIdentifyingName,

   SegmentDefinition^ pParent

)


#### Parameters

*strIdentifyingName*
:   Identifying name of the segment definition. Can't be `null` or start with 'Eplan.'.

*pParent*
:   Parent of this new segment definition. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown if any of parameters is `null`. |
| [System.ArgumentException](#) | Thrown if any of parameters is is invalid. |
| [Eplan.EplApi.DataModel.ObjectCreationException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ObjectCreationException.html) | Thrown when object cannot be created. |

Remarks

Name of segment definition identifies the segment across the project. It has to be a non-zero string which has to contain a char: '.' and can't start with a digital. User-defined segment definition can't start also with text: 'Eplan.'.
