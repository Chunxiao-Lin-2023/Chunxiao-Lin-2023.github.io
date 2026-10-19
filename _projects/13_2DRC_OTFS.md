---
title: "2D Reservoir Computing for OTFS Detection on FPGA"
collection: projects
excerpt: 'Ongoing: a complex-valued FPGA datapath for 2D reservoir computing (2D-RC) OTFS symbol detection.'
date: 2026-06-01
status: From 2026-06, ongoing
---

OTFS detects symbols on the delay-Doppler grid, and the 2D-RC model lets the reservoir state recur in two dimensions. All signals and weights are complex-valued, and a real/imaginary split would double the work.
Research direction:
1.	Complex-valued multiplication units.
2.	A complex-valued neural network datapath end to end, with a 2D window front end.
