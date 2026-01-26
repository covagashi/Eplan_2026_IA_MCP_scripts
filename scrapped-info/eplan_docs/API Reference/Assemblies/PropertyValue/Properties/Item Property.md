# Item Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Item.html

---

Returns or sets the object of a persistent [PropertyValue](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue.html) which points to a specific index. To use the Item property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property).

Syntax

**C#**



public PropertyValue this[ 

   int index

]; {get; set;}

public:

property PropertyValue^ default [int] {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

Exceptions

| Exception | Description |
| --- | --- |
| [InvalidIndexException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.InvalidIndexException.html) | InvalidIndexException |
| [NotIndexedPropertyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NotIndexedPropertyException.html) | NotIndexedPropertyException |
| [IndexedPropertyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IndexedPropertyException.html) | IndexedPropertyException |
| [System.InvalidOperationException](#) | Is thrown when set is used on a transient property. |

Remarks

If an invalid index is used, an exception of type InvalidIndexException is thrown. If no index is specified for an indexed property, an exception of type IndexedPropertyException will be thrown.

Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

PropertyValue propertyValue = function.Properties.FUNC_CONNECTIONDESIGNATION;

if(propertyValue.Definition.IsIndexed && propertyValue.Definition.MaxIndex >= 2)

{

    // We will let the variable propertyElement point to an indexed property, so an index is needed to get the logical value.

    PropertyValue propertyElement = propertyValue[1]; // Now propertyElement points to the first index of the FUNC_CONNECTIONDESIGNATION property

    string sProperty = propertyElement.ToString();

}

```
