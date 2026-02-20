# ARTICLE_PLCGROUP_DATALENGTH_INPUTS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_PLCGROUP_DATALENGTH_INPUTS().html

---

PLC device: Data length (inputs) # 20571.

Syntax

**C#**



public PropertyValue ARTICLE_PLCGROUP_DATALENGTH_INPUTS {get; set;}

public:

property PropertyValue^ ARTICLE_PLCGROUP_DATALENGTH_INPUTS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Required length in the address space for the inputs of the PLC card. The specification is in bits. The address range of the PLC card is determined from the data length together with the start address. Note that there are PLC cards, for example technology modules, which are only assigned to a few inputs / outputs, but still require a larger address range than the one currently occupied. Always enter the maximum required length for the address range of the inputs here.
