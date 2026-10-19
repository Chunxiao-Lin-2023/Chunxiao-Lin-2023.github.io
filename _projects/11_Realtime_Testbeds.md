---
title: "Real-Time PC-FPGA Testbeds for DMIMO Channel Prediction"
collection: projects
excerpt: 'Two PC-FPGA testbeds that run a 2-mode windowed ESN live in a distributed MIMO channel-prediction loop.'
date: 2024-09-01
status: From 2024-09 to 2026-10
---

In this project, I put the FPGA ESN accelerators into a live loop with a distributed MIMO (DMIMO) testbed: a 4-antenna gNB serves two 2-antenna UEs through a PROPSIM F16 channel emulator, and the FPGA retrains and predicts the CSI of each UE at every frame.
More details:
1.	1 GbE PS-PL hybrid testbed (ZCU216): lwIP UDP/IP on the ARM processor, the ESN/WESN accelerator in the programmable logic; under 2 ms end to end, used to bring up every new model.
2.	10 GbE PL-based testbed (VC709): Ethernet MAC + PHY and two WESN channels in pure RTL, one 10 GbE link per UE; at most 900 us end to end, 1250 CSI frames/s per UE, 3.42 W.
3.	Live prediction lowers the NMSE from 0.0119 (outdated CSI) to 0.0087.

![](/images/projects/testbed_10g.jpg)
