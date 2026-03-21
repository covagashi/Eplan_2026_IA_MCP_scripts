---
title: "Connection points for actuators and sensors"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_modeling_sensors_actuators_terminals.htm"
file: "eecplc_k_modeling_sensors_actuators_terminals"
category: "eecplc"
---

# Connection points for actuators and sensors

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Connection points for actuators and sensors

Every sensor and actuator requires one or more connections. The various connections of the sensors and actuators are modeled by parameters. The properties of these parameters are defined by the parameter type (cf. the section on [Properties of connection points](concept_k_properties_of_connection_points.htm)). The PLC system library contains the requisite basic types for these definitions:

    1. IX for modeling binary inputs,
    2. IX for modeling binary outputs,
    3. IB for modeling inputs in byte format,
    4. QB for modeling outputs in byte format,
    5. IW for modeling inputs in word format,
    6. QW for modeling outputs in word format,
    7. ID for modeling inputs in double-word format,
    8. QD for modeling outputs in double-word format,

Customized types can be defined based on these basic types, for example, IX24V for a binary 24V input.

When executing an IO-generator action, the address of the connection to which the sensor or actuator is wired is registered as the parameter value (see the below diagram).
