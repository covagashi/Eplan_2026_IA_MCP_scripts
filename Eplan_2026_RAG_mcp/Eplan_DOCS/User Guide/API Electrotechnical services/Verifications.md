# Verifications

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Verifications.html

---

You can use an Eplan API add-in to add new verifications (in GUI called "**check runs**"). Eplan will use them in the same way as already existing internal verifications.

For a new verification, the add-in must  implement the  IVerification  interface.

```csharp
public class NewVerification : Eplan.EplApi.EServices.Verification
 {
     private int m_iMessageId = 30;
 
     /// <summary>
     /// Default constructor.
     /// </summary>
     public NewVerification()
     {
     }
 
     /// <summary>
     /// This function implements the test logic. 
     /// </summary>
     /// <param name="oObject1">
     /// This object is tested. One can be certain that here only
     /// function objects of the desired category arrive here.
     /// </param>
     public override void Execute(Eplan.EplApi.DataModel.StorableObject oObject1)
     {
         DoErrorMessage(oObject1, oObject1.Project, "Verification dynamic text");
     }
 
     /// <summary>
     /// This function is called after end of all verifications run.
     /// </summary>
     public override void OnEndInspection()
     {
         // TODO:  Add NewVerification.OnEndInspection implementation
     }
 
     /// <summary>
     /// Registration function of the verification
     /// </summary>
     /// <param name="strName">
     /// Under this name, the new verification registered  in the system.
     /// </param>
     /// <param name="iOrdinal">
     /// Overload priority
     /// </param>
     public override void OnRegister(ref string strName, ref int iOrdinal)
     {
         strName = "NewVerification";
         iOrdinal = 30;
         this.VerificationPermission = IVerification.Permission.OnlineOfflinePermitted;
         this.VerificationState = IVerification.VerificationState.OnlineOfflineState;
     }
 
     /// <summary>
     /// This function is called before start of all verifications run.
     /// </summary>
     /// <param name="bOnline">
     /// true: online verification
     /// false: offline verification
     /// </param>
     public override void OnStartInspection(bool bOnline)
     {
         // TODO:  Add NewVerification.OnStartInspection implementation
     }
 
     /// <summary>
     /// This function must deliver the accompanying message text. 
     /// A test has always exactly one accompanying message text. 
     /// </summary>
     /// <returns>The message text</returns>
     public override string GetMessageText()
     {
         return "Verification static text . %1!s!";
     }
 
     /// <summary>
     /// This function is called when the aid text is supposed to be indicated in a message. 
     /// It lies in the responsibility of the implementation of the function to call
     /// the suitable aid system in the correct language.
     /// In the simplest case, for example only a simple dialog can be called. 
     /// </summary>
     public override void DoHelp()
     {
         // TODO:  NewVerification.DoHelp implementation
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
         strCreator = "Author";
         eRegion = IMessage.Region.Externals;
         iMessageId = m_iMessageId;
         eClassification = IMessage.Classification.Error;
         iOrdinal = 20;
     }
 }

```

In order to simplify the creation of a verification, the Eplan API has some base classes that provide some service functions.

These base classes are:

- FunctionVerification
- PotentialVerification
- InterruptionPointVerification
- PartVerification

In your add-in, simply have your verification class inherit from one of these base classes and implement the necessary interface functions. For outputting messages, several variations of the  AddMessage()  function are available. In addition, the classes contain some functions for finding cross-referenced objects.

If you want to implement a verification that cheks something about potentials, then you implement a new verification derived from  PotentialVerification. In the  Execute  function of your new verification, you can use the  GetAllPotentialsWithSameName()  function to get the potential from the verification cache. It makes no sense to call this function in any other context than in the Execute()  verification.

All registered verifications are called by the system using Check project.... If you want to execute only your verification, you have to configure the check settings (create new scheme, disable other verifications (Type of check: "No")).

Please take into account that compared to 1.9 version, verifications inheriting from the  Verification  class must have the  override  keyword in the base methods definitions. This is required since the API extension has been migrated to C++/CLI .

### How to start a verification

Verifications can be invoked from API or GUI in 3 modes:

- **Online mode** ' This is called when a change was done and the  UndoStep  was disposed:

```csharp
using (UndoStep oUndo = new UndoManager().CreateUndoStep())
 {
     oFunction.Location = new PointD(oFunction.Location.X + 10.0, oFunction.Location.Y + 10.0);
 }

```

- **Prevent errors mode** (restrictive mode) ' This is similar to the online mode, but if  DoErrorMessage()  is called, the last  UndoStep  is automatically undone, so the last changes are reverted. For the "Prevent errors mode" you should set the following options in the  OnRegister  method of the verification:

```csharp
this.VerificationPermission = IVerification.Permission.RestrictivePermitted;
 this.VerificationState = IVerification.VerificationState.RestrictiveState;

```

- **Offline mode** ' This can be done using:
  - the  check  action
  - the  Check  class (VerifyProject  and  VerifyPages  methods)
  - the Check project dialog for project verification and the Parts management dialog for parts verification

For more detailed information on parts verifications, please take a look at the [Verifying parts](file:///U:/EplanW3_master/Eplan/Extensions/API_Documentation/DocumentX/VerifyingParts.html) chapter.
