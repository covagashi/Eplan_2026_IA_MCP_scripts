---
title: "Solution Step 1: Chapter-Pages-Map"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_frf_example_page_numbering_step1.htm"
file: "refformulas_r_frf_example_page_numbering_step1"
category: "refformulas"
---

# Solution Step 1: Chapter-Pages-Map

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Solution Step 1: Chapter-Pages-Map First a map (Parameter ChapterPagesMap) is composed with all pages of a chapter (keys=chapters, values=pages). The aim of the solution step: Chapter-Pages-Map  
---  
Key | Values  
1 | <<PageA>>, <<PageC>>, <<PageF>>  
2 | <<PageB>>,<<PageE>>  
3 | <<PageD>>  
      
        $ChapterPagesMap=mroot.rmos('ECAD.ChapterElement').intoInject(Page,map|
    if not map.containsKey(Page.$Chapter)
    then map.add(Pair{Page.$Chapter,List{Page}})
    else map.add(Pair{Page.$Chapter,map.value(Page.$Chapter).append(Page)}) endif,Map{})
