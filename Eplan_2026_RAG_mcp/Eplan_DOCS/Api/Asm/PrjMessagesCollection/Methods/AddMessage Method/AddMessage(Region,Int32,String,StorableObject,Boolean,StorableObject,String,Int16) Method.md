# AddMessage(Region,Int32,String,StorableObject,Boolean,StorableObject,String,Int16) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1300.html

---

Adds a new message to the database with electrotechnical messages (Project data\Messages\Management). Any existing message from the system can be added as well as messages registered by an add-in.

Syntax

**C#**



public ProjectMessage AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   string strErrTextParam,

   StorableObject oObject1,

   bool bImmediateShow,

   StorableObject oObject2,

   string strAdditionalInfo

)

public:

ProjectMessage^ AddMessage( 

   IMessage.Region eRegion,

   int nErrNr,

   String^ strErrTextParam,

   StorableObject^ oObject1,

   bool bImmediateShow,

   StorableObject^ oObject2,

   String^ strAdditionalInfo

)


#### Parameters

*eRegion*
:   A message of this [IMessage.Region](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IMessage+Region.html) is added.

*nErrNr*
:   A message with this message number is added.

*strErrTextParam*
:   reference to a parameterstring to substitute placeholders in the resource error text. Multiple parameters must be separated with "|". In the error text parameters should be signed by "%1!s!", "%2!s!" etc. If the error text doesn't have any parameter to substitute strErrTextParam must be an empty string

*oObject1*
:   The message refers to this object. Optional parameter; can also be NULL.

*bImmediateShow*
:   True: The message is immediately displayed in the message window.

*oObject2*
:   A second object to which this message also refers. Optional parameter; can also be NULL.

*strAdditionalInfo*
:   Additional language\-independent message text. Is saved as specified in the database. Optional parameter; this string may also be empty.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentException](#) | Thrown when `eRegion` is ePRJMSG\_REGION\_UNKNOWN. |

Remarks

In order to add an error message to the system messages list, please refer to the method [Eplan.EplApi.Base.BaseException.FixMessage](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~FixMessage.html).

Example

The following example shows how to append the new message 999025 to the message database of the current project.

**C#**

```


    PrjMessagesCollection oPrjMessagesCollection = new PrjMessagesCollection(m_oTestProject);

    if (m_oTestProject == null)

{

    ProjectManager oProjManager = new ProjectManager();

    m_oTestProject = oProjManager.CurrentProject;

}

    if (m_oTestProject != null)

{

    Page[] arrPages = m_oTestProject.Pages;

    Function[] arrFunction = arrPages[5].Functions;

    StorableObject oObject1 = arrFunction[0];

    StorableObject oObject2 = arrFunction[1];

    ProjectMessage oProjectMessage = oPrjMessagesCollection.AddMessage(Eplan.EplApi.EServices.IMessage.Region.Externals, 25, "XYZ", oObject1, false, oObject2, "Additional Text");

    Console.WriteLine(" Addded message " + oProjectMessage.GetText() + " to the project");

}

```
