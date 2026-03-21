---
title: "column"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_column.htm"
file: "refformui_r_column"
category: "refformui"
---

# column

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  column The element <column> is exclusively used for the configuration of columns within <pureTable>. The attribute heading specifies the name of the column and is displayed in the header of the table. If the text of a heading is too long, line breaks can be inserted at any position with \n. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
heading | required |  |  | Defines the name of the column in a table heading.  
hSize | optional |  |  | Width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMax | optional |  |  | maximum width of the element  
EEC = width in characters  
Web application = width in pixels  
hSizeMaxPx | optional |  |  | maximum width of the element in pixels  
hSizeMin | optional |  |  | minimum width of the element  
EEC = minimum width in characters  
Web application = minimum width in pixels  
hSizeMinPx | optional |  |  | minimum width of the element  
EEC = minimum width in pixels  
Web application = minimum width in pixels  
hSizePx | optional |  |  | Width of the element  
EEC = width in pixels  
Web application = width in pixels  
readonly | optional | true, false |  | true = Column is read-only.  
false = Input can be written to the column.  
selectionReceiver | optional |  |  | Formula to the object, which stores the selected values of the table.  
selectionValue | optional |  |  | Writes the result of the formula instead of the selected cell content to the selectionReceiver  
tooltip | optional |  |  | Text or Form-UI of the overlaying tooltip (see [tooltip](JavaScript:TL_1902191.HHClick\(\)))  
visible | optional | true, false | true | true = table column is visible  
true = table column is invisible  
Allowed sub-elements | Quantity  
---|---  
[action](refformui_r_action.htm) | any  
[img](refformui_r_img.htm) | any  
[input](refformui_r_input.htm) | any  
[label](refformui_r_label.htm) | any  
[switch](refformui_r_switch.htm) | any  
Note For the element <input> only the types check and text are allowed, yet. If the determined object for selectionReceiver is a collection, any number of values may be stored by **multiple choice**. Table with multiple choice: To show this function, the following example code is inserted into the RTS24 Form-UI configuration. In addition the parameter pureTableSelection with the type List and Selection with the type String are created. Next to the table is a drop-down list where the content is determined by the selected items of the table. [Example code](javascript:void\(0\);)
    
        <table columns="2">
    	<td>
    		<pureTable variable="x" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    			<column hSizeMax="20" heading="Circular Transfer System">
    				<label text="this.name"/>
    			</column>
    			<column hSizeMaxPx="50" heading="Place">
    				<label text="=x.$Place"/>
    			</column>
    			<column hSizeMinPx="150" heading="Name" selectionReceiver="parameter('pureTableSelection')">
    				<label text="=x.name"/>
    			</column>
    		</pureTable>
    	</td>
    	<td valign="top">
    		<input font="Arial-bold" type="combo" values="=$pureTableSelection.collect(x|Pair{x,x})" receiver="parameter('Selection')"/>
    	</td>
    </table>

Table with actions: For each station listed in a pureTable table an action should be executed by a button. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=rmos" variable="x">
    	<column heading="Actions">
    		<action name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.ShowInfoDialogAction" arguments="List{'Title','Text'}" type="button" text="Info" />
     	</column>
    	<column heading="Station" hSizeMinPx="100">
    		<label text="x.name"></label>
    	</column>
    </pureTable>

Table passes the value of a formula instead of the selected cell content to the selectionReceiver: Within a pureTable table not the selected cell content should be passed to the selectionReceiver, but the resulting value of a formula. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=mos">
    	<column selectionReceiver="=parameter('selectionReceiver')"
    		selectionValue="mc.name + '.' + this.name" 
    		heading="Name"> 
    		<label text="this.name" /> 
    	</column>
    </pureTable> 
    <line> 
    	<label>Wert der Auswahl:</label> 
    	<gap hSizePx="10"/> 
    	<label text="$selectionReceiver" />
    </line>

Table contains images in the first column: In a pureTable table, an image is to be displayed in the first column. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=rmos" variable="x"> 
    	<column heading="Image"> 
    		<img src="=type('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Images.next_class').image"></img> 
    	</column> 
    	<column heading="Station" hSizeMinPx="100">  
    		<label text="x.name"></label> 
    	</column>   
    </pureTable

Table with controlled visibility for individual columns: The following example shows a table that originally had 4 columns. The visibility of the columns is controlled with a variable for which the value can be selected in a dropdown list field. The figure shows the table with a hidden column 4. [Example code](javascript:void\(0\);)
    
        <input receiver="parameter('visibility')" type="combo" values="=List{Pair{'hide no column',0},Pair{'hide column 1',1},Pair{'hide column 2',2},Pair{'hide column 3',3},Pair{'hide column 4',4}}">
    </input>
    <pureTable variable="x" receiver="=mos"
    	selectionMode="cell" width="900">
    	<column heading="First Column" visible="=if $visibility=1 then false else true endif">
    		<label text="=mos('Documentation_UI_Configuration.ProjectLibrary.HelpObjects.Station').indexOf(x)+1" />
    	</column>
    	<column heading="Second Column" visible="=if $visibility=2 then false else true endif">
    		<label text="x.name" />
    	</column>
    	<column heading="Third Column" visible="=if $visibility=3 then false else true endif">
    		<label text="=x.comment" />
    	</column>
    	<column heading="Fourth Column" visible="=if $visibility=4 then false else true endif">
    		<label text="date('dd.MM.yyyy')" />
    	</column>
    </pureTable>
