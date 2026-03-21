---
title: "Modularization of schematics"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/concept_k_modularization_of_schematics.htm"
file: "concept_k_modularization_of_schematics"
category: "concept"
---

# Modularization of schematics

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Modularization of schematics

In many application contexts, whole pages or even whole sections of schematics are reusable within a project or in several projects. The only requirement is that certain texts on the schematic pages, such as DTs, voltages, and frequencies, be adjustable, i.e. parameterizable. A sample application would be documentation for a roller conveyor that is installed several times with a similar structure in the same installation.

Sometimes the variance is so large, however, that not even a schematic page can be reused in other projects in a sensible way. The following diagram presents an example and illustrates the modularization approach:

The above example shows a schematic page that contains an input card and two switches. In general, any combination of different sensors (current paths) can be connected to an input card. It is therefore pointless to maintain a completed schematic page in a modular system. In order to minimize the variance of modular-system components, it is necessary to disassemble the schematic page. A schematic page, which will be referred to in the following as simply a **page** , now contains only the basic, invariant components of a page, for example, an input card. The current paths indicated in the example can be positioned on one page as **fragments**.

Wiring diagrams are thus modularized by means of the following three basic elements (**ECAD objects**):

     * **Schematic** : Every project requires at least one element of the schematic type. This object represents the corresponding project in the ECAD system and provides the framework for the pages and fragments to be incorporated.
     * **Page** : Represents a schematic page. A page contains both the page properties and all or part of the graphical content of a schematic page. Typical parameters include the location or the page number.
     * **Fragment** : Objects of the fragment type represent the lowest structural level of ECAD-specific objects. They encapsulate a partial circuit within a schematic page. Fragments, in turn, can contain other fragments. The âreversing contactor circuitâ fragment, for example, can contain the âbrakeâ fragment.
