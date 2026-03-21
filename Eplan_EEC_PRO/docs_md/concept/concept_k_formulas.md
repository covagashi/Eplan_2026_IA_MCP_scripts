---
title: "Formulas"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_formulas.htm"
file: "concept_k_formulas"
category: "concept"
---

# Formulas

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Formulas

It is only possible to consistently reduce the number of parameters and to simplify the parameterization via the concept of derivation by making a comprehensive formula apparatus available. The formula apparatus makes it possible not only to query specific configurations using simple if-then-else constructs, but also to use basic mathematical operations to calculate device tags or IO addresses.

Formulas are used in a manner similar to how they are used in MS Excel. For example, a formula always begins with an equals sign =. Parameters are addressed by using the full name of the parameter preceded by a dollar sign $.

Example:

An equation for the sum of parameters A and B would appear as follows:

=$A+$B

In addition to simple calculations, the formula apparatus can also be used to ânavigateâ through the entire structure of a machine or plant. This means that every parameter, regardless of which component it belongs to, can be included in a calculation. There are various formula constructs for this type of navigation; the most important ones are mentioned here. Should a user wish to address a parameter from a superordinate level within a machine or plant, this can be accomplished using the mc construct.

Example:

If a user wishes to calculate the sum of parameters A and B, where parameter B belongs to a superordinate element, the equation would appear as follows:
    
        =$A+mc.$B

A detailed breakdown of all available formulas may be found in the [Formulas](refformulas_r_formulas.htm) section.
