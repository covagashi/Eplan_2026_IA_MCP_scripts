# SYMBLIB_FRAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDSymbolLibraryPropertyList~SYMBLIB_FRAME().html

---

Plot frame to edit symbol # 15030.

Syntax

**C#**



public MDPropertyValue SYMBLIB_FRAME {get; set;}

public:

property MDPropertyValue^ SYMBLIB_FRAME {

   MDPropertyValue^ get();

   void set (    MDPropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The plot frame which is used for editing the symbol.

If you assign a value using the Application Programming Interface, please ensure that the relevant master data are available in the project.
