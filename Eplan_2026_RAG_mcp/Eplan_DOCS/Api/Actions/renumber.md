# renumber

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/renumber.html

---

```
Action corresponds to numbering functionality.

```

| Parameter | Description |
| --- | --- |
| ``` TYPE
 ``` | ``` Type of task to be performed by the action.
 '¢ "DEVICES": Renumber devices
 '¢ "PAGES": Renumber pages
 '¢ "TERMINALS": Renumbering terminals
 '¢ "CABLES": Renumbering cables
 '¢ "CONNECTIONS": Renumbering connections
 ``` |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "PAGES", "TERMINALS", "CABLES", "CONNECTIONS".
 ``` |
| ``` USESELECTION
 ``` | ``` If this flag is set, only the objects currently selected in GUI will be renumbered instead of all objects in the project (optional).
 Possible values: 0 = No (default value), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "PAGES", "TERMINALS", "CABLES", "CONNECTIONS".
 ``` |
| ``` FILTERSCHEME
 ``` | ``` Name of the filter scheme (optional).
 Default value: most recently used filter scheme. If this parameter is not available, then no filtering takes place.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES".
 ``` |
| ``` CONFIGSCHEME
 ``` | ``` Name of the configuration scheme (optional).
 If not specified, the last used scheme will be selected again.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "TERMINALS", "CABLES", "CONNECTIONS".
 ``` |
| ``` STARTVALUE
 ``` | ``` Start value (integer, optional, default value: 1). 
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "PAGES", "TERMINALS", "CABLES".
 ``` |
| ``` STEPVALUE
 ``` | ``` Increment value. (integer, optional, default value: 1). 
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "PAGES", "TERMINALS", "CABLES".
 ``` |
| ``` POSTNUMERATE
 ``` | ``` If this flag is set, only invalid device tags (i.e. those containing "?" character) will be renumbered (optional).
 Possible values: 0 = No, 1 = Yes (default value).
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "TERMINALS".
 ``` |
| ``` ALSONUMERATEDBYPLC
 ``` | ``` If this flag is set, device tags which are influenced by PLC numbering will be numerated (optional).
 Possible values: 0 = No (default value), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES", "TERMINALS".
 ``` |
| ``` PERMITSORTCHANGE
 ``` | ``` Permit sort change (optional).
 Possible values: 0 = No (default value), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` FILLGAPS
 ``` | ``` Fill Gaps (optional).
 Possible values: 0 = No (default value), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` IDENTIFIER
 ``` | ``` Identifier, e.g. "X*" (optional). 
 If used, all devices from the project matching the identifier are taken for renumeration regardless of whether the USESELECTION parameter is used or not.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES".
 ``` |
| ``` NUMERATECABLES
 ``` | ``` If this flag is set, cables whose device tags contain source and target information are also numerated (optional).
 Possible values: 0 = No (default value), 1 = Yes.
 This parameter is only effective with the following values of the TYPE parameter: "DEVICES".
 ``` |
| ``` STRUCTUREORIENTED
 ``` | ``` Set this parameter to true to provide numbering per structure identifier.
 If false, then pages are continuously numbered without accounting for the structure identifiers.
 This parameter is only effective with the following values of the TYPE parameter: "PAGES".
 ``` |
| ``` KEEPINTERVAL
 ``` | ``` In combination with the definition of the start page, this parameter retains the increments between the selected pages for the target pages.
 In this way you can move any desired number of selected pages by a specified increment.
 Entering the increment size is not possible in this case. 
 This parameter is only effective with the following values of the TYPE parameter: "PAGES".
 ``` |
| ``` KEEPTEXT
 ``` | ``` Set this to 1, if the alphabetic part of the page name should not be overwritten.
 This parameter is only effective with the following values of the TYPE parameter: "PAGES".
 ``` |
| ``` SUBPAGES
 ``` | ``` Values are:
 '¢ 0 = Retain: Existing subpages are adopted unchanged into the target page.
 '¢ 1 = ConsecutiveNumbering: Existing subpages are renumbered using the starting value "1" and an increment of "1".
         At every change of the main page, the subpage numbering begins again from "1".
         The subpage numbering follows the project settings defined in the project setting "Characters for subpages".
 '¢ 2 = ConvertIntoMainPages: Subpages are converted to main pages and renumbered.
 This parameter is only effective with the following values of the TYPE parameter: "PAGES".
 ``` |
| ``` PREFIX
 ``` | ``` Prefix.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` SUFFIX
 ``` | ``` Suffix.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` SEQUENCE
 ``` | ``` Mode to use for numbering. Values are:
 0 = Like sorting: The terminal / pin sorting sequence displayed under terminal strips - (project name) or plugs - (project name) is used. 
 Select this option if you would like to number existing terminals / pins but retain the existing sorting.
 '¢ 1 = Page oriented
 '¢ 2 = Cable oriented
 '¢ 3 = Level oriented
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` EXTENT
 ``` | ``` Parameter to define the scope of numbering. Values are:
 '¢ 0 = Selected - only the selected terminals or pins will be numbered.
 '¢ 1 = All selected terminal strips - all terminals of the same strip as selected terminal will be numbered.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` POTENTIAL_N
 ``` | ``` Parameter to determine how N terminals will be treated during numbering. Values are:
 '¢0 = Ignore
 '¢1 = Do not modify, include in sequence. PE, N or SH terminals are not modified during numbering but are taken into account when numbering the other terminals.
         This means that the designations of the other terminals are assigned as though the PE, N or SH terminals were being included in the numbering.
 '¢2 = Renumber
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` POTENTIAL_PE
 ``` | ``` Parameter to determine how PE terminals will be treated during numbering. Values are:
 '¢ 0 = Ignore
 '¢ 1 = Do not modify, include in sequence. PE, N or SH terminals are not modified during numbering but are taken into account when numbering the other terminals.
         This means that the designations of the other terminals are assigned as though the PE, N or SH terminals were being included in the numbering.
 '¢ 2 = Renumber
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` POTENTIAL_SH
 ``` | ``` Parameter to determine how SH terminals will be treated during numbering. Values are:
 '¢ 0 = Ignore
 '¢ 1 = Do not modify, include in sequence. PE, N or SH terminals are not modified during numbering but are taken into account when numbering the other terminals.
         This means that the designations of the other terminals are assigned as though the PE, N or SH terminals were being included in the numbering.
 '¢ 2 = Renumber
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` MULTIPLETERMINALS
 ``` | ``` Also renumber multi path terminals. Values are:
 '¢ 0 = Don't modify - terminals with the property "Allow same designations" are ignored during numbering.
 '¢ 1 = Number same - terminals with the same designation with the "Allow same designations" property are given the same number.
 '¢ 2 = Number individually - terminals with the "Allow same designations" property are each given their own number.
         Therefore, multiple terminals which had the same number before numbering will have different numbers after numbering.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` KEEPALPHA
 ``` | ``` Keep alphabetical elements of the terminal number. Values are:
 '¢ 0 = Don't modify - terminals or pins with alphabetical elements in the designation are ignored during numbering.
 '¢ 1 = Keep alphabetical elements - the alphabetical elements of the terminal or pin designation are retained. The first numeric elements are renumbered. If the designation only has alphabetical elements, the old designation is attached to the new numbering. Sequential terminals with different counters but the same numerical component receive the same numerical component in the counter even after the numbering. 
 '¢ 2 = Number - all terminals / pins are renumbered. In doing so, the old designation is overwritten.
 This parameter is only effective with the following values of the TYPE parameter: "TERMINALS".
 ``` |
| ``` KEEPEXISTING
 ``` | ``` Keep existing cable DTs (optional). 
 Possible values: 0 = No (default value), 1 = Yes. 
 '¢ 0 = Renumber all of the cable DTs.
 '¢ 1 = Renumber only newly generated or copied cables. The DT of the already numbered cables is retained. The cables with "?" character in the identifier will be numbered.
 This parameter is only effective with the following values of the TYPE parameter: "CABLES".
 ``` |
| ``` KEEPIDENTIFIER
 ``` | ``` Keep the identifier (optional).
 Possible values: 0 = No (default value), 1 = Yes. 
 '¢ 0 = Overwrite the identifiers of the cables with the identifier from the identifier set that is used during numbering.
 '¢ 1 = Renumber existing cables and only reassign the counters. The identifier of the already numbered cables remains. The character "?" at the beginning of the identifier is not retained.
 This parameter is only effective with the following values of the TYPE parameter: "CABLES".
 ``` |
| ``` STARTVALUE_n
 ``` | ``` Start value. Where n is a connection group number (1,2,3...).
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` STEPVALUE_n
 ``` | ``` Step value. Where n is a connection group number (1,2,3...).
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` GROUP_n
 ``` | ``` Group parameter. Where n is a connection group number (1,2,3...).
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` OVERWRITE
 ``` | ``` Overwrite mode. Values are:
 '¢ 0 = All - always overwrite.
 '¢ 1 = ExceptManuals - overwrite all except those, which are marked as "manually set". 
 '¢ 2 = None - never overwrite.
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` AVOIDIDENTICALDESIGNATIONS
 ``` | ``` Values are:
 '¢ 0 = In entire project
 '¢ 1 = In the selection
 '¢ 2 = None
 '¢ 3 = Per counter reset range (structure/page)
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` VISIBILITY
 ``` | ``` Visiblity. Values are:
 '¢ 0 = All visible
 '¢ 1 = Do not modify
 '¢ 2 = Once per page and range
 This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |
| ``` MARKASMANUAL
 ``` | ``` Mark as "manually set". This parameter is only effective with the following values of the TYPE parameter: "CONNECTIONS".
 ``` |

**Example**

```
Numbering devices:

renumber /TYPE:DEVICES /STARTVALUE:1 /STEPVALUE:1 /USESELECTION:0 /OMITNUMERATEDBYPLC:0 /NUMERATECABLES:0 /IDENTIFIER:X* /CONFIGSCHEME:\"Kennbuchstabe ZÃ¤hler\" /POSTNUMERATE:0

renumber /TYPE:DEVICES /IDENTIFIER:V /POSTNUMERATE:0 /ALSONUMERATEDBYPLC:1 /NUMERATECABLES:1 /STARTVALUE:100 /STEPVALUE:5 /USESELECTION:1       

Numbering pages:

renumber /TYPE:PAGES /STRUCTUREORIENTED:0 /STARTVALUE:3 /STEPVALUE:10 /KEEPINTERVAL:1 /KEEPTEXT:0 /SUBPAGES:1 /USESELECTION:0

Numbering cables:

renumber /CONFIGSCHEME:Standard /TYPE:CABLES /STARTVALUE:7 /STEPVALUE:7 /USESELECTION:1 /KEEPEXISTING:1

renumber /CONFIGSCHEME:Standard /TYPE:CABLES /STARTVALUE:1 /STEPVALUE:1 /USESELECTION:0 /KEEPEXISTING:0 /KEEPIDENTIFIER:1

renumber /TYPE:CABLES /STARTVALUE:999 /USESELECTION:0

Numbering connections:

renumber /TYPE:CONNECTIONS /CONFIGSCHEME:Verbindungsorientiert /STARTVALUE_1:1 /STEPVALUE_1:1 /OVERWRITE:1 /AVOIDIDENTICALDESIGNATIONS:1 /VISIBILITY:1 /MARKASMANUAL:0 /USESELECTION:1 /GROUP_1:1

renumber /TYPE:CONNECTIONS /CONFIGSCHEME: Potenzialorientiert /STARTVALUE_1:13 /STEPVALUE_1:3 /OVERWRITE:0 /AVOIDIDENTICALDESIGNATIONS:0 /VISIBILITY:1 /MARKASMANUAL:1 /USESELECTION:0 /GROUP_1:1

Numbering terminals:

renumber /TYPE:TERMINALS /CONFIGSCHEME:Numerisch /SEQUENCE:1 /POTENTIAL_N:1 /POTENTIAL_PE:2 /POTENTIAL_SH:2 /POSTNUMERATE:0 /ALSONUMERATEDBYPLC:1 /MULTIPLETERMINALS:1 /KEEPALPHA:0 /STARTVALUE:1 /STEPVALUE:1 /PREFIX:p_ /SUFFIX:_s /USESELECTION:1

```