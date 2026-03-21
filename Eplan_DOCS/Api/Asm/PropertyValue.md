# PropertyValue

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html

---

Class holding value of P8 property.

Inheritance Hierarchy

[System.Object](#)  
   **Eplan.EplApi.DataModel.PropertyValue**

Syntax

**C#**



[DefaultMember("Item")]

public sealed class PropertyValue

[DefaultMember("Item")]

public ref class PropertyValue sealed


Remarks

Its object can be created and assigned to the following types:

'¢ int

'¢ string

'¢ double

'¢ bool

'¢ DateTime

'¢ [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html)

'¢ [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html)

By definition of several conversion operators from and to other types, it simplifies access to P8 properties stored inside all kinds of PropertyList classes. The user does not have to use this class explicitly, it allows to simply assign a P8 property value to a user defined variable (See example below).

The PropertyValue object can appear in 3 different states. Please take a look at the corresponding examples below.

Example

1st state: Transient ' created by the user

**C#**

```
// This will create a new transient property and assign it to the variable oTransientProperty. 

// If you wish to change the value of the property, use the method Eplan::EplApi::DataModel::PropertyValue::Set.

PropertyValue oTransientProperty = oFunction.Properties[Properties.Function.FUNC_COMMENT];

oTransientProperty = oTransientProperty + " additional comment";
```

Again 1st state: Transient ' created by the user

**C#**

```
// This object is not connected with any property list or StorableObject. That is why this type of property is called "transient" (or "offline").

PropertyValue oTransientProperty = new PropertyValue();

oTransientProperty.Set("Setting a value to a transient property.");

```

2nd state: Persistent ' collected from property list

**C#**

```
// The object stays connected to the property list and is therefore called a "persistent" (or "online") property.

// In this case, the usage of Eplan::EplApi::DataModel::PropertyValue::Set updates the values in the original locations.

FunctionPropertyList oFunctionPropertyList = new FunctionPropertyList();

PropertyValue oPersistentProperty2 = oFunctionPropertyList["EPLAN.Project.UserSupplementaryField1"];

// oFunctionPropertyList["EPLAN.Project.UserSupplementaryField1"] contains an empty string

// oPersistentProperty2 contains an empty string

oFunctionPropertyList["EPLAN.Project.UserSupplementaryField1"] = "Test_1";

// oPersistentProperty2 also contains the value "Test_1"

oPersistentProperty2.Set("Test_2");

// oFunctionPropertyList["EPLAN.Project.UserSupplementaryField1"] also contains the value "Test_2"

```

3rd state: Persistent ' collected from any data model object

**C#**

```
// The object stays connected to the data model object and is therefore called a "persistent" (or "online") property.

// In this case, the usage of Eplan::EplApi::DataModel::PropertyValue::Set updates the values in the original locations.

PropertyValue oPersistentProperty = m_oTestProject.Properties["EPLAN.Project.UserSupplementaryField1"];

// m_oTestProject.Properties.PROJ_CUSTOM_SUPPLEMENTARYFIELD01 contains an empty string

m_oTestProject.Properties["EPLAN.Project.UserSupplementaryField1"] = "Test1";

// Now oPersistentProperty also has the value "Test1"

oPersistentProperty.Set("Test2");

// Now m_oTestProject.Properties.PROJ_CUSTOM_SUPPLEMENTARYFIELD01 also has the value "Test2"

```

Assigning and retrieving the property value

**C#**

```


Article article = myProject.Articles[0]; // A valid Article object

// Below here the PropertyValue is implicitly created from int '2' and assigned to the property list.

article.Properties[Properties.Article.ARTICLE_HEIGHT] = 2; 

// Below here the PropertyValue is implicitly created from string "5" and assigned to the property list.

article.Properties[Properties.Article.ARTICLE_HEIGHT] = "5";

// Below here the PropertyValue is read form the property list and implicitly converted to string.

string s = article.Properties[Properties.Article.ARTICLE_HEIGHT]; 

// Below here the PropertyValue is read form the property list and implicitly converted to int.

int i = article.Properties[Properties.Article.ARTICLE_HEIGHT]; 

```

Public Constructors

|  | Name | Description |
| --- | --- | --- |
| Public Constructor | [PropertyValue Constructor](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~_ctor().html) | Default constructor. Creates the PropertyValue object. |



Public Properties

|  | Name | Description |
| --- | --- | --- |
| Public Property | [Definition](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Definition.html) | Returns an object that provides information about the property and its definition. The information includes: name of the property, its data type, whether it's indexed or not, whether it's read-only, upper/lower bounds of values for numerical properties. To use the Definition property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [Id](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Id.html) | Returns the P8 property descriptor (id and index) that the object points to. To use the Id property, the PropertyValue object must point to a project property (persistent property). Transient PropertyValue objects don't have descriptors because they point directly to a value. A transient PropertyValue is created by operator and takes values of base types. |
| Public Property | [Indexes](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Indexes.html) | Returns the valid / actually used indexes. It can be used with the PropertyValue::operator []. To use the Indexes property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [IsEmpty](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~IsEmpty.html) | Checks if the property is empty. If it's not, it could be read. IMPORTANT: If property is indexed you have to set the index. |
| Public Property | [Item](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Item.html) | Returns or sets the object of a persistent [PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) which points to a specific index. To use the Item property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [LastUsedIndex](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~LastUsedIndex.html) | Returns the number of the highest used index. Indexes start at 1. If the property is not indexed or there is no used index, LastUsedIndex is 0. To use the LastUsedIndex property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property). |
| Public Property | [Parent](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Parent.html) | Property list to which this property value is connected. |



Public Methods

|  | Name | Description |
| --- | --- | --- |
| Public Method | [CopyTo](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~CopyTo.html) | Copies property value to destination including all indexes. If source property is indexed destination has to be also indexed. Only indexes from 1 to minimum of both MaxIndex are copied. |
| Public Method | [Dispose](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Dispose().html) | Destructor for deterministic finalization of PropertyValue object. |
| Public Method | [Equals](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Equals.html) | Overloaded. Determines whether two PropertyValues objects have the same value. |
| Public Method | [GetDisplayString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~GetDisplayString.html) | Display value of property as [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [GetHashCode](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~GetHashCode.html) | Serves as the default hash function. |
| Public Method | [Set](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Set.html) | Overloaded. Sets [System.DateTime](#) value in PropertyValue object. |
| Public Method | [ToBool](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToBool.html) | Used in conversion of the PropertyValue object to `bool`. |
| Public Method | [ToDouble](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToDouble.html) | Used in conversion of the PropertyValue object to `double`. |
| Public Method | [ToInt](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToInt.html) | Used in conversion of the PropertyValue object to `int`. |
| Public Method | [ToMultiLangString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToMultiLangString.html) | Used in conversion of the PropertyValue object to [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html). |
| Public Method | [ToPointD](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToPointD.html) | Used in conversion of the PropertyValue object to [Eplan.EplApi.Base.PointD](Eplan.EplApi.Baseu~Eplan.EplApi.Base.PointD.html). |
| Public Method | [ToString](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToString.html) | Overloaded. Returns string value of this property. When type of property is MultiLangString then only the specified language is returned. In case of a transient PropertyValue object, the stored value is returned without any cast. When property can not be read, `default_value` is returned instead of throwing an `EmptyPropertyException` . |
| Public Method | [ToTime](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~ToTime.html) | Used in conversion of the PropertyValue object to `time`. |



Public Operators

|  |  |
| --- | --- |
| public Operator [Equality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~op_Equality.html) | Determines whether two PropertyValues objects have the same value. |
| public Operator [Implicit Type Conversion](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~op_Implicit.html) | Overloaded. Used in conversion of the PropertyValue object to `int`. |
| public Operator [Inequality](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~op_Inequality.html) |  |


