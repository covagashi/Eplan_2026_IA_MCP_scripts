# IsEmpty Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDPropertyValue~IsEmpty.html

---

Checks if property value is empty. If it's not it can be read.  
IMPORTANT: If property is indexed you have to specify index.

Syntax

**C#**



public bool IsEmpty {get;}

public:

property bool IsEmpty {

   bool get();

}


Remarks

On an indexed property you need to check IsEmpty for each property index, you want to get, e.g. `if(propertyValue[10].IsEmpty) { //Add your code here }` . If you want to make property empty, just create a new property and assign it to the Property: {object}.{Properties}.{property id} = new MDPropertyValue()
