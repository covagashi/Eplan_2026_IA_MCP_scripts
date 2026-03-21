# SYMB_CREATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_CREATIONDATE().html

---

Creation date # 16021.

Syntax

**C#**



public PropertyValue SYMB_CREATIONDATE {get; set;}

public:

property PropertyValue^ SYMB_CREATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Creation date of the symbol. The time is output in the local time of the user in accordance with the set time zone.
