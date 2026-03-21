---
title: "Logging preferences"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_prefs_logging.htm"
file: "admin_r_prefs_logging"
category: "admin"
---

# Logging preferences

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Logging preferences

Path to the preferences:

Menu Window > Preferences

Dialog Preferences > Logging

For the error search in a model, notes (debug output) are output in the console view during the execution of different actions.

The following output is provided for the structure generators:

     * All plug and socket values
     * All objects that do not fit because
     * the superordinate component is not permitted or
     * the subordinate component would become its own superordinate component.

The debug output is enabled and/or disabled via Preferences > Logging > User > Structure generator DEBUG or Preferences > Logging > User > Structure generator > <Discipline name> DEBUG (see the following figure). Below Structure generator, only those disciplines are offered for which the action Generate structure has already been started.

### [Tab Logfile](javascript:void\(0\);)

The Activated option switches the logging on/off.

You define the formatting of a log entry (deactivated) in the Layout input field.

Enter the name of the log file in the File input field (deactivated).

Enter the possible size of the log file in the input field Maximum file size.

### [Tab Rolling logfile](javascript:void\(0\);)

The Activated option switches rolling logging on/off.

You define the formatting of a log entry (deactivated) in the Layout input field.

Enter the directory, the file pattern and the file extension of the rolling log file in the File pattern input field.

You can run the rolling logging at intervals from Minute-based to Weekly. In rolling logging, a new log file is generated for each new time interval during which a log entry is made. The file name of the log file corresponds to the time stamp, for example 2022-11-24_14-45.log. For a user-defined interval you specify an interval pattern in the input field Derive from pattern, for example YYYY\MM\dd\hh-mm generates a directory structure for the year, the month and the day and in it a log file, for example 2022\11\24\14-45.log.

### [Tab Console (external:OS)](javascript:void\(0\);)

The Activated option switches on/off the output to the operating system console.

You define the formatting of a log entry in the Layout input field.

Statement | Meaning | Example | Result  
---|---|---|---  
%d{Format} | Time stamp | %d{ISO8601} | 2022-11-24 14:45:09.533  
%d{YYY-MM-dd hh:mm:ss} | 2022-11-24 14:45:09  
%c{1} | Component | <%c{1}> | <P8Generator>  
%m | Message text | %m | Cannot find parameter 'Parameter name'.  
  
### [Tab Console (internal)](javascript:void\(0\);)

The Activated option switches on/off the output to the internal console.

You define the formatting of a log entry in the Layout input field.

Enter a value in kilobytes (kB) for the buffer memory of the internal console in the Console buffer input field.

Statement | Meaning | Example | Result  
---|---|---|---  
%d{Format} | Time stamp | %d{ISO8601} | 2022-11-24 14:45:09.533  
%d{YYY-MM-dd hh:mm:ss} | 2022-11-24 14:45:09  
%c{1} | Component | <%c{1}> | <P8Generator>  
%m | Message text | %m | Cannot find parameter 'Parameter name'.
