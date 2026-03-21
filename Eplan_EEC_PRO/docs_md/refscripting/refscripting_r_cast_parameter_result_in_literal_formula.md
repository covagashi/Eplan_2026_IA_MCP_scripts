---
title: "Change parameter result to literal formula"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_cast_parameter_result_in_literal_formula.htm"
file: "refscripting_r_cast_parameter_result_in_literal_formula"
category: "refscripting"
---

# Change parameter result to literal formula

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Change parameter result to literal formula If the result of a parameter should be fixed, it can be written to the parameter as a literal formula. The LiteralFormulaBuilder class performs this for all base types (Integer, Double, Boolean, String, Pair, Map, OrderedMap, BidiMap, List, Bag, Set) and for mechatronic components and classes as well. The least are created as pattern of the following forms:  
      
        if existsRef('p.b.c.d'') then ref('a.b.c.d') else default endif

and
    
        if existsType('b.c.d.e') then type('b.c.d.e') else default endif

[Example code in Groovy](javascript:void\(0\);)
    
        import com.mind8.mechatronic.skill.api.LiteralFormulaBuilder;
    // mo is any mechatronic component
    parameter = mo.getParameter("Param1");
    formulaResult = parameter.getCalculatedValue();
    parameter.setPrettyValue(LiteralFormulaBuilder.buildLiteralFormula(formulaResult));
