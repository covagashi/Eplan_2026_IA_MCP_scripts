# XMIaInsertMacro

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMIaInsertMacro.html

---

Imports a macro to the current project.

| Parameter | Description |
| --- | --- |
| ``` filename ``` | ``` Filename of macro that should be inserted. If this parameter is empty, a file selection dialog opens. ``` |
| ``` variant ``` | ``` Variant of macro that should be inserted. Value range [0-15];                                         0  - variant A                                         1  - variant B                                         2  - variant C                                         3  - variant D                                         4  - variant E                                         5  - variant F                                         6  - variant G                                         7  - variant H                                         8  - variant I                                         9  - variant J                                         10 - variant K                                         11 - variant L                                         12 - variant M                                         13 - variant N                                         14 - variant O                                         15 - variant P   ``` |
| ``` RepresentationType ``` | ``` Representation type of macro that should be inserted. Value range [1-13]                                         1 - MultiLine                                         2 - SingleLine                                         3 - PairCrossReference                                         4 - Overview                                         5 - Graphics                                         6 - ArticlePlacement                                         7 - PI_FlowChart                                         8 - Fluid_MultiLine                                         9 - Cabling                                         10 - ArticlePlacement3D                                         11 - Functional                                         12 - Planning                                         12 - FluidFunctionalOverview   ``` |
| ``` AskForNumeration ``` | ``` Specifies whether to display or suppress a dialog asking for the numeration (optional).  Possible values are: true = show dialog asking for the numeration (default value), false = suppress asking for numeration   ``` |
| ``` NumberModus ``` | ``` Numeration mode (optional).  Possible values are: 0 = don't modify, 1 = number, 2 = number using flag "?", 3 or -1 = show dialog asking for the numeration mode   ``` |
| ``` RenumberPrefixes ``` | ``` Specifies whether to renumber the prefixes (optional). Can only be set if "NumberModus" = 1.  Possible values are: true = renumber prefixes, false = don't renumber prefixes (default value)   ``` |

**Example**

```
XGedStartInteractionAction /Name:XMIaInsertMacro /filename:"?"
```