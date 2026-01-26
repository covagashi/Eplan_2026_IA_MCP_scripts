# ExecuteScript

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/ExecuteScript.html

---

```
 Runs the given script.

```

| Parameter | Description |
| --- | --- |
| ``` ScriptFile
 ``` | ``` Script file to be run. File name with full path.
 ``` |
| ``` <further parameter>
 ``` | ``` Any further parameter will be passed on to the function of the script which is marked with the "[Start]" attribute.
 ``` |

**Remarks**

```
 Only scripts with the "[Start]" attribute can be run.

 It is possible to use scripts with ActionCallingContext as a parameter. The specified ActionCallingContext will be passed on to the script (just as any other further parameter). See also "Eplan.EplApi.ApplicationFramework.ActionCallingContext".

 For more information see also "User Guide" > "API Framework" > "Scripts" > "Simple script with parameters".

```

**Example**

```
In the following example, the script (i.e. the script function) requires 3 string parameters "Param1", "Param2" and "Param3":

      EPLAN.exe /Variant:"Electric P8" ExecuteScript /ScriptFile:"C:\...\EPLAN\Electric P8\Scripts\...\SimpleScriptWithParameters.cs" /Param1:"Hello" /Param2:"EPLAN" /Param3:"API developer!"

```