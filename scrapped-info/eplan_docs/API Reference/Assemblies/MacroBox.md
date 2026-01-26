# MacroBox

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox.html

---

This class represents a macro box object. This is box for elements of Eplan.EplApi.DataModel.MasterData.Macro.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)  
            **Eplan.EplApi.DataModel.MacroBox**

Syntax

**C#**



public class MacroBox : SymbolReference, IPropertyPlacementsContainer

public ref class MacroBox : public SymbolReference, IPropertyPlacementsContainer

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MacroBox Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~_ctor().html) | Default constructor. Should never be used. Always throws NotImplementedException. It was designed only for COM compatibility. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AreTargetsSpecifed](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~AreTargetsSpecifed.html) | The value determines if target is taken from net-based routing or not. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [Block](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Block.html) | Returns a block which this SymbolReference object is part of. If this object is not a part of any block, this property returns NULL. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [GenerateProtectedGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~GenerateProtectedGroup.html) | Gets or sets generate protected group property. |
| Public Property | [GraphicalConnectionPoints](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnectionPoints.html) | An array of the symbols's connection points (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [GraphicalConnections](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GraphicalConnections.html) | An array of [SymbolReference.GraphicalConnection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference+GraphicalConnection.html) objects representing all auto-connecting lines connected to the pins of the symbol. This property may be useful to check graphical layout of connections associated with the symbol (including T-nodes, corners, etc.). (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [HasPolylineAsLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~HasPolylineAsLogicalArea.html) | Returns true if the symbol's logical area is a polyline (consisting of segments) rather than just a rectangle. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [InsertionPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~InsertionPoint.html) | Coordinates of insertion point |
| Public Property | [InsertionPointActive](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~InsertionPointActive.html) | InsertionPoint |
| Public Property | [InsertMacroBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~InsertMacroBox.html) | Gets or sets insert macro box property. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsSurfaceFilled](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~IsSurfaceFilled.html) | Indicates whether surface is filled or not. |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~Location.html) | Get or set the placement's location. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [LogicalAreaSegments](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~LogicalAreaSegments.html) | Gets/Sets an array of segments that the symbol's logical area may consist of. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [MacroName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~MacroName.html) | Macro name |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~Properties.html) | .NET Property enabling access to P8 properties of the MacroBox object. |
| Public Property | [PropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacements.html) | Returns [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html)s assigned to the SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) | Returns [SymbolReference.PropertyPlacementsSchemas](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~PropertyPlacementsSchemas.html) assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [ReferencedPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~ReferencedPlacements.html) | All referenced objects |
| Public Property | [ReferencesActive](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~ReferencesActive.html) | This property corresponds with the "Individual objects assignment" flag in the macro box dialog. |
| Public Property | [RepresentationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~RepresentationType.html) | Representation Type property of the macro box |
| Public Property | [SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SymbolVariant.html) | Specifies [Eplan.EplApi.DataModel.MasterData.SymbolVariant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolVariant.html) assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [SymbolWiringType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SymbolWiringType.html) | Set configuration type to select different variants for point or destination wiring (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [TakeConnectionPointDesignationsIntoAccount](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~TakeConnectionPointDesignationsIntoAccount.html) | Gets or sets take connection point designations into account property. |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [TypeOfUsage](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~TypeOfUsage.html) | Gets or sets type of usage. |
| Public Property | [UseLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~UseLocalPropertyPlacements.html) | Return true if the instance uses the local property instances, otherwise it uses the ones of the variant. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Property | [Variant](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~Variant.html) | Variant |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [AddReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~AddReference.html) | Adds reference to object, that belongs to macro |
| Public Method | [ConvertToGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ConvertToGraphics.html) | Converts the symbol representing this object into a group of graphical placements. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~Create.html) | Overloaded. Creates a MacroBox object. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor for deterministic finalization of MacroBox object. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~GetGraphics.html) | Gets a Placement object that represents the macro box graphically on a page. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetLogicalArea.html) | Returns a rectangle which is the logical area of the object derived from SymbolReference. For objects having symbols consisting of segments, this method returns the bounding box of the polyline created by those segments. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [GetPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~GetPropertyPlacements.html) | Gets list of property placements of given type. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [IsPointInsideLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~IsPointInsideLogicalArea.html) | Checks, if the point is inside logical area of the symbol. Returns true, if the symbol has a logical area and the point is inside. The logical area may be a rectangle or a polyline without arcs. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [RemoveAllReferences](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~RemoveAllReferences.html) | Remove all references |
| Public Method | [RemoveReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroBox~RemoveReference.html) | Remove reference |
| Public Method | [ReorderPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~ReorderPropertyPlacements.html) | Reorders property placements of one type, which are assigned to this SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetLogicalArea](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SetLogicalArea.html) | Sets rectangular logical area for objects derived from SymbolReference. (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [SwitchLocalPropertyPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference~SwitchLocalPropertyPlacements.html) | Copies or removes all local ProperyPlacemnets and sets flag (Inherited from [Eplan.EplApi.DataModel.SymbolReference](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReference.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


