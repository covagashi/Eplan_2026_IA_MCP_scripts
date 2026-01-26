# FunctionFilterSchemaData Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.ReportBlock~FunctionFilterSchemaData.html

---

Property data represents function filter scheme settings for report generation.

Syntax

**C#**



public string FunctionFilterSchemaData {get; set;}

public:

property String^ FunctionFilterSchemaData {

   String^ get();

   void set (    String^ value);

}


Remarks

String contains function filter criteria properties and its values for given report.  
  
To get value of such string in proper form first create template function filter settings scheme in report generation GUI. Then export whole template to .xml file and find value for 'SubFilterSchemeData' setting name.
