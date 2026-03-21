# GetSelectedPartDatabaseItems Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPartsManagement~GetSelectedPartDatabaseItems.html

---

Gets the selected PartItem(s) in the parts management (or parts navigator)

Syntax

**C#**



public MDPartsDatabaseItem[] GetSelectedPartDatabaseItems( 

   bool bRecursive

)

public:

array<MDPartsDatabaseItem^>^ GetSelectedPartDatabaseItems( 

   bool bRecursive

)


#### Parameters

*bRecursive*
:   decide if all items below a node will be returned (bRecursive=true), or only the first leave in the tree (like the selection of the parts managemnt GUI) (bRecursive=false) ( Set bRecursive=true to get the behavior of the old property SelectedParDatabaseItems

Remarks

In the parts navigator only MDParts can be selected. In parts management dialog also MDConstruction, MDAddress and MDConnectionPointInfo are available
