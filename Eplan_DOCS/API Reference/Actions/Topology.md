# Topology

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Topology.html

---

```
Action for topology-related operations.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 "RouteConnections": Routes given topology connections.
 "CreateFunctions": Creates topology functions that are connected to structure routing fulcrums.
 ``` |

**Remarks**

```
This action is available only for users with license option: Cabling.

```

**Example**

```
Route topology connections

Topology /TYPE:RouteConnections /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

Topology function generation

Topology /TYPE:CreateFunctions /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

```