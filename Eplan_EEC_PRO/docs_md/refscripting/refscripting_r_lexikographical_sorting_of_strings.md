---
title: "sort(List list, ComparatorClass c)"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refscripting_r_lexikographical_sorting_of_strings.htm"
file: "refscripting_r_lexikographical_sorting_of_strings"
category: "refscripting"
---

# sort(List list, ComparatorClass c)

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  sort(List list, ComparatorClass c) Sorts the alphanumeric strings of an array or list. EEC is provided with an own comparator (DefaultStringComparator), which lexicographic sorts strings. This enables the correct treatment of numbers. This allows lists and arrays of strings of the type Text1, Text2, etc. , Text10, Text11 to be sorted correctly. This comparator is also used in the formula language to sort string lists. sort(List list, ComparatorClass c)  
---  
Argument | List | list | List of alphanumeric strings.  
ComparatorClass | c | DefaultStringComparator.  
Return value |  |   
Exception error |  |  |   
Plug-in |  org.foederal.util.DefaultStringComparator java.util.Arrays java.util.ArrayList java.util.Collections  
[Example code](javascript:void\(0\);) Requirements:
     * The model data of install\scripting\scripting.eox have been imported.
The following script example (ScriptingExamples.sortLexigraphical) creates an unsorted array of alphanumeric strings. After the array has additionally been converted into a list, both are sorted and the results are output in the User Message Collector. For the example the SelectionAction sortLexigraphical can be executed on each project component. The methods Arrays.sort(stringArray, new DefaultStringComparator()) and Collections.sort(stringList, new DefaultStringComparator()) sort the array and the list lexigraphically (see rows 19 and 20). Information is output in the message log (see rows 10, 16, 23, 26 and 29).
    
        import org.foederal.util.ui.messages.UserMessageCollector;
    import org.foederal.util.DefaultStringComparator;
    import java.util.Arrays;
    import java.util.Collections;
    import java.util.ArrayList;
    
    void main(obj){
    	String scriptName = "sortLexigraphical";
    	String info = "### Start of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// Creating the example array and the example list
    	stringArray = new String[] { "text5", "text30", "text10", "text1", "text2"};
    	stringList = new ArrayList(Arrays.asList(stringArray));
    	info = "Unsorted list: "+ stringList;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	// Sorting
    	Arrays.sort(stringArray, new DefaultStringComparator());
    	Collections.sort(stringList, new DefaultStringComparator());
    	info = "Sorted list: "+ stringList;
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    	
    	info = "### End of script '" + scriptName + "' ###";
    	UserMessageCollector.addInfo(LIBRARY,'self',null,"Scripting",info);
    }                                    
    main(obj);

Result: Applied to the project component Feeder_Extended1.Mechatronic.Feeder of the tutorial, the SelectionAction specifies the strings of the sorted array and the sorted list in the User Message Collector.
    
        ### Start of script 'sortLexigraphical' ###
    Unsorted list: [text5, text30, text10, text1, text2]
    Sorted stringArray: [text1, text10, text2, text30, text5]
    Sorted stringList: [text1, text10, text2, text30, text5]
    ### End of script 'sortLexigraphical' ###
