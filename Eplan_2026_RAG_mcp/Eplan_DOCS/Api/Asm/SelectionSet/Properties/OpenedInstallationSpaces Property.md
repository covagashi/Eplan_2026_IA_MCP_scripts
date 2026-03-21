# OpenedInstallationSpaces Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~OpenedInstallationSpaces.html

---

Gets installation spaces opened in GED.

Syntax

**C#**



public InstallationSpace[] OpenedInstallationSpaces {get;}

public:

property array<InstallationSpace^>^ OpenedInstallationSpaces {

   array<InstallationSpace^>^ get();

}


#### Property Value

Returns an array of opened installation spaces.

Remarks

If GED is currently displaying an installation space it is at the first position in the array.

Note that if [LockSelectionByDefault](Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~LockSelectionByDefault.html) is `true` then only objects from projects open in read-write mode will be locked.
