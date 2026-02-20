# PlcIOPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList.html

---

This class represents collection of properties of [PlcIO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIO.html) class. Please check also base classes for other properties which are available for [PlcIO](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIO.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.PlcIOPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class PlcIOPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class PlcIOPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [PlcIOPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [AUTOMATIONML\_OBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~AUTOMATIONML_OBJECTID().html) | AutomationML GUID # 25030. |
| Public Property | [AUTOMATIONML\_OBJECTID\_2](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~AUTOMATIONML_OBJECTID_2(Int32).html) | AutomationML GUID 2 # 25031. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FUNC\_PLC\_SIGNALRANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLC_SIGNALRANGE().html) | Signal range # 20388. |
| Public Property | [FUNC\_PLCCONFIGURATIONPROJECT\_INDIRECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCCONFIGURATIONPROJECT_INDIRECT().html) | Configuration project (indirect) # 20108. |
| Public Property | [FUNC\_PLCCPU\_INDIRECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCCPU_INDIRECT().html) | CPU (indirect) # 20434. |
| Public Property | [FUNC\_PLCSTATIONNAME\_INDIRECT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCSTATIONNAME_INDIRECT().html) | PLC station: ID (indirect) # 20420. |
| Public Property | [FUNC\_PLCTERMINAL\_INDEX\_OF\_STARTADDRESS](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCTERMINAL_INDEX_OF_STARTADDRESS().html) | PLC subdevice: Index # 20384. |
| Public Property | [FUNC\_PLCTERMINAL\_NO\_ADRESSING](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNC_PLCTERMINAL_NO_ADRESSING().html) | Do not include in addressing # 20380. |
| Public Property | [FUNCTION\_PLCIMPORTCOMPARE\_MARKEDTOBEDELETED](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~FUNCTION_PLCIMPORTCOMPARE_MARKEDTOBEDELETED().html) | Marked for deletion # 20186. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [PLCIOENTRY\_COMMUNICATIONENTITY\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~PLCIOENTRY_COMMUNICATIONENTITY_NAME().html) | Name of the communication unit # 23400. |
| Public Property | [PLCIOENTRY\_DIRECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~PLCIOENTRY_DIRECTION().html) | Direction # 23403. |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of PlcIOPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PlcIOPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


