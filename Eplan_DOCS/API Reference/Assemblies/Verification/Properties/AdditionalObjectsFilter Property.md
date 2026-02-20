# AdditionalObjectsFilter Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.Verification~AdditionalObjectsFilter.html

---

Type of class which filters objects that are additionally passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method.

Syntax

**C#**



public virtual Type AdditionalObjectsFilter {get;}

public:

virtual property Type^ AdditionalObjectsFilter {

   Type^ get();

}


Remarks

Set of types that can be passed to be verified, is created from type returned by this property and all type that inherit from it.

Depending on the value of the filter, framework can also pass additional object to be checked. They are objects of classes: Connections, DeviceListEntry, ArticleReference and PlanningSegment.

This property is used only when check is done for hole project.

This property is only a tip for framework. Set of objects passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method is a sum of types passed by all verifications executed in current check.

While check of whole project is done all pages and installation spaces are always passed to [IVerification.Execute](Eplan.EplApi.EServicesu~Eplan.EplApi.EServices.IVerification~Execute.html) method, regardless value of this property.
