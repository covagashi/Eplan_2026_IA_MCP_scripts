# API Parts Selection Interface

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/API_PARTS_SELECTION.html

---

In Eplan, you have the possibility to switch between different data sources for the part selection. You can get parts data via:

- **Eplan database**
- **SQL Server**
- **API**

 Setting the data source to "API" means that an API action will be called in case of operations related to accessing parts, for example:

- A new part (or reference) is added to a project.

- The part reference is changed in a project.

- The part information is loaded from system.

- A part is synchronized to a project.

- A new macro with parts is inserted to a project.

- A new device is inserted to project.

- A new device is selected (with device section).

- A new device list item is inserted to project.

In this way, the user can create his own dialog for setting parts data, set additional properties when selecting a part, etc.

An example of its use is the "Eplan Data Portal" scheme ' after setting it, the standard dialog for selecting parts is replaced by a custom one, which allows advanced selection of parts from the Data Portal database.

Please note that the API parts selection cannot completely substitute the parts management databases such as Eplan database or SQL Server. In some operations, they still have to be used.

This topic describes how to use the API parts selection interface.

### a) Setting the API parts selection action

To be able to use the API parts selection interface, you first have to enable and configure it. To do this, you open the Settings dialog in Eplan and select User > Management > Parts. In this dialog you create a new scheme and activate the API radio button.

By clicking the ellipsis [...] button next to the API radio button, you can open a dialog with further settings for the API interface.

In this dialog you enter the name of an API action that is called by Eplan when the parts selection is started.

The following describes how to develop the action and set its parameters.

### b) Creating an action

Please create an action with the name that was set in Settings dialog. The best way is to use the Visual Studio wizard:

### c) Handling action parameters

The part data is passed through the  ActionCallingContext  of the action. The object contains a set of input and output parameters that are passed as strings.

**C#**
```csharp
public bool Execute(ActionCallingContext oActionCallingContext)

    Public Function Execute(oActionCallingContext As Eplan.EplApi.ApplicationFramework.ActionCallingContext) As Boolean _

        Implements Eplan.EplApi.ApplicationFramework.IEplAction.Execute
```

In this way, it is possible to have an access to properties of a selected part, for example:

```csharp
string sMode = "";
 ctx.GetParameter("Modus", ref sMode);
 string sProp00 = "(int)Properties.Article.ARTICLE_DEPTH" + sSeparator + "1";
 ctx.AddParameter(sProp00, "44.0");

```

The  Modus  parameter is used to identify the mode in which the parts selection is called. It can take one of the following values:

- Selection  ' A part is selected.
- Read  ' A part is updated.
- Create  ' A part is created and parts selection action is called as alternative parts data source.
- Exist  ' Check if part exist.

Here is also a table with other input parameters:

|  |  |
| --- | --- |
| **Mode** (Modus  parameter) | **Input parameters** |
| Selection | objectid  ' The object ID of the function on which the part selection was started. You can use the object ID to locate the function in the project and get additional information about it.  separator  ' Contains the separator between property number and part index in parameter name  SingleSelection  ' Is set to "1" if only one part can be set. Otherwise it is "0" or an empty string.  ForceNoResolve  ' Is set to "1" if the assembly should not be resolved. Otherwise it is "0" or an empty string.  GraphicalPreview  ' Is set to "1" if the user wants a preview of the part. Otherwise, it is "0" or an empty string.  preselectpartnr  ' Contains the part number in the table cell from which the part selection is started. If the cell is empty, the parameter contains an empty string.  preselectvariant  ' Contains the part variant number in the table cell from which the part selection is started.  PartSelection  ' Is set to "1" if only a selection dialog should be shown. If it is "0", the parts can also be edited.  DatabaseId  '  StorableObject.DatabaseIdentifier  of the current project.  UsePreSelection  ' Is set to "1" if the preselection list should be considered. Otherwise it is "0" or an empty string.  codeletter  '  Identifier  property of selected symbol  symbollib  ' Symbol library of selected symbol  symbolnr  ' Symbol number of selected symbol  craft  ' Trade number of selected part  \_cmdline  ' Name of calling action |
| Read | Separator  ' Contains separator between property number and part index in parameter name, for example:                          <property number><separator><part index>[<separator><property index>]  ' e.g. "22001\_1", value "SIE.5SX2102-8"  22024\_<part index>  ' part variant  \_cmdline  ' Name of calling action |
| Create | Separator  ' Contains separator between property number and part index in parameter name, for example:                          <property number><separator><part index>[<separator><property index>]  ' e.g. "22001\_1", value "SIE.5SX2102-8"  \_cmdline  ' Name of calling action |
| Exist | Separator  ' Contains separator between property number and part index in parameter name, for example                          <property number><separator><part index>[<separator><property index>]  ' e.g. "22001\_1", value "SIE.5SX2102-8"  22024\_<part index>  ' part variant  \_cmdline  ' Name of calling action |

The **output parameters** are the following:

- The property to set.  
  The parameter name has the format:  <property number><separator><part index>[<separator><property index>].  
  It is required to set the part number property (22001). Other properties are optional.  
  The  <part index>  is used to pass more than one part simultaneously.  
  It starts from the 1. example : "1234\_1". As a value, it can be any string for example '11.0', etc.

- Count of the parts to transmit.  
  The parameter name is  count. The value is determined by the last  <part index>.

- In case of the  Exists  mode, there is also a  Result  parameter that determines whether a part exists.

A very important input parameter is the object ID (objectid). Using the object ID, you can locate the function in the project and get additional information about it.

The following example shows an API parts selection action that displays the FormPartSelection user dialog and passes the fields  Partnumber,  Typenumber  and  Description1.

```csharp
public class MyPartSelectionAction : IEplAction
 {
     public bool Execute(ActionCallingContext oActionCallingContext)
     {
         // Object ID from which part selection is started
         string sObjectId = "";
         oActionCallingContext.GetParameter("ObjectId", ref sObjectId);
         // Get Function object
         Function oFunction = getFunction(sObjectId);
         FormPartSelection frm = new FormPartSelection();
         frm.Description = "";
         frm.Typenumber = "";
         frm.Partnumber = "new part";
         // Start part selection dialog
         if (frm.ShowDialog() == DialogResult.OK)
         {
             string sTypenumber = frm.Typenumber;
             string sPartnumber = frm.Partnumber;
             string sDescription = frm.Description;
             // Count of parts
             oActionCallingContext.addParameter("count", "1");
             // Get separator between property and index
             string sSeparator = "";
             oActionCallingContext.GetParameter("Separator", ref sSeparator);
             int prop;
             int idx = 1;
             string sProp;
             // Set part number
             prop = (int)Properties.Article.ARTICLE_PARTNR;
             sProp = prop.ToString() + sSeparator + idx.ToString();
             oActionCallingContext.AddParameter(sProp, sPartnumber);
             // Set type number
             prop = (int)Properties.Article.ARTICLE_TYPENR;
             sProp = prop.ToString() + sSeparator + idx.ToString();
             oActionCallingContext.AddParameter(sProp, sTypenumber);
             // Set description 1
             prop = (int)Properties.Article.ARTICLE_DESCR1;
             sProp = prop.ToString() + sSeparator + idx.ToString();
             oActionCallingContext.AddParameter(sProp, sDescription);
             if ((oFunction != null))
             {
                string strArticleCharacteristics = (int)Properties.Article.ARTICLE_CHARACTERISTICS + sSeparator + "1";
                ctx.AddParameter(strArticleCharacteristics, "5,5kW");      // Set characteristics to 5,5 kW
             }
         }
         return true;
     }
     // Locate the function by its object ID
         private Function getFunction(string sObjectId)
         {
             ProjectManager projectManager = new ProjectManager();
             Project project = projectManager.CurrentProject;
             DMObjectsFinder objectFinder = new DMObjectsFinder(project);
             FunctionPropertyList functionPropertyList = new FunctionPropertyList();
             functionPropertyList[Properties.StorableObject.PROPUSER_DBOBJECTID] = sObjectId;
             FunctionsFilter functionsFilter = new FunctionsFilter();
             functionsFilter.SetFilteredPropertyList(functionPropertyList);
             Function[] aFunction = objectFinder.GetFunctions(functionsFilter);
             if (aFunction.Length > 0)
             {
                 return aFunction[0];
             }
             return null;
         }
 
     public bool OnRegister(ref string Name, ref int Ordinal)
     {
         Name = "MyPartSelectionAction";
         Ordinal = 20;
         return true;
     }
     public MyPartSelectionAction()
     {}
 }

```