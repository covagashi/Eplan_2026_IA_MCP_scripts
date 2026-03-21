---
title: "HTML example"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eectext_k_example_case_html.htm"
file: "eectext_k_example_case_html"
category: "eectext"
---

# HTML example

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  HTML example HTML: The HTML object in the example is of the **TextDisciplineConfiguration** type. It is the central object in the configuration of a text discipline, and it bears the name that was assigned when the discipline was created. Central settings, e.g. the name displayed in the popup menu, are specified here: In the HTMLDisciplineConfiguration, the user can also specify whether, when dealing with new components, the resources in the model should be saved internally or externally (see internal and external resources). Another important aspect when configuring the discipline is the configuration page of the editor, which offers the following setting options: Configuration parameter | Meaning  
---|---  
Discipline root | Reference to the object that represents the root of the discipline structure in projects.  
Top-level discipline component | Reference to the component that all of the components of the discipline inherit from  
Parameter unit | Unit within the library where parameters are automatically created, as needed. If, for example, a resource with previously unknown parameters is inserted, EEC automatically creates new parameters in this unit.  
Resource storage location | Path to the folder containing the external resources of the discipline.  
Parser configuration | Reference to the object in which the configuration of the parser is set for the resources of the discipline.  
Structure generator | Specification of the behavior of the structure generator. In general, the structure generator currently operates on the basis of a plug-socket concept at all times. It is possible to set whether a socket can also be defined by the name of a component. If the ânames do not define socketsâ option is selected, then only parameters of the socket type are used as sockets.  
Code generator | It is possible to set whether the contents of all of the resources of a discipline structure are to be created in one file, or whether a specific file should be created for each resource, e.g. when HTML documentation with multiple pages and hyperlinks is created.  
Hyperlinks can be used to navigate to referenced components (ALT+left mouse-click). HTMLRoot: The HTMLRoot object is the library component for the root of the discipline-specific structure in the project: The icon and the displayed name can be modified for this root: HTMLComponents: For each text discipline, a top-level component is created; all of the components of the discipline derive from this component. HTMLParserConfiguration: The configuration of the parser for the resources of a text discipline is set via a separate object. This includes setting the syntax that can be used to specify parameters in the existing resources. HTML-Commands: When the HTML discipline is created, objects are created that can be used to execute specific commands for the HTML discipline:
     * **GenerateHTMLStructureCommand:** Generates the HTML discipline structures in a project from the mechatronic structure.
     * **GenerateHTMLCodeCommand:** Generates the HTML document in the Eclipse workspace from the HTML discipline structure
     * **OpenHTMLWithEclipseCommand:** Opens the created HTML document in the editor specified in Eclipse (set via Settings -> General -> Editors -> File associations)
     * **OpenHTMLWithOSCommand:** Opens the created HTML document in the editor assigned by the operating system for opening HTML files.
The commands reference disciplines for which they are executable via the editorâs Disciplines page: HTML actions: When the HTML discipline is created, objects are created that extend the UI to include certain actions. The actions provide the user with access to the commands:
     * **HTMLGenerateStructure:** Executes GenerateHTMLStructureCommand.
     * **HTMLCodeGenerieren:** Executes GenerateHTMLCodeCommand.
     * **HTMLGenerateAndOpenStructure:** Executes GenerateHTMLStructureCommand, GenerateHTMLCodeCommand, and OpenHTMLWithEclipseCommand in a single step.
The actions should be understood as useful suggestions for deploying a text discipline. They can, of course, be modified as needed. Text discipline: In the \install\icon-collection folder we have started collecting icons that can be used in configuring text disciplines (additional contributions to the collection are very welcome!). Plug-socket variant adjustable: The text discipline supports the two plug-socket variants Plug Socket (Names are sockets) and Plug Socket (Names do not define sockets) of the structure generator. They can be set in the text discipline editor.
