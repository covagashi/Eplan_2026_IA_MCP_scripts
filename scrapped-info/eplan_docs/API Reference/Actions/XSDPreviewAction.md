# XSDPreviewAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XSDPreviewAction.html

---

```
 Opens or closes the preview of a project page or macro

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Name of the project. If the path is missing, the default value is used (see $(MD_PROJECTS))
 ``` |
| ``` PAGENAME
 ``` | ``` Name of page as string
 ``` |
| ``` MACRONAME
 ``` | ``` Complete path to a window or page macro (with extension). If the path is missing, the default value is used (see $(MD_MACROS))
 ``` |
| ``` SHOW
 ``` | ``` 1: The preview of the page/macro will be opened.
                 0: The preview will be closed.
 ``` |

**Remarks**

```
 If PAGENAME and MACRONAME are empty, all pages of the project will be displayed in the preview

```

**Example**

```
 Preview of a page:

 XSDPreviewAction /PROJECTNAME:EPLAN_Sample_Project /PAGENAME:=CA1+EAA/1

 XSDPreviewAction /PROJECTNAME:"C:\\Users\\Public\\EPLAN\\Electric P8\\Projects\\EPLAN\\EPLAN_Sample_Project" /PAGENAME:=CA1+EAA/2

 Preview of a window macro:

 XSDPreviewAction /PROJECTNAME:EPLAN_Sample_Project /MACRONAME:Macro_0001.ema

 XSDPreviewAction /PROJECTNAME:$(MD_PROJECTS)\\EPLAN_Sample_Project /MACRONAME:$(MD_MACROS)\\Macro_0001.ema

```