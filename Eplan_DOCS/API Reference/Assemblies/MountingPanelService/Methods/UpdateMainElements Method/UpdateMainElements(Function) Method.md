# UpdateMainElements(Function) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~UpdateMainElements(Function).html

---

Transfers part references of a part placement to the corresponding main function. Corresponds to the 'Devices -> 2D panel layout -> Navigator -> Update main elements' ribbon item.

Syntax

**C#**



public Function[] UpdateMainElements( 

   Function funcArticlePlacement

)

public:

array<Function^>^ UpdateMainElements( 

   Function^ funcArticlePlacement

)


#### Parameters

*funcArticlePlacement*
:   The article placement to update from.

#### Return Value

An array of modified main functions.
