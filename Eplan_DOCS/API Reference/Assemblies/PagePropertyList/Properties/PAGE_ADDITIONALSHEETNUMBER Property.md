# PAGE_ADDITIONALSHEETNUMBER Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~PAGE_ADDITIONALSHEETNUMBER().html

---

Suppl. field: Sheet no. # 11033.

Syntax

**C#**



public PropertyValue PAGE_ADDITIONALSHEETNUMBER {get; set;}

public:

property PropertyValue^ PAGE_ADDITIONALSHEETNUMBER {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

The sheet number is used in addition to the page name and can consist of any combination of numbers and letters. It must be unique within an identifier block (same function designation / location designation). A start number must be entered, e.g. M1 or LM010, so that the property can be automatically assigned in reports.
