# FUNC_CONNECTIONDIMENSIONS Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1484.html

---

Connection dimension # 20374.

Syntax

**C#**



public MDPropertyValue FUNC_CONNECTIONDIMENSIONS( 

   int index

) {get; set;}

public:

property MDPropertyValue^ FUNC_CONNECTIONDIMENSIONS {

   MDPropertyValue^ get(int index);

   void set (int index, MDPropertyValue^ value);

}


#### Parameters

*index*

#### Property Value

Returns property value of type System.String.

Remarks

Property is indexed. Possible indexes are from 1 to 1000.
