---
title: "replaceAll(String regex, String new)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_string_replaceall.htm"
file: "refformulas_r_string_replaceall"
category: "refformulas"
---

# replaceAll(String regex, String new)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  replaceAll(String regex, String new) String methods Replaces all character strings which are matching the regular expression regex by the character string new. If non character string matches the regular expression the original is returned. Please mind that for regex all characters which have a special meaning in regular expressions (e.g. $, (, ) have to be quoted by \. For the character string new the $-sign and \ are to be quoted, because the $-sign allows a group reference (see example: ='123'.replaceAll('(\\\d)','a$1b')). replaceAll(String regex, String new)  
---  
Arguments | String | regex | Regular expression  
String | new | Substituting string  
Return value | String |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
='abad'.replaceAll('a','xyz') | xyzbxyzd  
See also: [Regular Expressions (RegEx)](refregex_r_regular_expressions.htm)
