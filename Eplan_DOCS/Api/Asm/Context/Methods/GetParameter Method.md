# GetParameter Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.Context~GetParameter.html

---

Gets a parameter from the Context.

Syntax

**C#**



public virtual void GetParameter( 

   string strParameterName,

   ref string strParameterValue

)

public:

virtual void GetParameter( 

   String^ strParameterName,

   String^% strParameterValue

)


#### Parameters

*strParameterName*
:   Name of the parameter whose value is determined. Leading and trailing white-space characters are ignored.

*strParameterValue*
:   Value of the parameter you search for.
