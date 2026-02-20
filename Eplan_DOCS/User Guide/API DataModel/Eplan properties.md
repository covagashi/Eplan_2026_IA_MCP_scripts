# Eplan properties

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/EPLAN_Properties.html

---

The Eplan API allows accessing object properties, i.e. characteristics that are visible in GUI in the Properties dialog.

This is possible through the  Properties  property which is defined for almost all data model objects.

The list of all available properties for a particular object can be found in the properties of the  Properties  class (for example  Properties::AllMDSymbolLibraryPropIDs).

### Property types

Eplan properties are typed. The property values can have one of the following types:

- bool
- int
- double
- DateTime
- PointD
- MultiLangString

With help of the PropertyDefinition.PropertyType, you can determine the type of a property:

| PropertyDefinition.PropertyType | Corresponding .NET Framework type |
| --- | --- |
| Point |  |
| MultilangString |  |
| Variable | System.String |
| String | System.String |
| Time | System.DateTime |
| Bool | System.Boolean |
| Double | System.Double |
| Coord | System.Double |
| Long | System.Int64 |

The following example gets the type of a page property:

**C#**
```csharp
PropertyDefinition.PropertyType oPropType = oPage.Properties[Properties.Page.DESIGNATION_PLANT].Definition.Type;
```

### Setting and getting a property

The following example shows how to set a  bool  property:

**C#**
```csharp
oFunction.Properties[Properties.Function.FUNC_ARTICLE_SUPPRESSINPARTSLIST] = true;

oFunction.Properties(Properties.Function.FUNC_ARTICLE_SUPPRESSINPARTSLIST) = PropertyValue.op_Implicit(True)
```

The following example shows how to get a  MultiLangString  property (project description):

**C#**
```csharp
MultiLangString mlTest = oProject.Properties[Properties.Project.PROJ_INSTALLATIONNAME];
```

As an alternative syntax, you can also write:

**C#**
```csharp
MultiLangString mlTest = oProject.Properties.PROJ_INSTALLATIONNAME;
```

Finally an example that loops over all  string  properties of a project:

**C#**
```csharp
string strTmp = string.Empty;

 PropertyValue oPropValue;

 // Iterate over all project properties

 foreach (AnyPropertyId hPProp in Eplan.EplApi.DataModel.Properties.AllProjectPropIDs)

 {

     // Check if exists

     if (!m_oProject.Properties[hPProp].IsEmpty)

     {

         if (m_oProject.Properties[hPProp].Definition.Type == PropertyDefinition.PropertyType.String)

         {

             // Read string property

             oPropValue = m_oProject.Properties[hPProp];

             strTmp = oPropValue.ToString();

         }

     }

 }

For Each hPProp In  Eplan.EplApi.DataModel.Properties.AllProjectPropIDs

         oPropValue = m_oProject.Properties(hPProp)

         strTmp = oPropValue.ToString()

Next hPProp
```

### Setting name properties

In the case of the name properties, their setting must be done through the  .NameParts  property, for example:

**C#**

```


var functionBasePropertyList = new FunctionBasePropertyList();

// Set function name

functionBasePropertyList.DESIGNATION_LOCATION = "A1";

functionBasePropertyList.DESIGNATION_PLANT = "E01";

oNewFunction.NameParts = functionBasePropertyList;

```

The only difference is with  DESIGNATION\_PRODUCT  property. It needs to be set by  FUNC\_CODE  and  FUNC\_COUNTER  then it is composed from them.

### Conversion property value to another types

It is possible to get a property as a value of the .NET Framework type or Eplan API type (for example  Eplan.EplApi.Base.MultiLangString). It can be done explicitly by the  PropertyValue.To<type>(), for example:

```csharp
string strStringValue = oFunction.Properties.FUNC_CODE.ToString();
```

or implicitly:

```csharp
int nValue = oFunction.Properties.FUNC_CRAFT;
```

It is not allowed to convert the property value to a non-matching type, for example  MultiLangString  to  int. In such cases, a runtime warning is generated (as an Eplan system message) or an exception is thrown:

```csharp
string strValue = oArticle.Properties.ARTICLE_DEPTH.ToString(); // Will generate a system warning
 double dValue = oArticle.Properties.ARTICLE_DEPTH.ToDouble(); // OK
 string strValue2 = oArticle.Properties.ARTICLE_DEPTH.ToDouble().ToString("0.00", CultureInfo.InvariantCulture); // Also OK
```

Here is a table that shows which conversions are allowed:

|  | Eplan.EplApi.Base.Point    PropertyValue.ToPointD() | Eplan.EplApi.Base.MultiLangString  PropertyValue.ToMultiLangString() | System.String                     PropertyValue.ToString() | System.DateTime             PropertyValue.ToTime() | bool                                   PropertyValue.ToBool() | double                                   PropertyValue.ToDouble() | long                               PropertyValue.ToInt() |
| --- | --- | --- | --- | --- | --- | --- | --- |
| PropertyType.Point | ' |  |  |  |  |  |  |
| PropertyType.MultilangString |  | ' |  |  |  |  |  |
| PropertyType.Variable |  |  | ' |  |  |  |  |
| PropertyType.String |  |  | ' |  |  |  |  |
| PropertyType.Time |  |  |  | ' |  |  |  |
| PropertyType.Bool |  |  |  |  | ' |  |  |
| PropertyType.Double |  |  |  |  |  | ' |  |
| PropertyType.Coord |  |  |  |  |  | ' |  |
| PropertyType.Long |  |  |  |  |  | ' | ' |

### Indexed properties

Properties can have more than one value. In this case, we call it an "**indexed property**". The index is passed after the property designation. The example gets the index 1 of the function property  FUNC\_CONNECTIONDESIGNATION:

**C#**
```csharp
strConnDes1 = oFunction.Properties[Properties.Function.FUNC_CONNECTIONDESIGNATION, 1].ToString();

strConnDes1 = oFunction.Properties(Properties.Function.FUNC_CONNECTIONDESIGNATION, 1).ToString()
```

Alternatively:

**C#**
```csharp
strConnDes1 = oFunction.Properties.FUNC_CONNECTIONDESIGNATION[1].ToString();

strConnDes1 = oFunction.FUNC_CONNECTIONDESIGNATION(1).ToString()
```

### User-defined properties

Eplan API supports also user-defined properties that were introduced in Eplan 2.4.

The following enhancements were added due to it:

- Access to properties by case-sensitive  string  identifiers:

```csharp
// Setting user-defined property
 oProject.Properties["EPLAN.Project.UserSupplementaryField1"] = "test1";
 // Getting user-defined property
 string strValue = oProject.Properties["EPLAN.Project.UserSupplementaryField1"];
```

- UserDefinedPropertyDefinition  class extending  PropertyDefinition. The class allows creating custom property definitions or accessing information from existing ones:

```csharp
// Create a new property definition:
 UserDefinedPropertyDefinition oUDPDProject = UserDefinedPropertyDefinition.Create(oCurrentProject, "API.Property.Project", UserDefinedPropertyDefinition.Enums.ClientType.Project);
 oCurrentProject.Properties["API.Property.Project"] = "something";
 
 var oCategory = oProject.Properties["EPLAN.Project.UserSupplementaryField1"].Category;  // Gets the category information
 MultiLangString strDisplayedName = oProject.Properties["EPLAN.Project.UserSupplementaryField1"].DisplayedName; // Gets the name that is displayed in the GUI properties window
```

- Import / export property definitions (ExportPropertyDefinitions,  ImportPropertyDefinitions  from the  PrePlanningService  class)

- The new  AnyPropertyId  constructor allowing to create an ID of a user-defined property:

```csharp
public AnyPropertyId(
     ref Eplan::EplApi::DataModel::Project pProject,
     ref System::String strUserDefiniedPropertyIdentName
 );
```

- The  AnyPropertyId.AsString  propety to get the identifying name from  AnyPropertyId  which represents a user-defined property.

- Actions that expect the ID of a property were extended to support also identifying names. Please go to the "[API Reference](API Reference.html)" section for details.

### Accessing default user-defined properties

Some user-defined properties are created by default, for example "EPLAN.Project.UserSupplementaryField1".

They have the same internal IDs as the old  \*\_CUSTOM\_SUPPLEMENTARYFIELD\*  properties (like "PROJ\_CUSTOM\_SUPPLEMENTARYFIELD01", etc).

The use of old identifiers is still possible for compatibility reasons, but they generate warnings and will be removed in the future.

Therefore, please replace them with the new IDs to avoid problems in forthcoming Eplan versions:

```csharp
MultiLangString oMLS = oProject.Properties.PROJ_CUSTOM_SUPPLEMENTARYFIELD01;             // Old code, generates warning
 MultiLangString oMLS = oProject.Properties["EPLAN.Project.UserSupplementaryField1"];     // New code
 
 m_oTestProject.Properties.FUNC_ARTICLE_CUSTOM_SUPPLEMENTARYFIELD01[1] = strTestValue;     // Old code, generates warning:
 ArticleReference oArticleReference = oProject.ArticleReferences[0];                       // New code
 oArticleReference.Properties["EPLAN.PartRef.UserSupplementaryField1"] = strTestValue;
 oArticleReference.StoreToObject();
```

### Accessing user-defined properties through ArticleReference parent object

In the case of an  ArticleReference  object, when accessing a user-defined property through a parent  ArticleReference, it is necessary to add the  EPLAN.ArticleRef.  prefix to its identifying name. In addition, an index must be provided to indicate the position of the  ArticleReference  in the parent object.

```csharp
var propertyValue1 = oArticleReference.Properties["UserProperty.1"].ToString();  // Accessing user-defined property from ArticleReference
 var propertyValue2 = oArticleReference.Parent.Properties["EPLAN.ArticleRef.UserProperty.1"][1].ToString(); // Accessing user-defined property from a parent of the ArticleReference
```