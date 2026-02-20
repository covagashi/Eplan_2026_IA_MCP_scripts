# LockProjectByDefault Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~LockProjectByDefault.html

---

If set to true, the objects returned and the rest objects from project by the SelectionSet method are locked. Default value is `false`.

Syntax

**C#**



public bool LockProjectByDefault {get; set;}

public:

property bool LockProjectByDefault {

   bool get();

   void set (    bool value);

}


Remarks

`LockProjectByDefault` should be set to `true` before any chagnes on any inside elements of obtained objects.
