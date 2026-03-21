---
title: "Quantifiers in Regular Expressions"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refregex_r_quantifier.htm"
file: "refregex_r_quantifier"
category: "refregex"
---

# Quantifiers in Regular Expressions

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Quantifiers in Regular Expressions Characters | Meaning | Example | Result  
---|---|---|---  
? | exactly once | 'a' matches ('a?')  
'aa' matches ('a?') | true  
false  
+ | once or more times | 'a' matches ('a+')  
'aa' matches ('a+')  
'' matches ('a+') | true  
true  
false  
* | zero or once or more times | 'aa'.matches('a*')  
''.matches('a*') | true  
true  
{n} | exactly n times | 'aaa'.matches('a{3}')  
'aaa'.matches('a{2}') | true  
false  
{n,} | at least n times | 'aaa'.matches('a{2,}') | true  
{n,m} | at least n times but not more than m times | 'a'.matches('a{1,2}')  
'aa'.matches('a{1,2}')  
'aaa'.matches('a{1.2}') | true  
true  
false
