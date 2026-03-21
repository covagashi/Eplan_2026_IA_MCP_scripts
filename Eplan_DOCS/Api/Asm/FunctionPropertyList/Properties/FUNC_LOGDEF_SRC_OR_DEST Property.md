# FUNC_LOGDEF_SRC_OR_DEST Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_LOGDEF_SRC_OR_DEST(Int32).html

---

Connection point logic: Source / target # 20611.

Syntax

**C#**



public PropertyValue FUNC_LOGDEF_SRC_OR_DEST( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_LOGDEF_SRC_OR_DEST {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.Int64.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
