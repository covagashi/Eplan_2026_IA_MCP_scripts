# OnBeforeInit Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddInShadowCopy~OnBeforeInit.html

---

Called by the framework before [IEplAddIn.OnInit](Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnInit.html) and passes the location from which add-in assembly has been registered.

Syntax

**C#**



void OnBeforeInit( 

   string strOriginalAssemblyPath

)

void OnBeforeInit( 

   String^ strOriginalAssemblyPath

)


#### Parameters

*strOriginalAssemblyPath*
:   Full path to location from which the add-in assembly has been registered.

Remarks

Any exception thrown by this method don't influence the initialization process. Such exception is wrapped and logged into System messages.
