# OptionFragmentPropertyList

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList.html

---

This class represents collection of properties of [OptionFragment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragment.html) class. Please check also base classes for other properties which are available for [OptionFragment](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragment.html) objects: [StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)

Inheritance Hierarchy

[System.Object](#)  
   [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)  
      [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)  
         [Eplan.EplApi.DataModel.OptionBasePropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionBasePropertyList.html)  
            **Eplan.EplApi.DataModel.OptionFragmentPropertyList**

Syntax

**C#**



[DefaultMember("Property")]

public class OptionFragmentPropertyList : OptionBasePropertyList

[DefaultMember("Property")]

public ref class OptionFragmentPropertyList : public OptionBasePropertyList


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
| Public Constructor | [OptionFragmentPropertyList Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~_ctor.html) | Overloaded. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [ExistingIds](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingIds.html) | Returns array of property ids. Returns array of AnyPropertyId objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [ExistingValues](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~ExistingValues.html) | Returns array of PropertyValue objects. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [OPTION\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTION_DESCR().html) | Project option: Description # 23106. |
| Public Property | [OPTION\_ISACTIVE](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTION_ISACTIVE().html) | Project option active # 23103. |
| Public Property | [OPTION\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTION_NAME().html) | Project option: Name # 23101. |
| Public Property | [OPTIONFRAGMENT\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONFRAGMENT_DESCR().html) | Project option section: Description # 23105. |
| Public Property | [OPTIONFRAGMENT\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONFRAGMENT_NAME().html) | Project option section: Name # 23102. |
| Public Property | [OPTIONGROUP\_DESCR](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONGROUP_DESCR().html) | Project option group: Description # 23104. |
| Public Property | [OPTIONGROUP\_NAME](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~OPTIONGROUP_NAME().html) | Project option group: Name # 23100. |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Parent.html) | StorableObject to which this property list is connected. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Property | [Property](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~Property.html) | Overloaded. Method used by operator[] in order to access indexed properties. |
| Public Property | [PROPUSER\_DBOBJECTID](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList~PROPUSER_DBOBJECTID().html) | Overloaded. Object identification # 2000. (Inherited from [Eplan.EplApi.DataModel.StorableObjectPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObjectPropertyList.html)) |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~CopyTo.html) | Overloaded. Copies properties to other property list. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Dispose()](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~Dispose().html) | Destructor for deterministic finalization of OptionFragmentPropertyList object. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |
| Public Method | [Exists](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.OptionFragmentPropertyList~Exists.html) | Overloaded. Checks property existence for used obiect. |
| Public Method | [getPropList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList~getPropList.html) | Internal method. (Inherited from [Eplan.EplApi.DataModel.UniversalPropertyList](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.UniversalPropertyList.html)) |


