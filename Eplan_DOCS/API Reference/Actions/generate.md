# generate

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/generate.html

---

```
Action class for generate functions: generate connections and generate cables.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action:
 CONNECTIONS: Connection generation
 CABLES: Cable generation 
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is  called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` CREATIONSCHEME
 ``` | ``` Name of the scheme; for cable generation (optional).
 Default value = Most recently used scheme.
 This only applies to cable generation.
 ``` |
| ``` NUMBERINGSCHEME
 ``` | ``` Name of the scheme; for cable numbering (optional).
 Default value = Recent scheme.
 This only applies to cable generation.
 ``` |
| ``` AUTOSELECTSCHEME
 ``` | ``` Name of the scheme; for automatic cable selection (optional).
 Default value = Recent scheme.
 This only applies to cable generation.
 ``` |
| ``` KEEPOLDNAMES
 ``` | ``` Specifies whether existing cable names are to be preserved (optional, 0 = No, 1 = Yes).
 Default value = 1
 This only applies to cable generation.
 ``` |
| ``` STARTVALUE
 ``` | ``` Start value for DT counter (optional).
 Default value = 1
 Only applies to cable generation.
 ``` |
| ``` STEPVALUE
 ``` | ``` Increment; value by which the DT counter is increased (optional).
 Default value = 1
 Only applies to cable generation.
 ``` |
| ``` ONLYAUTOCABLES
 ``` | ``` Specifies whether the cable selection should be made only for automatically generated cables (optional, 0 = No, 1 = Yes).
 Default value = 1
 Only applies to cable generation.
 ``` |
| ``` REBUILDALLCONNECTIONS
 ``` | ``` If set to 1, the action     rebuilds all connections, otherwise it updates only.
 ``` |
| ``` PAGENAME
 ``` | ``` Name of the page to be updated (optional).
 This parameter is only effective with the CONNECTIONS value of the TYPE parameter.
 ``` |
| ``` USEPAGEFILTER
 ``` | ``` Determines if only filtered pages should be used or all project pages (optional). It corresponds to "Active" check box in GUI. 
 These parameters are only effective with the CONNECTIONS value of the TYPE parameter.
 Default value = 0 
 ``` |
| ``` PAGEFILTERNAME
 ``` | ``` Pages are read from pagefilter with the name pagefiltername.These parameters are only effective  with the CONNECTIONS value of the TYPE parameter.
 ``` |
| ``` PAGENAMEn
 ``` | ``` Names of the pages to be included in connections update (optional), where n is a number e.g. /PAGENAME1:=AP+ST1/2 /PAGENAME2:=AP+ST1/4 /PAGENAME3:=AP+ST1/7 etc. 
 These parameters are only effective with the CONNECTIONS value of the TYPE parameter.
 ``` |
| ``` SELn
 ``` | ``` Identifier of the pages to be included in connections update  (optional), where n is a number (e.g. /SEL1:38/4/12/0 (result from StorableObject.ToStringIdentifier())) parameters are only effective with the CONNECTIONS value of the TYPE parameter.
 ``` |

**Remarks**

```
When an error occurs during a generate operation, a "BaseException" is thrown.

```

**Example**

```
Connection generation

generate /TYPE:CONNECTIONS /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk

Cable generation

generate /TYPE:CABLES /KEEPOLDNAMES:0 /STARTVALUE:5 /STEPVALUE:2 /ONLYAUTOCABLES:0

```