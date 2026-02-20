# GetSelectedObject Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.SelectionSet~GetSelectedObject.html

---

\Returns the first selected object.

Syntax

**C#**



public StorableObject GetSelectedObject( 

   bool bFirst

)

public:

StorableObject^ GetSelectedObject( 

   bool bFirst

)


#### Parameters

*bFirst*
:   true\: the first object. false\: the next object.

#### Return Value

Returns StorableObject of the selected element or null.

Remarks

When a node is selected, this is only the first element.
