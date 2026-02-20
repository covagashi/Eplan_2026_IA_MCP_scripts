# GetSourcesAndTargets(ICollection<StorableObject>,ICollection<StorableObject>,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic702.html

---

Gets sources and targets of the cable.

Syntax

**C#**



public void GetSourcesAndTargets( 

   ICollection<StorableObject> colSources,

   ICollection<StorableObject> colTargets,

   bool bForAllWires

)

public:

void GetSourcesAndTargets( 

   ICollection<StorableObject^>^ colSources,

   ICollection<StorableObject^>^ colTargets,

   bool bForAllWires

)


#### Parameters

*colSources*
:   Collection which will be filled with sources of the cable. Can't be null or read-only.

*colTargets*
:   Collection which will be filled with targets of the cable. Can't be null or read-only.

*bForAllWires*
:   If set to `true` collections for sourcres and target will be filled for every connection. If set to `false` works like overloaded method.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | If any parameter is `null`. |
| [System.NotSupportedException](#) | Thrown if given collection is read-only. |
| [Eplan.EplApi.DataModel.InvalidHandleException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidHandleException.html) | Thrown when internally used handle is not valid. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | Thrown when an internal error occured. Please refer to the error message. |

Remarks

Method removes all elements from given collections and fills them with sources and targets of a cable. When method is used for all wires it outputs device tags of sources and targets with detailed information about connections.
