# ArePlanningObjectsStructureMerged Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Insert~ArePlanningObjectsStructureMerged.html

---

Indicates whether planning objects structure will be merged with existing nodes or renumbered and added.

Syntax

**C#**



public bool ArePlanningObjectsStructureMerged {get; set;}

public:

property bool ArePlanningObjectsStructureMerged {

   bool get();

   void set (    bool value);

}


Remarks

This flag is used in situation when structure of pre-planning objects imported from macro, contains nodes which already exists in project. If `ArePlanningObjectsStructureMerged` is `true` then all children of duplicated node are added to coresponding nore from project. If value is `false` then new name is assigned to such node and it is added to project with all its children.
