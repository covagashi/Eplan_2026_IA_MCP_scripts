# CustomDefaultPath Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.FileSelectDecisionContext~CustomDefaultPath.html

---

Set or get the CustomDefaultPath. This is the path the File Select Dialog opens first. The second time the path is used the user has selected the last time. Then the context menu "Set to standard" will select this path again.

Syntax

**C#**



public string CustomDefaultPath {get; set;}

public:

property String^ CustomDefaultPath {

   String^ get();

   void set (    String^ value);

}


Remarks

When the strCustomDefaultPath is empty, the system fills it automatically again.
