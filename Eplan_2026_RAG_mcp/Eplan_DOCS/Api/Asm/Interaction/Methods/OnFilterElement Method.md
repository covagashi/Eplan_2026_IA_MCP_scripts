# OnFilterElement Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~OnFilterElement.html

---

Is called by framework to determine if oObject should be included in selection or will be highlighted.

Syntax

**C#**



public virtual bool OnFilterElement( 

   StorableObject oStorableObject

)

public:

virtual bool OnFilterElement( 

   StorableObject^ oStorableObject

)


#### Parameters

*oStorableObject*
:   [Eplan.EplApi.DataModel.StorableObject](Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.StorableObject.html) which will be examine.

#### Return Value

If `true` placement will be included into selection.

Remarks

This method is called by the framework when [IsPlacementFilterActive](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Ged.Interaction~IsPlacementFilterActive.html) is set to true and last returned **Eplan::EplApi::EServices::Ged:** contains **Eplan::EplApi::EServices::Ged::ReqeustCode:** or **Eplan::EplApi::EServices::Ged::ReqeustCode:**. Depending on the context in which this methods was call, the returned value determines if element will be highlighted or taken into selection.
