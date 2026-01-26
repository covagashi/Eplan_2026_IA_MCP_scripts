# FunctionDefinitionLibraryPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList.html

---

This class represents collection of properties of [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) class. Please check also base classes for other properties which are available for [FunctionDefinitionLibrary](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibrary.html) objects: [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         **Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class FunctionDefinitionLibraryPropertyList : Eplan.EplApi.DataModel.StorableObjectPropertyList

[DefaultMember("Property")]

public ref class FunctionDefinitionLibraryPropertyList : public Eplan.EplApi.DataModel.StorableObjectPropertyList


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
| Public Constructor | [FunctionDefinitionLibraryPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [FCTDEFLIB\_CREATIONDATE](topic726.html) | Creation date # 15504. |
| Public Property | [FCTDEFLIB\_CREATOR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList~FCTDEFLIB_CREATOR().html) | Creator # 15503. |
| Public Property | [FCTDEFLIB\_LASTMODIFICATIONDATE](topic727.html) | Modification date # 15501. |
| Public Property | [FCTDEFLIB\_LASTMODIFICATOR](topic728.html) | Last editor: Sign-in name # 15505. |
| Public Property | [FCTDEFLIB\_VERSION](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList~FCTDEFLIB_VERSION().html) | Version information of function definition library # 15502. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |
| Public Property | [PROPUSER\_LAST\_USERCODE](topic733.html) | Last editor: ID # 3010. |
| Public Property | [PROPUSER\_LAST\_USEREMAIL](topic734.html) | Last editor: E-mail # 3013. |
| Public Property | [PROPUSER\_LAST\_USERNAME](topic735.html) | Last editor: Name # 3011. |
| Public Property | [PROPUSER\_LAST\_USERPHONE](topic736.html) | Last editor: Phone # 3012. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of FunctionDefinitionLibraryPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.FunctionDefinitionLibraryPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


