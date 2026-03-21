# FUNC_CONNECTIONDESCRIPTION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_CONNECTIONDESCRIPTION(Int32).html

---

Function: Connection point description # 20023.

Syntax

**C#**



public PropertyValue FUNC_CONNECTIONDESCRIPTION( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_CONNECTIONDESCRIPTION {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.

Shows the connection point descriptions of the function. The index can be used to define a max. of 100 sets of connection point descriptions.
