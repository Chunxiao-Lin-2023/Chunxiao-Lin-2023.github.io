---
title: "ML-based Handover Algorithm for Non-Terrestrial Networks in NS3"
collection: projects
#permalink: /project/2022_Paper2_ISQED
excerpt: 'In this project, I proposed a clustering-based handover algorithm for an LEO satellite network using the NS3 simulator.'
date: 2023-06-01
status: From 2023-06 to 2023-10
#venue: '2022 23rd International Symposium on Quality Electronic Design (ISQED)'
---


The motivation is: 
The user performance in LEO satellite network is limited by the fast-moving satellites. 
The speed of satellites is much faster than the users. This requires users to switch to new satellites more often than cellular networks.
Also, long distances introduce a long delay in RRC signaling, making handover prediction and management more important.

Project overview:
1. developed a clustering-based handover algorithm, and a target satellite selection algorithm.
2. Aiming to reduce the handover rate by grouping similar satellites.
3. To achieve better performance in the TX/RX bitrate, delay, and jitter.

Setup: 
1. ns3-based NTN system
2. 10 on-ground users and 93 on-satellite base stations.
