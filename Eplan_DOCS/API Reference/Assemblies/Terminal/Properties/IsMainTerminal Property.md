# IsMainTerminal Property

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/Eplan.EplApi.DataModelu~Eplan.EplApi.DataModel.EObjects.Terminal~IsMainTerminal.html

---

Determines whether terminal is main.

Syntax

**C#**



public bool IsMainTerminal {get; set;}

public:

property bool IsMainTerminal {

   bool get();

   void set (    bool value);

}


Remarks

This property returns true if this terminal is a main terminal. The terminal is then similar to a main function. For example, for a main terminal the function templates are displayed in the terminal strip navigator, and a device selection can be performed. A terminal strip can contain as many main terminals as you want. See also chapter 'Defining Multi-level Terminals' of EPLAN Help for more information concerning multi-level terminals.

Example

In order to create a multi-level terminal, please use the following code:

**C#**

```


//preparing terminal symbol

string strSymbolLibName = "IEC_symbol";

string strSymbolName = "X2_B";

int nVariant = 1;

Symbol oSymbol = new Symbol(new SymbolLibrary(m_oTestProject, strSymbolLibName), strSymbolName);

SymbolVariant oSymbolVariant = new SymbolVariant();

oSymbolVariant.Initialize(oSymbol, nVariant);

int iDevicePos = 1; // be sure this ID is unique in terminal strip

int iSortPos = 1;

Terminal term1 = new Terminal();

term1.Create(oPage, oSymbolVariant);

term1.NameParts = plName;

term1.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term1.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term1.Properties.FUNC_TERMINALLEVEL = 3;

term1.IsMainTerminal = true;

++iSortPos;

Terminal term2 = new Terminal();

term2.Create(oPage, oSymbolVariant);

term2.NameParts = plName;

term2.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term2.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term2.Properties.FUNC_TERMINALLEVEL = 2;

term2.IsMainTerminal = false;

++iSortPos;

Terminal term3 = new Terminal();

term3.Create(oPage, oSymbolVariant);

term3.NameParts = plName;

term3.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term3.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term3.Properties.FUNC_TERMINALLEVEL = 1;

term3.IsMainTerminal = false;

++iSortPos;

++iDevicePos;  // new device will be created

Terminal term4 = new Terminal();

term4.Create(oPage, oSymbolVariant);

term4.NameParts = plName;

term4.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term4.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term4.Properties.FUNC_TERMINALLEVEL = 3;

term4.IsMainTerminal = true;

++iSortPos;

Terminal term5 = new Terminal();

term5.Create(oPage, oSymbolVariant);

term5.NameParts = plName;

term5.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term5.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term5.Properties.FUNC_TERMINALLEVEL = 2;

term5.IsMainTerminal = false;

++iSortPos;

Terminal term6 = new Terminal();

term6.Create(oPage, oSymbolVariant);

term6.NameParts = plName;

term6.Properties.FUNC_TERMINALDEVICEPOSITION = iDevicePos;

term6.Properties.FUNC_TERMINALSORTCODE = iSortPos;

term6.Properties.FUNC_TERMINALLEVEL = 1;

term6.IsMainTerminal = false;

++iSortPos;

```
