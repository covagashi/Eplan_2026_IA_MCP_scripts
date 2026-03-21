# Verifying parts

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/VerifyingParts.html

---

You can create your own parts verification (in GUI called "**check run**") and integrate it into the system.

To do this, you first need to create a class that implements these interfaces:

- Eplan.EplApi.EServices.PartVerification
- Eplan.EplApi.EServices.IVerificationBase
- Eplan.EplApi.EServices.IMessage

The actual check logic can be implemented in the  Execute  method. The messages generated during a parts check run are stored in the message database, and displayed in the Parts management dialog > tab Messages.

The check logic in the  Execute  method can be adapted to your requirements. You can access and verify all kind of information a part provides. For example you could test if the part numbers correspond to a specific pattern, if the short name of the manufacturer has the correct length or if the part image file is corrupted.

The  OnStartInspection  method and the  OnEndInspection  method allow you to specify what should be executed at the start and end of the check run.

In order to use it, the check run must be registered / loaded in Eplan. It can then be executed for selected parts or all parts in various ways:

- via the  check  action
- via the  Check  class:  VerifyMDPartsDatabaseItems  method
- in GUI using the Parts management dialog > context menu > Check project

For further information on verifications, please take a look at the [Verifications](Verifications.html) chapter. In the example below, an error message is created if the ERP number is not empty:

```csharp
public class ERPNumberFoundVerification : Eplan.EplApi.EServices.PartVerification, Eplan.EplApi.EServices.IVerificationBase, Eplan.EplApi.EServices.IMessage
 {
     private int m_iMessageId = 530;
 
     /// <summary>
     /// Default constructor
     /// </summary>
     public ERPNumberFoundVerification()
     {
         // TODO: Add constructor logic here
     }
 
     #region IVerification Members
 
     /// <summary>
     /// This function implements the test logic. 
     /// </summary>
     /// <param name="oObject1">
     /// This object is tested. One can be certain that only
     /// function objects of the desired category arrive here.
     /// </param>
     public override void Execute(Eplan.EplApi.MasterData.MDPartsDatabaseItem oMDPartItem)
     {
         if (oMDPartItem == null)
             return;
 
         MDPart part = oMDPartItem as MDPart;
         if (part == null)
             return;
        
         if (!part.Properties.ARTICLE_ERPNR.IsEmpty)
         {
             string message = part.Properties.ARTICLE_ERPNR.ToString();
             if (!string.IsNullOrEmpty(message))
             {
                 DoErrorMessage(oMDPartItem.Properties.ARTICLE_PARTNR, oMDPartItem.Properties.ARTICLE_VARIANT, message);
             }
         }
     }         
 
     /// <summary>
     /// Registration function of the verification
     /// </summary>
     /// <param name="strName">
     /// Under this name, the new verification is registered in the system.
     /// </param>
     /// <param name="iOrdinal">
     /// Overload priority 
     /// </param>
     public override void OnRegister(ref string strName, ref int iOrdinal)
     {
         strName = "ERPNumberFoundVerification";
         iOrdinal = 30;
     }
 
     /// <summary>
     /// This function is called before the start of all verification runs.
     /// </summary>
     /// <param name="bOnline">
     /// true: online verification
     /// false: offline verification
     /// </param>
     public override void OnStartInspection(bool bOnline)
     {
         // TODO: Add logic to execute before the start of the verification here
     }
 
     /// <summary>
     /// This function is called after the end of all verification runs.
     /// </summary>
     public override void OnEndInspection()
     {
         // TODO: Add logic to execute after the end of the verification here
     }
 
     #endregion // #region IVerification Members
 
     #region IMessage Members
 
     /// <summary>
     /// This function must deliver the accompanying message text. 
     /// A test has always exactly one accompanying message text. 
     /// </summary>
     /// <returns>The message text</returns>
     public override string GetMessageText()
     { 
         ResourcesCulture.UseGuiLanguage();
         return Resources.IDS_ERP_NUMBER_FOUND;
     }
 
     /// <summary>
     /// This function is called if to a message the aid text is supposed to be indicated. 
     /// It lies in the responsibility of the implementation of the function to call
     /// the suitable aid system in the correct language.
     /// In the simplest case, for example only a simple dialog can be called. 
     ///</summary>
     public override void DoHelp()
     {
         // TODO: Add implementation of ERPNumberFoundVerification.DoHelp here
     }
 
     /// <summary>
     /// This function is called of the system if the message of this test
     /// is supposed to be registered in the system. 
     /// </summary>
     /// <param name="strCreator">Creator of the message</param>
     /// <param name="eRegion">Message region</param>
     /// <param name="iMessageId">Number of the message</param>
     /// <param name="eClassification">Default classification</param>
     /// <param name="iOrdinal">Overload priority</param>
     public override void OnRegister(ref String strCreator, ref Eplan.EplApi.EServices.IMessage.Region eRegion, ref int iMessageId, ref Eplan.EplApi.EServices.IMessage.Classification eClassification, ref int iOrdinal)
     {
         strCreator = "de.eplan";
         eRegion = IMessage.Region.PartMasterData;
         iMessageId = m_iMessageId;
         eClassification = IMessage.Classification.Warning;
         iOrdinal = 20;
     }
 
     #endregion // #region IMessage Members
 }
```
