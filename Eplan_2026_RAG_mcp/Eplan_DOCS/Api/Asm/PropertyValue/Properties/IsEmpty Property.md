# IsEmpty Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PropertyValue~IsEmpty.html

---

Checks if the property is empty. If it's not, it could be read. IMPORTANT: If property is indexed you have to set the index.

Syntax

**C#**



public bool IsEmpty {get;}

public:

property bool IsEmpty {

   bool get();

}


Remarks

On an indexed property you need to check IsEmpty for each property index, you want to get, e.g. `if(propertyValue[10].IsEmpty){}`. If you want to empty a property, just create a new property and assign it to the Property: {object}.{Properties}.{property id} = new PropertyValue()

Example

**C#**

```
oConnection.Properties.CONNECTION_WIRENUMBER = new PropertyValue();

Console.Out.WriteLine(oConnection.Properties.CONNECTION_WIRENUMBER.IsEmpty.ToString()); // The property is empty

oConnection.Properties.CONNECTION_WIRENUMBER = 1;

Console.Out.WriteLine(oConnection.Properties.CONNECTION_WIRENUMBER.IsEmpty.ToString()); // Now the property isn't empty anymore

```
