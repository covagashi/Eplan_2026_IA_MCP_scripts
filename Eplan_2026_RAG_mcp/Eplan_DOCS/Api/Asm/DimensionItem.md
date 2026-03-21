# DimensionItem

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem.html

---

This class represents the DimensionItem on the page.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)  
            **Eplan.EplApi.DataModel.Graphics.DimensionItem**

Syntax

**C#**



public class DimensionItem : GraphicalPlacement

public ref class DimensionItem : public GraphicalPlacement

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [DimensionItem Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~_ctor().html) | Constructor. When object created with this constructor, its `create` method must be call. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DimensionCalculated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionCalculated.html) | Gets or sets whether the value of the dimension (the dimension's text) is automatically calculated. |
| Public Property | [DimensionDisableZero](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionDisableZero.html) | Gets or sets whether presicion is setted or not. |
| Public Property | [DimensionDistanceToLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionDistanceToLine.html) | Gets or sets the distance of dimension text to dimension line. |
| Public Property | [DimensionExtensionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionExtensionLine.html) | Gets or sets the length of dimension extension help line. |
| Public Property | [DimensionLineTermination](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionLineTermination.html) | Gets or sets the dimension line termination. |
| Public Property | [DimensionPositionCalculated](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionPositionCalculated.html) | Gets or sets whether the dimension's text is automatically positioned (in relation to the DimensionItem itself). |
| Public Property | [DimensionPrecision](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionPrecision.html) | Gets or sets the presicion of DimensionItem. |
| Public Property | [DimensionPrefix](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionPrefix.html) | Gets or sets the prefix of DimensionItem. |
| Public Property | [DimensionShowUnits](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionShowUnits.html) | Gets or sets whether unit is displayed or not. |
| Public Property | [DimensionSuffix](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionSuffix.html) | Gets or sets the suffix of DimensionItem. |
| Public Property | [DimensionText](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionText.html) | Gets or sets the value of DimensionItem. |
| Public Property | [DimensionUnit](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionUnit.html) | Gets or sets the unit of DimensionItem. |
| Public Property | [DimensionValueCenteredInLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~DimensionValueCenteredInLine.html) | Gets or sets whether dimension value is centered in line. |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [EndPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~EndPoint.html) | Gets or sets the end point of the DimensionItem. |
| Public Property | [ExtensionLineFirst](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~ExtensionLineFirst.html) | Gets or sets whether first extension help line is displayed or not. |
| Public Property | [ExtensionLineSecond](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~ExtensionLineSecond.html) | Gets or sets whether second extension help line is displayed or not. |
| Public Property | [FirstPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~FirstPoint.html) | Gets or sets the first point of the DimensionItem. |
| Public Property | [GetAngleInRad](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~GetAngleInRad.html) | Gets angle value in radians for angular dimension type only. |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Eplan.EplApi.DataModel.Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~IsVisible.html) | Gets/Sets the actual visibility state of the object. (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Property | [Layer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~Layer.html) | Gets or sets object's graphical layer. If object is not assigned to a project (Project is null), null is returned (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Property | [LayerId](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~LayerId.html) | Gets layer id of layer assigned to this object. (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~Location.html) | Overridden. Get or set the placement's location. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [OffsetFromFirstExtensionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~OffsetFromFirstExtensionLine.html) | Gets or sets the offset from the first dimension, meaning the distance of the first dimension to the displayed help line. |
| Public Property | [OffsetFromSecondExtensionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~OffsetFromSecondExtensionLine.html) | Gets or sets the offset from the second dimension, meaning the distance of the second dimension to the displayed help line. |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Pen](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~Pen.html) | Sets [Pen](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Pen.html) related to this object. (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~Properties.html) | .NET Property enabling access to P8 properties of the Page object. |
| Public Property | [SecondPoint](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~SecondPoint.html) | Gets or sets the second point of the DimensionItem. |
| Public Property | [SuppressDimensionLine](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~SuppressDimensionLine.html) | Gets or sets whether dimension line is suppressed. |
| Public Property | [TextColor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~TextColor.html) | Color for displayed text. Color index (0-255) Please use -16002 as "From layer" value. Predefined values for line colour index are:  0 = black  1 = red  2 = yellow  3 = green  4 = cyan  5 = blue  6 = magenta  7 = white  252 = darkgray  253 = gray |
| Public Property | [TextFontInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~TextFontInfo.html) | Font for displayed text. |
| Public Property | [TextHeight](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~TextHeight.html) | Gets or sets the height of the text. |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~CopyTo.html) | Overloaded. Copy Placement and insert the Copy into destination group. Copied placement will be inserted into desired project of destination group. If this placement is temporary, the copy will be persistent, if the destination group is also persistent. Group or Page, where the placement will be inserted. Defines whether a layer should be matched by name.Defines whether user-defined property definitions should be matched by identifying name. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~Create.html) | Overloaded. Creates a linear DimensionItem on the given page. |
| Public Method | [CreateAngular](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.DimensionItem~CreateAngular.html) | Creates an angular DimensionItem on the given page. |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~GetBoundingBox.html) | Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Remove.html) | Removes placement. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetVisibilityDependingOnLayer](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement~SetVisibilityDependingOnLayer.html) | This method sets the visibility of the graphical instance to depend on the layer setting (Inherited from [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)) |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Eplan.EplApi.DataModel.Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Eplan.EplApi.DataModel.Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |


