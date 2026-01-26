# API Labeling Modification Interface

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API_LABELING_MODIFICATION.html

---

The API Labeling Modification Interface allows you to modify the result of label generation via API.

The following steps must be perfomed to use it in an API program:

### a) Create labeling scheme settings Action

Each labeling scheme now contains a property, where you can set an action name:

If an action with this name is registered in Eplan, it is called during label generation.

You can use the action to influence the objects that are reported and the order in which they appear.

The action is called from the template with the following parameters:

Parameters:

project  ' Input parameter; value: ID of a project

mode  ' Input parameter; value: "ModifyObjectList"

objects  ' Input / output parameter; value: IDs of objects that will be evaluated separated by semicolon

This list can be modified (but not the objects themselves!). You can add or remove object IDs from the list or change their order in the list.

### b) Create label texts processing action

You can now add an action to a label:

This action will be called, when the label is created. The action is called with the following parameters:

objects ' Input parameter; value: main object for the line (can be more than one).

ActionCallingContext.SetStrings()  ' Output parameter; call  SetStrings()  of the calling context to set the result text. More than one result text will generate new lines.

Please set only one string in the string array you pass to  SetStrings().

Line breaks are always written to the output file as they are in the string. If necessary, remove line breaks from the strings.