---
title: "FPGA-based Reservoir Computing with On-chip Learning for MIMO Channel Prediction"
collection: publications
category: manuscripts
permalink: /publication/2026_Paper9_TCAD
excerpt: '<span style="color: blue;">Author List: Chunxiao Lin, Ummay Sumaya Khan, Meiyu Zheng, Muhammad Farhan Azmine, Lingjia Liu, Daniel J. Jakubisin, Yang Yi</span><br>
          This paper presents a complete on-chip ESN system on FPGA, with inference and recursive least squares (RLS) training on the same chip, for high-dimensional MIMO channel prediction. One training step takes 3.87 us, with 5.3x lower NMSE than the prior on-chip learner and over 1600x / 290x the energy efficiency of CPU / GPU implementations.<br>
          <b>My contributions in this work are:</b><br>
          (1) Designed a divider-free, three-stage pipelined RLS learner whose update time grows linearly with the state size.<br>
          (2) Proposed a systolic-array-based matrix-vector multiplier (DSP_SA) for the output layer, reused by the RLS learner.<br>
          (3) Integrated inference and training into a unified real-time ESN system with a Q-format fixed-point design.<br>
          (4) Applied the on-chip ESN system to MIMO channel prediction, outperforming AR, MLP, CNN and GRU baselines.
          '
date: 2026-01-15
status: Published
venue: 'IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD)'
paperurl: 'https://doi.org/10.1109/TCAD.2026.3715776'
---
