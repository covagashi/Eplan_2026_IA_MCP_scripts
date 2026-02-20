# XMDeleteReprTypeAction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMDeleteReprTypeAction.html

---

```
 Removes a representation type from selected macros and what is stored in a selected directory.

```

| Parameter | Description |
| --- | --- |
| ``` RepresentationType
 ``` | ``` Representation type of macro that should be removed. Value range [0-13];
         0       - Neutral
         1       - MultiLine
         2       - SingleLine
         3       - PairCrossReference
         4       - Overview
         5       - Graphics
         6       - ArticlePlacement
         7       - PI_FlowChart
         8       - Fluid_MultiLine
         9       - Cabling
         10      - ArticlePlacement3D
         11      - Functional
         12      - Planning
         13      - FluidFunctionalOverview
  
 ``` |
| ``` Source
 ``` | ``` Specifies which files should be changed.
  Either a file, a directory name or a pattern must be specified.
  
 ``` |
| ``` Destination
 ``` | ``` Destination directory
  
 ``` |

**Remarks**

```
 The action can only be used interactively.

```

**Example**

```
  XMDeleteReprTypeAction /RepresentationType:0 /Source:c:\macros\*.ema /Destination:c:\dest

```