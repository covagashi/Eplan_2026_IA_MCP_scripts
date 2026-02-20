# LockProjectByDefault Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~LockProjectByDefault.html

---

Returns whether project(s) are locked by default

Syntax

**C#**



public bool LockProjectByDefault {get; set;}

public:

property bool LockProjectByDefault {

   bool get();

   void set (    bool value);

}


#### Property Value

true : [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)s are locked by default (default value)

false : [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)s are not locked by default

Remarks

Determines if projects accessed by [CurrentProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~CurrentProject.html) and [OpenProjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProjects.html) should be locked by default or not.
