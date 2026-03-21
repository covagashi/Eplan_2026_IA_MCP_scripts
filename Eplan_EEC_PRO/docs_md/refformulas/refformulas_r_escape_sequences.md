---
title: "Escape sequences"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_escape_sequences.htm"
file: "refformulas_r_escape_sequences"
category: "refformulas"
---

# Escape sequences

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Escape sequences Texts have to partially contain control or special characters which cannot be input with the available amount of characters:  
     * **Special characters:** The formula mechanism defines the apostrophe (') as a special character to mark text, e.g. ='au' + 'to'. The apostrophe sometimes has to be part of a text, for example when creating a parts list.
     * **Control characters:** A text needs control characters for line breaks, tabulators, etc.
Special characters and control characters within text are marked by a backslash in front (**quote, escape sequence**). The following table contains all escape sequences which are recognized by the formula language: Case | Result | Value (Formula) | Comment  
---|---|---|---  
Apostrophe | a'b | ='a\'b' |   
Backslash | a\b | ='a\\\b' |   
Line break |  a b | ='a\nb' |   
Tabulator | a b | ='a\tb' |   
Carriage return |  | ='a\rb' | Command carriage return  
Form feed |  | ='a\fb' | Command form feed
