# Interaction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html

---

Base class for special GED interaction.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.Ged.Interaction**  
      [Eplan.EplApi.EServices.Ged.InsertInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction.html)  
      [Eplan.EplApi.EServices.Ged.SelectionInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.SelectionInteraction.html)

Syntax

**C#**



public class Interaction

public ref class Interaction


Example

Here is an example of an Interaction class: Starting an interaction is done by action 'XGedStartInteractionAction' :

**C#**

```
public class MyInteraction : Interaction

{

    public override RequestCode OnStart(InteractionContext oContext)

    {

        return RequestCode.Point;

    }

    public override RequestCode OnPoint(Position oPosition)

    {

        m_arrPoints[m_iPoints] = oPosition.FinalPosition;

        ++m_iPoints;

        if (m_iPoints == 2)

        {

            return RequestCode.Success;

        }

        return RequestCode.Point;

    }

    public override void OnSuccess(InteractionContext oContext)

    {

        Line oLine = new Line();

        oLine.Create(Page, m_arrPoints[0], m_arrPoints[1]);

    }

    private int m_iPoints = 0;

    private PointD[] m_arrPoints = new PointD[2];

}

```

**C#**

```
string strAction = "XGedStartInteractionAction";

ActionManager oActionManager = new ActionManager();

Action oAction = oActionManager.FindAction(strAction);

if (oAction != null)

{

    ActionCallingContext oContext = new ActionCallingContext();

    oContext.AddParameter("Name", "MyInteraction");

    oAction.Execute(oContext);

}

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Interaction Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Description.html) | Description of undo step for this interaction. |
| Public Property | [DraggingMouseCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~DraggingMouseCursor.html) | Mouse cursor which will be used for next dragging operation. |
| Public Property | [InstallationSpace](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~InstallationSpace.html) | Installation space, the editor belongs to. |
| Public Property | [IsAutorestartEnabled](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsAutorestartEnabled.html) | Returns `true`, if interaction should restart after stop. |
| Public Property | [IsInsertInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsInsertInteraction.html) | Returns `true`, if interaction is used to insert one ore more placements on page. |
| Public Property | [IsObjectPlacementModeActive](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsObjectPlacementModeActive.html) | Returns `true`, if special object placement mode is active. |
| Public Property | [IsPlacementFilterActive](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsPlacementFilterActive.html) | If true, then placement-filter is active. |
| Public Property | [IsReadOnly](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsReadOnly.html) | Returns `true`, if function does not change the project database. |
| Public Property | [IsSelectionInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsSelectionInteraction.html) | Returns `true`, if interaction is a helper interaction to select placements. |
| Public Property | [MousePosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~MousePosition.html) | current mouse position |
| Public Property | [Page](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Page.html) | Page, the editor belongs to. |
| Public Property | [Project](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Project.html) | Project, the editor belongs to. |
| Public Property | [PromptForCommandLine](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~PromptForCommandLine.html) | Prompt for command line. |
| Public Property | [PromptForStatusLine](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~PromptForStatusLine.html) | Prompt for status line. |
| Public Property | [RootPlacement3D](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~RootPlacement3D.html) | Root placement to which the editor belongs. |
| Public Property | [StartPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~StartPosition.html) | start position of Interaction. The StartPosition is needed to calculate the current position while ortho mode is active or after input of length or angle the start position is automatically set after point input and before call of OnPoint after start of an interaction StartPosition is null |
| Public Property | [WereLogicalPlacementsChanged](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~WereLogicalPlacementsChanged.html) | Returns true, if logical placements were changed. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [ClearCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~ClearCursor.html) | Remove Cursor-Representation. |
| Public Method | [Dispose](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Dispose().html) | Destructor for deterministic finalization of Interaction object. |
| Public Method | [GetResult](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~GetResult.html) |  |
| Public Method | [IsEnabled](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsEnabled.html) | Returns true, if interaction should be enabled in ribbon |
| Public Method | [OnAngle](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnAngle.html) | Is called after input of an angle by the user. |
| Public Method | [OnCalculateCursorPos](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCalculateCursorPos.html) | Is called to calculate the cursor position. |
| Public Method | [OnCalculateStaticCursorPos](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCalculateStaticCursorPos.html) | Is called to manipulate the position of the static CAD cursor. |
| Public Method | [OnCancel](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCancel.html) | Is called after abort of interaction. |
| Public Method | [OnChar](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnChar.html) | Is called after keyboard inputs by the user. |
| Public Method | [OnCursorMove](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCursorMove.html) | Is called on move of cursor by mouse or keys. |
| Public Method | [OnDeactivate](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnDeactivate.html) | Is called after start of a new interaction with same or higher priority. In this case the current interaction is deactivated until the new interaction stops. |
| Public Method | [OnDrawCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnDrawCursor.html) | Is called to get drawable objects for the cursor representation. |
| Public Method | [OnEdge](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdge.html) | Is called after edged of a 3D mesh was selected by user. |
| Public Method | [OnEdgeBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdgeBelowMouse.html) | Is called after edge was found below the mouse pointer. |
| Public Method | [OnElementFound](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnElementFound.html) | Is called, when the placement below the mouse pointer changes as result of mouse movement. |
| Public Method | [OnEndDrag](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEndDrag.html) | Is called after end of a dragging operation. |
| Public Method | [OnFace](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFace.html) | Is called after face of a 3D mesh was selected by user. |
| Public Method | [OnFaceBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFaceBelowMouse.html) | Is called after face was found below the mouse pointer. |
| Public Method | [OnFilterElement](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFilterElement.html) | Is called by framework to determine if oObject should be included in selection or will be highlighted. |
| Public Method | [OnInputFinish](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnInputFinish.html) | Is called after special input operation has finished. |
| Public Method | [OnLength](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnLength.html) | Is called after input of length. |
| Public Method | [OnMouseLeavingWindow](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnMouseLeavingWindow.html) | Is called after Mouse leave the window. |
| Public Method | [OnPoint](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnPoint.html) | Is called after a point input by user via mouse or keyboard. That means, that the user has clicked into the CAD Window or opened the command line and input the coordinates of a point. |
| Public Method | [OnReactivate](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnReactivate.html) | Is called after stop of the current interaction and this interaction is reactivated. |
| Public Method | [OnRestart](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnRestart.html) | Is called after restart of the interaction. |
| Public Method | [OnReturnFromSubInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnReturnFromSubInteraction.html) | Is called on end of sub-interaction. |
| Public Method | [OnSelect](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSelect.html) | Is called after object selection in the graphical editor by user. |
| Public Method | [OnSpecialEvent](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSpecialEvent.html) | Special event has occurred. Usually caused by user input. |
| Public Method | [OnStart](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStart.html) | Is called after start of interaction |
| Public Method | [OnStartDrag](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStartDrag.html) | Is called after begin of a dragging operation. |
| Public Method | [OnStop](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStop.html) | Is called before an interaction stops. |
| Public Method | [OnSuccess](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSuccess.html) | Is called after successful input of all necessary data as reaction to the request code Success |
| Public Method | [OnVertex](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertex.html) | Is called after vertex of a 3D mesh was selected by user. |
| Public Method | [OnVertexBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertexBelowMouse.html) | Is called after vertex was found below the mouse pointer. |
| Public Method | [SetRubberboxCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetRubberboxCursor.html) | Active Rubber-box cursor. |
| Public Method | [SetRubberlineCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetRubberlineCursor.html) | Active Rubber-line cursor. |
| Public Method | [SetSelection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetSelection.html) | Changes the selection. Should only be used inside the OnSelect() method. |
| Public Method | [SetStaticCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetStaticCursor.html) | Overloaded. Sets [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html), that will be temporary drawn as Cursor Representation. |


