# Position

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position.html

---

This class represents a mouse position.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.EServices.Ged.Position**

Syntax

**C#**



public class Position

public ref class Position


Remarks

The class should be used only by Interaction methods. It cannot be used in a normal Action to determine the mouse position.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Position Constructor](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AdditionalMateSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~AdditionalMateSnapped.html) | Returns true, if additional mate was found. |
| Public Property | [BaseMateSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~BaseMateSnapped.html) | Returns true, if base mate was found. |
| Public Property | [CursorPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~CursorPosition.html) | Position of mouse in the world coordinate system |
| Public Property | [Direction](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~Direction.html) | Direction of the 3D search vector orthogonal to the screen surface |
| Public Property | [FinalPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~FinalPosition.html) | Final Position of CAD Cursor in world coordinates. |
| Public Property | [GridSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~GridSnapped.html) | Returns true, if grid-snap was found. |
| Public Property | [InsertionPointSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~InsertionPointSnapped.html) | Returns true, if InsertionPoint was snapped. |
| Public Property | [MateSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~MateSnapped.html) | Returns true, if PreConnectionSnap was snapped. |
| Public Property | [OnWorkplane](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~OnWorkplane.html) | Returns true, if final position is on work plane. |
| Public Property | [OrthoPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~OrthoPosition.html) | Cursor position considering ortho-mode. |
| Public Property | [PointSnapped](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~PointSnapped.html) | Returns true, if object-snap was found. |
| Public Property | [ScreenPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~ScreenPosition.html) | Position of mouse in the system (Windows) coordinate system. |
| Public Property | [SnapPosition](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~SnapPosition.html) | Position found snap point near mouse position. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~Dispose().html) | Destructor for deterministic finalization of Position object. |
| Public Method | [GetAsString](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~GetAsString.html) |  |
| Public Method | [IsCtrlKeyPressed](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~IsCtrlKeyPressed.html) | Returns true, if ctrl key was pressed at the moment, when position was stored. |
| Public Method | [IsShiftKeyPressed](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~IsShiftKeyPressed.html) | Returns true, if shift key was pressed at the moment, when position was stored. |
| Public Method | [SetFromString](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~SetFromString.html) |  |



Public Operators

|  |  |
| --- | --- |
| public Operator [Assign](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~op_Assign.html) | Assignment constructor. |
| public Operator [Implicit Type Conversion](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Position~op_Implicit.html) | Overloaded. Used in conversion from [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html) to the `Position` object. |


