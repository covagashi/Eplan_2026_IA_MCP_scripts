# Throwing and catching exceptions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ThrowingAndCatchingExceptions.html

---

Error handling in Eplan is preferably done using exceptions. The API framework provides the  BaseException  base class that provides you access to the error handling of Eplan.

If an exception object of this type is thrown, the Eplan framework catches the exception and writes the data to the system error management or shows the error message in the Eplan error dialog.

**C#**
```csharp
Eplan.EplApi.Base.BaseException exc2= new Eplan.EplApi.Base.BaseException(

                                                "Error from CSharpAction thrown as exception",

                                                Eplan.EplApi.Base.MessageLevel.Error);

throw exc2;

                                                  Eplan.EplApi.Base.MessageLevel.Error)

Throw exc2
```

Of course, you can also catch exceptions in your API application and evaluate them, e.g. to display your own error message.

**C#**
```csharp
// Test wrong settings name (throws BaseException that is handled here)

try

{

    String strGuiLanguage= Settings.GetStringSetting("USER.SYSEM.GUI.LANGUAGE", 0);

    new Decider().Decide(EnumDecisionType.eOkDecision, "The current GUI language is: "+ strGuiLanguage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

catch (BaseException exc)

{

    String strMessage= exc.Message;

    new Decider().Decide(EnumDecisionType.eOkDecision, "Exception: " + strMessage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

}

Try

   dec.Decide(EnumDecisionType.eOkDecision, "The current GUI language is: "+  strGuiLanguage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)

   dec.Decide(EnumDecisionType.eOkDecision, "Exception: " + strMessage, "", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
```