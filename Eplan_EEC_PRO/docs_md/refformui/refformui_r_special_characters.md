---
title: "Displaying Special Characters"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_special_characters.htm"
file: "refformui_r_special_characters"
category: "refformui"
---

# Displaying Special Characters

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Displaying Special Characters Special characters cannot be used directly in text or in formulas of attributes, but must be inserted as named characters (named entities) (e.g. &amp;). For text, numerical notation is also permitted (e.g. &#9871;). A special role is one of successive spaces, because they are interpreted and displayed as one single space, as the following example shows. Note The > character is currently automatically replaced by the &gt; in Form-UI configurations. Tip The < and & characters are currently not permitted in Form-UI configurations and thereby prevent the editor from being saved. Before the editor can be saved, these characters must be replaced by their entities. [Example code](javascript:void\(0\);)
    
        <label>
    	Text Text
    </label>

Result: Text Text In order to use multiple spaces, e.g. to arrange the text in a structure, the numerical notation for each space is inserted: &#32; [Example code](javascript:void\(0\);)
    
        <label>
    	Text&#32;&#32;&#32;Text
    </label>

Result: Text Text The following table lists the most common special characters: Special characters | Description | Entity | Numerical notation  
---|---|---|---  
| Blank |  | &#32;  
" | Straight quotes | &quot; | &#34;  
& | Ampersand | &amp; | &#38;  
' | Apostrophe | &apos; | &#39;  
< | Left angle bracket | &lt; | &#60;  
> | Right angle bracket | &gt; | &#62;
