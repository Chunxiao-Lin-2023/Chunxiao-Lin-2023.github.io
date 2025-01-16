---
title: "Low Power 10T-SRAM Design for In-Memory Computing with Leakage Current Reduction"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'This paper proposed a bit-serial-based matrix multiplication for the reservoir neuron design in Echo State Network.'
date: 2020-10-01
status: From 2020-10 to 2020-12
#venue: '2022 23rd International Symposium on Quality Electronic Design (ISQED)'
---


The 10T-SRAM is an extension of the 8T-SRAM for in-memory computing.
Compared with the 6T-SRAM, 8T-SRAM has two extra transistors for independent read operation, which can read the SRAM value Q or QB into a Read BitLine.
Therefore, with two more transistors than 8T-SRAM, the 10T-SRAM can read the Q and QB to two RBLs simultaneously for different in-memory computing.

Details of the in-memory computing:
If two SRAMs share one RBL, and the two values in the SRAMs are A and B, the voltage level of the RBL can be 00, 01, 10, and 11.
By adding two inverters to the output of the RBL, and control the trip point of them, we can make the output logic to be NOR or NAND.

![](/images/projects/8T-SRAM_in-memory_computing.png)
