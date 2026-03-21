---
title: "Use of Maps: Page Numbering Example"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_frf_example_page_numbering.htm"
file: "refformulas_r_frf_example_page_numbering"
category: "refformulas"
---

# Use of Maps: Page Numbering Example

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Use of Maps: Page Numbering Example The aim is to calculate the page number (parameter page number) for wiring diagram macros. The following rules apply:
     * All page objects are assigned a chapter (parameter chapter).
     * Within each chapter the page numbering should begin again with "1".
[Example](javascript:void\(0\);) ECAD.ChapterItems | Chapter | page number to calculate  
---|---|---  
PageA | 1 | 1  
PageB | 2 | 1  
PageC | 1 | 2  
PageD | 3 | 1  
PageE | 2 | 2  
PageF | 1 | 3
