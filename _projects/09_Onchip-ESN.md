---
title: "FPGA-based ESN with on-chip RLS Learning for Channel Prediction"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'This paper proposed a bit-serial-based matrix multiplication for the reservoir neuron design in Echo State Network.'
date: 2023-08-02
status: From 2023-08 to 2023-12
#venue: '2022 23rd International Symposium on Quality Electronic Design (ISQED)'
---


In the latest project, I proposed a FPGA-based online recursive least square learning algorithm, and a systolic-array-based vector-matrix multiplier.
The motivation is to achieve the on-chip learning instead of the previous offline learning for ESN. And explore the ESN-based method for MIMO channel prediction.
More details:
1.	Systolic array is the key component of the Google TPU, the advantage of it is to achieve high parallelism and resource sharing, and break the limitation of IO ports.
2.	There are multiple configurations of the systolic array, weight-stationary and output-stationary. 
3.	In our case, the weight matrix is pretty large, and the number of MAC operation is also large, and the reuse of weights is not that frequent, therefore I choose to use the output-stationary configuration.
4.	In our channel prediction task, where the number of inputs is much larger than the number of states, the computational efficiency can be estimated to 
one MAC operation/DSP/Cycle.
With the systolic-array-based vector-matrix multiplier, and the previous DSP-array-based vector multiplier, I then built a pipelined design for the online RLS learning method.

