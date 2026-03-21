---
title: "Processor"
source: "https://www.eplan.help/en-us/infoportal/content/eecpro/2026/Content/htm/eecplc_k_typical_hardware_components_processor.htm"
file: "eecplc_k_typical_hardware_components_processor"
category: "eecplc"
---

# Processor

This functionality is only available for certain module packages. [Info / Copyright](license.htm)

You are here: 

## Processor

In principle, a processor can only be represented with a single object, the controller. In practice, however, no processor works in isolation. It processes input signals and creates output signals. It is therefore essential that the input and output modules be logically connected to the processor.

In the simplest case, the processors have their own input and output connections. For this purpose, the communications channel of a controller can be directly connected with the channel of one or more terminals. However, most processors are capable of expansion and have ports that can be used to connect additional hardware components. Although this expansion is often accomplished via bus systems, it can also be carried out via the so-called backplane bus. In both cases, the controller is also connected with a coupler channel. If, for example, a process has a backplane bus, an interface for the programming device and a PROFIBUS connection, one controller and two couplers are employed.

The above example depicts a CPU assembly that provides three communication channels: a backplane bus, a DP PROFIBUS, and an MPI bus. The assembly is depicted with one controller and two couplers. The OutgoingBus parameter of the controller contains the same value as the IncomingBus parameter in both of the couplers. Furthermore, every object that uses the backplane bus as a communication channel (e.g. the IO assemblies that are built into the same rack) must contain this value in its IncomingBus parameter. However, the two couplers must have different values in their OutgoingBus parameters, and these must also differ from the value for the backplane bus.
