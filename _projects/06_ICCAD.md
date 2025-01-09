---
title: "FPGA-based ML Model Design for MIMO-OFDM Symbol Detection"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'This paper proposed a bit-serial-based matrix multiplication for the reservoir neuron design in Echo State Network.'
date: 2022-06-01
status: From 2022-06 to 2022-11
#venue: '2022 23rd International Symposium on Quality Electronic Design (ISQED)'
---


In this project, I proposed a DSP-based vector multiplier for the MAC operations in ESN. The motivation is to exploit the utilization of the DSP48E1 slides in the Xilinx Vertex-7 FPGA and reduce the utilization of the CLB. (100MHz)
More details:
1.	For the DSP48E1 slide, with different configurations, it can perform multiple operations, such as MAC, three-input addition, and up to 64 options.
2.	We build a 3x3 DSP array for vector multiplication, with a 3-stage design. In the first stage, all the 9 DSPs will perform the MAC operation, until all the inputs are processed. Then in the second stage, 9 DSPs will be divided into 3 groups, in each group, one of the DSP will be used to accumulate the SoPs, therefore, totally 3 partial SoPs will be generated. In the third stage, the 3 partial SoPs will be further accumulated into the final SoP.
3.	Actually this is not a fully optimized design, the DSP utilization rate is around 70% in our case, while with the scale increases, the utilization rate can grow up.
4.	There are some potential methods I am looking into, like using the add tree for accumulation. Which may only increase power.

We also built an SDR/FPGA testbed for the 2x2 MIMO-OFDM symbol detection task.
More details:
1.	The testbed consists of a linux PC, a Virtex-7 FPGA, and 2 USRPs.
2.	The USRPs serve as the RF transceivers.
3.	The WiFi radio system is implemented in the GNU Radio software, which generates the transmitted signals. The signals are sent to the Receiver through the real-world wireless channel. 
4.	The receiver will send the distorted signal back to the PC, and then keep sending the data to the FPGA-based symbol detector for signal recovery. This is done with the ethernet cable, which allows 1000 Mbit/s transmission in maximum.
5.	The recovered signal from FPGA will be used for the BER calculation on PC.



