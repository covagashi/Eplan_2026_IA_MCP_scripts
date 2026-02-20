# IsMatching Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ICustomFilter~IsMatching.html

---

This method should be overridden in order to implement the filter.

Syntax

**C#**



bool IsMatching( 

   StorableObject objectToCheck

)

bool IsMatching( 

   StorableObject^ objectToCheck

)


#### Parameters

*objectToCheck*
:   Object that is to be tested by the filter. Always is different than `null`.
