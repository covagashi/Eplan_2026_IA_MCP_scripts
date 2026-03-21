# Project Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~Project.html

---

Returns project in context of which the verification is run.

Syntax

**C#**



public Project Project {get;}

public:

property Project^ Project {

   Project^ get();

}


#### Property Value

Project for which this verification is run, or `null`.

Remarks

Each time when offline verification is started then it is done for some project all for some elements of a project. This property returns such project. However this isn't true if the check is done as online verification. In current version of EPLAN this will return `null` instead of a project.

Have in mind that the project object returned by this property isn't lock base on flag **Eplan::EplApi::HEServices::SelectionSet:** as it is done when it is returned by **Eplan::EplApi::HEServices::SelectionSet:** or [Eplan.EplApi.DataModel.ProjectManager.OpenProjects](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectManager~OpenProjects.html). Also please notes that locking any object in code of verification can have bed influence on performance.
