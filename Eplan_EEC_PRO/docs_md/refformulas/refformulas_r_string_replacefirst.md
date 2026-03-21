---
title: "replaceFirst(String regex, String new)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_string_replacefirst.htm"
file: "refformulas_r_string_replacefirst"
category: "refformulas"
---

# replaceFirst(String regex, String new)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  replaceFirst(String regex, String new) String methods Replaces the first occurrence of the character string which is matching the regular expression regEx by the character string new. If non character string matches the regular expression the original is returned. Please mind that for regex all characters which have a special meaning in regular expressions (e.g. $, (, ) have to be quoted by \. For the character string new the $-sign and \ are to be quoted, because the $-sign allows a group reference (see example: ='123'.replaceFirst('(\\\d)','a$1b')). replaceFirst(String regex, String new)  
---  
Arguments | String | regex | Regular expression  
String | new | Substituting string  
Return value | String |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
='abad'.replaceFirst('a','xyz') | xyzbad
