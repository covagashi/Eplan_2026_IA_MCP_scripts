# IsNamePart Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyDefinition~IsNamePart.html

---

Allows to check if a given property is name part.

Syntax

**C#**



public bool IsNamePart {get;}

public:

property bool IsNamePart {

   bool get();

}


#### Property Value

'¢ true = Property is name part

'¢ false = Property is not name part

Remarks

Can only be called after retrieving a property list from the given API class.

Example

**C#**

```


Function function = page.Functions[0]; // A valid Function object

bool isNamePart = function.Properties.FUNC_COUNTER.Definition.IsNamePart;

```
