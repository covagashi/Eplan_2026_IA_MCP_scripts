# FUNC_TERMINALDESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_TERMINALDESCRIPTION(Int32).html

---

Connection point description # 20029.

Syntax

**C#**



public PropertyValue FUNC_TERMINALDESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_TERMINALDESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 100.

Shows the connection point descriptions of a connection point. A maximum of 100 connection point descriptions can be defined by using the index.
