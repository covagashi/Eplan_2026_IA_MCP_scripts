---
title: "tabbedPane"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_tabbedpane.htm"
file: "refformui_r_tabbedpane"
category: "refformui"
---

# tabbedPane

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  tabbedPane Multiple Form-UIs can be displayed in a single editor as tabs via the <tabbedPane> element. Each individual tab is defined via the <tab> element (see tab). Tabs can also be created generically by means of the <loop> element (see also [loop](refformui_r_loop.htm)). Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
readonly | optional | true, false |  | true = Tab view is read-only.  
false = Input fields in the tab view can also be written to.  
Allowed sub-elements | Quantity  
---|---  
[tab](refformui_r_tab.htm) | any  
[loop](refformui_r_loop.htm) | any  
Tabs created statically: The following example displays three static tabs. [Example code](javascript:void\(0\);)
    
        <form id="tabbedPane" title="tabbed pane">
    	<tabbedPane>
    		<tab title="tab 1" >
    			<table border="2" boColor="0,0,0" columns="3">
    				<td> <label>Cell 1.1</label> </td>
    				<td> <label>Cell 1.2</label> </td>
    				<td> <label>Cell 1.3</label> </td>
    				<td> <label>Cell 2.1</label> </td>
    				<td> <label>Cell 2.2</label> </td>
    				<td> <label>Cell 2.3</label> </td>
    			</table>
    		</tab>
    		<tab title="tab 2">
    			<table border="2" boColor="255,0,0" columns="3">
    				<td> <label>Cell 1.1</label> </td>
    				<td> <label>Cell 1.2</label> </td>
    				<td> <label>Cell 1.3</label> </td>
    				<td> <label>Cell 2.1</label> </td>
    				<td> <label>Cell 2.2</label> </td>
    				<td> <label>Cell 2.3</label> </td>
    			</table>
    		</tab>
    		<tab title="tab 3">
    			<table border="2" boColor="0,255,0" columns="3">
    				<td> <label>Cell 1.1</label> </td>
    				<td> <label>Cell 1.2</label> </td>
    				<td> <label>Cell 1.3</label> </td>
    				<td> <label>Cell 2.1</label> </td>
    				<td> <label>Cell 2.2</label> </td>
    				<td> <label>Cell 2.3</label> </td>
    			</table>
    		</tab>  
    	</tabbedPane>
    </form>

Tabs created by means of a loop: The following example shows tabs that are generically created with a loop. [Example code](javascript:void\(0\);)
    
        <form id="loopedTabbedPane" title="looped tabbed pane">
    	<tabbedPane>
    		<loop receiver="=mos('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Station')" variable="x">
    			<tab title="=x.name">
    				<table border="2" boColor="0,255,0" columns="3">
    					<td> <label>Cell 1.1</label> </td>
    					<td> <label>Cell 1.2</label> </td>
    					<td> <label>Cell 1.3</label> </td>
    					<td> <label>Cell 2.1</label> </td>
    					<td> <label>Cell 2.2</label> </td>
    					<td> <label>Cell 2.3</label> </td>
    				</table>
    			</tab>
    		</loop>
    	</tabbedPane>
    </form>
