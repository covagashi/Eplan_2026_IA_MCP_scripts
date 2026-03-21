---
title: "date(String format)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_function_data_string_format.htm"
file: "refformulas_r_function_data_string_format"
category: "refformulas"
---

# date(String format)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  date(String format) Functions Current date in date format specified by <format>. The date format is specified by combinations of letters. h hours in 12 hour format H hours in 24 hour format a AM/PM mark m minutes s seconds S milliseconds d day of the month D day of the year E weekday w week of the year W week of the month M month y year with two digits z time zone verbal (e.g.: CET) Z time zone in +/- hour format (e.g.: +0100) Moreover, the frequency of particular letters will affect the format: E weekday in short (e.g.: Mo) EEEE weekday in full (e.g.: Monday) M month with one digit (e.g.: 1,5,10) MM month with two digits (e.g.: 01,05,10) MMM month in short (e.g.: Jan, May, Oct) MMMM month in full (e.g.: January, May, October) yy year with two digits yyyy year with four digits zzzz time zone in full (e.g.: Central European Time) In addition to these letters any character may be used in the data format. The formatting characters must be quoted (e.g.: '\'CW\' w') If <format> is omitted, the current date in standard date format 'dd.MM.yyyy hh:mm:s:S' is returned. date(String format)  
---  
Argument | String | format | Date format  
Return value | String | Formatted date  
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
=date('dd.MM.yyyy - HH:mm') | 22.01.2016 - 11:14
