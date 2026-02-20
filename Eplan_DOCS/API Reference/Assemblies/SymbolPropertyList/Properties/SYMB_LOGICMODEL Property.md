# SYMB_LOGICMODEL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_LOGICMODEL().html

---

Target tracking # 16010.

Syntax

**C#**



public PropertyValue SYMB_LOGICMODEL {get; set;}

public:

property PropertyValue^ SYMB_LOGICMODEL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The logic model is stored for "virtual" functions, such as T-nodes and corner nodes. Target tracking determines the direction of the "paths" from one device to another for automatic reports.
