---
title: "Calling script in scripts"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_calling_script_in_script.htm"
file: "refscripting_r_calling_script_in_script"
category: "refscripting"
---

# Calling script in scripts

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Calling script in scripts Scripts can be called in other scripts. The following fragment can be used to call a script: [Example code in Groovy](javascript:void\(0\);)  
      
        import com.mind8.mechatronic.skill.eos.TypeClass;
    TypeClass.findType(self.getUnitOfWork(),<AbsoluteName>).perform(
    <MethodName>,<Argument1>,<Argument2>,...);

This runs with up to 10 arguments, beyond that an array has to be used as the second argument (the array can also be used with less than 10 arguments). [Example code in Groovy](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.eos.TypeClass;
    arguments = new Object[]{<Argument1>,<Argument2>,...,<Argument23>};
    TypeClass.findType(self.getUnitOfWork(),<AbsolutName>).perform(
    <MethodName>,arguments);
