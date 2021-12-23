# Final-Year-Project
<p align="justify">
Modeling of Metastatic Cancer and its Treatment using Swarm Intelligence Based-Control. This study investigates the use of swarm robotics and nanotechnology to target cancer cells autonomously and efficiently, focusing on exploring new control algorithms inspired by the combined behaviour of social animals.
</p>

<p align="justify">
Metastatic cancer is defined as cancer growth in a primary site before spreading to other parts of the body via the blood or lymph system arising from the mutation of crucial genes in a set of healthy cells and develops into a solid tumour due to abnormally rapid proliferation.
</p>

**Cellular Automata Based Model of Cancer Growth**
<p align="justify">
A two-dimensional grid of square cells is generated with n×n rows and columns depending on the desired pixel density, parameters and space of the simulation. The grid size and the number of initial cancer cell randomly located in the initial grid at t0 are first entered independently before assigning blood cells, defining the tissue’s environment. The cellular grid is composed of a large matrix of numbers, where each number defines a specific cell type and colour.
</p>

<p align="center">
<img width="552" alt="Screen Shot 2021-12-23 at 9 32 22 AM" src="https://user-images.githubusercontent.com/70657426/147204880-e9931700-7517-49c8-84de-0e8023ba26ed.png">
</p>

<p align="justify">
It is primordial to ensure that the computational model is valid and similar to real-life tumour growth in any typical cancer patient. The dataset provided is secured from a Chinese hamster V79 fibroblast tumour cell line consisting of forty-five volume measurements through a period of 60 days. The tumour volume was plotted against time, and a linear regression curve elevated to the fourth polynomial degree was fitted through the scatter plot below.
</p>

<p align="center">
<img width="500"  alt="Figure_1" src="https://user-images.githubusercontent.com/70657426/147205113-58371bf9-e5e9-4f7e-9365-8fed30bf0bba.png">
</p>

A new algorithm was designed using EoN (Epidemics on Networks), a Python library for analytic estimation adapted from Miller and Ting, 2019, to obtain a representative plot of our simulation Figure 6. By comparing both figures, we can see that the trend is similar and almost identical.

<p align="center">
  
![Figure_3](https://user-images.githubusercontent.com/70657426/147205410-2db0d17c-9b0b-4d2a-a2f9-f5fba7cb6ec2.png)
</p>

**Cellular Automata Based Model of Nanorobots**
<p align="justify">
Once the tumour growth is achieved, the second stage of our experiment introducing a swarm of nanorobots is set. We assume that one cancerous cell starts its apoptosis if and only if one nanobot have trespassed the cell. When moving in the x-direction, the nanorobots are capable of healing both lower and adjacent upper cells at the next iteration. When progressing vertically, the particles are able to target the horizontally located cells. The grid’s dimensions are fixed by boundaries conditions, halting further displacement of the nanoparticle along these lines. The nanorobots can only move to one of their four neighbours, i.e. either to the x or y-direction of the grid. Each nanorobot can only move to a single square per iteration/second. Finally, as we are using precise targeting treatment, we assume that when one cancerous cell is destroyed, another normal cell replaces it in the simulation.
</p>

<p align="center">
  
<img width="563" alt="Screen Shot 2021-12-23 at 9 40 44 AM" src="https://user-images.githubusercontent.com/70657426/147205743-cdf8b8ed-b02b-4c4b-954a-81445e30b108.png">
</p>










  
  
  
  
