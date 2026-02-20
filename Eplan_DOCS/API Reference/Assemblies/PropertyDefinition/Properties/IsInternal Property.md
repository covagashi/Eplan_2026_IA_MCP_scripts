# IsInternal Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsInternal.html

---

Allows to check if a given property is marked as internal. Don't use this property.

Syntax

**C#**



public bool IsInternal {get;}

public:

property bool IsInternal {

   bool get();

}


#### Property Value

'¢ true = Property is internal

'¢ false = Property is not internal

Remarks

Can only be called after retrieving a property list from the given API class.

Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

bool isInternal = function.Properties.FUNC_COUNTER.Definition.IsInternal;

```
