# ARTICLE_ADDRESSRANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_ADDRESSRANGE().html

---

Address range (SIEMENS STEP 7 Classic) # 22106.

Syntax

**C#**



public PropertyValue ARTICLE_ADDRESSRANGE {get; set;}

public:

property PropertyValue^ ARTICLE_ADDRESSRANGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Property of a part variant. Enter the size of the address range within the PLC controller that the card occupies here, for example "4 bytes". The address range is entered on the "Properties" tab in parts management. To this purpose enter the number of input / output bytes or the number of input / output bits that the PLC card uses by default, depending on the card type. For a card that has both inputs and outputs, the value of the inputs is entered here.
