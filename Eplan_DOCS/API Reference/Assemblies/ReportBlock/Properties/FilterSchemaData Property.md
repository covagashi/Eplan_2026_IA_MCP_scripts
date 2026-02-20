# FilterSchemaData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FilterSchemaData.html

---

Property data represents filter scheme settings for report generation.

Syntax

**C#**



public string FilterSchemaData {get; set;}

public:

property String^ FilterSchemaData {

   String^ get();

   void set (    String^ value);

}


Remarks

String contains filter criteria properties and its values for given report.  
  
To get value of such string in proper form first create template filter settings scheme in report generation GUI. Then export whole template to .xml file and find value for 'FilterSchemeData' setting name.
