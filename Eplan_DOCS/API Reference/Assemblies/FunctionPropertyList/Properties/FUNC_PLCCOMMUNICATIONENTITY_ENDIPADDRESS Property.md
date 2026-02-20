# FUNC_PLCCOMMUNICATIONENTITY_ENDIPADDRESS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCOMMUNICATIONENTITY_ENDIPADDRESS(Int32).html

---

End IP address # 20169.

Syntax

**C#**



public PropertyValue FUNC_PLCCOMMUNICATIONENTITY_ENDIPADDRESS( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCOMMUNICATIONENTITY_ENDIPADDRESS {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 10.

This property is no longer in use and only taken into consideration in old projects. End IP address of the current project. Using the index, you can differentiate between up to 10 addresses.
