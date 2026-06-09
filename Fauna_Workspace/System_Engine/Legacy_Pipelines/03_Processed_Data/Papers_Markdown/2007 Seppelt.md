--- 
source: 2007 Seppelt.pdf
--- 

Ralf Seppelt
Computer-Based Environmental
Management
Computer-Based Environmental Management. Edited by Ralf Seppelt
Copyright © 2003 Wiley-VCH Verlag GmbH & Co. KGaA, Weinheim
ISBN: 978-3-527-30732-6


Related titles
Martin Scheringer
Persistence and Spatial Range of
Environmental Chemicals
308 pp., 2002.
ISBN: 3-527-30527-0
David P. Paine, James D. Kiser
Aerial Photography and Image
Interpretation
656 pp., 2003.
ISBN: 0-471-20489-7
David P. Lawrence
Environmental Impact Practical
Solutions to Recurrent Problems
568 pp., 2003.
ISBN: 0-471-45722-1
Bruce E. Logan
Environmental Transport Processes
672 pp., 1999
ISBN: 0-471-18871-9


Ralf Seppelt
Computer-Based Environmental Management


The Authors
Dr. Ralf Seppelt
Institute of Geoecology
Technical University Braunschweig
Langer Kamp 19c
38106 Braunschweig
Germany
This book was carefully produced. Never-
theless, author and publisher do not warrant
the information contained therein to be free
of errors. Readers are advised to keep in
mind that statements, data, illustrations, 
procedural details or other items may 
inadvertently be inaccurate.
Library of Congress Card No. applied for
British Library Cataloguing-in-Publication
Data: A catalogue record for this book is
available from the British Library.
Bibliographic information published by
Die Deutsche Bibliothek
Die Deutsche Bibliothek lists this publication
in the Deutsche Nationalbibliografie; 
detailed bibliographic data is available in the
Internet at <http://dnb.ddb.de>.
© 2003 WILEY-VCH Verlag GmbH & Co.
KGaA, Weinheim
All rights reserved (including those of trans-
lation into other languages). No part of this
book may be reproduced in any form – by
photoprinting, microfilm, or any other
means – nor transmitted or translated into
machine language without written permis-
sion from the publishers. Registered names,
trademarks, etc. used in this book, even
when not specifically marked as such, are not
be considered unprotected by law.
printed in the Federal Republic of Germany
printed on acid-free paper
Printing
Druckhaus Darmstadt GmbH,
Darmstadt
Bookbinding
Litges & Dopf Buchbinderei
GmbH, Heppenheim
ISBN
3-527-30732-X


Foreword
As an active designer, user, and teacher of models and modeling, I’m always on the
lookout for better tools. Ralf Seppelt’s book is a unique and welcome addition to that
toolbox. It is unique in its comprehensive integration of the theory and practice of
environmental modeling and management.
Because of this integration, the book will appeal to three broad audiences and be
useful:
(1) as an upper level or graduate course text in environmental modeling and man-
agement;
(2) as a guide for practitioners to get up to speed on the latest developments in
computer modeling of the environment;
(3) asaguideforenvironmentalmanagerstogetagoodhandleonthelatestdevelop-
ments in modeling and how they couldbe useful in making better environmental
decisions.
As a teacher of environmental modeling, I’ve been searching for many years for the
perfect text to use in courses. There are several books out there that are each very
good in their own way, but which cover only some of the issues needed to get a
good, comprehensive grasp of modeling and the uses of modeling in environmental
management. It’s also hard to ﬁnd a text that is at just the right level — not so
general as to be useless yet not so technical as to be useful only to a small, specialized
v


vi
FOREWORD
audience. My search has ended with the publication of Ralf Seppelt’s book and I
intend to use it as a core text in modeling courses.
As a practitioner of modeling as a method to achieve an integrated understanding
of complex systems, I can appreciate the range of applications covered in the book.
Ralf spent a sabbatical year at our Institute when were still at the University of
Maryland and jointly developed several of the applications discussed in the book.
That year was extremely productive for all of us, and helped to expand the envelope
of spatially explicit environmental modeling, as reported in the book. I intend to use
the book to make researchers in our Institute fully conversant with the theory and
latest applications in environmental modeling so they can take the next steps forward.
As someone who interacts with environmental managers and tries to help them to use
modeling effectively in their decision-making, I can see that the book will be very
useful. Managers need a single source that can show them both how models work and
how they can be useful in decision-making. By integrating theory and applications,
this book can quickly bring environmental managers up to speed and help them to
use existing models more effectively, to commission better models in the future, and
to actively participate in the modeling process themselves. I intend to recommend
this book to environmental managers as the best way to familiarize themselves with
the latest theory and uses of environmental modeling.
Finally, as Ralf Seppelt makes clear in this book, modeling is an activity, and this
activity is itself at least as important and valuable as the models themselves. Mod-
eling as an activity can be seen as the essence of the scientiﬁc method. The unique
integration that this book represents is thus also a good platform for talking about
what science is at a very fundamental level. The links between science and policy
are so tenuous today precisely because of some fundamental confusions about what
science is, and how it can best inform decision-making. Science is not certainty, as it
is often mischaracterized in the media. Science is about understanding uncertainty,
and modern science recognizes that complex systems can never be understood with
certainty. Computer modeling is the best tool we currently have to describe and un-
derstand uncertainty in complex systems. By clarifying these confusions, this book
will be a valuable and important tool at a very fundamental level, and will help to
create a better link between science and policy in general.
July 2003
Robert Costanza
Gund Professor of Ecological Economics
and Director, Gund Institute of Ecological Economics
The University of Vermont
Burlington, VT, USA


Acknowledgments
Ecological modeling is a fast developing area in the ﬁeld of environmental science
in which substantial progress has been achieved in recent years. User-friendly soft-
ware packages, including high performance numerical tools, enable environmental
scientists to code complex systems and thus study environmental processes in a sys-
tematic fashion. Modeling has become an important part of environmental research.
Redundancy and a confusing diversity, however, have been a frequent result of this
development. In this book, the recent state of environmental modeling is presented in
a concise manner, and model applications in environmental management are studied.
This project would have been impossible without the support of several colleagues
and friends whom I would like to thank especially now that this project has been
completed.
First of all, I would like to thank Otto Richter for his support and inspiring ideas.
Special thanks go to the good humor of Dagmar S ¨ondgerath and Boris Schr¨oder
for many fruitful discussions, suggestions and critical remarks, and — much more
important — the resulting motivation.
The ideas and results presented in this publication are the outcome of numerous
co-operations and projects. I appreciate having worked together closely with the
following people (in alphabetic order): Robert Costanza, Michael Flake, Claudia
Hiepe, Olaf Jensen, Verena Korr, Matthias Kuhnert, Tom Maxwell, Florian Stange,
Christian Thiel, Christine Vogel, and Alexey Voinov. I gratefully appreciate their
suggestions, inspiring discussions and ideas.
vii


viii
My thanks are due to Klaus-J¨urgenSchmalstieg for his support related to GIS analysis
and data management, to Wolfgang Max for his unfailing technical support as well
as to Kerstin Schulze for technical assistance with ﬁgures, tables, bibliography and
several simulation runs. Marko-Michael Temme and Conrad Hoffmann spent much
of their spare time in programming and tweaking the software presented in this book.
I am very grateful to Wolfgang Pittroff, Leland J. Jackson and Charles A.S. Hall for
their remarks and suggestions for this book in a very early stage of the project. Mary
Korndorffer has carefully edited the ﬁnal manuscript. Very special thanks to her,
as well as to Carsten Dormann who provided many valuable comments on the ﬁnal
manuscript.
Finally, not only does environmental science make progress, so too did the situation
of my private life. Since my ﬁrst projects in environmental science several years ago
Tim, Anika, and Moritz were born and changed our life fundamentally. Thus, most
of all I owe a deep sense of gratitude to my wonderful family and especially to my
wife Martina who supported me all these years.
R. S.


Contents
Foreword
v
Acknowledgments
vii
Introduction
xvii
Part I
Setting the Scene: Diversity of Environmental Modeling
1
From Conceptual Modeling to Computer Simulations
1
1.1
Introduction
1
1.2
The Modeling Process
3
1.2.1
System Analysis: Conceptual Models
3
1.2.2
Properties: Granularity, Extent and Scale
7
1.2.3
Toolbox and Language: Mathematical Models
10
1.2.4
Results: Computer Models
12
1.3
Model Analysis
14
1.3.1
Veriﬁcation, Validation and Calibration
14
1.3.2
Intrinsic Veriﬁcation and Predictive Power
15
1.3.3
Uncertainty
17
1.3.4
Categories and Classiﬁcations
18
ix


x
CONTENTS
1.4
Linking Real World Data and Models
21
1.4.1
Regionalization: Applications to Investigation
Sites and Spatial Validity
21
1.4.2
Parameter Estimation
23
1.5
Modeling Languages and Development Platforms
24
1.5.1
Overview
24
1.5.2
Mathematical Languages
25
1.5.3
Generic Tools for Model Development
27
1.5.4
Conceptual Modeling Tools
28
1.5.5
Modeling and Programming Environments
29
1.5.6
Numerical Mathematics
30
1.6
Summary
33
2
Environmental Models: Dynamic Processes
35
2.1
Introduction
35
2.2
First Trophic Level: Primary Producers
35
2.2.1
Crop Growth
36
2.2.2
Temporal Patterns of Annual Plants
37
2.2.3
Nitrogen Uptake
38
2.2.4
Interspeciﬁc Competition: Weeds and Weed
Control
39
2.3
Parameter Estimation (Part I)
39
2.3.1
Experimental Design of Field Experiments
40
2.3.2
Application of Algorithms
41
2.3.3
Parameters of Crop Growth
43
2.3.4
Competition Models
46
2.3.5
Results
49
2.4
Abiotic Environment: Water and Matter Dynamics
50
2.4.1
Nutrient Cycle: Detritus
51
2.4.2
Xenobiotica Fate: Agrochemicals
52
2.5
Parameter Estimation (Part II)
53
2.5.1
Laboratory Experiments
54
2.5.2
Results
54
2.6
Higher Trophic Levels: Consumers or Pest Infestation
55
2.6.1
Continuous Population Dynamics
55
2.6.2
Age-structured Populations
57
2.6.3
Types of Population Dynamic Models
60
2.7
Model Integration: Generic Agroecosystem Model
62
2.8
Summary
65


CONTENTS
xi
3
Environmental Models: Spatial Interactions
67
3.1
Spatial References in Environmental Models
67
3.1.1
Spatial Scales and Model Support
67
3.1.2
Models for Spatial Data Structures
70
3.1.3
Spatial Patterns
72
3.2
Aggregated Spatially Explicit Models
73
3.2.1
Abiotic Processes
73
3.2.2
Biotic Processes
76
3.3
Integrating Spatially Explicit Models
85
3.3.1
Regionalization of Site Models
85
3.3.2
Cellular Automata
89
3.3.3
Generic Landscape Models
91
3.4
Discussion
94
Part II
Integrated Models
4
Multi-paradigm Modeling
99
4.1
Introduction
99
4.2
Fundamental Aspects of Environmental Modeling
100
4.3
Mathematics of Environmental Modeling
102
4.3.1
General Model Equation
102
4.3.2
Integrated Models
103
4.4
Model Documentation and Model Databases
104
4.4.1
Introduction
104
4.4.2
Model Databases
105
4.4.3
Meta-modeling Concepts
107
4.5
Summary and Outlook
110
5
Concepts: Hybrid Petri Nets
111
5.1
Introduction
111
5.1.1
Concepts of Hybrid Model Development
111
5.1.2
Aim and Scope of the Development
112
5.2
Theoretical Background
112
5.2.1
Hybrid Low Level Petri Nets
112
5.2.2
Functional Behavior
114
5.3
Development Platform
115
5.3.1
Overview
115


xii
CONTENTS
5.3.2
Meta-modeling Concept
117
5.3.3
Core Simulation Algorithm and Model
Analysis
117
5.4
An Ecological Modeling Example
118
5.4.1
Predator–Prey Interactions
118
5.4.2
Event-based Modeling of Predator–Prey
Interactions
119
5.4.3
Simulation Results
120
5.4.4
Discussion and Extensions
121
5.5
Concluding Remarks
122
6
Case Studies: Hybrid Systems in Ecology
123
6.1
Introduction
123
6.2
Hybrid Crop Growth Models
123
6.2.1
Modeling of Crop Growth with Dynamically
Changing Model Structures
123
6.2.2
Hybrid Petri Net
125
6.2.3
Results
126
6.3
The Gal´apagos Archipelago and the Blue-winged
Grasshopper
128
6.3.1
Meta-population in Island Biogeography
128
6.3.2
Spatially Explicit Hybrid Petri nets
130
6.3.3
Results
131
6.3.4
Comparison
132
6.4
Summary
135
7
Applications: Environmental Impact Assessment
137
7.1
Introduction
137
7.2
Aim and Scope
138
7.3
Methodology
138
7.3.1
Life Cycle Inventory
139
7.3.2
The Link: Environmental Fate Modeling
140
7.3.3
Fuzzy Expert Systems for Impact Assessment
140
7.4
Life Cycle Inventory of the Production Process
143
7.5
Environmental Fate Modeling of NOx-Emissions
145
7.5.1
Overview
145
7.5.2
Atmospheric Transport Model
146
7.5.3
Process Model
148
7.5.4
Results
150


CONTENTS
xiii
7.6
Environmental Impact Assessment
151
7.6.1
Soil Acidiﬁcation
151
7.6.2
Eutrophication
152
7.6.3
Plant Damage
154
7.7
Discussion
154
Part III
The Big Picture: Environmental Management
8
Scenario Analysis and Optimization
159
8.1
Introduction
159
8.2
Optimization and Environmental Modeling
161
8.2.1
Analytical Treatment and Non-spatial
Applications
161
8.2.2
Spatially Explicit Applications
162
8.3
Assessing the Environment Variables
162
8.3.1
Indicators
162
8.3.2
. . . and Applications for Optimization
166
8.4
General Optimization Task
167
8.4.1
Performance Criteria
167
8.4.2
General Optimization Task
169
8.4.3
Methodology
170
8.5
Discussion
171
9
Prerequisites: Temporal Hierarchies and Spatial Scales
173
9.1
Introduction
173
9.2
Hierarchical Dynamic Programming
174
9.2.1
Introduction
174
9.2.2
Hierarchies and Temporal Scales
176
9.2.3
Program Library
180
9.2.4
Concluding Remarks
182
9.3
Optimization and Spatially Explicit Models
182
9.3.1
Computational Effort
183
9.3.2
Local and Global Performance Criteria
183
9.3.3
Grid Search Strategy on Local Problem
185
9.3.4
Disturbing a Solution: Monte Carlo
Simulation
185
9.3.5
Genetic Algorithm Solving the Global Problem 187
9.3.6
Toolbox for Spatially Explicit Optimization
188


xiv
CONTENTS
9.4
Summary
191
10 Optimum Agroecosystem Management: Temporal Patterns
193
10.1 Introduction
193
10.2 Assessing the State of an Agroecosystem
194
10.2.1 External Cost and Non-measurable Variables
194
10.2.2 Performance Criteria
194
10.2.3 Weighting Schemes
195
10.3 Agricultural Optimum Control Problem
196
10.3.1 Optimization Task
196
10.3.2 Hierarchical Structure of the Problem
197
10.4 Short-term Solutions: Managing a Vegetation Period
198
10.4.1 Optimum Fertilizing Schemes
198
10.4.2 Optimum Pesticide Application Timing
199
10.5 Long-term Solutions: Managing Crop Rotations
201
10.5.1 Nutrient Balance
201
10.5.2 Pest Control
201
10.6 Discussion
202
11 Optimum Agroecosystem Management: Spatial Patterns
207
11.1 Introduction
207
11.1.1 Site-speciﬁc Agroecological Modeling
207
11.1.2 Aims, Scope and Region
208
11.2 Optimum Control in Regionalized Models
208
11.2.1 Agroecological Simulation Model
208
11.2.2 Optimization Task
210
11.3 Concept of Optimum Spatial Control
210
11.4 Optimization and Simulation Experiments
213
11.4.1 Types of Spatial Solutions
213
11.4.2 Results
216
11.5 Discussion
217
12 Changing Landscapes: Optimum Landscape Patterns
221
12.1 Introduction
221
12.2 Performance Criteria for Landscape Optimization
223
12.2.1 Economic–Ecologic Assessment
223
12.2.2 Localization of Optimization Problem
225
12.2.3 Multi-criteria Assessment of Ecosystem
Functions
226


CONTENTS
xv
12.2.4 Numerical Effort
227
12.3 Validation of Concept: Results for Hunting Creek
Watershed
228
12.3.1 Local Optimization
228
12.3.2 Monte Carlo Simulations
229
12.3.3 Statistical Analysis
232
12.3.4 Genetic Algorithms
233
12.4 Results of Multi-criteria Optimization
235
12.4.1 General Results for Optimum Land Use
Patterns
235
12.4.2 Scenarios of Optimized Land Use Patterns
239
12.5 Climatic Variability and Optimum Land Use Patterns
244
12.6 Multi-scale Analysis of Landscape Patterns
244
12.6.1 Distance Measure of Discrete Maps
246
12.6.2 “Correlation”-analysis of Landscape Patterns
247
12.6.3 Optimization Results on Differing Scales
248
12.7 Summary and Outlook
250
12.7.1 Methodological Aspects
250
12.7.2 Optimization Results as Multi-stage Decision
Process
251
12.7.3 Application of Results
251
12.7.4 Patterns and Processes
252
12.7.5 Outlook
253
13 Conclusions, Perspectives and Research Demands
255
13.1 Retrospection
255
13.2 Conclusions
256
13.3 Perspectives
257
References
259
Additional References
279
Web Ressources
279
Copyrights and Sources
279
Quotations
280
Index
281


Introduction
“and what is the use of a book,” thought Alice,
“without pictures or conversations?”
—Lewis Carroll1
Modeling, . . .
Our environment with its dynamic and spatial processes is recognized as complex,
highlyinteractingandspatiallydistributed. Thesepropertiesmakeanalyzing,describ-
ing, modeling and even simulating our environment a challenging task. A framework
that enables us to study, for example, the consequences of human inﬂuences on eco-
logical systems without even disturbing these is a valuable and important tool for
environmental management. Models are therefore identiﬁed as important and neces-
sary tools for studying and understanding ecological processes, testing hypotheses of
the functioning of ecosystems in a systematic manner and for investigating environ-
mental response to human impact.
This makes modeling an important part of the interdisciplinary research ﬁeld of en-
vironmental science. Ecological modeling however is done less and less by mathe-
maticians and more and more by practicing ecologists and environmental scientists.
1see p. 280 for references of quotations.
xvii


xviii
INTRODUCTION
The present state of environmental modeling is characterized by a number of model
developments. Several authors state that a general concept is missing in ecologi-
cal or environmental modeling. Recent development of environmental models has
shown that a multitude of possible approaches and theories have been developed.
Some authors complain that we have produced an enormous redundancy. This mul-
titude of different approaches refers to the considered temporal scale, the considered
mathematical languages — such as differential equations (partial or ordinary), matrix
models, fuzzy systems etc. — and the chosen concept of regionalization and spatial
extent. The incorporation of spatial attributes into the modeling process causes a
mismatch between the scale at which attributes are obtained, and the scale at which
the processes occur.
The ﬁrst part of the book (Chapters 1 to 3) gives a synthesis of model development
concepts. Compiling mathematical equations and setting up simulation models is
a complex and challenging task. Setting up ecological models requires a detailed
system analysis of the processes of interest. A systematic way to achieve a concise
and valid simulation model is to start with a conceptual model, which every scientist
usually has in mind when investigating a process. Chapter 1 traces the path from
conceptual models to validated regionalized environmental simulation models. The
step of translating conceptual models into computer models is assisted by several de-
velopmentplatforms. These platformstranslate conceptualmodels into mathematical
equations of a certain mathematical “dialect”.
Focusing on processes of the abiotic environment as well as the ﬁrst two trophic
levels of the biotic environment, several different translations of conceptual diagrams
into mathematical models are studied in Chapters 2 and 3. The ﬁrst focuses on the
dynamic patterns on different temporal scales such as nutrient ﬂow, water transport,
growth of crops and weed, population dynamics, competition, etc. Migration of
species, vertical and horizontal ﬂuxes of matter and information through a landscape
are the characteristic properties of ecosystems. In Chapter 3 spatial interactions are
discussed and the possible mathematical modeling concepts are presented, starting
from highly aggregated mathematical models given by partial differential equation
systems, we end up with with a discussion of cellular automata. For comparison,
different mathematical “dialects” are used for modeling the same process to analyze
and compare different methodologies.
Integration, . . .
Although there is consensus on a general methodology of model development, one
needs to consider that environmental modeling is a diverse ﬁeld of research. First of
all because it is an interdisciplinary issue. Biologists, ecologists, computer scientists,
mathematicians, physicists have to work together and to integrate their methodology
to solve ecological problems of the 21st century. This diversity leads to a multitude
of approaches solving similar or even identical tasks. Several scientists complain of
a lack of theoretical foundation of environmental modeling.


INTRODUCTION
xix
For example, conceptual difﬁculties stem from the fact that processes of different
dynamic quality interact. The dynamics of technical systems are mostly time discrete
and their dynamics are closely related to discrete spatial structures, whereas many
environmental processes are continuous in time and space. The whole system can be
characterized as structured time discrete and time continuous. One is faced with a
problem that can be summarized as mathematical heterogeneity. It is not feasible to
model integrated systems in the framework of one mathematical “dialect”.
An environmental model requires the integration of all these approaches. This re-
quires a general theoretical framework. The subject of Part II of the book is to bring
together modern mathematical methodologies to solve the task of integration. These
concepts are used to assess the anthropogenic impacts of production and the use of
goods and services on the environment. This life cycle impact assessment methodol-
ogy comprises a system-wide analysis of mass- and energy ﬂows, performed within
the step of life cycle inventory. Distributions of emissions are estimated within an
environmentalfate model including dispersion–reactionmodeling and impact assess-
ment has to be performed for different impact categories. The product is a hybrid
model which integrates different environmental techniques and demonstrates how
these effects can be addressed in environmental assessment.
. . . and Management
Quantitative and qualitative analysis of environmental processes by computer mod-
els is one aspect of ecosystem modeling. Additionally, a very frequent application
of ecological models is to study the consequences of anthropogenic impact on the
ecosystem with respect to the environmental fate of substances, habitat suitability of
species, persistence of populations etc. In this way different management strategies
can be compared. The question of the degree of impact which nature can sustain
without harm to the environment has already been posed. Ideas like most sustainable
yield were introduced in the late 1960s. Ecosystem management has become now
an important discipline of scientiﬁc research and is an important branch in the po-
litical decision-making process. Because ecological models are complex and highly
interacting, as stated above, this decision making process requires methodological
support. The third part of the book deals with applications of ecological models
in the decision-making process: either by the use of scenario analysis technique or
by the application of optimum control theory to an ecosystem model. Problems of
ecosystem management are solved by the use of numerical optimization. This can
be interpreted as the follow up of the most sustainable yield concept by the use of
scientiﬁc computing.
With increasing complexity of ecosystem models, one becomes aware, that scenario
analysis may not be the appropriate tool to vary all required control parameters.
Systematically sorting through all possible combinations of control variables yields
a desired optimal scenario. This is achieved by the optimization or optimum control
approach. Chapter 8 introduces this third part of the book, offers an overview of


xx
INTRODUCTION
the approaches “scenario analysis” versus “optimization” and deﬁnes the tasks to be
solved for optimum control of environmental systems.
Complexity of environmental models leads to an enormous computational effort, if
these models are to be used in optimum control theory. Introducing certain hierarchies
is one concept which can deal with increasing complexity. In Chapter 9 a framework is
proposed for an application of environmentalmodels in optimum control theory. This
developmentfocuses on spatially explicitmodels as well as models with a broadrange
of temporal patterns and dynamics. The generic code can cope with hybrid models.
It requires appropriate numerical procedures, too. This is achieved by a hierarchical
approach to the optimization problem and this decreases numerical effort.
Applications of this concept are presented in Chapters 10 to 12. Chapter 10 focuses
on optimum temporal patterns of management strategies of an agroecosystem. Dif-
ferent results of optimum fertilizer input, pest management, weed control and crop
rotation schemes are presented. Several scenarios of environmental assessment are
compared using the tool of optimization. These results are then studied within a
regionalized model. Beside the dynamic solution, Chapter 11 focuses on the region-
alization of the optimum control problem. The task is solved by the identiﬁcation
of homogeneous units in the observed region by a geographic information system.
The second innovative topic, which enables a regionalized solution of the optimum
control problem, is the estimation of families of optimum solutions parameterized by
spatial properties. The proposed methodology supports the step of decision support
in site-speciﬁc farming.
In Chapter 12 all these concepts are applied to solve management problems of land
use with a spatially explicit model on a landscape scale. Spatially explicit ecosystem
models allow the calculation of water and matter dynamics in a landscape as functions
of spatial localization of habitat structures and matter input. For a mainly agricultural
region the nutrient balance as a function of different management schemes is studied
in this chapter. The results are tested using Monte Carlo simulations which are based
on different stochastic generators for the independent control variables. Gradient
free optimization procedures are used to verify the simplifying assumptions. The
framework offers tools for optimization with the computational effort independent of
the size of the study area. As a result, important areas with high retention capabilities
are identiﬁed and fertilizer maps are set up depending on soil properties. This shows
that optimization methods can be a useful tool even in complex simulation models
for systematic analysis of management strategies for ecosystem use.
Summary: How this Book is structured
Aspects of ecological modeling are of increasing importance in any branch of ecol-
ogy, biology, landscape ecology, and environmental management. The book focuses
on two main issues: the integration of different modeling approaches, together with
applications in optimization and optimum control theory. It aims at supporting prob-
lems of environmental management and tries to bring together modern mathematical


INTRODUCTION
xxi
methods with environmental ecological research. The concept of the book is to offer
a theoretical and methodological platform for environmental modeling, that can pro-
vide a starting point for every environmental scientist to solve a particular modeling
problem. This is achieved by using the level of conceptual models as a starting point
for model development and explanes the types of models that can be derived from
one conceptual diagram.
Recent progress in ecological modeling is presented in a concise way showing results
of high standard mathematical methods, such as the use of numerical solutions of
partial differential equations for modeling water and matter transport, as well as
populationdynamics and migration in real landscapes. This provides a foundationfor
aggregated spatially explicit models using geographic information systems. Finally
these high standard mathematics are used to develop concepts of solving optimization
and optimum control problems for environmental management.
This structure of the book follows these objectives. Chapter 1 introduces terms and
methodologiesand presents an overview of environmentalmodeling concepts. Chap-
ters 2 and 3 can be understood as a toolbox for translating conceptual models into
equations. These chapters providethe necessary functions and equations used in most
ecological models. It must be noted that all equations presented are illustrated with
examples and applications. Chapter 4 discusses the results obtained in the context of
meta modeling and scientiﬁc theory. Further applications of hybridmodels in biology
as well as in environmental assessment are reported in Chapters 6 and 7. The focus
in Chapters 5 and 9 is on the mathematical foundation of the integrating modeling
concept as well as the application of environmental models in optimization. Applica-
tions of concepts are presented in Chapters 10 through 12, which are understandable
without reading Chapters 5 or 9 in detail.
