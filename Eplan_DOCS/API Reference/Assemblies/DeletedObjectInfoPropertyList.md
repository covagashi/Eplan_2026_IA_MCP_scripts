# DeletedObjectInfoPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList.html

---

This class represents collection of properties of [DeletedObjectInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfo.html) class. Please check also base classes for other properties which are available for [DeletedObjectInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfo.html) objects: [SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html), [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            [Eplan.EplApi.DataModel.SymbolReferencePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.SymbolReferencePropertyList.html)  
               **Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class DeletedObjectInfoPropertyList : SymbolReferencePropertyList

[DefaultMember("Property")]

public ref class DeletedObjectInfoPropertyList : public SymbolReferencePropertyList


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
| Public Constructor | [DeletedObjectInfoPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DMDELETEDOBJECTINFO\_EDITINGAREA](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_EDITINGAREA().html) | Defined working section # 36617. |
| Public Property | [DMDELETEDOBJECTINFO\_OBJECTNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_OBJECTNAME().html) | Deleted object: Name # 36600. |
| Public Property | [DMDELETEDOBJECTINFO\_OBJECTNAME\_HIST](topic195.html) | Deleted object (further): Name # 36605. |
| Public Property | [DMDELETEDOBJECTINFO\_OBJECTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_OBJECTTYPE().html) | Deleted object: Type # 36601. |
| Public Property | [DMDELETEDOBJECTINFO\_OBJECTTYPE\_HIST](topic196.html) | Deleted object (further): Type # 36606. |
| Public Property | [DMDELETEDOBJECTINFO\_PROJECTREVISION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_PROJECTREVISION().html) | Associated project revision # 36610. |
| Public Property | [DMDELETEDOBJECTINFO\_PROJECTREVISION\_HIST](topic197.html) | Associated project revision (further) # 36611. |
| Public Property | [DMDELETEDOBJECTINFO\_PROJECTREVISION\_NAME](topic198.html) | Associated revision name # 36604. |
| Public Property | [DMDELETEDOBJECTINFO\_PROJECTREVISION\_NAME\_HIST](topic199.html) | Associated revision name (further) # 36609. |
| Public Property | [DMDELETEDOBJECTINFO\_REVISION\_LOG\_CHANGE](topic200.html) | Deleted object: Reason for revision change (change tracking) # 36616. |
| Public Property | [DMDELETEDOBJECTINFO\_REVISION\_LOG\_DESCRIPTION](topic201.html) | Deleted object: Revision description (change tracking) # 36615. |
| Public Property | [DMDELETEDOBJECTINFO\_REVISION\_LOG\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_REVISION_LOG_NAME().html) | Deleted object: Revision index # 36614. |
| Public Property | [DMDELETEDOBJECTINFO\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_TIME().html) | Delete date # 36603. |
| Public Property | [DMDELETEDOBJECTINFO\_TIME\_HIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_TIME_HIST(Int32).html) | Delete date (further) # 36608. |
| Public Property | [DMDELETEDOBJECTINFO\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_USER().html) | User name # 36602. |
| Public Property | [DMDELETEDOBJECTINFO\_USER\_HIST](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~DMDELETEDOBJECTINFO_USER_HIST(Int32).html) | User name (further) # 36607. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
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
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of DeletedObjectInfoPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeletedObjectInfoPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


