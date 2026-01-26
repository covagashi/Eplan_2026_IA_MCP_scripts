# BaseException Constructor(String,MessageLevel,BaseException)

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException~_ctor(String,MessageLevel,BaseException).html

---

Constructor

Syntax

**C#**



public BaseException( 

   string strErrorText,

   MessageLevel eErrorLevel,

   BaseException innerException

)

public:

BaseException( 

   String^ strErrorText,

   MessageLevel eErrorLevel,

   BaseException^ innerException

)


#### Parameters

*strErrorText*
:   Note on the exception that occurred.

*eErrorLevel*
:   Severity of the exception that occurred.

*innerException*
:   The exception that is the cause of the current exception, or a null reference (Nothing in Visual Basic) if no inner exception is specified.
