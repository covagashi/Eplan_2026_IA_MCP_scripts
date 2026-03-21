---
title: "de.eplan.eec.enableStartStopFormulaCalculation"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/admin_r_vmargs_enablestartstopformulacache.htm"
file: "admin_r_vmargs_enablestartstopformulacache"
category: "admin"
---

# de.eplan.eec.enableStartStopFormulaCalculation

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## de.eplan.eec.enableStartStopFormulaCalculation

The EEC argument must be transferred with the following syntax:
    
        -D<Argument>=<Value>

EEC argument |  Usage  
---|---  
-Dde.eplan.eec.enableStartStopFormulaCalculation=true/false |  Optional  
**Annotation**  
With the EEC argument de.eplan.eec.enableStartStopFormulaCalculation the possibility is activated to stop the renewed calculation of formula results and restart them. If the possibility is activated, the  button appears in the Parameter editor of a mechatronics project component. If the formula calculation is switched off, the renewed calculation of all parameters is not executed in the editor when a formula is being edited. The results already calculated are used for the calculation of the edited formula. Example:
    
        -Dde.eplan.eec.enableStartStopFormulaCalculation=true  
  
### Tip

Environment variables of Windows are supported for this specification. Environment variables are enclosed by percentage signs, e.g. %WINDIR%. A percentage sign is masked by %% and can be used as part of a path specification.

Environment variables that cannot be broken up are listed in the ec.log log file and EEC terminates.
