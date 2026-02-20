# CurrentlyEdited Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~CurrentlyEdited.html

---

Determines Page or InstallationSpace currently edited in graphical editor.

Syntax

**C#**



public StorableObject CurrentlyEdited {get;}

public:

property StorableObject^ CurrentlyEdited {

   StorableObject^ get();

}


#### Property Value

Page or InstallationSpace currently edited in graphical editor. Returns null if nothing is open in graphical editor.
