# Execute Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html

---

Called by EPLAN when a specific object is to be checked. Implements the "check."

Syntax

**C#**



void Execute( 

   StorableObject oObject1

)

void Execute( 

   StorableObject^ oObject1

)


#### Parameters

*oObject1*
:   This object is to be checked.

Example

The following example shows a method to prevent creating rectangle on page with plant "ETH". This is an example of verification with type - prevent. The error message will not be added into message dialog but message box will be displayed and creation of rectangle will be automatically canceled.

**C#**

```
public override void Execute(Eplan.EplApi.MasterData.MDPartsDatabaseItem oItem)

{

    if (this.VerificationState == IVerification.VerificationState.RestrictiveState)

    {

        Rectangle oRectangle = oObject as Rectangle;

        if (oRectangle != null)

        {

            if (oRectangle.Page != null)

            {

                if (oRectangle.Page.Properties.DESIGNATION_FULLPLANT == "ETH")

                {

                    DoErrorMessage(oRectangle, oRectangle.Page.Name);

                }

            }

        }

    }

}
```
