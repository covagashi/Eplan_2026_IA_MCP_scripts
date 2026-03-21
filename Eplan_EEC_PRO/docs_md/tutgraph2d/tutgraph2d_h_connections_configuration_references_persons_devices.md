---
title: "Referencing between persons and devices"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutgraph2d_h_connections_configuration_references_persons_devices.htm"
file: "tutgraph2d_h_connections_configuration_references_persons_devices"
category: "tutgraph2d"
---

# Referencing between persons and devices

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Referencing between persons and devices In the diagram, it should be possible to connect **one person** with **several devices** , for example, with PC and telephone. The relevant connected project component should be stored in the parameter WorkerConnection.
    1. Below the node with id=âMasterâ, insert the following lines.
    
        <!-- Connections -->
    <!-- Relation of Worker to Device -->
    <reference id="Worker_Reference"
    	type="connectable"
    	src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.SinglewayComponent')"
    	target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.SinglewayComponent')">
    	<forward multiplicity="1" connector="=getParameter('WorkerConnection')" />
    	<backward multiplicity="*" connector="=getParameter('WorkerConnection')" />
    </reference>

[Explanation](javascript:void\(0\);) The ID of the first relationship is Worker_Reference, which is still referenced in the configuration of the connection of person to device. The attribute type="connectable" is used when the connections are not pre-specified by a specific model structure but are interactively created in the diagram. The formula in the attribute src="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.SinglewayCompontent')" determines the type of components, which are permitted as a source of a connection. The formula in the attribute target="=isInstanceEO() and isInstanceOf('IT_ModularSystem.Basic.LAN_Jack')" determines the types of components that are permissible as the target of a connection. The tag <reference> encloses the tags <forward> and <backward> with whose attribute multiplicity it is determined that 1:N connections are being referenced. In addition, the attribute connector=â=getParameter(âWorkerConnection')" lays down that the source and target components are stored in the parameter WorkerConnection.
