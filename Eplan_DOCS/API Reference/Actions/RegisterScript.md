# RegisterScript

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/RegisterScript.html

---

```
 Register a script.

```

| Parameter | Description |
| --- | --- |
| ``` ScriptFile
 ``` | ``` Script file name with a complete path.
 ``` |
| ``` RegisterAgain
 ``` | ``` true: register a script with the same name again.
         When this parameter is set, no Decider is shown for this question.
 ``` |
| ``` ShowDecider
 ``` | ``` Show a Decider when needed. Value is true or false.
  The parameter is ignored when quiet mode is set. (Then RegisterAgain is set to true). 
 ``` |

**Remarks**

```
Two types of scripts can be registered: C#(*.cs) and VB.Net(*.vb)

```

**Example**

```
                RegisterScript /ScriptFile:c:\program\EPLAN\Scripts\myScript1.cs

```