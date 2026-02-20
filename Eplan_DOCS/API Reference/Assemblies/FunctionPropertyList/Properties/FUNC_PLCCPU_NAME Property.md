# FUNC_PLCCPU_NAME Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.FunctionPropertyList~FUNC_PLCCPU_NAME(Int32).html

---

CPU: Name # 20253.

Syntax

**C#**



public PropertyValue FUNC_PLCCPU_NAME( 

   int index

) {get; set;}

public:

property PropertyValue^ FUNC_PLCCPU_NAME {

   PropertyValue^ get(int index);

   void set (int index, PropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 128.

Name of the central processing unit (the processor) of a PLC controller. The CPU name has to be unique within the Eplan project. For all PLC boxes always enter the complete CPU name in the form [Configuration project].[Station ID].[CPU identifier], for example "Siemens SIMATIC S7.Station 300.1".

At PLC boxes that do not represent a CPU, but rather input or output cards, enter the name of the associated CPU. All addresses with the same CPU belong in an assignment list. By entering different CPUs, multiple PLC controls can be managed in one project. When you plan several PLC controls in a project, it is therefore necessary to identify all PLC boxes via this property.
