# Block

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block.html

---

A block object in P8 is a special kind of group which combines graphical placements (e.g. lines, circles, etc.) and optionally, one symbol reference. Such group is placed on a page and is referenced by a block reference object. In case a new block is created and it contains the symbol reference in itself, this symbol reference is also the block's reference and no extra block reference object is created. When trying to select a Block by its ID the SymbolReference inside the Block is selected instead. This Block class represents both the block itself as well as the block reference.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         **Eplan.EplApi.DataModel.Block**  
            [Eplan.EplApi.DataModel.ViewPart](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ViewPart.html)

Syntax

**C#**



public class Block : Placement, IPlacementsContainer

public ref class Block : public Placement, IPlacementsContainer


Remarks

\* Only one [SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html) object can be included in a block. \* A block may include another block's reference. \* Blocks are not listed in [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) SubPlacements, \* instead the Block is given as **Eplan::EplApi::DataModel:** Property.

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Block Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~_ctor().html) | Default constructor. Creates invalid Block object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Count](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Count.html) | Number of objects in the block. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Location.html) | Overridden. Get or set the placement's location. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Name.html) | Name of the referenced block. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Properties.html) | EPLAN properties of the block reference object. |
| Public Property | [RefCount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~RefCount.html) | Number of references. |
| Public Property | [SubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~SubPlacements.html) | Returns array of placements combined in this block. |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [BreakUp](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~BreakUp.html) | Overloaded. Breaks up the block into its individual elements, also recursively. |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Block~Create.html) | Creates valid `Block` object from the passed elements. At least two elements must be passed in `arrPlacements`. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Non-deterministic Finalizer of Block object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


