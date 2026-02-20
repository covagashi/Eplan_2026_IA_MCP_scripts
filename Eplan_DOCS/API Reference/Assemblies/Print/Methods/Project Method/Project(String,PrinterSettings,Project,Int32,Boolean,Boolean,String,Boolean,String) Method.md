# Project(String,PrinterSettings,Project,Int32,Boolean,Boolean,String,Boolean,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1420.html

---

Prints all pages of the given project on the specified printer.

Syntax

**C#**



public void Project( 

   string strPrinterName,

   PrinterSettings pSettings,

   Project pProject,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   string strTargetFile,

   bool bPrintChangedPages,

   string strLanguage

)

public:

void Project( 

   String^ strPrinterName,

   PrinterSettings^ pSettings,

   Project^ pProject,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   String^ strTargetFile,

   bool bPrintChangedPages,

   String^ strLanguage

)


#### Parameters

*strPrinterName*
:   Printer name.

*pSettings*
:   [System.Drawing.Printing.PrinterSettings](#) object to specify further printer settings.

*pProject*
:   Project to be printed.

*dNumber*
:   Number of copies to print.

*bPrintCollate*
:   Collate output.

*bPrintReverse*
:   Reverse printing.

*strTargetFile*
:   Full file name of the \output file in case of printing to file.

*bPrintChangedPages*
:   Print changed pages

*strLanguage*
:   Language of printed project

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

If `bPrintChangedPages` is used with non-empty strTargetFile and nothing was changed empty file will be created anyway. Warning! Please check settings under "Workstation->Graphical editing->Print" because they overwrite parameters of the method.
