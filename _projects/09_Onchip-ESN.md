---
title: "FPGA-based ESN with on-chip RLS Learning for Channel Prediction"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'FPGA-based ESN with on-chip RLS learning for MIMO channel prediction (IEEE TCAD 2026).'
date: 2023-08-02
status: From 2023-08 to 2026-01, published in IEEE TCAD 2026
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

Results (IEEE TCAD 2026):
1.	Inference and RLS training share the same DSP arrays; one training + prediction step takes 3.87 us on a Virtex-7 at 100 MHz.
2.	The three-stage pipelined RLS update takes 2L+4 cycles: the work is O(L^2), but the time grows only linearly with the state size L.
3.	5.3x lower NMSE than the prior on-chip ESN learner, and 264 Mb/s on 64-dimensional data.
4.	Over 1600x and 290x the energy efficiency of the same ESN + RLS on a CPU and a GPU.
