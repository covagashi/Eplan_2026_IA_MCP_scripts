# ARTICLE_ADDRESSRANGE_2 Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADDRESSRANGE_2().html

---

Address range 2 (SIEMENS STEP 7 Classic) # 22261.

Syntax

**C#**



public PropertyValue ARTICLE_ADDRESSRANGE_2 {get; set;}

public:

property PropertyValue^ ARTICLE_ADDRESSRANGE_2 {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. For PLC cards that have both inputs and outputs, you can use this property to specify a separate address range for the outputs. Enter the I/O address range here from which data is transmitted or where the data can be written. The address range is entered on the "Properties" tab in parts management. For this property to be reported during addressing, the Separate address range for inputs and outputs check box must be deactivated in the PLC-specific settings.
