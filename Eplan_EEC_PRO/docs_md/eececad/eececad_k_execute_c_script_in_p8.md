---
title: "Executing C# scripts in Eplan Electric P8"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eececad_k_execute_c_script_in_p8.htm"
file: "eececad_k_execute_c_script_in_p8"
category: "eececad"
---

# Executing C# scripts in Eplan Electric P8

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Executing C# scripts in Eplan Electric P8

After the generation of Eplan Electric P8 projects, the execution of a C# script in P8 can optionally be initiated.

A parameter with the absolute path to the C# script must exist in order to execute a script. The path has to be specified with double backslashes, for example =c:\\\scripts\\\ecad\\\myP8Script.cs.

A further parameter can optionally be specified that contains a map with the arguments that are transferred to the C# script when called.

The project components of the WiringDiagram type have to contain these parameters.

The names of these parameters are Script and ScriptArguments by default. Any names deviating from these are to be entered in the model variables.

The C# script for Eplan Electric P8 must contain a method that is identified by the [Start] attribute. The name of the method can be anything.

Currently, the data types string and int are supported for the arguments of the Start method. The order of the arguments does not have to be followed, because the assignment is realized via the parameter names.

### [Example](javascript:void\(0\);)

The following C# script should be called CreatePDF.cs.
    
        using System.Text;
    using System.Xml;
    using System.IO;
    using System.Windows.Forms;
    using Eplan.EplApi.Scripting;
    using Eplan.EplApi.ApplicationFramework;
    using Eplan.EplApi.Base;
    
    public class Script
    {
    	static int nActionsPercent = 100;
    	static int nActions = 7;
    
    	[Start]
    	public void Function(
    		string ProjectName,
    		//pdf
    		string PDFActive, string PDF_ExportPathPDF, string PDF_BlackWhite, string PDF_UseZoom, string PDF_Language, string PDF_3D_Modelview
    	)
    ...
    }

Explanation:

In order to execute this script, the name of the C# script has to be specified as the parameter value for the EEC parameter Script. In addition values for the C# script parameters PDFActive, PDF_ExportPathPDF, PDF_BlackWhite, PDF_UseZoom, PDF_Language and PDF_3D_Modelview are expected.

The extended values are handed over as a map by means of the EEC parameter ScriptArguments:
    
        =Map
    {
    	Pair{'PDFActive', 'true'},
    	Pair{'PDF_ExportPathPDF', '=c:\\TEMP'},
    	Pair{'PDF_BlackWhite', 'false'},
    	Pair{'PDF_UseZoom', 'false'},
    	Pair{'PDF_Language', 'de_DE'},
    	Pair{'PDF_3D_Modelview', 'false'}
    }

The refreshFS parameter can optionally be specified in a C# script. If the value of the parameter is true, the internal file system of the EEC is synchronized after execution of the script.

### Read more

     * [Eplan actions](../../../../plattform/2025/Content/htm/availableactions_k_start.htm)
