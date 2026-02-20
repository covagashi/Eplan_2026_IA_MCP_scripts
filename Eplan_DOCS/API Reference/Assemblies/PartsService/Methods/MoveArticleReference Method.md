# MoveArticleReference Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PartsService~MoveArticleReference.html

---

Moves ArticleReference to another index or to another object or both.

Syntax

**C#**



public ArticleReference MoveArticleReference( 

   ArticleReference oSourceAR,

   IArticleUser oTarget,

   int nTargetIndex

)

public:

ArticleReference^ MoveArticleReference( 

   ArticleReference^ oSourceAR,

   IArticleUser^ oTarget,

   int nTargetIndex

)


#### Parameters

*oSourceAR*
:   Article reference which defines source object and index

*oTarget*
:   Target object where ArticleReference will be moved to.

*nTargetIndex*
:   Target index where ArticleReference will be moved to.

#### Return Value

Newly created ArticleReference.

Remarks

If the user still holds ArticleReference objects which are affected by the change, or their internal object identifiers, they will get invalid after calling the method.
