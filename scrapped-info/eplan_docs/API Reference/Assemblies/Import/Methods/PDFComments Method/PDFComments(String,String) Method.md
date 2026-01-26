# PDFComments(String,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Import~PDFComments(String,String).html

---

Imports comments from PDF file.

Syntax

**C#**



public int PDFComments( 

   string strFullLinkFileName,

   string strFileName

)

public:

int PDFComments( 

   String^ strFullLinkFileName,

   String^ strFileName

)


#### Parameters

*strFullLinkFileName*
:   Full link file name of the project. Can't be `null`.

*strFileName*
:   Full file name of the PDF file to be imported. Can't be `null`.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid arguments. |
| **ArgumentNullException** | Null was passed to a parameter. |
| **ApplicationException** | API can't get access to this functionality of P8. A reason for this could be the lack of necessary rights or licenses. |
| [Eplan.EplApi.Base.BaseException](Eplan.EplApi.Baseu~Eplan.EplApi.Base.BaseException.html) | An error occurred during the import. Please read the exception message. |
