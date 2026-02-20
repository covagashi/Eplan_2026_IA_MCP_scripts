# Execute Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IPartVerification~Execute.html

---

Called by EPLAN when a specific MDPartsDatabaseItem is to be checked. Currently only MDPart objects are passed to this method. Implements the "check."

Syntax

**C#**



void Execute( 

   MDPartsDatabaseItem oMDPartItem

)

void Execute( 

   MDPartsDatabaseItem^ oMDPartItem

)


#### Parameters

*oMDPartItem*
:   This MDPartsDatabaseItem will be checked.

Example

The following example shows a method to check if part has empty ERP number. The error message will be added into message dialog.

**C#**

```
public override void Execute(Eplan.EplApi.MasterData.MDPartsDatabaseItem oMDPartItem)

{

	MDPart oPart = oMDPartItem as MDPart;

	if (oPart != null)

	{

		if (oPart.Properties.ARTICLE_ERPNR.IsEmpty)

		{

			DoErrorMessage(oPart.PartNr);

		}                

	}

}
```
