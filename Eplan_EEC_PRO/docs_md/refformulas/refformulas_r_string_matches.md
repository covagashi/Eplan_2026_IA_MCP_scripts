---
title: "matches(String regEx)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_string_matches.htm"
file: "refformulas_r_string_matches"
category: "refformulas"
---

# matches(String regEx)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  matches(String regEx) String methods Delivers true if the character string matches the regular expression regEx. matches(String regEx)  
---  
Argument | String | regEx |   
Return value | Boolean |   
[Examples](javascript:void\(0\);) Formula | Result  
---|---  
='abcaaefgaac'.matches('[a]{2}') | false  
='abcaaefgaac'.matches('\\\w*') | true  
='abcaaefgaac'.matches('abc.*') | true  
='abcaaefgaac'.matches('.*gaac') | true  
='abcaaefgaac'.matches('.*efg.*') | true
