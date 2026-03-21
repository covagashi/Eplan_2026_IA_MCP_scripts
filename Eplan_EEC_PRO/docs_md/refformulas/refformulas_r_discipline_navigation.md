---
title: "Navigation methods for discipline-specific components"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformulas_r_discipline_navigation.htm"
file: "refformulas_r_discipline_navigation"
category: "refformulas"
---

# Navigation methods for discipline-specific components

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Navigation methods for discipline-specific components Navigation methods for discipline components can only be applied if a discipline structure has already been generated. Without discipline structure the navigation methods for discipline components return an error. These errors are not logged but instead a message text is displayed instead of the parameter value. In this case the value field has a yellow background color. The following formula can be used to ensure that an explanatory text is displayed instead of an error message: [Example formula](javascript:void\(0\);)  
      
        =if(not(origin.isNull())) then
    	dc // this part should be replaced by the formular needed
    else
    	'Calculation is performed only in discipline structure'
    endif

Explanation: not(origin.isNull()) navigates to the mechatronic component in which the discipline-specific component is contained and checks whether the formula does not return the value null there. If this is the case, you are in the discipline structure and can have the desired calculation carried out. If this is not the case, you are in the mechatronic structure and the value is replaced by the text Calculation is performed only in discipline structure.
