---
title: "columnFilter"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/refformui_r_columnfilter.htm"
file: "refformui_r_columnfilter"
category: "refformui"
---

# columnFilter

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  columnFilter The <columnFilter> element configures one filter per table column within <pureTable>. The attribute filter determines the values to be filtered. Attribute name | Usage | Attribute values | Default value | Description  
---|---|---|---|---  
caseSensitive | optional | true, false | true | Controls consideration of case sensitivity for filtering  
true = case-sensitive filtering is considered  
false = case-sensitive filtering is not considered  
filter | required for type="text" |  |  | Defines the filter text: The wildcards * and ? can be used in the usual manner. The < filters strings which reach up to this character.  
type | optional | text  
combo | text | text = creates underneath the header row a filter for free text.  
combo = creates, underneath the header row, a filter as a drop-down list box, which contains all the values of the respective column.  
style | optional | default, multi | default | Shows the possible filter values in a drop-down list box.  
default = shows the possible filter values in a drop-down list box  
multi = shows the possible filter values in a drop-down list box with check boxes  
Allowed sub-elements | Quantity  
---|---  
none |   
Table with filter whose values are selected in a drop-down list box: The following example shows a table, which lists the name of the circular transfer system and, of its components of type 'Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator', the parameters Place and Name. The number of displayed items is limited by selection of filters in drop-down list boxes. [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    	<filters>
    		<columnFilter type="combo"/>
    		<columnFilter type="combo"/>
    		<columnFilter type="combo"/>
    	</filters>
    	<column heading="No">
    		<label text="=mroot.rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator').indexOf(x)"/>
    	</column>
    	<column hSizeMaxPx="50" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="150" heading="Name">
    		<label text="x.name">
    			<link receiver="x" ref="IOs"/>
    		</label>
    	</column>
    </pureTable>

Table with filter values in a drop-down list box which are selectable by check boxes: The following example shows a table, which lists the name of the circular transfer system and, of its components of type 'Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator', the parameters Place and Name. The number of displayed items is limited by selection of filters in drop-down list boxes with check boxes. [Example code](javascript:void\(0\);)
    
        <pureTable variable="x" receiver="=rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator')">
    	<filters>
    		<columnFilter type="combo"/>
    		<columnFilter type="combo" />
    		<columnFilter type="combo"/>
    	</filters>
    	<column heading="No">
    		<label text="=mroot.rmos('Pfuderer_ModularSystem.Mechatronic.SensorsActuators.Base.SensorActuator').indexOf(x)"/>
    	</column>
    	<column hSizeMinPx="110" heading="Place">
    		<label text="=x.$Place"/>
    	</column>
    	<column hSizeMinPx="300" heading="Name">
    		<label text="x.name">
    			<link receiver="x" ref="IOs"/>
    		</label>
    	</column>
    </pureTable>

Filter searches strings with limited length The following tables show how the sign < in a filter definition for pureTable is configured, in order to filter strings which only reach until to a specific character. The following figure shows the unfiltered results on the left side and the filtered results on the right side. Filter searches strings considering case sensitivity The following table shows how considering the case-sensitivity influences the number of filtered values. [Example code](javascript:void\(0\);)
    
        <table columns="2">
    	<td>
    		<label>caseSensitive="false"</label>
    	</td>
    	<td>
    		<label>caseSensitive="true"</label>
    	</td>
    	<td>
    		<pureTable receiver="=mos">
    			<filters>
    				<columnFilter type="text" caseSensitive="false" />
    			</filters>
    			<column heading="Name">  
     				<label text="this.name" />
    			</column>
    		</pureTable>
    	</td>
    	<td>
    		<pureTable receiver="=mos">
    			<filters>
    				<columnFilter type="text" caseSensitive="true" />
    			</filters>
    			<column heading="Name">
    				<label text="this.name" />
    			</column>
    		</pureTable>
    	</td>
    </table>

Text in header is broken with \n at any point The following tables show how the text in a header is broken by \n. [Example code](javascript:void\(0\);)
    
        <pureTable receiver="=List{1,2,3,4,5,6,7,8,9}" variable="x">
    	<column heading="Heading Line 1\nHeading Line 2\nHeading Line 3" hSizeMaxPx="150">
    		<label text="'Cell '+x"></label>
    	</column>
    </pureTable>
