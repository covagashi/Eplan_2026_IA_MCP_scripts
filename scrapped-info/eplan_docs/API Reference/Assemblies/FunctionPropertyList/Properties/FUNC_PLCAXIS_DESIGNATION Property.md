# FUNC_PLCAXIS_DESIGNATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCAXIS_DESIGNATION(Int32).html

---

Drive # 20576.

Syntax

**C#**



public PropertyValue FUNC_PLCAXIS_DESIGNATION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCAXIS_DESIGNATION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 64.

Drive systems consist of different components such as motors, converters, sensors etc. Such components belonging to a drive can be grouped by means of this property. Through the index up to 64 drives can be assigned to a function.
