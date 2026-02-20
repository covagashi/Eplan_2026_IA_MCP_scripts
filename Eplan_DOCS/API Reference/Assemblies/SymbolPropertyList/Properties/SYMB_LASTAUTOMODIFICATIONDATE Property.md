# SYMB_LASTAUTOMODIFICATIONDATE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MasterData.SymbolPropertyList~SYMB_LASTAUTOMODIFICATIONDATE().html

---

Modification date (automatic) # 16023.

Syntax

**C#**



public PropertyValue SYMB_LASTAUTOMODIFICATIONDATE {get; set;}

public:

property PropertyValue^ SYMB_LASTAUTOMODIFICATIONDATE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.DateTime.

Remarks

Date of last changes to the symbol. The time is output in the local time of the user in accordance with the set time zone.
