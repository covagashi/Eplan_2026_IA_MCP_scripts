# MacroEntryPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList.html

---

This class represents collection of properties of [MacroEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntry.html) class. Please check also base classes for other properties which are available for [MacroEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntry.html) objects: [PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html), [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)  
            **Eplan.EplApi.DataModel.MacroEntryPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class MacroEntryPropertyList : PlacementPropertyList

[DefaultMember("Property")]

public ref class MacroEntryPropertyList : public PlacementPropertyList


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
| Public Constructor | [MacroEntryPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_DATE().html) | Overloaded. Modification date (change tracking) # 19032. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER().html) | Overloaded. Revision marker (change tracking) # 19030. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_MARKER\_FORMAT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_MARKER_FORMAT().html) | Overloaded. Revision marker format (change tracking) # 19031. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_TIME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_TIME().html) | Overloaded. Modification time (change tracking) # 19034. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISION\_LOG\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISION_LOG_USER().html) | Overloaded. Creator (change tracking) # 19033. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONID().html) | Overloaded. Revision change marker (from property comparison) # 10153. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [INSTANCE\_REVISIONMARKER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~INSTANCE_REVISIONMARKER().html) | Overloaded. Revision marker (from property comparison) # 10152. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |
| Public Property | [MACROBOX\_COMPANYSTANDARD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_COMPANYSTANDARD().html) | Macro: Company standard # 23017. |
| Public Property | [MACROBOX\_DIRECTORY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_DIRECTORY().html) | Macro: Directory # 23015. |
| Public Property | [MACROBOX\_INSERTED\_BY](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_INSERTED_BY().html) | Macro: Inserted by # 23006. |
| Public Property | [MACROBOX\_INSERTMODE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_INSERTMODE().html) | Macro: Also insert macro box # 23013. |
| Public Property | [MACROBOX\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_MACRO().html) | Macro: File name # 23001. |
| Public Property | [MACROBOX\_MACRO\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_MACRO_DESCRIPTION().html) | Macro: Description # 23004. |
| Public Property | [MACROBOX\_MACRO\_SOURCE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_MACRO_SOURCE().html) | Macro: Source / reference # 23003. |
| Public Property | [MACROBOX\_MACRO\_VERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_MACRO_VERSION().html) | Macro: Version # 23002. |
| Public Property | [MACROBOX\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_NAME().html) | Macro: Name # 23009. |
| Public Property | [MACROBOX\_NORM](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_NORM().html) | Macro: Standard # 23016. |
| Public Property | [MACROBOX\_REPRESENTATION\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_REPRESENTATION_TYPE().html) | Macro: Representation type # 23007. |
| Public Property | [MACROBOX\_SOURCEPROJECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_SOURCEPROJECT().html) | Macro: Source project # 23005. |
| Public Property | [MACROBOX\_TYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_TYPE().html) | Macro: Type # 23010. |
| Public Property | [MACROBOX\_USAGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_USAGE().html) | Macro: Type of usage # 23011. |
| Public Property | [MACROBOX\_USECONNECTIONPOINTDESIGNATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_USECONNECTIONPOINTDESIGNATION().html) | Macro: Take connection point designations into account # 23014. |
| Public Property | [MACROBOX\_USEPROTECTEDGROUP](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_USEPROTECTEDGROUP().html) | Macro: Protected group # 23012. |
| Public Property | [MACROBOX\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROBOX_VARIANT().html) | Macro: Variant # 23008. |
| Public Property | [MACROFILE\_CHANGEDATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROFILE_CHANGEDATE().html) | Macro: Modification date # 23019. |
| Public Property | [MACROFILE\_EPLANVERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~MACROFILE_EPLANVERSION().html) | Macro: Eplan version # 23018. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Overloaded. Change protection (hierarchical) # 3015. (Inherited from [Eplan.EplApi.DataModel.PlacementPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlacementPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of MacroEntryPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MacroEntryPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


