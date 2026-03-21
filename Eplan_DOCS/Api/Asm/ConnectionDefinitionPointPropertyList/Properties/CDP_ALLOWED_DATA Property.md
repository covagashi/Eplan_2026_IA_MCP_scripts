# CDP_ALLOWED_DATA Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CDP_ALLOWED_DATA().html

---

Valid data # 31045.

Syntax

**C#**



public PropertyValue CDP_ALLOWED_DATA {get; set;}

public:

property PropertyValue^ CDP_ALLOWED_DATA {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Specifies the data that may be entered at the connection definition point:

0 = All data

1 = No connection designation

2 = Only connection designation.
