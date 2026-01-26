# DeviceListEntryPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList.html

---

This class represents collection of properties of [DeviceListEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntry.html) class. Please check also base classes for other properties which are available for [DeviceListEntry](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntry.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.DeviceListEntryPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class DeviceListEntryPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class DeviceListEntryPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [DeviceListEntryPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [DEVICELISTENTRY\_COUNTALLOWED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_COUNTALLOWED().html) | Number allowed # 23201. |
| Public Property | [DEVICELISTENTRY\_COUNTALLOWEDALL](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_COUNTALLOWEDALL().html) | Total number allowed # 23204. |
| Public Property | [DEVICELISTENTRY\_COUNTUSED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_COUNTUSED().html) | Used unit quantity # 23205. |
| Public Property | [DEVICELISTENTRY\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_DESCRIPTION().html) | Device description # 23202. |
| Public Property | [DEVICELISTENTRY\_DESIGNATION1](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_DESIGNATION1().html) | Part: Designation 1 # 23210. |
| Public Property | [DEVICELISTENTRY\_DESIGNATION2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_DESIGNATION2().html) | Part: Designation 2 # 23211. |
| Public Property | [DEVICELISTENTRY\_DESIGNATION3](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_DESIGNATION3().html) | Part: Designation 3 # 23212. |
| Public Property | [DEVICELISTENTRY\_DISCONTINUED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_DISCONTINUED().html) | Discontinued part # 23215. |
| Public Property | [DEVICELISTENTRY\_ERPNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_ERPNR().html) | ERP / PDM number # 23216. |
| Public Property | [DEVICELISTENTRY\_MACRO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_MACRO().html) | Macro # 23214. |
| Public Property | [DEVICELISTENTRY\_MANUFACTURER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_MANUFACTURER().html) | Manufacturer # 23213. |
| Public Property | [DEVICELISTENTRY\_ORDERNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_ORDERNR().html) | Order number # 23207. |
| Public Property | [DEVICELISTENTRY\_PARTNR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_PARTNR().html) | Part number # 23200. |
| Public Property | [DEVICELISTENTRY\_PLANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_PLANT().html) | System part # 23208. |
| Public Property | [DEVICELISTENTRY\_RESERVE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_RESERVE().html) | Spare quantity # 23206. |
| Public Property | [DEVICELISTENTRY\_TYPENR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_TYPENR().html) | Type number # 23203. |
| Public Property | [DEVICELISTENTRY\_VARIANT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~DEVICELISTENTRY_VARIANT().html) | Variant # 23209. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_CRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~FUNC_CRAFT().html) | Trade # 20466. |
| Public Property | [FUNC\_SUBCRAFT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~FUNC_SUBCRAFT().html) | Subtrade # 20467. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of DeviceListEntryPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.DeviceListEntryPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


