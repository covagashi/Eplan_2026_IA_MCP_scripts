# GetAvailableFormats Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.PlcService~GetAvailableFormats.html

---

Returns a string array of available formats that may be used for exporting PLC data.

Syntax

**C#**



public string[] GetAvailableFormats( 

   string strConverterId

)

public:

array<String^>^ GetAvailableFormats( 

   String^ strConverterId

)


#### Parameters

*strConverterId*
:   ID of the PLC data converter to use. The IDs of the registered PLC converters together with their full names may be obtained by calling the GetAvailableConverters method.
