# Add Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.PrjMessagesCollection~Add.html

---

Adds an item to the `PrjMessagesCollection`.

Syntax

**C#**



public virtual void Add( 

   BaseProjectMessage item

)

public:

virtual void Add( 

   BaseProjectMessage^ item

)


#### Parameters

*item*
:   The object to add to the `PrjMessagesCollection`.

Exceptions

| Exception | Description |
| --- | --- |
| [System.NotSupportedException](#) | The `PrjMessagesCollection` is read-only. |

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
