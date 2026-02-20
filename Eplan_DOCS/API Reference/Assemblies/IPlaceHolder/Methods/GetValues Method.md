# GetValues Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.IPlaceHolder~GetValues.html

---

\Returns the values of all variables in the nIndex-th PlaceHolder of a Macro variant for a given record.

Syntax

**C#**



StringCollection GetValues( 

   string strRecordName

)

StringCollection^ GetValues( 

   String^ strRecordName

)


#### Parameters

*strRecordName*
:   Record name.

#### Return Value

The values of the variables.

Exceptions

| Exception | Description |
| --- | --- |
| [System.ArgumentNullException](#) | Thrown in case of missing parameters. |
| [System.ArgumentException](#) | Thrown in case of invalid arguments. |
| [System.ApplicationException](#) | The internal interface for place holders could not be created. |
