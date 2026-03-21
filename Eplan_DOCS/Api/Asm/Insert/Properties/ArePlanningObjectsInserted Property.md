# ArePlanningObjectsInserted Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~ArePlanningObjectsInserted.html

---

Indicates whether additional planning objects are inserted from macro into project.

Syntax

**C#**



public bool ArePlanningObjectsInserted {get; set;}

public:

property bool ArePlanningObjectsInserted {

   bool get();

   void set (    bool value);

}


Remarks

If macro contains pre-planning object structure this flag determine if it is imported or not. Structure from macro is inserted under root node of project and only if its segment definition allows such parent.

This flag has influence only on functions importing window macros.
