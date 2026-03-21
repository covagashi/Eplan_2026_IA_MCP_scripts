---
title: "Script syntax"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_script_syntax.htm"
file: "refscripting_r_script_syntax"
category: "refscripting"
---

# Script syntax

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Script syntax Scripts are created in native Java. The following rules apply to strings that contain a $ character. If the string is emphasized by double quotes, the properties of the object are accessed in Groovy, similar to the accessing of parameters in EEC. This produces a string that contains the result of this access. In order to display the $ character in a string, the string must be emphasized by single quotes. [Example code:](javascript:void\(0\);)
    
        String w = 'world';
    String s1 = 'Hello $w';
    String s2 = "Hello $w";
    System.out.println(s1); // -> Hello $w
    System.out.println(s2); // -> Hello world

The s1 variable saves the string in a character-perfect manner. In the case of the s2 variable, the w variable is resolved, and the value is inserted. Existing scripts in which formulas with parameter access are defined in this manner must be checked for notation and modified if necessary to avoid any problems. As of Version 2023 EEC supports SCRIPTING in Groovy 4. Existing scripts (for Groovy 1) that use global final variables may need to be customized to the changed support. [Example code for global "final variable" in Groovy 1](javascript:void\(0\);)
    
        final def variable = 5 //no longer valid for Groovy 4

[Example code for global "final variable" in Groovy 4](javascript:void\(0\);)
    
        def method() {
    	final def variable = 5 //valid for Groovy 4
    }

The complete scope of a Groovy script in Groovy 1 must be encapsulated by a method so that global "final variables" are valid. [Example code for the migration of global "final variables" from Groovy 1 to Groovy 4](javascript:void\(0\);) Before the migration:
    
        final def variable = 5
    variable = variable + 1
    print variable

After the migration:
    
        main()
    def main() {
    	final def variable = 5
    	variable = variable + 1
    	print variable
    }
