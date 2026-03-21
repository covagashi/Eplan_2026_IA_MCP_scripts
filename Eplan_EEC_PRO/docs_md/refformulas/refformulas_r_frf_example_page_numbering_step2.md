---
title: "Solution Step 2: Pages-Pagenumber-Map"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_frf_example_page_numbering_step2.htm"
file: "refformulas_r_frf_example_page_numbering_step2"
category: "refformulas"
---

# Solution Step 2: Pages-Pagenumber-Map

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Solution Step 2: Pages-Pagenumber-Map The Pages-Pagenumbers-Map (parameter PagesPagenumbersMap) can now be built from the Chapter-Pages-Map. The keys are the pages, the values are the calculated page numbers. The aim of the solution step: Pages-Pagenumber-Map  
---  
Key | Value  
<<PageA>> | 1  
<<PageB>> | 1  
<<PageC>> | 2  
<<PageD>> | 1  
<<PageE>> | 2  
<<PageF>> | 3  
      
        $PagesPagenumbersMap=mroot.rmos('ECAD.ChapterElement').intoInject(Page,map|  
    map.add(Pair{Page, $ChapterPagesMap.value(Page.$Chapter).indexOf(Page)+1}),Map{})

The page numbers can be calculated with this formula:
    
        $Pagenumber=mroot.$PagesPagenumbersMap.value(origin.ifNull(this))

The performance will not increase by the Pages-Pagenumbers-Map, because even without this map the page number is accessed only once per page. Strictly speaking, the performance decreases slightly, because in addition to the indexOf(this) in the construction of the map the hash function to determine the keys is performed n times for the query on the map. The page numbers without Pages-Pagenumbers-Map can be calculated with this formula:
    
        $Pagenumber=mroot.$ChapterPagesMap.value($Chapter).indexOf(origin.ifNull(this))+1
