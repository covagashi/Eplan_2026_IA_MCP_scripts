---
title: "Layout spaces"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecpropanel_k_layoutspace.htm"
file: "eecpropanel_k_layoutspace"
category: "eecpropanel"
---

# Layout spaces

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Layout spaces

The mechanical structure is created within a layout space that is represented by a component of the LayoutSpace type.

A layout space with all the components installed in it can be exported as a 3D graphical macro or as a 3D symbol macro. This is carried out during he generation of the Pro Panel data. To this purpose the following parameters are to be created and to be inserted into the component of the LayoutSpace type:

Parameter | Parameter type | Meaning | Example  
---|---|---|---  
ExportMacroDescription | String | Specifies a description of the macro to be exported (optional). Must be completed with a semicolon! |  de_DE@Einspeisung;zh_CN@çµæº;en_US@Power supply;es_ES@AlimentaciÃ³n;fr_FR@Alimentation;nl_NL@Voeding;sv_SE@Matning;da_DK@Forsyning;ru_RU@Ð­Ð»ÐµÐºÑÑÐ¾Ð¿Ð¸ÑÐ°Ð½Ð¸Ðµ;pl_PL@Zasilanie;  
ExportMacroFullPath | String | Specifies the absolute name of the macro to be exported. If no value is entered, no macro is created. |  ="C:\\\Users\\\Public\\\EPLAN\\\DATA\\\Macros\\\MyLayoutSpace.ema"  
ExportMacroVariables | Map | Specifies free properties of the macro to be exported (optional). |  =Map{  
Pair{'config-id',12345}  
}  
ExportMacroVariant | String | Specifies the variant of the macro to be exported (optional). |  A  
  
If several layout spaces that have a valid value for the ExportMacroFullPath parameter exist in a configuration, these are transported as individual macros.

Optionally an item description can be specified. To do this, create a parameter of the PropertyMap type and add it to the component for the layout space. A map with the following syntax has to be specified as the value:
    
        =Map{
    	Pair{'36018','<Item description>'}
    }

### Read more

     * [Parameter](eecpropanel_k_parameter.htm)
