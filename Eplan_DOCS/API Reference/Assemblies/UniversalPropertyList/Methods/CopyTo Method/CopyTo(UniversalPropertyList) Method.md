# CopyTo(UniversalPropertyList) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo(UniversalPropertyList).html

---

Copies properties to other property list.

Syntax

**C#**



public void CopyTo( 

   UniversalPropertyList destination

)

public:

void CopyTo( 

   UniversalPropertyList^ destination

)


#### Parameters

*destination*
:   Object of class derived from UniversalPropertyList or just UniversalPropertyList where properties will be copied.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | When destination property list is null. |

Remarks

All existing and not empty properties will be copied, excluding name parts. If target property list is transient, properties will be checked if they can exists for target object.
