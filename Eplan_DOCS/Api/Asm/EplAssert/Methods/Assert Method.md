# Assert Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplAssert~Assert.html

---

A Delevoper Assertion. When the boolean Expression fails, the debugged application fails into the debugger. Some Text is written to the EplLog.txt

Syntax

**C#**



public void Assert( 

   bool bExpression,

   string strInformation

)

public:

void Assert( 

   bool bExpression,

   String^ strInformation

)


#### Parameters

*bExpression*


*strInformation*
:   The message to be traced to epllog.txt
