# ARTICLE_HOLE_PATTERN Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticlePropertyList~ARTICLE_HOLE_PATTERN().html

---

Hole pattern # 26437.

Syntax

**C#**



public PropertyValue ARTICLE_HOLE_PATTERN {get; set;}

public:

property PropertyValue^ ARTICLE_HOLE_PATTERN {

   PropertyValue^ get();

   void set (    PropertyValue^ value);

}


#### Property Value

Returns property value of type [Eplan.EplApi.Base.MultiLangString](Eplan.EplApi.Baseu~Eplan.EplApi.Base.MultiLangString.html).

Remarks

Specification of the arrangement of cut-outs. Hole patterns can be created in accordance with the standard or manufacturer-specifically, for example as a paper template. A hole pattern point is not a drilling pattern in Eplan. (information on the generation of drilling patterns can be found in the help system in the section "Drilling Patterns from Machine Data".)
