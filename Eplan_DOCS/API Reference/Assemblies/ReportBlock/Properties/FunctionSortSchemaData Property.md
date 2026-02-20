# FunctionSortSchemaData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionSortSchemaData.html

---

Property data represents function sort scheme settings for report generation.

Syntax

**C#**



public string FunctionSortSchemaData {get; set;}

public:

property String^ FunctionSortSchemaData {

   String^ get();

   void set (    String^ value);

}


Remarks

String contains function sort criteria properties for given report.  
  
To get value of such string in proper form first create template function sort settings scheme in report generation GUI. Then export whole template to .xml file and find value for 'SubSortSchemeData' setting name.
