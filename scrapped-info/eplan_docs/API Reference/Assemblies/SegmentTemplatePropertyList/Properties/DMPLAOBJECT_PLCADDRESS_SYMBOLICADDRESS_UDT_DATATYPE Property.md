# DMPLAOBJECT_PLCADDRESS_SYMBOLICADDRESS_UDT_DATATYPE Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1089.html

---

Symbolic address (single component) # 44053.

Syntax

**C#**



public PropertyValue DMPLAOBJECT_SYMBOLICADDRESS_PART {get; set;}

public:

property PropertyValue^ DMPLAOBJECT_SYMBOLICADDRESS_PART {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

At segments, a single component of the symbolic address can be entered. These single components are linked at the PLC inputs and outputs of the planning objects starting with the top node and provide the automatically determined symbolic address.
