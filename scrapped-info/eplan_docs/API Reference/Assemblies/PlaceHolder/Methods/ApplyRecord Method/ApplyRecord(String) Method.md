# ApplyRecord(String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.Graphics.PlaceHolder~ApplyRecord(String).html

---

Applies a record of values on a PlaceHolder object.

Syntax

**C#**



public virtual void ApplyRecord( 

   string strRecordName

)

public:

virtual void ApplyRecord( 

   String^ strRecordName

)


#### Parameters

*strRecordName*
:   Name of the record to apply.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |

Remarks

Sets also the page data.
