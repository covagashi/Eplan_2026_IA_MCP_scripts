# Trace(Assembly,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.Baseu~Eplan.EplApi.Base.EplTrace~Trace(Assembly,String).html

---

Writes the text to EplLog.txt when Trace is on.

Syntax

**C#**



public virtual void Trace( 

   Assembly assembly,

   string strMessage

)

public:

virtual void Trace( 

   Assembly^ assembly,

   String^ strMessage

)


#### Parameters

*assembly*
:   The assembly calling this function. This when Trrace is on for this assembly, the output is written.

*strMessage*
:   The message to be traced to epllog.txt
