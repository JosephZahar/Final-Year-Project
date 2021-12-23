# Final-Year-Project
<p align="justify">
Modeling of Metastatic Cancer and its Treatment using Swarm Intelligence Based-Control. This study investigates the use of swarm robotics and nanotechnology to target cancer cells autonomously and efficiently, focusing on exploring new control algorithms inspired by the combined behaviour of social animals.
</p>

<p align="justify">
Metastatic cancer is defined as cancer growth in a primary site before spreading to other parts of the body via the blood or lymph system arising from the mutation of crucial genes in a set of healthy cells and develops into a solid tumour due to abnormally rapid proliferation.
</p>

## Cellular Automata Based Model of Cancer Growth
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

## Cellular Automata Based Model of Nanorobots
<p align="justify">
Once the tumour growth is achieved, the second stage of our experiment introducing a swarm of nanorobots is set. We assume that one cancerous cell starts its apoptosis if and only if one nanobot have trespassed the cell. When moving in the x-direction, the nanorobots are capable of healing both lower and adjacent upper cells at the next iteration. When progressing vertically, the particles are able to target the horizontally located cells. The grid’s dimensions are fixed by boundaries conditions, halting further displacement of the nanoparticle along these lines. The nanorobots can only move to one of their four neighbours, i.e. either to the x or y-direction of the grid. Each nanorobot can only move to a single square per iteration/second. Finally, as we are using precise targeting treatment, we assume that when one cancerous cell is destroyed, another normal cell replaces it in the simulation.
</p>

<p align="center"> 
<img width="563" alt="Screen Shot 2021-12-23 at 9 40 44 AM" src="https://user-images.githubusercontent.com/70657426/147205743-cdf8b8ed-b02b-4c4b-954a-81445e30b108.png">
</p>

## Multi-Agent based model of Nanorobots
<p align="justify">
The development environment in question is Netlogo, primarily written in Scala with some part in Java. The program allows different use of mobile agents known as turtles that circulate over a stationary cellular grid referred to as patches, equivalent to our cellular automata domain. This part focuses on developing a specialised control algorithm for our swarm of nanorobots inspired by swarm intelligence behaviour.
</p>

<p align="center">
<img width="598" alt="Screen Shot 2021-12-23 at 9 45 53 AM" src="https://user-images.githubusercontent.com/70657426/147206303-a84e1044-3474-4465-8dab-c2c4204fa021.png">
</p>

### Random Motion Algorithm
<p align="justify">
The random motion algorithm refers to the arbitrary movement of nanoparticles without involving any connection between the agents, i.e. each agent cannot sense the other members of the swarm and vary their direction accordingly.
</p>
<p align="center">
<img width="690" alt="Screen Shot 2021-12-23 at 9 48 40 AM" src="https://user-images.githubusercontent.com/70657426/147206633-28ea91fb-6e93-4797-acde-4fbe575778cc.png">
</p>

### Flock Motion Algorithm
<p align="justify">
The flock motion algorithm aims to copy the group migration of birds generally adopted for safety from predation and foraging benefits. Here, the nanorobots move in a flock shape by sensing the other swarm members present in their radius and alternating their direction suitably.
</p>
<p align="center">
<img width="690" alt="Screen Shot 2021-12-23 at 9 48 28 AM" src="https://user-images.githubusercontent.com/70657426/147206576-b168d517-8319-4233-8c89-20d178dd6364.png">
</p>

### Search Dominated Motion Algorithm
<p align="justify">
The search dominated algorithm is very similar to the flock motion of the nanoparticle in terms of programming; however, another piece of code is implemented to target the cancer cells. In addition to the ability of the nanorobots to sense their neighbours over a defined radius, the capabilities of the agents to detect cancerous cells was implemented.
</p> 
<p align="center">
<img width="690" alt="Screen Shot 2021-12-23 at 9 49 40 AM" src="https://user-images.githubusercontent.com/70657426/147206761-42bc7428-2d47-46d2-8b21-9832f1da3a7b.png">
</p> 

### Flock Dominated Motion Algorithm
<p align="justify">
This final algorithm is almost identical to the cancer targeting code, and the only con- trast remains in the distribution of the nanoparticles tasks. In fact, instead of starting by targeting cancer cells, the flock dominated algorithm first sight to form a connected flock before searching for cancer cells.
</p> 
<p align="center">
<img width="690" alt="Screen Shot 2021-12-23 at 9 50 33 AM" src="https://user-images.githubusercontent.com/70657426/147206869-93fe5a5a-4a8c-4980-b3f3-f6ed53caf175.png">
</p> 

## Variables Investigation

### 50 Nanobots
<p align="center">
<img width="924" alt="Screen Shot 2021-12-23 at 9 56 39 AM" src="https://user-images.githubusercontent.com/70657426/147207624-a56480c5-08ce-4814-8b75-a5b0f86fde81.png">
</p> 
<p align="justify">
The figure above shows the investigation of the variables for a swarm population of 50 nanorobots where figure d) combine the most efficient variable of each algorithm into one plot to allow further analysis.
</p> 

### 100 Nanobots
<p align="center">
<img width="816" alt="Screen Shot 2021-12-23 at 9 58 11 AM" src="https://user-images.githubusercontent.com/70657426/147207810-2cdec147-3c68-4060-90cd-db6bb2853de9.png">
</p> 
<p align="justify">
The figure above investigate the change of variable for a population of 100 agents. Here, the flock motion simulation displays a specific cancer treatment with extensive stagnation phases and steep slopes. This trend reveals the swarm’s effectiveness to treat the disease when in contact with a tumour, yet their struggle at finding the targeted cells.
</p> 

### 150 Nanobots
<p align="center">
<img width="816" alt="Screen Shot 2021-12-23 at 9 59 02 AM" src="https://user-images.githubusercontent.com/70657426/147207914-7edfd8fb-629d-40e0-9d9d-011f717ed551.png">
</p> 
<p align="justify">
For 150 nanorobots in figure 18, the flock motion algorithm shows a decrease in plateau and sharper slopes. The best outcome is obtained for the lowest variables values and the worst results for both high variables.
</p> 

### 200 Nanobots
<p align="center">
<img width="816" alt="Screen Shot 2021-12-23 at 10 00 10 AM" src="https://user-images.githubusercontent.com/70657426/147208046-cf659f0f-764b-4525-9c8f-c0b23b65b423.png">
</p> 


## Further Applications for our algorithms
### Floor Decontamination
<p align="justify">
The potential applications of swarm robotics are vast and may include any miniaturisation task, collective exploration, targeting and monitoring application that favour the coop- erative behaviour of a group of agents to superior performance. Further applications comprise firefighting drones, agriculture and precision farming, construction task, disinfection robots for hospitals and decontamination floor use.In this section, another background environment is created in Netlogo to test the search- dominated motion algorithm’s efficacy on a pollution source for decontamination.
</p>
<p align="center">
<img width="804" alt="Screen Shot 2021-12-23 at 10 04 09 AM" src="https://user-images.githubusercontent.com/70657426/147208495-28bf7429-29ea-445e-8eab-68830d5d647b.png">
</p>  
  
### Investigation of the speed and size of the swarm
<p align="center">
<img width="804" alt="Screen Shot 2021-12-23 at 10 05 17 AM" src="https://user-images.githubusercontent.com/70657426/147208654-d815b0c0-fa51-46e5-aadd-be6ccaa31182.png">
</p>

### Bee Shimeering
Another application of the cellular automata algorithm designed at the beginning of the study can be used to model bee shimmering. More GIF files and pictures are available in the repository. 
<p align="center">
<img width="987" alt="Screen Shot 2021-12-23 at 10 12 19 AM" src="https://user-images.githubusercontent.com/70657426/147209554-7039111a-2c78-485a-b6fc-24fdb4fcaf3d.png">
</p>

<p align="center">
<img width="300" alt="Screen Shot 2021-02-19 at 3 22 36 PM" src="https://user-images.githubusercontent.com/70657426/147209752-a786ef93-ca79-44a1-9dda-2eb83c9d7c62.png">
</p>



  
