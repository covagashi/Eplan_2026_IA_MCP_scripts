# PROJ_CUSTOMER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ProjectPropertyList~PROJ_CUSTOMER().html

---

Customer # 10370.

Syntax

**C#**



public PropertyValue PROJ_CUSTOMER {get; set;}

public:

property PropertyValue^ PROJ_CUSTOMER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

This property is populated during the data transfer of projects from EPLAN 5. It is only required for EPLAN 5 due to compatibility reasons and is no longer used in new projects. If data has been backed up in EPLAN 5 and the project has been filed off, the name of the customer to whom the project was delivered is indicated here.
