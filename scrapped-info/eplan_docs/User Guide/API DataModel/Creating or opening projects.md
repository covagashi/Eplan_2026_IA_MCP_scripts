# Creating or opening projects

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/CreateOpenProject.html

---

The most important object in the  Eplan.EplApi.DataModel  namespace is the  Project. The project must be opened in Eplan in order to be able to work with it. In an add-in, you will usually work with the project that the user has opened interactively via the GUI. You can get the project currently selected by the user via the  SelectionSet  object described in the "[Getting the current selection](HE_Selectionset.html)" topic.

However, you may also want to open or create a project in Eplan via the API ' this will certainly be the case with [offline programs](UsingEplanAssemblies.html). For this and other project-related tasks, the  Eplan.EplApi.DataModel  namespace provides the  ProjectManager  class.

To create a project, use the  CreateProject  method. It takes two parameters, the full filename of the new project link file to be created and the project template link file. The project template can be a basic project in  \*.zw9  format or a project backup in  \*.zw1  format. After successfully creating the project, it is opened and the method returns the new  Project  object.

The following example shows how to create a project.

```csharp
Project oProject = new ProjectManager().CreateProject("$(MD_PROJECTS)\\Example_003.elk", "$(MD_TEMPLATES)\\IEC_bas003.zw9");
```

To open a project, use the  OpenProject  method. Its only parameter is the full name and path of the project link file.

```csharp
Project oProject = new ProjectManager().OpenProject("$(MD_PROJECTS)\\EPLAN_Sample_Project.elk");
```

### Remarks

In offline programs, you need to open a LockingStep, before you open or create an Eplan project or use any other data model object.