# AddPropertyCondition Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.MasterDatau~Eplan.EplApi.MasterData.MDObjectFilter~AddPropertyCondition.html

---

Add a property condition to the object filter. Adding multiple conditions without a separating OR-condition means, they must all match (logical AND-combination)

Syntax

**C#**



public void AddPropertyCondition( 

   MDAnyPropertyId propertyId,

   MDObjectFilter.CompareOperator nCompareOperator,

   string value

)

public:

void AddPropertyCondition( 

   MDAnyPropertyId^ propertyId,

   MDObjectFilter.CompareOperator nCompareOperator,

   String^ value

)


#### Parameters

*propertyId*


*nCompareOperator*


*value*
