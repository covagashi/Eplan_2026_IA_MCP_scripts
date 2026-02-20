# API Reports Modification Interface

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API_REPORTS_MODIFICATION.html

---

The API Reports Modification Interface makes it possible to take influence on the result of report generation via an API action.

In this way, it is possible to filter or change the order of objects for a report.

Warning: When a report action is used, please don't set a filter or sort settings because it can be inconsistent with the action!

The following steps need to be done to in order to use the interface:

### a) Create a report processing action

Each report template now contains a property that allows you to set an action name:

If an action with this name is registered in Eplan, it is called on several occasions during report generation.

During these steps, you can influence the texts that appear in the report as well as the objects that are reported and the order in which they appear.

The steps are distinguished by the  mode  parameter of the called action.

The action from the template is called with the following parameters:

*Step 1.*

Parameters:

project  ' Input parameter; value: ID of a project

mode  ' Input parameter; value: "Start"

objects  ' Input parameter; value: IDs of objects that will be updated (only if you UPDATE a report)

Prepare project data for this report if necessary, fill caches etc.

*Step 2.*

Parameters:

project  ' Input parameter; value: ID of a project

mode  ' Input parameter; value: "ModifyObjectList"

objects  ' Input / output parameter; value: IDs of objects that will be evaluated separated with semicolon

This list can be modified (but not the objects themselves!). You can add or remove object IDs from the list or change their order in the list.

The  objects  parameter can be set only in "ModifyObjectList" mode!

*Step 3.*

Parameters:

project  ' Input parameter; value: ID of a project

mode  ' Input parameter; value: "ModifyPages"

pages  ' Input parameter; value: IDs of created pages separated by semicolon

The created pages and their properties can be modified.

*Step 4*.

Parameters:

project  ' Input parameter; value: ID of a project

mode  ' Input parameter; value: "Finish"

Clean up caches or undo changes made in step 1.

### b) Prepare a form to be processed

It is recommended to use a custom form that will be processed by the action described above.

This will ensure that reports can be created either in the "standard" way or in the new one.

The easiest way is to use a copy of an existing form. Such a form should be set in the Form field of the project template:

The form can have a custom actions assigned to the placeholder text. This can be set in the Form editor:

Now it is necessary to create the text processing action (see below).

### c) Create a placeholder text processing action

This action is called when the placeholder text is evaluated during the report generation. The action is called with the following parameters:

objects  ' Input parameter; value: main object for the line (can be more than one).

ActionCallingContext.SetStrings()  ' Output parameter; call  SetStrings()  of the calling context to set the result text. More than one result text will generate new lines.

color  ' Input / output parameter; value: "ColorId". Set this parameter to change the color of the placeholder text. It works with one result text only.   
Possible values are from 0 to 256. Please use "-16002" as "From layer" value.

Predefined values for line color index are:

0 = black

1 = red

2 = yellow

3 = green

4 = cyan

5 = blue

6 = magenta

7 = white

...

252 = dark gray

253 = gray

...

### d) Make sure that the new form is included in the project master data pool

This can be done using the  Eplan::EplApi::HEServices::Masterdata  class.

The following example shows how to create an embedded report with report a processing action:

```csharp
// Copy a form with placeholder text processing action to the master data directory
 File.Copy("c:\\temp\\PlugDiagramReportActionFormular.f22", new ProjectManager().Paths.Forms + "\\PlugDiagramReportActionFormular.f22", true);
 //... and add it to project master data
 StringCollection oProjectNewEntries = new StringCollection();
 oProjectNewEntries.Add(@"PlugDiagramReportActionFormular.f22");
 System.Collections.Hashtable oResult = new Masterdata().AddToProjectEx(m_oReportActionProject, oProjectNewEntries);
 // Prepare the ReportBlock object
 ReportBlock oReportBlock = new ReportBlock();
 oReportBlock.Create(m_oReportActionProject);
 // Set a form with a placeholder text processing action
 oReportBlock.FormName = "PlugDiagramReportActionFormular";
 oReportBlock.Type = DocumentTypeManager.DocumentType.PlugDiagram;
 // Set the report processing action
 oReportBlock.Action = "PlugDiagramReportAction";
 // Generate the embedded report
 ReportBlockReference oReportBlockReference = new Reports().CreateEmbeddedReport(oReportBlock, oPage, new PointD(10.0, 300.0));
```