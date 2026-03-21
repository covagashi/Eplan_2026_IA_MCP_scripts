# XGedUpdateMacroAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XGedUpdateMacroAction.html

---

```
 Updates macros.

 It can be passed the full path of a project. When project is not opened, this action opens it and closes it automatically.

```

| Parameter | Description |
| --- | --- |
| ``` ProjectName
 ``` | ``` The full path of project (optional). When project specified by ProjectName is not open, this action opens it and closes it automatically.
 ``` |
| ``` SchemeName
 ``` | ``` Defines a concrete scheme to use (optional when called from a command line). If not given, last used scheme name is used. 
 ``` |
| ``` AutoAssignLastUsedRecord
 ``` | ``` Applies the last used record for several placeholders automatically (optional), overwrites value of scheme. 
 ``` |
| ``` NewVariant
 ``` | ``` Allows replacement of one macro variant to another variant of same macro.
 ``` |

**Remarks**

```
 If no path is passed, action takes selected object in GED. Object can be a macrobox or an object of macrobox.

 Alternatively, an object can be passed by a special DMBaseHandleContext.

 This object can be also a macrobox, an object of macrobox or a project.

```

**Example**

```
 Example 1 (Selected object in GED)

 XGedUpdateMacroAction

 Example 2 (Full path of project)

 XGedUpdateMacroAction /ProjectName:"C:\\My Folder\\MyProject.elk"      //absolute

 XGedUpdateMacroAction /ProjectName:"C:\\My Folder\\MyProject"          //absolute without file-extension

 XGedUpdateMacroAction /ProjectName:"My Folder\\MyProject.elk"          //relative to standard-folder

 XGedUpdateMacroAction /ProjectName:MyProject.elk                                               //relative to standard-folder

 XGedUpdateMacroAction /ProjectName:MyProject                                                   //relative to standard-folder without file-extension

 Example 3 (Full path of project, in scripting)

 CommandLineInterpreter oCommandLineInterpreter = new CommandLineInterpreter();

 bool bRet = oCommandLineInterpreter.Execute("XGedUpdateMacroAction /ProjectName:\"C:\\My Folder\\MyProject.elk\"");    //absolute

 bool bRet = oCommandLineInterpreter.Execute("XGedUpdateMacroAction /ProjectName:\"C:\\My Folder\\MyProject\"");                //absolute without file-extension

 bool bRet = oCommandLineInterpreter.Execute("XGedUpdateMacroAction /ProjectName:\"My Folder\\MyProject.elk\"");                //relative to standard-folder

 bool bRet = oCommandLineInterpreter.Execute("XGedUpdateMacroAction /ProjectName:MyProject.elk");                                               //relative to standard-folder

 bool bRet = oCommandLineInterpreter.Execute("XGedUpdateMacroAction /ProjectName:MyProject");                                                   //relative to standard-folder without file-extension

 Example 4 (Object passed by context)

 StorableObjectContext context = new StorableObjectContext();

 context.StorableObject = hProject;                             //option 1: project

 context.StorableObject = aMacroBox;                            //option 2: macrobox

 context.StorableObject = hInstanceFromMacroBox;        //option 3: instance of macrobox

 new CommandLineInterpreter().Execute("XGedUpdateMacroAction ", context);

```