# check

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/check.html

---

```
Action class for checking functions: check a project and check pages.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action.
 Possible values are:
 '¢ "PROJECT": Check project
 '¢ "PAGES": Check pages
 '¢ "INSTALLATIONSPACE": Check installation space
 '¢ "ONLYCOMPLETED": Check project, only completed messages
 '¢ "PARTS": Check parts
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` VERIFICATIONSCHEME
 ``` | ``` Name of scheme used for the project check (optional, scheme name only, without path).
 When the parameter Type = "PARTS", then PROJECTNAME parameter is not required
 Default value: Most recently used scheme.
 ``` |
| ``` VERIFYCOMPLETEDONLY
 ``` | ``` Verifies completed messages only, when set to 1. Default is 0.
 This parameter is only effective with the PROJECT and PARTS value of TYPE parameter, and without the PARTNUMBERn parameter.
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). 
 It corresponds to "Active" check box in GUI
 Default value: 0 
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to be checked (optional).
 ``` |
| ``` SELn
 ``` | ``` Identifier of the pages to be Checked (optional), where n is a number (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())) parameters are only effective with the PAGE value of the TYPE parameter.
 ``` |
| ``` PARTNUMBERn
 ``` | ``` Part number to be checked (optional), where n is a counter (e.g. /PARTNUMBER1:MyPartNumberA /PARTNUMBER2:MyPartNumberB
 ``` |
| ``` PARTVARIANTn
 ``` | ``` Part variant to be checked (optional), where n is a counter.
 Parameter is only effective with corresponding PARTNUMBER parameter (e.g. /PARTNUMBER1:MyPartNumberA /PARTVARIANT1:V2
 ``` |
| ``` INSTALLATIONSPACENAME
 ``` | ``` Name of the installation space to be checked. Value stored under property INSTALLATIONSPACE_DESIGNATION.
 ``` |
| ``` INSTALLATIONSPACENAMEn
 ``` | ``` Name of the installation space to be checked, where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /STRUCTURE1:=EB3+ET1 /INSTALLATIONSPACENAME2:BR2 /STRUCTURE2:=EB3+ET2 etc.
 Value stored under property INSTALLATIONSPACE_DESIGNATION.
 ``` |
| ``` STRUCTURE
 ``` | ``` Structure identifier of installation space to be checked. This parameter is only effective with the INSTALLATIONSPACE value of the TYPE parameter.
 ``` |
| ``` STRUCTUREn
 ``` | ``` Structure identifier of installation space to be checked, where n is a number e.g. /INSTALLATIONSPACENAME1:BR1 /STRUCTURE1:=EB3+ET1 /INSTALLATIONSPACENAME2:BR2 /STRUCTURE2:=EB3+ET2 etc.
 This parameter is only effective with the INSTALLATIONSPACE value of the TYPE parameter.
 ``` |

**Remarks**

```
If a page was explicitly entered by the PAGENAME parameter, then only this page is checked and the USEPAGEFILTER parameter is ignored. 

If no specific page was explicitly entered by the PAGENAME parameter, project pages are determined. 

If USEPAGEFILTER is set to 1, only pages filtered in GUI page navigator will be checked. 

If USEPAGEFILTER is not used or if it is set to 0, all project pages will be checked. USEPAGEFILTER corresponds to "Active" check box in the page navigator.

If an error occurs during a check operation, a "BaseException" is thrown.

```

**Example**

```
Check project with scheme: Offline

check /TYPE:PROJECT /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /VERIFICATIONSCHEME:Offline

Check most recently used project with most recently used scheme

check /TYPE:PROJECT

Check pages

check /TYPE:PAGES /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /PAGENAME:=AP+ST1/6

Check pages of the recently used project 

check /TYPE:PAGES /USEPAGEFILTER:1

Check an installation space

check /TYPE:INSTALLATIONSPACE /INSTALLATIONSPACENAME:BR1

```