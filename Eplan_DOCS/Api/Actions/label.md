# label

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/label.html

---

```
Action class to create labels for projects.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Configuration scheme (optional).
 Default value: Most recently used configuration scheme.
 ``` |
| ``` FILTERSCHEME
 ``` | ``` Filter scheme (optional).
 Default value: Filter scheme name is taken from configuration scheme. If this parameter is not available, nofiltering can be performed.
 ``` |
| ``` SORTSCHEME
 ``` | ``` Sorting scheme.
 Default value: Sorting scheme name is taken from configuration scheme. If this parameter is not available, no sorting can be performed.
 ``` |
| ``` LANGUAGE
 ``` | ``` Language (e.g., en_US or ??_?? for all display languages).
 ``` |
| ``` DESTINATIONFILE
 ``` | ``` Target file where the labeling results are saved.
 The following formats are supported: txt, xls, xlsx, xml. Format must be set according to the extension that is in CONFIGSCHEME.
 This parameter supports PROJPROP_* Eplan variables.
 Default value: file indicated by a configuration scheme (CONFIGSCHEME parameter) 
 ``` |
| ``` RECREPEAT
 ``` | ``` Optional: Number of repetitions per label (>=1).                     
 Default value: 0
 ``` |
| ``` TASKREPEAT
 ``` | ``` Optional: Number of repetitions of total output (>=1).                       
 Default value: 0
 ``` |
| ``` SHOWOUTPUT
 ``` | ``` Optional: Decide whether the output file should be shown.
 Default value: 0
 ``` |
| ``` USESELECTION
 ``` | ``` Optional: Decide if use the selection as an input objects for labeling.
 Default value: 0
 ``` |

**Remarks**

```
        '¢ If the current selection in the project should be included in the output of the labeling, then you must use the /USESELECTION parameter.

        '¢ Microsoft Excel application is necessary to run Labeling with output file extension set to .xls (Excel format)

        '¢ When an error occurs during a label operation, a "BaseException" is thrown.

```

**Example**

```
label /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk  /CONFIGSCHEME:config_scheme /FILTERSCHEME:filter_scheme  /SORTSCHEME:sort_scheme /LANGUAGE:en_US /DESTINATIONFILE:C:\temp\labeling.txt /RECREPEAT:3 /TASKREPEAT:2

Use the most recent configuration scheme: The CONFIGSCHEME parameter is not entered. It is empty.

label /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /FILTERSCHEME:filter_scheme /SORTSCHEME:sort_scheme /LANGUAGE:en_US /DESTINATIONFILE:C:\temp\labeling.txt /RECREPEAT:3 /TASKREPEAT:2

Carry out labeling without filtering and sorting: The FILTERSCHEME and SORTSCHEME parameters are not passed in this case.

label /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk  /CONFIGSCHEME:config_scheme /LANGUAGE:en_US /DESTINATIONFILE:C:\temp\labeling.txt /RECREPEAT:3 /TASKREPEAT:2

```