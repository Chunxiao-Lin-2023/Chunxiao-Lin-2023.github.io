---
title: "2-Mode WESN for Large-Scale DMIMO Channel Prediction on One FPGA"
collection: projects
excerpt: 'Ongoing: scaling real-time channel prediction from 4x2 to 8x2 DMIMO on a single FPGA with a 2-mode windowed ESN.'
date: 2026-03-01
status: From 2026-03, ongoing
---

A flattened WESN already takes more than half of the FPGA at 4x2 DMIMO. The 2-mode WESN keeps the CSI as a matrix and needs far fewer weights.
Research direction:
1.	A systolic-array-based triple matrix multiplication for W1 U W2.
2.	Reuse of the DSP_SA readout and the on-chip learner.
3.	A fixed per-frame latency at 8x2.
