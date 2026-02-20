# Automatic actions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/AutomaticActions.html

---

This topic describes the automatic actions for the Eplan command line ' we also call them "**command line actions**". In contrast to a normal ribbon action, an automatic action does a complete task without any user interaction. It will show no dialogs.

### How do automatic actions work?

A command line action first checks, whether all parameters passed to it are valid. It checks if a given parameter exists or if the given project is available, etc. It then processes the parameter values so that they can be passed to the parameters of the corresponding API  HEServices  class. Now, the  HEServices  function is called and performs the actual task. This approach ensures that command line actions and  HEServices  functions conduct exactly the same internal functionality.

A command line action has either the complete or a subset of the functionality of the respective  HEServices  class. The following figure shows the principle:

These are some of the available command line actions:

- Backup projects and master data
- Restore projects and master data
- Compress projects
- Import
- Export
- Device list
- Parts list
- Connections and cable generation
- Search
- Edit
- Print
- Translate
- Check
- Labeling
- Getting the selected project or page
- ...

### General remarks

- If the project name parameter is not specified, the currently selected project is used. When calling the action from the Windows command line the  PROJECTNAME  parameter must be set.

- Boolean values need to be set as  0  for "false" and  1  for "true".

- You may not pass an empty string as parameter value (e.g.  /PARAMETER:""). If you do not want to set a specific parameter, just skip it.

- For most parameters that specify a scheme name, the last used scheme will be used, if the respective parameter is not set. You can easily check in GUI which scheme is last used.

- In general, parameter names are not case sensitive, while parameter values may be case sensitive depending on their purpose.