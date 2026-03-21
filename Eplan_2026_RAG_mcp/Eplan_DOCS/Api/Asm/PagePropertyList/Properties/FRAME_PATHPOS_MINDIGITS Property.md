# FRAME_PATHPOS_MINDIGITS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.PagePropertyList~FRAME_PATHPOS_MINDIGITS().html

---

Number of characters for column / row # 12029.

Syntax

**C#**



public PropertyValue FRAME_PATHPOS_MINDIGITS {get; set;}

public:

property PropertyValue^ FRAME_PATHPOS_MINDIGITS {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.Int64.

Remarks

Number of characters for column and row numbers for numerical representation; fills in the "missing" digits with zeros, such as column number "1" in the three-digit representation: "001".
