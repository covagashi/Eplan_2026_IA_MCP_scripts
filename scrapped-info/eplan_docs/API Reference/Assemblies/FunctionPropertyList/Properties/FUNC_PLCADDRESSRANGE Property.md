# FUNC_PLCADDRESSRANGE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCADDRESSRANGE().html

---

Address range (SIEMENS STEP 7 Classic) # 20432.

Syntax

**C#**



public PropertyValue FUNC_PLCADDRESSRANGE {get; set;}

public:

property PropertyValue^ FUNC_PLCADDRESSRANGE {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

Enter the size of the address range within the PLC controller that the card occupies here, for example "4 bytes". The property is entered on the "PLC box" tab of the property dialog. To this purpose enter the number of input / output bytes or the number of input / output bits that the PLC card uses by default, depending on the card type. For a card that has both inputs and outputs, the value of the inputs is entered here.
