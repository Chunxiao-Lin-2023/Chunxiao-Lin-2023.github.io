---
title: "Optimized Reservoir Node Architecture for FPGA-based RC Systems"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'This paper proposed a bit-serial-based matrix multiplication for the reservoir neuron design in Echo State Network.'
date: 2021-10-01
status: From 2021-10 to 2022-02
#venue: '2022 23rd International Symposium on Quality Electronic Design (ISQED)'
---



In the first project, I proposed a low-cost design for the reservoir neuron of the ESN.
The motivation is to exploit the properties of the ESN weight matrix. The input and reservoir weight matrices are fixed and sparse, which means there are a large number of zero elements and other values are known and unchanged.
I adopted the bit-serial matrix multiplier and direct spatial implementation of the weight matrix. The canonical signed digit representation is also employed to further optimize the multiplier logic.
More details:
1.	Bit-serial multiplier can achieve a lower resource utilization at the cost of the latency. However, by adopting optimization principles at bit level, we can highly reduce the logic for multiplication with zero values, and even zero bits within a number.
2.	For example, in a multi-bit by single-bit multiplication, we can just use an AND gate for mult and a shift register for multi-bit value. Since the single-bit operand is known, we can just remove all the logic if it’s 0, or just remove the AND gate if it’s 1.
3.	The adoption of canonical signed digit representation is to reduce the count of non-zero bits, which can further enhance the proposed bit-serial multiplier. 




<!-- ![](/images/projects/foo-bar-identity.jpg) -->
