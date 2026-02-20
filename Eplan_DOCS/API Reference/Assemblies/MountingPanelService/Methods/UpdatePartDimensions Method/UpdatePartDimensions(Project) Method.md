# UpdatePartDimensions(Project) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~UpdatePartDimensions(Project).html

---

Transfers dimensions from articles to article placements. Corresponds to the 'Devices -> 2D panel layout -> Navigator -> Update part dimensions' ribbon item.

Syntax

**C#**



public Function[] UpdatePartDimensions( 

   Project prj

)

public:

array<Function^>^ UpdatePartDimensions( 

   Project^ prj

)


#### Parameters

*prj*
:   A project to update article placements in.

#### Return Value

An array of modified article placements.
