# import3d

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/import3d.html

---

```
Action for importing 3d data.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "STEP": Import 3D data in STEP format
 '¢ "DESIGNSPACE": Import design space (as a STEP file)
 '¢ "JT": Import 3D data in JT format
 For more information please see Eplan Platform Help.
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path. 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` IMPORTFILE
 ``` | ``` Path and name.
 ``` |
| ``` SCHEME
 ``` | ``` Import scheme (optional). If the parameter does not exist or is empty (""), the last used scheme will be applied.
 ``` |