---
title: "Hybrid DSP-CLB Reservoir Neuron for High-Speed MIMO Channel Prediction"
collection: projects
excerpt: 'A hybrid DSP-CLB neuron (MAC_DA) and a range-addressable tanh for high-speed ESN inference (ICNC 2026).'
date: 2024-06-01
status: From 2024-06 to 2025-08, published in ICNC 2026
---

In this project, I balanced the DSP and CLB resources inside each reservoir neuron.
The CLB-only neuron (ISQED 2022) uses no DSPs but is slow, and the DSP-only neuron (ICCAD 2023) leaves DSPs idle while the cascaded slices wait on each other.
More details:
1.	MAC_DA: nine DSP slices multiply-accumulate, and a CLB-based fast adder tree compresses their partial sums, so the DSPs never sit idle.
2.	On a 72x72 matrix-vector multiplication: +25% DSP efficiency and 13% less processing time than the DSP-only MAC.
3.	Range-addressable LUT (RALUT) tanh: linear interpolation where tanh bends, the LUT intercept in the near-saturation range, and +-1 in saturation; the DSP is clock-gated above the threshold and the table BRAM drops by 25%.
4.	A full ESN (64, 8, 64) predicts in 0.97 us (65.98 MS/s) and beats the AR predictor by 5.7-14.2 dB in NMSE.
