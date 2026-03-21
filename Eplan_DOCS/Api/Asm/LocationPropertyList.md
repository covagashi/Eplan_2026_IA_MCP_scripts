# LocationPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList.html

---

This class represents collection of properties of [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location.html) class. Please check also base classes for other properties which are available for [Location](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Location.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.LocationPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class LocationPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class LocationPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [LocationPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AUTOMATIONML\_OBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~AUTOMATIONML_OBJECTID().html) | AutomationML GUID # 25030. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [LOCATION\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_DESCRIPTION().html) | Structure description # 1002. |
| Public Property | [LOCATION\_DESCRIPTION\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_DESCRIPTION_2().html) | Structure description 2 # 1007. |
| Public Property | [LOCATION\_DESCRIPTION\_3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_DESCRIPTION_3().html) | Structure description 3 # 1008. |
| Public Property | [LOCATION\_DESCRIPTION\_SUPPLEMENTARYFIELD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_DESCRIPTION_SUPPLEMENTARYFIELD(Int32).html) | Structure description Supplementary field # 1009. |
| Public Property | [LOCATION\_FULLNAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_FULLNAME().html) | Complete structure identifier # 1001. |
| Public Property | [LOCATION\_FULLNAME\_WITHPREFIX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_FULLNAME_WITHPREFIX().html) | Complete structure identifier with preceding sign # 1003. |
| Public Property | [LOCATION\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_NAME().html) | Structure identifier # 1000. |
| Public Property | [LOCATION\_NAMEPART](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_NAMEPART(Int32).html) | Structure identifier: superior name component # 1010. |
| Public Property | [LOCATION\_TYPENAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_TYPENAME().html) | Identifier block # 1004. |
| Public Property | [LOCATION\_TYPENAME\_NR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_TYPENAME_NR().html) | Identifier block (ID) # 1006. |
| Public Property | [LOCATION\_UPPERLOCATION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_UPPERLOCATION(Int32).html) | Structure identifier superior # 1011. |
| Public Property | [LOCATION\_UPPERLOCATION\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_UPPERLOCATION_DESCRIPTION(Int32).html) | Structure identifier superior: Description # 1012. |
| Public Property | [LOCATION\_USE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~LOCATION_USE().html) | Usage count # 1005. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [WRITEPROTECTED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~WRITEPROTECTED().html) | Change protection # 3014. |
| Public Property | [WRITEPROTECTED\_AUTOMATIC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~WRITEPROTECTED_AUTOMATIC().html) | Change protection (hierarchical) # 3015. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of LocationPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.LocationPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


