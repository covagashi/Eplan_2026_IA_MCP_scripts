---
title: "Operators"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_operators.htm"
file: "refformulas_r_operators"
category: "refformulas"
---

# Operators

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Operators Besides the methods also operators are defined for types of objects. Operators which are to be used in EEC are the basic calculation types (+,-,*,/), boolean operators (and, or, implies) and the compare operators (=,<,> <=,>=,<>). The following table shows the basic types of the model and the operators which can be used by them. Basic type | Meaning | Operator | Example  
---|---|---|---  
String | Character string | +, =, <, >, <=, >=,<> | 'This is a string'  
Boolean | Boolean expression | and, or, implies,=,<> | false, true  
Integer | Integer (32 bit) | +, -, *, /, =, <, >, <=, >=, <> | 1, - 5, 10  
Double | Floating point (64 bit) | +, -, *, /, =, <, >, <=, >=, <> | 1.5, -2.5, 0.0213, 2e-3  
The operators are processed in formulas in the following sequence:
     * negative preceding sign and not-operator (-, not)
     * Multiplication and division (*,/)
     * Addition and subtraction (+,-)
     * Comparison operators (=, <, >, <=, >=,<>)
     * Logic operators (and, or, implies)
     * Question mark operator (see [Conditions](refformulas_r_conditions.htm))
Using round parentheses influences the sequence of procedure.
