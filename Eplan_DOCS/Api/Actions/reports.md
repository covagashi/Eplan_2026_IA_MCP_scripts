# reports

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/reports.html

---

```
Action class to update all project evaluations.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 '¢ "PROJECT": Generate project reports.
 '¢ "PAGES": Update all reports of the same type as given pages. Only the particular report, to which the page belongs, will be updated
 '¢ "UPDATEMODELVIEWPAGES": Update model views on given pages.
 '¢ "CREATEMODELVIEWS": Create model views
 '¢ "CREATECOPPERUNFOLDS": Create copper unfolds
 '¢ "CREATEDRILLINGVIEWS": Create drilling views
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used, in case the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to be updated (optional).
 If specified, only the particular report, to which the page belongs, will be updated.
 This parameter is only effective with the "PAGES" and "UPDATEMODELVIEWPAGES" values of the TYPE parameter.
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). 
 It corresponds to "Active" check box in GUI. 
 These parameters are only effective with the "PAGES" and "UPDATEMODELVIEWPAGES" values of the TYPE parameter.
 Default value: 0 
 ``` |
| ``` PAGEFILTERNAME
 ``` | ``` Pages are read from pagefilter with the name pagefiltername.
 These parameters are only effective with the "PAGES" and "UPDATEMODELVIEWPAGES" values of the TYPE parameter.
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be  included in reports update (optional), where n is a number e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc. 
 These parameters are only effective with the "PAGES" and "UPDATEMODELVIEWPAGES" values of the TYPE parameter.
 ``` |
| ``` SELn
 ``` | ``` Identifier of the pages to be included in report update (optional), where n is a number (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())) parameters are only effective with the "PAGES" and "UPDATEMODELVIEWPAGES" values of the TYPE parameter.
 ``` |
| ``` TEMPLATEn
 ``` | ``` Templates used for generating report pages, where n is a number e.g. /TEMPLATE1:"Template1" /TEMPLATE2:"Template2" etc. These parameters are only effective with "CREATEMODELVIEWS", "CREATECOPPERUNFOLDS" and "CREATEDRILLINGVIEWS" value of the TYPE parameter.
 ``` |
| ``` REPLACEEXISTING
 ``` | ``` Replaces existing model views, copper unfolds or drilling views when set to 1.
 This parameter is only effective with "CREATEMODELVIEWS", "CREATECOPPERUNFOLDS" and "CREATEDRILLINGVIEWS" value of the TYPE parameter.
 ``` |

**Remarks**

```
When an error occurs during a reports operation, a "BaseException" is thrown.

```

**Example**

```
reports /TYPE:PROJECT /PROJECTNAME:C\\Projects\EPLAN\EPLAN_Sample_Project.elk

```