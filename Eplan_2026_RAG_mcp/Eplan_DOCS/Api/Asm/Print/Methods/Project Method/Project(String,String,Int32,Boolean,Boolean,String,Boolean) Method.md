# Project(String,String,Int32,Boolean,Boolean,String,Boolean) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.HEServicesu~Eplan.EplApi.HEServices.Print~Project(String,String,Int32,Boolean,Boolean,String,Boolean).html

---

Prints all pages of the given project on the specified printer.

Syntax

**C#**



public void Project( 

   string strPrinterName,

   string strFullLinkFileName,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   string strTargetFile,

   bool bPrintChangedPages

)

public:

void Project( 

   String^ strPrinterName,

   String^ strFullLinkFileName,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   String^ strTargetFile,

   bool bPrintChangedPages

)


#### Parameters

*strPrinterName*
:   Printer name.

*strFullLinkFileName*
:   Full link file name of the project to be printed.

*dNumber*
:   Number of copies to print.

*bPrintCollate*
:   Collate output.

*bPrintReverse*
:   Reverse printing.

*strTargetFile*
:   Full file name of the \output file in case of printing to file.

*bPrintChangedPages*
:   Print changed pages.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \parameters, e.g. the project does not exist. |
| **ArgumentNullException** | Thrown if a parameter is set to null. |
| **ApplicationException** | The \internal interface necessary for printing could not be created. |
| **Eplan\:\:EplApi\:\:Base\:\:BaseException** | An error occurred during the print process. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:PrinterMissing** | The given printer could not be found. |
| **Eplan\:\:EplApi\:\:DataModel\:\:OperationCanceledException** | The print process was canceled by the user. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:UnknownPrinter** | Some undefined error occurred, e.g. HDC could not be created. |

Remarks

The specified project may be open in EPLAN or not. If the project is not opened from the beginning, it will be opened for the printing process and will be closed subsequently. If `bPrintChangedPages` is used with non-empty strTargetFile and nothing was changed empty file will be created anyway. Warning! Please check settings under "Workstation->Graphical editing->Print" because they overwrite parameters of the method.
