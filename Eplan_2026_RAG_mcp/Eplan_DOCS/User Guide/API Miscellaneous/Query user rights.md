# Query user rights

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/QueryUserRights.html

---

Eplan can link user interactions with specific rights. This is done by the Eplan rights management module. If this module is not available or not licensed, the rights management is not active in Eplan. The following screenshot shows the Rights management dialog with a list of rights.

In your API application, you can find out, whether the rights management module is active and you can query the status of a given user right. The following example checks the user right for "XPLEditorStart", using the  checkUserRights  and the  checkRightFor  method.

**C#**
```csharp
UserRights oUserRights = new UserRights();

bool bRights = oUserRights.CheckUserRights();

if (bRights)

{

     bool bAnRight= oUserRights.CheckRightFor("XPLEditorStart");

     if (bAnRight)

     {

       new Decider().Decide(EnumDecisionType.eOkDecision, "You have the right to call XPLEditorStart!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

     }

     else

     {

       new Decider().Decide(EnumDecisionType.eOkDecision, "You don't have the right to call XPLEditorStart!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

     }

}

else

{

    new Decider().Decide(EnumDecisionType.eOkDecision, "This application works without rights management!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

      dec.Decide(EnumDecisionType.eOkDecision, "You have the right to call XPLEditorStart!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)               

   Else

      dec.Decide(EnumDecisionType.eOkDecision, "You don't have the right to call XPLEditorStart!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)             

Else

   dec.Decide(EnumDecisionType.eOkDecision, "This application works without rights management!", "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
```

For information about the rights available in Eplan and about their assignment to the users, please refer to the Rights management dialog. You cannot add new user rights via API.