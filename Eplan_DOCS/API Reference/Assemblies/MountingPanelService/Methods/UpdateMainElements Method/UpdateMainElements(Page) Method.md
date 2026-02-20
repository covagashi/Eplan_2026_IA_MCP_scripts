# UpdateMainElements(Page) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.MountingPanelService~UpdateMainElements(Page).html

---

Transfers part references of all part placements on the page to main functions. Corresponds to the 'Devices -> 2D panel layout -> Navigator -> Update main elements' ribbon item.

Syntax

**C#**



public Function[] UpdateMainElements( 

   Page page

)

public:

array<Function^>^ UpdateMainElements( 

   Page^ page

)


#### Parameters

*page*
:   A panel layout page to update main functions from.

#### Return Value

An array of modified main functions.
