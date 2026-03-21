# ARTICLE_SAFETYRELATED_SILCL Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~ARTICLE_SAFETYRELATED_SILCL().html

---

Safety-related values: SIL CL # 40330.

Syntax

**C#**



public PropertyValue ARTICLE_SAFETYRELATED_SILCL {get; set;}

public:

property PropertyValue^ ARTICLE_SAFETYRELATED_SILCL {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

SIL limit (short for "Safety Integrity Level Claim Limit"). The safety integrity level SIL (short for "Safety Integrity Level") specifies the requirements of the safety functions of a control system. Level 1 denotes the lowest requirements; Level 4 the highest. The SIL limit is the maximum SIL required for a subsystem.
