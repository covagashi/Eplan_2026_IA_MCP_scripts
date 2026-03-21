# CONNECTION_TYPEOFENDSTOP_DESTINATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~CONNECTION_TYPEOFENDSTOP_DESTINATION().html

---

Wire termination processing target # 31052.

Syntax

**C#**



public PropertyValue CONNECTION_TYPEOFENDSTOP_DESTINATION {get; set;}

public:

property PropertyValue^ CONNECTION_TYPEOFENDSTOP_DESTINATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Specifies for the target connection point of the connection the manner in which the connection is to be closed, e.g., with a conductor sleeve or a cable lug. This property is needed for transmissions to the manufacturing machines or for reports for manual manufacturing.
