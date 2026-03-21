# SYMB_PREVENTPLACEMENT Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolPropertyList~SYMB_PREVENTPLACEMENT().html

---

Prevent new placement # 16012.

Syntax

**C#**



public MDPropertyValue SYMB_PREVENTPLACEMENT {get; set;}

public:

property MDPropertyValue^ SYMB_PREVENTPLACEMENT {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.Boolean.

Remarks

Prevents the symbol being used in new schematics. If this property is activated, then the symbol is no longer shown in the project symbol selection, i.e. it can no longer be newly inserted. The symbol can still be edited in the master data.
