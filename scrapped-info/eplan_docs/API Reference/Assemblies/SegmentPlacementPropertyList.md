# SegmentPlacementPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList.html

---

This class represents a collection of properties of [SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html) class. Please also check the base classes for other properties that are available for [SegmentPlacement](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacement.html) objects: [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html), [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)  
               **Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class SegmentPlacementPropertyList : Eplan.EplApi.DataModel.SymbolReferencePropertyList

[DefaultMember("Property")]

public ref class SegmentPlacementPropertyList : public Eplan.EplApi.DataModel.SymbolReferencePropertyList


Remarks

It uses the [] operator in order to access its elements (stored properties).

Property list is a container for property values and just like them can be `persistent` (also called `online`) or `transient` (also called `offline`). If a property list is `persistent`, this means that it is associated with the properties of some StorableObject or other property list. If any property is added, changed or removed from the property list in this case, the result is also visible in the related objects. Whether a property list is `persistent` or `transient` is determined at the time of its creation and cannot be changed.

Example

This example shows the different usage of persistent property lists and transient property lists:

**C#**

```
// Creation of a persistent property list

FunctionPropertyList oPersistentPropertyList1 = oFunction.Properties;

oPersistentPropertyList1.FUNC_COMMENT = "Comment";

// Now, oFunction.Properties.FUNC_COMMENT is equals "Comment"

FunctionPropertyList oPersistentPropertyList2 = new FunctionPropertyList(oFunction);

oPersistentPropertyList2.FUNC_COMMENT = "Test";

// Now, oFunction.Properties.FUNC_COMMENT equals "Test"

// Creation of a transient property list

FunctionPropertyList oTransientPropertyList = new FunctionPropertyList();

oTransientPropertyList.FUNC_COMMENT = "Test comment";

oFunction.Properties.FUNC_COMMENT = oTransientPropertyList.FUNC_COMMENT;

oTransientPropertyList.FUNC_COMMENT = "Transient comment";

// Now, oTransientPropertyList.FUNC_COMMENT equals "Test comment"

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [SegmentPlacementPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList~_ctor().html) | Constructor |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_CROSSREFERENCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList~FUNC_CROSSREFERENCE().html) | Cross-reference (main / aux. function) # 20300. |
| Public Property | [FUNC\_SYMB\_DESC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_DESC().html) | Overloaded. Symbol description (function) # 20114. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NAME().html) | Overloaded. Symbol name # 20112. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_NUMBER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_NUMBER().html) | Overloaded. Symbol number # 20168. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMB\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMB_VARIANT().html) | Overloaded. Symbol variant # 20113. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMBLIB\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBLIB_NAME().html) | Overloaded. Symbol library # 20111. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [FUNC\_SYMBOL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~FUNC_SYMBOL().html) | Overloaded. Symbol # 20575. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_ACTIVE\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_ACTIVE_PROPERTYSET().html) | Overloaded. Property arrangement # 19307. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_FULLPLACEMENTLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_FULLPLACEMENTLOCATION().html) | Overloaded. Placement # 19007. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGEFULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGEFULLNAME().html) | Overloaded. Page name (full) # 19023. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGENAME().html) | Overloaded. Page name # 19022. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PAGETYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PAGETYPE().html) | Overloaded. Page type # 19020. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_PATHID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_PATHID().html) | Overloaded. Column number # 19005. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_POSID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_POSID().html) | Overloaded. Row number # 19006. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_TYPE().html) | Overloaded. Representation type / report type # 19021. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_USER\_DEFINED\_PROPERTYSET](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_USER_DEFINED_PROPERTYSET().html) | Overloaded. User-defined property arrangement: Name # 19008. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_XCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_XCOORD().html) | Overloaded. X coordinate # 19002. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [INSTANCE\_YCOORD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList~INSTANCE_YCOORD().html) | Overloaded. Y coordinate # 19003. (Inherited from [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of SegmentPlacementPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Planning.SegmentPlacementPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


