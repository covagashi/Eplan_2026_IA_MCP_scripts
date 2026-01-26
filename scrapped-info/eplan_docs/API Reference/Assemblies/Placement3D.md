# Placement3D

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html

---

Represents object from project which has 3D representation.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      **Eplan.EplApi.DataModel.E3D.Placement3D**  
         [Eplan.EplApi.DataModel.E3D.AuxiliaryLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.AuxiliaryLine.html)  
         [Eplan.EplApi.DataModel.E3D.Function3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Function3D.html)  
         [Eplan.EplApi.DataModel.E3D.MateEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.MateEntry.html)  
         [Eplan.EplApi.DataModel.E3D.Plane](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane.html)

Syntax

**C#**



public class Placement3D : Eplan.EplApi.DataModel.StorableObject, Eplan.EplApi.DataModel.IPropertyPlacementsContainer

public ref class Placement3D : public Eplan.EplApi.DataModel.StorableObject, Eplan.EplApi.DataModel.IPropertyPlacementsContainer

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Placement3D Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~_ctor().html) | Default constructor. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AbsoluteTransformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformation.html) | Absolute position and rotation represented by transformation matrix. |
| Public Property | [AbsoluteTransformationOfMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AbsoluteTransformationOfMacro.html) | Absolute position and rotation represented by transformation matrix where transformation of macro is considered. |
| Public Property | [AreConnectionPointPositionsLocal](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AreConnectionPointPositionsLocal.html) | Determines if connection point data are saved locally at the part placement. |
| Public Property | [Children](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Children.html) | Returns all children of this object. |
| Public Property | [Color](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Color.html) | Color of 3D Placement |
| Public Property | [Connection3Ds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Connection3Ds.html) | All existing 3d connections whose beginning or end is this placement. |
| Public Property | [ConnectionPointPositions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~ConnectionPointPositions.html) | Array of connection points data. |
| Public Property | [Corners](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Corners.html) | Represents coordinates of corners |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FunctionDefinition.html) | Returns the [Eplan.EplApi.DataModel.FunctionDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionDefinition.html) of the Placement3D. |
| Public Property | [Group3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Group3D.html) | Returns a Group3D object that the Placement3D object belongs to. If the Placement3D object doesn't belong to any group3D, NULL is returned. |
| Public Property | [InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~InstallationSpace.html) | Returns [InstallationSpace](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.InstallationSpace.html) in which this object exists. |
| Public Property | [IsHidden](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsHidden.html) | Indicates whether object is currently hidden in 3D editor view. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsMeshCreated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsMeshCreated.html) | Returns `true` if a mesh is created for this objects and assigned for it. |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~IsPlaced.html) | Returns true if the placement is placed. |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Layer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Layer.html) | Returns the [Eplan.EplApi.DataModel.Graphics.GraphicalLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalLayer.html) of the Placement3D. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Parent.html) | Gets or Sets parent placement. Caution: The Change of the parent will also change the absolute position because Placement3D stores the position relative to his parent |
| Public Property | [PlacementArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PlacementArea.html) | Represents placement area of a Placement3D. |
| Public Property | [Planes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Planes.html) | Returns children of this object which are [Plane](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Plane.html). |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Properties.html) | .NET Property enabling access to EPLAN properties of the Placement3D object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacements.html) | Returns [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacementsSchemas.html) assigned to this Placement3D. |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~PropertyPlacementsSchemas.html) | Returns [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) assigned to this SymbolReference. |
| Public Property | [RelativeTransformation](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformation.html) | Position and rotation relative to the parent placement represented by transformation matrix. |
| Public Property | [RelativeTransformationOfMacro](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RelativeTransformationOfMacro.html) | Relative position and rotation represented by transformation matrix where transformation of macro is considered. |
| Public Property | [TopLevelParent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~TopLevelParent.html) | Gets the root 3d placement from tree of 3d elements which this object is part of. |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [UseLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~UseLocalPropertyPlacements.html) | Return true if the instance uses the local property instances, otherwise it uses the ones of the variant. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddConnectionPointPosition.html) | Creates new connection point position. |
| Public Method | [AddMatePersistent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~AddMatePersistent.html) | Add copy of a mate to a Placement3D. |
| Public Methodstatic (Shared in Visual Basic) | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~CopyTo.html) | Overloaded. Copy 3D Placement Placement3D and its children will be copied into the same Project as newParent Then parent of the copy will be set to newParent new parent of copy |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of Placement3D object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [FindSourceMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindSourceMate.html) | Overloaded. Find source mate by name. Mate namePlacement optionsConsider child mounting surfaces |
| Public Method | [FindTargetMate](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~FindTargetMate.html) | Overloaded. Find target mate by name. Mate nameConsider mounting clearanceConsider child mounting surfaces |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBox.html) | Returns bounding box of a Placement3D. |
| Public Method | [GetBoundingBoxRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetBoundingBoxRelative.html) | Returns relative bounding box of a Placement3D. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetSourceMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetSourceMates.html) | Overloaded. Get array of all source mates from this object. Placement optionsConsider child mounting surfaces |
| Public Method | [GetTargetMates](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~GetTargetMates.html) | Overloaded. Get array of all target mates from this object. Consider mounting clearanceConsider child mounting surfaces |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Move.html) | Move this object. |
| Public Method | [MoveRelative](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~MoveRelative.html) | Move this object relative to its parent. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~Remove.html) | Removes object from project and all its children. |
| Public Method | [RemoveConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemoveConnectionPointPosition.html) | Removes connection point data stored under given index. |
| Public Method | [RemovePlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~RemovePlacement.html) | Removes object and all its children only from layout space. |
| Public Method | [SetParent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SetParent.html) | Sets parent placement. Sets parent placement. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [StoreConnectionPointPosition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~StoreConnectionPointPosition.html) | Stores data from connection point position in function under given index. |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


