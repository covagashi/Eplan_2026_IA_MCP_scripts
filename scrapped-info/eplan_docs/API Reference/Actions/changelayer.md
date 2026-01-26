# changelayer

**Source URL:** https://www.eplan.help/en-us/Infoportal/Content/api/2026/changelayer.html

---

```
Changes graphical layer properties.

```

| Parameter | Description |
| --- | --- |
| ``` PROJECTNAME
 ``` | ``` Project name with full path (optional).
 If not entered, the selected project is used when the action is called from GUI (like from a script or ribbon bar). 
 If called from the windows command line, the PROJECTNAME must be set or the ProjectAction must be used first (see also "ProjectAction"), otherwise an exception is thrown (see also "System.ArgumentException").
 ``` |
| ``` LAYER[n]
 ``` | ``` Name of layer. Parameter name may be followed by a number.
 ``` |
| ``` VISIBLE[n]
 ``` | ``` The layer is visible (optional). Parameter name may be followed by a number.
 ``` |
| ``` PRINTED[n]
 ``` | ``` The layer is printed (optional). Parameter name may be followed by a number.
 ``` |
| ``` TEXTHEIGHT[n]
 ``` | ``` Specifies text height of layer (optional). Parameter name may be followed by a number.
 ``` |
| ``` COLORID[n]
 ``` | ``` Specifies color index of layer (0-255) (optional). Parameter name may be followed by a number.
 ``` |
| ``` TRANSPARENCY[n]
 ``` | ``` Specifies transparency of 3D layer as double with a value between 0.0 and 1.0 (optional). Parameter name may be followed by a number.
 ``` |

**Remarks**

```
It is possible to change properties of more than one layer in a single action call. First it is necessary to add the /LAYER parameter followed by a number - /LAYER1:EPLAN100, then each parameter should be followed by the same number /VISIBLE1:1 /COLORID1:10 etc.

In this way we can add the next layers to change - /LAYER2:EPLAN110 /VISIBLE2:1 /COLORID2:55 (...) /LAYER15:EPLAN200 /TEXTHEIGHT15:3.75. Please look at the example.

```

**Example**

```
        changelayer /LAYER:EPLAN100 /VISIBLE:1 /PRINTED:1 /TEXTHEIGHT:2.75 /COLORID:1 

        changelayer /PROJECTNAME:C:\Projects\EPLAN\EPLAN_Sample_Project.elk /LAYER:EPLAN200 /VISIBLE:1 /PRINTED:0 /TEXTHEIGHT:5.5 /COLORID:15 

        changelayer /LAYER:560 /VISIBLE:1 /COLORID:9 /TRANSPARENCY:0.1

        changelayer /LAYER1:110 /VISIBLE1:1 /PRINTED1:1 /TEXTHEIGHT1:5 /COLORID1:1 /LAYER2:300 /VISIBLE2:1 /PRINTED2:1 /TEXTHEIGHT2:6 /COLORID2:11

```