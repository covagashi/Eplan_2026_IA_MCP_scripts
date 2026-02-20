# FUNC_PLCSYMBOLICADDRESS_CALCULATED Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCSYMBOLICADDRESS_CALCULATED().html

---

Symbolic address (determined) # 20403.

Syntax

**C#**



public PropertyValue FUNC_PLCSYMBOLICADDRESS_CALCULATED {get; set;}

public:

property PropertyValue^ FUNC_PLCSYMBOLICADDRESS_CALCULATED {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Using target tracking, the connected sensor (for an input) or actuator (for an output) is found, and its identifying DT is automatically entered as the symbolic address. If no sensor / actuator is found, the identifying DT of the last connected function before the search was canceled is entered. For the determined symbolic address, information from the connection point logic is used to decide at which connection point of the function the search for a sensor / actuator is to be continued.
