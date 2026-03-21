# _kResponse

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.AFu~Eplan.EplApi.BaseRemoting._kResponse.html

---

Syntax

**C#**



public enum _kResponse : System.Enum

public enum class _kResponse : public System.Enum


Members

| Member | Value | Description |
| --- | --- | --- |
| **clientNotConnectedToServer** | 6 | Client not connected to server |
| **reqExceptionRaisedInClient** | 9 | Exception raised on Eplan client side |
| **reqExceptionRaisedInServer** | 8 | Exception raised on Eplan server side |
| **reqExecuted** | 2 | client request executed |
| **reqNotExecuted** | 3 | client request not executed |
| **reqRejected** | 1 | client request rejected |
| **reqTransmitted** | 4 | client request transmitted to Eplan remoting server |
| **reqUndefined** | 0 | undefined client request |
| **serverBusy** | 5 | Eplan remoting server is busy |
| **timeOutIntervalElapsed** | 7 | Time out on server side. This is the maxi time set to execute a request. |

Inheritance Hierarchy

[System.Object](#)  
   [System.ValueType](#)  
      [System.Enum](#)  
         **Eplan.EplApi.BaseRemoting.\_kResponse**
