---
title: "Reference between devices among one another"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_connections_configuration_devices.htm"
file: "tutgraph2d_h_connections_configuration_devices"
category: "tutgraph2d"
---

# Reference between devices among one another

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Reference between devices among one another Only a slave node  of one device may be connected to another slave node of another device at any time. The connected slave node is saved in the parameter Connection of the respective connected slave node.
    1. Below the node with id=âWorker_Referenceâ, insert the following lines.
    
        <!-- Relation of Slave to Slave -->
    <reference id="LAN_Reference"
    	type="connectable"
    	src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')"
    	target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')">
    	<forward multiplicity="1" connector="=getParameter('Connection')" />
    	<backward multiplicity="1" connector="=getParameter('Connection')" />
    </reference>

[Explanation](javascript:void\(0\);) The ID of the second relationship is LAN_Reference, which is still referenced in the configuration of the connection of slave node to slave node. The formula in the attribute src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" determines the types of components that are permissible as the source of a connection. The formula in the attribute target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" determines the types of components that are permissible as the source of a connection. The tag <reference> encloses the tags <forward> and <backward> with whose attribute multiplicity it is determined that 1:1 connections are being referenced. In addition, the attribute connector="=getParameter('Connection')" lays down that the source and target components are stored in the parameter Connection.
