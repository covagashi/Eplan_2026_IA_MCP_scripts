# FUNC_FULLCONNECTIONDESTINATIONNAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.E3D.Placement3DPropertyList~FUNC_FULLCONNECTIONDESTINATIONNAME(Int32).html

---

Name of target connection point (full) # 20048.

Syntax

**C#**



public PropertyValue FUNC_FULLCONNECTIONDESTINATIONNAME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_FULLCONNECTIONDESTINATIONNAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only. Property is indexed. Possible indexes are from 1 to 1000.

Provides the full name of a target connection point (max. 100 words allowed). This consists of the device tag plus the connection point designation. For terminals and pins, the terminal or pin designation is output in addition to the connection point designation.
