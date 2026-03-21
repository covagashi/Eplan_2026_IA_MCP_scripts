---
title: "Parameter sequences"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecoffice_k_parameter_sequences.htm"
file: "eecoffice_k_parameter_sequences"
category: "eecoffice"
---

# Parameter sequences

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Parameter sequences

A parameter sequence is a text block defined by a special basic structure that is rarely encountered in documents. The sequence begins with the opening token and ends with the closing token. The default values for the tokens are #{ for the opening token and } for the closing token. These values can be modified via model variables (see [Model variables](eecoffice_k_word_config_modelvariables.htm) and [ Word configuration](eecoffice_k_word_config.htm)).

The parameter to be applied is defined between the opening and closing token. The name of the parameter is required for this.

Other properties of the parameter can also be specified, but these will be evaluated only if the parameter does not yet exist when the document is read in. Type, Default value, and Comment can be entered in the sequence.

The syntax then follows this pattern:
    
        #{Typ:Parametername=Standardwert//Kommentar}

### [Example](javascript:void\(0\);)
    
        #{String:Ort=St01Einsetzen//Einbauort}

This means that Type, Default value, and Comment are independent of each other, and each is optional.

When a resource is assigned or edited and then saved, the content is read in and the parameter sequences are evaluated. The Office discipline then determines which parameters already exist and which have yet to be created. In the latter case, the appropriate parameters are created, while taking all of the entries into account.

In the process, missing entries for optional information, i.e. Type, Default value, and Comment, are replaced by the following values:

Statement | Value  
---|---  
Type | String  
Default value | <empty>  
Comment | <empty>  
  
If a new parameter has been created, or if a parameter already exists with the stated name, it is assigned to the main document or fragment whose resource has just been read in.
