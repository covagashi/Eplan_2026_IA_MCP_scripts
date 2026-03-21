# RegisterCustomPropertyEditorAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/RegisterCustomPropertyEditorAction.html

---

```
 Registers/Unregisters a custom editor dialog for a property ID

 or identifying name of a user-defined property.

```

| Parameter | Description |
| --- | --- |
| ``` PropertyId
 ``` | ``` Property ID
 ``` |
| ``` PropertyIndex
 ``` | ``` Property index
 ``` |
| ``` PropertyIdentName
 ``` | ``` Identifying name of the user-defined property
 ``` |
| ``` Action
 ``` | ``` This action will be called for editing the specified property.
 ``` |
| ``` Editable
 ``` | ``` "true" (1): edit inside of the hotspot cell allowed.
 ``` |
| ``` Register
 ``` | ```  "true" (1): register this action.
  "false" (0): unregister this action.
 ``` |

**Remarks**

```
 You can replace the behavior from all properties in a property grid.

 If you edit a property in a property grid, you get a hotspot button instead of the default control type.

 If you click on the hotspot button, the given action will be started and you can modify the displayed value in a separate dialog with the given calling context.

 Calling context of the registered Action are:

 * Parameters *

 PropertyId:           Property ID

 PropertyIndex:        Property Index

 PropertyIdentName:    Identifying name of user-defined property

 DbObjectId:           Object ID from the first data model

 Value:                Displayed string or multilanguage string

 * Return values *

 DialogModalResult:   1 for OK

 DialogModified:      1 (True) for modified

 Value:               new display value or new multilanguage string

```

**Example**

```
       RegisterCustomPropertyEditorAction /Register:True /Action:WPF_Demo_Custom_Editor /PropertyId:40001 /PropertyIndex:0 /Editable:False

       RegisterCustomPropertyEditorAction /Register:True /Action:WPF_Demo_Custom_Editor /PropertyId:40002 /PropertyIndex:0 /Editable:True

       RegisterCustomPropertyEditorAction /Register:1 /Action:WPF_Demo_Custom_Editor /PropertyId:20901 /PropertyIndex:1 /Editable:0

       RegisterCustomPropertyEditorAction /Register:1 /Action:WPF_Demo_Custom_Editor /PropertyId:20901 /PropertyIndex:2 /Editable:1

       RegisterCustomPropertyEditorAction /Register:1 /Action:WPF_Demo_Custom_Editor /PropertyIdentName:EPLAN.Page.UserSupplementaryField1 /Editable:0

       RegisterCustomPropertyEditorAction /Register:1 /Action:WPF_Demo_Custom_Editor /PropertyIdentName:EPLAN.Page.UserSupplementaryField2 /Editable:1

       RegisterCustomPropertyEditorAction /Register:False /Action:WPF_Demo_Custom_Editor /PropertyId:40001 /PropertyIndex:0

       RegisterCustomPropertyEditorAction /Register:0 /Action:WPF_Demo_Custom_Editor /PropertyId:40002 /PropertyIndex:0

       RegisterCustomPropertyEditorAction /Register:False /Action:WPF_Demo_Custom_Editor /PropertyId:20901 /PropertyIndex:1

       RegisterCustomPropertyEditorAction /Register:0 /Action:WPF_Demo_Custom_Editor /PropertyId:20901 /PropertyIndex:2

       RegisterCustomPropertyEditorAction /Register:False /Action:WPF_Demo_Custom_Editor /PropertyIdentName:EPLAN.Page.UserSupplementaryField1

       RegisterCustomPropertyEditorAction /Register:0 /Action:WPF_Demo_Custom_Editor /PropertyIdentName:EPLAN.Page.UserSupplementaryField2

```