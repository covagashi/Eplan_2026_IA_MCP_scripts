# FUNC_FULLNAME_WITH_CONNECTIONDESIGNATIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_FULLNAME_WITH_CONNECTIONDESIGNATIONS().html

---

Name (complete with connection point designations) # 20342.

Syntax

**C#**



public PropertyValue FUNC_FULLNAME_WITH_CONNECTIONDESIGNATIONS {get; set;}

public:

property PropertyValue^ FUNC_FULLNAME_WITH_CONNECTIONDESIGNATIONS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Outputs the full name and behind it, separated by a colon, all the connection point designations, for example "=EB3+ET1-X0:L1".
