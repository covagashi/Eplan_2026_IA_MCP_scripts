# FUNC_ARTICLE_RATED_OUTPUT_TORQUE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ConnectionPropertyList~FUNC_ARTICLE_RATED_OUTPUT_TORQUE(Int32).html

---

Nominal output torque # 26465.

Syntax

**C#**



public PropertyValue FUNC_ARTICLE_RATED_OUTPUT_TORQUE( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_ARTICLE_RATED_OUTPUT_TORQUE {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 50.

Maximum torque that a gearbox or a drive unit can transmit continuously under normal operating conditions. Torque available after transfer by the transmission. The torque is specified in Newton meters (Nm).
