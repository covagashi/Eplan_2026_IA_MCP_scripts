# FUNCTION_EDP_ADAPTER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNCTION_EDP_ADAPTER().html

---

Eplan Data Portal: Configurator # 20287.

Syntax

**C#**



public PropertyValue FUNCTION_EDP_ADAPTER {get; set;}

public:

property PropertyValue^ FUNCTION_EDP_ADAPTER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Name of the external configurator that is accessed via the Data Portal. Such a configurator, for example, can be used to subsequently configure devices and macros that have been placed via the Data Portal.
