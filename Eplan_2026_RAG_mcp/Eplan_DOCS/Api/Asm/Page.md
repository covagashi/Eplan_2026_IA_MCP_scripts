# Page

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html

---

Page class represents an EPLAN project's page.

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)  
      [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)  
         [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)  
            [Eplan.EplApi.DataModel.DocumentBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentBase.html)  
               **Eplan.EplApi.DataModel.Page**

Syntax

**C#**



public class Page : DocumentBase, IPlacementsContainer, IWriteProtection

public ref class Page : public DocumentBase, IPlacementsContainer, IWriteProtection


Remarks

Some properties of the class are not linked with their owners even if from the syntax it may seem otherwise. This concerns NameParts property and array properties like : AllFirstLevelPlacements, AllGraphicalPlacements, AllPlacements, Functions, PLCs, PlugStrips, TerminalStrips.

Example

The following example shows how to use class Page.

**C#**

```
PagePropertyList oPPL = new PagePropertyList();

oPPL.DESIGNATION_LOCATION = "A";

oPPL.DESIGNATION_PLANT = "O";

Page oPage = new Page(m_oTestProject, DocumentTypeManager.DocumentType.Circuit, oPPL);

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [Page Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AllFirstLevelPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllFirstLevelPlacements.html) | All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s including [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)s placed on this page. They are not filtered. All returned [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s are placed directly on this page. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). |
| Public Property | [AllGraphicalPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllGraphicalPlacements.html) | All [Eplan.EplApi.DataModel.Graphics.GraphicalPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.GraphicalPlacement.html)s placed on this page. They are not filtered. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). |
| Public Property | [AllPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~AllPlacements.html) | All [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s, placed on this page. [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)s are ungrouped and contained [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s are returned. They are not filtered. This method does not return embedded objects (like for example [Eplan.EplApi.DataModel.Graphics.Shielding](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.Shielding.html)). This method does not return [Eplan.EplApi.DataModel.Graphics.PropertyPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PropertyPlacement.html). |
| Public Property | [BoxedDevices](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~BoxedDevices.html) | Returns all [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s placed on the page. If the filter was set up, returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching the filter. |
| Public Property | [CrossReferencedObjectsAll](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~CrossReferencedObjectsAll.html) | Returns an array of objects cross-referenced with this object (i.e. having the same name - in case of functions - or otherwise associated) (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DatabaseIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~DatabaseIdentifier.html) | Returns the project as number. The number is unique for all open projects in one session. The number changes when the project is closed and opened again. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [DrawingOrder](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~DrawingOrder.html) | Sets display sequence. The drawing order flag will be used to sort elements according to drawing order within a group. If elements chare the same value the drawing order will result from order of the data model. Default value is 67. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [Filter](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Filter.html) | Page's property that allows to access current page's filter. It affects properties "Functions", "Terminals", "TerminalStrips", "Plugs", "PlugStrips" and "PLCs". |
| Public Property | [Functions](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Functions.html) | Returns all [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s placed on the page. If the filter was set up, returns [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html)s matching the filter. |
| Public Property | [GridSize](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~GridSize.html) | Gets/sets the size of the page's grid. |
| Public Property | [Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Group.html) | Returns a group that the Placement object belongs to. If the Placement object doesn't belong to any group, NULL is returned. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IdentifyingName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~IdentifyingName.html) | Returns identifying name of the page. |
| Public Property | [IsLocked](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsLocked.html) | Determines if the the StorableObject is locked.  The StorableObject is locked when it was explicitly or implicitly locked. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsLogicalPage](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~IsLogicalPage.html) | Returns if the page is a logical page. |
| Public Property | [IsPlaced](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsPlaced.html) | Returns true if the placement is placed (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsReadOnly](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsReadOnly.html) | Determines if StorableObject is read-only (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsSetAsVisible](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~IsSetAsVisible.html) | Gets/Sets visibility of the object as set in its properties dialog. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [IsTransient](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsTransient.html) | Determines if the the StorableObject is transient.  The StorableObject is transient when it was created by default constructor and:  it is a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) and it was not assigned a [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Project.html),  it is a [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) or any class derived from it and was not assigned a [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html). (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [IsValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~IsValid.html) | Determines if StorableObject is correct database object and is not deleted. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentBase~Location.html) | Get or set the placement's location. (Inherited from [Eplan.EplApi.DataModel.DocumentBase](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DocumentBase.html)) |
| Public Property | [MacroRepresentationType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~MacroRepresentationType.html) | Page's property describing type of macro. This type is used to find a suitable variant of macro, which can be insert on this page. While inserting macro on page, inserting variant of macro is get from page's MacroRepresentationType and variant of macro defined by user. This property depends on property PageType. |
| Public Property | [Name](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Name.html) | Get or set name of the page. When setting this property, it is not checked whether the given name already exists in project. |
| Public Property | [NameParts](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~NameParts.html) | Gets/Sets the name of a page. |
| Public Property | [ObjectIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ObjectIdentifier.html) | Returns the object identifier as number. The number is unique for all objects of this type. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Page.html) | Returns the page the Placement is on, or assigns a Page object to the placement. If the placement was previously assigned to another page, it is removed from old one and assigned to the page given as an argument. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [PageType](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageType.html) | Gets/sets a page's property describing type of document |
| Public Property | [PageTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PageTypeName.html) | Returns name of the page's type. |
| Public Property | [PlanningSegment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PlanningSegment.html) | Get or set planning objects to which this page is assigned or null. |
| Public Property | [PLCs](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PLCs.html) | Returns all [Eplan.EplApi.DataModel.EObjects.PLC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PLC.html)s placed on the page. If the filter was set up, returns [BoxedDevice](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.BoxedDevice.html)s matching the filter. |
| Public Property | [PlotFrame](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PlotFrame.html) | Returns the page PlotFrame. |
| Public Property | [PlugStrips](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PlugStrips.html) | Returns all [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s placed on the page. If the filter was set up, returns [Eplan.EplApi.DataModel.EObjects.PlugStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.PlugStrip.html)s matching the filter. |
| Public Property | [Project](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Project.html) | Returns the project to which the StorableObject belongs. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [Properties](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Properties.html) | Property enabling access to internal properties of the Page object. |
| Public Property | [ReportBlock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~ReportBlock.html) | `ReportBlock` which contains data describing report from this page. |
| Public Property | [Size](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Size.html) | Returns the exact size of the page, takes into account page scale. The size is calculated from center of border lines. |
| Public Property | [SubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~SubPlacements.html) | Returns all grouped [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Property | [TerminalStrips](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~TerminalStrips.html) | Returns all [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)s placed on the page. If the filter was set up, returns [Eplan.EplApi.DataModel.EObjects.TerminalStrip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.TerminalStrip.html)s matching the filter. |
| Public Property | [Tooltip](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Tooltip.html) | Gets the tooltips of the object as can be seen in the GED (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Property | [TypeIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~TypeIdentifier.html) | Returns the type of the object as number. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Property | [WriteProtected](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~WriteProtected.html) | Check if object is currently write protected or sets Manual write protection |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [ConvertToGraphics](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~ConvertToGraphics.html) | Converts all symbols and connections on the page into graphical instances. Graphical instances of a given symbol are automatically grouped. |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~CopyTo.html) | Overloaded. Creates copy of this page. |
| Public Method | [Create](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Create.html) | Overloaded. Creates a new Page object. It is placed in the project under location given as parameters. |
| Public Method | [DeepUnGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~DeepUnGroup.html) | Overloaded. Remove all [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group and it's sub groups. If true method will remove also SubGroups. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Dispose().html) | Destructor. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~Equals.html) | Operator of comparison implementation. Checks if two StorableObjects refer to the same object in the project. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetBoundingBox](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~GetBoundingBox.html) | Overridden. Placement bounding box. Bounding box is a rectangle which contain this placement. It can be also used to determine placement size. |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetHashCode.html) | Serves as the default hash function. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetTypeName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~GetTypeName.html) | Returns object type name. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [GetWriteProtectionFlagSet](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~GetWriteProtectionFlagSet.html) | Checks if a specific write protection kind was set. |
| Public Method | [InsertSubPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacement.html) | Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) to a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [InsertSubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~InsertSubPlacements.html) | Insert [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s to a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [IsEditable](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsEditable.html) | Check if the Group is editable. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [IsGroupValid](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~IsGroupValid.html) | Returns true, if group is valid if not, the group should be dissolved (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [LockObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~LockObject().html) | Tries to lock current object in database for exclusive access. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [Move](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~Move.html) | Moves the group (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [PauseWriteProtection](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~PauseWriteProtection.html) | Temporarily disables write protection. Note that current write protection flags are not cleared. |
| Public Method | [Remove](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~Remove.html) | Overridden. Removes placement. |
| Public Method | [RemoveSubPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacement.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) from the group and from the project. The Placement object passed into this method is no longer valid. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [RemoveSubPlacements](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~RemoveSubPlacements.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s from the group and from the project. The Placement objects passed into this method are no longer valid. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |
| Public Method | [Scale](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement~Scale.html) | Overloaded. Scales the placement (or group of placements) by the specified factors in X and Y axis with scaling origin point specified by the ptOrigin parameter. (Inherited from [Eplan.EplApi.DataModel.Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)) |
| Public Method | [SetName](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetName(PagePropertyList).html) | Sets the name of the page. Name parts should be given in the PagePropertyList. |
| Public Method | [SetProject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page~SetProject.html) | Assigns a page to a given project. |
| Public Method | [SmartLock](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~SmartLock.html) | Tries to lock current object. If object is [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html) - it's page will be locked as well; [Eplan.EplApi.DataModel.E3D.Placement3D](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3D.html) locks it's installation space; [Function](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Function.html) locks all it's connections and connection definition points; [Page](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Page.html) locks all placements from this page. Throws [Eplan.EplApi.Base.LockingException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.LockingException.html) on failure. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [ToStringIdentifier](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject~ToStringIdentifier.html) | Returns this object as string identifier. (Inherited from [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html)) |
| Public Method | [UnGroup](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group~UnGroup.html) | Overloaded. Remove [Placement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Placement.html)s only from a group. (Inherited from [Eplan.EplApi.DataModel.Group](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Group.html)) |


