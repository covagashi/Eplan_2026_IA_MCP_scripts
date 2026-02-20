# LastUsedIndex Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~LastUsedIndex.html

---

Returns the number of the highest used index. Indexes start at 1. If the property is not indexed or there is no used index, LastUsedIndex is 0. To use the LastUsedIndex property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property).

Syntax

**C#**



public int LastUsedIndex {get;}

public:

property int LastUsedIndex {

   int get();

}


Exceptions

| Exception | Description |
| --- | --- |
| [NotIndexedPropertyException](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.NotIndexedPropertyException.html) | Thrown when property is not indexed. |

Remarks

When there are unused indexes between the used ones, this property will return the last one before the first empty property index.

For example:

1st, 2nd and 10th indexes are used so LastUsedIndex will return 2nd index as last used.

Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

PropertyValue propertyValue = function.Properties.FUNC_CONNECTIONDESIGNATION;

if (propertyValue.Definition.IsIndexed)

{

    for (int i = propertyValue.LastUsedIndex ; i >= 1 ; --i)

    {

        PropertyValue propertyElement = propertyValue[i];

        string sProperty = propertyElement.ToString();

    }

}

```
