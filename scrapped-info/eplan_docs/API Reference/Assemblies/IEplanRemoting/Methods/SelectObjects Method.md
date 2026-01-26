# SelectObjects Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Remotingu~Eplan.EplApi.Remoting.IEplanRemoting~SelectObjects.html

---

Select Objects in Ged.

Syntax

**C#**



EplanResponse SelectObjects( 

   string strFullProjectName,

   StringCollection objectIds,

   bool bDeselectAll

)

EplanResponse^ SelectObjects( 

   String^ strFullProjectName,

   StringCollection^ objectIds,

   bool bDeselectAll

)


#### Parameters

*strFullProjectName*
:   Full project path name.

*objectIds*
:   Ids of objects to select.

*bDeselectAll*
:   Deselect all objects which already selected.

#### Return Value

Eplan response.

Remarks

This call is executed synchronously.
