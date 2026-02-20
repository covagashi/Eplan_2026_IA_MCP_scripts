# GridMate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate.html

---

Represents grid mate.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)  
      **Eplan.EplApi.DataModel.E3D.GridMate**

Syntax

**C#**



public class GridMate : Mate

public ref class GridMate : public Mate


Remarks

GridMate object is only a container of information, that describes the grid (like size, increment, start position, etc) but 3d objects will snap only on a GridLineMate objects.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [GridMate Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~_ctor().html) |  |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Description](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Description.html) | Description of this mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [IncrementX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~IncrementX.html) | Increment in X direction |
| Public Property | [IncrementY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~IncrementY.html) | Increment in Y direction |
| Public Property | [IsBaseMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsBaseMate.html) | Return true, if mate is base mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsReadOnly.html) | Determines if Mate can be modified. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [IsUserDefined](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~IsUserDefined.html) | Returns true, if mate is used defined. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [LengthX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~LengthX.html) | Number of cells in X direction |
| Public Property | [LengthY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~LengthY.html) | Number of cells in Y direction |
| Public Property | [MatchingMateNames](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~MatchingMateNames.html) | Names of mates that can be snapped to this one separated by '#'. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Name.html) | Name of this mate. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Placement.html) | [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) to which this mate is assign. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [Rotation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Rotation.html) | Angle by which the components are to be rotated when they are placed on the mounting point. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [RotationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~RotationType.html) | Rotation type which this mate force while snapping. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [SizeX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~SizeX.html) | Grid size, X coordinate |
| Public Property | [SizeY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~SizeY.html) | Grid size, Y coordinate |
| Public Property | [Source](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Source.html) | Returns object from which the mate was returned or changed by: Placement3D.GetTargetMates, Placement3D.GetSourceMates, Placement3D.AddMatePersistent or BaseMate property. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Property | [StartPositionX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~StartPositionX.html) | Start position in X direction |
| Public Property | [StartPositionY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.GridMate~StartPositionY.html) | Start position in Y direction |
| Public Property | [Transformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transformation.html) | Position and rotation relative to the parent placement represented by transformation matrix. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Dispose().html) | Destructor for deterministic finalization of Mate object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Equals.html) | Operator of comparison implementation. Checks if two mates have same name and belongs to the same object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Remove.html) | Removes the Mate object. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [StoreToObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~StoreToObject.html) | Stores changes into a project database. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |
| Public Method | [Transform](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate~Transform.html) | Transform mate position. (Inherited from [Eplan.EplApi.DataModel.E3D.Mate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Mate.html)) |


