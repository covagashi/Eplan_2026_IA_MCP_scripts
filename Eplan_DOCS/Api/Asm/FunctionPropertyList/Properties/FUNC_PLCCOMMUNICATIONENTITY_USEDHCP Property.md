# FUNC_PLCCOMMUNICATIONENTITY_USEDHCP Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCOMMUNICATIONENTITY_USEDHCP(Int32).html

---

Use DHCP # 20182.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_USEDHCP( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_USEDHCP {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Boolean.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. The Dynamic Host Configuration Protocol (DHCP) facilitates the dynamic assignment of an IP address and other configuration parameters to computers in a network (e.g. internet or LAN) using the relevant server.
