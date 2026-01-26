# MDPropertyValue

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html

---

Class holding value of P8 Master Data property.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.MasterData.MDPropertyValue**

Syntax

**C#**



[DefaultMember("Item")]

public sealed class MDPropertyValue

[DefaultMember("Item")]

public ref class MDPropertyValue sealed


Remarks

An MDPropertyValue object can be in one of three states:  
'¢ 1 Transient ' created by the user. This object is not connected with any property list or `object stored in the master data database`. It is a transient property (also called "offline").  
'¢ 2 Persistent ' collected from a property list. It is a persistent property (also called "online").  
'¢ 3 Persistent ' collected from any master data object. It is a persistent property (also called "online").  
  
In the two last cases (persistent properties), the overloads of the [MDPropertyValue.Set](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set.html) method set the values in the original locations.  
  
  
An MDPropertyValue object can hold values of the following types:  
'¢ int  
'¢ string  
'¢ double  
'¢ bool  
'¢ DateTime  
'¢ [MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html)  
'¢ [PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html)  
  
The class implements conversion operators that will simplify the access to P8 property values stored inside of an MDPropertyList class object.  
The user does not have to use this class explicitly, it allows to assign P8 property values in a simple way (see example).  
Value of the property can be changed using overloads of the [MDPropertyValue.Set](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set.html) method:  
'¢ [Set(Double)](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(Double).html)  
'¢ [Set(Boolean)](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(Boolean).html)  
'¢ [Set(String)](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set(String).html)  
'¢ etc.

Example

Creating transient properties: Creating persistent properties:

**C#**

```
MDPropertyValue oPv = oPart.Properties[Properties.MDPartsDatabaseItem.ARTICLE_DESCR1];

oPv = oPv + " additional comment";

// Creates a new transient property value object and assigns it to the variable oPv.
```

**C#**

```
MDPart oPart = m_MDPartsDatabase.Parts[0]; // A valid master data part object

// Here, the MDPropertyValue object is implicitly created from an int constant ('5') and is assigned to the property list.

oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT] = 5;

// Here, the MDPropertyValue object is implicitly created from a string constant ("7") and is assigned to the property list.

oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT] = "7";

// Here, the MDPropertyValue object is read form a property list and implicitly converted to string.

string s = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT];

// Here, the MDPropertyValue object is read form a property list and implicitly converted to int.

int i = oPart.Properties[Eplan.EplApi.MasterData.Properties.MDPartsDatabaseItem.ARTICLE_HEIGHT];
```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [MDPropertyValue Constructor](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~_ctor().html) | Default constructor. Creates a MDPropertyValue object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Definition](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Definition.html) | Returns an object that provides information about the property and its definition.  The information includes: name of the property, it's data type, whether it is indexed or not, whether it is read-only, upper/lower bounds of values for numerical properties. |
| Public Property | [Id](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Id.html) | Returns P8-Property descriptor (id and index) of the object.  Offline MDPropertyValue objects don't have descriptors because they point to value directly. An offline MDPropertyValue is created by operators that take base types values. |
| Public Property | [Indexes](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Indexes.html) | Returns array of indexes for which property value is not empty. It can be used with MDPropertyValue::operator []; |
| Public Property | [IsEmpty](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~IsEmpty.html) | Checks if property value is empty. If it's not it can be read.  IMPORTANT: If property is indexed you have to specify index. |
| Public Property | [Item](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Item.html) | Returns [MDPropertyValue](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue.html) object at specified index. |
| Public Property | [LastUsedIndex](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~LastUsedIndex.html) | Returns number of highest used index. Index value starts from 1. If it is a not indexed-property or if their index is not used, LastUsedIndex is 0.  An object of MDPropertyValue has to point to online property. |
| Public Property | [Parent](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Parent.html) | Property list to which this property value is connected. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [Dispose](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Dispose().html) | Destructor for deterministic finalization of MDPropertyValue object. |
| Public Method | [GetDisplayString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~GetDisplayString.html) | Display value of property as [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [Set](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~Set.html) | Overloaded. Sets [System.DateTime](#) value in MDPropertyValue object. |
| Public Method | [ToBool](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToBool.html) | Converts this MDPropertyValue object to `System::Boolean`. |
| Public Method | [ToDouble](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToDouble.html) | Converts this MDPropertyValue object to `doule`. |
| Public Method | [ToInt](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToInt.html) | Converts this MDPropertyValue object to `long`. |
| Public Method | [ToMultiLangString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToMultiLangString.html) | Converts this MDPropertyValue object to [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [ToPointD](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToPointD.html) | Conversion this MDPropertyValue object to [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html). |
| Public Method | [ToString](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToString.html) | Overloaded. Returns string value of this property. When type of property is MultiLangString then only specified language is returned. In case of offline MDPropertyValue object, stored value is returned without any cast. When property can not be read, `default_value` is returned instead of throwing `MDEmptyPropertyException` . |
| Public Method | [ToTime](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~ToTime.html) | Converts this MDPropertyValue object to `System::DateTime`. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Implicit Type Conversion](Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~op_Implicit.html) | Overloaded. Converts MDPropertyValue object to `long`. |


