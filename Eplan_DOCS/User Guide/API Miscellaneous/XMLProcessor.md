# XMLProcessor

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/XMLProcessor.html

---

### The XMLProcessor interface

In general, Eplan uses  XML  as its interchange format. Furthermore Eplan is required to support various other export / import formats. It is not practical to consider all possible of these formats.

### Solution

Eplan carries on exporting / importing its  XML  format. Additionally, conversion modules can be added to Eplan that convert the created  XML  files into other import / export formats.

Import of different formats:

Export of different formats:

The following work flow is used:

Import:

- starting the import and selecting the import format  XYZ
- converting  XYZ  to  XML  through the conversion module
- importing the  XML  file

Export:

- starting the export and selecting the export format  XYZ
- exporting the  XML  file
- converting  XML  to  XYZ  through the conversion module

### Interface

API conversion modules can be created by implementing the  IXMLProcessor  interface. Although not all formats are read as well as written, it makes sense to handle both import and export in one interface.

The following example shows the usage of the interface, where only the export is implemented:

```csharp
public class MySimpleXMLConverter : Eplan.EplApi.ApplicationFramework.IXMLProcessor
 {
     public MySimpleXMLConverter()
     {
         //
         // TODO: Add constructor logic here
         //
     }
     string m_sError = string.Empty;
     Options m_optionsXMLProcessor = new Options();
     #region IXMLProcessor Members
     /// <summary>
     /// Returns a settings dialog for this processor.
     /// Dialog is only created, but not displayed!
     /// </summary>
     /// <returns>Interface of the created dialog.</returns>
     public Eplan.EplApi.ApplicationFramework.IOptions GetOption()
     {
         return m_optionsXMLProcessor;
     }
     /// <summary>
     /// Returns the name of the converter, as it will appear in the selection list.
     /// </summary>
     /// <returns>Name of converter, is shown in selection list.</returns>
     public string GetName()
     {
         String strName = "SimpleXMLProcessor";
         strName += " (";
         strName += GetFileFilter();
         strName += ")";
         return strName;
     }
     /// <summary>
     /// Returns an error message if an error occurred during export/import.
     /// </summary>
     ///<returns>Error message</returns>
     public string GetErrorMessage()
     {
         // TODO:  Add XMLProcessor.getErrorMessage implementation
         return m_sError;
     }
     /// <summary>
     /// Is called after import has been completed.
     /// </summary>
     /// <returns>If true, an Information dialog box is displayed.</returns>
     public bool PostImport()
     {
         // TODO:  Add XMLProcessor.postImport implementation
         return false;
     }
     /// <summary>
     /// Is called after export has been completed.
     /// </summary>
     /// <returns>If true, an Information dialog box is displayed.</returns>
     public bool PostExport()
     {
         // TODO:  Add XMLProcessor.postExport implementation
         return false;
     }
     /// <summary>
     /// Indicates whether the converter provides an export option.
     /// </summary>
     /// <param name="oContext">Context with parameters</param>
     /// <param name="bSupportsProgress">Indicates whether the converter supports a progress bar.</param>
     /// <returns>true: export is possible; false: export is not possible</returns>
     public bool CanExport(Eplan.EplApi.Base.Context oContext, ref bool bSupportsProgress)
     {
         bSupportsProgress = false;
         return true;
     }
     /// <summary>
     /// Converts the XML file to a special file.
     /// </summary>
     /// <param name="strXmlFile">Input file</param>
     /// <param name="strOutputFile">Output file</param>
     /// <param name="oContext">Context with parameters</param>
     /// <returns> Returns true if successful.</returns>
     public bool Export(string strXmlFile, string strOutputFile, Eplan.EplApi.Base.Context oContext)
     {
         bool bRet = false;
         try
         {
             // Short example for a simple export conversion
             System.Xml.XmlTextReader xRead = new System.Xml.XmlTextReader(strXmlFile);
             System.IO.StreamWriter swOut = new System.IO.StreamWriter(strOutputFile);
             xRead.WhitespaceHandling = System.Xml.WhitespaceHandling.None;
             string sFirstLang = string.Empty;
             while (xRead.Read())
             {
                 if ((xRead.XmlLang.CompareTo(String.Empty) != 0) && (xRead.Value.CompareTo(String.Empty) != 0))
                 {
                     if (sFirstLang.CompareTo(String.Empty) == 0) sFirstLang = xRead.XmlLang;
                     if (xRead.XmlLang.CompareTo(sFirstLang) == 0) swOut.WriteLine();
                     swOut.Write(xRead.XmlLang + ":" + xRead.Value + ";");
                 }
             }
             swOut.Close();
             xRead.Close();
             bRet = true;
         }
         catch (Exception e)
         {
             m_sError = string.Format("Exception: {0}", e.ToString());
         }
 
         return bRet;
     }
     /// <summary>
     /// Returns the filter string for the file selection box.
     /// </summary>
     /// <returns>Filter string</returns>
     public string GetFileFilter()
     {
         string strFilter = "*.*";
         return strFilter;
     }
     /// <summary>
     /// Indicates whether the converter can convert external formats to XML.
     /// </summary>
     /// <param name="oContext">Context with parameters</param>
     /// <param name="bSupportsProgress">Indicates whether the converter supports a progress bar.</param>
     /// <returns>true: conversion is possible; false: conversion is not possible</returns>
     public bool CanImport(Eplan.EplApi.Base.Context oContext, ref bool bSupportsProgress)
     {
         bSupportsProgress = false;
         return false;
     }
     /// <summary>
     /// Conversion from sImportFile to sXmlFile.
     /// sXmlFile might be passed as "". In this case, the converter must set a file name.
     /// EContext may point to an EProgress object to support a progress bar.
     /// Returns true if successful.
     /// </summary>
     /// <param name="strInputFile">Input file</param>
     /// <param name="strXmlFile">Output file</param>
     /// <param name="oContext">Context with parameters</param>
     public bool Import(string strInputFile, string strXmlFile, Eplan.EplApi.Base.Context oContext)
     {
         // TODO:  Add XMLProcessor.import implementation
         return false;
     }
 }
```

**Registering a conversion module**

Each conversion module must be registered with Eplan so that it is available during import or export. Since a conversion is only intended for a specific task, the scope of functions of the converter must be set during registration. This is done via the  IInterface  interface, as it is shown at the end of the above example.

The  InterfaceName  property returns the interface name followed by the interface category. The category specifies in which export dialog the new processor will be displayed. The available interface categories can be found in the list of available XML processors under  Eplan.EplApi.ApplicationFramework.XMLConverter  and  Eplan.EplApi.ApplicationFramework.XMLConverterCategories.
