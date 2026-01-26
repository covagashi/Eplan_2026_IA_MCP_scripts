# ConnectionPointsInfoPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList.html

---

This class represents collection of properties of [ConnectionPointsInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfo.html) class. Please check also base classes for other properties which are available for [ConnectionPointsInfo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfo.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class ConnectionPointsInfoPropertyList : StorableObjectPropertyList

[DefaultMember("Property")]

public ref class ConnectionPointsInfoPropertyList : public StorableObjectPropertyList


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
| Public Constructor | [ConnectionPointsInfoPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ARTICLE\_ATTRIBUTE\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~ARTICLE_ATTRIBUTE_VALUE(Int32).html) | Attributes # 22051. |
| Public Property | [ARTICLE\_CUSTOM\_DATA\_INDEX](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~ARTICLE_CUSTOM_DATA_INDEX(Int32).html) | API Parts Management Extension: Name of add-in # 22212. |
| Public Property | [ARTICLE\_CUSTOM\_DATA\_VALUE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~ARTICLE_CUSTOM_DATA_VALUE(Int32).html) | API Parts Management Extension: Value from add-in # 22213. |
| Public Property | [ARTICLE\_PARTTYPE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~ARTICLE_PARTTYPE().html) | Record type # 22023. |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [PART\_CREATE\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_CREATE_DATE().html) | Creation date # 22983. |
| Public Property | [PART\_CREATE\_DATE\_UTC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_CREATE_DATE_UTC().html) | Creation date (UTC) # 22985. |
| Public Property | [PART\_CREATE\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_CREATE_USER().html) | Creator # 22982. |
| Public Property | [PART\_LASTCHANGE\_DATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_LASTCHANGE_DATE().html) | Modification date # 22981. |
| Public Property | [PART\_LASTCHANGE\_DATE\_UTC](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_LASTCHANGE_DATE_UTC().html) | Modification date (UTC) # 22986. |
| Public Property | [PART\_LASTCHANGE\_USER](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_LASTCHANGE_USER().html) | Last editor # 22980. |
| Public Property | [PART\_TERMINAL\_ADDITIONALLENGTHDEFAULT](topic134.html) | Additional length (default) # 22942. |
| Public Property | [PART\_TERMINAL\_CREATE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_CREATE().html) | Creator / Creation date (connection point pattern) # 22943. |
| Public Property | [PART\_TERMINAL\_DESCRIPTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_DESCRIPTION().html) | Description (Connection point pattern) # 22946. |
| Public Property | [PART\_TERMINAL\_DIRECTION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_DIRECTION().html) | Routing direction (default) # 22948. |
| Public Property | [PART\_TERMINAL\_LASTCHANGE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_LASTCHANGE().html) | Last editor / Modification date (connection point pattern) # 22944. |
| Public Property | [PART\_TERMINAL\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_NAME().html) | Name (connection point pattern) # 22945. |
| Public Property | [PART\_TERMINAL\_TERMINALSIZE\_DEFAULT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_TERMINALSIZE_DEFAULT().html) | Connection dimension (default) # 22969. |
| Public Property | [PART\_TERMINAL\_TYPEDEFAULT](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~PART_TERMINAL_TYPEDEFAULT().html) | Wire termination processing (Eplan Cabinet, default) # 22947. |
| Public Property | [PART\_TERMINAL\_TYPEOFTERMINAL\_DEFAULT](topic135.html) | Connection category (default) # 22968. |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of ConnectionPointsInfoPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPointsInfoPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


