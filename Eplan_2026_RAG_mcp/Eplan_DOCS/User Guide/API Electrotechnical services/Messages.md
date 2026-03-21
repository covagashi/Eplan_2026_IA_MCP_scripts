# Messages

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Messages.html

---

As an API developer, you can add new electrotechnical messages to Eplan and write them to the message management.

In order to create a new message, add a class to your project that inherits from the Eplan.EplApi.EServices.Message class.

The  Eplan.EplApi.EServices.Message class declares 3 functions:

1. The parameters of the  OnRegister()  function define the properties of the message and how it is registered in Eplan.
2. The  GetMessageText()  function returns the message text that is displayed in dialogs if requested by Eplan.
3. The  DoHelp()  function is called by the system if Eplan requests help on the message.

**C#**
```csharp
public class Message1 : Eplan.EplApi.EServices.Message

{

    public override void OnRegister(ref string creator, ref IMessage.Region eRegionId, ref int iMessageId,

      ref IMessage.Classification eClassification, ref int iOrdinal)

    {

        creator = "Creator name";

        eRegionId = IMessage.Region.Externals;

        iMessageId = 25;

        eClassification = IMessage.Classification.Error;

        iOrdinal = 20;

        return;

    }

    public override System.String GetMessageText()

    {

        // TODO: Provide text from resource in active GUI language

        return "Message text for %1!s! from Eplan.EplAddIn.Demo.Messages";

    }

    public override void DoHelp()

    {

        new Decider().Decide(EnumDecisionType.eOkDecision, "DoHelp was called!", "Eplan.EplAddIn.Demo.Messages", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);

        // TODO: activate help for this message

    }

}

Public Class Message1

   Implements Eplan.EplApi.EServices.Message

                          Implements Eplan.EplApi.EServices.IMessage.OnRegister

      creator = "Creator name"

      eRegionId = IMessage.Region.Externals

      iMessageId = 25

      eClassification = IMessage.Classification.Error

      iOrdinal = 20

      Return

   Public Function GetMessageText() As System.String Implements Eplan.EplApi.EServices.IMessage.GetMessageText

      Return "Message text for %1!s! from Eplan.EplAddIn.Demo.Messages"

      dec.Decide(EnumDecisionType.eOkDecision, "DoHelp was called!", "Eplan.EplAddIn.Demo.Messages", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK)
```

It is also possible to create such classes automatically using the Eplan API Add-in Wizard.

### Adding a new message

A registered message can be now added to the message management of Eplan using the PrjMessagesCollection class.

**C#**
```csharp
var projectMessageCollection = new PrjMessagesCollection(myProject);

IMessage.Region region = IMessage.Region.Externals;

int messageId = 25;

var storableObject1 = myProjectPage.Functions[0] as StorableObject;

var storableObject2 = myProjectPage.Functions[1] as StorableObject;

//Add new message using AddMessage method

projectMessageCollection.AddMessage(

    region,

    messageId,

    "param text 1",

    storableObject1,

    true,

    storableObject2,

    "additional info 2");

//or using BaseProjectMessage class

var newMessage = new BaseProjectMessage(region, messageId, "param text 2", "BECK.BK3100", "additional info 2");

projectMessageCollection.Add(newMessage);

projectMessageCollection.AddMessage(region, messageId, "param text 1", storableObject1, True, storableObject2, "additional info 2")

projectMessageCollection.Add(newMessage)
```

### Overriding the text of an existing message

It is **not** possible to change an existing verification by overriding it via API (by setting the same name and a higher Ordinal number). However, you can override an existing message and change the default message text to your own text. You need to implement a message with the same iMessageId and eRegion, but use a higher  iOrdinal, e.g. 50. Other properties of the message will not be affected.

The following example shows how to override the existing message 007005 "Device without main function.":

```csharp
/// This function returns the message text.
 /// One verification needs always exactly one message text
 public string GetMessageText()
 {
    return "This device has absolutely no main function!!!!";
 }
 
 /// This is the registration function of the message belonging to the verification.
 /// Parameters:
 ///   message region
 ///   message number
 ///   classification: error, message or info.
 ///   overload priority
 public void OnRegister(ref String strCreator, ref Eplan.EplApi.EServices.IMessage.Region eRegion, ref int iMessageId, ref Eplan.EplApi.EServices.IMessage.Classification eClassification, ref int iOrdinal)
 {
    strCreator = "de.Eplan.Demo";
    eRegion = IMessage.Region.Devices;
    iMessageId = 5;
    eClassification = IMessage.Classification.Error;
    iOrdinal = 50; // Higher than 20
 }
```
