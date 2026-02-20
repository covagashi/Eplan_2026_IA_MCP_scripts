# InsertInteraction

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction.html

---

Base class for specific interactions that inserts objects.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)  
      **Eplan.EplApi.EServices.Ged.InsertInteraction**

Syntax

**C#**



public class InsertInteraction : Interaction

public ref class InsertInteraction : public Interaction

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [InsertInteraction Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction~_ctor.html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Description.html) | Description of undo step for this interaction. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [DraggingMouseCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~DraggingMouseCursor.html) | Mouse cursor which will be used for next dragging operation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [InsertedItems](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction~InsertedItems.html) | Returns placements inserted by interaction. |
| Public Property | [InstallationSpace](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~InstallationSpace.html) | Installation space, the editor belongs to. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [IsAutorestartEnabled](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsAutorestartEnabled.html) | Returns `true`, if interaction should restart after stop. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [IsInsertInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction~IsInsertInteraction.html) | Overridden. Returns `true`, if interaction is used to insert one ore more placements on page. |
| Public Property | [IsObjectPlacementModeActive](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsObjectPlacementModeActive.html) | Returns `true`, if special object placement mode is active. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [IsPlacementFilterActive](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsPlacementFilterActive.html) | If true, then placement-filter is active. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsReadOnly.html) | Returns `true`, if function does not change the project database. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [IsSelectionInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.InsertInteraction~IsSelectionInteraction.html) | Overridden. Returns `true`, if interaction is a helper interaction to select placements. |
| Public Property | [MousePosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~MousePosition.html) | current mouse position (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [Page](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Page.html) | Page, the editor belongs to. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [Project](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Project.html) | Project, the editor belongs to. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [PromptForCommandLine](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~PromptForCommandLine.html) | Prompt for command line. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [PromptForStatusLine](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~PromptForStatusLine.html) | Prompt for status line. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [RootPlacement3D](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~RootPlacement3D.html) | Root placement to which the editor belongs. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [StartPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~StartPosition.html) | start position of Interaction. The StartPosition is needed to calculate the current position while ortho mode is active or after input of length or angle the start position is automatically set after point input and before call of OnPoint after start of an interaction StartPosition is null (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Property | [WereLogicalPlacementsChanged](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~WereLogicalPlacementsChanged.html) | Returns true, if logical placements were changed. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [ClearCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~ClearCursor.html) | Remove Cursor-Representation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [Dispose()](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~Dispose().html) | Destructor for deterministic finalization of InsertInteraction object. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [GetResult](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~GetResult.html) | (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [IsEnabled](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsEnabled.html) | Returns true, if interaction should be enabled in ribbon (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnAngle](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnAngle.html) | Is called after input of an angle by the user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnCalculateCursorPos](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCalculateCursorPos.html) | Is called to calculate the cursor position. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnCalculateStaticCursorPos](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCalculateStaticCursorPos.html) | Is called to manipulate the position of the static CAD cursor. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnCancel](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCancel.html) | Is called after abort of interaction. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnChar](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnChar.html) | Is called after keyboard inputs by the user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnCursorMove](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnCursorMove.html) | Is called on move of cursor by mouse or keys. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnDeactivate](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnDeactivate.html) | Is called after start of a new interaction with same or higher priority. In this case the current interaction is deactivated until the new interaction stops. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnDrawCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnDrawCursor.html) | Is called to get drawable objects for the cursor representation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnEdge](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdge.html) | Is called after edged of a 3D mesh was selected by user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnEdgeBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEdgeBelowMouse.html) | Is called after edge was found below the mouse pointer. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnElementFound](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnElementFound.html) | Is called, when the placement below the mouse pointer changes as result of mouse movement. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnEndDrag](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnEndDrag.html) | Is called after end of a dragging operation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnFace](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFace.html) | Is called after face of a 3D mesh was selected by user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnFaceBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFaceBelowMouse.html) | Is called after face was found below the mouse pointer. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnFilterElement](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFilterElement.html) | Is called by framework to determine if oObject should be included in selection or will be highlighted. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnInputFinish](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnInputFinish.html) | Is called after special input operation has finished. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnLength](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnLength.html) | Is called after input of length. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnMouseLeavingWindow](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnMouseLeavingWindow.html) | Is called after Mouse leave the window. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnPoint](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnPoint.html) | Is called after a point input by user via mouse or keyboard. That means, that the user has clicked into the CAD Window or opened the command line and input the coordinates of a point. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnReactivate](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnReactivate.html) | Is called after stop of the current interaction and this interaction is reactivated. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnRestart](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnRestart.html) | Is called after restart of the interaction. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnReturnFromSubInteraction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnReturnFromSubInteraction.html) | Is called on end of sub-interaction. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnSelect](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSelect.html) | Is called after object selection in the graphical editor by user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnSpecialEvent](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSpecialEvent.html) | Special event has occurred. Usually caused by user input. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnStart](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStart.html) | Is called after start of interaction (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnStartDrag](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStartDrag.html) | Is called after begin of a dragging operation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnStop](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnStop.html) | Is called before an interaction stops. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnSuccess](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnSuccess.html) | Is called after successful input of all necessary data as reaction to the request code Success (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnVertex](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertex.html) | Is called after vertex of a 3D mesh was selected by user. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [OnVertexBelowMouse](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnVertexBelowMouse.html) | Is called after vertex was found below the mouse pointer. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [SetRubberboxCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetRubberboxCursor.html) | Active Rubber-box cursor. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [SetRubberlineCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetRubberlineCursor.html) | Active Rubber-line cursor. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [SetSelection](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetSelection.html) | Changes the selection. Should only be used inside the OnSelect() method. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |
| Public Method | [SetStaticCursor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~SetStaticCursor.html) | Overloaded. Sets [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html), that will be temporary drawn as Cursor Representation. (Inherited from [Eplan.EplApi.EServices.Ged.Interaction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction.html)) |


