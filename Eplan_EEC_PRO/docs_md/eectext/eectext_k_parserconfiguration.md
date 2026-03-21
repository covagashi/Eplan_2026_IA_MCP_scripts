---
title: "Parser configuration of text disciplines"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eectext_k_parserconfiguration.htm"
file: "eectext_k_parserconfiguration"
category: "eectext"
---

# Parser configuration of text disciplines

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Parser configuration of text disciplines For each text discipline you can specify settings for the parsing of the resource files independently. The call takes place via the text discipline component <Text discipline name>Parser Configuration. The following figure shows a typical parser configuration with the default settings: The name of the parser configuration automatically conforms to the name of the text discipline. A separate icon can be specified in the Image field for each text discipline. Tokens can be specified for the following parser elements in the Parameter syntax area: Parameter | Default token | Meaning  
---|---|---  
Start | #{ | With this token the parser recognizes the beginning of a parameter sequence  
Type Name Separator | : | With this token the parser detects that all characters between the start token and the separator token are to be interpreted as the type and all subsequent characters up to a further token as the name of the parameter  
Token assignment | = | If an assignment token follows the name of a parameter, all the subsequent characters up to a further token are interpreted as the parameter value  
Comment identifier | // | After the token for the comment start all further characters until the token end are interpreted as a comment  
End | } | With this token the parser recognizes the end of a parameter sequence
