# ViewPlacementPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList.html

---

This class represents collection of properties of [ViewPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement.html) class. Please check also base classes for other properties which are available for [ViewPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacement.html) objects: [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            [Eplan.EplApi.DataModel.GroupPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.GroupPropertyList.html)  
               **Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class ViewPlacementPropertyList : Eplan.EplApi.DataModel.GroupPropertyList

[DefaultMember("Property")]

public ref class ViewPlacementPropertyList : public Eplan.EplApi.DataModel.GroupPropertyList


Remarks

It uses operator[] in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `online` or `offline`. If property list is `online` it means that is associated with properties of some StorableObject or other property list. In this case if any property is added, changed or removed from property list the result is also visible in related objects. Whether property list is online or offline is being determine in time of it's creation and can not be changed.

Example

Example shows usage of online an offline property list:

**C#**

```
// creation of persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// now oFunction.Properties.FUNC_COMMENT is equal "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// now oFunction.Properties.FUNC_COMMENT is equal "Test"

// creation of transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// now oTransientPropertyList.FUNC_COMMENT is equal "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [ViewPlacementPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DMG\_VIEWPLACEMENT\_ADIMSCHEME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_ADIMSCHEME().html) | Model view: Scheme for automatic dimensioning # 36511. |
| Public Property | [DMG\_VIEWPLACEMENT\_BUILDINGAREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_BUILDINGAREA().html) | Model view: Layout space name # 36504. |
| Public Property | [DMG\_VIEWPLACEMENT\_BUILDINGAREA\_DESCRIPTION](topic714.html) | Model view: Layout space description # 36505. |
| Public Property | [DMG\_VIEWPLACEMENT\_CONSIDER\_TRANSFORM\_OF\_PLANE](topic715.html) | Model view: Apply viewpoint to mounting surface # 36508. |
| Public Property | [DMG\_VIEWPLACEMENT\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_DESCRIPTION().html) | Model view: Description # 36500. |
| Public Property | [DMG\_VIEWPLACEMENT\_DESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_DESIGNATION().html) | Model view: Name # 36503. |
| Public Property | [DMG\_VIEWPLACEMENT\_DISPLAY\_FREE\_ROUTED\_CABLES](topic716.html) | Model view: Display freely routed cables # 36515. |
| Public Property | [DMG\_VIEWPLACEMENT\_DISPLAY\_FREE\_ROUTED\_PIPES](topic717.html) | Model view: Display freely routed pipes # 36523. |
| Public Property | [DMG\_VIEWPLACEMENT\_EDGE\_WIDTH](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_EDGE_WIDTH().html) | Model view: Edge width # 36524. |
| Public Property | [DMG\_VIEWPLACEMENT\_FREE\_ROUTED\_CONNECTIONS](topic718.html) | Model view: Display freely routed wires # 36516. |
| Public Property | [DMG\_VIEWPLACEMENT\_FREE\_ROUTED\_HOSES](topic719.html) | Model view: Display freely routed hoses # 36518. |
| Public Property | [DMG\_VIEWPLACEMENT\_FROZEN\_VIEW](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_FROZEN_VIEW().html) | Model view: Frozen # 36502. |
| Public Property | [DMG\_VIEWPLACEMENT\_LABELINGSCHEME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_LABELINGSCHEME().html) | Model view: Item labeling # 36507. |
| Public Property | [DMG\_VIEWPLACEMENT\_MAINOBJECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_MAINOBJECT().html) | Model view: Basic item # 36509. |
| Public Property | [DMG\_VIEWPLACEMENT\_MANUAL\_CENTER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_MANUAL_CENTER().html) | Model view: Manual displacement # 36501. |
| Public Property | [DMG\_VIEWPLACEMENT\_ORIENTATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_ORIENTATION().html) | Model view: Rotation # 36514. |
| Public Property | [DMG\_VIEWPLACEMENT\_ROUTED\_HOSE\_ASSEMBLY](topic720.html) | Model view: Display freely routed hose lines # 36517. |
| Public Property | [DMG\_VIEWPLACEMENT\_SCALE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SCALE().html) | Model view: Scale # 36510. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWBENDINGAREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWBENDINGAREA().html) | Show bending extents # 36521. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWBENDINGHINT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWBENDINGHINT().html) | Show bending note # 36522. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWBENDINGLINES](topic721.html) | Show bending line # 36520. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWBLACKWIHTE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWBLACKWIHTE().html) | Model view: Display item edges in black # 36526. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWDRILLINGS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWDRILLINGS().html) | Show drilling pattern # 36519. |
| Public Property | [DMG\_VIEWPLACEMENT\_SHOWSILOUETTES](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_SHOWSILOUETTES().html) | Model view: Display item silhouettes # 36513. |
| Public Property | [DMG\_VIEWPLACEMENT\_TEMPLATE\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~DMG_VIEWPLACEMENT_TEMPLATE_NAME().html) | Model view: Name of the report template # 36512. |
| Public Property | [DMG\_VIEWPLACEMENT\_TEXTDIRECTION\_LIKE\_IN\_3D](topic722.html) | Model view: Do not automatically rotate texts from layout space # 36525. |
| Public Property | [DMG\_VIEWPLACEMENT\_UNITSELECTIONSCHEME](topic723.html) | Model view: Selection scheme # 36506. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_COMMENT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~FUNC_COMMENT().html) | Remark # 20045. |
| Public Property | [FUNC\_MOUNTINGPLATE\_CAPTIONFORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~FUNC_MOUNTINGPLATE_CAPTIONFORM().html) | Enclosure legend form # 20440. |
| Public Property | [FUNC\_MOUNTINGPLATE\_FORMEVALUATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~FUNC_MOUNTINGPLATE_FORMEVALUATION().html) | Suppress generation of the enclosure legend # 20441. |
| Public Property | [INSTANCE\_ACTIVE\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~INSTANCE_ACTIVE_PROPERTYSET().html) | Property arrangement # 19307. |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_USER\_DEFINED\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~INSTANCE_USER_DEFINED_PROPERTYSET().html) | User-defined property arrangement: Name # 19008. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of ViewPlacementPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.ViewPlacementPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


