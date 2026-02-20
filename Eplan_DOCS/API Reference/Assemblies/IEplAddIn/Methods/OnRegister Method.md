# OnRegister Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.ApplicationFramework.IEplAddIn~OnRegister.html

---

Is called once when a new add-in is selected.

Syntax

**C#**



bool OnRegister( 

   ref bool bLoadOnStart

)

bool OnRegister( 

   bool% bLoadOnStart

)


#### Parameters

*bLoadOnStart*
:   TRUE: The module is loaded at system startup and OnInit() is called.

#### Return Value

TRUE, if the add-in was successfully loaded and registered.

Remarks

When this function returns FALSE, the add-in is not added to the system. At next start of Eplan the add-in is not loaded.  
  
If bLoadOnStart is set to FALSE, the API add-in assembly is registered but not loaded automatically on the next startup of Eplan. Still all actions registered with the add-in are known in Eplan and the add-in will be loaded once one of the actions is executed. Please mind, that in this case OnInitGui(), etc. is only called, when the dll is loaded, so normal ribbon items from the add-in are not created, when Eplan starts.
