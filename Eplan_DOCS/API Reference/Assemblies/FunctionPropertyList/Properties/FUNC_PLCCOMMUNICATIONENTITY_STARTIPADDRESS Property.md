# FUNC_PLCCOMMUNICATIONENTITY_STARTIPADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCOMMUNICATIONENTITY_STARTIPADDRESS(Int32).html

---

Start IP address # 20165.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_STARTIPADDRESS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_STARTIPADDRESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. Start IP address of the current project. Using the index, you can differentiate between up to 10 addresses.
