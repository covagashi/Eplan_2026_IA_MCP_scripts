# SymbolReference

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html

---

A class that represents logical elements of [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html)'s [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) that are placed in projects logical hierarchy. Although it does not have to be a device, in most cases it is.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         **Eplan.EplApi.DataModel.SymbolReference**  
            [Eplan.EplApi.DataModel.DeletedObjectInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfo.html)  
            [Eplan.EplApi.DataModel.DynamicConnectionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DynamicConnectionLine.html)  
            [Eplan.EplApi.DataModel.FunctionBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionBase.html)  
            [Eplan.EplApi.DataModel.MacroBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox.html)  
            [Eplan.EplApi.DataModel.Planning.SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html)  
            [Eplan.EplApi.DataModel.PotentialDefinition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PotentialDefinition.html)  
            [Eplan.EplApi.DataModel.StrandConnector](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandConnector.html)  
            [Eplan.EplApi.DataModel.StrandInterConnector](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StrandInterConnector.html)

Syntax

**C#**



public class SymbolReference : Placement, IPropertyPlacementsContainer

public ref class SymbolReference : public Placement, IPropertyPlacementsContainer


Remarks

Some properties of Data model classes are not linked with their owners even if from the syntax it may seem otherwise. For example: `oRectangle.Pen.ColorId = 5;` the ColorId of the Pen is changed, but oRectangle object doesn't know about it since the Pen property is a stand-alone value not aware of oRectangle object existence. This remark applies to the following SymbolReference property: PropertyPlacements. When a new object was created by API, the displayed properties are set from original default scheme of the symbol, even if another was set as default by user.

Example

**C#**

```
oRectangle.Pen.ColorId = 5;
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SymbolReference Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~_ctor().html) | Default constructor. Creates the SymbolReference object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AreTargetsSpecifed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~AreTargetsSpecifed.html) | The value determines if target is taken from net-based routing or not. |
| Public Property | [Block](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Block.html) | Returns a block which this SymbolReference object is part of. If this object is not a part of any block, this property returns NULL. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [GraphicalConnectionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnectionPoints.html) | An array of the symbols's connection points |
| Public Property | [GraphicalConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnections.html) | An array of [SymbolReference.GraphicalConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+GraphicalConnection.html) objects representing all auto-connecting lines connected to the pins of the symbol. This property may be useful to check graphical layout of connections associated with the symbol (including T-nodes, corners, etc.). |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [HasPolylineAsLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~HasPolylineAsLogicalArea.html) | Returns true if the symbol's logical area is a polyline (consisting of segments) rather than just a rectangle. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Location.html) | Overridden. Get or set the placement's location. |
| Public Property | [LogicalAreaSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~LogicalAreaSegments.html) | Gets/Sets an array of segments that the symbol's logical area may consist of. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Properties.html) | EPLAN properties of the SymbolReference object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacements.html) | Returns [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference. |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) | Returns [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) assigned to this SymbolReference. |
| Public Property | [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SymbolVariant.html) | Specifies [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this SymbolReference. |
| Public Property | [SymbolWiringType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SymbolWiringType.html) | Set configuration type to select different variants for point or destination wiring |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [UseLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~UseLocalPropertyPlacements.html) | Return true if the instance uses the local property instances, otherwise it uses the ones of the variant. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [ConvertToGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ConvertToGraphics.html) | Converts the symbol representing this object into a group of graphical placements. |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Create.html) | Overloaded. Creates a SymbolReference. It is placed on the page passed as a parameter, using a given SymbolVariant. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of SymbolReference object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetLogicalArea.html) | Returns a rectangle which is the logical area of the object derived from SymbolReference. For objects having symbols consisting of segments, this method returns the bounding box of the polyline created by those segments. |
| Public Method | [GetPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetPropertyPlacements.html) | Gets list of property placements of given type. |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [IsPointInsideLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~IsPointInsideLogicalArea.html) | Checks, if the point is inside logical area of the symbol. Returns true, if the symbol has a logical area and the point is inside. The logical area may be a rectangle or a polyline without arcs. |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [ReorderPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ReorderPropertyPlacements.html) | Reorders property placements of one type, which are assigned to this SymbolReference. |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SetLogicalArea.html) | Sets rectangular logical area for objects derived from SymbolReference. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


