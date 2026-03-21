---
title: "Tutorial"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/tutorial_k_tutorial.htm"
file: "tutorial_k_tutorial"
category: "tutorial"
---

# Tutorial

This functionality is only available for certain module packages. [Info / Copyright](license.htm) You are here:  Tutorial The step-by-step development of a modular system will be used to demonstrate functional engineering. The resulting modular system is used to create a Feeder station, a demo assembly developed at the Esslingen University of Applied Sciences: This [film](../Pictures/TZ_ablauf.wmv) shows a cycle of the demo assembly in operation. The tutorial is structured so that each chapter can be completed on its own (see figure below). Once the example machine has been visualized, the next step is to create a mechatronic modular system (feeder). The modular system for the feeder can be expanded to include disciplines. These can be created separately from each other. The purpose of every discipline is to create files such as a list of components or a schematic diagram. Presentation of the example machine ([Example Feeder](tutorial_k_example_feeder.htm)):
     * The diagram of the example machine serves as the basis for the [Functional assembly](tutorial_k_example_feeder_functional_structure.htm).
     * The functional assembly is used to create the abstract [Modular system](tutorial_k_example_feeder_modular_system.htm).
     * Next, the resulting architecture model is visualized ([Architecture model](tutorial_k_example_feeder_architecture.htm)).
Once the example machine has been visualized, the development of the [Mechatronic](tutmechatronic_h_mechatronic.htm) is described as follows:
     * In the first step, the basic architecture is defined ([Create mechatronic architecture model](tutmechatronic_h_create_mechatronic_architecture.htm)).
     * Building on this, the components required for the feeder are specified ([Design mechatronic modular system](tutmechatronic_h_develop_mechatronic_modular_system.htm)).
     * This then serves as the basis for configuring the feeder mechatronically ([Configuration](tutmechatronic_h_projects.htm)).
     * The [Generation of variants via disabler](tutmechatronic_h_create_variants_per_disabler.htm) and the [Generation of variants via parameterization](tutmechatronic_h_create_variant_per_parameterization.htm) are explained in separate sections.
A list of actuator and sensor components is used as an example to demonstrate how it is possible to create a text file from the mechatronic model using the [Text discipline](tuttext_h_text.htm):
     * The ListOfComponents is to be seen as the created results of a new discipline (see [Task: Generate a ListOfComponents](tuttext_h_task_generate_loc.htm)).
     * The ListOfComponents discipline is then added to the existing mechatronic model for the feeder ([Adding the ListsofComponents discipline to the mechatronic model](tuttext_h_extend_mechatronic_with_loc_discipline.htm)).
     * How it possible to use the plug-socket concept to generate a ListOfComponents that differs in structure from the functional layer is demonstrated in the section [Mechatronic model: Generating non-functional structures](tuttext_h_generate_nonfunctional_structure.htm) shown.
The ECAD discipline shows how a schematic for [Eplan Electric P8](tutp8_h_eplan_electric_p8.htm) can be created on the basis of the mechatronic model.
     * The first step is to [Create EPLAN Electric P8 components](tutp8_h_create_p8_components.htm) for this discipline.
     * The Eplan Electric P8 discipline is then added to the existing mechatronic model for the feeder ([Adding the schematic discipline to the mechatronic model](tutp8_h_extent_mechatronic_with_schematics_discipline.htm)).
     * The test at the end of the chapter [Use formulas for plugs, sockets, and PLC inputs](tutp8_h_assign_formulas_to_plugs_sockets_plc_inputs.htm) shows how to create a schematic that is aligned to the installed components on the basis of the plug-socket concept.
The Pro Panel discipline shows how a schematic for [Eplan Pro Panel](tutpropanel_h_propanel.htm) can be created on the basis of the mechatronic model.
     * The first step is to create discipline components for this discipline ([Creating EPLAN Pro Panel discipline components](tutpropanel_h_create_propanel_discipline_components.htm)).
     * The Eplan Pro Panel discipline is then added to the existing mechatronic model for the feeder ([Expanding the mechatronic model with Eplan Pro Panel components](tutpropanel_h_extend_mechatronc_with_propanel_components.htm)).
     * [Generating the finished state of the enclosure](tutpropanel_h_test2_generate_current_enclosure.htm) shows how an enclosure that is adapted to the installed components can be created with the aid of the disabler concept.
The PLC discipline is used to show how to create a program for [SIMATIC STEP 7](tutstep7_h_step7.htm) on the mechatronic model. This discipline is divided into four sections:
     * The first section shows how a STEP 7 program is to be created for the Feeder example machine ([Creating a STEP 7 program for Feeder](tutstep7_h_task1_generate_code.htm)).
     * In the second section addresses for the inputs and outputs are assigned ([Task 2 - Allocating addresses for the inputs and outputs](tutstep7_h_task2_assign_ioaddresses.htm)).
     * The third section shows how a symbol table is created ([Task 3 - Creating the symbol table](tutstep7_h_task3_generate_symboltable.htm)).
     * The last section shows how interrupt messages are inserted into the STEP 7 program ([Task 4 - Inserting fault messages into the STEP 7 code](tutstep7_h_task4_insert_error_messages.htm)).
The Office discipline shows how to create a list of actuators and sensors in table form as a Word file on the basis of the mechatronic model:
     * Word components are created first for this discipline ([Creating Word components](tutword_h_create_word_components.htm)).
     * The Word ListOfComponents is then added to the existing mechatronic model for the feeder ([Adding ListofComponents to the mechatronic model](tutword_h_extent_mechatronic_by_loc.htm)).
     * How it possible to use the plug-socket concept to generate a ListOfComponents that differs in structure from the functional layer is demonstrated in the section [Generating non-functional structures](tutword_h_generate_nonfunctional_structure.htm) shown.
The GRAPH2D discipline does not reference the model of the example machine; for this reason, it has its own separate mechatronic model. The discipline shows to configure the office infrastructure with the help of the graphical diagram.
     * A diagram configuration is created from the ground up ([Create new diagram configuration](tutgraph2d_h_create_diagram_configuration.htm)).
     * Container objects (floor, room) are defined as polygons and linked with Form-UIs to enable data to be entered ([Expanding the configuration with nodes for floor and room](tutgraph2d_h_extend_configuration_by_floor_and_room_nodes.htm) and [Configuring tooltips for displaying Form-UIs](tutgraph2d_h_configuration_of_tooltips_for_formuis.htm)).
     * Devices and persons can be added as images to rooms. These can be linked using connections. Data can be added to these objects by way of Form-UI calls ([Configuring connections](tutgraph2d_h_connections_configuration.htm)).
     * The devices receive slave objects with which they can be tagged and through which they can be linked in order to map an IT landscape ([Configuring slave nodes as labels](tutgraph2d_h_configuration_of_slave_nodes_as_label.htm)).
     * Container objects, devices, persons, and connections are assembled in a tool palette ([Configuring palette entries](tutgraph2d_h_configuration_of_palette_entries.htm)).
     * Commands allow the creation of nodes from the project tree and the instantiation of new nodes and edges from the tool palette ([Commands for inserting room components (RoomComponent) from the project tree](tutgraph2d_h_commands_to_insert_roomcomponents_from_projecttree.htm) and [Test 7 - Insertion of nodes and connections from the palette](tutgraph2d_h_test7_insert_nodes_connections_from_palette.htm)).
The project generation via import shows how a complete configuration of the Feeder station is created on the basis of the mechatronics modular system via import wizard.
     * The import of IMX and XML files is used to show how a configuration is created.
     * it is shown how individual components are installed in the configuration on placeholders through the import of IMX and XML files.
     * The import of an IMX file is used to show how components are placed on placeholders and extension points.
     * In the completed configuration parameter values are et through the import of CSV files. This is shown with individual parameters of different types, but also with a parameter of the Map type that is filled with key-value pairs.
     * A further scenario shows how the imports are triggered by means of actions in a configuration UI, instead of via the import wizard.
The application of the Job Server shows how a configuration of the Feeder station is created on the basis of the mechatronical modular system by the Job Server or, respectively, by the Worker registered at it.
     * A Job definition is created in order to create a configuration via fileTrigger.
     * It is shown how the Job definition is extended in order to store the created configuration in a specific local folder.
     * The next step shows how the IMX file to be imported is changed in order to place components on placeholders and extension points.
     * A further scenario shows how a Job is started from the browser in order to create a configuration of the Feeder station.
     * The last section shows how key-value pairs are transferred to the URL by means of POST Job parameters in order to store these in a parameter in the configuration.
