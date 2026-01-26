# INSTANCE_FULLPLACEMENTLOCATION Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.MergedArticleReferencePropertyList~INSTANCE_FULLPLACEMENTLOCATION().html

---

Placement # 19007.

Syntax

**C#**



public PropertyValue INSTANCE_FULLPLACEMENTLOCATION {get; set;}

public:

property PropertyValue^ INSTANCE_FULLPLACEMENTLOCATION {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type System.String.

Remarks

This property is read-only..

Provides the full placement consisting of page, internal column and internal row (these do not reflect the column and row numbers). For functions and interruption points, the own cross-reference is output.
