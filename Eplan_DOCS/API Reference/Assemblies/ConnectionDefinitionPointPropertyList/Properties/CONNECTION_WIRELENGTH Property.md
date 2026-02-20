# CONNECTION_WIRELENGTH Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionDefinitionPointPropertyList~CONNECTION_WIRELENGTH().html

---

Connection: Length with unit # 31003.

Syntax

**C#**



public PropertyValue CONNECTION_WIRELENGTH {get; set;}

public:

property PropertyValue^ CONNECTION_WIRELENGTH {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Length of a connection with specification of the displayed measuring unit. If you do not enter a unit, the unit of length specified in the project settings is used.
