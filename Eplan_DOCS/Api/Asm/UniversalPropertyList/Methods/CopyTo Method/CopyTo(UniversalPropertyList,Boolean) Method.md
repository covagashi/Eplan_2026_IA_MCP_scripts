# CopyTo(UniversalPropertyList,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo(UniversalPropertyList,Boolean).html

---

Copies properties to other property list.

Syntax

**C#**



public void CopyTo( 

   UniversalPropertyList destination,

   bool includeNameparts

)

public:

void CopyTo( 

   UniversalPropertyList^ destination,

   bool includeNameparts

)


#### Parameters

*destination*
:   Object of class derived from UniversalPropertyList or just UniversalPropertyList where properties will be copied.

*includeNameparts*
:   Include name parts properties.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | When destination property list is null. |

Remarks

Existing and not empty properties will be copied, except from name properties which considering is dependent on includeNameparts parameter. If target property list is transient, properties will be checked if they can exists for target object.
