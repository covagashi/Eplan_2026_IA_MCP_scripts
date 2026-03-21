---
title: "pureTable"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_puretable.htm"
file: "refformui_r_puretable"
category: "refformui"
---

# pureTable

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  pureTable The element <pureTable> is used to display large amounts of data in a table. Within a table column only one of the elements <label> or <input> are presented. For the <input> element only the types check, text and combo are allowed. The attribute receiver has to return a list which is used to iterate over in the table. Sorting the content: The content of the table is displayed in order of iterations, but can be sorted in ascending or descending order for each column. Each mouse click on the columns header switches between unsorted, ascending order and descending order. The manually selected value is stored persistently. Content filtering: To limit the amount of viewable content filters can be activated and configured as needed. The following filter types are possible:
     * Filter for free text.
     * Filter for selection of existing cell content out of a drop-down list.
Filter for free text: If this filter is configured, a row underneath the header row appears, where filter text may be input for each column. Predefined filter are also displayed underneath the header row and may be overwritten. If the content is limited by a predefined filter and the filter is changed afterwards to show more content, a scrollbar appears on the right border of the table. The manually entered value is stored persistently. Filter for selection of existing cell content out of a drop-down list: If this filter is configured, a row underneath the header row appears, containing a drop-down list box for each column. The drop-down list boxes are filled-up with values of the respective column. The selected value of a drop-down list box limits the shown number of table rows. A selected filter value is stored persistently. Column width: The width of the columns is predefined by several attributes but may be changed manually. The manually entered columns widths are stored persistently. Modifying of cell contents: To start the editor in a modifiable cell the following actions are possible:
     * A single click opens the editor and the complete cell content is marked.
     * A double click opens the editor and places the cursor at the mouse cursor.
     * Pressing the Enter key or the [F2] key opens the editor and the complete cell content is marked.
Marking and copying of table contents: The content of a single table cell (attribute selectionMode="cell") is marked copied to the clipboard by means of the mouse and the key-combination [Ctrl] \+ [C]. Further table cells are marked by pressing the [Ctrl] key at the same time and an area of cells is marked by pressing the [Shift] key at the same time. A complete table row is also marked with the mouse, if the selectionMode="row" attribute is set. To past the content of the clipboard back into table cells the key combination [Strg] \+ [V] is used. The files in the clipboard should be conform to the Excel format, meaning that columns are separated by tabulators, rows by line breaks, cells are surrounded by quotation marks. To show a quotation mark it must be written twice. [Example code of valid clipboard contents](javascript:void\(0\);)
    
        1.1 2.1 3.1  
    1.2 2.2 "(""2.3"")"  
    1.3 2.3 3.3

Possible inserting modes:
     * Inserting the complete clipboard content:
If the clipboard contains **as many values** **as cells** are **marked in the table** , the values are pasted into the marked cells. If the clipboard contains **less values** than **cells** are **marked** in the table, then the values of clipboard are pasted into the according number of table cells.
     * Multiple pasting of a single value:
If the clipboard contains only a single value, this value is pasted into all marked table cells. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
columnsMax | optional, only together with freezeLeft and/or freezeRight |  |  | Maximum number of displayed columns beside/between fixed columns.  
freezeLeft | optional | true, false | false | Number of fixed columns on the left side of the table.  
freezeRight | optional | true, false | false | Number of fixed columns on the right side of the table.  
height | optional | Integer, fillForm |  | Height of the entire table.  
Integer = height of the table in pixel  
fillForm = the table occupies the entire height of the Form-UI  
maxHeight | optional, only together with height="fillForm" |  |  | The pureTable will not grow higher than the maximum height in pixel when the Form-UI window is enlarged.  
maxWidth | optional, only in conjunction with width="fitToForm" |  |  | The pureTable will not grow wider than the maximum width in pixel when the Form-UI window is enlarged.  
minHeight | optional, only together with height="fillForm" |  |  | The Form-UI window cannot become smaller than the minimum height of the pureTable in pixels.  
minWidth | optional, only in conjunction with width="fitToForm" |  |  | The Form-UI window cannot become smaller than the minimum width of the pureTable in pixels.  
readonly | optional | true, false |  | true = pureTable is read-only.  
false = Input can be written to the pureTable.  
receiver | required |  |  | A list has to be returned. In the table is iterated over the list and thus the number of lines below the header determined.  
If a formula returns a list of components, the determined component can be referenced for each iteration.  
selectionMode | optional | cell, row | row | Switches the selection mode between cell content and row content.  
rows | optional |  |  | Number of displayed table rows  
rowsMax | optional |  |  | Maximum number of displayed table rows  
rowsMin | optional |  |  | Minimum number of displayed table rows The minimum number of table rows cannot be less than 3.  
variable | optional |  |  | Name of the variable  
visible | optional | true, false | true | true = table is visible  
true = table is invisible  
width | optional | Integer, fitToForm |  | Width of the entire table.  
Integer = Width of the table in pixels  
fitToForm = Table takes on the entire width of the Form-UI  
Allowed sub-elements | Quantity  
---|---  
[column](refformui_r_column.htm) | any  
[filters](refformui_r_filters.htm) | 0..1  
Table with two columns: The following example shows a table that lists, for all the components of type Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator, the parameters Place and Name. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    	<column heading="Place">
    		<label text="=$Place"/>
    	</column>
    	<column heading="Name">
    		<label text="=this.name"/>
    	</column>
    </pureTable>

Table with three columns of predefined width: The following example shows a table, that lists the name of the circular transfer system and of all components of the type 'Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator' the parameters Place and Name. [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    	<column hSizeMax="20" heading="Circular Transfer System">
    		<label text="this.name"/>
    	</column>
    	<column hSizeMaxPx="50" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="150" heading="Name">
    		<label text="=x.name"/>
    	</column>
    </pureTable>

Table with predefined filter: The following example shows a table, that lists the name of the circular transfer system and of all components of the type 'Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator' the parameters Place and Name. The number of items to display should be limited to the sensors and actuators, which are installed in the station St21. [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.Sensors.
    	SensorsActuators.Base.SensorActuator ')">
    	<filters>
    		<columnfilter />	
    		<columnfilter filter="St21" />
    	</filters>
    	<column hSizeMax="20" heading="Circular Transfer System">
    		<label text="this.name"/>
    	</column>
    	<column hSizeMaxPx="50" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="150" heading="Name">
    		<label text="=x.name"/>
    	</column>
    </pureTable>

Table with limited number of rows: The following example shows a table, which has a limited number of rows with rowsMax="10". [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" rowsMax="10" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    	<column heading="No">
    		<label text="=mroot.rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator').indexOf(x)"/>
    	</column>
    	<column hSizeMaxPx="50" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="150" heading="Name">
    		<label text="=x.name"/>
    	</column>
    </pureTable>

Table with minimum number of rows: The following example shows a table, which has a minimum number if rows, predefined with rowsMin="10". [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" rowsMin="10" receiver="=mos('Pfuderer_ModularSystem.Mechatronic.Stations.Base.AbstractStation')">
    	<column heading="No">
    		<label text="=mos('Pfuderer_ModularSystem.Mechatronic.Stations.Base.AbstractStation').indexOf(x)"/>
    	</column>
    	<column hSizeMaxPx="50" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="150" heading="Name">
    		<label text="=x.name"/>
    	</column>
    </pureTable>

Double-clicking on a table row starts an action In the following table an action is started by double-clicking any row. [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" receiver="=mos">
    	<column hSize="20" heading="Name">
    		<command event="doubleclick" name="Documentation_UI_Configuration.ProjectLibrary.HelpObjects.okAction" arguments="List{x}" />
    		<label text="x.name" />
    	</column>
    </pureTable>

Table with fixed columns: The following example shows a table which representation is limited to a maximum of 5 rows and 7 columns. One of the 7 columns is fixed on the left-hand side and 2 columns are fixed on the right-hand side. The columns and rows in between are reached by means of scrollbars. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4,5,6,7,8,9}" variable="x" freezeLeft="1" freezeRight="2" columnsMax="7" rowsMax="5">
    	<column heading="Line">
    		<label text="x" />
    	</column> 	
    	<column heading="Column 1"> 
    		<label text="'Cell 1.'+ x" /> 
    	</column> 
    	<column heading="Column 2"> 
    		<label text="'Cell 2.'+ x" />
    	</column>
    	<column heading="Column 3"> 
    		<label text="'Cell 3.'+ x" /> 
    	</column> 
    	<column heading="Column 4">
    		<label text="'Cell 4.'+ x" />
    	</column> 
    	<column heading="Column 5">
    		<label text="'Cell 5.'+ x" />
    	</column> 
    	<column heading="Column 6">
    		<label text="'Cell 6.'+ x" />
    	</column> 
    	<column heading="Column 7">
    		<label text="'Cell 7.'+ x" />
    	</column> 
    	<column heading="Column 8">
    		<label text="'Cell 8.'+ x" />
    	</column> 
    	<column heading="Column 9">
    		<label text="'Cell 9.'+ x" />
    	</column> 
    	<column heading="Column 10">
    		<label text="'Cell 10.'+ x" /> 
    	</column>
    </pureTable>

Table with fixed height: The following example shows a table whose height is fixed at 150 pixels. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4}" variable="x" **height="150"** > 
    	<column heading="Col 1"> 
    		<label text="='Cell 1.'+ x">
    		</label> 
    	</column> 
    	<column heading="Col 2"> 
    		<label text="='Cell 2.'+ x">
    		</label> 
    	</column> 
    	<column heading="Col 3"> 
    		<label text="='Cell 3.'+ x">
    		</label> 
    	</column>
    </pureTable>

Result: Table with a dynamic height: The following example shows a table whose height matches that of the Form-UI. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4}" variable="x" **height="fillForm"** > 
    	<column heading="Col 1"> 
    		<label style="left" text="='Cell 1.'+ x">
    		</label> 
    	</column> <column heading="Col 2"> 
    		<label style="center" text="='Cell 2.'+ x">
    		</label> 
    	</column> 
    	<column heading="Col 3"> 
    		<label style="right" text="='Cell 3.'+ x">
    		</label> 
    	</column>
    </pureTable>

Result: Table with fixed width: The following example shows a table whose width is fixed at 350 pixels. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4}" variable="x" width**="350"** >
    	<column heading="Col 1"> <label style="left" text="='Cell 1.'+ x">
    		</label>
    	</column>
    	<column heading="Col 2">
    		<label style="center" text="='Cell 2.'+ x">
    		</label>
    	</column>
    	<column heading="Col 3">
    		<label style="right" text="='Cell 3.'+ x">
    		</label>
    	</column>
    </pureTable>

Result: Table with dynamic width: The following example shows a table, whose width matches that of the Form-UI. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4}" variable="x" width="fitToForm">
    	<column heading="Col 1">
    		<label style="left" text="='Cell 1.'+ x">
    		</label>
    	</column>
    	<column heading="Col 2">
    		<label style="center" text="='Cell 2.'+ x">
    		</label>
    	</column>
    	<column heading="Col 3">
    		<label style="right" text="='Cell 3.'+ x">
    		</label>
    	</column>
    </pureTable>

Result:
