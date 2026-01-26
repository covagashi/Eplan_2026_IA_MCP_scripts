# GetSourcesAndTargets(ICollection<StorableObject>,ICollection<StorableObject>) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic703.html

---

Gets sources and targets of the cable.

Syntax

**C#**



public void GetSourcesAndTargets( 

   ICollection<StorableObject> colSources,

   ICollection<StorableObject> colTargets

)

public:

void GetSourcesAndTargets( 

   ICollection<StorableObject^>^ colSources,

   ICollection<StorableObject^>^ colTargets

)


#### Parameters

*colSources*
:   Collection which will be filled with sources of the cable. Can't be null or read-only.

*colTargets*
:   Collection which will be filled with targets of the cable. Can't be null or read-only.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.NotSupportedException](#) | Thrown if given collection is read-only. |
| [Eplan.EplApi.DataModel.InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when internally used handle is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an internal error occured. Please refer to the error message. |

Remarks

Method removes all elements from given collections and fills them with sources and targets of a cable. Please consider that the method outputs device tags of sources and targets without detailed information about connection points. It is the same as in 'Connection overview' standard report.
