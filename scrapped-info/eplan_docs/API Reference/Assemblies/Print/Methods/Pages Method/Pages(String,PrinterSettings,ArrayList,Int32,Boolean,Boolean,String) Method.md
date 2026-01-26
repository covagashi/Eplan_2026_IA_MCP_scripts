# Pages(String,PrinterSettings,ArrayList,Int32,Boolean,Boolean,String) Method

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/topic1414.html

---

Prints pages on the specified printer.

Syntax

**C#**



public void Pages( 

   string strPrinterName,

   PrinterSettings pSettings,

   ArrayList arrayPages,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   string strTargetFile

)

public:

void Pages( 

   String^ strPrinterName,

   PrinterSettings^ pSettings,

   ArrayList^ arrayPages,

   int dNumber,

   bool bPrintCollate,

   bool bPrintReverse,

   String^ strTargetFile

)


#### Parameters

*strPrinterName*
:   Printer name.

*pSettings*
:   [System.Drawing.Printing.PrinterSettings](#) object to specify further printer settings.

*arrayPages*
:   ArrayList of page names to be printed.

*dNumber*
:   Number of copies to print.

*bPrintCollate*
:   Collate output.

*bPrintReverse*
:   Reverse printing.

*strTargetFile*
:   Full file name of the output \file in case of printing to \file.

Exceptions

| Exception | Description |
| --- | --- |
| **ArgumentException** | Thrown in case of invalid \parameters. |
| **ArgumentNullException** | Thrown if a parameter is set to null. |
| **ApplicationException** | The \internal interface necessary for printing could not be created. |
| **Eplan\:\:EplApi\:\:Base\:\:BaseException** | An error occurred during the print process. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:PrinterMissing** | The given printer could not be found. |
| **Eplan\:\:EplApi\:\:DataModel\:\:OperationCanceledException** | The print process was canceled by the user. |
| **Eplan\:\:EplApi\:\:HEServices\:\:Exceptions\:\:UnknownPrinter** | Some undefined error occurred, e.g. HDC could not be created. |

Remarks

The specified pages can belong to one project or a number of projects. The projects have to be opened, otherwise nothing is printed. Warning! Please check settings under "Workstation->Graphical editing->Print" because they overwrite parameters of the method.
