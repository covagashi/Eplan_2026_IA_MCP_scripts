# Indexes Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~Indexes.html

---

Returns the valid / actually used indexes. It can be used with the PropertyValue::operator []. To use the Indexes property, the PropertyValue object must point to a project property (persistent property).It cannot point to an individual value (transient property).

Syntax

**C#**



public int[] Indexes {get;}

public:

property array<int>^ Indexes {

   array<int>^ get();

}


Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

// Get all used indexes for indexed property FUNC_CONNECTIONDESIGNATION

int[] indexes = function.Properties.FUNC_CONNECTIONDESIGNATION.Indexes;

// Iterate over all indexes of FUNC_CONNECTIONDESIGNATION property

PropertyValue propertyValue = function.Properties.FUNC_CONNECTIONDESIGNATION;

if(propertyValue.Definition.IsIndexed)

{

    foreach (int index in propertyValue.Indexes)

    {

        PropertyValue propertyElement = propertyValue[index];

        string sProperty = propertyElement.ToString();

    }

}

```
