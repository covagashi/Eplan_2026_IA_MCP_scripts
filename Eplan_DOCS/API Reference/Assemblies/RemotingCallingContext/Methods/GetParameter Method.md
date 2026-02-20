# GetParameter Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.RemoteServer.RemotingCallingContext~GetParameter.html

---

Syntax

**C#**



public void GetParameter( 

   string strParameterName,

   ref string strParameterValue

)

public:

void GetParameter( 

   String^ strParameterName,

   String^% strParameterValue

)


#### Parameters

*strParameterName*
:   Paramter name (input parameter)

*strParameterValue*
:   Parameter value (output parameter)

Remarks

If the parameter exists, strParameterValue contains its value after executing this method. If the parameter is not found, strParameterValue is set to nullptr.
