# Interactions

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Interactions.html

---

In the Eplan API, the term "**interactions**" refers to classes that are used to handle events related to interactive work in the GED (graphical editor).

The mechanism of interactions is mostly based on the  XGedStartInteractionAction  action, which is called by the Eplan framework when moving, adding or selecting an object in the GED. For example, when inserting a window macro on a page, the Eplan framework calls the action:

```


XGedStartInteractionAction /Name:XMIaInsertMacro

```

Its parameter  Name  is used to pass the name of an interaction.

Usually, interactions are used for 2 purposes: creating custom ones or overriding the default (system).

Please note that interactions work only in the context of the currently open page or layout space (InstallationSpace  in API). So it is not possible to handle events from other windows, like navigators. Also, when leaving the current page, the interaction is aborted by default (i.e. the  OnCancel  method is called).

### Creating custom interactions

The Eplan API enables programmers to create their own custom interactions.

```csharp
public class DeleteTerminalsInteraction : Interaction
 {
    public override RequestCode OnStart(InteractionContext pContext)
    {
       // The interaction has been stated.
       // Set the initial state
       m_state = State.Start;
       // Activate the placement filter
       IsPlacementFilterActive = true;
       // Request point and set prompt for user
       this.PromptForStatusLine = "select Terminals";
       return  RequestCode.Select;
   }
   // Can be used to filter for selection or for highlight
   public override bool OnFilterElement(StorableObject placement)
   {
      if (placement is Terminal)
      {
         return true;
      }
      return false;
    }
    public override RequestCode OnSelect(StorableObject[] placements, SelectionContext context)
    {
       m_Terminals = placements.Cast<Terminal>().ToArray();
       m_state = State.Select;
       return RequestCode.Success;
    }
    public override void OnSuccess(InteractionContext result)
    {
       if (m_state == State.Select)
       {
          for (int i = 0; i < m_Terminals.Length; i++)
          {
             m_Terminals[i].Remove();
          }
       }
    }
    enum State
    {
       Start = 0,
       Select,
    };
 
    State m_state;
    Terminal[] m_Terminals;
 }

```

To add an interaction to Eplan, it must be included in an API add-in or add-on. The interaction is registered under the name of its class when the API add-in containing it is loaded.

There is also a special class  InsertInteraction  for interactions that insert objects on a page. It contains an additional property showing a placed object.

### Deriving interactions

The programmer can derive a new interaction from an existing one in order to inherit its functionality. In this case, there should be the  Interaction  attribute set with  Name

as the name of the new interaction,  NameOfBaseInteraction  as the name of the existing interaction to be hinherited. Also the  Ordinal  number must be set to a value higher than 30.

The following example shows how to create a new interaction derived from a standard symbol insertion interaction:

```csharp
[Interaction(Name = "DerivedSymbolInsertInteraction", NameOfBaseInteraction = "XEGedIaInsertSymRef", Ordinal = 50)]
     class DerivedSymbolInsertInteraction : InsertInteraction
     {
         public override RequestCode OnStart(InteractionContext pContext)
         {
             return base.OnStart(pContext);
         }
         public override void OnSuccess(InteractionContext result)
         {
             // Execute standard operation of symbol insert interaction
             base.OnSuccess(result);
 
             // Set property of inserted function
             Placement[] placements = InsertedItems as Placement[];
             for (int i = 0; i < placements.Length; i++)
             {
                 Function f = (Function)placements[i];
                 if (f != null)
                 {
                     f.Properties[Properties.Function.FUNC_TEXT] = "API_Demos : DerivedSymbolInsertInteraction";
                 }
             }
         }
     }
```

### Overriding default interactions

API interactions can also override default Eplan interactions. This way the execution will be passed to a user code instead of the Eplan core. As with derived interactions, such interactions must also be derived from the  Interaction  class. The only change that must be made is in the  Interaction  attribute, i.e both  Name  and  NameOfBaseInteraction  must be set to the same base interaction:

```


[Interaction(Name = "XEGedIaInsertSymRef", NameOfBaseInteraction = "XEGedIaInsertSymRef", Ordinal = 50)]

```

This way, all events connected with the default interaction (i.e inserting a symbol in this case) are routed to the core interaction  XEGeIaInsertSymRef.

### Getting feedback from the GED

Most of the interaction methods return a [Eplan::EplApi::EServices::Ged::RequestCode](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.RequestCode.html) which is used to control the workflow of an interaction. The default implementation of the  Interaction::OnStart  method returns  RequestCode::Success, which causes the interaction to end. If it is overridden and returns  RequestCode::Point, the interaction remains active and when the user clicks the mouse button, the Interaction::OnPoint method is called by Eplan.
