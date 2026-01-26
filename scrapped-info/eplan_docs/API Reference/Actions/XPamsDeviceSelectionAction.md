# XPamsDeviceSelectionAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XPamsDeviceSelectionAction.html

---

```
 Selects device or updates device information. This object can be a project/function/connection.

```

| Parameter | Description |
| --- | --- |
| ``` ProjectName
 ``` | ``` The full path of project (optional). When project specified by ProjectName is not open, this action opens it and closes it automatically.
  If nothing is entered, the selected project will be used if the action is to be run over the user interface (e.g. via script or the ribbonbar).
  When executing from the Windows command line, ProjectName must be specified or ProjectAction has to be used before that. Otherwise a system message will appear.
  
 ``` |
| ``` Mode
 ``` | ```  Mode (optional)
  Supported modes are:
  '¢ selectDevice (default value): Selects a new device for the existing objects.
  In the process all device data including the part reference data is deleted and reassigned in accordance with the device selection.
  '¢ updateDevice : Updates only the device data of the parts of the existing objects. The part numbers and part reference data are retained.
  The functionality corresponds to the update device data context menu item in the bill of materials navigator.
  
 ``` |
| ``` KeepSwappedConnPointInformation
 ``` | ``` This parameter specifies if swapped connection point designations or wire colors (relative to the order in
  the function templates) will be kept (optional). It is only effective, if all connection point designations or wire colors will match as a set.
  
 ``` |

**Remarks**

```
 It can be passed the full path of a project. When project is not opened, this action opens it and closes it automatically.

 Alternatively, an object can be passed by a special DMBaseHandleContext.

```

**Example**

```
 Example 1 (Full path of project)

 XPamsDeviceSelectionAction /ProjectName:"C:\\My Folder\\MyProject.elk" //absolute

 XPamsDeviceSelectionAction /ProjectName:"C:\\My Folder\\MyProject"             //absolute without file-extension

 XPamsDeviceSelectionAction /ProjectName:"My Folder\\MyProject.elk"             //relative to standard-folder

 XPamsDeviceSelectionAction /ProjectName:MyProject.elk                                  //relative to standard-folder

 XPamsDeviceSelectionAction /ProjectName:MyProject                                              //relative to standard-folder without file-extension

 Example 2 (Full path of project, in scripting)

 CommandLineInterpreter oCommandLineInterpreter = new CommandLineInterpreter();

 bool bRet = oCommandLineInterpreter.Execute("XPamsDeviceSelectionAction /ProjectName:\"C:\\My Folder\\MyProject.elk\"");       //absolute

 bool bRet = oCommandLineInterpreter.Execute("XPamsDeviceSelectionAction /ProjectName:\"C:\\My Folder\\MyProject\"");           //absolute without file-extension

 bool bRet = oCommandLineInterpreter.Execute("XPamsDeviceSelectionAction /ProjectName:\"My Folder\\MyProject.elk\"");           //relative to standard-folder

 bool bRet = oCommandLineInterpreter.Execute("XPamsDeviceSelectionAction /ProjectName:MyProject.elk");                                  //relative to standard-folder

 bool bRet = oCommandLineInterpreter.Execute("XPamsDeviceSelectionAction /ProjectName:MyProject");                                              //relative to standard-folder without file-extension

 Example 3 (Object passed by context)

 StorableObjectContext context = new StorableObjectContext();

 context.StorableObject = hProject;                             //option 1: project

 context.StorableObject = hFunction;                            //option 2: function

 context.StorableObject = hConnection;                  //option 3: connection

 new CommandLineInterpreter().Execute("XPamsDeviceSelectionAction ", context);

```