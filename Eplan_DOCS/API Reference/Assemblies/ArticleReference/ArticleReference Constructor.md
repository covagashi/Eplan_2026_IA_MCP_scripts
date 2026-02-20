# ArticleReference Constructor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ArticleReference~_ctor(String,String,UInt32).html

---

Constructor used to create transient article reference object. That object can be passed as a parameter to ConnectionDefinitionPoint() function.

Syntax

**C#**



public ArticleReference( 

   string strPartNr,

   string strVariant,

   uint nCount

)

public:

ArticleReference( 

   String^ strPartNr,

   String^ strVariant,

   uint nCount

)


#### Parameters

*strPartNr*


*strVariant*


*nCount*

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown when `strPartNr` is `null`. |
| [System.ArgumentNullException](#) | Thrown when `strVariant` is `null`. |
| [System.ArgumentException](#) | Thrown when `nCount` is less than `0`. |
