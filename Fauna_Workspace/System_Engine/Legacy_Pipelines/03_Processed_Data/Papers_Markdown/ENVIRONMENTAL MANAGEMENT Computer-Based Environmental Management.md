--- 
source: ENVIRONMENTAL MANAGEMENT Computer-Based Environmental Management.pdf
--- 

Ralf Seppelt
Computer-Based Environmental
Management


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


Part I
Setting the Scene:
Diversity of Environmental
Modeling
The Analytical Engine has no pretensions whatever to originate any-
thing. It can do whatever we know how to order it to perform. It
can follow analysis; but it has no power of anticipating any analytical
relations or truths.
—Ada Byron


1
Tour d’horizon:
from Conceptual Modeling
to Computer Simulations
1.1
INTRODUCTION
Environmental models are tools which help us understand how ecological processes
work and allow us to test hypotheses about ecological processes in a systematic
manner. Setting up an ecological model requires detailed system analysis of the
processes of interest. After this translation into mathematical equations is performed.
Recent development of ecological and ecosystem models has provided a multitude
of possible approaches and theories. Some authors complain that we produced an
enormous redundancy (M¨uller, 1997).
Why? Environmental processes are recognized as complex, highly interacting and
spatiallydistributed. Thesepropertiesmakeanalyzing,describing,modelingandeven
simulating our environment a challenging task. One probably intrinsic property of
ecological models is that these models are hybrid or mathematically heterogeneous.
For an explanation of this property it necessary ﬁrst to analyze how mathematical
models of ecological processes are set up in general.
Development of environmental models encompasses physical, mathematical, and
conceptual modeling. All belong to the same process and none of the parts can be ne-
glected in compiling a well-deﬁned simulation model. Table 1.1 gives an explanation
for this.
Two examples are chosen to illustrate this close relationship of conceptual, mathe-
matical, and physical models. Let us consider the problem of modeling population
dynamics of an insect species in a ﬂood plain. The questions to be answered are, how
do ﬂooding events change habitat properties, and is it possible to identify a minimal
viable population from this analysis?
1


2
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Table 1.1
Conceptual, physical, and mathematical modeling. The table contains three sen-
tenceswiththreedifferentoptions. Startreadingwiththeﬁrstcolumnandcompletethesentence
with the completion in the column (conceptual, physical, or mathematical) of your choice.
Models are . . .
mental or conceptual.
physical.
mathematical.
System identiﬁcation
encompasses . . .
deﬁnition of system boundary, components, interactions.
The model is . . .
a conceptual verbal de-
scription of system be-
havior.
a scaled reproduction
of a real system.
coupling of functions,
rules, equations.
Elements of a model
are . . .
premises, conclusions,
syllogism.
a physical object.
mathematical
func-
tions
and
(state)
variables.
With the plausibility
check . . .
conclusions are tested
(for well-known situa-
tions).
an experiment
in a
well-known
environ-
ment is performed.
model
behavior
is
analysed
using
dif-
ferent
methodologies
(stability or sensitivity
analysis).
Finally, a simulation is
. . .
a
Gedankenexperi-
ment.
a physical
measure-
ment by given bound-
ary conditions.
a (numerical) solution
of the mathematical
equations or rules un-
der given initial and
boundary conditions.
The second example brieﬂy discussed considers the problem of sediment erosion in
a watershed and the question of which landscape elements can help to prevent soil
loss at a given investigation site.
System analysis, as noted in Table 1.1, encompasses the deﬁnition of the system
boundaries, important components and processes, and the interaction between them.
The system boundary of our ﬂood plain is bordered by the river and the embankment.
The temporal system boundary is deﬁned by a number of generations of the popu-
lation. The more physical approach to answering the question raised may be either
the location of traps in the investigation site, in which the abundances of the studied
species can be counted,presumably as a function of abiotic parameters,or a laboratory
experiment in which the parameters of the population dynamics are identiﬁed.
The system boundary of a hydrological catchment is deﬁned by the hydrological
watershed. The important component is an element of the landscape, which size
is to be determined, characterized by the properties elevation, slope and roughness.
Element size and its properties are strongly related. The question of scale comes up
in this context and will be discussed later on. A physical model might focus on two
issues. First, ground truth data may be derived from ﬁeld experiments. The second
idea of a physical model is to rebuild the landscape on a laboratory scale. A physical
model of typical elements of the landscape under consideration is rebuilt. Knowledge
of the sediment runoff process is derived from several laboratory experiments.


THE MODELING PROCESS
3
A mathematical model for both examples is based on the parameters derived from the
physical models, from laboratory and ﬁeld experiments and usually from literature
data.
Note that compiling a mathematical model necessitates consideration of physical
models and conceptual models. Without a clear speciﬁcation of system boundaries
of the parameters of interest, without knowledge of important and less important
processes and without well-educated guesses of the values of sensitive parameters,
an environmental model cannot be set up. We will now focus on the step of model
development in detail, aiming at a mathematical model for an environmental process
of interest.
1.2
THE MODELING PROCESS: FROM CONCEPTUAL MODELS TO
COMPUTER SIMULATIONS
1.2.1
System Analysis: Conceptual Models
The starting point of any kind of model development is the design of a conceptual
model. The conceptual model aggregates our knowledge of the system and implies a
thorough (albeit subjective) selection of components and processes judged essential
for the processes under study in a given spatio–temporal context.
An example is given in Figure 1.1.
It shows three different conceptual models.
Figure A displays possible migration pathways of a neozoan between the Gal ´apagos
archipelago. Figure B summarizes seven stages of development of a ground beetle
(Carabidae species) that is possibly invading the Gal´apagos archipelago. Figure
C displays the small and large circular ﬂow of matter, in this case nutrients and
pesticides, through an agricultural ecosystem together with abiotic parameters (such
as precipitation and radiation) and anthropogenic disturbances (by harvesting, pest
control and seed).
All these conceptualizations have this in common: certain components, here islands,
containers, individuals, are connectedby directed arrows. These arrows denote a ﬂow
of information, matter or substances. The graphical representation in a conceptual
model helps to identify dependencies and helps to identify the processes that depend
on each other. Feedback-loops are easily found.
Deﬁnition 1.1 (Conceptual Model) A conceptual model is graphically presented in
the form of a compartment system. Compartments are deﬁned with respect to mor-
phology and to physical, chemical and biological states. Connection between these
compartments denotes exchange of matter or information between certain compart-
ments or processes. Certain compartments may act as containers for sub-structures
or sub-models.
Jørgensen & Bendoricchio (2001) distinguish several types of conceptual models
or diagrams. With some modiﬁcations, these authors list the following types of
conceptualization:


4
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Isabela
Santa Cruz
Santiago
San Cristóbal
Floreana
Espanola
Santa Fe
Pinzón
Rábida
A
Adult
Fertile Adult
Larva
Egg
B
Producers
Crops & Weed
Consumers
Inorganic
Nutrients
Pest
Control
Harvest
Crop
 Rotation
Bacteria
Mineral
Fertilizer
Consumers
Pesticide
Pesticide
Dead Organic
Matter
Upper soil layer (root zone)
C
Metabolite
Pupa
Fig. 1.1
Three different graphical representations of a conceptual model. Figure A shows
spatial migration pathways of a neozoan species in the Gal´apagos archipelago. Figure B shows
the development of a ground beetle (Carabidae species) simpliﬁed to a stage structured model.
Finally, Figure C shows a conceptual scheme of mass and energy ﬂuxes in an agricultural
ecosystem.


THE MODELING PROCESS
5
Word models are based on language as a conceptualization tool and are a verbal
description of the process. This concept is related to the Gedankenexperiment
noted in Table 1.1.
Picture Models use illustration of components seen in nature and place them within
a framework of spatial or temporal relationships. Figure 1.1.B is an example
of this conceptualization method.
Signed Digraphs allow the display of qualitative dependencies between compo-
nents, displayed by boxes. Inﬂuences between the components are speciﬁed by
connections and a plus or minus sign denoting positive or negative inﬂuence.
Box-models Figure 1.1.C is an example of this commonly used conceptual design.
Each box represents an compartment, arrows denote ﬂuxes of matter, energy
or information.
Input/Output Models, Black-box, White-box Models can be considered as box-
models. However the term “input/output” suggest that everything between
input and output is not of interest for the considered model.
In this context the terms “white-box”and“black-box” models will be discussed.
Models are labeled black-box models if their internal functional relationships
are derived from simple input/output relationships, e.g. statistical analysis, re-
gression functions. Often these models are called input/output models, too.
White-box models are derived from basic physical or chemical laws and are
constructed on causality for all processes. Obviously, there are many models
that contain some causalities and some input/output relations. These models
usually are termed grey-box models.
Feedback Dynamics are a symbolic language introducedbyForrester (1968). These
diagrams are a special form of box-models, that allows automatic translation
from the graphical representation of the system to a system of (nonlinear)
differential equations.
Energy Circuit Diagrams were developed by Odum (1983). There diagrams give
information of thermodynamic constraints, feedback mechanisms and energy
ﬂows.
What all these conceptualization methods have in common, is that the dynamic be-
havior of the system is implicitly deﬁned by the topology of the network and the
speciﬁcation of the network element with their parameter. The growth of a crop, the
amount of biomass added in a certain period of time, for instance in Figure 1.1.A,
depends on the growth rate, that probably is also a function of nutrient availability
(another component of the network), temperature, precipitation and CO 2 content.
The choice of a certain conceptualization method will depend on the modelers habits
and preferences and on the modeling problem to be solved. However, what all these
types of conceptual model have in common, is the issue of a graphical representation


6
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
(State) Variables
Parameters
Adjunct Functions
Processes
Flows
Control Variables
Boundary Conditions
Forcing Functions
Box Models
Feedback 
Dynamics
Energy 
Flow
Models
State Var
Rate
Constant,
Function
Sink/Source
StateVar
Constant
Function
Flow
Event
Event
Input-
Output
Models
Rate
State
Petri Nets
Place
Flow
Transition
Interaction
Exchange of 
Information
Sub-Systems
Source
Sink
Transaction
Consumer
Storage
Amplifyer
Cycling Receptor
Fig. 1.2
Summary of icons in conceptual models used in deedback dynamics, energy ﬂow
models, box-models, Petri nets separated by the mathematical translation (state) variables,
parameters, control and process.
of the system of interest. Figure 1.2 lists the most important icons of the conceptual-
ization methods ordered by the operation performed with a dynamic model. In this
diagram state variables, mathematical functions, parameters and boundaryconditions
are identiﬁed by different graphical icons. While these icons may differ from one
type of conceptual model to another, the core concept remains the similar.
As information on the topology of the system is available at this stage,the ﬁrst analysis
of the system can be based on the resulting adjacence matrix. Based on the adjacence
matrix, direct and indirect interactions can be identiﬁed. The adjacence or matrix
modelisﬁrstusedasanintermediatestepfortranslatingthegraphicalrepresentationof


THE MODELING PROCESS
7
a model into a mathematical notationandtosupport numerical solutionof the resulting
equations. Additionally, the matrix model is an intermediate format to translate
between different conceptual models, see Chapter 4. Matrix conceptualization or
matrix models are a tool for model description and analysis as well as an additional
conceptualization methodology.
1.2.2
Properties: Granularity, Extent and Scale
Modeling environmental systems requires selection of a problem-speciﬁc set of pro-
cesses, that is — as mentioned above — albeit and subjective. This focus is deﬁned
by the problem to be solved. For example, studying climate change needs considera-
tion global temperature, atmospheric CO2 concentration, radiation, vapor etc. Within
this area processes like runoff, nutrient cycling in soil are neglected. However these
variables determine the process. More crucially, depending on the spatial resolution,
even clouds are described by a single parameter rather than a shadowed area.
The decision to exclude variables or processes from a model is based the modeler’s
experience, on expert knowledge: a variable may have an inﬂuence on the process
studied, but this inﬂuence may be considered to be small compared to the other
variables studied. Selecting variables for a process to be modeled deﬁnes a system
boundary. System boundaries are deﬁned in every modeling process. The important
topic environmentalistsare faced with is that environmentalsystems are opensystems.
Asystemboundaryisdeﬁnedonlybythemodelersandthescientistmustdecidewhich
variables are important and which not.
Based on this selection of components — variables, processes and parameters, a
precise deﬁnition will be given below — the conceptual model deﬁnes the scale
of applicability. Conceptual modeling is therefore the step of model development in
whichprocessesandtheirgranularityaredeﬁnedandcompartmentsareseparatedwith
respect to a speciﬁc problem-oriented scale. The question of scale of an ecological
model ﬁnds widespread discussion in recent literature (Wu & David, 2002; Turner
et al., 2001).
Scale itself refers to temporal aspects of model dynamics, called temporal scale, and
to the spatial scale. Temporal and spatial scale is determined by granularity or grain,
which denotes the ﬁnest level of spatial or temporal resolution of a model or a given
data set and the extent, which denotes the size of the study area or the duration of
time under consideration. Spatial and temporal scale depend on each other in terms
of modeling as well as in terms of data analysis: in general, one observes that if the
domain of a certain model with respect to spatial and temporal scale is displayed
within a diagram plotting spatial scale again temporal scale, model domains are
arranged along the bisectrix, cf. Figure 1.3. Turner et al. (2001) presented examples
for environmental disturbance regimes, biotic responses and vegetational patterns in
this framework, see also (Levin, 2000).
Temporal Scale
deﬁnes the time interval Δt or the characteristic time τ = 1/Δt
which are valid for most of the dynamic process of the model. In entirely linear models


8
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Spatial Scale
Temporal Scale
characteristic time [s]
Sec
Ecosphere
(global)
Regional
Landscape
Investigation
site
100
101
102
103
104
105
106
107
108
Min
Hour
Day
Month
Year
10-2
100
102
104
106
108
grain [m]
Lysimeter or
Laboratory
Averaging, Intro-
duction of effective
Parameters
Lower Level
Focal Level
Introduction of control
variables, forcing
functions, boundary
conditions etc.
Upper Level
Domains of
models
Fig. 1.3
Illustration of model domains with respect to temporal and spatial scales.
the characteristic times are given by the eigenvalues of the model systems. Eigen-
values are mostly used to analyze the general system behavior. There is an abundant
literature in theoretical ecology on this methodology,see (Jørgensen & Bendoricchio,
2001, p. 274). Table 1.2 summarizes a list of processes related to agricultural ecosys-
tems together with their characteristic times and the type of mathematical model used
for simulation.
All eigenvalues deﬁne the spectrum of the system or model. If this spectrum has
a wide range over several decades one speaks of a stiff system. This means, that
models include very slow as well as very fast processes. In terms of Figure 1.3,
the domain of the model would have a large horizontal extent. Stiff systems are
usually difﬁcult to solve numerically. Special procedures have to be applied (Hairer
& Wanner, 1980). Model development tools as discussed in Section 1.5 rarely offer
algorithms for dealing with stiffness. This is one of the reasons to focus on a speciﬁc
temporal scale. In Chapter 9 we will analyze environmental models with respect to
temporal scale and offer a methodology to group complex model by dynamics.
Spatial Scale
With the spatial scale we denote the spatial extent or the spatial
granularity that is chosen to develop a spatial model. At ﬁrst glance one can think
about the grid size in a grid based model or the average diameter of polygons in
a vector based model. On the other hand the spatial scale is related to the size of
the investigation area, for example an agricultural ﬁeld, a small catchment, a region
including large urbanized area or a continent or the world.
Spatially explicit modeling is always confronted with the question of how to handle,
store and manage spatially explicit data — as well as acquiring — the data. Managing


THE MODELING PROCESS
9
Table 1.2
Agroecological processes on different time scales and the modeling approaches.
Abbr.: ODE: ordinary differential equation; DAE: difference algebraic equation; DDE: delay
differential equation; PDE: partial differential equation.
Process
Variables
Characteristic time
Mathematical model
Growth of microbial
populations
Biomass,
Nitrogen
content, activity
30 minutes
ODE
Nitriﬁcation, denitriﬁ-
cation
NH+
4 , NO−
3 , N2O, N2,
microbial activity
1 day to 1 week
System of ODE
Degradation,
volatilization
of
agrochemicals
Concentration in liq-
uid and solute phase
Minutes to weeks
System of ODE
Populations dynamics
Density of eggs, juve-
niles, larvae, adults
Weeks to vegetation
periods
Matrix
equations,
DAE, DDE
Crop growth
Organ biomass, nitro-
gen content, leaf area
index
Month
(Systems of) ODE
Population
dynamics
of weed
Seed dispersal, cover-
age level
Vegetation period
DAE
Water transport in un-
saturated soil zone
Water content
1 hour
PDE
Solute transport in un-
saturated soil zone
Concentration in liq-
uid and solute phase
Large spectrum
PDE
coupled
with
ODE systems
Solute
transport
in
aquifer
Concentration in liq-
uid and solute phase
up to several years
PDE
coupled
with
ODE systems
spatiallyexplicitdatarequiresthechoiceofanappropriatedatamodel. Alltheseissues
will be discussed in Chapter 3.
Complexity
Characterization of the spatial or temporal scale is related to the deﬁ-
nition of a certain degree of complexity or simply complexity. Complexity of systems
systems are characterized by four topics (Wu & Marceau, 2002). Complex systems:
• are thermodynamically open, they exchange energy, mass or information with
their environment;
• are composed of a large number of of diverse components;
• have systems components that interact in a nonlinear way;
• exhibit a high degree of heterogeneity in time and space.
Integration of Scales
Wu & David (2002)emphasis a second importantproperty
of environmental models. When selecting a certain spatial and temporal scale — the
scale in this context is called the focal level — all related variables or processes from
other scales or levels are denoted by special icons. For example components from


10
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
the level above the focal level, e.g. the larger time or spatial scale, are denoted by
context, constraints, control, driving forces or boundary conditions.
Wu & David do not exemplify the same issue for levels below the focal level, consid-
ered scale, whereas Jørgensen & Bendoricchio (2001) distinguish between constraints
“from below” and “from above”. This is as important as the consideration of certain
boundary conditions. To answer the question, what are the components of the lower
level, we have to answer the question, what happened in system analysis when we
neglected a certain scale that was much too detailed? We decided to neglect certain
processes, as their temporal patterns do not inﬂuence the processes of the focal level.
In this case we have the ability to parameterize the process in a different way. Usually
a nonlinear function is introduced at the focal level. For example for degradation of
a pesticide the high speed process of an enzymatic reaction is unimportant, and we
can assume a nonlinear Michaelis–Menten kinetic, (Richter et al., 1996).
When modeling environmental processes, one has to be aware of following facts
related to scaling and levels:
• Notation of components changes through scales. A state variable of a large
temporal scale model can be a boundary condition or driving force in a small
temporal scale model. As scaling is frequently used with the task of integrating
the model from a different scale this is an important topic.
• In general it holds true that, the more one steps away from the bisecting line,
the less is the physical base of the model, the more phenomenological aspects
enter the model. Or, we move away from a white-box to a black-box model.
Scale therefore is also related to the distinction of black- and white-boxmodels.
• Therefore spatial and temporal aggregation helps us to neglect low level scales.
Mostly this aggregationleads to the incorporationof nonlinear processes in our
model.
1.2.3
Toolbox and Language: Mathematical Models
Notations and Deﬁnitions
Several notations have been used in the preceding
paragraphs. A precise deﬁnition will be given in the following. Conceptual models
consist of several components identiﬁed by their icons, cf. Figure 1.2. Although these
icons differ from one conceptionalizationmethod to another, all these components re-
late to certain mathematical elements. These are state variables, parameters, control
variables and mathematical equations.
Deﬁnition 1.2 (State Variables) All time- or space-dependent variables that are re-
quired to deﬁne the state of the system are denoted by ⃗x or ⃗X and are called state
variables. Dependency to location is denoted by ⃗x(⃗z). Time dependency is denoted
by ⃗x(t).


THE MODELING PROCESS
11
Thesetorvectorofstatevariablesisminimal,e.g.thevectorcollectsallthesevariables
that are necessary to derive the succeeding state of the system from the given state.
Variables that can be derived from the state variable by an explicit or implicit equation
do not belong to the state vector. These variables are called auxiliary or adjunct
variables or functions.
The starting point for a simulation run is deﬁned by a given set of state variables.
This setup is called the initial condition. If a time interval from t 0 to tend deﬁned
by t ∈[t0, tend] is considered, the vector with initial conditions shall be denoted by
⃗x0 = ⃗x(t0).
Spatial dependency of a dynamic system is introduced, if the state variables depend
on a location ⃗z. In this case a certain study area is considered. Let us denote a study
area or region by R. All locations are speciﬁed by location vectors ⃗z ∈R ⊂ 2,3.
Usually R is a subset of the two-dimensional Euclidean space. The border of the
study area is denoted by ∂R. Spatially explicit models are characterized by the fact
that state variables show a functional dependency from state variable from a different
— usually neighboring — location.
This raises the question of how to specify state variables that depend on the state
of locations that are outside the study area. For those variables x(⃗z) with ⃗z ∈∂R
boundary conditions are deﬁned.
Processes of a considered system are translated into mathematical equations. These
equations describe the exchange of information between the variables depending on
space and time.
Deﬁnition 1.3 (Mathematical Model) A dynamic model is deﬁned by a set of math-
ematical equations, summarized with in a model equation MΔt. The equation calcu-
lates a succeeding state ⃗x(t1) from an initial state ⃗x(t1) as a function of time t and
location ⃗z.
A spatially explicit dynamic system is speciﬁed by a model equation M t, an initial
condition ⃗x0 and sufﬁcient boundary conditions. A complete speciﬁcation of the
deﬁned mathematical equations requires the speciﬁcation of
Deﬁnition 1.4 (Coefﬁcients, Parameters) Parameters or coefﬁcients are constant,
e.g. not time-dependent, variables that specify mathematical functions. Parameters
may depend on the spatial location. In the aggregated vector notation of a model
system, we denote parameters by the vector ⃗c(⃗z).
The notations ⃗c or ⃗x for the vector of parameters or state variables are used if a
model is discussed in a general way with respect to its structure or its application
to different methodologies. In model development notations for the parameters are
used that imply the function or meaning of the parameter or state variable. There
is an abundant number of parameter notations, that have a more or less well-deﬁned
denotation or meaning, see Table 1.3. In general, parameters are notated by lower
case, (state) variables by upper case letters.


12
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Table 1.3
Some of the frequently used notations for state variables (upper part) and param-
eters (lower part of table) in environmental models.
Symbol
Denotation
P
Population
C
Concentration
Θ
Water content, Moisture
Ψ
Water pressure
T
Temperature
r
growth rate
F
Fertility, Fecundity
k, ka,b
exchange rates, from compartment a to b
ρ
bulk density
pi
transition probability, population dynamics modeling
With the choice of a relevant scale or level, certain components of the (open) envi-
ronmental system acquire a special meaning.
Deﬁnition 1.5 (Control Variables) Control variables or so-called forcing functions
denote variables that incorporate inﬂuence in to a model that are driven by processes
outside the model system boundary. These variables are to be deﬁned before running
a model. Control variables are ⃗u(t,⃗z) and depend on time and space.
The deﬁnition of the control variables is related to the deﬁnition of initial conditions
and boundary conditions. All these three items are to be deﬁned before running a
simulation. A common interpretation of control variables in environmental modeling
is the incorporation of anthropogenic inﬂuences into an ecological process. Differ-
ing parameterization of control variables deﬁne so-called scenarios, for a scenario
analysis. Within the scope of optimization control variables have a special meaning,
as these variables are estimated by special numerical procedures, see Part III.
1.2.4
Results: Computer Models
An adaptation from computer science and software engineering can illustrate the
steps of model development in Figure 1.4: The “Water ﬂow Model” summarizes the
steps of system analysis, conceptualization, mathematical modeling and the result of
a computer model. Running through these steps, different conceptualization methods
are involved.
The resulting step of translating conceptual or graphical models into mathematical
equations and solving these by the application of numerical algorithms leads to a
computer model. The computer model then consists of numerical codes for the
solution of initial value or initial boundary value problems.


THE MODELING PROCESS
13
System Analysis
Conceptual Model
Mathematical Model
Computer Model
Model Analysis
Graphical Representation
Model Application
Application of Numeric Procedures
Parameter Estimation
Translation
Word Models
Box Models
Feedback Dynamics
Computer Flow Charts
Picture Models
Steps supported by 
Model Development Tools
Fig. 1.4
An adaptation from computer science and software engendering: The “Water ﬂow
Model” clearly illustrates and summarizes the steps of model development in environmental
system analysis: Starting with system analysis, conceptualization, mathematical modeling one
derives a computer model. Several steps of model analysis may require us to step back and
reformulate the previous step.
In general,the methodology of translatingconceptual networks into equations is based
on setting up the adjacence matrix — the matrix model — derived from the topology
of the conceptual network. The matrix is then extended by parameters specifying the
arcs between the graphical elements. Depending on the model concept chosen (see
Figure 1.2) the resulting model consists of an equation system (input/outputmodel), a
time discrete, event-basedmodel (Petri nets) or ordinarydifferential equation systems
(box-model, feedback dynamics, energy ﬂow models).
A common way of computer modeling (Richter et al., 2001) is to start by designing
the computer algorithm directly. The starting point of a model like this is a computer
ﬂow chart. Jørgensen & Bendoricchio (2001) add this to conceptualization methods,
too. This is a common approach for rule-based models. The major difference from
the conceptualization methods discussed above is that a computer ﬂow chart deﬁnes
a well-determined sequence of events whereas, for example, energy models deﬁne
exchange rates of information and matter only. From this a sequence of computer
instructions is derived thereafter.
In all cases, the ﬁnal computer model is based on codes which are derived from math-
ematical models. Well-deﬁned mathematical problems such as the solution of initial
boundary value problems are a feasible starting point for simulation models, if the
underlying processes are amenable to a direct formulation in a mathematically closed
form. This is the case for most physical processes under controlled experimental
conditions.


14
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
In environmental systems, where physical, chemical, biological, economic and other
processes are interlocked at different scales and at different levels of complexity and
information quality, codes cannot be derived via mathematical models, although the
formulation of a general mathematical framework is still possible. In this case the
code is a direct implementation of the conceptual model. Frequently encountered
examples are grid-based models describing (mostly biological) spatial phenomena
e.g. the spread of forest ﬁres or of animal and plant populations, the migration of
non-endemic species, the spread of pests and diseases or of certain genotypes. The
latter example plays an important role in risk assessment of the spread of genetically
modiﬁed organisms.
1.3
MODEL ANALYSIS
Whenever a computer model is ﬁnalized and ready to use, the question of model
analysis arises. Two major issues are related to this topic. First, does the model cover
all model processes correctly? This question will lead us to tasks such as, veriﬁca-
tion, validation, model testing. Second, how does the model behave if parameters,
boundary conditions or initial values are speciﬁed from a domain that was not in the
scope of model development? Or, in a different formulation, what does a model tell
us in unknown situations? These may be either differing location or site condition,
future states or different management strategies, differing anthropogenic input. The
ﬁrst question aims at a model analysis focusing on intrinsic veriﬁcation, the second
on predictive power.
1.3.1
Veriﬁcation, Validation and Calibration
The use of the terms veriﬁcation,validation,conﬁrmation,and the goodness of models
is the subject of ongoing debate in the literature. Oreskes et al. (1994) derived an
explication of these terms from philosophy with special respect to environmental
models. The term veriﬁcation (from Latin, versus, meaning true) implies, that the
truth of a model has been proven. This implies the reliability of the model as a basis
for decision making. Understanding veriﬁcation within this scope of philosophical
logic, it is impossible to verify a model, as a model is per se a simpliﬁcation of reality
and the conditions under which a model need to be veriﬁed are inﬁnite.
The term veriﬁcation is also frequently used in terms of assessing numerical solutions
of mathematical equations. With increasing availability of development tools for
modeling, the underlying code of solving the derived equation system needs to be
tested, too. In this context the veriﬁcation of a numerically derived solution is done
by a comparison of an analytical solution — usually obtained only for a simpliﬁed
model — with the numerical solution.
In contrast to veriﬁcation, validation denotes the establishment of legitimacy. For
instance, a valid argument is one that does not contain obvious errors of logic,


MODEL ANALYSIS
15
cf. (Oreskes et al., 1994). By analogy, a validated model is internally consistent
and does not contain any ﬂaws.
The term calibration is used, if certain parameters of a model are unknown, and may
be derived only, if the model output is ﬁtted to real world data. The mathematical
problem of this task is parameter estimation. This precisely denotes a mathematical
procedure of identiﬁcation of parameter values based on experimental data using sta-
tistical methods. Calibration is usually used in a broader context. It also includes the
choice of parameter values according to literature data. What can be done, if neither
parameter estimations are possible, because ﬁeld data is insufﬁcient, and no literature
data is present? If the considered process is identiﬁed as an important part of the
modeled process, the only chance of continuing the model building process is to use
well-educated guesses. Within the framework of model analysis one must test care-
fully, how the model reacts on modiﬁcations of these arbitrarily chosen parameters,
cf. sensitivity analysis, model analysis, see below.
To continue with common denotation in literature the following can be found pretty
frequently: After a model is “calibrated” based on training data, the model is “val-
idated” comparing the model results with so far unused test data. If this step is
successful, the model is classiﬁed as “veriﬁed”. The outcome is that the terms of
the section heading are frequently used in recent literature, rarely with a well-deﬁned
explanation.
To cope with the task of model analysis and to answer the question which introduced
Section 1.3, we now consider intrinsic veriﬁcation.
1.3.2
Intrinsic Veriﬁcation and Predictive Power
The basic question of intrinsic veriﬁcation is: Are model equations and the numerical
methods correctly implemented?
One may derive an analytical solution of the mathematical model only for certain
usually simplifying conditions. However, this is still a complex task and computer
algebra systems may assist this step, see for instance Section 1.5.2. Care should be
taken with nonlinear models, as special dynamic patterns may be lost, if the model
is simpliﬁed too much. For these special cases comparison of numerical and analyt-
ical solutions yields benchmarks for goodness and correctness of the implemented
numerical methods.
There are different ways to answer the question if the model outcomes match our
(or some experts) prior knowledge of the system. If computer models are based
on mathematical formulations, one is able to analyze the mathematical structure
ﬁrst. This type of system analysis focuses on the general system behavior. General
properties of the dynamics system are analyzed, these are stationary points, or more
general topological invariants (Arrowsmith & Place, 1994). It shows the capability
of the model to describe processes which are qualitatively correct. This analysis may
only be possible for simpliﬁed versions of the model — similar to the derivation of an
analytical solution of the model. However, it is a worthwhile approach, as the derived


16
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
results are independent of parameter settings and allow a very general assessment and
description of the system. For complex systems, systems that aim to be close to real
systems, this approach is inappropriate.
Veriﬁcation procedures and assessment ofpredictive powerdependonthe information
available. If only expert knowledge is available the model can be analyzed using
scenario analysis. Scenario simulations are set up by a deﬁned set of input variables
which characterize certain conditions (drought vs. wet climatic conditions, limited
nutrients vs. sufﬁcient nutrients). This is comparable to the Gedankenexperiment
mentioned in Table 1.1. Using scenario analysis for intrinsic veriﬁcation as well as
assessing the predictive power the following recommendations are given:
• Crucial conditions as well as realistic conditions are recommended to test the
robustness and the applicability of the model.
• Scenario simulations can be characterized as hypothesis testing. The hypoth-
esis is that the model is capable of simulating certain situations known, and
extrapolates to unknown situations in an appropriate way. The outcome of this
type of scenario analysis is coarse. Either the simulations yield results expected
by experts or not.
• If possible,scenario parameterization shouldcoverthe entiredomainofa model
in terms of temporal and spatial scale, refer to Figure 1.3.
For this step of model analysis algorithms exist that test all possible hypotheses, that
are automatically generated from a knowledge base, which explain a lack of ﬁt. As
a result model parts are identiﬁed, which cause the differences of model output from
observations. Additionally, information on processes not included in the model is
identiﬁed. This analysis make use of the concept of qualitative reasoning (Struss
& Heller, 1998). Ecological modeling applications are presented for instance by
McIntosh (2003). This approach may be denoted as model veriﬁcation in the strong
deﬁnition given by Oreskes et al. (1994).
Results, acceptance and generality of model depend on the capability of the modeler
to deﬁne appropriate characteristic scenarios. As the number of parameters increases
with growing complexity of models, a sufﬁcient analysis of model behavior to ev-
ery parameter is hardly possible. Sensitivity analysis and Monte Carlo analysis are
methodologies that allow an automated generation of model runs. Model output
can be analyzed systematically based on predeﬁned intervals or distributions that de-
ﬁne the range of variation of parameters. Computational effort is high using these
methodologies if the number of parameters increases. However, if knowledge on
the distribution of parameters (Monte Carlo analysis) of parameter range (sensitivity
analysis) are known or can be assumed, these methodologies offer an automatically
estimation of model domain.
The predictive power can be analyzed by statistical tests if data from designed ex-
periments are available at an ordinal scale or at a metric scale. Cross-validation is
a widespread technique of model analysis in this case. This approach distinguishes


MODEL ANALYSIS
17
the steps of model calibration and assessment of predictive power. Two subsets of
the underlying data set are selected randomly. The ﬁrst subset is used for calibration
(e.g. parameter estimation, see below). Assessment of predictive power is performed
using the second subset. No changes are made to the model in this step. The results
are statistical measures that assess the predictive power of the model.
1.3.3
Uncertainty
One has to be aware of the fact that uncertainty is an intrinsic property of environ-
mental models, even if a model run through all steps of model analysis successfully.
Jørgensen & Bendoricchio (2001, p. 80) propose an uncertainty relationship for eco-
logical observations derived from Heisenberg’s Uncertainty Principle, which can be
applied to the energy balance of the world’s ecosystem. They conclude that uncer-
tainty cannot be avoided in principle in ecological studies. With a more theoretical
focus, Haag & Kaupenjohann (2001) discuss the aspects of model uncertainty in the
framework of philosophy of science. For practical purposes however, it is important
to know the origin of uncertainty and the related consequences and conclusions.
Beven et al. (2001) collected several sources of uncertainty: lack of knowledge of
the processes studied; lack of appropriate descriptive theories; errors in initial and
boundary conditions; errors in inputting forcing data and calibration data; the difﬁ-
culties in measuring the complex characteristics of the system at the scale of interest,
and the limitations of numerical algorithms and computational power.
From this we identify three general different aspects that determine the degree of
uncertainty of a model.
• Non-availability of data: Several steps in model deﬁnition and analysis require
data to obtain statistical measurements of model performance, such as residual
sum of squares (SQR), the correlation coefﬁcient (r 2) or model efﬁciency (EF),
(Loague & Green, 1991). Missing data or missing parameters lead to the
uncertain speciﬁcation of parts of the model, boundary or initial conditions.
When we are assessing uncertainty therefore, we must take into account the
uncertainty of the input data as well as the uncertainty of model parameters.
Well-known statistical tools such as analysis of variation can assess uncertainty
of data. Spatial data require geostatistical procedures. Uncertainty of model
parameters can be assessed for instance by Monte Carlo analysis.
• Choice of scale: As mentioned in Section 1.2.2, the selection of the processes
and the choice of theappropriate mathematicalformulationandthechosen scale
are arbitrary. Therefore, a speciﬁc selection of a certain mathematical notation
of the process of interest incorporates uncertainty. Especially if processes of the
level different from the focal level (see Figure 1.3) are to be incorporated into
the model, several possible choices of model structures may be available. This
is related to the question of uncertainty due to up- or down-scaling (Heuvelink,
1998).


18
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Anassessmentoftheuncertaintyofthemodelisperformedbydifferentmethod-
ologies. First, well-known Monte Carlo analysis and sensitivity analysis are
successful tools, cf. (Turner et al., 2001). Based on these concepts B ¨arlund &
Tattari (2001) used the tool UNCSAM to rank uncertainty of model parame-
ters. Beven et al. (2001) suggest comparing different models to identify the
correct model structure by applying the Generalised Likelihood Uncertainty
Estimation (GLUE).
• Algorithms: Finally, uncertainty of simulation results is increased by the un-
known error of numerical algorithms. Environmental models are very fre-
quently coded by complex mathematical equations that require the application
of one or more numerical procedures to obtain a solution. If possible one
should select numerical procedures that are capable of controlling the error
automatically, such as embedded Runge–Kutta formulae (RK) (Hairer et al.,
1980).
The three items above are inter-related. With a minimum of data or observations
available one cannot develop a complex model with a large number of processes
considered and a high degree of accuracy of the resulting simulation. The model is
over-parameterized.
1.3.4
Categories and Classiﬁcations
Modeling is a problem driven methodology. This implies, that a model does not only
depend on the selected spatial and temporal scale. The elements used for modeling
also depend on the considered problem and on the viewpoint of the problem. The
proceeding section summarized the methodology present for model development and
model analysis.
As an addition to this one can identify categories that are applied to environmen-
tal modeling for characterization and classiﬁcation of these models. Most of these
categories or classiﬁcations are derived from recent publications, see for instance
(Jørgensen & Bendoricchio, 2001). The most important classiﬁcations are summa-
rized in the following starting from simple mathematical properties aiming at more
general facts.
Autonomous vs. non-autonomous Models
are a classiﬁcation derived from
mathematical analysis. An equation can be denoted as autonomous, if the model
equation MΔt does explicitly not depend on the time t. This means for example for a
linear model of matter ﬂow, that reaction rates do not change with time.
Most of the more complex environmental models are non-autonomous, as basic pro-
cesses depend on time, either direct or indirect, making use of variables like daily
temperature, sun elevation etc. However, adding an adjunct variable
dx
dt = 1 with
x(0) = 0 and substituting t by x transforms any non-autonomous system into an
autonomous system. This classiﬁcation therefore is somewhat arbitrarry.


MODEL ANALYSIS
19
Static vs. Dynamic Models
Static models do not depend on time. These models
for example assess environmental parameters and derive variables or indicators im-
portant for further analysis. Habitat suitability models, which derive the probability
of existence of a certain species as a function of abiotic conditions, are examples of
these kinds of models.
Informationonthestaticorsteadystatebehaviorofthedynamicmodelcanbeobtained
by a stability analysis of a dynamic model. Information on stationary points with
attractive or non-attractive behavior is the result of this analysis.
Deterministic vs. Stochastic Models
Models entirely based on differential
equations, matrix equations or algebraic equations are denoted as deterministic mod-
els. If a model contains a stochastic element, a random variable, the model is called
stochastic. Monte Carlo simulation is a methodology that transforms a deterministic
model into a stochastic model using assumptions on the stochastic distribution of
selected model variables.
Distributed vs. Lumped Models
This classiﬁcation refers to the spatial scale
and the spatial granularity of a model. Spatial processes may either be described
by spatial distributed parameters and state variables, or one may identify so-called
effective parameters. Effective parameters are derived from averaging over a certain
spatial extent or domain (see support of model in Section 3.1.1). This is obtained
by identifying the spatial distribution of the parameters and the estimation of the
distribution function. A model that is based on effective parameters shows no spatial
dependence and is frequently called a lumped model.
Complex vs. Aggregated Models
Similar to the terms distributed and lumped
the terms complex and aggregated are used. However, these terms are used more
generally in literature and refer to temporal as well as to spatial scales. The meaning
ofthetermscomplexandaggregatedhaschangedthroughtheyearswiththeincreasing
computer power, the support by development tools for modeling, and the availability
of easy-to-use numerical algorithms.
Analytic vs. Numerical Models
The categories analytic and numeric are more
appropriate to characterize a model compared with the previous paragraph. An an-
alytic model focuses on the mathematical structure and the system behavior of the
developed model. It aims at presenting structures that are valid for a broad range of
applications and can be studied without ﬁnalizing the speciﬁcation of parameter to
deﬁned values. Well-known examples for these model types are the Lotka–Volterra
equation in lots of different speciﬁcations of predator–prey modeling or the most
sustainable yield problem for analyzing stability of harvest models, etc.
Numerical models require all parameters to be speciﬁed. These models are usually
discussed within a certain frameworkof application and aspects of validation, calibra-
tion and veriﬁcation (see above). In this context the chance of deriving an analytical


20
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
solution of a model equation may be discussed (Costanza et al., 1993; Hall, 1988).
With the available tools of model development and numerical solution of complex
equations, this discussion has disappeared from recent publications.
Research vs. Management Models
Management models aim at the applica-
tion of models, whereas research models aim at identiﬁcation of the environmental
processes. The idea behind this classiﬁcation is the observation that simulation mod-
els resulting from research projects are usually too complex, too large (and mostly
too poorly documented) to be applied to questions of management.
Biosphere vs. Anthroposhere
It is usual to distinguish between biosphere and
anthroposphere as domains of certain models. However, knowing that mankind takes
part in an ecosystem and mutuallydependson the ecologicalenvironment,the distinc-
tion between the two spheres seems to be overcome. In my opinion, this classiﬁcation
may remain valid in the future, for reasons of perception, even though we should aim
to overcome this anachronistic distinction. We should aim at an integrative rather
than an anthropocentric view of our problems, and the same applies to our method of
tackling the problem, the tool of modeling.
The difference of modeling a system from techosphere in comparison with an eco-
logical system is that for the technical system, in most cases a conceptual model was
present at the stage of building the system. For ecological systems the steps system
analysis, conceptual models and parameter estimation must be performed, to assess
if we know the system to a desired stage. One may argue, that even for a techni-
cal system, a system analysis is required to describe the system. The difference in
system dynamics is more general. Beddington (1981) noted that “there are no New-
tonian laws in ecology”. The following chapters will show that there is a multitude
of methodologies to describe an ecological process appropriately, but this is rarely
the case for technical systems.
The distinction between anthroposphere and biosphere is — besides the concept of
scaling in time and space — another reason for the introduction of control variables.
Control variables and forcing functions are frequently deﬁned by a system boundary
that separates of those two spheres.
Integrated Models
In this context the term integrated model appears in recent lit-
erature. Integrated models aim at overcoming this separation of different disciplines.
This means that these models aim at integration of anthropospheric as well as biotic
processes. These models try to integrate aspects from such disciplines as ecology,
economy and sociology. The system boundary of an integrated model is deﬁned by
the region studied rather than the processes of interest in the time scale.


LINKING REAL WORLD DATA AND MODELS
21
1.4
LINKING REAL WORLD DATA AND MODELS
The problem of applying an environmental model to a real world situation shows
a spatial and a temporal aspect. First, parameters and coefﬁcients that show a de-
pendency on spatial location — written as ⃗x0(⃗z) or ⃗c(⃗z), cp. Deﬁnition 1.2, 1.4 —
need to be set up. This implies the necessity of accessing spatially referenced data.
The problem is denoted by regionalization of a simulation model. Second, process
parameters must be identiﬁed: the dynamics of a model have to be identiﬁed. This
aspect is related to parameter estimation.
1.4.1
Regionalization: Applications to Investigation Sites and Spatial
Validity
Regionalization denotes the procedure of making a model depend on spatially dis-
tributed parameters or initial conditions. A methodology required to solve this task
is cartographic modeling usually performed with the framework of a Geographic
Information System (GIS), (Longley et al., 2001). First, cartographic modeling is a
tool in itself for processing spatial information, for instance creating new maps by
the combination of information of several layers. Second, cartographic modeling
is a tool for regionalization of local computer models by identifying basic spatial
units, which are characterized by homogeneous attributes. These units are called for
example elementary watersheds (hydrotopes) or elementary landscapes (ecotopes).
Before looking at different ways of regionalization,two different concepts of handling
spatial data must be summarized. Two general approaches exist for regionalization
of computer models using GIS.
• In the vector representation the boundary of any two-dimensional object is
described by a sequence of point coordinates, a polygon. Attributes of the
object are stored in a database.
• In raster systems the investigated area is set up by a regular grid of cells. For
each cell, a representative feature attribute is stored as code value.
An application of one concept or the other depends onthe task under consideration and
on the identiﬁed spatial area of validity — the support — of the model. The support
speciﬁes the spatial extent for which a model is assumed to be valid (Heuvelink,
1998). Initial conditions as well as set up of model parameters are constant for the
area of model support, a basic spatial unit.
The vector data approach is more ﬂexible and has more prerequisites to the function-
ality of GIS. With this approach one is able to determine the appropriate areas for
which a simulation model is valid. The GIS functions used are the intersection of a set
of information layers (e.g. habitat suitability maps as intersection of vegetation maps,
soil humidity maps and land use pattern maps), neighborhood analysis (computation
of slopes or aspect), network analysis (shortest routes), etc.


22
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
For a raster based regionalization approach the support of the model is equal to the
cell size. This data model has the advantage of a simple data structure. Additionally,
neighborhood relationships are easy to derive,as there is a distinct number of neighbor
cells. A cellular automaton (CA) has much in common with cartographic modeling
using a raster based data structure. The raster approach is suitable for use in chang-
ing landscape patterns. Changing patterns, time depending land use or vegetation
dynamics including migration processes can easily be implemented with the raster
approach, as this can be performed by changing grid cell attributes only. Modeling
the change of spatial patterns on the basis of vector data needs to dynamically change
geometry information, which is a difﬁcult task, and needs to modify the underlying
GIS database.
In this context it becomes obvious, that coupling a dynamic simulation model with
spatailly explicit data either for the speciﬁcation of the location dependentparameters
⃗c(⃗z) or location dependent initial conditions ⃗x0(⃗z) requires integration of a simulation
model into a GIS. One can distinguish different approaches for this task:
• A loose integration uses the GIS to compile a data-set including parameter
speciﬁcation and feed this into the model and to start several model runs for
every spatial unit;
• the integration of simulation functionality into a GIS;
• the integration of spatial data maintaining function into a model.
The ﬁrst item can be used only if the simulation model does not include any inter-
actions of processes between two models on different elementary landscapes. For
example lateral, horizontal ﬂow of matter and information, migration of species can-
not be described by this approach. It is appropriate only if the model support can be
identiﬁed in a way that there are no ﬂows across the boundary of the support. This is
for example the case in hydrological catchments. The time scale of the model must
be considered for this analysis, too. For example, lateral ﬂows can be neglected if
studying degradation of substances in soil, if degradation and vertical transport is fast
compared to lateral ﬂows.
Integration of simulation functionality with a GIS is very expensive in terms of de-
velopment costs. Some products can be found for distinct problems, such as ground
water modeling or atmospheric transportation of substances.
Spatially explicit models, that cover both dynamic and spatial processes including
ﬂow of information, matter or energy across the boundary of model support, are
usually set up by integrating GIS functionality into the model code. Additionally,
modelerschose the raster data format, as this needs less effortto handlespatial data, as
the topology of the raster data model is pretty simple. Chapter 3 focuses on spatially
explicit environmental models.


LINKING REAL WORLD DATA AND MODELS
23
1.4.2
Parameter Estimation
The crucial point in performing a realistic and convincing ecosystem simulation is
the information of basic model parameters. Often, it is difﬁcult even to assess the
correct order of magnitude of important parameters (Richter & S ¨ondgerath, 1990).
Parameter estimation is a synonym for statistical procedures to obtain reasonable
values for model parameters based on data. Dependent on the data available, different
methods of parameter estimation can be applied.
The classical approach of parameter estimation are regression methods (Draper &
Smith, 1966; Seber & Wild, 1989; Marsili-Libelli, 1992). With these methods pa-
rameter estimates are derived by minimizing the sum of squared deviations of model
predictions and data. Numerical algorithms for the simple case of a linear model, as
well as for nonlinear models, exist and are part of any statistical software package
such as SPSS or SAS. Regression techniques to determine parameter values from un-
derlying data are widely used (Kelpin et al., 2000)and are embedded in software tools
such as EASYFIT (Schittkowski, 1994) or MODELMAKER (Walker, 1997), even if
the ecosystem model is given in terms of (ordinary or partial) differential equations
with no explicit analytical solution. The goodness-of-ﬁt can be judged by looking
at the conﬁdence regions and correlation matrix. However, successful application
of regression techniques necessitates an appropriate experimental design. Measured
data and model structure must ﬁt together (Gubbins & Gilligan, 1996).
Other statistical approaches to obtain realistic parameter values are likelihood tech-
niques which are based on a distribution assumption, or Bayesian methods which
use some prior information (Foley, 2000). If there are no sufﬁcient data, no prior
information or if the model is not given in analytical form, other methods to obtain
parameter values must be used instead. In these cases so-called expert systems can be
derived. Current notations are also rule-based systems or knowledge-based systems
(Salski, 1992). Roughly speaking these are sets of “if-then” rules built up with the
help of practitioners or other experts. One example for gradient free optimization
methods, which can be used for parameter estimation on rule-based model systems,
are genetic algorithms (GA) (Wall, 1996).
If one is dealing with spatially explicit models additional problems arise with pa-
rameter estimation. This is because the number of parameters to be estimated for a
grid-basedmodel is proportionalto the numberof cells. Thereforemethods have been
developed to derive the model parameters from easy-to-determine cell properties e.g.
via transfer functions (Tietje & Tapkenhinrichs, 1993). In soil science this technique
is a common method to derive transport parameters from soil characteristics to avoid
a huge experimental effort. It is also used in connection with scaling up of process
models i.e. when applying process models to real landscapes.


24
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
1.5
MODELING LANGUAGES AND DEVELOPMENT PLATFORMS
1.5.1
Overview
Computer modeling is supported by a number of software packages, which sup-
port the previously described steps of model development from conceptual models
to computer code, see for instance (Walker, 1997; Hulbert et al., 2000; Heller &
Struss, 1997; Struss & Heller, 1998; Wolfram, 1999; Muetzelfeld & Massheder,
2003; Soetart et al., 2002; Lischke et al., 2002). These software tools allow a (semi)-
automatic translation from conceptual models to computer models, usually restricted
to a certain mathematical language (ordinary differential equations, Petri-Nets, etc.).
The use of development tools leads to the question, how to verify the software tool
used. The steps of model veriﬁcation described above are also valid for the ver-
iﬁcation of development tools. These tools consist of different functionality, like
translation of conceptual models into mathematical models, numerical solution of
differential equation system, analysis tools like sensitivity analysis or Monte Carlo
analysis. The performance of these software systems can be assessed based on mod-
els with well-known system behavior. Problems frequently encountered are: stiff
equation systems (Hairer et al., 1980; Hairer & Wanner, 1980), robust parameter
estimation (Schittkowski, 1994), mathematical heterogeneity.
Tools for computer modeling comprise one or more of the following functions:
• Graphicaldesignof a conceptualmodelwithin a graphicaluser interface (GUI);
• Speciﬁcation of compartments, deﬁnition of parameters, initial conditions;
• Deﬁnition and speciﬁcation of mathematical function;
• Translation of fully speciﬁed conceptual networkintoset of mathematical equa-
tions;
• Export of set of equation into computer code of high level language or into
meta-modeling language;
• Derivation of numerical solutions of derived mathematical equations, for in-
stance numerical solution of differential equations;
• Speciﬁcation of spatially referenced parameters by spatial databases, geo-
graphic information systems;
• Tools for visualization, plot of selected variables, plot of maps;
• Tools for model analysis, for instance sensitivity analysis, optimization, re-
peated runs, Monte Carlo analysis, parameter estimation.


MODELING LANGUAGES AND DEVELOPMENT PLATFORMS
25
Table 1.4
Comparison of model development tools. Part 1: General model development.
Name
MATHEMATICA
MATLAB
Company
Wolfram Research
The Mathwoks Inc.
URL
http://www.wolfram.com
http://www.mathwoks.com
Operating
System
Win, Mac, Unix
Unix, Win
Mathematics Large symbolic mathematics package,
large numerical packages, e.g. analytical
solutions of PDE, ODE, statistics
Large numerical mathematica toolbox,
e.g. ODE, matrix equations etc.
Numerics
ODE, PDE solvers, (adaptive, stiff sys-
tems)
ODE solvers, (adaptive, stiff systems)
Model
Analysis
several
several
Extendible
internal programming language, Math-
LINK interface
internal programming language
Graphical
Front end
yes
yes
1.5.2
Mathematical Languages
Mathematics offers a general language for describing and analyzing complex envi-
ronmental problems. Without a general language like mathematics it would hardly
be possible to analyze any of the recent environmental problems. Complexity of sys-
tems has increased in the recent decades. This was supported by the good availability
of mathematical and computer science support to environmental researchers. The
crucial point with this is, that a multitude of methodologies exists, that compile a
mathematical or computer model out of a conceptual model. So even if we identify
a consensus on a conceptual model, the mathematical translation can look entirely
different.
Let us examine some examples: for transport and reaction processes the mathematics
are ordinary or partial differential equations. If compartments are regarded as spa-
tially homogeneous, one is led to systems of ordinary differential equations. Another
class of models is based on stochastic processes. In the context of environmental
modeling, soil properties related to soil structure and soil composition determine
transport and reactivity parameters. Each of these properties can be regarded as real-
izations of stochastic random processes. Once the process is speciﬁed, for example
via a variogram, spatial realizations can be generated by a code (Deutsch & Journel,
1992; Cressie, 1991). All this leads to the problem of mathematical heterogeneity of
environmental models, and this will be discussed in detail in Chapter 4.
Concerning the step automatic translation of graphical systems in mathematical equa-
tions, most of the available development tools choose a certain mathematical dialect.
This means within a selected tool only time-discrete or matrix equations can be com-
piled, within another tool only systems ofordinarydifferential equations are generated
and a third tool might focus on event-based Petri nets.


26
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Table 1.5
Comparison of model development tools. Part 2: Development tools and envi-
ronments for spatially explicit models.
Name
FemLAB
SME
SIMILE
ICMS
Author,
organi-
zation,
company
The
Mathworks
Inc.
Thomas Maxwell,
Gund
Institute
of
Ecological
Economics,
Univ. Vermont
Simulistics
Ltd.,
Edinburgh
Tech-
nology
Transfer
Centre
CSIRO Land and
Water,
Integrated
Catchment Assess-
ment and Manage-
ment, ANU, Aus-
tralia
URL
http://www.
mathworks.
com
http://www.
uvm.edu/
giee/SME3
http://
simulistics.
com
http:
//www.cbr.
clw.csiro.
au/icms
Operating
system
Win, Unix
Unix, Linux
Win, Unix, Linux
Win
Mathematics PDE
regionalized ODE
ODE,
DAE,
Matrix,
object-
oriented
object
oriented
user code
Numerics
FEM
(adaptive,
stiff systems)
2nd order RK
1st order RK, Euler
—
Programming
language
within MATLAB
C++
C++
MICKL, C subset
Spatial
data
vector
raster
implicit by spatial
reference of mul-
tiple instances of
model objects
vector, raster
Graphical
front end
yes
optional,
model
development
by
STELLA etc.
yes
yes
This is a comprehensible way of restricting the required numerical procedures for
solving the system generated. However, this restriction to a certain mathematical
dialect often determines the ability of the modeler to describe a certain system. The
strength and the functionality of the modeling toolbox strongly determines our per-
ception of the system. The results of this issue is, that
• several models are developed, describing similar or even equal processes but
with different methodologies. Redundancy is increased (M ¨uller, 1997);
• it is hardly possible to deﬁne a general language for a meta-data environmental
model that is capable of describing and documenting environmental model in
general (Benz & Knorrenschild, 1997).
Therefore, mathematical models of environmental processes are mathematically het-
erogeneous, cf. Part II. In the following a brief overview of widespread development
tools is given, that supports the steps of model development discussed in this chapter.
Tables 1.4–1.6list some of the widespread tools used for developmentof environmen-
tal models, see also (Costanza & Voinov, 2001; Muetzelfeld & Massheder, 2003).


MODELING LANGUAGES AND DEVELOPMENT PLATFORMS
27
The table lists the program name, the company or institution responsible for main-
tenance and development and the related URL for further information. For detailed
discussion the underlyingmathematical dialect of the system is given, as well as some
comments on the extendability of the system. Note, this is a more or less subjective
choice based on the experiences of the author. There is much development in this
area, which leads to new inventions of development systems. Compare for instance
systems FEMME (Soetart et al., 2002), RAMSES (Lischke et al., 2002).
Adistinctionismadebetweenconceptualmodelingtoolsandprogrammingtools. The
former support a graphical representation of the considered processes and mostly
support an automatic translation of conceptual models into mathematical equation
systems. The latter support the steps of model development with a tool set of functions
that are helpful for environmental model development. In the following some of the
systems are described in more detail.
1.5.3
Generic Tools for Model Development
MATHEMATICA
was developed in 1986 by Stephen Wolfram. It is a general
symbolic and numeric solver, capable of performing a wide variety of mathematical
computations. It uses its own programming language, which makes it a very ﬂexible
solver. Its internal functions can also be called by external programs, and the data
outputcan be used by those programs. The MATHEMATICAprogramminglanguage
contains a rich set of commands, for solving calculus, algebra, differential equations,
linear algebra, and trigonometric problems. MATHEMATICA performs very well
as a differential equation solver for ODE as well as PDE, presenting solutions both
numerically, if available analytically and of course graphically. MATHEMATICA
has a wide variety of graphing capabilities, including 3D graphs and plots, which can
be exported to Postscript (PS or EPS) documents.
While this diversity makes MATHEMATICA a very comprehensive solver system,
it also makes MATHEMATICA a particularly difﬁcult program to use, requiring a
fairly long training period. As an aid in learning and using Mathematica, a number of
“notebooks” are included with the package. A “notebook” is a collection of MATH-
EMATICA commands, textual documentation concerning those commands, and any
data which might be used by those commands. It is the standard way MATHEMAT-
ICA organizes and saves a work session. MATHEMATICA also creates sub-groups
of functions within notebooks, allowing for more ﬂexibility in creating solutions. In
fact, ﬂexibility is the key word in describing Mathematica.
MATLAB
isexclusivelynumerical,withnosymbolicsolvingfeaturesincorporated.
It is geared very much toward engineering and scientiﬁc applications. It comes with
all necessary documentation, including many tutorial scripts and lessons. The main
features of MATLAB are a very powerful and rich numerical mathematics package,
and a relatively easy command syntax. For most applications, scripts can be written
which use the solver tools provided, many applications can be created by dragging


28
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
and linking appropriate icons, which represent MATLAB’s solver tools, to build the
necessary application.
1.5.4
Conceptual Modeling Tools
Tools for conceptual modeling are often called graphical modeling environments.
Systems like these have a long history starting from the ﬁrst works by Forrester
(1968) and Odum (1983). Recent developments encompass most of all functions for
model development as listed above and displayed in Figure 1.4. Some systems even
offer the functionality of model analysis and parameter estimation.
For the systems listed in Table 1.6 follows a short description.
EXTEND
is used for discrete-event, continuous and hybrid simulations. Features
of this system are the ability for the user to package up a sub-model with its own icon,
which can then be used as a higher-level component. This supports hierarchical and
modular model development.
MADONNA
This system is very similar to MODELMAKER and STELLA. It is a
system dynamics visual modeling package that generates very efﬁcient models based
on ODE systems.
MODELMAKER
is a visual simulation modeling package designed for scientists
and engineers (Walker, 1997). Based on system dynamics ODE systems can be
graphically designed. Models can be structured hierarchically with the deﬁnition of
sub-models. MODELMAKER offers — compared with the other systems listed in
this section — a good functionality concerning the analysis of the deﬁned model.
Monte Carlo analysis, sensitivity analysis as well as parameter estimation and model
optimization is implemented. Initial values of unknown model coefﬁcients for pa-
rameter estimation can be calculated using a genetic algorithm approach or by a grid
search strategy. Statistical documentation of a parameter estimation is profound,
including correlation matrices and standard deviation of the parameters as well as
statistical test.
POWERSIM
offers a range of tools for building simulation models based on the
system dynamics paradigm. The system is primarily aimed at the fast-growing busi-
ness, Web-oriented market.
STELLA
This is the best-established of the system dynamics visual modeling pack-
ages with a large number of users. STELLA offers a range of components in addition
to the standard “stock” symbol. Model analysis functions are limited. Function
for parameter estimation are missing. User-customizable interfaces are supported
(Hulbert et al., 2000).


MODELING LANGUAGES AND DEVELOPMENT PLATFORMS
29
VENSIM
Originally VENSIM was designed as a tool for running STELLA models
more efﬁciently. It is now a modeling package in its own right, combining causal
loop and system dynamics elements.
SIMULINK
MATLAB also comes with SIMULINK, which is a program for sim-
ulating dynamic systems. SIMULINK is graphic oriented, and the user can build
the dynamic system by dragging and linking the appropriate icons. In contrast to the
system dynamics platform, the icon concept in SIMULINK makes use of engineering
concept, such as integrations, differentiator, etc. The dynamic nature of SIMULINK
lends itself particularly well to solving differential equations systems.
FEMLAB
In contrast to all mentioned systems above,FEMLAB offers the ability to
setup models based on partial differential equations (Comsol AB, 2001). The required
ﬁnite-element meshes are automatically generated and the underlying geometries
may be imported from standard geometry ﬁles (DXF), for example exported from
a geographic information system. As FEMLAB is embedded into the MATLAB
framework, extendibility is given based on the programming facilities of MATLAB.
1.5.5
Modeling and Programming Environments
Restriction to a certain mathematical dialect requires us to code some part of an
environmental model within the framework of a high level programming language.
However, high-level programming languages (like C++ for instance) require speciﬁc
extensionsforenvironmentalmodeling. Forexample, themostfrequentextensionsre-
ﬂect the spatial localization of environmental processes and the connectionto database
system for parameters speciﬁcation. This is why most of the programming environ-
ments listed below support interactions and exchange with GIS. Several systems are
in development that aim either at an integration of different models or at an support of
spatially explicit model, see for instance the overviewby Woodburyet al. (2002). For
detailed discussion we focus on the Spatial Modelling Environment (SME), which is
used for the case studies in this book and Simile, former known as AME.
Spatial Modeling Environment
The Spatial Modeling Environment (SME) at-
tempts to address the conceptual and computational complexity barriers to spatio–
temporal model development. SME links icon-based graphical modeling environ-
ments with a generic object database (Costanza & Maxwell, 1991; Maxwell &
Costanza, 1997a). This system allows us to create and share modular, reusable model
components, and utilize advanced parallel computer architectures. The SME de-
sign has arisen from the need to support collaborative model development among a
large, distributed network of scientists involved in creating a global-scale ecological
and economic model. The system is designed to support a range of platforms, both
in the front-end development environment and in the back-end parallel computing
environment, cf. (Maxwell & Costanza, 1997a; Maxwell & Costanza, 1997b).


30
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Table 1.6
Comparison of model development tools. Part 3: Icon-based modeling environ-
ments with graphical front ends for conceptional models
Name
STELLA
POWERSIM
MODELMAKER
Company
High
Performance
Sys-
tems Inc.
POWERSIM
Cherwell Scientiﬁc
URL
http://www.
hps-inc.com
http://www.
powersim.com
http://www.
cherwell.com
Operating
system
Mac, Win
Win
Win
Mathematics ODE
ODE
ODE, DDE
Numerics
4th order RK
up to 4th order RK
Model
Analysis
Repeated runs, unit analy-
sis
Sensitivity analysis, opti-
mization, scenario man-
agement, unit analysis
Parameter
estimation,
Sensitivity analysis
Extendible
no
no
DDL programming
Simile
is a software environment for building and running simulation models in
ecology, biology, environmental science and related disciplines. It features a pow-
erful and expressive diagram-based language for designing models, including both
system dynamics and object-based concepts. Simile also supports modular model
construction, and modules can be nested to any depth.
The resulting models can be run very efﬁciently as compiled C programs, and deliv-
ered to others as stand-alone models. Simile provides a range of tools for displaying
model behavior but also allows you to add your own, customized to your own needs.
OneoftheaimsofSimiledevelopmentistoshowthatitispossibletoradicallyimprove
the way that modeling is undertaken within research programs, without restricting
the ability of researchers to design the models they want.
1.5.6
Numerical Mathematics
These development platforms offer a good functionality for developing and running
simulation models. With a graphical user interface several important functions are
hidden from the user. However, these functions are very important for an understand-
ing and correct assessment of the output derived. This section therefore sheds some
light on the underlying methodologies implemented in model the development tool.
Having identiﬁed the mathematical elements induced by the conceptual model to-
gether with the topology deﬁned by the conceptual network, two questions arise:
• How is a mathematical or computer model derived and (automatically) gener-
ated from the conceptual network?
• What mathematical procedures are required to perform a simulation based on
the derived equations and what is required to solve the model equations?


MODELING LANGUAGES AND DEVELOPMENT PLATFORMS
31
Table 1.6
cont.
Name
SIMULINK
EXTEND
VENSIM
Company
Mathworks
Image That! Inc.
Ventana System Inc.
URL
http://www.
mathworks.com
http://www.
imaginethatinc.
com
http://www.
vensim.com
Operating
system
Mac, Win, Unix
Mac, Win
Mac, Win
Math. lan-
guages
ODE
ODE
ODE
Numerics
see MATLAB
up to 4th order RK
Model
analysis
Optimization,
Monte
Carlo analysis, etc.
Monte
Carlo
analysis,
optimization,
sensitivity
analysis
Extendible
within MATLAB
yes
DLL programming
These two questions are related together, as the numerical procedures available for
the second item determine the methodology for translating a conceptual network into
a mathematical model. For a model run of the derived model one or more algorithms
related to the following numerical issues are required.
ODE Solutions
The most common way of performing a simulation of a model
based on a ordinary differential equation system is to apply a standard Runge–Kutta
method to the system, see (Hairer et al., 1980). Usually Runge–Kutta schemes up to
order of 4 or 5 of the classical Runge–Kutta formulae are chosen. Good ODE solvers
work with an embedded step size control, which aims at controlling the numerical
error by applying two ODE solvers to the same system and comparing the solutions.
If the solutions divergethe time step of the solution is decreased to limit the simulation
error.
High performancemodel developmentpackages additionallyanalyzethe dynamicsof
the model system and identify the stiffness of the system. Note, stiffness is a dynamic
property of the nonlinear systems. If stiffness is identiﬁed — a model incorporates
processes with a large range of characteristic time — special ODE solvers are applied,
e.g. GEAR or BDF scheme (Hairer & Wanner, 1980).
Implicit Equations
come up if the result of a function is at the same time an
argument of the same function. This type of equation is a typical outcome of ﬂow
networks, for instance recycling loops. Common model development platforms are
not capable of solving these equation (STELLA, MODELMAKER, MADONNA,
VENSIM). Iterative procedures, like regular–falsi or Newton are used to solve this
type of equation. As these are iterative procedures an appropriate starting value for
iteration is required (Stoer & Bulirsch, 1983).


32
FROM CONCEPTUAL MODELING TO COMPUTER SIMULATIONS
Matrix Equations
are usually solved by well-known procedure of numerical lin-
ear algebra. However, if the systems tend to be high-dimensional and the system
matrices are sparse, it is recommended that a high performance equation solver be
chosen that is capable of reducing error caused by ﬂoating point arithmetics.
Partial Differential Equations
In general partial differential equations are not
generated by translating conceptual models into mathematical equations if no spa-
tial dependencies of variables are deﬁned. These types of mathematical model are
the outcome of a spatial referencation of state variables. These models are highly
aggregated and incorporate a wide range of processes by a very limited set of param-
eters, cf. Chapter 3. Numerical solutions are derived by difference procedures, ﬁnite
element methods of line methods.
Eigenvalue Problems
Besides the foremost problems of estimating model so-
lution the task of model analysis is related to numerical problems, too. Eigenvalue
problems must be solved, if the dynamic properties of a model system are to be identi-
ﬁed. The results are used to assess system dynamics, perform a stability analysis and
calculate, for example, probability of species extinction (Stoer & Bulirsch, 1983).
Nonlinear Minimization or Maximization
Optimum Control or Optimization
Optimization or the special topic of time-
dependent control variables, optimum control aims at the identiﬁcation of a set of
control variables, that result in a desired system behavior. If the function is nonlinear
but analytically derived, we have a nonlinear optimization problem, which is solvable
by well-known Simplex or Levenberg–Marquardt algorithms (Press et al.,1988; Stoer
& Bulirsch, 1983). These procedures require at least a numerical approximation of
the derivative of the goal function to the control variables. If these are not available or
do not exist, derivative-freeprocedures like genetic algorithms may be an appropriate
choice, see (Wall, 1996).
Several well-tested procedures for solving optimum control problems are available.
These mostly focus on optimum control problems with underlying ODE for the dy-
namic system (Bulirsch et al., 1993; Bulirsch & Kraft, 1994).
Parameter Estimation
Optimizationintermsofcertainmodelparametersisacom-
mon feature of several model development tools, see tables. MODELMAKER offers
the functionality of parameter estimation based on well-known Levenberg–Marquardt
as well as Simplex algorithms, see (Press et al., 1988). The general concept of numer-
ically solving parameter estimation problems is to transform the given problem into
a general nonlinear programming problem using a Gauss–Newton and quasi-Newton
method. This is implemented in the algorithm DFNLP from Schittkowski (1983).
The remaining optimization problem is solved by a sequential quadratic program-
ming method (Schittkowski, 1980). These procedures calculate estimators for the
parameters as well as standard deviations and covariance matrices.


SUMMARY
33
More sophisticated algorithms that reﬂect on typical ecological problems such as
sparse data of spatially explicit processes are developedand discussed by Bock (1983)
(PARFIT) with applications in environmental fate modelingof pesticides byAltmann-
Dieses et al. (2002) as well as Schittkowski (1980) with the toolbox EASYFIT.
In ecological models set up by different mathematical elements or dialects, more
algorithms are presented for parameter estimation, that have fewer prerequisites on
the model structure. The methodologies make use of gradient-free optimization al-
gorithms such as genetic algorithmsq (Wang, 1997; Doherty, 1994).
1.6
SUMMARY
This chapter has given a general introduction to environmental modeling methodol-
ogy. Important concepts are introduced such as the water ﬂow concept for model
development (see Figure 1.4) and the general criteria for model analysis and model
performance assessment. These concepts are valid for a broad range of modeling
problems and are independent from the considered spatial or temporal scale, see
Figure 1.3.
The steps in the water ﬂow model are supported by several software tools that support
the development of environmental models. From this, two important conclusions can
be drawn.
First, it is neither necessary to start modeling from scratch nor to perform all the steps
of model development alone. That means development of environmental models
has to make use of existing approaches. Available models can be used or integrated
into a model that fulﬁlls our needs. This also means that, compared with former
documentations in ecological modeling, see for instance Jørgensen (1979), one does
not need to consider for instance, the programming language or platform the model
will be coded in. Abstraction to the mathematical formulation of the processes is a
tremendous success in modeling. This is supported be the increasing capability of
numerical algorithms in modern modeling platforms, see Section 1.5.
Second, even if modeling is supported by a broad range of tools, the material is still
needed. This material is given by a set of mathematical equations that describe the
most important environmentalprocesses. In this context the next two chapters present
a basic stock of important and frequently used models and modeling approaches for
environmental processes.


2
Environmental Models:
Dynamic Processes
2.1
INTRODUCTION
The main purpose of this chapter is to perform a system analysis of ecological pro-
cesses of a general ecosystem in terms of ﬂuxes of mass and information. The empha-
sis is on ecosystems with strong anthropogenic inﬂuences, for instance agricultural
ecosystems. Several examplesare given of possible translations of conceptualmodels
into mathematical equations with special respect to non-spatial dynamic processes.
We focus on the ﬁrst two trophic levels. The steps of model development as presented
in Chapter 1 are run through on the ﬁrst trophic levels of a general (agro)ecosystem
model. The ﬁrst trophic levels of the biotic sphere are analyzed in detail: interspeciﬁc
competition between weeds and agricultural crops, and populations of phytophagous
insects with age-structured population dynamics. Secondly, we focus on the mathe-
matical heterogeneity, an intrinsic property of ecological models based on the variety
of approaches capable of modeling the processes of interest. This is illustrated by
presenting different possible mathematical translations for one conceptual model for
selected processes.
2.2
FIRST TROPHIC LEVEL: PRIMARY PRODUCERS
Figure 2.1 shows a conceptual network of processes. This conceptual network focuses
on the processes. More general foodwebs and conceptual systems of agricultural
ecosystems can be found (Begon et al., 1986).
35


36
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Producers
Crops & Weed
Consumers
Inorganic
Nutrients
Pest
Control
Harvest
Crop
 Rotation
Bacteria
Mineral
Fertilizer
Consumers
Pesticide
Pesticide
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
CL(t)
CS(t)
A(t)
F(t)
Upper soil layer (root zone)
Metabolite
CM(t)
Fig. 2.1
Conceptual model of an agricultural ecosystem. The boxes denote compartments,
arrows denote general transport of mass, energy. Dashed arrows denote dependencies or ﬂow
of information. State and control variables are noted at the upper left corner of the compartment
boxes.
2.2.1
Crop Growth
Let W(t) denote the weight of the above ground biomass in [kg/ha] of a speciﬁc crop,
a primary producer, see Figure 2.1. We distinguish between crop biomass W C and
biomass of weeds WW. The literature for modeling crop growth is abundant. The
approach used here simulates crop growth in a single differential equation and covers
the processes of growth (parameter r in [1/d]), mortality (μ C in [1/d]) and senescence
(function fs(t)), cf. (Richter et al., 1991). f s is monotonically decreasing and equals
unity at t = 0. It incorporates the reduction in dry matter biomass during maturity
stages of crops into the model.
dWC
dt
=
rC fs(t) −μC WC
(2.1)
The parameter rC denotes the growth rate. The growth of a crop depends on the
support of nitrogen, the rate of photosynthesis and the interspeciﬁc competition of
weed or pests. All factors reduce a possible maximum growth rate r C,max [1/d]. These
inﬂuences are described by reducing functions r N(N), and rC,W(WC, WW), which are
normalized to one, if no reduction of the maximum growth rate takes place. The
reductions functions rN(N), rC,P(P4) ∈[0, 1] describe the dependence of growth on
soil nitrogen and a pest population P4, see below Section 2.6.2.


FIRST TROPHIC LEVEL: PRIMARY PRODUCERS
37
rC = rC,max
i
ri(⃗c) = rC,maxrN(N) rC,W(WC, WW) rC,P(P4)
(2.2)
The dependence of growth on nutrients is incorporatedinto the model via the function
rN(N). It is reasonable to use a Michaelis–Menten form (Richter et al., 1991).
rN(N) =
N
N + kN
(2.3)
N in [kg/ha] denotes the amount of applied fertilizer, k N in [kg/ha] the Michaelis–
Menten constant.
Two effects of competition must be considered. First a higher amount of weed reduces
crop growth. Second, the more crop biomass exists, the less inﬂuence on crop growth
under weed is observed. Growth reduction by weed decreases, the more crop biomass
is developed. This interaction can be incorporated into the model by the equation
rC,W(WC, WW) = 1 −
l WC
WW
s
(2.4)
with a shape parameter s [1] and a critical weed/crop relation l [1].
The possible extension concerns time and the physiological age of the crop. The
concept of biological time (Cabelguenne et al., 1999; Schr ¨oder & S¨ondgerath, 1995)
can be used to incorporate a physiological age, depending on daily temperature. The
biological time tbiol(t) substitutes the logical time t in the senescence function f s. This
is a consistent extension to the concept of a general senescence function as described
above, as tbiol increases monotonically which lets fs(t) decrease monotonically.
With a functional representation of the development rate r D(T) depending on the
temperature T(t) the biological time tbiol(t) is evaluated by
tbiol(t) =
t
0
rD(T(τ)) dτ
(2.5)
There are several mathematical functions which describe the nonlinear dependency
between temperature and development rate r D(T), for instance the O’Neill function,
see Section 2.4.2.
2.2.2
Temporal Patterns of Annual Plants
Annual plants show temporal patterns. For example,potato vine reaches its maximum
of growth between blossom and berry-development. With yellowing of the plant,
biomass starts to decrease continuously. With decreasing shading capacity weed
biomass increases sharply. As a driving process or function for these patterns certain
development stages have been identiﬁed. The temporal patterns are governed by


38
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
the function fs(t). It incorporates stages of senescence into the model where biomass
decreases. It is reasonable to postulate the following properties of this control function
i) fs(t) > 0 and lim
t→∞fs(t) = 0
ii) fs(t) may be normalized to unity, f s(0) = 1.
Consider as an example the function
fs(t) = (1 + ρ1) e−ρ2t
1 + ρ1e−ρ2t
(2.6)
The characteristic temporal pattern is governed by the function f s(t). Its shape is
deﬁned by ρ1 and ρ2.
The function fs(t) normalized by one and decreases in a
sigmoid manner. In Equation (2.6) f s(t) incorporates a growth phase (rP fs(t) > μW)
and a loss of biomass in a phase of senescence.
Phenological stages of development, for instance the beginning of the tillering phase
given by tDC in winter crops such as winter wheat or winter barley are described by
the function
fDC(t) =
0
if t < tDC
1
else
(2.7)
with tDC denoting the beginning of a speciﬁc stage of phase of development of a crop.
Note that fDC is predestined to be used as a function of biological time t biol as deﬁned
by Equation (2.5) rather than (system) time, cf. (Schr ¨oder & S¨ondgerath, 1995).
2.2.3
Nitrogen Uptake
The amount of nitrogen taken up by the crop is calculated using the reference content
of nitrogen in the crop biomass kcn(t) derived from unlimited nutrient availability
(Schr¨oder&Richter,1993). Thefunctionkcn(t)denotestherelativenitrogenreference
content in the crop biomass WC(t). During the vegetation period a decrease of nitrogen
content is observed. Therefore a function of the following form is used here
kcn(t) =
k1
if t < tDC
(kmax −k0)e−t−tDC
τ2
γc
−(kmax −k1)e−t−tDC
τ1
γc
+ k0
else
(2.8)
with ﬁnal relative nitrogen content in crop k0 [1], the relative nitrogen content in crop
in ﬁrst development stages k1 [1] and the maximum relative nitrogen content in crop
kmax [1]. The temporal patterns of this function are deﬁned by the development stages
of the crop (cf. Equation (2.7)) as well as the parameters τ 1, that specify the time of
maximum nitrogen content and τ2 that holds the time of highest decrease of nitrogen
content in crop. γc is a shape parameter of the function. The simpliﬁcation of this
ansatz kmax = k1 leads to sigmoid behavior. It becomes constant with kmax = k0 = k1.


PARAMETER ESTIMATION (PART I)
39
2.2.4
Interspeciﬁc Competition: Weeds and Weed Control
A growth model for weed must consider a whole population of weed species. A
practicable approach for weed development is the classical
dWW
dt
= rW WW
1 −WW
Kw
(2.9)
with the weed biomass WW [kg/ha], the speciﬁc growth rate rW [1/d] and the ca-
pacity KW [kg/ha]. Weed growth depends on the availability of nutrients, too. This
dependency can be incorporated into the model via the function of r N(N) (see Equa-
tion (2.11) with a speciﬁc Michaelis–Menten constant k N,W for weeds.
A further reduction factor is introduced for the competition for light. Weed growth
depends on the remaining photosynthetically-active radiation (PAR) on the ground,
which depends on the leaf biomass of the crop biomass. Therefore the growth rate of
weed is a product of a maximum growth rate r Q and the factor rQ(Q) which depends
on photosynthetically-active radiation denoted by Q in [W/m 2].
rW = rW,maxrQ(Q).
(2.10)
The less radiation that reaches the ground between the crop, the more reduction has
to be applied to the growth rate of weeds. This is applied by
rQ(Q) =
Q
Qmax
c
(2.11)
with shape parameters Qmax in [W/m2] and c [1] to the growth model of weeds. The
function for the photosynthetically-active radiation depending on the crop biomass
Q(WC) is deﬁned by a 2nd order polynomial interpolation based on the observed data.
Weed biomass is reduced by a factor pi at the time of weed control t∗. This reducing
factor can be identiﬁed as surviving possibility of a selected treatment i for weed
control. The application to the weed growth equation follows
WW(t∗+ Δt) = WW(t∗) pi
(2.12)
The coupled Equations (2.1) to (2.12) set up a simulation model for crop dynamics
including nutrient-dependent growth, temporal patterns of annual crops as well as
weed competition. See Section 2.7 for a summary of all model parts and Table 2.11
inthischapteronpage64, whichlistsallparametersintroducedandtheirphysiological
interpretation.
2.3
PARAMETER ESTIMATION (PART I)
Before continuing the translation of the conceptual model of an agricultural ecosys-
tem displayed in Figure 2.1, we ﬁrst analyze the model in hand and try to specify


40
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Fig. 2.2
Location of the study area “Neuenkirchen” of the Collaborative Research Project
“Water- and Matter Dynamics of Agroecosystems” and the investigation site “Scheyern” of
the Research Association for Agricultural Ecosystems Munich (FAM).
the parameters introduced. Most of the parameters are effective parameters of phe-
nomenological patterns rather than biological parameters which are derivable by cer-
tain physical measurements. We therefore use the technique of parameter estimation
based on ﬁeld experiments to specify these parameter values.
2.3.1
Experimental Design of Field Experiments
Data for the parameter estimation was derived from two different investigation sites
in Germany. The general methodology of measuring the above-ground biomass is:
plant development (crop and weed) was determined by cutting biomass above ground
and estimating ground coverage level every two to three weeks. Simultaneously, the
shading capacity of the canopy was measured as photosynthetically-active radiation
at ground level. Weeds were counted in deﬁned periods.
Investigation Site “Neuenkirchen”
Parameters of the simulation model are
speciﬁed using data series from the Collaborative Research Project “Water- and
Matter Dynamics in Agroecosystems” (CRP 179), project A2 “Modeling Crop Dy-
namics of Main Crops” of the Technical University of Braunschweig, Germany.
Field experiments were carried out at one of the investigation areas of the CRP 179
“Neuenkirchen”, located in the northern forelands of the Harz mountains in Lower
Saxony (Niedersachsen), Germany. This investigation area is about 16 km 2 in area.


PARAMETER ESTIMATION (PART I)
41
Soil parent material consists of a 1–2 m thick layer of loess topped by 0.2–1m col-
luvial sediments, see McVoy et al. (1995) for a more detailed site description of the
catchment. Figure 2.2 shows the location of this study area.
Investigation Site “FAM”
Figure 2.2 show the location of the investigation site
“Scheyern” of the Research Association for Agricultural Ecosystems Munich (FAM).
Within the scope of the research project ﬁeld trials on integrated weed management
have been carried out from 1993 to 1995. Besides chemical and mechanical treat-
ments, cultivation techniques that stimulate crop competitiveness were also included.
The ﬁeld trials were located in the “Terti¨arh¨ugelland” about 40 km north of Munich
on sandy loam soil about 450 m above sea level, see Figure 2.2. Climatic conditions
are characterized by 815 mm annual precipitation and an annual average temperature
of 7.4
. Through all investigation years, weed infestation reached medium levels
(about 27 weeds/m2 before the second earthing up). The majority of weeds belonged
to Polygonum- and Chenopodium species, typical for potato cultivation.
The potato variety “Selma” was cultivated with a fertilization rate of 60, 120 and
180 kg nitrogen per hectare [kg-N/ha]. Weed control was carried out as “chemical”
(common herbicide), “mechanical intensive” (rigid-tine-weeder and a second late
earthing up) and “mechanical extensive” (only a second late earthing up) treatment.
The experiment was laid out in a split-plot design with four repetitions and a plot size
of 27 m2.
Direct weed control by herbicide application reached an average efﬁcacy of 92%,
comparedto77%bymechanicalintensivetreatmentand52%bymechanicalextensive
treatment. Nevertheless, at medium and high fertilizer levels no signiﬁcant yield
differences occurred between mechanical extensive and chemical treatment, while
crop yield decreased by an average of 4% on the weedy, low fertilized plots. Even
if no visible damage occured on potato vine, the use of the rigid-tine-weeder caused
damage to roots and stolons of the potato plant. Therefore, yield decreased at all
fertilizer levels by 7.5% with mechanical intensive weed control. Based on these
results the following values for pi (i = 1, 2, 3) are determined: p1 = 0.0 (chemical
treatment), p2 = 0.25 (mechanical intensive treatment) and p3 = 0.54 (mechanical
extensive treatment), cmp. Equation (2.12).
2.3.2
Application of Algorithms
Some general remarks that hold true for all steps of parameter estimation presented
in the following should be noted. The nonlinear ordinary differential equation system
described has no analytical solution. Numerical procedures are used to solve the
differential equation system and to solve the parameter estimation problem 1, see
Sections 1.4.2 and 1.5.6 on page 32.
1Model development tools used in this chapter are MODELMAKER and EASYFIT.


42
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
winter barley
0
2000
4000
6000
8000
10000
12000
14000
0
50
100
150
200
250
300
[d]
N0
N4
0.0
0.5
1.0
1.5
2.0
2.5
0
50
100
150
200
250
300
N [%]
[d]
winter wheat
0
2000
4000
6000
8000
10000
12000
14000
0
50
100
150
200
250
[d]
N0
N4
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
50
100
150
200
250
N [%]
[d]
oats
0
2000
4000
6000
8000
10000
12000
14000
0
20
40
60
80
100
120
[d]
N0
N4
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
20
40
60
80
100
120
N [%]
[d]
Fig. 2.3
Growth curves of winter wheat, winter and spring barley, sugar beets, oats and oil
radish (non fertilized): measurement values (×, +) and results of models ﬁts. left: biomass of
N0 (no fertilization) and N4 (farmers usual fertilization). right: N-content of biomass in % of
the variant N4. Part 1: winter wheat, winter barley, oats.
For the analysis of the results a convenient and widely-used performance criterion of
the parameter estimation is used: the residual sum of squares r 2. From the statistical
analysis of the estimators, denoted by x in the tables, values for the standard deviation
σ can be obtained. The value is listed in round brackets in the tables. A large value
of the standard deviation indicates that the underlying data does not allow a statis-
tically sufﬁcient estimation of the parameter. This is also related to the correlation
coefﬁcients derived from the statistical analysis. These coefﬁcients are a suitable
measure for the (stochastic) correlation between two random variables. These are


PARAMETER ESTIMATION (PART I)
43
spring barley
0
2000
4000
6000
8000
10000
12000
14000
0
20
40
60
80 100 120 140
[d]
N0
N4
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
20
40
60
80
100 120 140
N [%]
[d]
sugar beet
0
5000
10000
15000
20000
25000
0
20 40 60 80 100120140160180
[d]
N0
N4
0.0
1.0
2.0
3.0
4.0
5.0
6.0
0
20 40 60 80 100120140160180
N [%]
[d]
oil radish
0
2000
4000
6000
8000
10000
0
20
40
60
80
100
120
[d]
0.0
0.5
1.0
1.5
2.0
2.5
3.0
3.5
0
20
40
60
80
100
120
N [%]
[d]
Fig. 2.3
contd. Part 2: spring barley, sugar beets and oil radish.
the unknown model parameters in terms of parameter estimation. Values close to ±1
indicate a strong dependence, whereas values close to zero indicate (stochastic) inde-
pendence. Strong dependence, correlation is an indicator for a over-parameterization
of the model, which may lead to misinterpretations of the results.
2.3.3
Parameters of Crop Growth
The results of model parameterization can be displayed only in summary without
lengthening the topic too much. Figure 2.3 summarizes the results of the parameter
estimation and Table 2.2 displays the results of the statistical analysis. Figure 2.4 and


44
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
0
2000
4000
6000
8000
10000
12000
0
20
40
60
80 100 120 140
[d]
0
20
40
60
80
100
0
20
40
60
80 100 120 140
[d]
Fig. 2.4
Growth curve of the biomass of ﬁeld beans (left) and nitrogen content in soil (right).
Table 2.1
Parameters of crop growth models. Fixed parameters (not estimated by parameter
estimation procedure) are printed in italics.
Crop
Sugar
Spring
Oats
Winter
Winter
Field
Oil
beet
barley
wheat
barley
beans
radish
Abbr. (α)
sub
spb
oa
ww
wb
fb
or
Parameter
W0
0.034
1.2
1.02
1.9
2.0
0.2
1.0
[100 kg/ha]
rmax = ρ2
0.0784
0.0615
0.0689
0.0709
0.0484
0.0682
0.0709
[1/d]
kN
3.41
5.0
5.178
1.643
6.28
0
1.0
[kg-N/ha]
ρ1
6930
227
251
154
205
590
256
[1]
μW
0
0.005
0
0.00732
0.005
0.002
0.0107
[1/d]
tDC
43.4
—
—
144
153
—
—
[d]
k0
0.937
0.698
1.08
1.39
1.22
2.85
0.657
N [%]
k1
5.12
5.54
4.98
5.02
1.54
k0
3.02
N [%]
kmax
k1
k1
k1
k1
2.84
k1
k1
N [%]
τ1
—
—
—
—
41.6
—
—
[d]
τ2
50.6
78.5
72.2
39.9
71.2
—
65.2
[d]
γc
1.5
3.0
3.0
3.0
3.0
—
3.0
[1]
r f
0
0
0
0
0
2.42
0
[kg-N/d]
kf
0
0
0
0
0
0.97
0
[dt/ha]
Fertil. N0
84
80
36
0
0
—
—
[kg-N/ha]
N4
108
130
126
216
171
—
—
[kg-N/ha]
Table 2.3 summarize results of the parameter estimation of the crop growth model
for ﬁeld beens including the sub-model of nitrogen ﬁxation, see next Section 2.4.1.
Note that the growth curves of different fertilizing schemes are ﬁtted simultaneously.
All parameter estimations show good results. The estimated values of standard devia-
tion are acceptably low and the correlation matrix shows that there are no correlations
among the parameters, see Table 2.2. This shows that the problemsare not ill-deﬁned.


PARAMETER ESTIMATION (PART I)
45
Table 2.2
Covariance matrix, estimator x and variance σ2 (level of signiﬁcance 5%) from
the parameter estimations of the crop growth model Equation (2.1) and nitrogen content model
Equation (2.8). All parameter values printed in italics are ﬁxed.
rmax
ρ1
tEC 21
μW
k1
t2
t1
kmax
= ρ2
tEC6
x
σ2
Sugar beet
kN
–0.26
–0.23
3.41
2.47
rmax
0.98
0.078
0.017
ρ1
6930
11700
μW
0.0
k0
–0.055
–0.82
0.49
0.937
0.14
k1
0.15
–0.43
5.12
0.073
t2
–0.82
50.6
5.19
tDC
43.4
2.94
Spring barley
kN
0.0186
0.0649
5.0
16.9
rmax
0.738
0.0615
0.0464
ρ1
227
476
tDC
0.0
μW
0.005
k0
0.174
–0.561
0.698
0.0563
k1
–0.585
5.54
0.0816
t2
78.5
1.44
Oats
kN
–0.653
–0.833
5.18
8.76
rmax
0.744
0.0689
0.029
ρ1
251
1930
tDC
0.0
μW
0.005
k0
0.286
–0.813
1.08
0.637
k1
–0.58
4.98
0.53
t2
72.2
11.7
Winter wheat
kN
0.51
–0.96
0.96
–0.24
1.64
8.02
rmax
–0.52
0.53
–0.63
0.071
0.013
ρ1
–0.99
0.25
154
3510
tEC
–0.25
144
328
μW
0.00732
0.0039
k0
0.11
–0.605
1.39
0.26
k1
–0.446
5.02
0.25
t2
39.9
3.52
Winter barley
kN
–0.12
–0.97
0.863
6.278
6.59
rmax
0.128
0.225
0.0484
0.0098
ρ1
–0.85
205
1000
tDC
152
70
μW
0.005
k0
–0.060
–0.19
–0.42
–0.015
1.22
1.18
k1
0.37
–0.63
–0.53
1.54
1.67
t2
–0.25
–0.95
71.2
191
t1
0.33
41.6
33.9
kmax
2.84
8.11


46
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.3
Covariance matrix, estimator x and variance σ2 (level of signiﬁcance 5%) from
the parameter estimations of the ﬁeld been growth and nitrogen ﬁxation model.
x (σ2)
ρ1
μW
k0
kf
rf
rmax
0.0682
(0.00146)
0.443
0.33
-0.513
-0.284
-0.306
ρ1
590
(109)
0.91
-0.276
0.103
0.0794
μW
0.002
(0.00129)
0.11
0.012
0.0169
k0
2.85
(0.23)
-0.05
0.0824
kf
0.965
(0.485)
0.927
rf
2.42
(0.211)
Table 2.4
Parameter estimation results of crop growth (parameter values, variance in paren-
theses, and correlation matrix).
x (σ2)
ρ1
kN
μW
rP,max = ρ2
0.142
(0.146 10−3)
-0.912
0.377
-0.412
ρ1
78.7
(4.68)
-0.187
0.694
kN
12.6
(0.371)
-0.219
μW
0.0109
(0.31 10−3)
2.3.4
Competition Models
A very convenientway of solving the problem of parameter estimation for the compe-
tition model is to solve the problem for sub-models or modules separately in several
steps. For detailed study the ﬁeld experiments on weed–potato competition from the
“FAM” investgation site are selected.
Step 1: Sub-model Potato Growth
Using the data sets of potato growth, which
grew up without any weed inﬂuence, under chemical based weed control, leads to
rC,W = 1. This uncouples the crop growth equation from the weed growth model and
enables a parameter estimation based on the data sets of the three different fertilizer
amounts.
The parameter estimation of the potato growth sub-model is based on the data series
of biomass weight and coverage under the chemical treatment in the year 1994. This
treatment results in undisturbed potato growth without weed infestation. Growth
parameters can be estimated without competition (rC,W = 1). Table 2.4 shows the
resulting parameter estimations together with the correlation matrix of the estimates.
Figure 2.5 displays a plot of the data together with the ﬁtted trajectories. The ﬁt is
satisfying as no estimates are correlated and the residual sum of squares results in
r2 = 0.97.


PARAMETER ESTIMATION (PART I)
47
0
1000
2000
3000
4000
5000
6000
0
20
40
60
80
100
120
[d]
chemical treatment
60
120
180
0
10
20
30
40
50
60
0
20
40
60
80
100
120
[d]
chemical treatment
60
120
180
0
1000
2000
3000
4000
5000
6000
0
20
40
60
80
100
120
[d]
mechanical extensive treatment
60
120
180
0
100
200
300
400
500
600
700
800
900
1000
0
20
40
60
80
100
120
[d]
mechanical extensive treatment
60
120
180
0
1000
2000
3000
4000
5000
6000
0
20
40
60
80
100
120
[d]
mechanical intensive treatment
60
120
180
0
500
1000
1500
2000
2500
0
20
40
60
80
100
120
[d]
mechanical intensive treatment
60
120
180
Fig. 2.5
Growth curves of potato biomass WC (left column) and weed biomass WW (right
column) for different treatments of weed control for 1994.


48
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.5
Parameter estimation results of weed growth (values, variance in parentheses, and
correlation matrix).
x (σ2)
c
Qmax
WW,0
0.0887
(0.0247)
0.963
0.921
c
2.85
(0.0807)
0.837
Qmax
29.0
(0.155)
rW,max
0.4
Step 2: Sub-model Weed Growth
In the second step of model developmentthe
parameters of weed growth are estimated. As stated before, weed growth depends on
remaining photosynthetically-active radiation reaching the ground, and this depends
on the standing biomass of potatoes. The reducing factor r Q (Equation (2.11)) is a
function of WC. The potato biomass determines the PAR for weed. This function
Q(WC) is derived by a 2nd order polynomial interpolation with the coefﬁcients b i
(i = 0, 1, 2). With a resulting r2 = 0.61, the parameters b0 = 30.8, b1 = −9.4 10−3
and b2 = 8.5 10−7 are identiﬁed.
The parameter estimation of the weed growth part of the model is based on the
mechanical extensive treatment. A higher weed infestation is observed here. Table
2.5 shows the resultant parameterestimationand correlationmatrix. This goodresults
are characterized by r2 = 0.79, acceptable correlations and still extremely small
standard deviations.
Sub-model Competition
The previous parameter ﬁts set up the basis for the es-
timation of the parameters l and s. The last step of model development incorporates
the inﬂuence of weed into the crop growth model. It closes the feedback-loop from
weed growth to the potato growth model. The parameter ﬁt is necessarily based on all
data-sets: chemical, mechanical extensive and intensive treatment incorporatedby the
surviving probabilities due to these treatments and fertilizing schemes. Growth pa-
rameters are not changed. Results of this parameterestimation are l = 0.821 (±0.107)
and s = 2.42 (±0.134). With a correlation of 0.91 between s and l. These ﬁnal results
are summarized by an acceptable correlation between l and s and a residual sum of
squares r2 = 0.81.
Final Step: Full Model Parameter Estimation
Finally a full parameter esti-
mation can be performed. It uses all the parameters identiﬁed before as initial values.
The approach can be summarized as stepwise identifying parameters of sub-models.
It is the only way for identifying parameters in a model like this. An estimation of all
parameters from scratch would lead to an ill-deﬁned problem, as the underlying data
does not fulﬁll the demands of parameter estimations of the full model. Using this
stepwise approach we avoided the task of solving an ill-deﬁned global optimization


PARAMETER ESTIMATION (PART I)
49
problem by setting up several local optimization problems that construct appropriate
starting values for the global optimization, see Chapter 8, Section 8.4.3 on page 170.
The process described in the previous steps may be continued in an iterative manner,
till a sufﬁcient result is achieved. The assessment of the goodness-of-ﬁt should not
solely be base on r2 values. A visual interpretation should emphasis the stages of
active growth of the canopy.
2.3.5
Results
Two general results are derived from parameter estimation. First, a capacity of dry
matter biomass has never been reached by ﬁeld experiments and K W cannot be identi-
ﬁed by means of parameter estimation. For this reason unlimited exponential growth
was used, to describe weed growth.
Second, parameter estimation shows no dependency on available nutrients in weed
growth. The introduction of a Michaelis–Menten function into Eqn (2.9) equally to
Equation (2.2) yields high correlations (±1) between the Michaelis–Menten coefﬁ-
cient and the maximum growth rate of weeds. The parameter estimation of k N,W
is not possible without correlations to other parameters. Therefore the inﬂuence of
fertilizing on weed growth is not signiﬁcant. However, in the ﬁeld experiments it was
observed that potato vine and shading capacity increased with higher doses of fertil-
ization. For this reason, weed infestation in highly fertilized plots was signiﬁcantly
lower, which is reproduced by the model.
Predictive Power
A major question, introduced in Chapter 1, is the question
of the predictive power of a model and the applicability to new conditions. Model
parameters were estimated based on data series from the experiments of the year
1993. To test the predictive power the model is applied to the data set of the year
1994. In this year no mechanical intensive treatment was carried out because of
weather conditions. Without any modiﬁcations to the parameter values the resultant
residual sum of squares r2 = 0.49.
The following parameters depend on site and climatic conditions: the maximum
growth rates, the parameterization of the senescence function, the initial weed infes-
tation, and the attrition rate. The statistical analysis has been performed as follows.
All parameters from the parameter estimation from year 1994 are used, and the pa-
rameters mentioned above are re-estimated. The results are shown in Table 2.6. The
table lists the ﬁnal parameters and the coefﬁcient of correlation which is a measure
of how precisely the algorithm of parameter estimation identiﬁes a parameter value
with respect to the underlying data.
This statistical analysis shows clearly that with the base of the data series from 1993
and 1994 no different parameter values can be estimated for r C,max, ρ1, ρ2 and μW,
see Table 2.6. Signiﬁcantly differences are identiﬁed in the parameters W W,0 and
rW,max. Both parameters are highly correlated. It shows that these different years
have a signiﬁcantly different initial weed infestation. This was observed during the


50
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.6
Statistical analysis of the simulation model focusing on the question of application
on different sites and years including the ﬁnal parameter sets.
1994
1993
Parameter
x (σ2)
x (σ2)
Signiﬁcant difference
ρ1
80.1
(15.3)
92.5
(15.4)
no
c
3.20
(0.293)
3.20
kN
11.5
(0.209)
11.5
l
0.358
(0.953)
0.358
μW
0.0112
(0.0227)
0.0141
(0.000362)
no
Qmax
28.5
(1.16)
28.5
ρ2
0.127
(0.00446)
0.127
(0.00403)
no
rC,max
0.139
(0.00177)
0.132
(0.00143)
no
rW,max
0.307
(0.0359)
0.176
(0.00332)
yes
s
1.68
(0.714)
1.68
WW,0
0.705
(0.580)
14.3
(1.313)
yes
experiments but no measurement values were taken before weed control. Figure 2.6
shows the simulation results.
Model Analysis and Application
A scenario: “What happens to crop growth,
or yield depending on different initial weed infestations?” can be answered by the
model. A simulation scenario is set up to answer that question. Assume different
initial weed infestation from 0.5% to 7.5% coverage level before weed control, given
by the initial condition WW,0. Figure 2.7 shows a plot of the estimated potato biomass
as a function of this initial weed infestation and fertilizer amount for the mechanical
extensivetreatment. Thissimulationscenarioclearlyshowstheinﬂuenceoffertilizing
to potato–weed competition. With a fertilizing level of 180 N–kg/ha no reduction of
yield can be found. This is caused by a quickly growing potato crop shadowing the
weeds. A yield reduction greater than 5% occurs with an initial weed infestation of
more than 8% with a fertilizing level of 120 kg–N/ha. A signiﬁcant loss of yield can
be found with the fertilizing level 60 kg–N/ha. These results of the simulation model
extrapolate the data observed in the ﬁeld experiments. This shows that sufﬁcient
fertilizing reduces weed infestation.
2.4
ABIOTIC ENVIRONMENT: WATER AND MATTER DYNAMICS
The second important part of the generic (agroecological) ecosystem model focuses
on the abiotic parameters and the related processes that determine the environmental
fate of nutrient and xenobiotica namely agrochemicals, pesticides.


ABIOTIC ENVIRONMENT: WATER AND MATTER DYNAMICS
51
0
500
1000
1500
2000
2500
3000
3500
4000
4500
0
20
40
60
80
100
120
[d]
chemical treatment
60
120
180
0
50
100
150
200
250
300
0
20
40
60
80
100
120
[d]
chemical treatment
60
120
180
0
500
1000
1500
2000
2500
3000
3500
4000
0
20
40
60
80
100
120
[d]
mechanical extensive treatment
60
120
180
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
0
20
40
60
80
100
120
[d]
mechanical extensive treatment
60
120
180
Fig. 2.6
Validation: Model application to data series of 1993. In this year no mechanical
intensive treatment occurred (WC(t) potato biomass, WW(t) weed biomass).
2.4.1
Nutrient Cycle: Detritus
The plant-accessible pool of mineral nitrogen in soil is denoted by N(t) in [kg/ha].
Plant growth depends on this pool. The simulation model couples the processes of
nitrogen uptake by plants, nitrogen leaching out of the root zone, decomposition,
mineralization, NO2 ﬁxation and fertilization.
dN
dt = −d(W, t) −klN + kmμWW + rf
W
W + k f
+ F(t)
(2.13)
The above-ground biomass may be deﬁned by either the crop biomass W = W C, the
weed biomass WW or the sum of both W = WW + WC. Leaching and mineralization
are modeled by linear ﬂows with the rates kl and km [1/d]. Fixation of NO2 is modeled
by a Michaelis–Menten function with the parameters r f [1/d] and k f [kg/ha]. The
demand of nitrogen taken up by the crop d(W, t) is calculated using the reference


52
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
50%
55%
60%
65%
70%
75%
80%
85%
90%
95%
100%
1%
2%
3%
4%
5%
6%
7%
8%
60 kg-N/ha
120 kg-N/ha
180 kg-N/ha
Potato biomass
relative to maximum
Initial weed infestation W0
Fig. 2.7
Simulation experiment: Expected relative biomass depending on weed infestation
observed at time of possible weed control and fertilization, to mechanical extensive treatment.
content of nitrogen in the crop biomass kcn(t) in [%] and is deﬁned by:
d(W, t) = d
dt kcn(t)W(t)
= kcn
dW
dt + dkcn
dt W
(2.14)
Decreasing biomass leads to negative values of d(W, t). This may be interpreted as
mineralization of dead biomass. This completely different process cannot be set up
by the same parameter of nitrogen uptake. Therefore d is restricted to be positive or
zero.
2.4.2
Xenobiotica Fate: Agrochemicals
The differential equations for the fate of agrochemicals are derived from the com-
partment scheme in Figure 2.1 with the assumption of linear ﬂuxes. Let C L denote
the concentration [mg/l] of a pesticide on the crops’ leaf and C S the concentration
[mg/l] in the upper soil layer. Precipitation is the driving force for transport from
leaf surface to soil surface (kw) and for leaching out of the upper soil horizon (k l).
Degradation of the chemicals is assumed as linear ﬁrst order process (k d).
dCL
dt
=
−kdCL −kwCL + ν(W)A(t)
(2.15)
dCS
dt
=
−kdCS + kwCL −klCS + (1 −ν(W))A(t)
(2.16)
The distribution of the amount of applied pesticide A(t) [mg/l] depends on the current
state of crop, on the leaf area index. The more leaf area is present, the more pesticide


PARAMETER ESTIMATION (PART II)
53
reaches the plant leaf. This is expressed by the function, cf. (Schr ¨oder et al., 1995)
ν(W) =
cLAIW
cLAIW + 1
(2.17)
Degradation or decay of chemicals in the environment is frequently a process that
depends on a broad range of environmental factors. Focusing on degradation in soil,
probably driven by microbial enzymes, depends on temperature T and humidity θ.
The following approach is frequently used for modeling this bifactorial dependency:
kd(T, θ) = kd,max kT(T) kθ(θ)
(2.18)
A maximum degradation rate kd,max is modiﬁed by two dimensionless factors that
range between zero and unity and describe the univariate dependency to temperature
kT(T) and soil moisture kθ(θ).
The classical form of temperature response curves is given by an Arrhenius temper-
ature dependence function. Since degradation is mediated by biological processes
at the level of micro-organisms and enzymes, it is evident that the Arrhenius law is
valid only in a conﬁned temperature range and should be replaced by a biological
temperature law, if larger temperature ranges are considered:
kT(T) =
Tmax −T
Tmax −Topt
β
exp
β Tmax −T
Tmax −Topt
(2.19)
However, since the shape of the curve at higher temperatures is determined by the
two parameters, optimal temperature topt and lethal temperature tmax, biologically
plausible values can be assigned to these parameters. The classical form of humidity
response curves is given according to Walker, see (Richter et al., 1996).
kθ(θ) = θa
(2.20)
It has also taken into account that degradation may decrease at water contents near
saturation, so a more general form of a response surface is considered which takes
into account both effects
kθ(θ) =
θ
θopt
a
exp
1 −
θ
θopt
a
(2.21)
2.5
PARAMETER ESTIMATION (PART II)
Identifying the parameters of the abiotic part of an ecosystem model has to make use
of parameters that are physically measurable at the investigation. In the context of the
model system developed, parameters of this type are the mineralization rate k m, the
leaching or percolation rate kl and the rate of runoff kw. These variables are highly
dynamic and dependon precipitation and micro-meteorologicaldata. These variables
are also highly variable in space. Methodology for estimation of those parameters are
presented in Chapter 3. For the moment we assume that effective parameter values,
and appropriate averages are available, cmp. Section 3.1.1.


54
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.7
Design of four slurry batch experiments for degradation studies of a pesticide.
Experiment
A
B
C
D
Moisture θ
80
40
60
40
[%]
Temperature T
5
10
15
30
[
]
Table 2.8
Statistical analysis of parameter estimation of pesticide degradation model.
x (σ2)
kd,max
A:CS,0
B:CS,0
C:CS,0
D:CS,0
Topt
kd,max
0.77 (0.042)
A:CS,0
88.8 (5.23)
0.228
B:CS,0
62.3 (3.69)
0.0743
0.102
C:CS,0
90.5 (5.56)
-0.0189
0.0458
0.0914
D:CS,0
81 (6.2)
0.244
0.00702
0.00331
0.0256
Topt
37.8 (0.41)
0.909
0.288
0.120
-0.0236
-0.0825
β
1.17 (0.11)
-0.849
-0.3132
-0.161
-0.00581
-0.0417
-0.987
a
0.3
Tmax
45
2.5.1
Laboratory Experiments
As an example for the estimation of parameters of abiotic processes, the degradation
of a pesticide is selected for detailed study. Degradation of the pesticide Idosulferon
is studied as a function of temperature and moisture. A two-factorial laboratory ex-
periment was set up. Table 2.7 lists the conﬁguration of temperature T i and moisture
θj used for the degradation study. The underlying degradation studies using Iodosul-
furon have been published elsewhere (Schraut, 2001). Temperature and humidity
response curves of the degradation rate can be identiﬁed from data of degradation
studies performed under different combinations of temperature T i and moisture θ j
conditions. For several other examples the reader is referred to Richter et al. (1996)
as well as (Diekkr¨uger et al., 1995; Formsgaard, 1997; Vink et al., 1994; Novozhilov
et al., 1995) and a general overview in (Richter, 1998).
2.5.2
Results
The simulation of the degradation curves assumes a linear ﬁrst order degradation, as
modeled by parameter kd in Equation (2.16), with a degradationcoefﬁcient dependent
on temperature and moisture from Equation (2.18). For temperature dependence the
O‘Neill approach according to Equation (2.19) is chosen.
Moisture dependence
follows the approach by Walker in Equation (2.20).
Basedonthefourdataseries(A,B,C,D)fromthelaboratoryexperiment, theunknown
coefﬁcients kd,max, a, β, Topt and Tmax are to be identiﬁed by a multi-experiment


HIGHER TROPHIC LEVELS: CONSUMERS OR PEST INFESTATION
55
Fig. 2.8
Temperature and humidity response function kd(T, θ) of Idosulforon.
regression analysis. The parameter estimation shows high correlations between the
parameters determining the nonlinearities in the model: a, β and k 0. This problem
can be solved by ﬁxing one of the parameters a or β. Setting parameter a = 0.3 an
acceptable parameter estimation can be performed. Table 2.8 documents these results.
The underlying data is insufﬁcient for signiﬁcant identiﬁcation of more parameters.
Figure 2.8 shows the response surface for Iodosulfuronderived from the two-factorial
degradation study displayed in Figure 2.9. Note, Figure 2.9 use a semi-log scale
that transforms the exponential decay curves into straight lines. The correlation of
modeled and measured data is very good with r 2 = 0.92.
2.6
HIGHER TROPHIC LEVELS: CONSUMERS OR PEST INFESTATION
Modeling processes of higher trophic levels is related to the broad ﬁeld of popula-
tion dynamics modeling. With respect to our goal of setting up an (agro)ecosystem
model we focus on examples of population dynamics modeling of the ﬁrst trophic
levels. More examples will be presented in the following chapters. In the context of
agroecosystems the population dynamics of powdery mildew and a sugar beet cyst
nematode will be analyzed.
2.6.1
Continuous Population Dynamics
An example of a pest is powdery mildew (Erysiphe graminis) which is both simple
and aggregated. This population develops in distinct stages. However, we assume
0
10
20
30
Temperature
0
0.2
0.4
0.6
0.8
1
Water content
0
0.1
0.2
0.3
k
0
10
20
30
Temperature


56
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
0
10
20
30
40
50
time [d]
1
10
100
Substance  [µg/kg]
A
B
C
D
Fig. 2.9
Semi-log plot of degradation curves for Idosulforon obtained under different com-
binations of the factors temperature and humidity.
that we have no knowledge about the division into different stages, and assume a
model for the entire population P in terms of a differential equation. Population
growth depends of the ability to extract biomass from the host.
dP
dt = rP,max
W
W + kP
P −μPP −μPrP,C (CL)CLP
(2.22)
Growth of the pest population depends on the available crop biomass using a function
of Michaelis–Menten type. The parameter kP [kg/ha] denotes the amount of biomass
required to attain 50% of the maximum growth rate r P,max [1/d]. The parameters of
degradation are introduced. μP speciﬁes the natural mortality of the population in
[1/d] and μC the mortality due to pesticide application. The latter depends on a critical
pesticide concentration on the leaf, Ccrit in [mg/m2] using a nonlinear dose–response
function
rP,C(CL) = 1 −exp
−
CL
Ccrit
2
(2.23)
Besides the modiﬁcation of a maximum growth rate of crop, see Equation (2.2), a
ﬂow of matter or energy from the hosting crop to the pest is an appropriate approach
for modeling the inﬂuence of a pest on a crop. For powdery mildew we follow this
approach and modify Equation (2.1) by another sink
dW
dt = · · · −γ
W
W + kp
P
(2.24)
γ can be interpreted as an efﬁciency parameter and speciﬁes the fraction of biomass
needed for population growth.


HIGHER TROPHIC LEVELS: CONSUMERS OR PEST INFESTATION
57
2.6.2
Age-structured Populations
Model Development
Pest population modeling is a very good example of mathe-
maticalheterogeneityinecologicalmodeling. Theﬁrstpopulationofpowderymildew
showed very fast exponential growth in one year and must be controlled by pesticide
applications. In this second example a matrix model is set up. The second pest pop-
ulation considered shows a slow population dynamic, about one to three generations
per vegetation period. A population like this must be taken into account in crop
rotation design.
An example for this type of pest population is the sugar beet cyst nematode Het-
erodera schachtii population ⃗P(ti). This population develops in distinct stages. For
H. schachtiithe stages: eggs and juveniles(P1), hatchedlarvae (P2), penetratedlarvae
(P3) and adults (P4) are distinguished. The population grows with the fertility F 0 of
the individuals in the adult stage. This approach leads to a matrix-equation based on
a Leslie matrix (Richter et al., 1991; Schmidt et al., 1993):
⃗P(ti+1) =
ps
0
0
F0
ph
0
0
0
0
pp
0
0
0
0
pd
0
⃗P(ti)
(2.25)
Schmidt et al. (1993) deﬁne the following transition probabilities for hatching p h,
penetration pp and adult development pd
ph(ϑh, j)
=
ph0
j
1 −e−ϑh
(2.26)
pp(ϑpd f, ϑh, P2, j)
=
pp0ϑpd f exp
−
P2
ϑpd f Dp
γp
(2.27)
pd(ϑpd f, ϑh, P3, j)
=
pd0ϑpd f exp
−
P3
ϑpd f Dd
γd
(2.28)
with the maximum probabilities for hatching p h0, penetration pp0 and adult develop-
ment pd0 [1] and the critical density for penetration D p and adult development Dd in
[e.+j./100 g]. P1 [e.+j./100 g] holds the number of eggs and juveniles per 100 g soil
and j denotes the current generation of the year. The parameters γ p, γd deﬁne the
shape of the nonlinear functions.
From an agricultural point of view P1, the number of eggs and juveniles in a unit soil in
spring is decisive in determining potential crop damage. The adults P 4 inﬂuence crop
growth of sugar beets, see Equation (2.2). This is modeled by an additional reducing
factor of the maximum growth rate rC,max. If the crop sugar beets are planted on the
ﬁeld the function
rC,P(P4) = r0
e−γ1(P4−Pr)2 −e−γ1P2
r
+ (1 + r1)e−γ2P4
1 + r1e−γ2P4
(2.29)
modiﬁes the maximum growth rates of the crop, with the factor of growth stimulation
r0 [1], the number of adults for growth stimulation P r in number of larvae per 100 g


58
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.9
List of parameters for speciﬁcation of crop-dependent host suitability.
Crop
Sugar
Spring
Oats
Winter
Winter-
Field
Oil
beet
barley
wheat
barley
beans
radish
Abbr. (α)
sub
spb
oa
ww
wb
fb
or
ϑh
1.0
0.54
0.55
0.47
0.44
0.39
0.048
[1]
ϑz
ϑh
ϑh
ϑh
ϑh
ϑh
ϑh
0.87
[1]
γa
0
0
0
0
0
0
1.36
[1]
γb
0
0
0
0
0
0
-0.56
[1]
Pr
14.6
—
—
—
—
—
—
[e.+j./100 g]
r0
0.146
—
—
—
—
—
—
[1]
γ1
0.0164
0
0
0
0
0
0
[1]
r1
59.5
0
0
0
0
0
0
[1]
γ2
0.0261
—
—
—
—
—
—
[1]
soil and shape parameters r1, γ1 and γ2 [1]. The function equals unity for P4 = 0.
Slight pest infestations stimulate crop growth (Schmidt et al., 1993). For small values
of P4 the ﬁrst term of the function models an increase of crop growth by r C,P(P4) > 1,
higher values lead to a sigmoid decrease to zero.
All development stages of the nematode are inﬂuenced by the host, too. The param-
eters ϑpd f and ϑh for each development stage describe the potential suitability, as
a host, of a crop. For sugar beet the parameter is arbitrarily set to 1, and all other
crops or non-hosts are related to the sugar beet. For special crops, such as oil radish,
Schmidt et al.(1993) calculates different values of ϑ pd f and ϑh for the distinct stages
by
ϑpd f = ϑz10γaPk(ti)γb (k = 2, 3)
(2.30)
with the suitability parameterϑz and two additionalshape parametersγa and γb. Table
2.9 list the crop-dependent parameters, see (Schmidt et al., 1993).
The number of eggs and juveniles in a unit of soil P 1(ti) in spring is decisive in deter-
mining potential crop damage. The variable P 1(ti+1) depends upon the development
of the population in the previous year:
P1(ti+1) = P1(ti)pov
G(ti)
j=1
F0ϑpd f(ti)phpp(j)pd(j) + ps(1 −ph(j))
(2.31)
with number of generations G(ti) in year i and the probability of over-wintering p ov.
The number of generations G is determined by the overall environment conditions in
a particular growing season ti. The model is coupled to the crop growth model by the
population of adult H. schachtii in the soil.
Model Analysis
Modelparametersarederivedfromaformerpublication(Schmidt
et al., 1993). Table 2.10 lists all parameters for the population dynamic model. This
model is a very good example for demonstrating dynamic properties. There is no


HIGHER TROPHIC LEVELS: CONSUMERS OR PEST INFESTATION
59
Table 2.10
Summary of model parameters of the population dynamic model for H. schachtii.
Parameter
Value
Probability of over wintering
pov = 0.6
Survival probability
ps = 0.9
Hatch probability
ph0 = 0.8
Penetration probability
pd0 = 0.7
Probability of adult development
pd0 = 0.4
Fertility
F0 = 10 [e. + j./100 g]
Critical density for penetration
Dp = 2500 [e. + j./100 g]
Critical density for adult development
Dd = 800 [e. + j./100 g]
Shape parameters
γp = 4.0
γd = 2.5
knowledge on system behavior for this model. No parameter estimation can be per-
formed. No information on the goodness-of-ﬁt or the correlation between model
parameters can be derived from this step of model development. Therefore this is
an excellent example to analyze the system with respect to dynamic behavior in the
framework of a sensitivity analysis. For detailed study the parameter ϑ h is chosen.
Figure 2.10 displays the asymptotic behavior of the population dynamics of referring
to the number of eggs and juveniles in 100g soil. This so-called Ljapunov diagram
displays the state of the variable after large number of iterations, e.g. a large number
of generations G as a function of the host-crop suitability coefﬁcient ϑ h.
0
1000
2000
3000
4000
5000
6000
7000
8000
9000
10000
0
0.2
0.4
0.6
0.8
1
1.2
1.4
Fig. 2.10
Ljapunov diagram of asymptotic behavior of the population of eggs and juveniles
in 100 g soil as a function of the parameter determining the host crop suitability ϑh.


60
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
2.6.3
Excursus: Types of Population Dynamic Models
Population dynamic modeling is an important aspect of ecological and environmental
modeling. Matrix models are only one possible methodology, frequently used for
clearly age-structured populations. However, for populations that show distinct age
structure less clearly, different mathematical approaches are available. The following
short excursus summarizes two additional mathematical approaches.
Partial Differential Equations
We consider a population P(a, t) which depends
on time t ≥0 with an age or length a ∈[0, A].
Together with the partial differential equation according to McKendrick and Foerster
for age-structured population dynamics (Henson, 1999) this leads to the following
general equation
∂P
∂t + ∂P
∂a = −f(a, P,⃗z)P.
(2.32)
The function f(t, a,⃗z) ≥0 contains the per capita death rate due to different processes
like mortality, harvesting or interspeciﬁc cannibalism.
The initial condition
P(0, a,⃗z) = P0(a)
speciﬁes an initial age-structured population. The boundary condition
P(t, 0) = r
A
 0
F(a)P(t, a) da
speciﬁes the growth of the population P. r denotes the per capita growth rate, which
may depend on the location⃗z. F(a) denotes the fertility at age a. Section 3.2.2 (p. 76)
discusses application of population dynamics modeling based on PDE.
Delay Differential Equations
According to Kuang (1993) the application of
delay-differential equations in population dynamics dates back to the 1920s, when
Volterra (1927) investigated the well-known predator–prey model. It was only in
the last three decades however that a greater interest in the mathematics of delay-
differential equations and their application in the context of population dynamics and
other areas of mathematical biology have arisen (MacDonald, 1989; Diekmann et al.,
1995).
Delay-differential equations have shown their usefulness in formulating population
models for species with well-deﬁned physiological stages, see for example (Gurney
et al., 1983; Nisbet & Gurney, 1983; Tuljapurkar& Caswell, 1997; Apel et al., 2003).
To illustrate how the introduction of time delays into the regulatory mechanisms of
population dynamics is achieved through their stage structure, let us assume a simple
stage-structured model of a closed population with only two stages, juveniles N J and


HIGHER TROPHIC LEVELS: CONSUMERS OR PEST INFESTATION
61
adults NA. The ﬁrst step is to formulate the balance equations, which are
dNA
dt
=
RA(t) −DA(t)
dNJ
dt
=
RJ(t) −MJ(t) −DJ(t)
 





(2.33)
with RJ(t) and RA(t) being the respective recruitmentrates, D J(t) and DA(t) the respec-
tive total death rates and MJ(t) the total maturation rate from the juvenile stage at time
t. This maturation rate M j(t) is equal to the recruitment rate of the adult population
RA(t), MJ(t) = RA(t). The following model functions deﬁne the rate processes
DA(t)
=
µANA(t)
DJ(t)
=
µJNJ(t)
RJ(t)
=
βNA(t)
 

(2.34)
µJ and µA are the per capita death rates and β the fecundity.
Note that the maturation rate fromthe juvenile stage at time tis equal to the recruitment
rate of the same stage but at the earlier time t −τ. This is the important step, which
will guide us to a delay-differential equation. The maturation rate from the juvenile
stage M j(t) is equal to the number of matured juveniles, in mathematical terms:
MJ(t) = RJ(t −τ)e−µJτ = βNA(t −τ)e−µJτ
(2.35)
Consequently τ deﬁnes the duration of the juvenile stage. System (2.33) can now be
rewritten as follows:
dNA
dt
=
βNA(t −τ)e−µJτ −µANA(t)
dNJ
dt
=
βNA(t) −βNA(t −τ)e−µJτ −µJNJ(t)
 





(2.36)
In this form it becomes obvious that Equations (2.36) are delay-differentialequations.
The rate of change of NA at any time t depends on its current state as well as on its
state at time t −τ. Equations (2.36) are of ﬁrst order and linear. Besides the initial
conditions, those kinds of equation require the deﬁnition of an initial history. This
means, solving Equation (2.36) starting with t = 0, requires well-deﬁned values for
NA(t) for t ∈[−τ, 0].
Summary
This short excursion, together with the two examples for population
dynamics modeling, clariﬁes an important statement from Chapter 1. Even if we
start from a single conceptual diagram that is in some sense a consensus of different
knowledge on the ecology of a population the resulting model does not only differ
in parameters, equations of implementational details. The models differ entirely in
their resulting structures.
These four different mathematical structures for populationdynamics modeling cover
the spectrum of approaches found in recent population ecology. However, one can


62
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
identify close relationships of these approachesand one can ﬁnd intermediate types of
models. ForexampletheLesliemodelmakesitpossibletoseparatetheclassicalstages
into a large number of “sub-stages” that can be compared to the delayed differential
equation model.
2.7
MODEL INTEGRATION: GENERIC AGROECOSYSTEM MODEL
All the model equations introducedare ordinarydifferential equations or matrix equa-
tions. Interactions are deﬁned by coupling functions of explicitly deﬁned ﬂows of
matter from one compartment to another. Equations (2.1) to (2.31) deﬁne the fol-
lowing model system of an agroecosystem model. The following set of equations
summarize this generic agroecosystem model. The main state variables and only the
important functions are listed. If possible a short and aggregated formula is chosen,
see this chapter for more detailed explanation.
dWC
dt
=
rC,max rN(N) rC,W(WC, WW) rC,P(Pd) fs(t)
−μW
fDC(t) WC −γ
WC
WC + kP
P
dWW
dt
=
rW,maxrQ(Q)
1 −WW
KW
dN
dt
=
−klN −d(W, t) + kmWμ + r f
W
W + k f
+ F(t)
dCL
dt
=
−kdCL −kwCL + ν(W)A(t)
dCS
dt
=
−kdCS + kwCL −klCS + (1 −ν(W))A(t)
P1(ti+1)
=
P1(ti)pov
G(ti)
j=1
F0ϑpd f(ti)phpp(j)pd(j) + ps(1 −ph(j)) , ti+1 −ti = 1a
dP
dt
=
rP,max
W
W + kP
P −μPP −μCrP,C (CL)CLP
In some cases one cannot distinguish between crop or weed biomass. Here W =
WW + WC denotes the total above-ground biomass. Table 2.11 gives a summary
of the processes considered, the modeling functions and the parameters and their
physiological or physical meaning.
The model is speciﬁed by different control variables such as fertilization scheme F,
application of pesticide A and weed control pi(t∗) as well as the crop selection, that
is denoted by α.
F(t)
=
q−1
i=0
Fiδ(t −ti)


MODEL INTEGRATION: GENERIC AGROECOSYSTEM MODEL
63
A(t)
=
q−1
i=0
Aiδ(t −ti)
α(ti)
=
(α1, α2, . . .)
αi ∈{wheat, fallow, barley, . . .}
Notethatthemodelisparameterizedandcanbeusedtodescribebothabioticandbiotic
processes of the ﬁrst trophic levels for different species. Especially for different crops
the model covers the dynamics of the sugar beet (abbreviated by “sub”), winter wheat
(“ww”), winter barley (“wb”), oats (“oa”), spring barley (“spb”) and potatoes (“pt”)
and the fallow seeds: oil radish (“or”) and ﬁeld beans (“fb”) and weed. Simplifying
parameterizations can be chosen for simulating bare soil or fallow.
The characteristic times of the model vary from years (population dynamics in ⃗P) to
weeks for growth of crop and weed, to days for degradation of pesticides. These are
deﬁned be the following parameters and parameter functions:
rN
=
N
N + kN
rC,P(P4)
=
r0
e−γ1(P4−Pr)2 −e−γ1P2
r
+ (1 + r1)e−γ2P4
1 + r1e−γ2P4
with P4(ti) = phpppdP1(ti)
rC,W(WC, WW)
=
1 −
lWC
WW
s
fs(t)
=
1
if t < td
(1+ρ1)e−ρ2t
1+ρ1e−ρ2t
else
rP,C(CL)
=
1 −e−
CL
Ccrit
2
rQ(Q)
=
Q
Qmax
c
kcn(t)
=
k1
if t < tDC
(kmax −k0)e−t−tDC
τ2
γc
−(kmax −k1)e−t−tDC
τ1
γc
+ k0
else
kd(T, θ)
=
kd,max kT(T) kθ(θ)
kT(T)
=
Tmax −T
Tmax −Topt
β
exp
β Tmax −T
Tmax −Topt
kθ(θ)
=
θa
From this it follows that the control variable “crop planted” α(t i) modiﬁes the model
parameters. Additionally, for special cases, such as “fallow”, the structure of the
model is also modiﬁed. The dependence from site-speciﬁc parameters introduces
spatial aspects into the model, which require regional simulations.


64
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
Table 2.11
Summary of model parameters.
Compartment
Term
Parameter
Physiological meaning
Crops
WC
rC,max [1/d]
maximum growth rate, relative increase of biomass per
day
WW,0 [kg/ha]
initial crop biomass, biomass at time of planting
μC [1/d]
attrition rate, relative decrease of biomass in stage of
senescence
rN
kN [kg/ha]
denotes amount of nitrogen necessary to attain half of the
maximum growth rate (Michaelis–Menten parameter)
rC,W
l [1]
critical weed density relative to crop biomass
s [1]
parameter of nonlinearity, equal behavior to c
rC,P
r0
growth stimulation due to pest infestation
Pr
density of pest for growth stimulation
r1, γ1, γ2 [1]
shape parameters
fs
ρ1 [1/d], ρ2 [1]
shape parameters
Weed
WW
rW,max [1/d]
maximum growth rate, relative increase of biomass per
day
WW,0 [kg/ha]
initial weed infestation, at time of planting
kW [kg/ha]
maximum carrying capacity of weed at observed site
rQ
Qmax [%]
critical level of photosynthetically-active radiation, in
case of actual Q exceeds Qmax weed growth increases,
otherwise weed growth decreases
c [1]
parameter of nonlinearity, the dependency described in
upper row to a more sensitive (c > 1) or insensitive (c <
1) behavior
Pest pop.
P
rP,max[1/d]
maximum growth rate of pests
kP [kg/ha]
denotes amount of crop biomass necessary to attain half
of the maximum growth rate (Michaelis–Menten param-
eter)
μC [1/d]
natural mortality of pest population
μP [1/d]
mortality of pest population due to pesticide treatment
rP,C
Ccrit [kg/ha]
threshold value of pesticide on crop leaf that to attain a
signiﬁcant mortality of pest population
⃗P(ti)
see Table 2.10 for a parameter summary
Nutrients
N
kl [1/d]
inﬁltration rate
km [1/d]
rate of mineralization
rf [1/d]
maximum rate of N2 ﬁxation for legume crops
kf [kg/ha]
amount of crop biomass of legumes necessary to attain
half of the maximum ﬁxation rate
Pesticides
CL
kW [1/d]
runoff rate of pesticide from leaf to soil surface
kd
kd,max [1/d]
maximum degradation rate
kθ(θ)
a
shape parameter
kT (T)
Topt
temperature of maximum degradation of pesticides
Tmax
maximum temperature from which no pesticide degra-
dation occurs
β
CS
kl [1/d]
inﬁltration rate


SUMMARY
65
2.8
SUMMARY
This chapter has presented examples for the steps of model development presented
in Chapter 1. The starting point is the conceptual diagram in Figure 2.1 that can be
classiﬁed as a feedback model or box-model. From this a set of mathematical equa-
tions was derived summarized in the previous section. In this process of compiling
the mathematical model we must clarify that the conceptual diagram is a guideline
only. For example, some boxes are speciﬁed in detail by more than one differen-
tial equation (which is supported for example in the concept of energy diagrams of
feedback diagrams).
Then we examine the steps of parameter identiﬁcation and model analysis. It is typical
for ecological modeling that the speciﬁcation of parameters is obtained from
• Literature values and databases (such as (Jørgensen et al., 2000)): k l, ϑpd f, ϑh,
γ1, γ2, γa, γb, r0, r1, etc.
• Field trials and following parameter estimation: rC,max, rC,max, rWC,max, μC, μW,
ρ1, ρ2, r f , k f, kmax, k0, k1, etc.
• Laboratory experiment together with parameter estimation: β, k d,max, Topt, etc.
• physical measurements and possible the aggregation to effective parameters:
kl, km, etc.
• and not to forget educated guesses: a, T max, etc.
Speciﬁcation of parameters is always subject to uncertainty. This uncertainty re-
quires a detailed analysis of the derived model, focusing on dynamic properties and
predictive power. Several examples in this chapter showed many possible results of
dynamic behavior. The model shows different patterns in different temporal scales.
Characteristic time vary from years (population dynamics) to weeks (crop growth) to
days (pesticide degradation).
Patterns in reality are redrawn. Statistically this is measured by the r 2 values. Addi-
tionally statistical analysis showed that the model should be set up with a minimum
number of parameters. This assists in applying the model to modiﬁed conditions
(such as different crops) as well as different locations. Regionalization of the model
is supported, cf. Section 1.4.1.
Besides this, the highly nonlinear model show chaotic patterns, which are rarely
visibleinrealityintheformonecanderivefromamathematicalmodel. Inthiscontext,
and knowing the uncertainty of model parameters, it should be noted that the domain
of appropriate model parameters is a subset of biologically useful parameters (which
again is a subset of the mathematically admissible parameters). The rejected domain
with parameters, which may be biologically useful, but which does not lead to useful
model output is a conjunction of two different domains: the domain of parameter
that leads to chaotic patterns due to the mathematical structure of the model, and the


66
ENVIRONMENTAL MODELS: DYNAMIC PROCESSES
domain of parameters that lead to chaotic patterns due to the numerical solution of
the underlying equation set. In most cases of environmental modeling one cannot
distinguish between these two domains.
Several variables of the model, introducedmanagementmodeledby controlvariables.
These variables denote the link of anthroposphere to biosphere. These variable are
used to deﬁne scenarios. For example different amounts of fertilizer can be applied.
Finally, a ﬁrst management task was investigated within the weed control model. The
concept of threshold values could be veriﬁed with a model with this kind of structure.
Besides the modiﬁcation of different state variables, the control variable selected
crop α(ti) switches between different model types.
This is possible because the
model shows a very general structure that makes it applicable to different crops
(and investigation sites). The minimum number of parameters is one prerequisite for
obtaining a general or generic model. Additionally the model is generic. This means
the model structure itself can change depending on control variables or parameters.
For example the model structure can be used to simulate bare soil by setting all crop
growth variables to zero or unity.
A second item that helped us to obtain such a generic model is the modularity.
Modularity is important for achieving results in the parameter estimation step, and
modularity is important for model integration of different building blocks in a model.
Modularityisaveryhelpfulpropertyinthestepofmodelanalysis, too. Theconclusion
to be derived from this is that a model structure must be deﬁned in an open way to
allow a simple integration of an additional part or modify existing parts.
However, advocating an open and modular structure of dynamic simulation models,
raises a difﬁcult question. What is the appropriate mathematical tool, that can couple
different mathematical models? As we have seen from this chapter,ecological models
may be set up by different types of differential equations as well as different types of
time-discrete equation sets. Possible relationships between time-discrete and time-
continuous modeling approaches of dynamic processes are identiﬁed. Nevertheless,
there is no formal theory which provides a link between continuous and discrete
systems (Savill & Hogeweg, 1999). In environmental modeling we have to cope
with both approaches. This mathematical heterogeneity so far is visible in forms
of coupling matrix equations with nonlinear ordinary or partial differential equation
systems. Additionally, environmental problems always refer to a spatial domain.
So the question arises, what kind of system do we get, when introducing spatial
dependencies?


3
Environmental Models:
Spatial Interactions
3.1
SPATIAL REFERENCES IN ENVIRONMENTAL MODELS
3.1.1
Spatial Scales and Model Support
The models introduced in Chapter 2 depend on the properties of the investigation
site being considered. For instance, growth parameters depend on radiation, exposi-
tion, nutrient availability. Population dynamics of species are a function of habitat
suitability. This dependency on attributes of the investigation site is primarily intro-
duced by a spatial dependency of the vector of model parameters from the location
⃗c = ⃗c(⃗z). As a consequence, state variables of a model acquire a spatial dependency,
too ⃗x(t) = ⃗x(t,⃗z).
If a variable has a spatial dependency, this potentially requires an inﬁnite amount
of information for speciﬁcation, since there are inﬁnite variables at every point in
any deﬁned geographic area. A spatial discretization of the considered area for each
layer of information, e.g. each variable and parameter, is required. The topic of
spatial discretization can be approached from several directions. If good data is
available, discretization of spatial data can be understood as a question of spatial data
analysis. Several well-known mathematical procedures obtained from geostatistics
are available, for example (Zhang & Grifﬁth, 1997). For instance, variogram analysis
of spatial data sets calculates indicators of the range of spatial variability. The reader
is referred to (Cressie, 1991; Deutsch & Journel, 1992).
However, good data availability is rare, the larger the considered spatial scale of the
modeling task is. In general the steps of model development and the step of acquiring
67


68
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
spatial information are two processes, that cannot be performed independently. The
following issues are closely related:
1. A model is a simpliﬁcation of real world processes with a certain purpose,
cf. Chapter 1.
This holds true for spatial discretization of information: a
spatial model simpliﬁes reality according to two dimensions: processes and
spatial extension.
2. In most cases spatial data is often absent or of a much lower quality. Spa-
tial discretization of data may be deﬁned by the availability of spatial data,
that determines the modeling process. For instance, data available from a re-
mote sensing source is used frequently in raster-based models, with the data
determining the raster cell size.
3. It follows that the process of model development is strongly inﬂuenced by
the choice of an appropriate data model for spatial data. The translation of a
conceptual diagram into mathematical equations depends on the chosen spatial
data model. This glues several steps of model development together, that were
introduced as independent steps in Chapter 1.
4. Even the processes considered and their mathematical formulation differs de-
pending on the selected spatial scale. Different processes dominate at different
scales, which leads to the fact that different processes are ignored in the step
of conceptual modeling, which is the step of simpliﬁcation in environmental
modeling.
Models representing equal processes vary considerably across scales, even if environ-
mental processes on large scales are to a great degree the result of processes at smaller
scales, cmp. Figure 1.3 on page 8. In this context Heuvelink (1998) introduces the
term model support:
Deﬁnition 3.1 (Support) The support of a model denotes a spatial unit for which
averaging in terms of model processes as well as data is admissible for the given
modeling problem.
The support of a model is closely related to“level of aggregation” or “sample volume”.
In this chapterresults and solutions from several examples are discussed in the context
of these three topics of spatial environmental modeling.
As an example for different types of spatial discretization and the resulting math-
ematical structure we focus on the processes of water- and matter dynamics in the
unsaturated soil zone. Figure 3.1 displays the location of the investigation site called
“Nienwohlde”, an investigation site of the CRP 179, situated in Lower Saxony. Soil
properties of this investigation site show a high spatial variability as this site is sit-
uated in a push terminal and ground moraine region, typical for northern Germany,
see (Pollex et al., 1995) for further information. Figure 3.2 displays a soil column for


SPATIAL REFERENCES IN ENVIRONMENTAL MODELS
69
Fig. 3.1
Location of the investigation site “Nienwohlde” of the Collaborative Research Cen-
ter “Water- and Matter Dynamics of Agroecosystems”.
which the transport of water is to be modeled. Modeling of processes in soil (unsatu-
rated or saturated) is subject to the problem of spatial variation on a very small range.
Figure 3.2 gives an example of 1.80 m deep soil column located at this investigation
site. Figure 3.2.a shows a photograph of the soil column after a tracer experiment
using a conservative red-colored tracer. The ﬂow region is colored by Rhodamine
applied during the tracer experiment.
Starting from the photograph (Figure 3.2.a) of the soil column, different steps of
discretization can be performed. First, homogeneous units, spatial units for which
an averaging of soil parameters is appropriate, are identiﬁed. This leads to a map
with several homogeneous units (Figure 3.2.b), the support of the model. This is
performed within a GIS using a vector data model, see below.
For the next steps the chosen model or model structure has to be taken into account
for spatial data management. If a partial differential equation in two dimensions
is used for transport modeling a 2D-ﬁnite-element mesh has to be set up from the
map of homogeneous soil regions, Figure 3.2.c. If a single soil column, is to be
modeled by a 1D-PDE model based on the identiﬁcation of a representative soil
column a 1D-discretization has to be identiﬁed, Figure 3.2.d. Finally, if a system
of ordinary differential equations, instead of a PDE, is used to solve the problem
of simulation water ﬂow through the soil column, a further aggregation of spatial
information is required. The result is a conceptual diagram using a box for each
spatially homogeneous region in soil, Figure 3.2.e.


70
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
a) Photography of soil
column after tracer
experiment
c) 2-dimensional
Finite Element Mesh
based on classification
b) Classification of soil
type
d) 1-dimensional
discretization
e) Discretization
according to profile
soil type horizons
Horiz. 1
Horiz. 2
Horiz. 3
Horiz. 4
Horiz. 5
1
θ
2
θ
3
θ
4
θ
5
θ
kl
kl
kl
kl
Fig. 3.2
Characterization of different modeling approaches together with different spatial
resolution of spatial data. From left to right: a) Photograph of soil column, b) Spatial dis-
cretization of homogeneous units in soil (GIS), c) 2D-ﬁnite-element mesh, underlying dis-
cretization for numerical solving the PDE, d) 1D discretization for numerical solution of PDE,
e) Discretization according to coarse classiﬁcation of properties of the soil horizons (“bucket”
model).
3.1.2
Models for Spatial Data Structures
The technical issue of storing, maintaining and analyzing spatial data is supported
by geographic information systems (Longley et al., 2001). Two concepts are used to
reduce geographic information for making spatial information available by computer
databases, that are requiredto developmodels for a geographicarea: raster and vector
data (Longley et al., 2001).
Raster Data
In a raster representation of geographic space, that space is divided
into an array of cells that are usually square. All geographic variation is expressed
by assigning properties to theses cells. The striking advantage of this concept is the
simplicity of the data model. Raster data sets can be handled as simple matrices,
which are available in a broad range of programming languages.
For each property a separate layer of cells is introduced. The size of raster cells is the
smallest possible unit with which spatial variability can be expressed, the smallest
possible support of a model. Larger homogeneous areas are expressed by a cluster
of raster cells with identical properties. In general an integration of several cells to
one homogeneous object is not possible. However, there are concepts that make use
of different raster cell sizes, such a multi grid or quad-tree approach (Nievergelt &
Widmayer, 1991). No spatial variability is covered that appears below a raster cell
size. Raster cell size therefore determines the precision with which spatial variability
is covered within the model.


SPATIAL REFERENCES IN ENVIRONMENTAL MODELS
71
Table 3.1
Comparison of characteristic topics of vector- and raster-based data structure for
environmental modeling.
Vector
Raster
Appropriate for modeling single, unique objects
Single objects (points or lines) are stored unstruc-
tured
Controllable precision of object location and
shape
Approximization of object
High effort for data acquisition
Data acquisition “simple” in some cases, e.g. re-
mote sensing
Low storage capacity required
High storage capacity required
Transformation of projection or co-ordinates sim-
ple
Projection transformations may change shape of
raster cells and topology
Logical operation between several layers is com-
plex function (intersection)
Implementation of logical operation or calcula-
tion simple, if raster maps show equal orientation
and location
A spatial application of an environmental model is performed using a repeated sim-
ulation of the model for every grid cell. This is the reason why the raster cell size
determines the complexity and computational effort of a model, too. The compu-
tational effort of a spatial model based on raster data increases quadratically with
decreasing cell size.
Vector Data
In a vector representation, all lines are captured as points connected
by precisely straight lines. If spatial information is given using a vector-based data
set, units with spatially homogeneousproperties, for examples soil properties, or land
cover, are given be a polygonal object, bordered by a polygon, a sequence of points.
One can derive vector-based data sets from grid-based data sets by aggregating grid
points with similar attributes using classiﬁcation algorithms, see (Sadler et al., 1998;
Lu et al., 1997; Weibel, 1997). The result, is a map S of homogeneous areas s ∈S .
Figure 3.2.b gives an example based on the photograph of a soil column.
Attributes, parameters are associated to this polygon using the layer concept. Every
spatial layer holds a single piece of information, for example a soil parameter. Inter-
section different polygonal layers is a well-known function of GIS (Breunig, 1996,
p. 77). This is displayed in the last row in Figure 3.9, see Section 3.3.1, p. 85.
Comparison
Table 3.1 lists a short summary of several topics related to the use
of raster or vector data. Both approaches are widely used in environmental modeling
and are well supported by GIS. Transformation between the two data structures is
possible. Transformation from raster to vector leads to the estimation of iso-surfaces,
transformation from vector to raster data leads to discretization of the considered area
deﬁned by a given cell size.


72
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
3.1.3
Spatial Patterns
If dynamic models are set up using parameters, coefﬁcients and state variables that
show a spatial reference, the simulation results show temporal as well as spatial pat-
terns. Two different sources of spatial patterns can be identiﬁed. Savill et al.(1999)
distinguish between exogenous and endogenous spatial patterns. Exogenous spatial
patterns are caused by external data fed into a simulation model. For instance soil
properties, land use, biotope attributes. Endogenouspattern emerge, if spatial interac-
tions are part of the model. Spatial interactions can be dispersal of species, diffusions
of substances, migration along landscape gradients.
So spatially distributed parameters of models do not necessarily lead to endogenous
patterns. On the other hand it is a necessary condition for obtaining endogenous
patterns, that a model incorporates spatial interactions between state variables.
For example, Anderson et al. (2002) investigate the question: which patterns of
driving forces cause which spatial patterns using different model systems? Their
conclusion is, that in many cases, the local interactions are chosen so that the neigh-
bors involved are within a ﬁxed range and contribute equally. The choice of the
neighborhood is not driven by realism.
From these introductory discussions one can distinguish two classes of spatial models.
At this stage, a textual deﬁnition can be given for both types of models:
Deﬁnition 3.2 (Regionalized Model) With the regionalization of a model, the fol-
lowing methodology is understood: all model parameters that describe environmental
factors are identiﬁed and speciﬁed using georeferenced data, obtained from a GIS.
The simulation is a repeated run of the model for each of the georeference data set⃗z i
using the model parameters ⃗c(⃗zi) and initial conditions ⃗x0(⃗zi) (i = 1, 2, 3 . . .).
Model structure may frequently change for different spatial patches. These models
are suitable for discrete habitat, or patchy landscapes. Second, information exchange
between state variables of different patches or homogeneous units is difﬁcult, which
complicates the implementation, for example, of horizontal ﬂuxes.
For these types of models much effort is spent on the identiﬁcation of effective model
parameters and representative spatial units that show homogeneous attributes char-
acterized by spatially constant parameters, see for instance (Bormann et al., 1999;
Beven & Kirkby, 1979; Wu & Levin, 1997). This may either be achieved within a
grid-based or vector-based data structure.
Deﬁnition 3.3 (Spatially Explicit Model) A spatially explicit model describes dy-
namic processes in a way that, for each arbitrarily chosen location vector⃗z, all state
variables are well-deﬁned. This methodologyexplicitly offers the ability to implement
processes that are based on exchange of matter and information between the spatial
units.
Spatially explicit models make use of both types of spatial data structures: vector or
grid data. Spatially explicit models based on vector data are presented for instance


AGGREGATED SPATIALLY EXPLICIT MODELS
73
by Krysanova et al. (2002), Beven et al. (1997), Kurz et al. (2000), and Wu & Levin
(1997). From a survey of recent publications on spatially explicit models, the most
frequent choice seems to be the grid-based data structure, see for instance (Rao et al.,
2000; Tyre et al., 2001; Congleton et al., 1997; Hargrove et al., 2000; Boumans et al.,
2001; Voinov et al., 1998; Voinov et al., 1999; Thulke et al., 1999; Yacoubi et al.,
2003).
Hybrid approaches combining vector and raster data structures, are presented by Ti-
schendorf et al. (1997) who use a quad-tree approach for analysis of habitat fragmen-
tation and Berger & Hildenbrandt (2000) who selected a hybrid data set combining
point and raster data for a spatially explict mangrove tree growth model.
This chapter will present examples for both types of models and explains the dif-
ferences between the two model classes. The starting point is an aggregated model
with several examples for biotic and abiotic processes. After this several examples
of integrated spatial models will be given.
3.2
AGGREGATED SPATIALLY EXPLICIT MODELS
Deﬁnition 3.4 Aggregated spatially explicit models are spatially explicit models
which are characterized by the use of a single mathematical “dialect” and a very
limited number of equations.
The important property of this deﬁnition is the uniqueness of the mathematical lan-
guage. This distinguishes aggregated models from models, that integrate several
different functions or equation systems, that probably change structurally for differ-
ent spatial objects. The mathematical structure of aggregated models remains equal
for all spatial objects (polygons or raster cells) of the investigation site.
In the following sections several examples of aggregated models are presented, fo-
cusing on mesoscalic applications and the relevant applications that are required for
the following chapters of this book.
3.2.1
Abiotic Processes
Modeling transport processes of substances throughdifferent media has two principle
components: modeling of transport and modeling of reaction. Both can be handled in
different ways,which depend on the media,the considered scale and the mathematical
dialect. For instance, transport of xenobiotica in soils may be modeled using box (or
“bucket”) models, which lead to ordinary differential equation systems or using the
convection dispersion equation, which leads to a partial differential equation. Both
approaches are based on an assumption of homogeneity of a certain volume of soil.
Water and Matter Transport in Soil
Transport processes in soil are charac-
terized by the number of phases or substances to be considered. In the upper soil


74
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
layer, water, soil substance as well as air set up the compartment of the unsaturated
soil zone. Two different phases (water and air) are to be considered in a transport
model. If there is also non-aquiferphase liquid (NAPL) the two-phase model changes
to a multi-phase model. This holds true for the aquifer compartment which is char-
acterized by the non-existence of air. One speaks of a multi-phase model for this
compartment if water as well as NAPL media is present (Bear & Bachmat, 1990).
Modeling of processes in soil (unsaturated or saturated) is subject to spatial variation
on a very small range. Figure 3.2.a shows a photographofthe soil column after a tracer
experiment. Following the discussion from Section 3.1.1 the identiﬁcation of the
support of a transport model, that depends on highly variable parameters determining
thetransportvelocities(suchasconductivity, orsorption)thesupportofasoiltransport
model is deﬁned by the assumption of an average or characteristic unit in which
model parameters are homogeneousand constant. A porous medium domain is called
homogeneouswith respect to a macroscopicgeometricalparameter characterizingthe
conﬁguration of the void space or of any phase withinthe domain,if that parameter has
the same value at all points of the domain. In this context a representative elementary
volume (REV) is deﬁned. Foremost is the requirement that the values of all averaged
geometrical characteristics of the microstructure of the porous material at any point
in the macro space of the porous medium domain be single valued function of the
location of that point of time only, independent of the size of the REV (Bear &
Bachmat, 1990).
The soil displayed in Figure 3.2 was analyzed in such a way. In a ﬁrst step the
photograph of 3.2.a was analyzed, homogeneous areas were identiﬁed and the soil
structure was rebuilt using the vector data model for deﬁning polygonal objects of
homogeneous soil areas. In a second step a model was used to describe the process
of water transport on such a geometry.
Richards Equation
For unsaturatedconditionsthe Richards equationdescribes the
process of movement of water content in the unsaturated soil zone
∂
∂tθ = ∂
∂x
D(θ) ∂θ
∂x
+ ∂
∂y
D(θ)∂θ
∂y
+ ∂
∂z
D(θ)∂θ
∂z −K(θ)
+ S
(3.1)
where θ denotes the water content [%], K the conductivity and S a source or sink
term. For a homogeneous, isotropic medium K is a scalar. In an anisotropic medium
K is a tensor. This equation is derived from the mass conservation equation with the
volumetric ﬂux density ⃗q
∂
∂tθ = −∇· ⃗q + S
(3.2)
which states that the rate of change of water content per unit volume equals the net
gain of ﬂuid per unit volume plus sink or source within the unit (REV), the Darcy
law. The nabla operator abbreviates
∂
∂x, ∂
∂y . The missing functional relationship
between the ﬂux density ⃗q and the water content θ in Equation (3.2) is derived from
the equation
⃗q = −K(θ)∇Ψh
(3.3)


AGGREGATED SPATIALLY EXPLICIT MODELS
75
in which Ψh denotes the hydraulic potential in [hPa]. The hydraulic potential is an
additive variable that is set up by the gravimetric potential Ψ z, that is simply expressed
by the vertical distance from a reference elevation, the matrix potential Ψ m, which is
due to the adsorptive forces of the soil matrix and depends on the water content of
the soil: Ψh = Ψz + Ψm. Note, that in Equation (3.1) Ψ denotes the matrix potential
Ψm (the index m will be dropped in the following) and it is set Ψ z = z with a negative
sign below the surface (even if surface is chosen as the reference level).
Note, the conductivity K as well as Ψm depends on the water content. A functional
relationship for both functions must be giventhat yields a speciﬁcationofthe unknown
variable D in Equation (3.1). Using the capacity function ∂θ/∂Ψ one gets
D(θ) = K(θ)∂Ψ
∂θ
(3.4)
The conductivity function is written in the form K = K sKr, where Ks denotes the
saturated conductivity,which is a parameter and Kr, which is referred to as normalized
hydraulic conductivity, describes the functional relationship. Similarly θ r denotes
the residual water content, and θs the saturated water content, the normalized water
content becomes
Θ = θ −θr
θs −θr
(3.5)
Several parameterizations of empirical relationships for ∂θ/∂Ψ and K(θ) are in use.
As one example the parameterizationaccordingto vanGenuchten(1980) and Mualem
(1976) is given here. It is a widely used ﬂexible approach, that is applicable to a large
number of soil types
Θ(Ψ)
=
1 + (α|Ψ|)
1
1−m
−m
for Ψ ≤0
1
for Ψ > 0
(3.6)
Kr(Θ)
=
Θ1/2
1 −1 −Θ1/m m
2
(3.7)
with ﬁtting parameters α and m.
Note, that the notation for the state variable water content Equation (3.1) is valid for
unsaturated conditions only. A general overview of unsaturated soil and groundwater
reaction dispersion models can be found in Baer & Verruijt (1987) and Anderson &
Woessner (1992).
Convection Dispersion Equation
Based on the convective transport of solute
matter in the soil water the convection dispersion equation (CDE) can be noted.
Denoting the concentration of a substance by C(t,⃗z) the CDE is written as
∂
∂tC = ∇· D∇C −⃗qC + S
(3.8)
S denotes a sink or source term in the considered REV. ⃗q speciﬁes the ﬂux density
derived from the Richards equation (3.2). D denotes the dispersion of the substance.


76
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
One assumes that movementof the solute along with the water is associated with a fur-
ther effect arising from the random motion of the water through the porous medium.
This effect is called mechanic dispersion and is treated in analogy to molecular dif-
fusion. The classical approach is to relate the ﬂux to a gradient of the concentration.
The negative sign determines the direction of the ﬂux from higher to lower concen-
tration. The relation only holds in an isotropic medium. Additionally Equation (3.8)
may be extended by sorption to the solid phase, and reactions such as degradation or
transformation to metabolites. These processes are incorporated into the model by
a modiﬁcation of the sink/source term of ODE-type equations. The process model
which deﬁne the sink/source term may be very complex. For instance Umgiesser et
al. (2003) present a complex dynamic model for nutrient cycling in the Venice lagoon
within the hydrodynamic model of the lagoon, solved by FEM numerics.
Boundary Conditions
Spatially explicit models of any kind need the speciﬁcation
of boundary conditions. These conditions specify the behavior of a model at the edge
of investigated region. In the theory of PDEs two important boundary condition types
are distinguished. The Dirichlet type speciﬁes a ﬁxed, but possibly time depending,
value of the state variable. The VonNeumanntype speciﬁes the values of the derivative
of the state variable in the direction of the vector orthogonal to the system boundary.
Simulation Study
Referring to the soil column displayed in Figure 3.2.a a sim-
ulation study1 is performed that models the transport of a tracer substance through
soil using a precise discretization of soil according to the 2D-ﬁnite-element mesh
generation, Figure 3.2.c. Figure 3.3 displays the concentration of a ﬁctive tracer for
the time steps t = 30 h to t = 240 h (a) to (h). The initial condition is given by a
homogeneous tracer wave in the ﬁrst 10 cm of the soil. This wave moves slowly
downwards. In the ﬁrst 50 cm the initial shape remains. After t = 120 h the spatially
distributed model parameters, such as conductivity, offer preferential ﬂow paths for
the substance. Finally the initial wave separated into two parts. Part of the applied
substance reached the lower edge of the soil column at 1.80 m and part remained at
partly impermeable layers at 1 m. These patterns are clearly exogenous, as these are a
result of the speciﬁcation of the conductivityparameters based on spatially referenced
model parameters ⃗c(⃗z).
3.2.2
Biotic Processes
Population Dynamics
In Section 2.6.3 the PDE for age-structured population
dynamics according to McKendrick and Foerster was introduced, cf. Equation (2.32).
Introducing spatial explicitness to this equation makes P depend on time, age and
location ⃗z: P(a, t,⃗z). Without loss of generality we consider a 2-dimensional habitat.
1Nummerical solutions of PDE-type models presented in this book are calculated using the model devel-
opment tool FEMLab, see Section 1.5.4, p. 29.


AGGREGATED SPATIALLY EXPLICIT MODELS
77
Fig. 3.3
Results of tracer transport modeling based on the soil of the “Nienwohlde” study
area. The tracer substance is homogeneous distributed in the upper 10 cm of the soil in the
initial condition. Figures a) to h) show the time steps 30, 60, . . . , 240 h. (See p. 279 for
additional ressources.)
a) t = 30 h
b) t = 60 h
c) t = 90 h
d) t = 120 h
e) t = 150 h
f) t = 180 h
g) t = 210 h
h) t = 240 h


78
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Spatial localization is given by a vector ⃗z = (x, y). An extension to a 3-dimensional
approach can easily be set up. The latter is frequently used in marine ecology.
Let us ﬁrst focus on the migration of species. The vector ⃗j denotes ﬂow of population
P(t, a,⃗z). ⃗j incorporates dispersion ⃗jD and active movement to more suitable habitats
⃗jH as well as advective drift by wind or current ⃗jv. It yields
⃗j = ⃗jD + ⃗jH + ⃗jv
Dispersion
In analogy to the derivation of the convection dispersion equation,
dispersion of the population denotes the spatial spread due to random motion of
individuals. However, the behavior of a living organism differs from substances or
solute. A frequent assumption in population dynamics modeling is that dispersal
depends on the population density of the considered location. The more dense the
population, the higher the the pressure to move to a different location. This leads to
a density dependent-dispersal term
⃗jD = −DD
P
Pcrit
n
∇P
Pcrit denotes a critical density and n is a shape parameter. The negative sign denotes
density-dependent migration directed to the lower population density. Note, that the
operator does not include age.
Habitat Suitability
Let H(⃗z) denote a function that describes the suitability of a
given location⃗z being a habitat for the considered species or community. There is an
abundant literature on habitat modeling methodologies, see for instance (Guisan &
Zimmermann, 2000; Tyre et al., 2001). For the following we assume a given habitat
suitability function obtained by an arbitrary model. The higher the value H(⃗z) returns,
the more suitable the habitat is at location⃗z. It may depend on several environmental
factors like availability or prey, or absence of predatory species. An example for
population density is
H(⃗z) = 1 −
P(⃗z)
Pmax(⃗z)
where Pmax denotes the carrying capacity of habitat in⃗z. Mobile species may have the
ability to migrate to the more suitable habitat along a gradient of habitat suitability.
The related vector ⃗jH can be deﬁned by
⃗jH = DH P ∇H(⃗z)
where DH denotes the migration rate based on habitat gradients in the landscape. It
is appropriate to assume that DH is dependent on the habitat suitability H(⃗z). For
instance for a less suitable habitat (low values of H) DH(H) may be large and vice
versa.


AGGREGATED SPATIALLY EXPLICIT MODELS
79
Drift
With the availability of a vector ⃗v holding the speed and direction of the
surrounding medium (water or air) obtained from a convection model, the vector j v
can be speciﬁed by
⃗jv = ⃗v P
Together with Equation (2.32) describing age-structured population dynamics, the
following general equation is derived
∂P
∂t + ∂P
∂a + ∇· DHP∇H −DD
P
Pcrit
n
∇P + ⃗vP
= −f(a, P,⃗z)P.
(3.9)
The function f(t, a,⃗z) ≥0 contains the per capita death rate due to different processes
like mortality, harvesting, inter-speciﬁc cannibalism, environmentalfactors of habitat
⃗z. Initial conditions are in accordance to the model in Section 2.6.3 and are extended
by spatial references.
P(0, a,⃗z) = P0(a,⃗z)
speciﬁes an initial age-structured population, which is — without loss of generality
— equally distributed throughout the entire region. The boundary condition
P(t, 0,⃗z) = r(⃗z)
A
0
F(a)P(t, a,⃗z) da
speciﬁes the growth of the population P at location ⃗z. r(⃗z) denotes the per capita
growth rate, which may depend on the location ⃗z. F(a) denotes the fertility at age a.
Considering aquatic species, for example, appropriate spatial boundary conditions
are an impermeable boundary for coastline and Dirichlet boundary conditions for the
oceanside, setting the population density zero for inﬁnity. Because of the migration
term of the model, it is guaranteed that the population will stay in a region of high
habitat suitability.
Simpliﬁcations
If we neglect age-structures Equation (3.9) can be rewritten by
dropping the dependence on age a, its associated differential operator and by using a
closed and analytical function for growth f(P,⃗z). We get
∂P
∂t + ∇· DHP∇H −DD
P
Pcrit
n
∇P + ⃗vP
= r(⃗z)P
1 −
P
Pmax(⃗z)
(3.10)
using a logistic growth equation with a location-dependent growth rate r(⃗z).
Simulation Study
Investigation Site “Sandau”
The model is applied to an investigation site at the
river Elbe in northern Germany. With a length of 1091 km and a catchment size of
148.300 km2the Elbe is one of the most important rivers ofCentral Europe. In contrast


80
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Fig. 3.4
Location of investigation site “Sandau” at river kilometer 417–418 of river Elbe,
Germany.
to most other German rivers, the Elbe has maintained a relatively natural ﬂood plain
landscape because of its special situation of being a border river for several decades.
The location of the investigation site, which was a bank section of the river Elbe near
the small village Sandau (river kilometers 417–418) is shown in Figure 3.4. The
banks of the stream are separated by groynes, which are stone structures built out
transversely from the banks. This keeps the current in the middle of the embankment.
Between them, the riverbanksare subject to dynamic hydro-morphologicalprocesses.
From open soil patches of different soil textures and pioneer vegetation at the water’s
edge they go on to meadowland at higher altitudes. The study site is traversed by
some branches of the main stream as well as by temporaryalluvial channelsand ponds
because of the high water level in winter.
The ﬁrst step in applying the model in Equation (3.10) is to set up an appropriate
habitat suitability map for the investigation site. Figure 3.5 displays a map of the
estimated carrying capacity of the groundbeetle species Agonummarginatum derived
from ﬁeld observations (Vogel, 2002). The discretization of the spatial data is based
on the vector-based biotope map with the associated carrying capacity values. From
this a ﬁnite-element-mesh for the numerical solution of Equation (3.10) is generated,
see Figure 3.6. Model parameters like growth rate r are estimated within laboratory
experiments, see (Vogel, 2002).
Figure 3.7 displays four time steps of the spatially explicit population dynamic mod-
eling for A. marginatum at the Elbe investigation site. The initial condition t = 0 is
given by the upper left ﬁgure, the time steps t = 30 d, t = 60 d and t = 90 d follow
from left to right and from top to bottom. The ﬁnal stage shows abundances in the


AGGREGATED SPATIALLY EXPLICIT MODELS
81
same range as those identiﬁed by ﬁeld experiments, and that are given by the habitat
suitability, the carrying capacity, cp. Figure 3.5.
The important issue is to identify which dynamic patterns affect this ﬁnal stage and
what spatial patterns are responsible for these dynamic patterns. The initial popula-
tion is given arbitrarily by an average abundance of 10 individuals per square meter
at location ⃗z0 = (4502600, 5852700). Two processes determine the spread of the
population: growth and dispersal. The initial population is located at a less suitable
habitat. Dispersal therefore proceeds only slowly. When the ﬁrst individual reaches
the most suitable habitat near the river, population growth speeds up and this habitat
is occupied quickly. This very narrow-shaped habitat along the Elbe river acts as a
migration highway. This is why most of the most suitable habitats are occupied by
A. marginatum after 90 days, even if simple dispersal would have led to a migration
to the intersection line “A” to “B” in Figure 3.7 lower right. This is in accordance to
ﬁeld observations (Vogel, 2002).
Spatially explicit Predator–Prey Models
The model
The classical approach introduced by Volterra (1927) is widely used
for modeling predator–prey interactions based on two coupled nonlinear ordinary
differential equations, see for instance (Begon et al., 1986, p. 356). A prey population
denoted by P1 and a predator population P2 are considered. Several different types
of predator–prey models have been discussed in recent literature. We focus on the
Fig. 3.5
Carrying capacity parameters de-
rived from GIS. Coordinates denote the last
three digit of the German Gauß–Kr¨uger coor-
dinate system (4502xxx, 5852xxx).
Fig. 3.6
Data preprocessing for spatially
explicit solving or partial differential equation
population dynamics modeling.


82
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Fig. 3.7
Spatially explicit population dynamics for A. marginatum based on a partial dif-
ferential equation model. Units are individuals per square meter. (See p. 279 for additional
ressources.)
original predator–prey equation system introduced by Volterra (1927)
dP1
dt
=
βP1 −σP1P2
dP2
dt
=
αP1P2 −γP2
(3.11)
in this ODE-system the term βP1 denotes the (unlimited) growth of the prey popula-
tion, σP1P2 death of prey by predation, αP1P2 growth of the predator population due
to predation success and γP2 mortality of predator population. The following spec-
iﬁcations of the parameters are chosen: α = 0.05, β = 0.075, γ = 0.1 and σ = 0.2.
For detailed analysis we focus more qualitatively on the system behavior.


AGGREGATED SPATIALLY EXPLICIT MODELS
83
This ODE system can be used in the partial differential equation for spatially explicit
modeling of predator–prey processes, simply by modifying the right hand side of
Equation (3.10). This yields
∂P1
∂t −∇·
D11∇P1 + D12(P2)∇P1
=
βP1 −σP1P2
∂P2
∂t −∇·
D21(P1)∇P2 + D22∇P2
=
αP1P2 −γP2
(3.12)
This equation system is solved for an artiﬁcial domain, a square with unit length.
Boundary condition are of Neumann type, assuming population density is symmetri-
cally at the boundaries.
Setting D11 = D12 = 0 neglects any random movement of the population. Dispersal
is assumed to be density-dependent from the density of the second species. We
assume that the prey escapes from high predator populations setting D 12 = −d12P2
and assume that the predator population follows the prey population: D 21 = d21P1.
Note, that the model has no dependencies onany coefﬁcients andparameters that show
spatial variability. If spatial patterns appear in this simulation study, these patterns
are purely endogenous.
Results
Figure 3.8.a displays the initial condition t = 0 of the density of prey and
predator population. The initial population is set to P 1 = 0.9 and P2 = 0.4 adding a
small sinusoidal variation with amplitude 0.1, horizontally for P 1 and vertically for
P2. This introduces a slight variability and triggers the migration processes.
Figure 3.8.bshows the results after t = 20 time steps. The initial patternchanged. The
results for the spatial pattern can be characterized clearly by the following properties:
• High prey population with less predators present (upper left corner);
• Low predator population with still large prey population (upper right corner);
• High predator population with less prey present (lower left corner);
• Low predator population with less predators present (lower right corner).
This is the spatial analog shown by the dynamic pattern of predator–preysystems, see
Section 5.4.1 starting on page 118. Note that the initial variability increased to 0.7
units for P1. Final results are plotted in the last row (Figure 3.8.c). In these last 80
time steps the spatial pattern ﬁnally changes to a pattern that will oscillate further on.
The speciﬁc wavelength of approximate 0.2 units depends on the chosen coefﬁcient
of dispersal. Again spatial variability of the populations increased to 4 units for the
prey population P1 and 0.5 units for predator population P 2.


84
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Summary
The use of PDE leads to an aggregateddescriptioninthemodel. Within a
two-dimensionalequationsystemseveralprocessesareconsidered: growth,predation
and dispersal. The model is derived from a strictly modular approach. Spatially
explicit processes are derived from considerations described in Section 3.2.2. The
interspeciﬁc relationships are modeled as source/sink terms of the PDE denoting
growth processes see Equation (3.10), or reaction processes in the framework of the
chemical fate modeling, cmp. Equation (3.8).
P1(t,⃗z)
P2(t,⃗z)
a) t = 0
b) t = 20
1.9732
1.1192
0.19058
0.12466
c) t = 100
5.2258
0.72534
0.54681
-0.023217
Fig. 3.8
Endogenous patterns derived from simple spatially explicit predator–prey model.
From upper left to lower right the time steps t = 0, t = 20, and t = 100 are displayed. Note
different scaling of shading. (See p. 279 for additional ressources.)


INTEGRATING SPATIALLY EXPLICIT MODELS
85
The most striking fact derived from this artiﬁcial simulation study is that spatial pat-
tern could be derived based on endogenous processes only. Note, habitat suitability
is not considered in Equation (3.12), respectively assumed to be constant in the ar-
tiﬁcial region. The patterns displayed in Figure 3.8 are solely derived from internal
spatially dependencies. Second, endogenous patterns are obtained on different spa-
tial scales, cmp. (Levine, 2000). Copious literature on theoretical biology focuses on
the theoretical analysis of spatially explicit predator–prey models. We focus on the
patterns only, the reader is referred to to these papers, see (Savill & Hogeweg, 1999;
Kishimoto, 1982).
3.3
INTEGRATING SPATIALLY EXPLICIT MODELS
Philosophy of science proposes theories or theorems that explain most of the patterns
studied with a minimum number of assumptions, hypotheses or axioms — in the
framework of this book, with a minimum of mathematical equations or sub-models.
From this point of view, an aggregated model as discussed in the foregoing section
is the model of choice, as these models offer a large range of resulting patterns and
processes with a minimum of input.
However, spatially explicit models are frequently set up by integration of many dif-
ferent equations. Spatially explicit models like these are not necessarily deﬁned by
PDE’s. These are set up by systems of coupled (ordinary differential) equations with
spatially referenced parameters.
In this case a general theoretical framework for spatial modeling cannot be given.
This is why the following examples are structured by their methodological concept.
3.3.1
Regionalization of Site Models
Concept
The ﬁrst step for regionalization of a model is achieved by the identiﬁca-
tion of units with homogeneousenvironmentalparameters for which a repeated run of
model simulations based on varying initial conditions and parameters is performed,
see Deﬁnition 3.2. This approach necessitates the identiﬁcation of homogeneous re-
gions. In a landscape ecological context, these areas may be denoted by ecotopes
(Naveh & Lieberman, 1984). In terms of spatial model development these units are
denoted by the support of a model, see Deﬁnition 3.1.
Both approachescan be comparedas the underlyingmethodologicalis similar. Figure
3.9 illustrates this concept within a GIS framework. Focusing on a selected study
area (red in all ﬁgures) four different layers of spatial vector-based information are
displayed:
a) Sub-watersheds in the investigation site with the average elevation in [m];
b) Elevation, given by polygons with equal elevation in intervals of 20 m;


86
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
a) Study area and (sub)watersheds (10
objects)
b) Elevation (769 objects)
c) Land use (682 objects)
d) Soil properties, pedological units
(799 objects)
e) Intersection:
3234 polygonal ob-
jects with constant environmental pa-
rameters for each landscape element
Fig. 3.9
Regionalization concept using vector-based spatial data based on derivation of
smallest homogeneous unit: ecotopes.
c) Land use and habitat types (textual coding);
d) Soil properties, displaying effective ﬁeld capacity in [mm].
Applicationof an agroecosystemmodel, as summarized in Section 2.7 for this investi-
gation site using spatial references to different locations requires the identiﬁcation of
homogeneous spatial object. Calculating the largest spatial units with homogeneous
properties derived from all input layers a) to d) is performed by an map intersection.
The procedure of intersection is a GIS function (Breunig, 1996, p. 77) and (Gold
et al., 1997, p. 30). It generates new maps with shapes in particular polygons that
have homogeneous attributes with respect to all input layers.


INTEGRATING SPATIALLY EXPLICIT MODELS
87
A map S of a layer, for example soil properties, is given by the tessellation of the stud-
ied region R. The map may consist of a set of ni polygonal units s j. The mathematical
deﬁnition can be written as
S i =
sj
j = 1, . . ., ni,⃗z ∈sj, gi(⃗z) ∈
Here gi deﬁnes the attributes of map S i. For all points located in a polygonal unit si
of S i the attribution fucntion gi is constant.
Deﬁnition 3.5 (Intersection) Considering a set of polygonal maps S i i = 1, 2 . . ., m
intersection can be deﬁned by
S 0 =
i=1,...,m S i
=
sj1 ∩· · · ∩sjm
ji = 1, . . ., ni, i = 1, . . ., n
∀⃗z ∈sj1 ∩· · · ∩sjm∀i = 1, . . ., n : gi(⃗z) = const.
(3.13)
Note, that this is a simplifying description. Intersection of maps requires a high
computational effort. It exponentially increases with the number of vertices deﬁning
a single object. The calculation of intersection polygons leads to geometric units
called silver polygons (Breunig, 1996) with a small area but long extent. Silver
polygons are caused by similar but not necessarily identical input layers of maps.
These silver polygons need to be removed or joined to similar regions to reduced
computational effort.
Application
Agroecosystem Model
Based on these considerations the agroecological simu-
lation model developed in Chapter 2 can be regionalized by making all site-speciﬁc
model parameters and initial conditions depend on the ecotope map, see Section 2.7.
Figure 3.10 illustrates this concept for the investigation site “Neuenkirchen” intro-
duced in Section 2.3.1, see Figure 2.2. The map in the lower left shows a detail from
the 3234 element large ecotope map together with the identiﬁcator number used for
accessing spatial parameters from the database. Model parameters like initial nitro-
gen content, ﬁeld capacity and initial weed infestation are speciﬁed this way. Driving
functions such as planted crop, applied fertilizer amount, weed control strategy de-
pends on the considered ﬁeld — the ecotope, too. Application of this regionalized
agroecosystem model are discussed in Chapter 11.
Bucket Models
These considerations aim at regionalization of models to a two-
dimensional investigation site. Vertical transport of water and substances as intro-
duced in Section 3.2.1 are not considered. The Richards Equation (3.1) and the
convection dispersion Equation (3.8) can be coupled to the agroecosystem model.
This integration can be performed by simply using the upper boundary condition
and the source/sink term to couple the two models. Using the source/sink terms


88
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
in Equations (3.1) and (3.8) nitrogen uptake and transpiration is modeled. Inﬁltra-
tion, fertilization speciﬁes the upper boundary condition (Diekkr ¨uger et al., 1995;
Diekkr¨uger & Arning, 1995).
Second, water and matter transport is frequently modeled by systems of ordinary
equations. These models simplify the underlying assumption of Darcy ﬂow using the
assumption of a ﬁeld capacity in soil. A soil column is discretizised by units with
equal ﬁeld capacity. If water content in a layer reaches ﬁeld capacity, an overﬂow of
this “bucket” occurs and water ﬂows down to the bucket below. This is illustrated
by Figure 3.2.e. In this case the spatial discretization determines the conceptual
model. This is an excellent example for the interdependence of spatial discretization
and conceptual model design, as introduced in Section 3.1.1. These model types are
frequently used for applications on a larger scales, especially if parameters of the
Richards equation are not available through space.
Further Examples
Similar approaches on larger scales, including hydrological
aspects and surface runoff, which need to consider spatial interactions are introduced
by (Beven & Kirkby, 1979; Krysanova et al., 1989; Band et al., 1991; Sasowsky
& Gardner, 1991). With the tool TELSA Kurz et al. (2000) present a toolbox for
spatially explicit modeling of agricultural landscapes together with the analysis of
scenario simulation, see Chapter 8 based on a vector data set.
Producers
Crops & Weed
Consumers
Anorganic
Nutrients
Mineral
Fertilizer
Consumers
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
CL(t)
CS(t)
F(t)
Producers
Crops & Weed
Consumers
Anorganic
Nutrients
Mineral
Fertilizer
Consumers
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
CL(t)
CS(t)
F(t)
99
107
103
97
121
100
113
76
95
94
119
121
106
101
103
Ecotope map with connected database of
environmental parameters for each polygon
Dynamic site model (ODE)
Fig. 3.10
Regionalization of environmental models based on the ecotope concept, that as-
sume model parameters and initial conditions depending on homogeneous units and performs
a repeated run of an equal model structure.


INTEGRATING SPATIALLY EXPLICIT MODELS
89
If we are to consider scenarios of land use change, generated by economic consider-
ations, which were not envisioned in the design of the elementary spatial units, this
approach is inappropriate. The boundaries between spatial units are ﬁxed and cannot
be modiﬁed during the course of the simulation, which may be somewhat restrictive.
3.3.2
Cellular Automata
Concept
A widely used grid-based model is the cellular automata approach (Er-
mentrout & Edelstein-Keshet,1993). A cellular automaton consists of a regular lattice
of cells. Each cell can hold a ﬁnite number of possible states, which can be expressed
by a scalar, a vector, a matrix or other mathematical objects, an information or any
other property. In the simplest case, the state is expressed as a binary variable.
In mathematical terms, the observed region is modeled by a set of discrete grid points
R = {(i, j) | ni < i < Ni; m j < j < M j}. A grid cell of the map is denoted by
⃗z ∈. The notation is used for the description of spatially explicit models too, see
next section.
The states of the ensemble of cells are updated synchronously in discrete time steps
according to a set of local,identical interaction rules. The rules can be formulated both
in a rigorous mathematical or in a more qualitative way, e.g. with the help of fuzzy sets
(Zadeh, 1965). Apart from its own previous state, the state of a cell is determined by
the previous states of a surrounding neighborhood of cells. There are different ways
Dispersal between 
neighboured cells
Raster-map with
environmental parameters,
e.g. habitat suitability etc.
Population Dynamic Model
(
)
( )
i
d
p
h
s
i
t
P
p
p
p
F
p
t
P
=
+
0
0
0
0
0
0
0
0
0
0
0
0
1
(
)
( )
i
d
p
h
s
i
t
P
p
p
p
F
p
t
P
=
+
0
0
0
0
0
0
0
0
0
0
0
0
1
Adult
Fertile Adult
Larva
Egg
Pupa
Adult
Fertile Adult
Larva
Egg
Pupa
Fig. 3.11
Regionalization of integrated models based on cellular automaton model approach.


90
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
b) Water level = 25.80 m
a) Water level = 26.00 m
Pop. Index > 1
Water
Elevation
Fig. 3.12
Results of population index derived from spatially explicit population dynamics
model of A. marginatum using a CA approach.
of deﬁning neighborhoods. The vonNeuman neighborhood consists of all adjacent
cells, the Moore neighborhood also includes the diagonal cells. These deﬁnitions
can be extended by enlarging the distance to the next adjacent cells. However, the
characteristic property of the cellular automaton approach is that this neighborhoodis
limited to a small number of cells. It is impossible to change the state of the considered
cell by accessing all other cells or cells far beyond the neighborhood radius.
A second important property is, that CA models usually are autonomous models, see
Section 1.3.4. The new state of a cell only depends on the recent state and the state of
the cells in the deﬁned neighborhood. Cellular automaton models with memory were
introduced by Alonzo-Sanz (2003). These are examples of systems with endogenous
patterns.
Figure 3.11 illustrates this concept,assuming a population dynamic model as a matrix-
based dynamic system for the dynamic process of each grid cell. This example will
be used in the following application.
Application
Based on the parameter of the population dynamic model for A. mar-
ginatum a cellular automaton model for the “Sandau” investigation site of the river
Elbe is run, compare Section 3.2.2. In this example, the population dynamic model
is set up by a matrix equation (Leslie model), compare Section 2.6.2. Dispersal of
species was modeled by the neighborhood radius in the cellular automaton model
(Vogel, 2002). From the results in Section 3.2.2 we know that the important habitats
are the sandy area with less vegetation near the river Elbe and the branches. For the
application of the cellular automaton model, the focus is on changing water levels.
For aggregated display of the result the population index is calculated. This index
calculated by the quotient of the ﬁnal population divided by the initial population
at the beginning of the year for each grid cell. An index above unity denotes a
suitable habitat, as population is growing, an index below unity denotes a habitat with
decreasing suitability for A. marginatum. Figure 3.12 displays the results for two


INTEGRATING SPATIALLY EXPLICIT MODELS
91
Producers
Crops & Weed
Consumers
Anorganic
Nutrients
Mineral
Fertilizer
Consumers
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
CL(t)
CS(t)
F(t)
Producers
Crops & Weed
Consumers
Anorganic
Nutrients
Mineral
Fertilizer
Consumers
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
CL(t)
CS(t)
F(t)
Horizontal fluxes 
between cells
Raster-map with
environmental parameters,
e.g. habitat type, soil
properties, slope etc.
Dynamic site model (ODE)
Fig. 3.13
Regionalization of integrated models based on cellular automaton model approach.
different water levels 26 m and 25.8 m. Note, for the higher water level more suitable
habitats are available. This is because water level and vegetation together build up
an ideal pattern for A. marginatum, cf. (Vogel, 2002).
3.3.3
Generic Landscape Models
The generic landscape modeling concept, introduced ﬁrst for the Everglades ecosys-
tem by (Fitz et al., 1996) followed by an abundant list for further publications on the
concept (Voinov et al., 1999; Maxwell & Costanza, 1997a; Maxwell & Costanza,
1997b) integrates the two approaches discussed before. The general idea is to use
a grid-based topology introduced for cellular automaton models but extend the do-
main of possible cell state and process models. Additionally, the strict limitation to
a deﬁned neighborhood is dropped. Figure 3.13 illustrates this concept.
Concept
The ecosystem model used for the regional model covers the processes
of hydrology (above ground, unsaturated soil zone, ground water), macrophytes and
consumers as well as and nutrient cycling (Voinov et al., 1999). In this approach the
modeledlandscape is partitionedinto a spatial grid of square unit cells. The landscape
is modeled as a grid of relatively small homogeneous cells and run simulations for
each cell with relatively simple rules for material ﬂuxing between the cells (Sklar
et al., 1985; Burke et al., 1990; Costanza et al., 1990; Maxwell & Costanza, 1997a).


92
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Baltimore
Dover
Annapolis
Washington D.C.
Richmond
Norfolk
Ch
esa
p
e
a
k
e
B
a
y
Atlantic Ocean
37°
38°
39°
77°
76°
Baltimore
Annapolis
Washington D.C.
Pa
tu
xen
t
W
a
t
e
r
s
h
e
d
Hunting Creek
Watershed
c
c
38°30
39°00
77°00'
76°30'
Fig. 3.14
Location of Patuxent river within the catchment of the Chesapeake Bay region.
This approach requires extensive spatial data sets and high computational capabili-
ties in terms of both storage and speed. Note, the approach allows quasi-continuous
modiﬁcations of the landscape, where habitat boundaries may change in response to
socioeconomic transformations. This is one of the prerequisites for spatial scenario
analysis, since it allows one to modify the spatial arrangement of the model endoge-
nously, within the simulation procedures. With this approach, the model builds on
the format of a raster-based geographic information system, which is used to store all
the spatially referenced data included in the model.
Model Description
The model is designed to simulate a variety of ecosystem
types using a ﬁxed model structure for each habitat type, cf. the generic agroecosys-
tem model in Chapter 2, Figure 2.1, p. 36. The model captures the response of
macrophyte and algae communities to nutrient concentrations, water and environ-
mental inputs. These processes are driven by hydrological algorithms for upland,
wetland and shallow-water habitats. It explicitly incorporates ecological processes
that determine water levels or content of surface water and the saturated and unsat-
urated soil zone, plant production, nutrient cycling associated with organic matter
decomposition and consumer dynamics. Therefore the simulation model for a habi-
tat consists of a system of coupled nonlinear ordinary differential equations, solved
with a 1 day time step.
The model is hierarchical in structure, incorporating the ecosystem-level unit model
that is replicated in each of the unit cells representing the landscape. Although the
same unit model runs in each cell, individual models are parameterized according
to habitat type and georeferenced information for a particular cell, see Figure 2.1
for a general compartment scheme of the generic model. The habitat-dependent


INTEGRATING SPATIALLY EXPLICIT MODELS
93
information is stored in a parameter database, which includes initial conditions, rate
parameters, stoichiometric ratios, etc. The habitat type and other location-dependent
characteristics are referenced through links to GIS ﬁles.
The unit models in each cell exchange matter and information across space. Surface
and subsurface hydrology deﬁne the horizontal ﬂuxes. This joins the unit models
together. The spatial hydrology module calculates the amount of water ﬂuxed over
the surface and in the saturated sediment. The ﬂuxes are driven by cell-to-cell head
differences of surface water and saturated sediment water, respectively. Dissolved
and suspended material (nutrients) is carried by water ﬂuxes between cells. At each
time step, ﬁrst the unit model updates the stocks within each cell caused by vertical
ﬂuxing and then cells communicate to ﬂux matter horizontally, simulating ﬂows and
determining ecological conditions across the landscape.
This model approach has been used to construct the Hunting Creek model (HCM), a
sub-watershed of the Patuxent. The local dynamics in the Hunting Creek Model were
similar to those developed in Patuxent landscape model (Voinov et al., 1999), but
the spatial implementation, deﬁned by the study area, and the spatial resolution were
different. By focusing on a smaller sub-watershed, we could make many more model
runs, calibrate the model more precisely, and reﬁne our understanding of some of the
crucial ecological processes and spatial ﬂows in the ecosystem. Use of a relatively
small study area was especially essential for the optimization procedures that require
numerous computer runs of the model.
The problem is analyzed on different scales. For the largest study area, the entire
Patuxent watershed, a lattice with a grid size of 1 km to 1 km is chosen. For detailed
study the Hunting Creek sub-watershed is selected. Simulations for this area are
based on a 200 to 200 m grid. Figure 3.14 displays GIS maps with the underlying
land use data sets of 1990. For more detailed analysis a sub-watershed of Hunting
Creek with an equal grid size is selected.
Validation
Validation of this complex model was performed using a stepwise ap-
proach. First, calibration of the hydrologic module was conducted against the USGS
(1997) data for one gaging station on the watershed. The model was calibrated for the
1990 data and afterwards tested for 7 consecutive years (1990–1996). The results are
in fairly good agreement with the data and may be considered as model veriﬁcation,
because none of the parameters have been changed after the initial calibration stage
for 1990. No reliable data was available to calibrate the spatial dynamics of ground
water. Nevertheless, the general hydrologic trends seem to be captured well by the
model.
Once the watershed hydrology was mimicked with sufﬁcient accuracy, the calibra-
tion of the water quality component was performed. Finally, the model was able to
reproduce the trends of nitrogen concentration at the gaging station (USGS, 1995).
In addition to the daily nitrogen dynamics we obtained a fairly good ﬁt for the an-
nual average concentration. For detailed documentation of the validation results, see
(Voinov et al., 1999). Overall, the model seems to do a good job in predicting the
integral and distributed ﬂuxes of nutrients over the watershed.


94
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
1
31
61
91
121
151
181
211
241
271
301
331
361
700000
1994
0
100000
200000
300000
400000
500000
600000
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
      Jan         Feb        Mar.       April.       Mai        June       July       Aug.       Sept.     Okt.       Nov.        Dez           .
1990 
0
100000
200000
300000
400000
500000
600000
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
Rainfall
Gage Data
Model run
1991 
0
50000
100000
150000
200000
250000
300000
350000
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
1
31
61
91
121
151
181
211
241
271
301
331
361
700000
1993
0
100000
200000
300000
400000
500000
600000
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
00.1
1992
0
50000
100000
150000
200000
250000
300000
-0.8
-0.7
-0.6
-0.5
-0.4
-0.3
-0.2
-0.1
0
0.1
Rainfall [m]
Gage Data [m³/d]
Fig. 3.15
Hydrology calibration for 1990/91 and further runs of the model for 1992–1996.
The later model runs may be considered as model test in terms of its predictive power, since
the parameters derived from the 1990/91 calibrations were not changed any more.
3.4
DISCUSSION
The last two chapters, which complete the ﬁrst part of the book, have clariﬁed that
the recent state of environmental modeling shows a trend away from analytically
treatable models towards complex integrated models systems. One can hardly list


DISCUSSION
95
1991
0
0.5
1
1.5
2
2.5
3
3.5
0
50
100
150
200
250
300
350
1992
0
0.5
1
1.5
2
2.5
0
50
100
150
200
250
300
350
1993
0
0.5
1
1.5
2
2.5
3
3.5
4
0
50
100
150
200
250
300
350
1994
0
0.5
1
1.5
2
2.5
0
50
100
150
200
250
300
350
0
0.5
1
1.5
2
2.5
3
0
50
100
150
200
250
300
350
1990
Data
Simulation
      Jan.        Feb.       Mar.       April        May        June       July       Aug.       Sept.     Oct.       Nov.        Dec.           
      Jan.        Feb.       Mar.       April        May        June       July       Aug.       Sept.     Oct.       Nov.        Dec.           
      Jan.        Feb.       Mar.       April        May        June       July       Aug.       Sept.     Oct.       Nov.        Dec.           
      Jan.        Feb.       Mar.       April        May        June       July       Aug.       Sept.     Oct.       Nov.        Dec.           
      Jan.        Feb        Mar.       April        May        June       July       Aug.       Sept.     Oct.       Nov.        Dec.           
Concentration N [g/m²]
Fig. 3.16
Nitrogen calibration for the data at the USGS gaging station.
all equations coded in an integrated model as well as all conditions tested to start or
solve these implemented equations.
Before discussing the related problems, we ﬁrst focus on the general results from
this chapter. Spatially explicit models can be derived from different mathematical
approaches. Partial differential equations seem to be the most aggregated and the
most sophisticated approach. These systems require an enormous numerical effort.


96
ENVIRONMENTAL MODELS: SPATIAL INTERACTIONS
Related software tools are highly sophisticated. High standard numerics are required
to solve these system. A profoundmathematical knowledgeis required for the correct
setup of these models. This may be one reason why this approach did not ﬁnd its way
into recent modeling in landscape ecology, even though these are highly aggregated
and easily transferable to different site conditions. In this context, the important
summary is that the link between geometry in the landscape and the topology with
respect to the considered species or substance is derived using a GIS. Spatial patterns
are then derived from aggregated equations for processes of convection, growth or
dispersal. This shows the strength of the PDE methodology for real landscapes.
Using these PDE systems as a starting point, one can interpret all other solutions
as possible discretization of these system. For example, spatial discretization using
an equal step size vertically and horizontally, leads us to the concept of cellular
automata. Second, discretizing an age-structuredpopulation dynamics equation from
McKendrick–Foerster leads to a (extended) Leslie matrix.
However, aggregated spatially explicit models can become integrated models, just by
discretization in space. Soil process modeling is a good example for this statement.
With the use of discretization, models become more and more integrated and differ-
ent additional sub-models and equations can be coupled. Integrated models therefore
seem to be the logical consequence. Integrated models offer the extendibility nec-
essary to cope with all important environmental processes derived from different
disciplines and coded by different mathematical approaches. In this context it seems
as if the most favorable data structure is the raster data set when choosing integrated
model approaches. In any case, GIS is the important tool for data preprocessing and
supporting spatially explicit modeling.
Finally, spatial patterns are the most important result of spatially explicit models.
Opdam et al. (2002) state that the future of landscapeecology lies in the understanding
of how landscape pattern is related to the functioning of the landscape system, placed
in the context of (changing) social values and land use. Modeling and simulating
processes with a spatial reference together with analysis of the resulting patterns is
the methodological concept that can cope with this task. Studying the results from
this chapter, the most important result is that spatially explicit models encompass
exogenousas well as endogenous patterns. These two pattern types are superimposed
on the ﬁnal result of a model. From this it follows, that a ﬁnal answer to Opdam et al.’s
(2002) question needs identiﬁcation of what the endogenous and exogenous patterns
of a system are.


Part II
Integrated Models
“Pathetic,” he said. “That’s what it is. Pathetic.” He turned and walked
slowly down the stream for twenty yards, splashed across it, and walked
slowly back on the other side. Then he looked at himself in the water
again. “As I thought,” he said. “No better from this side. But nobody
minds. Nobody cares. Pathetic, that’s what it is.”
—A.A. Milne


4
Multi-paradigm Modeling
4.1
INTRODUCTION
Translation of conceptual models into mathematical equations so far ends up either
in aggregated spatially explicit models deﬁned by partial differential equations (see
Section 3.4) or by models integrating different mathematical equations on the basis of
a spatial discretization by grid or vector data (see Section 3.3). Most environmental
models are a mixture of these two possible categories. M ¨uller (1997) published
an overview and characterized development of ecological modeling by a lack of
theoretical background,and a missing general concept in ecological or environmental
modeling.
There are different reasons for this development. First, environmental models are set
up by different approaches. The last chapter exempliﬁed that population dynamics
are described by algebraic difference or matrix equations, while process models are
expressed by systems of ordinary differential equations. If spatial processes are to
be considered, partial differential equations have to be included. In an environmental
model, these processes have to be integrated.
Second, environmental models frequently trace ﬂows of substances through differ-
ent media. For instance, substances are emitted from a production site, transported,
probably transformed by chemical reactions, and dispersed in the lower atmosphere,
then disposed and maybe suspended in an aquatic ecosystem and ﬁnally taken up
by a species, see Chapter 7. It is very difﬁcult or even impossible to ﬁnd a model
that covers all these processes within a general mathematical structure and to give an
aggregated notation of the mathematical model. Multi-media models cause mathe-
matical heterogeneity.
99


100
MULTI-PARADIGM MODELING
Third, a conceptual difﬁculty arises stemming from the fact that processes of different
dynamic quality interact. The dynamics of technical systems are mostly time-discrete
and their dynamics are closely related to discrete spatial structures, whereas many
environmental processes are continuous in time and space. The whole system can be
characterized as structured time-discrete and time-continuous. An illustrative exam-
ple is crop production where continuous biological processes such as crop growths
or water transport in soil are embedded into time-discrete agrotechnical management
procedures.
One is faced with the problem of mathematical heterogeneity (Seppelt & Temme,
2001) or multi-paradigm models (Villa, 2001). It is not feasible to model integrated
systems in the framework of one mathematical theory like ordinary differential equa-
tions. More general methodologieswill be developedby integrationof heterogeneous
systems (McIntosh, 2003). Besides this an important consequence of mathematical
heterogeneity is, that the number of applicable procedures for model analysis is re-
duced, the more heterogeneous a model is. From this background some additional
criteria for assessing the performance of a model are to be studied. These criteria can
be derived from philosophy of science. The aspects offer a methodological frame-
work for developing general methodologies for model integration and for developing
mathematically heterogeneous or hybrid models.
4.2
FUNDAMENTAL ASPECTS OF ENVIRONMENTAL MODELING
The important questions stemming from this observation on environmental models
are: Is there a theoretical foundation of ecological modeling that can offer a guideline
for model development? Can mathematical heterogeneity be reduced? Can a theo-
retical foundation help us to choose the appropriate mathematical structure? Shortly,
how can the translation from conceptual models to mathematical models be guided
and theoretically founded?
From an analysis of the process of environmental or ecological modeling as brieﬂy
summarized in the precedingchapters the following important topics can be obtained:
1. Modeling the entire system in an integrative way requires input from modeling
approaches of different disciplines, such as soil science, biology, chemistry,
physics etc. This multi-disciplinarity of environmental modeling results in
differentconceptualizationsofenvironmentalprocesses, indifferentviewpoints
on the step of transferring and in a broad spectrum of underlying theoretical
concepts.
Environmental modeling can be approached in many different ways. Depend-
ing on the scale of interest, on the accessibility and usability of data sets, and
of the aim and scope of the problem to be solved, different simulations models
have been developed and used. Some authors complain about an enormous
redundancy (M¨uller, 1997).


FUNDAMENTAL ASPECTS OF ENVIRONMENTAL MODELING
101
2. The considered processes show a broad spectrum of time scales as well as
spatial scales. It seems as if the chosen temporal and spatial scale (cmp. Fig-
ure 1.3) determines the conceptual model, the structure of the equation and the
mathematical dialect chosen, see (Levin, 2000).
3. This motivated Beddington et al. (1981) to state that “there are no Newtonian
laws in ecology”. A similar statement is, that ecological modeling lacks so-
called ﬁrst principles.
Of course the basic laws of thermodynamics and physics are valid in envi-
ronmental systems. However, equal processes can be described by different
modeling approaches, while looking at the phenomena at different levels of
aggregation.
4. Finally, Wu & Hobbs (2002) advocate an applicationof methods from complex-
ity theory and associated methods, such as self-organizations, fractals, cellular
automata, genetic algorithms or neural networks in environmental modeling,
see also (Jørgensen & Bendoricchio, 2001).
The conclusion from these observations is that environmental modeling has to cope
with reductionistic as well as holistic approaches. Reductionistic approaches make
use of ﬁrst principles for example derived from thermodynamics, or physics wherever
applicable to the considered scale. Holistic approaches intend to describe entire
patterns on the considered scale and tend to be treated as black box models. A good
environmental model therefore is characterized by an appropriate combination of
reductionistic and holistic approaches.
Well-known measures of model goodness and statistical tests are used to identify
the fraction of variability in real world data that is reproduced by the model, see
Section1.3. However, theseproceduresaredifﬁculttoapplytointegratedandspatially
explicit models, see for instance (Boumans et al., 2001). More important, these
measures require data available for the comparison of real world data and model
output.
From this background the questions are raised: How can model performance be
assessed with reduced or missing real world data? How can model assessment be
extended to the entire process of model development? Model applications are under-
stood also in terms hypothesis testing (Jørgensen & Bendoricchio, 2001). Following
this idea the answer to the above question can be derived from some consideration of
scientiﬁc theory.
Developing a hybrid or integrated model by adding or coupling different modules has
to fulﬁll inner consistency, which means that a new model shows no contradictions
within the model itself. The new model has to fulﬁll outer consistency, too, which
means that a new model has no contradictions to other consistent models. This is
in accordance with the criteria developed in Chapter 1 for testing and analyzing a
model. The following criteria are new from this perspective. Adding a new module
must describe a new issue, a new feature or process, new in terms of environmental


102
MULTI-PARADIGM MODELING
issues, issues of scale, or of hierarchy, and which can be tested by experiments or
applications. These are necessary conditions in model development.
Important optional criteria that can be derived from scientiﬁc theory are generality,
depth, minimality, precision and accuracy of prognosis. Transferred to the method-
ological of environmental modeling, the following recommendations can be derived:
Precision and Accuracy aim at a minimum of deviation of the model results from
the data observed. Denoting this property as an optional criterion is no con-
tradiction to the explanations of Section 1.4.2, as there is an abundant list of
examples in which the derived patterns are of more interest than the precise
values of the state variables.
Generality denotes the size of the domain for which the model is applicable. A
modeler always aims at a large domain and a high generality.
Depth and Minimality are criteria that are very frequently used to assess models.
Models that offer a deep insight into the functioning of processes or that use
a minimum of equations are very good and preferred models. Examples for
these kinds of models are the spatially explicit population dynamic models
introduced in Section 3.2.2.
A scientiﬁc theory oriented assessment of models would prefer an aggregated
model,thatneedslessparameters,variablesandfunctionsandisabletodescribe
the same spatial and temporal patters as a complex, integrated model.
These criteria may be guidelines for developing a theoretical scaffolding of envi-
ronmental modeling frameworks. These criteria are very important and valuable for
those hybrid or integrated models for which less analytical and numerical procedures
are available for model testing, as shown in Section 1.3.
4.3
MATHEMATICS OF ENVIRONMENTAL MODELING
4.3.1
General Model Equation
Once we have identiﬁed that environmental models show this intrinsic property of
mathematical heterogeneity, we still need to apply these models in procedures for
model analysis or model application, even if criteria for assessment are available.
This requires us to abstract from all possible mathematical dialects integrated in a
mathematical model. To abstract from all these properties and to achieve a treatment
of the system on a more general level a general model equation is introduced:
Deﬁnition 4.1 Consider a dynamic system with the state variable ⃗x, the control vari-
ables ⃗u, a vector of parameters ⃗c and a right-hand side MΔt the equation
⃗x(ti+1,⃗z) = MΔt ⃗x(t,⃗z),⃗u(t,⃗z),⃗c(⃗z),⃗z
⃗z ∈R
(4.1)


MATHEMATICS OF ENVIRONMENTAL MODELING
103
deﬁnes a General Model Equation (GME), where Δt is deﬁned by Δt = t i+1 −ti with
an arbitrarily separation (ti)i=1,2,... of the time interval of simulation.
The initial condition is given by ⃗x0(⃗z). All model variables (state, control and param-
eter) may vary in space. This may be true for the system equation MΔt that may also
depend on space ⃗z. Boundary conditions are deﬁned for all ⃗z ∈∂R.
In this deﬁnition a distinction is made between control variables ⃗u and model param-
eters ⃗c. ⃗c collects all parameters, which specify the model due to site conditions,
such as soil conductivity, site-speciﬁc growth rates, precipitation etc. Whereas, the
control vector ⃗u sets up all those variables of the simulation model, which may be
deﬁned by different scenarios, by possible impact or control of an experiment or
by management strategies, such as fertilizer amounts, pesticide application, etc. In
Equation (4.1) MΔt integrates all mathematical equations, rules etc., which set up the
entire simulation model as well as numerical code, which is required to solve the
mathematical equation. Some examples of how to specify M Δt:
• In the case of pure matrix models (population dynamics, Leslie models) or pure
algebraic models, Equation (4.1) can be applied directly.
• In the case of ordinary differential equation systems, the estimation of the suc-
ceeding state ⃗x(ti+1) involves the numerical solution of the differential equation
system (Hairer et al., 1980; Hairer & Wanner, 1980). M Δt integrates the ODE-
system as well as the system solver. In this case MΔt is called the ﬂux of the
dynamic system (Arrowsmith & Place, 1994).
• In the case of a cellular automaton model MΔt also incorporates spatial inter-
action, e.g. ⃗x depends on a vector of location ⃗z. However, cellular automaton
models are deﬁned by a ﬁxed neighborhoodradius (which is often small, 1 to 2
cells), MΔt is structured, and can be written as a band matrix for their spatially
dependencies.
4.3.2
Integrated Models
Section 3.3 summarized three different types of spatial models, that make use of a
number of different equations or functions in spite of an aggregated spatially explicit
model deﬁned using a PDE. Integration in this context was meant by coupling the
models by a spatial data model.
Integrationcan be understoodin a more generalcontext, too. Integratedmodels aim at
a consistent description of economic as well as ecological processes (Boumans et al.,
2002),at integration of anthroposphere andbiosphere processes. In general integrated
models we aim at overcoming the classiﬁcations and characterization introduced in
Section 1.3.4. From this basic idea, and the explanations given up to this point, some
recommendations can be derived for the process of developing complex, spatially
explicit environmental models set up by many processes from different disciplines:


104
MULTI-PARADIGM MODELING
Modeling can hardly begin from scratch. While deﬁning a conceptual model, avail-
able models or modules need to be considered. Environmental models should be set
up by single modules or sub-models. System behavior, admissible domain of initial
variables, parameters and control variables and spatial and temporal grain and extent
must be available and need to be well documented. The module itself must be robust
for the given domains known, see Figure 1.3. This refers to the mathematical part
of the model as well as to the numerical procedures implemented to derived model
solutions if present.
Using predeﬁned modules reduces redundancy in a model, as well as redundancy in
environmental modeling. Vice versa, a conceptual diagram may be used to identify
where to start with the development of sub-models ﬁrst. The modularity derived in
this way helps to integrate, couple and document models. It supports achievement of
the recommended depth or minimality of a model.
Note that, even if the single modules are properly tested and sub-models system be-
havior is known, it is hardly possible to derive system behavior of the coupled system.
Model analysis techniques such as Monte Carlo simulation, sensitivity analysis, sta-
bility analysis, see Section 1.3, can and should be applied to integrated models, too.
The most important prerequisite of re-usability of models and modules seems to be
the documentation, there are several solutions available (see next section).
4.4
MODEL DOCUMENTATION AND MODEL DATABASES
4.4.1
Introduction
The major prerequisite of model integrationand usability ofmodules in different mod-
els is appropriate model documentation. This documentation has to cover the process
models, dynamics and patterns implemented and the domain to which the model can
be applied. Available model documentation methodologies can be classiﬁed by the
following topics:
• Model documentation treats the model as black box. Information on the in-
cluded processes, the meaning of input and output variables as well as the
domain of the state variables and parameters are given. If available, informa-
tion on the investigation sites, from which data for model development was
obtained, is added, too. This approach neglects any mathematical structures.
Information on the domainof application andontheexpecteddynamic behavior
(spatial and temporal patterns) is limited.
• The mathematical structure of a model is documented by listing the equations,
parametersandinitialconditions. Thisdocumentationincludesresultsofmodel
analysis, results from parameters estimation and the system behavior. Chapters
2 and 3 present examples for this type of model documentations.


MODEL DOCUMENTATION AND MODEL DATABASES
105
0
50
100
150
200
250
300
350
400
450
Organ
Individual
Population
Ecosystem
Landscape
Ecosphere
Organization Level
Number of Models
Fig. 4.1
Distribution of meta-documentation entries of models in the Register of Ecological
Models for different levels of organization.
• The most convenient (and less frequently chosen) procedure in documenting
environmental models is to include information on the development procedure
according to the decisions and considerations made, when going through all
steps of the water ﬂow model (Figure 1.4), presented in Chapter 1, page 13. As
these decisions and considerations determine the mathematical structure and
the heterogeneity, this is a very important step of model documentation.
In recent literature model documentation usually covers the ﬁrst topic of this list.
Documentation in terms of the remaining item is understood as so-called meta-
documentation or meta-modeling.
Different concepts for these tasks are available.
The following sections give a short overview of these concepts.
Meta-modeling concepts are used to solve two major problems. The ﬁrst task is to set
up appropriate databases on model documentations, that allow us to browse through
a list of available models and retrieve models that solve the problem of interest.
These databases are either meta-databases, e.g. databases that offer documentation
on models and the contact address of the modeler, only. Or, these databases permit
us to download the model code or run the model interactively. The following section
brieﬂy summarizes some concepts and examples.
4.4.2
Model Databases
Register of Ecological Models
The register of ecological models (REM) is the
result of the union of the databases of the REM database in its ﬁrst stage of devel-
opment and the Environmental Research Information System (UFIS), (Hoch et al.,
1998). REM provides easy access to and information on more than 600 ecosystem
models at different organization levels. Figure 4.1 shows the results of the screening


106
MULTI-PARADIGM MODELING
review of this database. Depending on the speciﬁed level of organization a model is
developed for, the number of available meta-information entries is displayed. One
may think that modelingecosystem process is of most interest in ecologicalmodeling.
REM is a meta-database for existing ecological models and is designed to offer infor-
mation on ecological models as a whole. The goal is to provide a tool that supports
interdisciplinary work among modelers as well as to give administrative bodies an
overview of national and international activities in ecological modeling. The avail-
ability of such an information system is believed to be crucial to international coordi-
nation of modeling activities, and to reduce redundancy in environmental modeling.
REM pay particular attention to data requirements of models, areas of application,
and scales of the model. REM as a meta-database is open to all modelers for submit-
ting information on new model development. Figure 4.2 displays an excerpt of the
web page for entering model information. The part related to model structure and
mathematical characterization is shown (Benz, 2003).
A part of REM which is closely linked to model documentation focuses on the de-
scription of data. Since there is no modeling without data it is natural to combine
information systems on data and models in one unit. UFIS does not intend to keep
data, but will keep information on where and how to access data (meta-data). De-
scriptions of data in the model information system will be compatible with the ones
in the meta-data information system such that relations between models and data can
be easily recovered (Knorrenschild et al., 1996).
The CAMASE Register of Agroecosystems Models
The project CAMASE
(Plentinger & de Vries, 2001) develop a comprehensive register of agroecosystems
models. The aim is to
• increase awareness among scientists of existing models and reduce redundancy
in model development, prevent reinvention-of-the-wheel effect;
• increase accessibility of these models;
• stimulate harmonization and compatibility of models;
• stimulate use of models.
The project aims to collect 80% of relevant models used in Europe for research, edu-
cation and application in intensively and extensively produced agricultural crops,
grasslands, forests, and their environments, cropping and farming systems, farm
households, land use. Additionally shells for such models and tools for such models
in decision support applications(e.g. micro-climate proﬁles for irrigationscheduling)
are listed. Models in the CAMASE Register need to be documented on a scientiﬁc
level and need to be validated, at least partially. Software tools are listed in the
database if they are closely related to agroecological modeling (Plentiger & de Vries,
1997).


MODEL DOCUMENTATION AND MODEL DATABASES
107
Fig. 4.2
REM/ECOBAS web page for entering meta-information on ecological models.
URL: http://eco.wiz.uni-kassel.de/ecobas.html [July 2003].
4.4.3
Meta-modeling Concepts
The second major problem that requires an appropriate methodology on meta-mo-
deling is the integration and model coupling of sub-models or modules. An automatic
integration and coupling of different (heterogeneous) models necessitates access and
work with data structures that make information on the type of model, variables and
domain accessible. The general idea for solving this problem is to identify models,
or the processes described, as objects using an object-oriented concept for modeling
the data structures of the meta-data as well as the model integration tools (Hoch et al.,


108
MULTI-PARADIGM MODELING
1998; Villa, 2001; Maxwell & Costanza, 1997a). The following examples brieﬂy
discusses implemented solutions without focusing too much on a highly sophisticated
computer science realization.
ECOBAS — Model Interchange Format
The ECOBAS_MIF model inter-
change format is used for model documentation as well as for supporting the model
database ECOBAS. The project aims at complete and consistent documentation of
models as well as to make them accessible and comparable (Benz et al., 1997). The
MIF ﬁle is an easily portable ASCII ﬁle and holds complete documentationof a model
including:
• General information for the speciﬁcation of the ecological process and source
of the mathematical description;
• Declaration and identiﬁcations of the attributes and quantities (inputs, outputs,
states and constraints) of the process modeled;
• Complete and consistent formulation of all input-output relations (functions
and equations);
• Information about the environment for which the documented model has de-
veloped.
Based on a properly deﬁned model using a MIF ﬁle the following functions can be
used within the associated framework (Hoch et al., 1998):
• Compilation of documentation in RTF, TEX, or HTML;
• Use the MIF ﬁle as source for modeling platforms such as MATLAB–SIMU-
LINK, cf. Section 1.5.3. p. 29.
The creation and maintenance of MIF based models is supported by a graphical front
end editor that supports editing all components of a MIF ﬁle.
Modular Modeling Language
Maxwell (1997a) presented the modular model-
ing language (MML). This modular modeling concept set up the foundation for the
spatial modeling environment, see Section 3.3.3. Similar to a MIF ﬁle, the MML
acts as an intermediate layer supporting the communication and interchange between
the model description layer and model implementation. As an important addition to
the MIF concept the spatial modeling environment offers a tool for translating out-
put from graphic model development platforms (STELLA) to MML ﬁle. The key
properties of a model description in MML are (Maxwell & Costanza, 1997a):
• Simplicity: Only the important details relevant to the dynamics of the models
are coded using MML. Implementational aspects are neglected.


MODEL DOCUMENTATION AND MODEL DATABASES
109
• Modularity: Components, sub-models or modules are separately represented
using this languages. These modules encapsulate their data and dynamics in
the sense that they can only be interfaced through their inputs and output.
• Encapsulation hierarchy: Modules may include or encapsulate other modules.
The scope of the encapsulated module cannot access modules declared outside
the encapsulating module.
• The inheritance hierarchy allows modules to inherit some of the functionality
of other modules. This property facilitates the construction of specialization
hierarchies.
• Connections: MML declares connections of input/output variables between
modules.
These properties of the MML are in accordance with the requirements listed above.
The major focus of this development is the integration of models and the construc-
tion of spatially explicit models rather then the documentation of models and model
retrieval. For instance, much information coded into a STELLA model, like docu-
mentation, units of variables etc., is dropped in the translation to a MML conﬁrm
model.
Integrated Modeling Architecture
Villa (2001) extends this concept by the
integrated modeling architecture (IMA). It specially focuses on the problem of math-
ematical heterogeneity and the problem of multi-paradigm and multi-scale environ-
mental models. The major characterization of environmental models follows the
three categories of representation, domain and scale. Referring to these categories
the concept of IMA offers a framework for making different modules comparable and
supports interaction between different modeling paradigms.
This is achieved by an open source modeling toolkit (Integrating Modeling Toolkit,
IMT) that offers several functions for translating, storing and coupling different mod-
ules based on a general mark-up language using the extensible mark-up language
XML. An example for a deﬁnition of a ordinary differential equation can be look
like, compare Section 3.2.2.
<STOCK NAME="P1">
<INIT> 10 </INIT>
<INFLOW NAME="BIRTH">
BETA*P1
</INFLOW>
<OUTFLOW NAME="PREDATION">
SIGMA*P1*P2
</OUTFLOW>
</STOCK>
<STOCK NAME="P2">
<INIT> 10 </INIT>


110
MULTI-PARADIGM MODELING
<INFLOW NAME="PREDATION">
ALPHA*P1*P2
</INFLOW>
<OUTFLOW NAME="MORTALITY">
GAMMA*P2
</OUTFLOW>
</STOCK>
A model documentation may be added to different module entities by adding an URL
to the object speciﬁcation. IMA and IMT are under development. Neither IMT nor
MML can cope with modules that base on partial differential equations.
4.5
SUMMARY AND OUTLOOK
As a summary from this short overview it becomes clear, that model based solution of
environmental problems and computer-based management of environmental systems
requires the setting up of models that satisfy the needs of the given problem, but
that are not developed from scratch. Sufﬁcient resources will rarely be available for
developing entirely new model systems. Model integration has been identiﬁed as the
important step. Several approaches show different possible implementations of model
integration and model coupling. Second, several criteria are derived from scientiﬁc
theory, that help to assess models and that supportthe step of modelanalysis described
in Section 1.3,and that are appropriate especially frommodels that are mathematically
heterogeneous because they are derived from different modeling paradigms.
This part of the book aims at an integration of the modeling languages presented in
Chapters 2 and 3 focusing on the problem of integrating anthroposphere and biosphere
processes. A possible methodological framework for this is the use of hybrid Petri
nets presented in the following chapter. Applications for hybrid ecological models
based on Petri nets are presented in Chapter 6. Finally, Chapter 7 then gives a real
world application to a problem of integratinganthroposphereand biosphereprocesses
including a environmental impact assessment.


5
Concepts:
Hybrid Petri Nets
5.1
INTRODUCTION
5.1.1
Concepts of Hybrid Model Development
Several applications of Petri nets can be found, which model mathematically hetero-
geneous or hybrid systems. Most of them originate in engineering science. Kluwe
et al. (1995) state that a combined “three-layer-model” may achieve an overall opti-
mum in modeling of quantitative and qualitative knowledge. The three-layer-model
consists of a rule-based qualitative layer; an event-based qualitative layer, which is
set up by Petri nets, and a quantitative model layer set up by differential equation
systems. J´avor (1995) proposes the lumping of Petri nets, and methodologies of ar-
tiﬁcial intelligence. Rodrigo et al. (1998) emphasize the interdisciplinary nature of
the modeling task.
Chouikha (1998) proposes the integration of differential equations with Petri nets.
Following this approach there is a relationship between net structure and structure
of a system matrix, which represents a differential equation system whose solution
is given by the fundamental matrix. In this way, it is possible to formulate a basic
equation for the description of continuous net behavior on the basis of the initial
marking and the fundamental matrix. The basic equation provides a formal basis of
this new description, which is necessary for the formal analysis and veriﬁcation of
system behavior.
Applications in ecological modeling by hybrid systems are proposed in (Gronewold
& Sonnenschein, 1998). They offer an object-oriented system modeling cellular
111


112
CONCEPTS: HYBRID PETRI NETS
automata. Petri nets are used here for asynchronous migration of species in cellular
automata. Ewing et al. (2002) suggest Petri nets in event-drivenpopulation dynamics
modeling and assess competing risks.
5.1.2
Aim and Scope of the Development
Requirements for a general integratingconceptof hybridor heterogeneousmodels are
met, for example, by Petri net theory. Hybrid low level Petri nets offer the basis for
a general theory, which combines structure and dynamics and is amenable to various
kinds of extensions (Chouikha &Schnieder,1998). We follow most of the suggestions
from Chouikha and extend them by several properties. The latter comprise time-
weighted and stochastic transitions and integration of differential equation systems.
Petri nets with these extended properties are capable of simulating the dynamics of
mathematically heterogeneous systems, which are structured by net topologies. They
serve as a theoretical basis for the analysis of topological properties and enable the
efﬁcient simulation of complex integrated technical–ecological systems. A simula-
tion tool has been developed, which allows graphical creation of the Petri nets and
includes the above-mentioned functionalities.
5.2
THEORETICAL BACKGROUND
5.2.1
Hybrid Low Level Petri Nets
The purpose of modeling environmental systems, requires the introduction of a non-
standard form of a Petri net with places and transitions. Extensions to the mathemat-
ical formulation of Petri nets are the association of time to transitions, and stochastic
and dynamic behavior of transitions in terms of ordinarydifferential equation systems
and time-discrete systems.
Structure and Topology
A Petri net is a directed graph with two types of nodes,
i.e. places pi ∈P and transitions t j ∈T. Alternate nodes are connected with arcs
a ∈A ⊆(P × T) ∪(T × P) (i.e. a place connected to a transition and vice versa).
Places are locations that hold tokens. The information carried by the token is trans-
formed by the transition nodes of the Petri net.
The state of a Petri net is given by the information of the tokens, the mapping m :
P × + →. It is deﬁned by the distribution of values mi in the places pi in time
τ ∈+ of the Petri net: m(pi, τ) = mi(τ). Real values are allowed for the marking,
which is a non standard extension. Places are also associated with attributes like
capacity c : P →+.


THEORETICAL BACKGROUND
113
Deﬁnition 5.1 (Petri net) A 5-tuple N = (P, m, T, A M, AI) deﬁnes a hybrid low level
Petri net N with
P = {p1, p2, . . .}
places
m : P →
marking
c : P →
capacity
T = {t1, t2, . . .}
transitions
AM, AI ⊆(P × T) ∪(T × P)
arcs
(5.1)
We distinguish between arcs which identify mass ﬂow A M, and ﬂow of information
AI.
Deﬁnition 5.1 up to this point incorporates the structural and qualitative descrip-
tion, the interconnection of events and processes: topology or a so-called conceptual
network.
Let I : T →P denote all input places and O : T →P denote all output places of a
given transition t ∈T:
II(t)
:=
{p ∈P | (p, t) ∈AI}
IM(t)
:=
{p ∈P | (p, t) ∈AM}
O(t)
:=
{p ∈P | (t, p) ∈AI ∪AM}
(5.2)
The functional and quantitative behavior of a Petri net is deﬁned by the speciﬁcation
of transitions and the weights associated with the arcs.
If processes which show different time characteristics are considered, transitions have
to be extendedby an attribute Δτ > 0. One can interpretΔτ as switching or processing
time or duration of execution.
Deﬁnition 5.2 Each transition t ∈T is associated with a switching period Δτ :
T →+. If Δτ is deﬁned for a transition t, the last time of switching is also stored:
τ : T →.
Flux of mass or information is deﬁned by weights associated with the arcs by a
function w : AM, AI →. Arcs from places to transitions are held in a matrix
W−= w−
i j i, j=1,2,..., and arcs from transitions are hold in a matrix W + = w+
i j i, j=1,2,....
The ﬂow from places to transitions is denoted by a negative sign; the ﬂow from
transitions to places is denoted by a positive sign. The incidence matrix is derived by
calculating W = W+ −W−.
Because we want to include extensions, four different types of weighting have to be
considered:
Deﬁnition 5.3 (Weights) Let t j ∈T be a free but ﬁxed transition:
1. Information is not “removed” from places
w−(pi, t j) := 0 for (pi, t j) ∈AI


114
CONCEPTS: HYBRID PETRI NETS
2. Weights are deﬁned by constant values
w−(pi, t j)
:=
wi j ∈+ for each pi ∈IM(t j)
w+(t j, pk)
:=
w jk ∈+ for each pk ∈O(tk)
3. Weights can be deﬁned by a linear relationship to the connected place
w−(pi, t j) := wi jmi(τ) for pi ∈P and wi j ∈+
4. Variable weights are deﬁned by functions which are associated with the con-
nected transition:
w+(t j, pk) := f jk(τ, w j1, . . ., wjn) for all pk ∈O(t j), n = |II(t j) ∪IM(t j)|
Two additional remarks need to be added here. If weights are deﬁned in terms of item
3 or 4 of Deﬁnition 5.3, the mass balance may be invalid in the net. Second, so-called
“reset arcs” may be deﬁned by setting wi j = 1 in step 3 of the deﬁnition. The deﬁnition
of weights introduces quantitative dependencies to the structural information of the
network. The quantitative relations induce the dynamics of the system.
5.2.2
Functional Behavior
Switching Conditions
The functional behavior is deﬁned by the transitions. To-
kens are moved from input places to output places if three conditions are fulﬁlled.
According to the input weights, all input places contain a sufﬁcient amount of tokens,
and according to the output weights, all output places must be able to store the results
if capacities are deﬁned. This is summarized by the deﬁnition:
Deﬁnition 5.4 Consider the transition t j ∈T and the time of simulation τ′ ≥0. If
the following conditions are fulﬁlled
∀pi ∈IM(t j)
:
mi(τ) ≥wi j
∀pk ∈O(t j)
:
mk(τ) + w+(t j, pk) ≤c(pk)
τ′ ≥τ(t j) + Δτ(t j)
(5.3)
the transition switches, which means the following equations are calculated:
∀pi ∈I(t j)\O(t j)
:
m(pi, τ′) = m(pi, τ) −w−(pi, t j)
∀pk ∈O(t j)\I(t j)
:
m(pk, τ′) = m(pk, τ) + w+(t j, pk)
∀p ∈I(t j) ∩O(t j)
:
m(p, τ′) = m(p, τ) −w−(p, t j) + w+(t j, p)
τ(t j) = τ′
(5.4)
The Deﬁnitions 5.1 to 5.4 set up a dynamic system in a very special manner. In
contrast to dynamic systems e.g. based on differential equations the sequence of
processes started is not obvious after model initialization. The sequence is determined
by testing the conditions in Equation (5.3) for all transition t ∈T and each state τ > 0
of the given Petri net N.


DEVELOPMENT PLATFORM
115
Stochastic Time Weighting and Ordinary Differential Equation Systems
This section gives an explanation of the important functional extensions to standard
Petri nets which are introduced by items 3 and 4 of Deﬁnition 5.3.
Let Z be a stochastic variable. The coefﬁcients of its distribution function depend
on the state of the connected places. The switching time Δτ of transition t j can be
estimated, using a random number generator, by
Δτ(t j) := Z(w1 j, . . ., wn j) with (pi, t j) ∈AI, n = |II(t j)|
(5.5)
Deﬁnition 5.5 Let d⃗y
dτ = ⃗g(τ,⃗c,⃗y) specify a nonlinear ordinary differential equation
system with the initial condition ⃗y(0) = ⃗y0 and a set of parameters ⃗c ∈n. The
(numerical) solution can be noted by the concept of ﬂux (Arrowsmith & Place, 1994)
by ⃗y(τ) = ⃗ϕτ(⃗y0,⃗c)
In most cases the given differential equation system may be nonlinear. Therefore the
solution noted by the ﬂux ⃗ϕ incorporates a procedure of numerical integration (Hairer
et al., 1980; Hairer & Wanner, 1980).
In the notation of the Petri net, a differential equation system is applied to a transition
t j by the following steps.
⃗y0
:=
w−(pi, t j) i=1,...,|IM(tj)| and w−(pi, t j) := 1
for (pi, t j) ∈AM
⃗c
:=
w−(pi, t j) i=1,...,|II(tj)| with (pi, t j) ∈AI
w+(t j, pk)
:=
f jk := ϕj,Δτ(τ,⃗c,⃗y0) for (t j, pk) ∈AI ∪AM,
k = 1, . . ., |O(t j)|
(5.6)
5.3
DEVELOPMENT PLATFORM
5.3.1
Overview
This theoretical framework is embedded into a graphical user interface, which forms
the development platform for development of hybrid low level Petri nets 1 (hPEN). It
allows graphical development and controls the simulation run. Figure 5.1 gives an
impression of model development. The following list summarizes the capabilities of
the platform:
• Graphical construction of a Petri net with transitions, places, arcs, and bidirec-
tional arcs.
1See p. 279 for availability of software.


116
CONCEPTS: HYBRID PETRI NETS
Fig. 5.1
Graphical User Interface (GUI) for development of hybrid low level Petri nets. The
development platform runs on any Windows operating system. The Petri net shown represents a
predator–prey model using two stages for population dynamics modeling and the speciﬁcation
of a hybrid transition “predation”. (See p. 279 for availability of software.)
• Speciﬁcations of places with capacities and interconnectionsto external tabular
data (measurement values, temperature data, etc.), see Equation (5.1).
• Deﬁnitionof transitions with static switching time, Equation(5.2), and stochas-
tic switching times using Erlang-k, exponential, equal and normal distributed
stochastic variables, see Equation (5.5).
• Coupling of external models (ordinary differential equation systems, etc.) to
transitions. Initial and parameter values and results are exchanged during run
time, see Equation (5.6).
• Graphical display of simulation results.
• Logging results for each time step to a ﬁle.
• Analysis of the system- or net-comitants, see next section.
• Export of incidence matrices W +, W−in different formats (esp. Mathematica)
for further analysis.


DEVELOPMENT PLATFORM
117
5.3.2
Meta-modeling Concept
Integration of different models deﬁned by other development tools or methodologies
than the Petri net concept requires the deﬁnition of an appropriate interchangeformat.
For instance, the transfer of initial conditions and parameters to a differential equation
solver that solves equations deﬁned according to Equation (5.6) requires a well-
deﬁned protocol. This is a task of meta-modeling and model documentation, see
Section 4.4.1.
Figure 5.1 displays how this is performed within the Petri net development platform.
External models are integrated in the Petri net bythe speciﬁcationofthe command line
sequencewhichstartstheexternalcomputermodelwiththecommandlineparameters.
Additionally, interface ﬁles may be used to exchange information such as initial
conditions and parameters. The modiﬁcation of these interface ﬁles follows a very
ﬂexible concept. Parameter values to be read or written by the Petri net development
platform are replaced by user deﬁned keywords. This enables data exchange based
on text ﬁles and command line instruction.
5.3.3
Core Simulation Algorithm and Model Analysis
The Petri net can be deﬁned usinggraphicalrepresentations. Transitions are identiﬁed
with squares, places with circles and arcs with arrows. Boxes with rounded corners
identify an external model, e.g. an integrated differential equation system. See for
instance in Figure 5.1 the population dynamics model for the predator–prey interac-
tion. In addtion, the notation in the development platform one might use solid arrows
to denote mass ﬂow and dashed arrows to identify ﬂow of information. Transitions
and places may be named and comments may be added to each model element (p, t).
The core algorithm, which evaluates Equations (5.4) to (5.6), is displayed in Figure
5.2, which summarizes the actions performedfor runninga dynamic simulation based
on a hybrid Petri net in a very aggregated way. The extensions to standard Petri nets
require precise formulation of the calculation sequence. The main loop starts with
the activation of all transitions and an input of external data. In the next step the ﬂow
of mass and information is set up using the incidence matrix W −according to items 2
and 3 of Deﬁnition 5.3, where item 2 is prior to item 3. After this, all simulation tasks
in external transitions are performed. This evaluates item 4 and the second equation
of item 2 in Deﬁnition 5.3. From this W + is obtained and the new marking can be
calculated.
For further analysis net invariant properties, so-called comitants, can be derived from
the incidence matrix W. For instance, the number n i of switching events of each
transition ti (i = 1, . . ., |T|) can be derived by estimating nontrivial solutions of the
equation W · ⃗n = 0 (Chouikha & Schnieder, 1998).


118
CONCEPTS: HYBRID PETRI NETS
data input through
workspace
transcribing data into
incidence matrix
read data from table
data table
matrix-vector addition
setting new activation
times for transitions
activate transitions
calculation passed?
yes
end calculation
set communication
edges
steering external
transitions
no
Fig. 5.2
Flow diagram of core algorithm for simulation of hybrid Petri nets.
5.4
AN ECOLOGICAL MODELING EXAMPLE
5.4.1
Predator–Prey Interactions
The classical predator–prey model (Volterra, 1927) was introduced in Section 3.2.2
on page 81. Denoting the prey population by P 1 and the predator population by P2,
the following system models predator–prey interaction by a nonlinear ODE system
dP1
dt
=
βP1 −σP1P2
dP2
dt
=
αP1P2 −γP2
(5.7)
Refer to page 81 for the description of the terms and parameters. The following pa-
rameters are assumed for this case study: α = 0.002, β = 0.09, γ = 0.01, P 1(0) = 10,
P2(0) = 15. For detailed analysis we focus on the system behavior more qualitatively.
The common results are oscillating phase-displacedpopulationdensities. The system
produces several stable tori or cycles in phase space depending on the initial condition.


AN ECOLOGICAL MODELING EXAMPLE
119
A close look at the underlying processes shows that the process of predating can be
consideredas a event “lynxmeets rabbit” in the system. In the followingthe predator–
prey system is described by an event-based Petri net.
5.4.2
Event-based Modeling of Predator–Prey Interactions
Looking at predator–prey interaction as an event-based system using the conceptual-
ization of a hybrid Petri net leads the following considerations: Populations of prey
and predator are described in one or more places. If we consider age-structured popu-
lations we may want to introducemore than one place for a population,see Figure 5.1.
In this case the “life-cycle” of a species is clearly speciﬁed by arrows. The places are
connected via transitions that denote simple growth (for the prey), simple mortality
(for the predators) and the interacting transition of predation. The latter is speciﬁed
by a analytical function — the terms σP1P2 and αP1P2 — all other transitions are
speciﬁed by parameters introduced in the classical Petri net framework.
This approach can be aggregated or condensed to a version displayed in Figure 5.3.
Using bidirectional arrows the system can be reduced to three places: “predator
Fig. 5.3
Example of an aggregated Petri net model using one place for the population “prey”
(P1) and “predator” (P2). The simulation results as presented within the development platform
are displayed in the pop-up window below.


120
CONCEPTS: HYBRID PETRI NETS
0
5
10
15
20
25
30
35
0
200
400
600
800
1000
1200
P1
t
Petri Net
ODE, Euler
ODE, RK
Fig. 5.4
Simulation results of predator–prey models. The results from the hybrid Petri net
model and the differential equation model are displayed. Note that from the simulation, results
vary depending on the numerical procedure chosen for solving the ODE system.
population”, “prey population” and “dead predators”. A meeting of predator and
prey is again modeled by a nonlinear external transition.
5.4.3
Simulation Results
Figure 5.4 displays the population dynamics of the prey population P 1. The solid
line gives the results from the hybrid Petri net model. The simulations result in the
well-known ﬂuctuating population densities. Figure 5.5 uses the state phase plane to
summarize the simulation results for the two populations P 1 and P2. A striking fact is
that the numerical solution based on the ODE from Equation (3.11) is identical to the
solution from the Petri net. Using equal parameters but changing the model structure
does not change the results.
A closer look at Figure 5.4 shows that there are differences between the two method-
ologies. Figure5.4comparesthesimulationofthePetrinetwiththesolutionsobtained
from the ODE system in Equation (3.11) by a standard Euler method with no step
size control and by a Runge–Kutta 4th order scheme and embedded step size control.
Note, all solutions differ. The solution derivedfrom the RK solution of the ODE is the
only solution that is consistent with stability analysis of the system. The qualitative
result from stability analysis is a stable tori or cycle depending on the initial condition
(Jørgensen & Bendoricchio, 2001). An increase of oscillation with continuing simu-
lation is a numerical artifact and not a property of the mathematical structure. This
is an example for the usually unknown domain of the numerically and structurally
unintended patterns of dynamic systems, as described in Section 2.8.


AN ECOLOGICAL MODELING EXAMPLE
121
2
4
6
8
10
12
14
16
18
20
22
0
5
10
15
20
25
30
35
P2
P1
Petri net
ODE, RK
Fig. 5.5
Results of Petri net model in state phase plane. The dotted line shows the reference
solution estimated by a Runge–Kutta scheme.
It follows that the Petri net simulation can be interpreted as a numerical solution of
the classical predator–prey model, showing that control of domains of stability in
discrete or event-based model is difﬁcult. This is supported by the information on
the stability analysis of the procedure for numerical approximation of the ordinary
differential equation system. An important requirement for the application of a nu-
merical integration procedure to a model system is that the domain of stability of
the numerical differential equation solver (the eigenvalue spectrum) is in the same
range as the eigenvalues of the dynamic system to be solved (Hairer et al., 1980). If
this is not the case, the numerical solution can be anything except the solution of the
differential equation modeled.
5.4.4
Discussion and Extensions
There is a broad range of possible extensions to the classical predator–prey model,
see for instance (Jørgensen & Bendoricchio, 2001). These extensions can be made
to the ODE model as well as to the Petri net. As expected, the way of introducing an
extension clearly varies between the modeling types.
Limitation of Growth
Abioticfactorsofahabitatdeterminethemaximumdensity
of a population carried or supported by this habitat. Capacity limited growth is
introduced into the ODE model by adding the factor (P max −P) to the growth terms
of the model. This introduces a stable attractor Pmax to the system behavior. Starting
from P(0) < Pmax growth will not exceed Pmax.
For the Petri net such a limitation can be incorporated by the deﬁnition of a maximum
size of a place. This a standard attribute of Petri nets. The consequence of such a


122
CONCEPTS: HYBRID PETRI NETS
limited storage capacity of a place, is that, if the place carries its maximum capacity,
all preceding transitions will stop switching. The dynamic behavior of the system
changes, as this is an event-based model.
Density-dependent Predation
Density-dependent predation rates are incorpo-
rated into the model by a modiﬁcation of the predation term P 1P2 in both equations.
Multiplication of this term by a term such as 1 −exp(−(P 1/Pcrit)c) reduces predator
growth, as well as prey death, if prey density is very low. In the Petri net model we
can deﬁne a density-dependent probability of predation success by using different
switching times of the predation transition. Using a stochastic time weighting with a
density-dependent mean introduces the desired density dependence. In addition, by
choosing the distribution one can extend the model with statistical knowledge of the
predation success of the species being studied.
Harvesting
Harvesting a population is denoted by adding a sink term like −H to
the harvested or huntedpopulation. In the conceptual frameworkoffeedback dynamic
modeling (ODE-type models) this formulation leads to the problem of identifying the
optimum or most sustainable yield (MSY). Sustainability in this context means the
stable survival of all populations. It is deﬁned by a threshold level of harvesting
rate that must not be exceeded in order to maintain the population. Frequently this
threshold level itself depends on the population density (of the considered or all
populations). The Petri net allows a very intuitive approach here. In the framework
of Petri nets this modeling task can simply be solved by adding a transition that
withdraws a speciﬁed amount of yield, or number of individuals only if a sustainable
conﬁgurationof populationsis present. Harvestingdependson the event“populations
are sustainable” not on a certain time.
5.5
CONCLUDING REMARKS
An obvious advantage of the techniques introduced here is the graphical represen-
tation, which allows systems to be described in a detailed but clear manner. The
extension of hybrid low level Petri nets offers an integrating platform for hybrid mod-
eling in ecology. With this conceptualization scheme an integration of any model
based on arbitrary mathematical dialects is supported. Second, with Petri nets the
classical deterministic concept of model development is broadened by event-driven
models. Actions and processes started in the Petri net model, depend highly on the
conﬁguration of states in the system. This is the basic principle of a event-based
model and must be distinguished from all modeling approaches presented in the pre-
vious chapters. Even with this ﬁrst example from ecological modeling, the possible
functional spectrum of the concept of hybrid Petri nets has been illustrated. The ca-
pability of this system will be analyzed in detail in the following chapter in different
case studies.


6
Case Studies:
Hybrid Systems in Ecology
6.1
INTRODUCTION
The concept of hybrid low level Petri nets as integrating platforms for environmental
models can be used to study examples from ecological modeling. The ﬁrst case study
extends the crop growth sub-model of the agroecosystem model from Section 2.2.1
to an event-triggered model with changing structure. The second case study presents
a meta-population model analysis of species invasion in fragmented landscapes and
compares this approach with the spatially explicit model based on PDE, as discussed
in Section 3.2.2.
6.2
HYBRID CROP GROWTH MODELS
6.2.1
Modeling of Crop Growth with Dynamically Changing Model
Structures
Crop development depends on biological, chemical, and physical processes and is
related to air temperature, humidity, nutrients, and density of growth. Section 2.2.1
introduced modeling approaches for the underlying processes in detail. The generic
model in Section 2.2.1 was applied to a large number of crops and different data sets.
However, two issues were neglected in this section:
• Crop growth models have to cope with distinct biological stages of annual crop
growth.
123


124
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
• Within these stages structural changes have to be considered (e.g. appearance
of new plant organs).
The simulation of agricultural yield necessitates the predictionof the harvest biomass.
For example, in a wheat growth model, modeling the total biomass is not a suitable
solution, because one has to differentiate between leaf, stem, and ear components.
The emergence of these different components depends on the development stage of
the crop. Crop development is separated into three stages, denoted by development
codes (DC) (see (Zadoks et al., 1974) for encoding of DC): growth during the winter
periodfrom seed to tillering phase (developmentstages DC01 to DC21); development
up to stem elongation (to DC31); and growth from ear emergence(DC51) to maturity.
Figure 6.1 displays a hybrid Petri net which sets up the framework for modeling three
different development stages with three different organs of the crop. Entering a new
development stage is modeled by an event in the Petri net. These events are triggered
by entering a new physiological stage. Physiological stages can be identiﬁed using
the concept of biological time tbiol(t) as deﬁned by Equation (2.5), see Section 2.2.1
on p. 37. Biological time is deﬁned as the integral over the development rate. This
nonlinear dependency between temperature and development rate can be described
by the O’Neill function, see Equation (2.19). The progress of the O’Neill function
describes the rising of the development rate from a temperature of 0 ◦C until a speciﬁc
optimum temperature is reached and the adjacent decreasing of the rate until lethal
temperature. This equation is based upon parameters, which are easily derived from
experimental data.
The differential equation system for the dynamically changing structure is given by
dWL
dt
=
100 rL
1 −
WL
WL,max
if tbiol(t) < tDC21
WL (rL fs(t) −μ)
else
(6.1)
dWS
dt
=
rS WL
λ −WS
WL
if tbiol(t) ≥tDC31
0
else
(6.2)
dWE
dt
=
rE WL
if tbiol(t) ≥tdc51
0
else
(6.3)
The biomass in [kg/ha] of leaf, stem and ear is given by W L, WS and WE. Note,
the leaf compartment can be interpreted as photosynthetically-active component, as
growth of all other compartments depend on the leaf biomass present. For a detailed
discussion on the phenomenology of the crop see (Schr ¨oder et al., 1995).
Based on experiments in the investigation site “Neunkirchen” (see page 40) the bi-
ological time for entering the development stages DC21, DC31 and DC51 were de-
termined: tDC21 = 4.81, tDC31 = 6.41 and tDC51 = 12.7. From this investigation
parameters for development rate rD using the O’Neill function Equation (2.19) were
determined: Topt = 16.8
, Tmax = 35.0
, rD,max = 0.054 and β = 14.7.


HYBRID CROP GROWTH MODELS
125
stem
biomass
leaf
biomass
growth model
leaf
w -
1,1
leaf
biomass
w+
1,2
growth models
leaf & stem
growth models
leaf, stem &
ear
leaf
biomass
w -
2,2
w+
2,3
w -
3,3
w+
2,4
w -
4,3
stem
biomass
w+
3,6
ear
biomass
leaf
biomass
w+
3,5
w+
3,7
O’Neill
function
temperature data
q
rmax
Tmax
Topt
duration
dc21
duration
dc31
Δτdc21
Δτdc21
Δτdc31
Δτdc31
flag:
Δτdc21
flag:
Δτdc51
flag:
Δτdc31
tillering phase
ear emergence
sum of
tempe-
ratur
w -
14,4 / w +
4,14
p1
p2
p3
p5
p4
p10
p6
p7
p8
p9
p11
p12
p13
p14
p15
p18
p16
p17
t1
t2
t3
t4
crop growth model
physiological stage
model
stem elongation
Fig. 6.1
Petri net model for integration of discrete development stages derived by a con-
tinuous model for biological time (physiological stage model, lower part of ﬁgure) and crop
development (upper part of ﬁgure).
Alltheremainingparametersoforgangrowtharedeterminedbyparameterestimation,
as documented in Section 2.3.3. Results are rL = 0.085 d−1, rE = 0.174 d−1,
rS = 0.0091 d−1, μ = 0.0681 d−1, WL,max = 395 kg/ha and λ = 10.6.
Based on this speciﬁcation, the differential equation for the biological time is used
by the Petri net to synchronize all the differential equation systems coupled by the
hybrid Petri net.
6.2.2
Hybrid Petri Net
Structure and Topology
The following processes must be coupled:
• physiological stage model;
• model for biomass production.
The model for biomass production underlies structural changes during the simulation
period. In the ﬁrst two development stages (to DC31) only one compartment can
be identiﬁed (leaf biomass). With the stage of stem elongation (DC31–DC51) two


126
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
0
10
20
30
40
50
60
70
80
90
100
110
120
130
140
150
160
170
180
190
200
210
220
230
240
250
260
270
280
290
300
time [d]
accumulated development rate [1/d]
1991/92
1992/93
1993/94
tillering (dc21)
stem elongation (dc31)
ear emergence (dc 51)
dc21
dc31
dc51
Fig. 6.2
Biological time as a function of different climatic conditions.
compartments are needed to describe crop growth, and in the maturity stage (from
DC51) three compartments are used to describe the processes. The physiological
model determines the structure of the growth model. The length of the different
phases is determined by an external variable, the climate.
Subnet: Physiological Stage Model
In the physiological stage model, the
daily temperatures from sowing till harvest are stored in a table connected with the
transition t4, which calculates the biological time tbiol. This is performed using an
external transition, which integrates the development rate depending on the daily
temperature value and the parameters of the O’Neill function.
A token is put in one of the places p10, p11, or p12, when a development stage is
entered. This activates the transition of the crop growth model, which means that the
differential equation system of the speciﬁc stage is solved numerically.
Subnet: Crop Growth
Three distinct growth models deﬁne the transitions t 1,
t2, and t3.
The differential equations for ⃗y = (WL)T, ⃗y = (WL, WS )T and ⃗y =
(WL, WS , WE)T are solved, when the transitions are activated. This activation of
the transitions is done by the places p10, p11, and p12, which contain a token, if the
speciﬁc stage is reached. The calculation time, switching time in terms of the Petri
net, depends on the length of the physiological stage. This Δτ–value is handed over
to the crop growth transition of the preceding stage by the places p 8 and p9. The
results of the simulation are the harvest biomasses in p5 to p7 at the maturity stage.
6.2.3
Results
The development of the biological time is shown in Figure 6.2 for the years 1991/92
to 1993/94. One can see that the beginning of the tillering phase is reached almost


HYBRID CROP GROWTH MODELS
127
385
581
54
385
535
44
386
555
28
0
1035
2776
0
808
2447
0
899
2431
0
0
6387
0
0
5892
0
0
6149
0
1000
2000
3000
4000
5000
6000
7000
day 175
1991/92
day 201
1991/92
day 280
1991/92
day 173
1992/93
day 194
1992/93
day 275
1992/93
day 178
1993/94
day 201
1993/94
day 289
1993/94
days after sowing and vegetation year
biomass [kg dm/ha]
leaf biomass
stem biomass
ear biomass
Fig. 6.3
Results of crop growth based on climate date from the years 1991/92 to 94/94.
at the same day of crop development each year. The end of the tillering phase in the
vegetation years 1991/92 and 1993/94 was reached after the same number of days but
in 1992/93, it ended one week earlier.
In 1992/93 maturity was observed 275 days after sowing, in 1991/92 after 280 days,
but because of the low temperatures in the summer of 1994 not before 289 days after
sowing (Figure 6.2). As with the biological time, the crop biomass shows a maximum
in 1991/92. This was caused by the mild temperatures during winter and summer.
In 1992/93, the biological time runs more quickly in comparison to the other years.
Wheat reached its maturity stage earlier but with less biomass. The cold winter and
spring of 1993/94 caused a slow development, so the wheat needed a long time for
development but with middle maturity at harvest. Figure 6.3 shows the results of the
simulated biomass for the years 1991 to 1994 for each organ.
This example demonstrates the capability of hybrid low level Petri nets for integration
of continuous and discrete processes includinga structural change of the mathematical
model. The Petri net is used to synchronize the speciﬁc stages with its processes.
Possible extensions in this ﬁrst case study are:
• a transition for a carbohydrate pool;
• retranslocation at the maturity stage;
• nutrient dependency, as described in Section 2.2.1, may be integrated into the
transition, and
• the integration of event-based management, see Chapter 10.


128
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
All these extensions can be supported by the proposed modeling framework of hybrid
low level Petri nets.
6.3
THE GAL ´APAGOS ARCHIPELAGO AND THE BLUE-WINGED
GRASSHOPPER
6.3.1
Meta-population in Island Biogeography
Insular Zoogeography
Colonization of an island, persistence and extinction of a
species depends on the habitat suitability and the distance to the next island or habitat
(MacArthur& Wilson, 1963). Simulationmodels for colonizationthereforecomprise
two processes: migration in spatial irregular structures and population dynamics on
each island or habitat.
The probability for new species to settle on a particular island decreases exponen-
tially with the distance to the living space. On the other hand, the probability for
extinction increases with the number of species resident in a habitat. Species have to
surmount inhospitable areas like oceans, deserts or mountains to reach a new island.
Small, unsuitable habitats may support migration to suitable areas, because two small
migration steps may be more successful than one big step. These islands are called
stepping stones.
The larger the target island’s cross-section, the likelier is a colonization (MacArthur
& Wilson, 1963). The following discrete equation is used to calculate the number n
of individuals that reach an island p1 from the source region p2:
n(p1, p2) = α A(p2) e−λ d(p1,p2) 1
π arctan
1
2
diam(p1, p2)
d(p1, p2)
(6.4)
This equation uses the area of source island p2 denoted by A(p2), the mean distance
d(p1, p2) from island p1 to p2 and the diameter diam(p1, p2) of recipient island p1
taken at a right angle to the direction from p1 to p2. This information is calculated us-
ing a geographic information system. The calculated number of individuals reaching
p1
p2
Destination Habitat
Habitat of Origin
p3
Stepping Stone
β
(
)
2
1, p
p
d
(
)
2
p
A
(
)
2
1, p
p
diam
Fig. 6.4
Visual representation of the angle of visibility of a species migration from habitat
p2 to p1. Additionally the migration path using a stepping stone island is sketched.


THE GAL ´APAGOS ARCHIPELAGO AND THE BLUE-WINGED GRASSHOPPER
129
an island p1 from p2 per time step n(p1, p2) requires the speciﬁcation of the parameter
λ which denotes the reciprocal of mean travel distance per time step and the number
of individually leaving recipient island α. These parameters are species-dependent.
Figure 6.4 visualizes the approach by MacArthur & Wilson (1963). The angle or
visibility of the destination habitat β is estimated by
β = 2 arctan
1
2
diam(p1, p2)
d(p1, p2)
(6.5)
If we divide this expression by the angle of a fullcircle, 2π, we can derive the fraction
of destination habitat that take part, with respect to all possible direction of migration,
the full cirlce.
Reproduction
Reproduction of individuals is estimated by the logarithmic growth
dP(p)
dt
= r P(p)
1 −P(p)
C(p)
(6.6)
P(p) denotes population density on island p. Parameters of habitat suitability are
introduced by the carrying capacity C(p) of habitat p and the growth rate r. The latter
is assumed to be constant for all islands. This continuous approach is suitable for
most insect populations and many other species (Richter & S ¨ondgerath, 1990).
In this ﬁrst approach C(p) is assumed to be linear depending on the island area
C(p) = γA(p), with a ﬁxed coefﬁcient γ > 0. For this ﬁrst case study the parameters
were arbitrarily set to γ = 0.1 and r = 0.06 1/h.
Case Study
For detailed analysis the Ecuadorian Gal´apagos islands were selected
as a typical oceanic archipelago. The Gal´apagos archipelago is located 1050 km west
of the shoulder of South America and contains 13 large islands, 6 small islands, and
42 islets with a total area of 8006 km2. Isabela, the largest one, is 4278 km2. The
distances between the islands range from 4 to 68 km. The archipelago’s geology
is completely volcanic and the vegetation ecosystem varies from rain forest to dry
habitats with sparse vegetation. 378 species are endemic: 60% have been introduced
by birds, 31% by wind, and 9% have been ﬂoated across the ocean. Nearly 800
species have been introduced by humans since 900 AD.
However, even if the Gal´apagos’ ecosystems suffered from several non-endemic
species, intruding the archipelago, this is clearly an artiﬁcial simulation experiment:
The blue-winged grasshopper, Oedipoda caerulescens (Linnaeus, 1758) is a palae-
arctic species with a distribution from North Africa and the Canary Islands in the
south to Central Europe in the north. Eastwards the distribution reaches Southwest
Asia and China (Harz, 1975). The xerothermophilousspecies can be found in regions
from plains up to mountains with sparse vegetation. These grasshoppers move about
10 m daily on average, but migration distances of 800 m per day have been recorded
(Appelt, 1996; Appelt & Poethke, 1997). In 1996 it was observed that Oedipoda


130
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
59
59
26621
2282
7730
8170
8456
74
74
74
74
75
97
82
97
73
332
(59)
(2282)
(14)
(1)
(8)
(23)
(23)
(258)
(59)
(26562)
(440)
(726)
(7671)
(1)
(1)
(1)
(1)
0 1000 km
Galápagos
Islands
Ecuador
South America
Fig. 6.5
Map of the Gal´apagos archipelago overlaid with the Petri net of a meta-population
model. Transitions with rounded corners specify the continuous population dynamic model,
differential equation. The numbers on the arcs denote the ﬁrst possible colonization of an
island. The numbers in brackets denote the average time in years grasshoppers need to migrate
from one island p1 to another p2: n(p1, p2)−1.
caerulescens have expanded their habitat from the island Rottumeroog to the island
Borkum, both located in the North Sea. The distance between these two islands is
4.7 km. From these observations we derived α = 0.11/km 2 and 1/λ = 6 km using
digital maps of the Gal´apagos archipelago in a GIS for the estimation of A(p), d(p),
and diam(p).
6.3.2
Spatially Explicit Hybrid Petri nets
Figure 6.5 shows a map of the larger islands of the Gal ´apagos archipelago overlaid
by the Petri net developed to estimate the expansion and population dynamics of
O. caerulescens. Each place represents the species’ population on an island. The
transitions with roundededges are connectedby bidirectionalarcs to the island places.
They model the population dynamics based on Equation (6.6).
The process of migration is modeled by stochastic transitions, which connect the
island places. Switching time of a migration transition is deﬁned by an equally


THE GAL ´APAGOS ARCHIPELAGO AND THE BLUE-WINGED GRASSHOPPER
131
distributed stochastic variable with the expectation value
n(pi, p j)−1 : Δτ(t j) = Z n(pi, p j)−1
with pi ∈I(t j), pk ∈O(t j).
In Figure 6.5 numbers at the arcs denote the mean travel time from one island to
another (numbers in brackets) and the date of the ﬁrst possible appearance at an
island after individuals have been released on San Crist ´obal. Calculating the shortest
route in the network using GIS functionality derives the latter.
6.3.3
Results
The following behavior is a typical result of the simulation experiments of intra-
archipelagic migration: reproduction starts as soon as the ﬁrst two grasshoppers are
released on San Crist´obal. Santa Fe is the ﬁrst island reached after a few years, but a
small grasshopper population is no guarantee for a durable colonization. Grasshop-
pers may vanish on Santa Fe a few years after their settlement. Nevertheless, some
individuals made the step from Santa Fe to Santa Cruz. There they were able to es-
tablish themselves and their population grew. Thereafter the ﬁrst individuals reached
the largest island Isabela using Santiago, R´abida, or Pinz´on as stepping stones.
The right-hand part of Figure 6.6 demonstrates that on smaller islands the population
is more often extinct than on larger ones. Reasons are the smaller population size
and the emigration rate. The left part of Figure 6.6 shows the population sizes for all
considered islands. For clarity, the population sizes of some selected islands can be
seen in the right part of Figure 6.6. On some islands, the number of individuals varies
widely depending on time. This effect has been observed in many ﬁeld studies and
is caused by the migration and immigration of grasshoppers.
The importance of the stepping stones can be quantiﬁed by analysis of the switch-
ing frequency of the migration transitions (part of net comitant). Figure 6.7 shows
different pathways from the island San Crist ´obal to Isabela using different stepping
stones. The thickness of the arrows denotes the relative importance of the migration
route with respect to the total number of migration events. The absolute number of
events is noted on the arrows.
One can see that the settlement of the island Isabela is mainly caused by the population
dynamics on the Island Santa Cruz and Santiago. The stepping stones Pinz ´on and
R´abida are used to reach Isabela.
This case study shows that
• the framework of hybrid low level Petri nets enables the integration of dynamic
populationmodels with migration or meta-populationmodels based on statistic
approaches;
• the net structure and network parameters may easily be set up by information
derived from GIS, which enables spatial simulations; and
• net comitants of Petri nets support an analysis of the developed model.


132
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
0
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
0
50
100
150
200
250
300
350
400
450
500
550
600
650
700
750
800
850
900
950
1000
time [a]
individuals
0
20
40
60
80
100
120
140
160
180
200
220
240
260
280
300
320
340
360
380
400
420
440
0
50
100
150
200
250
300
350
400
450
time [a]
individuals
San
Isabela
Floreana
Santa Fe
Santa Cruz
Pinzón
Cristóbal
Fig. 6.6
Results of population dynamics on different islands of the Gal´apagos archipelago.
The left ﬁgure shows the number of individuals of the larger islands Isabela and San Crist´obal.
The right ﬁgure shows the population dynamics of possible stepping stone habitats like Floreana
or Pinz´on.
6.3.4
Comparison
Spatially explicit population dynamics can be modeled by a partial differential equa-
tions system, see Section 3.2.2. This approach is applied to this Gal ´apagos example.
The parameterization of the PDE can easily be performed. Most of the required in-
formation is available from the model development. Parameters required for a single
species PDE-migration model are the growth rate r,carrying capacityC and migration
distance of dispersal coefﬁcient. The Petri net model uses a logistic growth model
which is speciﬁed by a growth rate and a carrying capacity. The latter depends on
the size of an island. This information is sufﬁcient for speciﬁcation of the right hand
side of Equation (3.10). The dispersal coefﬁcient D can be speciﬁed from the average
migration distance known for O. caerulescens.
Figure 6.8 displays six time frames of this simulation. The upper left picture shows
the initial population deﬁned on San Crist ´obal. With t = 75 a because of migration or
dispersal the populationdensity on this island decreased. It needs the same time for an
establishment of the population on the ﬁrst big stepping stone Santa Cruz (t = 150 a),
as habitat is more suitable for the grasshopper population growth. The next islands
are settled very quickly as several smaller islands support migration by their stepping
stone function. The last time steps chosen are t = 225 a and t = 250 a. Note the
population at Isabela reaches 250 individuals in accordance with the results from the
Petri net model. Note, the scale for the density plots in Figure 6.8 is deﬁned according
to the population densities of the early time steps.
Using the partial differential equation model, an analysis of the migration pathways
can be derived from a grasshopper-tracking analysis, a function most FEM-solver
programs are capable of, usually known as particle tracking. Figure 6.9 shows such


THE GAL ´APAGOS ARCHIPELAGO AND THE BLUE-WINGED GRASSHOPPER
133
Isabela
Santa Cruz
Santiago
San
Cristóbal
Floreana
Espanola
Santa Fe
Pinzón
Rábida
0
3
1
98
325
101
376
236
242
370
457
0
0
0
0
3
325
Migration Analysis
0% - 3.4%
3.4% - 6.8%
6.8% - 10.2%
10.2% - 13.6%
13.6% - 17%
17% - 20.4%
Fig. 6.7
Analysis of migration pathways of O. caerulescens in the Gal´apagos archipelago.
Based on a 2.500 year simulation the movement of individuals between two islands are counted
and noted at the arrows.
a grasshopper tracking analysis for time step t = 142.5 a. Each line displays the
migration pathway for an interval of 100 years. A general statement compared to
Figure 6.7 is difﬁcult to derive from the PDE-model. In the simulation the most
frequent (San Crist´obal, Santa Fe, Santa Cruz, Isabela) paths are displayed, which is
in accordance to the Petri net model.
Both modeling approaches may be applied to the problem in hand. Both methodolo-
gies show advantages and disadvantages. For detailed comparison of the two model-
ing approaches Table 6.1 gives a summary of different aspects. In terms of scientiﬁc
theory the partial differential equation system is the more concise, more aggregate
model with a broad range of resulting explanations (compared to the parameters fed
into the model). This equation collects the processes in one core equation. On the
other hand, with this model we can run into more problems concerning numerics and
interpretation. For instance, how shall we interpret positive population values (below
unity) for open water regions? Shall we suggest the more phenomenologicalPetri net
model, which has no physical explanation of Equation (3.10)? Or, is Equation (3.10)
the building block for the migration process in patchy habitats?


134
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
Fig. 6.8
Six time steps of spatially explicit population dynamics of O. caerulescens based
on partial differential equation. Shown are (from upper left to lower right) the time steps
t = 0, 75, 150, 200, 225, 250 a. (See p. 279 for additional resources.)
Modeling biological systems requires the development of mathematically heteroge-
neous or hybrid systems. This is because temporal or spatial processes show both
discrete and continuous behavior. Hybrid models based on different mathematical
modeling languages are the common result in ecological modeling. One possible
general approach to these is the concept of hybrid Petri nets as described in the here.
Analysis of the dynamic behavior of systems like these is indispensable when com-
paring and assessing different modeling approaches. The examples in this chapter
showed that entirely different modeling approaches produced qualitatively, and to a
certain degree quantitatively, equal dynamic behavior.
However, this can only be a starting point. Analysis of dynamic behavior includes
concepts of stability analysis and dynamic and spatial invariant properties. This may


SUMMARY
135
Fig. 6.9
Example of migration analysis based on partial differential equation system: A
grasshopper tracking analysis.
be achieved by comparing the topologies derived from different dynamic simulation
models.
Formoredetailedstudiesthemethodologypresented—comparingdifferentmodeling
approaches — allows dynamic properties of models derived from different hybrid
mathematical approaches to be studied, and enables the building blocks of ecological
models to be identiﬁed. This might be a fruitful research topic, as it offers a deep
insight into the relationship of different approaches in ecological modeling and might
help to identify the building blocks of ecological models.
6.4
SUMMARY
Both applications show capabilities characteristic of the system. The application
focussing on the hybrid crop growth model shows how a discrete system controls
the state and structure of a continuous differential equation system depending on
the states of a second differential equation. The application of the Gal ´apagos meta-
populationmodelshowshowstochasticdiscretesystemsofmigrationarecoupledwith
continuous systems for population dynamics. Furthermore,in this example properties
of places are extended by spatial properties derived from geographic information
systems. Additionally, Petri net theory supports the examination of these systems.
Besides the analysis of the system behavior of differential equation systems (stability),
the topology of the network can be investigated by the incidence matrix and dynamic
structure can be analyzed using the net comitants.


136
CASE STUDIES: HYBRID SYSTEMS IN ECOLOGY
Table 6.1
Comparison of the two modeling methodologies.
Petri net
Partial Differential Equation
Processes
Dynamics
Continuous (growth)
Continuous
Spatial
Stochastic, discrete (migration)
Continuous
Data
Topology of
habitats
The only information implemented into
the Petri net is the topological relation
between the habitats/islands
No information on topology of habitat
patches deducible from FEM-mesh
Geometry of
habitats
Only aggregated indicators on the geom-
etry of the archipelago are fed into the
PN-model: distance, diameter of a habi-
tat.
FEM-mesh directly derived from habitat
borders, imported from GIS.
Analysis,
Results
–
Stochastic analysis, Monte Carlo
analysis
–
Event-based model
–
stepping stones
–
Migration distance
–
Numerical solution by FEM using
adaptive mesh generation
–
Experimental migration pathways
–
Migration distance
–
Nonnegative populations for open
water regions
Classiﬁcation
Empirical approach
Physical foundation on well-known dif-
fusion/migration and growth models.
The important capability of the system is model development for anthroposphere–
biosphere interactions. A general concept at global scale is presented by Schellnhu-
ber (1998) based on a theoretical system approach in terms of ordinary differential
equations. In classical ecosystem models, anthropogenic effects enter the system as
environmental covariables or indirectly via the control parameters. Models of tech-
nical systems are primarily devised for process control and optimization and yield at
most the order of magnitude of emission rates. In reality both systems are closely
interlocked and should be treated as a whole at least at higher scales, see Section
1.3.4, p. 20. Environmental impact assessment of human activities necessitates a
comprehensive analysis of both industrial and ecological systems.


7
Applications:
Environmental Impact
Assessment
7.1
INTRODUCTION
Life cycle assessment (LCA) is widely used as a tool for assessing the environmental
aspects and potential impacts of products and services. While the methodology is
well developed for the steps goal deﬁnition and life cycle inventory (LCI), impact
assessment is still under discussion (Pohl et al., 1996; ISO, 1997).
The Society of Environmental Toxicology and Chemistry (SETAC) called for the
development of models which integrate the fate and impact of emissions in the as-
sessment of the life cycle of products (SETAC, 1993). There is also a need for expert
systems which facilitate the step of impact assessment within LCA (SETAC, 1993).
German Federal Environmental Agency (Umweltbundesamt) requests consideration
of global and local impacts within life cycle assessment (LCIA). The SETAC LCA im-
pact assessment work group asks for an integration of different techniques to conduct
a more complete and holistic environmental assessment (SETAC, 1997). Suitable
quantiﬁcation parameters exist for the calculation of the potential environmental im-
pact of emissions on a global scale such as global warming or tropospherical ozone
depletion. Impact potentials like global warming potential (GWP) or ozone depletion
potential (ODP) are already widely used in LCA.
The intensity of local and regional impacts, for example acidiﬁcation or eutrophica-
tion, depends on variable environmental conditions and is therefore site dependent.
Hence many authors, for instance Owens (1996), Tolle (1997) and Krewitt et al.
(1998), state that the concept of global parameters is not useful for the LCIA of lo-
cal and regional impacts. A research goal is then to develop and evaluate suitable
methods for assessing local and regional impacts within LCA.
137


138
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
7.2
AIM AND SCOPE
An appropriate methodological concept that can solve the problem of site-dependent
impact assessment of goods and services requires an integrated spatially explicit
model. The required integration can be achieved by the use of a hybrid Petri net.
The intention of this case study was to develop a generic concept for an integrated
approachfor environmentalassessment where LCI, environmentalfate modeling, and
environmental impact assessment together can be used as a tool to assess local and
regional impacts of emissions released along the life cycle of products. The actual
impacts at the point of emission for several impact categories ought be addressed
site-dependently. This approach is unusual, as it suggests a truly integrated approach.
It reaches far beyond LCIA by the use of other environmental modeling techniques.
This study was carried out in a co-operation with the Department of Environment
and Transportation of Volkswagen AG, Wolfsburg (Thiel et al., 1999). The following
section summarizes the basic concept of the general assessment model followed by
the description of a prototypical implementation of an application and the results.
7.3
METHODOLOGY
To meet the required extensions for a truly integrated approach, a general method was
developed which consists of three modules. These are:
• life cycle inventory;
• environmental fate modeling, comprising chemical reactions and the spatial
spread of emissions;
• a detailed environmental impact assessment based on the results of the previ-
ous step and operated by fuzzy expert systems, which allow an assessment of
ecological impacts for several categories at one site involved in the system life
cycle.
Figure 7.1 summarizes this methodological concept. In the upper part of the ﬁgure
the LCI phase is symbolized by a small Petri net. Petri nets are suitable for modeling
production processes, as these processes are frequently discrete and show all the
properties of event-based systems. Moreover, the Petri net model can be extended to
represent the entire life cycle of the product.
Production, use, and deposition as well as recycling of products, leads to emissions.
In this integrated concept emissions are traced by an environmental fate model. The
environmental fate model covers the processes of transport through different media
(atmosphere, soil, or water) and possible reactions the substances go through during
transport. Finally a substance reach environmental sinks, which are identiﬁed as
receptors of immissions. In this case study the focus is on atmospheric transport


METHODOLOGY
139
Fuzzy-Expert
-System
Dispersion
-Model
Life Cycle
Inventory
Soil-Acidification
Eutrophication
Ecosystem
Damages
Chemical Reactions
Dispersal
Winddrift
-20
0
20
40
60
80
100
0.0
0.2
0.4
0.6
0.8
1.0
center of gravity
no effect
low
medium
high
very high
membership degree
acidification impact 
(difference of immission and buffer capacity)[mol H+/ha a]
 Output set
Production Process
Rule based
impact assessment
Site Characteristics
Deposition (Spatially explicit)
Responses
Emissions
x
y
z
Vk
Vk+1
5°
Photochemistry
Deposition
Transport out
Transport in
Point of Emission
Background
concentration
Cx
Solar radiation
Mixed Layer
Volume Vk
Fig. 7.1
Methodological concept of the integrated approach for life cycle impact assessment.
of NOx. Soil, ecosystem, and plant are used as examples. They may be replaced
by any other receptor whose potential impacts have either a regional or local spatial
environmental sensitivity, see bottom of Figure 7.1.
Note, that from top to bottom of Figure 7.1 several methodological boundaries are
crossed. This methodological spectrum covers deterministic modeling (event-based
and continuous) and application of soft-computing methods. Soft-computing meth-
ods, in this example fuzzy expert systems, are used for the assessment of environmen-
tal impact on soil acidiﬁcation, eutrophication, and plant damage. The uncertainty of
the knowledge and the imprecision of the information increases from top to bottom
of the ﬁgure.
7.3.1
Life Cycle Inventory
LCI was performed using the theoretical background of Petri nets, cf. Chapter 5.
Material and ﬂow analysis are modeled by a network approach based on the Petri


140
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
nets. Production and transport processes are identiﬁed with transitions. The transi-
tions are the graphical representations of the mass and energy ﬂow equations of the
different processes. Storage places, products, raw material deposits, and emissions
are identiﬁed with places.
To undertake a LCI of a product, the sites of production are usually known (otherwise
the transport distances could not be determined). We did not aggregate the same
processes at different sites to unit processes but designed the Petri net in such a
way that we could calculate the site-speciﬁc mass ﬂows of the stationary emission
sources. Knowing annual production for the studied product,the mass ﬂow values can
be transformed into mean annual in- and output values. The site-speciﬁc emissions or
output places deﬁne the interface between the LCI and environmental fate modeling.
7.3.2
The Link: Environmental Fate Modeling
Environmental fate models support the calculation of the spatial spread of emissions
starting from the point of emission, providing the results as concentrations and im-
missions in space and time. It thus models the source–receptor relationship. The
environmental fate of emissions can be modeled by different approaches for the me-
dia soil, water, or air. All dispersion models are based upon systems of differential
equations which contain terms for transport, chemical reactions, and deposition pro-
cesses, see Chapter 3.
The sites of emission from the LCI have to be geographically localized. Their mass
ﬂows are identiﬁed as sources in the context of a dispersion model. Output places
from the LCI may be mobile (e.g. transports) or stationary point sources (e.g. stacks)
or diffuse inputs (such as nitrogen leaching out of agricultural sites). It depends on
the observed process (in the transitions) of the LCI. The GIS supports these different
types of information exchange from LCI results to reaction dispersion models.
Modeling the spatial spread of emission also depends on the observed media. Several
modeling approaches exist for transport modeling in atmosphere, water, or saturated
and unsaturatedsoil horizons, see Chapter 3. It is useful to couple models for different
media. In most cases the emitted substances pass from one medium to the other.
7.3.3
Fuzzy Expert Systems for Impact Assessment
Basic Concept
The results of the environmental fate modeling are used to assess
the exposure of environmental components to a certain substance or burden, cf. Fig-
ure 7.1. In the integrated approach the assessment is performed by a fuzzy expert
system, which links the results of transport modeling and environmental receptors.
The ﬁrst two phases of the integrated LCA approach, presented in Sections 7.3.1
and 7.3.2, describe physical and chemical processes which can be simulated by de-
terministic models. The ecological impacts of immissions are a result of complex
interactions, which can often be described only by heuristic approaches (Kelly &


METHODOLOGY
141
Harwell, 1989). Nevertheless, the causality between the exposure to a burden and the
response of a receptor can often be described by expert knowledge.
An environmental impact assessment tool must be capable of dealing with imprecise
data and must be able to come to a conclusion despite the uncertainty. An adequate
method for mathematical modeling of processes which deal with uncertainty is fuzzy
logic. In classical set theory the membership of an object x to a set A out of a class X is
deﬁned by the two values 1 if x belongs to A: x ∈A and 0 if x  A . In fuzzy set theory
a set A is characterized by a membership function μ : X →[0, 1] which assigns to
each object x ∈X a grade of membership to the set A ranging between zero and one.
This property of fuzzy sets can be useful in environmental impact assessment. For
example, the transition from favorable to unfavorable environmental conditions for a
receptor is often not crisp but fuzzy. The notions and operators of classical logic have
been extended to fuzzy sets within the theory of fuzzy logic allowing approximative
reasoning under uncertainty (Yager & Zadeh, 1992). The theory of fuzzy fogic is
outlined in Zadeh (1965).
One of the ﬁrst application of fuzzy logic in modeling social systems with non-
measurable variables was presented by Seppelt (1998). Based on these principal
ideas, a generalized exposure–response model using fuzzy logic was developed to
assess the environmental effects of the calculated immissions. Figure 7.2 shows the
structure of the generalized model. The use of fuzzy set theory in expert systems not
only allows crisp values from LCI to be used as input variables, but also linguistic
terms can be used in the database. In ecological assessment this is a particularly
important advantage.
Generic Expert System for Impact Assessment
In the ﬁrst step,the sensitiv-
ity of a receptor to a certain exposure is deﬁned by a buffering capacity. This concept
is well-known in soil science and agrochemistry, where it means the capability of the
soil to neutralize acid input or withdrawal of nutrients. For the integrated approach
we generalized this concept. The buffering capacity takes into account the ability
of the receptor in most of the exposure–response relationships, to buffer exposures
without showing any measurable effect. The buffering capacity depends on regional
characteristics. In Figure 7.2 the sub-model which calculates the buffering capacity
is shown in the box named environmental conditions. Here, the parameters 1 to n
represent environmental characteristics and determine the buffering capacity. The
sub-model for the calculation of the buffering capacity is applied to the different im-
pact categories, for example soil acidiﬁcation or eutrophication. The interdependence
of the environmentalcharacteristics and the bufferingcapacity has to be deducedfrom
expert knowledge.
In the second step, the possible response of the receptor is assessed by comparing
the buffering capacity with the immission values. If the immission values exceed the
buffering capacity, a measure for the potential ecological impact of the immission is
derived.
The environmentalassessment is performed by fuzzy expert systems in the integrated
LCA approach. In Figure 7.2 the squares represent variables whose different expres-


142
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
Buffering
Capacity
Exposure
Parameter n
Parameter 1
Response
Link to 
Environmental
Fate Modelling
Environmental 
Data
Environmental 
Data
Environmental 
Conditions
Fuzzyfication
Fuzzyfication
Fuzzyfication
Defuzzyfication
(if required)
Environmental Assessment 
Fig. 7.2
Structure of the generalized fuzzy expert system for environmental assessment of
substances exposure as an extension of a dose–response framework based on critical load
concept.
sions are deﬁned by fuzzy sets. The triangles represent rule nodes. A typical rule
could be: “if parameter 1 is low and parameter 2 is low, then the buffering capacity
is low”. The membership functions of the generalized response variable are deﬁned
as follows: If the membership degree of the fuzzy sets of “no effect” and “low” are
equal, then the defuzzyﬁcation of the result by center of gravity leads to the value 0,
see Figure 7.3. The response variable can easily be adapted to different receptors by
rescaling of the x-axis. Units for the x-axis should be chosen so that defuzzyﬁcation
leads to crisp values which represent determinable effects.
The fuzzy sets of the immission, the buffering capacity and the response variable are
deﬁned in connection with the rule node in a way that, when the immission exceeds
the buffering capacity, this leads to positive response values (i.e. negative effects). In
the opposite case the output of the response variable is “no effect”.
There are two alternatives for the interpretation of the resulting output:
• The ﬁrst possibility is to have the output as linguistic variables. As the resulting
output the fuzzy set with highest membership value is chosen. This could be
for example: “possible damage is very high” with the membership degree 0.6.
• The second alternative is a crisp value after defuzzyﬁcation. This is a theoretical
value which represents the difference between immission and buffering capac-
ity. Hence the impact on the receptor can be quantiﬁed and model estimates
can even be evaluated in on-site measurements.


LIFE CYCLE INVENTORY OF THE PRODUCTION PROCESS
143
-20
0
20
40
60
80
100
0.0
0.2
0.4
0.6
0.8
1.0
center of gravity
no effect
low
medium
high
very high
membership degree
acidification impact
(difference of immission and buffer capacity)[mol H+/ha a]
Output set
Fig. 7.3
Membership functions of the response-variable soil-acidiﬁcation.
System Speciﬁcation
The implementation of a fuzzy system requires the speci-
ﬁcation of a considerable number of parameters and options. The observance of all
the criteria described above leads to transparent and plausible conclusions within the
systems. For the development of the LCIA fuzzy expert systems the following rules
are used to minimize the number of free parameters in the fuzzy expert systems:
• deﬁnition of ﬁve fuzzy sets with normalized membership-functions per vari-
able: sets from “very low” (respective to “no effect” for the response sets) up
to “very high”, see also Figure 7.3;
• sum of all membership values over all fuzzy sets per variable equals one;
• deﬁnition of the membership functions in a way that one value can belong at
most to two different fuzzy sets;
• use of minimum operator for modeling of an “and”-connectionin the premises;
• use of maximum operator for modeling of an “or”-connection in the premises;
• use of Mamdani implication for the conclusion procedure;
• use of supremum-minimum operator for the propagation;
• (if desired:) ﬁnal calculation of a crisp value (“defuzzyﬁcation”) by the center-
of-gravity method.
7.4
LIFE CYCLE INVENTORY OF THE PRODUCTION PROCESS
The following section sheds light on the application of the modeling and assessment
concept presented above. The approach was applied to the life cycle of car compo-
nents produced by Volkswagen AG. A life cycle inventory has been prepared for the


144
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
planned production of magnesium (Mg) door parts using the annual Polo production
in Wolfsburg of 1995. The environmental fate modeling focused on the fate of emit-
ted nitrogen oxides as they cause several typically regional or local impacts. In the
environmental assessment of the NOx-emissions the possible response of the three
receptors crop, soil, and ecosystem were assessed.
The following processes were investigated in the LCI for the planned production of
the magnesium door parts:
• raw magnesia production,
• production of the alloy Mg-AM 60,
• smelter,
• die casting,
• part ﬁnishing,
• chromate treatment,
• recycling of the production residues (leading to input of secondary Mg-AM 60
in the smelter),
• transportation between the different production sites as well as the recycling
facilities.
The Mg-production and alloy production take place in Israel at the Dead Sea Works
plant, cf. Figure 7.4. The other processes from smelter to chromate treatment take
place in Germany. The data for the production activities were provided by Volkswa-
gen. The transportation processes between the production sites were calculated using
databases from the underlying LCI tool Umberto. The portion of secondary Mg-AM
60 input in the smelter was assumed to be 24.7%.
NOx-emissions are chosen for detailed study: The results of the LCI show that more
than 80% of the NOx-emissions are released in the ﬁrst two processes at the Dead Sea
Works in Israel. The remaining NOx-emissions occur at energy production sites in
Germany (16.8%) and in other operations (1.9%). The high share of NO x-emissions
in Israel is mostly due to the fact that at Dead Sea Works the energy demand is
covered by a power plant burning residual oil. The power plant is located in Israel
at the southern end of the Dead Sea. Hence, in the environmental fate modeling, we
focused our attention on the environment of this site. The emission results of the
LCI yield the input ﬂow of the reaction–dispersion model. We made calculations for
the annual Mg production of approximately 30000 t at Dead Sea Works. The annual
demand due to VW-Polo production is only about 8.2% of this amount. However,
to estimate the potential impact of the NOx-emissions on the environment near the
power plant, the calculations should be based on the energy demand for the entire
annual Mg production at this site.


ENVIRONMENTAL FATE MODELING OF NOX-EMISSIONS
145
Fig. 7.4
Location of Dead Sea Works plant south of Dead Sea, Israel.
Assessment of
emissions as a consequence of the production located at Wolfsburg factory in Germany. From
this plant have to refer to the environmental conditions of the surrounding study area.
7.5
ENVIRONMENTAL FATE MODELING OF NOx-EMISSIONS
7.5.1
Overview
Three different concepts can be distinguished for modeling atmospheric transport of
substances.
1. Physical models, that describe the processes of the Ekman layer with its tur-
bulent processes based on Navier–Stokes equation (Seinfeld & Pandis, 1998).
Using this methodological concept for the problem in hand, one has to solve
a system 3D partial differential equation, one equation for every substance.
These equations are coupled by their reaction terms. This approach therefore
creates an enormous numerical effort.
2. Stochastic models, that represent the process of dispersal by a spatially ex-
plicit stochastic variable, that gives several realizations of a random function
describing a puff (Liu & Du, 2003).
3. Aggregated models,that use analytical solutions of theNavier–Stokes equation,
or an arbitrarily chosen discretization of the spatial variable, together with
knowledge of the stochastic process of dispersal to parameterize analytical
equations (Seinfeld & Pandis, 1998).


146
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
x
y
z
Vk
Vk+1
5°
Photochemistry
Deposition
Transport out
Transport in
Point of Emission
Background
concentration
Cx
Solar radiation
Mixed Layer
Volume Vk
Fig. 7.5
Concept of atmospheric transport model for the processes of diffusion and wind
spread according to the box-model approach. Conceptual model of environmental fate model.
The processes of transport, reactions and deposition are assumed to be constant for a deﬁned
box of the atmosphere.
Integrated models result from modeling processes, that use discretization of aggre-
gated partial equations. Similar to the matter transport example from Section 3.2.1
environmental fate modeling of substances in the atmosphere requires consideration
of the two processes, transport and reaction.
7.5.2
Atmospheric Transport Model
The environmental fate modeling of the emitted NO x has been performed by a box-
model approach, (Fisher & Smith, 1987; Russell, 1988). The emission smoke plume
is numerically separated into several discrete compartments with a trapezoid surface
(x- and y-axis) and a constant height of 1000 m (z-axis). Figure 7.5 illustrates this
approach. The trapezoid surface takes into account the increasing width of the plume
(as a function of the distance to the emission source). The limitation to the height
of 1000 m is due to the observed mean height of the boundary layer (Stull, 1988).
This limitation of the boundary layer is caused by a temperature inversion in the
lower troposphere. The inversion has the effect of an exchange barrier between the
atmospheric layers above and below, cf. Figure 7.5.


ENVIRONMENTAL FATE MODELING OF NOX-EMISSIONS
147
NO2
NO
NO
NO2
O3
PAN
HNO3
NO3
deposition
NO
NO2
O3
PAN
HNO3
NO3
deposition
Emission
0.95
0.05
time (t), distance (d)
t0, d0
t1, d1
t2, d2
Fig. 7.6
Conceptual model of NOx environmental fate: chemical reactions and deposition
processes of the NOx dispersion–reaction model.
Most frequently meteorological situations based on long term meteorological mean
values are used to set up the base for reaction dispersion modeling scenarios. Fur-
thermore different scenarios can be deﬁned by possible future production of the car
components. For detailed study, production is assumed to be constant and different
meteorological scenarios are deﬁned.
For environmental fate modeling a box-model was chosen that couples the transport
processes of NOx with the chemical reactions in the atmosphere. Stack emissions are
approximated assuming continuous operation of the power plant. Mean wind speed
and direction for the site are taken from Adler (1985). Dispersion was calculated with
discrete time steps of 1 hour.
Chemical reactions and deposition are calculated for each numerical compartment of
the plume. Figure 7.6 shows the chemical reactions and substances which are taken
into account. The chemical reactions and deposition processes are modeled based
on an ordinary differential equation system. The box-model simulates the matter
transport by successive numerical solution of the initial value problem. Initial values
for the background concentrations were taken from Kr ¨uger & Graßl (1994). Chemical
reactions are a function of ambient temperature and concentrations. Parameterization
of those functions is according to Simpson et al. (1990) and Kr ¨uger & Graßl (1994).
Deposition rates are assumed to be constant, cf. (Grennfelt et al., 1987; Kr ¨uger &
Graßl, 1994). A practical assumption for long-term prediction in the considered dry
region is, to aggregate wet and dry deposition to a total deposition rate. Properties of
the boundary layer are different for day and night and in winter and summer.


148
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
7.5.3
Process Model
This section gives a summary of all model equations, parameters and background
concentrations of the model. The ODE system is run for each box-compartment,
cmp. Figure 7.5.
General Notations
The following general notations hold.
Time t dependent
concentrations of a substance i in a box-compartment k = 1, 2, . . . is denoted by
Ci,k(t) holding the concentration in [mol/cm3]. The box-compartmentk has a volume
Vk in [cm3]. Reaction coefﬁcients ki may depend on temperature T in kelvin [K].
Depositions rates di are given in [1/d].
General Initial Condition
Convection and dispersion is modeled by a general
initial condition, which presents the concentrations of a substance i in the following
box-compartment.
Ci,k+1(0) = Ci(0) +
1
Vk+1
Ci,k(t)Vk
1 −Ci(0)
Ci,k(0)
(7.1)
This equation deﬁnes that the initial condition of compartment k + 1 is calculated
by the background concentration C i plus the non-background fraction of substance
moving from compartment k, given by C i,kVk into compartment k + 1, considering
the attenuation by the larger box volume (1/V k+1).
System of Reaction Equations
The translation of the conceptual model in
Figure 7.6 into mathematical equations results in the following system of ODEs. The
system is linear, as all reactions are assumed to be linear. This equation system is
Table 7.1
Background concentration values Ci(0) and deposition rates di for substance i
used for the environmental fate model.
Substance
NO
NO2
PAN
HNO3
NO3
O3
Ci(0)
0.987
1.93
0.196
0.654
1.88
189000
10−17[mol/cm3]
di
0.036
0.144
0.0072
0.0036
0.018 (daytime)
[1/h]
0.0018 (at night)


ENVIRONMENTAL FATE MODELING OF NOX-EMISSIONS
149
Table 7.2
Parameters of reaction rates for environmental fate model of NOx.
Day
Night
[OH·]
[CH3COO2·]
T
[OH·]
[CH3COO2·]
T
α
[mol/cm3]
[mol/cm3]
[K] [mol/cm3]
[mol/cm3]
[K]
solstice
Summer
2.67 · 10−18
4.78 · 10−18
308 2.62 · 10−20
4.35 · 10−19
298
82.5◦
Winter
2.32 · 10−18
6.67 · 10−18
291 2.32 · 10−20
6.06 · 10−19
282
35.5◦
solved for each box-compartment k. The index k is not printed.
dCNO
dt
=
kNO2 NO(t)CNO2 −kNO NO2(T)CNOCO3
dCNO2
dt
=
kNO NO2(T)CNOCO3 + kPAN NO2(T)CPAN
−kNO2 NO(t)kNO2NO3(t, T)CO3 + kNO2 HNO3[OH·]
+kNO2 PAN[CH3COO2·] + dNO2 CNO2
dCHNO3
dt
=
kNO2 HNO3[OH·]CNO2 + kNO3 HNO3CNO3
−kHNO3 NO3 + dHNO3 CHNO3
dCPAN
dt
=
kNO2 PANCNO2[CH3COO2·]
−kPAN NO2(T) + dPAN CPAN
dCNO3
dt
=
kNO2 NO3(t, T)CNO2CO3 + kHNO3 NO3CHNO3
−kNO3 HNO3 + dNO3 CNO3
dCO3
dt
=
−kNO NO2(T)CNO + kNO2 NO3(t, T)CNO2 + dO3(t) CO3
kNO2 NO(t)CNO2
(7.2)
Coefﬁcients
Parameter values for background concentration of the molecules
considered are listed in Table 7.1. Values for the reaction coefﬁcients of the system
(7.2) are obtained from (Kr ¨uger & Graßl, 1994; Simpson et al., 1990). Table 7.2
gives an overview of all parameters needed for a model run. Several reaction rates
depend on time or temperature:
kNO NO2(T)
=
7.56 10−9 exp
−1450 1
T
[cm3/mol/h]
kNO2NO(t)
=
18 exp −0.39
1
sin(α)
daytime
0
else
[1/h]
(desert area)
kNO2 PAN
=
1.15 · 10−8 [cm3/mol/h]


150
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
-200
-100
0
100
200
300
10-19
10-18
10-17
10-16
10-15
10-14
10-13
10-12
10-11
background
 NO
 NO2
 HNO3
 PAN
 NO3
 O3
concentration [mol/cm³]
distance from point of emission [km]
Fig. 7.7
Results from long term forecasts of concentrations. For a comparison of the climatic
situation of winter and summer, the corresponding graphs are juxtaoposted: winter: dark dots,
summer: small circles.
kNO2 HNO3
=
3.96 · 10−8 [cm3/mol/h]
kPAN NO2(T)
=
2.7 · 1018 exp
−12530 1
T
[1/h]
kNO2 NO3(T, t)
=
8.64 · 10−10 exp −2450 1
T
at night
0
else
[cm3/mol/h]
kHNO3 NO3
=
3.6 · 10−2 [1/h]
kNO3 HNO3
=
1.8 · 10−2 [1/h]
7.5.4
Results
The results of this simulation are long-term forecasts of concentrations. Long-term
forecast is here understood as annual mean values in the time range of several years.
Figure 7.7 shows the results of the environmental fate modeling given as concen-
trations in the plume. To demonstrate the difference in the reaction dynamics in
winter and summer, the corresponding graphs are juxtaposed. Windwards of the
stack (left portion in Figure 7.7) the daily variation of the background concentrations
can be observed. Steady state conditions are presumed during the day and during
the night. Leewards of the stack (right portion in Figure 7.7) the plume’s inﬂuence
on the atmospheric concentrations of the considered substances is shown. The NO x-
concentrations near the stack are signiﬁcantly higher than the presumed background


ENVIRONMENTAL IMPACT ASSESSMENT
151
values. Nevertheless, the NOx-concentrations caused by magnesium production do
not exceed the average NOx-concentrations of Jerusalem, a NOx-burdened site in Is-
rael (Luria et al., 1985). About 250 km leewards of the stack, the NO x-concentrations
are almost down to the background level again. Note that in summer the reactions are
faster than in winter because temperatures and levels of oxidants (e.g. ozone) are both
higher. For the subsequent environmental impact assessment step, the mean concen-
tration and deposition values which were derived from the different winter/summer
and day/night scenarios, are used.
7.6
ENVIRONMENTAL IMPACT ASSESSMENT
From the generic fuzzy expert system discussed in Section 7.3.3 three models are
speciﬁed, that assess the impact of immissions on the ecosystem characterized by
selected indicators. The selected indicators are plant damage, soil acidiﬁcation, and
eutrophication.
7.6.1
Soil Acidiﬁcation
The model for soil acidiﬁcation caused by NO x is presented in detail below. It is
based on an expert system developed by Kuylensstierna et al. (1995). The fuzzy
expert system is illustrated in Figure 7.8. In this model, average soil pH values
and ambient precipitation/evaporationindices determine the buffering capacity of the
soils.
High pH values of the soil obviously result in a high buffering capacity. A low precip-
itation/evaporation index also leads to a high buffering capacity, because, in semiarid
or arid regions, we observe mostly ascending movements of the soil-water, which
leads to increase in calcium carbonates in the upper soil horizons. This eventually
contributes to the development of Pedocals (Eyre, 1968). High deposition of protons
(acids) and low buffering capacities lead to high acidiﬁcation impact and vice versa.
Figure 7.9 shows the result of the case study employed on the fuzzy expert system for
soil acidiﬁcation. In this scenario, impact for wind directionNorth-West is calculated,
Buffering
Capacity
H+ deposition
pH value / soil
Precipitation/
Evaporation
Acidification
Fig. 7.8
Structure of the fuzzy expert system for soil acidiﬁcation.


152
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
0
20
40
60
80
100
-15
-10
-5
0
5
10
acid deposition
soil-pH
prec./evap.-index
acidification-impact
In- and Output values
Distance to point of emission [km]
Fig. 7.9
Possible soil-acidiﬁcation impact in the scenario “South-East of the stock” (see text
for explanations of input and output values).
which means that the plume spreads in direction South-East of the stack. Data for
the environmental conditions is taken from Adler (1985). Units in this ﬁgure are:
H+-deposition
log[mol H+/ha/a]
pH-value
-log[H+]
precipitation/evaporation index
dimensionless [mm/mm]
possible impact
[mol H+/ha/a]
Here the impact is always below 0 which means that theH+-deposition due to the NOx-
emissions caused by the power plant is below the buffering capacity of the soil. This
example illustrates the high sensitivity of the model to changes in the environmental
conditions. From km 30 to km 50 the plume traverses the Jordan mountainous region.
The soils of this region are slightly more acid than the soils in the Jordan valley and
East of the mountains. The values for the possible acidiﬁcation-impact change with
the soil-pH. The calculations for the other 7 directions lead also to the result that
the H+-deposition due to the NOx-emissions caused by the power plant is below the
buffering capacity of the soil.
7.6.2
Eutrophication
The fuzzy expert system for eutrophication is based on the critical loads concept,
see (Nilsson, 1986). In this model, the different soil characteristics cation exchange
capacity (CEC), moisture, temperature and C/N-ratio determine the main N-buffers:
biomass, denitriﬁcation and humus. In the model, the capacity of the biomass to


ENVIRONMENTAL IMPACT ASSESSMENT
153
Distance to point of emission [km]
N-deposition
C/N-ratio
CEC
soil moisture
temperature
eutrophication risk
0
20
40
60
80
100
40
50
-5
0
5
20
25
30
-5
0
20
30
60
In- and Outputvalues
S
SE
Fig. 7.10
Possible eutrophication impact in the scenario “South” (upper part of ﬁgure) and
“South-East” (lower part) of the stack.
buffer an additional N-input is determined by the application of the minimum princi-
ple of Liebig. The capacity is limited on the one hand by the CEC which represents
the availability of nutrients and on the other hand by the precipitation/evaporation
index which indicates the availability of soil water. A high precipitation/evaporation
index and a high CEC have a positive effect on the biomass buffer and vice versa.
The denitriﬁcation performance of the microorganisms is inﬂuenced by the temper-
ature and the precipitation/evaporation index. High values of both factors lead to a
good denitriﬁcation performance. The immobilization of nitrogen within the humus
fraction is increased by a high C/N-ratio and vice versa (Gundersen, 1992).
The three N-buffers determine the buffering capacity of the ecosystem with respect
to nitrogen input. Supplementary N-input by microbiological ﬁxation of N 2 is not
considered, according to (Posch, 1993). Loss of nitrogen by leaching is negligible
due to the aridity of the region studied, cf. (Noy-Meir & Harpaz, 1977).
The model for eutrophicationof soils forecasts low impacts which are negligible. The
predicted ecological effects in this model also show a high sensitivity to the variability
of soil characteristics across the mountainous region of Jordan.
This is illustrated in Figure 7.10. In the upper part of the ﬁgure, the results are shown
for the possible impact South of the stack. In the lower part, the assessment results
South-East of the stack are indicated. The values for the environmentalconditions are


154
APPLICATIONS: ENVIRONMENTAL IMPACT ASSESSMENT
taken from Adler (1985). In Figure 7.10 the N-deposition is given as total nitrogen
in [kg/ha/a], the C/N-ratio and the precipitation/evaporationindex are dimensionless,
the CEC is given as meq/100 g soil. The unit for the mean ambient temperature near
the soil is
. The possible eutrophicationimpact is givenas [kg-N/ha/a]. It represents
the difference between N-deposition and buffering capacity.
Eutrophication impacts for the other six directions are negligible. This is mostly due
to the fact that the wind regime is dominated by the wind directions North and North-
West and therefore the highest NOx-immission values are South and South-East of
the power plant.
7.6.3
Plant Damage
NO- and NO2-immissions can have adverse effects on the development and phys-
iology of plants (Sanders et al., 1995). However, as nitrogen compounds are also
nutrients for plant growth, low doses of NO x can have positive effects on plants (Cur-
tiss & Rabl, 1996). Within the fuzzy expert system for possible plant damage, three
different fuzzy sets have been deﬁned for the susceptibility of plants to NO x. These
sets represent the dose–response relationships of the three plant categories: “very
susceptible”, “susceptible” and “less susceptible” to NOx-immissions. The threshold
values for adverse effects due to NO x-immissions have been deﬁned in accordance
to Kolar (1990) as follows: very susceptible plants: 100 μg/m 3 (given as mean
value over six months), susceptible plants: 160 μg/m 3 and less susceptible plants:
250 μg/m3. The possible nutritional effect of low NO x-immissions has been taken
into account within the fuzzy expert system.
In the ﬁrst step of the environmental impact assessment for possible plant damage the
different crops in the vicinity of the power plant (up to 250 km distance) are assigned
to their respective fuzzy sets of susceptibility and in the second step their response to
the NOx-immissions is estimated.
The model for plant effects forecasts a slight increase of potential crop yield South
of the power plant. The effects in the other 7 directions for which calculations have
been made are negligible.
7.7
DISCUSSION
LCIA faces spatial and temporal difﬁculties as well as problems concerning thresh-
old values and dose–response relationships for many impact categories. In order to
achieve a more extensive and accurate environmental assessment of product systems,
the combined use of relative assessment techniques such as LCA and absolute as-
sessing techniques such as environmental fate modeling and environmental impact
assessment is a solution (de Haes & Owens, 1998). To further investigate the ad-
vantages and difﬁculties of such an integrated approach an environmental impact
assessment in conjunction with LCA was employed.


DISCUSSION
155
As a result of the methodological extensions and the application of regional impact
assessment for improving the accuracy of LCIA discussed above, the following con-
clusions can be made:
• An important methodologicalextension is the couplingof heterogeneousmath-
ematicalmodelingdevelopments: Petrinetsfortechnicalsystems,ODEorPDE
systems for reaction dispersion modeling and fuzzy expert systems for indicator
development and assessment.
• This methodological extension allows the integration of different kinds of in-
formation: technically measurable data in LCI, chemical reactions and spatial
spread which is often difﬁcult to measure, as well as ecological impact assess-
ment which is based on expert knowledge and is difﬁcult to quantify.
• The ﬁrst two steps of the integrated approach allow the derivation of indicator
systems which assess spatial heterogeneous ecological situations.
• The approach circumvents one of the major limitations of LCIA. It can now
address actual impacts at the site of emission, for instance the observed power
plant. The suggested solution integrates absolute environmental assessment
techniques into LCA.
The modular structure of the integrated approach and the well-deﬁned interfaces
between the parts allow the exchange and improvement of each module separately.
Forinstance,itmaybeisnecessarytoexpandthemodelofenvironmentalfateforother
substances with their reactions or for a more complex geometries in other landscapes.
Anapplicationofthedescribedapproachtootherimpactcategoriesneedsanextension
of the fuzzy expert system. The use of fuzzy expert systems for assessment allows the
possible input of linguistic data, which is an important feature for ecological and non-
measurable data. A regional decision system for environmental impact assessment
of anthropogenic emissions should therefore consist of the four elements LCA, fate
modeling, assessing expert systems and geographic information systems.
We are now able to cope with mathematically heterogeneous systems for environ-
mental models integrating interrelationships of anthroposphere and biosphere. This
lays the foundation for a systematic search for optimum environmental management
strategies assessed by environmental indicators and described by spatially explicit
dynamic systems.


Part III
The Big Picture:
Environmental
Management
Ja mach nur einen Plan
Sei nur ein großes Licht!
Und mach dann noch ’nen zweiten Plan
Gehn tun sie beide nicht.
—Berthold Brecht


8
Scenario Analysis and
Optimization
8.1
INTRODUCTION
A frequent application of ecological models is to support decisions on the anthro-
pogenicimpactontheecosystemandtoassesscertaindifferentmanagementstrategies
for ecosystems. The question as to how much impact nature can bear without harming
our environment is quite old. Ideas like “most sustainable yield” were introduced in
the late 1960s. Ecosystem management has now become an important discipline of
scientiﬁc research and is an important branch in the political decision-making process.
Simulation models are recognized as efﬁcient tools for the analysis of environmental
processes, education, and decision-making. The most fascinating ability of a model
is the possibility of performing non-intrusive experiments over a system based on the
theoretical and practical knowledge about processes and interactions.
Because ecological models are complex and highly interactive, this decision-making
process requires methodological support. The third part of this book deals with appli-
cations of ecological models in the decision-making process: either by the use of the
scenario analysis technique, or by the application of optimum control to ecosystem
models. Applications of ecological and environmental models are studied. Problems
of ecosystem management are solved by the use of numerical optimization method-
ology. This can be interpreted as the follow-up of the most sustainable yield concept
by the use of scientiﬁc computing.
In this context a model consists of a simulator which represents the environmental
processes and connects control variables (also known as forcing functions or inputs)
to output variables, cf. Chapter 1. The former ones, the control parameters, may
159


160
SCENARIO ANALYSIS AND OPTIMIZATION
Steps of Modelling for Optimum Control Applications
Simulation Results
Control
Parameters
Functions of (numerical) optimization/optimum control procedure
Control parameter
Modification
( )t
ur
Producers
Crops & Weed
Consumers
Anorganic
Nutrients
Pest
Control
Harvest
Crop
 Rotation
Bacteria
Mineral
Fertilizer
α
Consumers
Pesticide
Pesticide
Dead Organic
Matter
N(t)
W(t)
P(t)
)
(t
P
r
CL(t)
CS(t)
A(t)
F(t)
Upper soil layer (root zone)
Simulation Model
(
)
( ) ( )
(
)
c
t
u
t
x
M
t
x
i
t
i
r
r
r
r
,
,
1
∆
+
=
J 
maximized
?
Time series
Maps
no
yes
Performance 
Criterion
[
]
(
)
z
dtd
u
x
f
u
x
J
r
r
r
r
r
∫∫
=
,
,
λ
Fig. 8.1
Concept of applications of environmental models in numerical optimum control
procedures. Basic elements of the modeling part are simulation models — displayed by the
conceptual model of an agroecosystem — and the performance criterion. Important part of
the optimization procedure is an intelligent modiﬁcation of the control vector driven by the
estimation of the performance criterion. Note, compared to the scenario analysis methodology,
which one could compare with an open control system, this is a control loop.
be used to deﬁne management strategies in terms of the model variables. The latter
ones, output variables, are used to describe the system behavior and to assess the
management strategies being studied. One or more of these output variables are used
to assess the simulation, the results of the modeling experiment. Because of this,
these variables are often called indicators. Figure 8.1 illustrates this concept.
To analyze the system and deﬁne the most appropriate management practices, usually
a number of scenarios are formulated and then fed into the model. The output results
are then comparedto choose the one that ﬁts the requirements, the management goals,
best of all. The formulation of a management scenario, assessment and comparison
of results requires considerable effort. Scenario deﬁnition requires knowledge on the
modeled system, which probably may not be available due to the complexity of the
investigated system (Jakeman & Letcher, 2003).
Instead of running numerous scenarios through the model and then comparing the
results, see for instance (Costanza et al., 2001; Kurz et al., 2000; Rao et al., 2000),
we may formulate a certain goal that we want the ecosystem to reach, and then let
the computer sort through the numerous parameter and pattern combinations to reach
that goal. In this case the variations of parameters and functions in the model input
(control)areperformedautomatically, aswellastheprocessingoftheoutput. Thecore
ofthisprocessisthealgorithmofnumericaloptimization, whichmakesthedecisionon
howtodeﬁnethenextscenariotoanalyze,basedontheavailableinformationaboutthe


OPTIMIZATION AND ENVIRONMENTAL MODELING
161
ofthisprocessisthealgorithmofnumericaloptimization, whichmakesthedecisionon
howtodeﬁnethenextscenariotoanalyze,basedontheavailableinformationaboutthe
results of previous model runs. This optimization procedure connects the scenarios,
the simulation process and the performance criterion. Algorithms of optimization
are capable of performing a systematic search in the space of control variables to ﬁnd
an input vector which controls the systems in the desired way, speciﬁed by the goal
function.
This is the basic idea of optimization — or if temporal patterns are considered —
optimum control, that are illustrated by Figure 8.1. The basic difference between
optimization and scenario analysis is the closed feedback loop in the ﬁgure. This
feedbackloopis closed by the conditionif the performancecriterion“J is maximized”
and the modiﬁcation of control parameters.
In the following this concept will be analyzed with respect to environmental pro-
cesses. The reader may guess that integrated models, mathematical heterogeneity,
use of several temporal and spatial scales as well as spatially explicit models lead to
methodological problems. To approach the problem the steps of model development,
modeling a performance criterion, and implementation of optimization procedures
are separated. In the following chapters we will focus on the set up of appropriate
algorithms for optimization and optimum control of environmental systems as well
as the development of general performance criteria for environmental systems.
8.2
OPTIMIZATION AND ENVIRONMENTAL MODELING
8.2.1
Analytical Treatment and Non-spatial Applications
Analytical solutions of optimum control problems were ﬁrst presented by van Dyne
et al. (1970). The importance of nonlinear models was noted, but there was no
methodology capable of solving nonlinear systems in terms of control theory. Clark
(1976)andClarketal.(1979)laidthefoundationforinvestigatingecologicaloptimum
control problems. Forest management and ﬁsheries were the ﬁrst applications, which
initiated a large number of publications on agricultural models (Cohen,1987b; Cohen,
1987a; Falkovitz & Feinerman,1994; Velten & Richter,1993; Velten & Richter,1995)
and ecological economics (Doherty Jr. et al., 1999). DeGee and Grasmann (1998)
studied sustainable use of renewable resources using analytical solutions of optimum
control problems based on Lotka–Volterra-type systems. The underlying simulation
modelsinthethesepapersweresetupusingsystemsofordinarydifferentialequations.
In terms of ecosystem management, more complex model systems, which cannot
be treated analytically will now be considered. Recent developments in numerical
procedures of optimum control focus on high performance real-time optimization
of large systems of ordinary differential equation systems, which can be written in
the form d⃗x/dt = ⃗f (⃗x, t); see, for instance, Bulirsch et al. (1993). Environmental
models do not fulﬁll the prerequisites. It is difﬁcult to transform ecological models


162
SCENARIO ANALYSIS AND OPTIMIZATION
into this notation. This hints at reasons for this lack of optimization applications in
environmental modeling, although it seems to be a very promising branch of system
theory and ecosystem management.
8.2.2
Spatially Explicit Applications
Table 8.1 summarizes recent publications on ecosystem management based on spa-
tially explicit or regionalized simulation models. We look at the model structure, the
control variables, the goal function, the processes, and the spatial database used. The
last column lists the location of the study area, if any.
The scope of ecosystem management problems ranges from forest management and
timber harvest (Loehle, 2000; Tarp & Helles, 1997) to agricultural problems (Nevo &
Garcia, 1996; Makowski et al., 2000) to general issues of land use change (Martinez-
Falero et al., 1998), and to habitat suitability (Bevers et al., 1997). The models
used differ in terms of mathematical structure. Modeling methodology ranges from
aggregated dynamic models based on difference equations of exponential growth
(Bevers et al., 1997; Loehle, 2000) to complex models based on systems of nonlinear
differential equations (Randhir et al., 2000). In terms of optimization methodology
one can ﬁnd a broad spectrum of approaches.
Hof & Bevers (1998) published an overview of application of optimization to land-
scape management problems. Together with Clark they are aware of the problem of
complex and spatially explicit systems. They use linear programming and nonlin-
ear program methodology to solve problems of pest management, re-establishment
of population forest treatment, and runoff by storms etc., mostly within artiﬁcial
landscapes. They are aware of the difﬁculties in deﬁning and solving optimizations
problem with highly complex nonlinear models in real landscapes.
8.3
ASSESSING THE ENVIRONMENT VARIABLES
8.3.1
Indicators . . .
In order to assess the results of a scenario analysis in terms of environmental, eco-
nomic, toxic, or social aspects, we need to consider more than one output variable.
To compare different simulation scenarios we then need to integrate output variables
into a scalar value. The other option would be to analyze a multi-dimensional deci-
sion problem. This function aggregates several output variables and is called a goal
function or performance criterion. In the mathematical formalization this function
must be maximized or minimized to reach the desired state.
The deﬁnition an appropriate performance criterion can be separated into two main
questions, which will be discussed later on in Section 8.4.1. The ﬁrst concerns the
technical aspects and the mathematical properties. Second, the more general aspect


ASSESSING THE ENVIRONMENT VARIABLES
163
Table 8.1
Application of spatial optimization in landscape ecology.
Reference
Model
structure,
process
Control variables
Performance
criterion
Optimization
algorithms
Spatial DB,
Scale, GIS
Case Studies,
Applications
Bevers
et
al.
(1997)
Time discrete mi-
gration & popula-
tion dynamics
– Location of re-
introduction
– Rodiacid treat-
ment
Habitat
sustain-
ability function
Nonlinear
pro-
gramming,
stochastic
varia-
tion
Raster
Badlands National
Park, Buffalo Gap
National
Park,
South Dakota, US
Hof et al. (1999)
Population
dynamics
Timing
of
habi-
tat protection for
prairie orchid
—
—
Raster,
ArcINFO
Sheyenne National
Grassland,
South
East North Dakota,
US
Loehle (2000)
Exp.
growth
of
forests
Timber harvest
Timber
harvest,
water quality
0–1 integer
pro-
gramming
Raster
—
Makowski et al.
(2000)
—
Spatial
distribu-
tion of agricultural
land use
—
Hierarchical struc-
tured linear pro-
gramming
—
European Union
Mart´inez
et
al.
(Martinez-Falero
et al., 1998)
Linear
model,
eqn. system
Land use modiﬁ-
cation
Ecological
sustainability, eco-
nomic costs, social
constraints
Baye’s approach to
land use changes
Raster
Torrelague
town-
ship,
Spain,
2787 ha
Nevo
&
Garcia
(1996)
—
Spatial
distribu-
tion of agricultural
land use
Habitat
sustain-
ability to wildlife
species
Two stage nonlin-
ear optimization
—
Lonetree Wildlife
Management
Area,
North
Dakota, US
Tarp
&
Helles
(1997)
—
Timber harvest
Sustainable forest
management
Simulated anneal-
ing,
linear
pro-
gramming
Vector
Boendernes Hegn,
Denmark
Randhir
et
al.
(2000)
EPIC
(Williams
et al., 1983)
Landuse
Water quality
erosion
Spatial
dynamic
programming
Raster,
GRASS
Experimental
watershed


164
SCENARIO ANALYSIS AND OPTIMIZATION
of a performance criterion is how to measure the state of an ecosystem. This refers
to an ongoing discussion about indicators of an ecosystem, in which many scientists
from different disciplines have presented valuable input.
Recent deﬁnitions of indicators and the use of terminologyin this area are particularly
confusing (Gallop´ın, 1997). Many authors and institutions give different deﬁnitions
and explanations what indicators are, what they should perform, and what properties
they should have. Three examples of deﬁnitions or explications are given, which are
presented from different origins.
Example 8.1 ((United States Environmental Protection Agency, 1995)) An envi-
ronmental indicator is a parameter (i.e. a measurement or observed property), or
some value derived from parameters (e.g. via an index or model), which provides
managerially signiﬁcant information about patterns or trends (changes) in the state
of the environment, in human activities that affect or are affected by the environment,
or about relationships among such variables. As deﬁned here, indicators include ge-
ographical (spatial referenced) information, and information used in environmental
management at any scale, i.e. not just for high-level policy makers.
This deﬁnition covers most of the issues discussed in the previous chapters. US EPA
recognizes the importance of models to be used within environmental assessment, as
models allow the derivation of unmeasurable variables. Second, this deﬁnition also
notes the importance of spatially referenced indicators, as shown in Chapter 7. Azar
et al. identify two problems in the deﬁnition of indicators. With special respect to
indicators assessing sustainability, they write
Example 8.2 ((Azar et al., 1996)) There are in many cases longtime delays between
a speciﬁc activity and the corresponding environmental damage. This means that
indicators based on the environmental state may give a warning too late, and in many
cases only indicate whether past social activities were sustainable or not.
The complexity of the ecosystem makes it impossible to predict all possible effects of
a certain social activity. Some damages are well-known, but others have not yet been
identiﬁed. Models of sustainability indicators suggested in literature are formulated
with respect to known effects in the environment.
These two topics clearly relate to the development of dynamic models describing
environmental processes of concern. First, because dynamic models can cope with
long time delays. Second, because models can handle and structure complex systems.
Refering to the second topic of Example 8.2, uncertainty is an inherent property of
indicators comparable to models, as not all processes may be known or may not be
considered in the deﬁnition an indicator or the underlying model, see Section 1.3.3.
However, from this one can conclude that indicator deﬁnition requires the use of
dynamic environmentalmodels. Winograd extends these considerations and suggests


ASSESSING THE ENVIRONMENT VARIABLES
165
Example 8.3 ((Winograd, 1997)) The function of indicators would be to:
• determine the condition of, or change in, the environment in relation to society
and the development process.
• diagnose the actual causes and effects of existing problems that have been
detected, in order to elaborate responses and actions.
• predict future impacts of human responses and actions.
Winogradextends the deﬁnition fromthe US EPA by the recommendationthat indica-
tors should offer cause-effect relationships, the necessity to predict the future, as well
as the basis to derive management strategies. With the background of the methodol-
ogy of environmental modeling (see for instance Figure 3.11) this seems to ask too
much of an indicator concept. Predicting future impacts is related to environmental
modeling, and elaboration of responses and actions will be a result of optimization
or optimum control. Indicators have to focus on the problem of assessment and
comparison. This is what Hunsaker (1993) is focusing on:
Example 8.4 ((Hunsaker et al., 1993)) Candidate indicators can be evaluated with
regard to the following criteria:
• The indicator must be operationally deﬁned and readily measured;
• The indicator must be sensitive to changes in pollutant deposition;
• The response of the indicator must be stable over the spatial and temporal
ranges of the assessment end point and of pollutant exposure;
• The indicator must be contained in the output of predictive models if it is to be
used as a predictor of future response;
• The indicator must be contained in databases that allow the resource to be
mapped or quantitatively characterized;
• Changes in indicator status should result in a willingness to change the regu-
lations of sources.
All these deﬁnitions aim at an identiﬁcation of the environmental state and its changes.
This is achieved either by the application of a model or bymeasuringan environmental
variable. This variable (either from model or measured) has to be stable over the
considered spatial and temporal range on the one hand, and sensitive to changes on
the other hand. To fulﬁll these recommendations it might be helpful to have a look
on what environmental models offer.


166
SCENARIO ANALYSIS AND OPTIMIZATION
8.3.2
. . . and Applications for Optimization
What can be derived from this discussion for the application of environmentalmodels
aiming at an estimation of optimum management strategies?
First, the indicator concepts help to deﬁne performance criteria J, cmp. Figure 8.1.
Several recommendations in Examples 8.1 to 8.4 hold true for the modeling of per-
formance criterion. The performance criterion
• is deﬁned as a function of the model output, e.g. a function of state variables
or derived auxiliary variables;
• is therefore a quantiﬁcation of the system state;
• depends on geographically referenced information, or aggregated/integrated
information for a speciﬁc region;
• should be sensitive to changes of the system state.
Additionally, environmental simulation models enlarge the spectrum of possible def-
initions of performance criteria. Using ecological models one is even able to use
unmeasurable variables for assessing management scenarios.
A deﬁnition of indicators and performance criteria must solve the problem of com-
paring and aggregating different variables with units that are difﬁcult to compare.
For instance, how can nitrogen loss and the probability of nitrogen in drinking water
reservoirs be compared with prices for agricultural products? Or, as a more landscape
ecological example, how can habitat maintenance for certain species be compared
with real estate prices for dwelling units?
Ecological systems are open systems. In a performance criterion variables can be used
whicharerepresentedinthesimulationmodel. Forinstance,anassessmentofpossible
ground water contamination with nitrate can only be assessed by the possible outﬂow
of nitrogen out of the plant-accessible root zone. In economic terms this means, that
external costs have to be internalized. Note that the deﬁnition of the system boundary
determines whether variables and costs are external or internal. For example, the
integration of the ecological impact at the production site at the Jordan river in the
environmental impact assessment study in Chapter 7 integrated these “costs” to the
impact study of the car production in Wolfsburg. However, environmental models
cannot cover all possible effects. Because of this a methodological treatment of
externalities is required.
This problem does not only occur when comparing state variables from biosphere
and anthroposphere. Even in assessing variables only from the biosphere, it is difﬁ-
cult to compare different variables on an equal level of information. There are two
approaches to solve this problem. Concerning anthroposphere-biosphereinteraction,
some authors advocate the use of monetary units for comparison. Giving prices for
ecosystem functions has been very successful (Costanza, 2000; Costanza et al., 1997;


GENERAL OPTIMIZATION TASK
167
Scheffer et al., 2000). Authors believe that this approach increases awareness of the
services provided by ecosystems to maintain life on earth.
Second, by comparing different ecosystem functions, one can make use of evolu-
tionary concepts underlying most of the patterns identiﬁed in ecology. Ecosystems
tend to use the energy available (from solar radiation) very efﬁciently. The means
on the other hand, that ecosystems tend to minimize unstructured energy, so-called
entropy. Several authors suggets using concepts like exergy,emergyetc. for assessing
ecosystem state (Jørgensen et al., 1998; M ¨uller, 1998).
The basic ideas obtained from this discussion are that two possible strategies can be
followed for deﬁning performance criteria. Either try to compare anthropogenic and
biosphere processes using monetary units, or use energy or entropy respectively to
compare processes for the deﬁnition of a goal function.
8.4
GENERAL OPTIMIZATION TASK
8.4.1
Performance Criteria
Considering the models presented in this publication, the following variables or pro-
cesses can set up performance criteria for optimization
1. leachate of hazardous substances into the environment (which is to be mini-
mized in terms of optimization):
• nitrate below rooting depth (agricultural production), cf. Sections 2.2.3,
2.4.1
• phosporous at the watershed mouth, from sewage input or caused by
erosion, see Section 3.3.3
• emitted substances like NOx or sulfur at a certain distance from an indus-
trial production site, cf. Chapter 7
• other xenobiotic substances, for instance pesticides, cf. Section 2.4.2
2. maintaining ecosystem functions
• maintaininghabitatsuitabilityforspecies, preservingbiodiversity, cf.Sec-
tions 3.2.2 and 3.3.2
• supporting CO2 retention capability, cf. Chapter 3
• maximizing nett primary production, cf. Chapter 2
3. maintain and support production by
• maximization of agricultural yield, cf. Section 2.2.1


168
SCENARIO ANALYSIS AND OPTIMIZATION
• minimization of input of energy, of work power, or minimizing of pro-
duction steps, for instance weed control or fertilization (Section 2.2.4,
2.4.1), or in terms of industrial production, see Chapter 7
• assessing yield stability considering a long term period
• minimization of weeds, cf. Section 2.2.4
4. support human life (recreation, housing, etc.)
Performance criteria aggregate different indicators. A performance criterion com-
prises a broad spectrum of different state variables for assessment with different
origins like economy, ecology, and social aspects. In the above list items 1 and 2
can be associated to ecological aspects; item 3 lists economic indicators; and item 4
belongs to social assessment. In most cases these are contradictory goals.
From a methodological point of view, two different approaches are available to cope
with this problem. Optimization problems may be formulated as scalar optimization
problems. The second approach is to deﬁne a multi-criteria optimization problem.
Both approaches will be considered in the following, starting with scalar optimization
problems. A mathematical deﬁnition for a scalar performance criterion is given by
the following deﬁnition:
Deﬁnition 8.1 (Performance Criterion) Consider a general environmental model
given by Equation (4.1). ⃗x denotes the vector of state variables. ⃗u denotes the vector
of control variables. Both depend on time t and location⃗z. A performance criterion
maps a trajectory from state and policy space to a real number J[⃗x,⃗u] ∈.
This mapping requires an aggregation in time as well as in space.
The general
transformation is achieved by the following function
J[⃗x,⃗u] =
tend
0 R
fλ
⃗x(t,⃗z)
⃗u(t,⃗z)
dt d⃗z
(8.1)
where R denotes the study area and tend the upper limit of simulation interval.
Assuming that fλ simply performs a linear combination of its arguments with a vector
of weighting coefﬁcients Equation (8.1) can be rewritten as follows
J[⃗x,⃗u] =
tend
0 R
⃗λT
⃗x(t,⃗z)
⃗u(t,⃗z)
dt d⃗z =
tend
0 R
n
i=1
λixi(t,⃗z)+
m
i=1
λi+nui(t,⃗z)dt d⃗z (8.2)
Additionally certain constraints or boundary condition may be deﬁned. A general
formulation is
f0(⃗x(t,⃗z),⃗u(t,⃗z)) ≤0 for all ⃗z ∈R, t ∈[0, T]
(8.3)
An application of Equation (8.2) can be found in the well-known example of en-
ergy minimization while landing a moon vessel. This is why this equation often is
considered as energy norm.


GENERAL OPTIMIZATION TASK
169
The deﬁnition of the weighting scheme ⃗λ turns out to be the crucial problem in mod-
eling performance criteria for environmental problems and the application of Equa-
tion (8.2) to an optimization problem. Nutrient contents, habitat suitability for certain
species, or net primary production denote ecological variables. Model variables like
harvest biomass and fertilizer input from/to a ﬁeld denote purely economic variables.
The crucial question is: How to integrate these indicators to a scalar value by a single
constant vector ⃗λ? One might note that using the more general Equation (8.1) might
offer more freedom for aggregation of these different variables. A nonlinear function
of assessment of indication does not simplify nor solve the problem. The following
chapter will show how to work with this technique of optimization based on scalar
performance criteria based on Equation (8.2).
A different aspect, which is to be noted here, is that more freedom in assessing the
processes is achieved, if multi-criteria approaches are used for assessing the process.
However, we will see that with certain techniques of optimization and by solving
the (so far undeﬁned optimization problems), a multi-criteria analysis using a scalar
performance criteria can be analyzed.
8.4.2
General Optimization Task
Based on the deﬁnitions of a general environmental model, cf. Equation (4.1), and
the performance criterion in Deﬁnition 8.1 we can now formulate the mathematical
problem of identifying optimum management strategies in environmental problems
in a general notation.
Task 8.1 (General Optimum Control Problem) Let MΔt deﬁne a simulation model
according to the General Model Equation (4.1): Calculate ⃗u ∗, so that
⃗x(t)
=
MΔt ⃗x0,⃗u∗,⃗c
J[⃗x,⃗u∗]
≥
J[⃗x,⃗u]
for all t ∈[0, T],⃗u ∈U
(8.4)
where U denotes the set of admissible sets of control variables.
Note ⃗u ∈U as well as ⃗x depend on time and space. This task in general deﬁnes a
spatio–temporal optimization problem:
Task 8.2 (Regionalized Optimum Control) Calculate ⃗u∗(t,⃗z) so that
⃗x(t,⃗z)
=
MΔt ⃗x0(⃗z),⃗u∗(t,⃗z),⃗c(⃗z)
J[⃗x(·,⃗z),⃗u(·,⃗z)∗]
≥
J[⃗x(·,⃗z),⃗u(·,⃗z)]
for all t ∈[0, T],⃗u ∈U
(8.5)
for all ⃗z ∈R.


170
SCENARIO ANALYSIS AND OPTIMIZATION
8.4.3
Methodology
The general form used in this deﬁnition together with the general notation of an envi-
ronmental model, see Deﬁnition 4.1, faces us with a number of problems concerning
the numerical solution of the problem notes in Task 8.1.
Numerical solutions for optimization problems usually make use of the structure of
the system. For instance, linear problems based on explicit solutions can be solved
analytically using linear programming methodology (Tarp & Helles, 1997). Nonlin-
ear optimization problems make use of the linearization of the problem of an iterative
procedure for identiﬁcation of the maximum or minimum of J as a function of the
control variable (Press et al., 1988; Stoer & Bulirsch, 1983).
Concerning optimum control, several solutions have been presented that required the
dynamic system to be set up by ordinary differential equation systems only (Bulirsch
et al., 1993; Bulirsch & Kraft, 1994). Optimization or optimum control based on
partial differential equation makes use of a discretization in space transforming the
problemintoasystemofordinarydifferentialequations(Altmann-Diesesetal., 2002),
see Section 1.5.6.
In general one can distinguish two different approaches for solving the optimization
problems.
Global optimization procedures are able to identify the global optimum.
This
means, that these procedures search through the entire space of control and
state variables, ﬁnally identifying this (spatio–temporal) control vector, that
maximizes or minimizes the performance criterion under the given boundary
conditions.
The enormous computational effort required for these procedures means that
they are only applicable to low dimensional systems.
Local Optimization procedures are based on an iterative procedure that improves
an initial solution stepwise in the direction of the increasing (or decreasing)
performance criterion — depending on maximization or minimization.
These procedures are applicable to a broad spectrum of models. Depending on
the implementation of the procedure, more or less prerequisites are required
such as the derivative of the performance criterion with respect to the control
variables.
The major drawback of this iteration is that these procedures stop if no change
of the performance criterion value can be identiﬁed. This does not necessarily
mean that the estimated control vector holds the set of control variables that
globally maximize or minimize the performance criterion.
Application of general environmental models in optimum control and optimization
applications requires the development of a methodology that can handle these mathe-
matically heterogeneous systems. Dynamic programming (Bellman, 1957; Angel &


DISCUSSION
171
Complexity of spatial interactions
and/or landscape patterns
Model Complexity
applications of
scenario technique
applications of
optimization
Model
Aggregation
Spatial Aggregation
Fig. 8.2
Graphical representation of the present state of the art in concepts of regional
optimization solutions.
Bellman, 1972) is a suitable methodology, which identiﬁes the global optimum of the
problem and has less restrictions to the underlying model. Chapter 9 will summarize
this concept together with several extensions and modiﬁcations required for envi-
ronmental models. The property of spatial explicitness of an environmental model
makes these problems even worse. The spatial explicitness of the model increases
the space of control variables and state variables exponentially. Because of this, local
optimization methodologies are required to solve optimization problems using envi-
ronmental models. For the successful application of these algorithms strategies have
to be found that give a good starting point for the iterative search in control space.
These questions will be discussed in the second part of the next chapter.
8.5
DISCUSSION
In environmental modeling the idea of applying simulation models to numerical opti-
mization algorithms in terms of optimum control theory is quite new, cmp. Table 8.1.
For this application it is necessary to use well-validated simulation models within the
framework of a robust and ﬂexible optimum control procedure. Both items are difﬁ-
cult to achieve in environmental modeling. The ﬁrst — validating an environmental
simulation model — is a complex task, cf. Chapter 1. The second, because modeling
environmental processes leads leads to mathematically heterogeneous mathematical
models as shown in the earlier part of this book.
The complexity of an optimization task depends on two factors: the complexity of
the ecosystem model (number of state variables, degree of nonlinearity etc.) and the


172
SCENARIO ANALYSIS AND OPTIMIZATION
spatial complexity (size of study area, grid cell size, number of spatially interacting
processes). The more complex the simulation model is and the more spatial relation-
ships are considered, the lower are the chances of success in the optimization. For
such complex models, scenario analysis is usually the only feasible method. Figure
8.2 illustrates this relationship.
Scenario analysis compares the outcome of a given number of scenarios, which are
identiﬁed with possible management strategies. Optimization procedures perform a
systematic search over the whole control space automatically, whereas optimization
tasks requiremuch less effortin preprocessingand formulatingthe numerousscenario
options, their computational complexity is incredibly high. The models described in
Table 8.1 are considered in an optimization context. Therefore they all required
certain simpliﬁcation or aggregation to allow optimization, cf. Figure 8.2. This was
achieved either by aggregation of the model or aggregation of the study area, or both.
Chapter 9 will introduce a set of methodological tools that extends the domain of
environmental model applicable in optimization and optimum control theory — they
move the boundary line in Figure 8.2 to the upper right. The following chapters
then present several case studies and applications of spatially explicit environmental
models and the estimation of management strategies.


9
Prerequisites:
Temporal Hierarchies and
Spatial Scales
9.1
INTRODUCTION
Environmental models are complex for different reasons. First of all the number of
state and control variables is an indicator for complexity of models. Second, the
number of mathematical “dialects” used to set up the model is a measure of the
mathematical heterogeneity. The more heterogeneous a model, the smaller is the
spectrum of possible numerical methods of optimization tasks. This is because the
number of fulﬁlled prerequisites of numerical methods is decreasing. Third, spatial
explicitness of regionalized models allows the space of state and control variables to
increase exponentially. This again lets computational effort increase in an additional
dimension.
One concept that can offer solutions to this problem is the introduction of different
temporal hierarchies as well as different spatial scales. This concept was introduced
in Chapter1 with Figure 1.3 (p. 8). In that chapterscales were used to characterizeand
classify models. In this chapter this concept will be used to develop solutions for the
application of complex environmentalmodels to optimization theory. A methodolog-
ical framework is proposed for the application of environmental models in optimum
control theory. Dynamic programmingalgorithms are used based on general dynamic
systems. Numerical effort is decreased by making use of properties of environmental
models. In the second part of this chapter spatially explicit models will be considered
in the process of optimization.
173


174
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
9.2
HIERARCHICAL DYNAMIC PROGRAMMING
9.2.1
Introduction
Formulation of optimum control problems and the numerical methods require a gen-
eral notation for simulation models. This formal representationneeds to abstract from
mathematical properties of the underlying simulation model, e.g. ODE, DAE, PDE.
Consider a dynamic system with the state variables ⃗x(t), the control variables ⃗u(t) and
the right-hand side ⃗ϕ(⃗x,⃗u) on a time interval ti ∈[0, T] = I. ⃗ϕ(⃗x,⃗u) is called the ﬂux
of the dynamic system (Arrowsmith & Place, 1994, ch. 1). On this system a q-stage
process can be deﬁned:
Deﬁnition 9.1 (q-stage-process) q stages are deﬁnedby 0 ≤t 0 < t1 · · · < tq−1 < tq =
T, e.g. q events of possible control. The sequence of control ⃗u(ti) i=0,...,q−1 modiﬁes
the dynamic system so, that
⃗x(ti+1) = ⃗ϕΔt(⃗x(ti),⃗u(ti))
(9.1)
with Δt = ti+1 −ti for i = 0, . . ., q −1.
Equation (9.1) can be applied directly to a dynamic system, which is deﬁned by
a time-discrete algebraic equation. In the case of a differential equation system,
the estimation of the succeeding state ⃗x(ti+1) involves the numerical solution of the
differential equation system (Hairer et al., 1980; Hairer & Wanner, 1980).
Application of optimum control theory to simulation models with the described prop-
erties requires methods that do not restrict the class of applicable models by strong
assumptions; for instance, derivatives of the model functions may not exist. Bellman
(1957) offered dynamic programming as a ﬂexible optimization approach applicable
to heterogeneous mathematical systems. Equation (9.1) sets up the bases for an ap-
plication of the algorithm of dynamic programming. Bellman (1962, p. 15) denotes
⃗u∗(t) an optimal policy if it maximizes a given performance criterion J[⃗x,⃗u]. J is a
functional deﬁned on the space of state and control functions. For an application of
dynamic programmingit is necessary to write J in a recurrence equation in the stages
i = 0, 1, . . ., q.
Deﬁnition 9.2 (Performance Criterion (recurrence equation))
J[⃗x,⃗u] = J ⃗x(t1), . . ., ⃗x(tq),⃗u(t0), . . .,⃗u(tq−1)
denotes the assessment of the entire process. J has Markoff property, if J can be
separated by continuous functions Ki in the stages i = 1, 2, . . ., q and Ji(⃗x(ti),⃗u(ti−1))


HIERARCHICAL DYNAMIC PROGRAMMING
175
can be set up by
J
=
Jq J1(⃗x(t1),⃗u(t0)), . . ., Jq(⃗x(tq),⃗u(tq−1))
Jq−i(Ji+1, . . . , Jq)
=
Kq−i
Ji+1, Jq−i−1(Ji+1, . . . , Jq)
for i = 0, . . ., q −2
J1(Jq)
=
Jq
for i = q −1.
(9.2)
Deﬁnition 9.3 With the notation from Deﬁnitions 9.1 and 9.2 state functions ξ i are
deﬁned by
ξ1(⃗x(tq−1))
=
max
⃗u(tq−1)
J1(Jq)
...
ξq−1(⃗x(t1))
=
max
⃗u(t1),...,⃗u(tq−1)
Jq−1(J2, . . ., Jq)
ξq(⃗x(t0))
=
max
⃗u(t0),⃗u(t1),...,⃗u(tq−1)
Jq(J1, . . ., Jq)
(9.3)
Principle of Optimality as proposed by Bellman & Dreyfus (1962, p. 15): An optimal
policy has the property that whatever the initial stage and initial conditions are,
the remaining decisions must constitute an optimum policy with regard to the state
resulting from the ﬁrst decision.
In the notation ⃗u(ti) with i = j, . . . , q −1 denote the remaining decisions. From this
principle a computational scheme can be derived:
Algorithm 9.1 (Dynamic Programming (DP)) Equation (9.2) is used to estimate
ξq−i(⃗x(ti)) for all possible ⃗x(ti) for i = q−1, . . ., 0. At each stage i the optimum control
vector ⃗u∗(ti) is stored as a function of ⃗x(ti). For the evaluation of Ji+1 depending on
⃗x(ti+1) Equation (9.1) is solved for a general dynamic system. The complete sequence
derived from that ⃗u∗(ti) i=0,...,q−1 is the solution of the optimum control problem for a
given initial condition ⃗x0. The mathematicalnotation of this procedure is summarized
by:
ξ1(⃗x(tq−1))
=
max
⃗u(tq−1) Jq(⃗ϕΔt(⃗x(tq−1),⃗u(tq−1)))
for i = q −1
ξq−i(⃗x(ti))
=
max
⃗u(ti) Kq−i Ji+1(⃗ϕΔt(⃗x(ti),⃗u(ti))),
ξq−i−1(⃗ϕΔt(⃗x(ti),⃗u(ti)))
for i = 0, . . ., q −2
(9.4)
The procedure estimates the global optimumsolution ofthe optimumcontrol problem.
Additionally, this procedure may be used to estimate the the kth-best solution (k =
1, 2, . . .). See the contradictory proofs in Bellman & Kalaba (1960).
Note, the sequence of optimum control vectors ⃗u(ti) i=0,...,q−1 is estimated as a func-
tion of the initial condition ⃗x(t0). This is an outcome of the principle of optimality.


176
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
In terms of numerical aspects this allows the derivation of an optimum control se-
quence from any initial condition ⃗x(t0) using the calculated ξ1, . . . , ξq without any
computational effort (Bellman & Dreyfus, 1962).
The computational effort of estimating ξ1, . . ., ξq increases polynomially with the
increasingdimensions of state or policy space. Let n, m denote the dimensions of state
and policy space and ni (i = 1, . . ., n), mi (i = 1, . . ., m) the number of possible values
of each state/control variable. The estimation of ξ1, . . ., ξn according to Algorithm
9.1 requires
S DP = q
n
i=1
ni
m
i=1
mi
(9.5)
evaluations of Equation (9.1). Bellman (1957) calls this property “dilemma of di-
mensionality”.
9.2.2
Hierarchies and Temporal Scales
The problem of hierarchy can be faced if one takes into account that environmental
systems are structured with respect to characteristic times. Ecological systems show
characteristic times from hours to years or decades, see Chapters 1 and 2, Table 1.2,
Figure 1.3. This property can be formalized for dynamic systems: only a few state
variables have to be considered for simulation and optimization, if the remaining state
variables stay approximately constant. Formally, this means the observed simulation
and optimization interval I has to be subdivided in a special manner. For the aims of
this contribution a Hierarchical Dynamic System HDS may be formalized by:
Deﬁnition 9.4 (Hierarchical Dynamic System (HDS)) If a pairwise disjunct par-
tition of sub-intervals I = ∪Ik = [0, T] can be found, with the property that a subset
(Xn′+1, . . . , XN) of all state variables (X1, . . ., Xn′, Xn′+1, . . ., XN) stays approximately
constant on each of the sub-intervals, a local simulation interval is deﬁned.
The variables of the local system are denoted with small symbols: ⃗x, q,⃗u, ⃗ϕ, ξ. The
variables of the global system are denoted with capital symbols ⃗X, Q, ⃗U, ⃗Φ, Ξ. The
function Ψ maps the entire dynamic system ⃗X′ = ⃗Φ(⃗X, ⃗U) to the local system
(X1, . . . , Xn′) = Ψ(⃗X) = ⃗x = ⃗ϕ(⃗x(t0),⃗u) and Ψ( ⃗U) = ⃗u
“Staying approximately constant” means that for a given ε > 0
∥(Xn′+1, . . ., Xn) ∥≤ε for all t ∈Ik
for each simulation interval Ik.
This procedure can be applied recursively to every sub-interval I k. A hierarchy of
simulation intervals is deﬁned by the characteristic time patterns of the simulation
model. This approach is known as the slavery principle and was ﬁrst described by


HIERARCHICAL DYNAMIC PROGRAMMING
177
Haken (1983). With this set-up an error of simulation is introduced. One can show
that this error depends on the length of simulation sub-intervals I k and the dynamics
of the simulation model. For linear systems one can show that a very efﬁcient set-up
of subintervals can be created if the eigenvaluespectrum shows distinct gaps (Seppelt,
1997, Chapter 4).
This approach is applied to the DP algorithm and offers a solution to the “dilemma
of dimensionality”. The computational effort for a solution of the optimum control
problem of the entire system is diminished, if Algorithm 9.1 can be modiﬁed to a
hierarchical dynamic system from Deﬁnition 9.4. Note that all above-mentioned
Deﬁnitions 9.1–9.3 can be applied to the local as well as to the global system. The
basic idea is to solve a local optimum control problem by DP once, and to use the
calculated state functions ξi every time a local problem has to be solved again.
Algorithm 9.2 (Hierarchical Dynamic Programming (HDP)) Accordingtothedy-
namic programming procedure for i = Q −1, . . ., 0 the state functions Ξ Q−i(⃗X(ti))
are calculated and the optimum control vectors ⃗U∗(ti) are stored as a function of
the system state ⃗X(ti). The estimation of Equation (9.1) requires either estimation
of the ﬂux or solution of a local optimum control problem on Ψ( ⃗X). In the last case
an optimization procedure according to Algorithm 9.1 is started, if no previously
estimated state functions Ψ(Ξi) = ξi(Ψ(⃗X)) are found. Once ξi are calculated, every
further request for a solution of the local optimum control problem makes use of the
previously calculated set of state functions.
This procedure diminishes the computational effort, as the recurrence equation (9.4)
has to be estimated for the local processes only once. All stage assessments ξq−i(⃗x(ti))
of the local problem are stored and can be used in the global optimization procedure.
For Algorithm 9.2 one can show that the global optimum solution is derived in a
similar manner as for Algorithm 9.1 (Seppelt, 1997, annex a.3). In addition to the
contradictory proof (Bellman & Kalaba, 1960), one has to ﬁnd an estimation for the
simulation error. This simulation error is caused by the assumption that several state
variables stay approximately constant, for numerical analysis see (Seppelt, 1997,
annex a.2).
With the introduction of HDS the computational effort of the DP procedures can
be diminished. Efﬁciency depends on how the HDS is set up. Consider a global
state/policy space of N/M variables with Ni, Mi possible values. An application of
the basic DP procedure requires
S = qQ
N
i=1
Ni
M
j=1
M j
steps to estimate Ξi, . . . , ΞQ, cmp. Equation (9.5). If local variables ⃗x, ⃗u with the
dimension n < N, m < M and ni < Ni(i = 1, . . ., N), m j < M j(j = 1, . . ., M) are


178
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
deﬁned, the computational effort is given by
S HDP = q
n
i=1
ni
m
j=1
m j + Q
N
i=n+1
Ni
M
j=m+1
M j
(9.6)
A crucial point of the hierarchical structuring of a multi-scale dynamic process in
terms of optimum control theory is that the identiﬁed time hierarchy may depend
on the current stage and the control vector. With a modiﬁcation of Equations (9.4)
Algorithm 9.2 can solve optimum control problems with a changing time schedule.
Let ν be a function that estimates the index of the succeeding stage of control j for a
given control vector⃗u(ti) and the current stage i so that j = ν(i,⃗u(ti)). In Equation (9.4)
the index i is replaced by ν:
ξq−i(⃗x(ti)) = max
⃗u(ti) Kq−i Jν(i,⃗u(ti))( · · · ), ξq−ν(i,⃗u(ti))( · · · )
for i = 0, . . ., q −2 (9.7)
This extension necessitates a restriction to the operator Ki(a, b), see Deﬁnition 9.2. If
certain stages i are omitted, Ki has to be identical for each stage: Ki(a, b) = K(a, b)
for all i = 0, . . ., Q.
Note, ν is not necessarily invertible. Before estimating Equations (9.4) all possible
stages of control are estimated. This may lead to set of possible stages of control
which are not taken into account during the estimation of the simulation trajectories
based on the optimumcontrol solution. However, the numerical effortis not increased
in that case because numerical effort is linear in time and number of stages.
If ⃗U, ⃗u, ⃗X or ⃗x are continuous, the problem is transformed into one with ﬁnite di-
mensions by approximating on a discrete grid in state or policy space, see Bellman
& Dreyfus (1962, Chapter IV). The interpolation error can be controlled by compar-
ing the interpolated results of the performance criterion with the exact value of the
performance criterion using the same control function.
The performance of the procedure can be improved if an appropriate deﬁnition of the
boundary of the state and policy space is deﬁned. If the state space boundaries are
violated, which may occur for distinct control vectors, these control vectors can be
treated separately:
Algorithm 9.3 (Treatment of Boundary Violation) If the calculation of Equation
(9.1) to a given control vector ⃗U(ti) violates the boundaries of state space, the fol-
lowing two cases are tested:
The state ⃗x(ti+1), ⃗X(ti+1)
1. describes a physiologically impossible constellation of state variables: the
control vector ⃗u(ti), ⃗U(ti) is marked as illegal. Further trajectories to this area
of state space will be excluded from policy space,
2. is physiologically possible, but outside of interpolation of state space: extrap-
olation will be used to estimate Equation (9.3).


HIERARCHICAL DYNAMIC PROGRAMMING
179
dp proc recalc() — Evaluation procedure estimating state functions Ξ, ξ
Repeat for each possible state ⃗X(tQ) (for continuous ⃗X refer to interpolation grid)
Evaluate performance criterion for ﬁnal stage
estimate JQ(⃗X(tQ)) (Call user-speciﬁed function criterion q())
Repeat for each stage ti (i = Q −1, . . . , 0)
Repeat for each possible state vector ⃗X(ti) (for continuous ⃗X refer to interpolation grid)
Repeat for each admissible control vector ⃗U(ti) (for continuous ⃗U refer to
interpolation grid)
Apply optimum control vector of this stage to system
modify ⃗X(t) by U(ti) (Call user-speciﬁed function control())
Estimate succeeding state
Estimate ⃗X
tν(i, ⃗U(ti)
according to Eqn. (9.1) (Call user-speciﬁed function
solve())
t = tν(i, ⃗U(ti)) estimate succeeding stage, if schedule depends on control vector
Evaluate performance criterion for this stage
Estimate Ji
⃗X(tν(i, ⃗U(ti))), ⃗U(ti)
(Call user–speciﬁed function
criterion i())
Identify ⃗U∗(ti) which maximizes Ji for this stage i and store state function Ξi
Fig. 9.1
Structure of HDP evaluation procedure. The estimation of Ξi or ξi for i = 0, . . . , Q
is performed in two steps: the calculation of JQ in the ﬁnal stage and then backwards to the
initial stage. After calling this procedure dp proc recalc() the calculated and stored state
functions are used to derive an optimum control solution to any possible initial condition, see
dp solve(). Remark: Initialization steps are omitted.


180
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
9.2.3
Program Library
Though DP solutions may dependon the speciﬁc problem(Bellman&Dreyfus,1962),
generic code was developedthat is applicable to a general dynamic system, which can
be written in the notation of Deﬁnition 9.1 and which can be hierarchically structured
according to Deﬁnition 9.4: the Library for Hierarchical Dynamic Programming 1
(LibHDP), (Seppelt, 2001). Figure 9.1 and 9.2 display a Nassi–Schneiderman dia-
gram for the core Algorithm 9.2 of HDP:
• Procedure dp proc recalc(): estimation of state functions Ξi, ξi, cf. Fig-
ure 9.1;
• Procedure dp solve(): estimation of the optimum control solution based
on the state function, cf. Figure 9.2.
Note, the recursive call of the optimum control problem solver for the local problem
in the procedure dp solve introduces the hierarchical concept. Recursive calls
terminate because the evaluation procedure dp proc recalc has to be called only
once in the algorithm, see Figure 9.2.
The following sub-libraries and numerical procedures are embedded:
• high order numerical solution of ODE systems with automatic step-size con-
trol, based on the Runge–Kutta formulae DOPRI5 and DOPRI8, see Hairer et
al. (1980);
• n-dimensional interpolation in state and policy space using linear and constant
interpolation functions;
• generation of interpolation grids in state and policy space (time-dependent, not
equally distributed);
• treatment of boundaries of state and policy space according to Algorithm 9.3.
The implementation of the numerical solution of an optimum control problem with
this library requires the following steps:
1. Deﬁnitionof hierarchicaldynamicsystem and hierarchical Q/q-stage processes
with model functions ⃗ϕΔt(⃗x,⃗u) and ⃗ΦΔT(⃗X, ⃗U), procedure solve(). In the
case of embedded ordinary differential equation systems, the sub-libraries DO-
PRI5 or DOPRI8 can be called.
2. A procedure control() must be deﬁned, which modiﬁes the state vector ⃗X
according to a given control vector ⃗U.
1See p. 279 for availability of software.


HIERARCHICAL DYNAMIC PROGRAMMING
181
dp solve() — HDP optimum control problem solver
yes
Does the dynamic system require the solution of an optimum control
problem for this stage ti?
no
yes
Do the ξi(i = 0, . . . , q) exist?
no
Estimate state function of local optimum
control problem
Estimate state function ξi for
(i = q, . . . , 0) for the local system and
store results. Recursion:
dp proc recalc() will call this
function again. (Call
dp proc recalc())
While t < tq do
Estimate ⃗u∗from ξ(t) as a function of current state
⃗x(t). In the case of continuous ⃗x use interpolation to
derive ⃗u∗from the nearest state vectors stored by
state functions, e.g. multi-dimensional linear or
constant interpolation
Apply optimum control vector of this stage to system
modify ⃗x(t) by u∗(Call user speciﬁed control())
Estimate succeeding state
Estimate ⃗x tν(i,⃗u∗)
according to Eqn. (9.1) (Call
user-speciﬁed function solve())
t = tν(i,⃗u∗) estimate succeeding stage, if schedule
depends on control vector
Estimate succeeding state
Estimate ⃗x (ti+1) according to
Eqn. (9.1) (Call user–speciﬁed
function solve())
t = ti+1
Return current state ⃗x(t) and stage t
Fig. 9.2
Structure of HDP optimum control problem solver dp solve(). The function
is the optimum control problem solver, either as a ﬁnal solution of a given optimum control
problem or as a local part of a structured HDP problem


182
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
3. Set up performance criterion J[ ⃗X, ⃗U] with Markoff property. According to
Equation (9.2) this means Ji (i = 0, . . ., q −1) and Jq are set up separately. JQ
is deﬁned by procedure criterion Q() and criterion i() deﬁnes Ji
for (i = 1, . . ., Q −1). The operator K(a, b) is speciﬁed by an identiﬁer when
calling the procedure dp proc recalc().
4. Set up main code. This is supported by several library functions which can be
used
– to set up the interpolation grid,
– to run the DP or HDP procedure, which recursively estimates Equa-
tion (9.4),
– to calculate an optimum control solution to a given initial state, and
– to apply a given control vector to the dynamic system.
9.2.4
Concluding Remarks
However the described developments of HDP are initiated by the identiﬁed mathe-
matical heterogeneity of environmental simulation models, applications of HDP for
technical systems were studied and compared to genetic programming algorithms in
Chouikha (1999). The optimum control procedure was used to set up an optimum
control system model by a hybrid Petri net. The comparison to genetic algorithms
shows that DP/HDP procedures are less efﬁcient, if it is not possible to re-use precal-
culated solutions in further steps of optimization, see Chouikha (1999, p. 157).
The proposed framework for optimum control and the HDP procedure can be used as
a general concept applicable to a large class of environmental models. Mathematical
heterogeneous systems can be treated within HDP. To apply HDP it is not necessary
to know any derivatives of the system to state or control vectors. The possibility of
iteratively excluding control vectors which lead to physiologically impossible stages
is an important feature, especially for ecological systems which may be calibrated
only for a distinct subset of system space.
On the other hand, the “dilemma of dimensionality” is an intrinsic property of the
underlying DP procedure. It offers approaches to this problem with special respect
to environmental models. But this problem cannot be eliminated completely. In
the following Chapters 10 and 11 the concept is used to solve several problems of
identiﬁcation of optimum management strategies in agroecosystems.
9.3
OPTIMIZATION AND SPATIALLY EXPLICIT MODELS
Introduction
Optimization in spatially explicit models differs entirely from the
task of optimum control theory anddeﬁnes a new class of optimizationproblems. Two


OPTIMIZATION AND SPATIALLY EXPLICIT MODELS
183
main topics are responsible for this difference. First, the vector of control variables ⃗u
to be determined is in this case a map of vectors. Without loss of generality we focus
on raster-based spatially explicit models. The observed region is denoted by a set of
discrete grid points R = {(i, j) | ni < i < Ni; m j < j < M j}. A grid cell of the map is
denoted by ⃗z = (i, j).
Second, the formulation of a scalar performance criterion has to map the space of
control and state variables to a scalar value. As state and control variables depend on
time and space, a performance criterion for spatially explicit optimization problems
is given by double integral in space and time, see Equation (8.1).
9.3.1
Computational Effort
The number of control variables to be determined is increased by the size of the in-
vestigation site |R|. Assume the control vector is deﬁned by two variables: a discrete
variable u1 with n1 different attributes and a continuous variable u 2 ∈[a, b]. In terms
of a combinatorial analysis of complexity we can assume that an appropriate dis-
cretization of u2 into, for instance, n2 discrete values can be given. The combinatorial
effort of identifying a optimum control map ⃗u(⃗z) for all ⃗z ∈R is given by the term
|R|n1n2. Complexity increases more than exponentially.
Against this background it is obvious that solutions of optimization problems in
spatially explicit models require an appropriate methodology as well as some general
simpliﬁcations. In general, we do not aim at the aggregation or simpliﬁcation of
the model itself, cf. Figure 8.2. In the following the structure of the general spatial
performance is analyzed to ﬁnd a simpliﬁcation of the problem.
9.3.2
Local and Global Performance Criteria
A spatially explicit ecological model offers a fascinating functionality in the assess-
ment of ecosystem functions. The ability of accessing any state variable at any loca-
tion in the investigation site is a function that makes spatially explicit models distinct
from all others. Imagine, for instance, that one is able to trace the concentration of a
speciﬁc substance at the mouth ⃗z0 of a watershed: xi(⃗z0). An optimization problem
can easily be written in the form: identify the management patterns for maintaining
the value of xi(⃗z0) below a deﬁned constraint or minimize this value, while locating
a maximum area of certain habitats.
The difﬁculties inherent in this optimization problem are obvious. The identiﬁcation
of an optimum location of the habitat is a large combinatorial problem with a single
restriction based on the assessment of the single value xi(⃗z0). A problem like this is
denoted as global optimization problem.
Task 9.1 (global problem) Find maps u∗
1, u∗
2, . . . which maximize J →max accord-
ing to Equation (8.1).


184
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
It is difﬁcult to solve a problem like this, with a complexity increasing more than ex-
ponentially, from scratch, that means without any knowledge of approximate patterns
of the solution.
To simplify the problem we can make use of the fact that spatially explicit models are
set up by a repeated application of the same model to different spatial units (either
so-called ecotopes, elementary landscapes, or raster cells, see Sections 3.3.1 to 3.3.3).
This implies that the state of the variable xi at location ⃗z0 is a result of the value of
xi of all cells ⃗z ∈R. Some cells may contribute more, some may contribute less, to
the ﬁnal result of xi(⃗z0) and the relationship between xi(⃗z),⃗z ∈R and xi(⃗z0) is highly
likely to be nonlinear.
The basic idea that follows from this is to deﬁne a local performance criterion in each
grid cell. This is structurally a different way, because it aims to map the regional goal
function onto the processes in a grid cell. The basic idea is to set up characteristic
functions, which are part of the performance criterion and are spatially dependent, as
part of the goal function. This approach is comparable with a functional decomposi-
tion of the landscape using a spatially explicit simulation model, compare (Cornwell
et al., 2001).
A general equation that summarizes the calculation of goal functions for each grid
cell is
Ai(⃗z) =
tend
0
⃗λT
⃗x(t,⃗z)
⃗u(t,⃗z)
dt
i = 1, 2, . . ., k
(9.8)
Ai are maps that hold local scalar values estimated from calculating the weighted sum
of state and control variables and aggregate this to a scalar value by integration over
time.
The derived maps may then be estimated by calculating
J[⃗x,⃗u] =
R
k
i=1
Ai(⃗z) d⃗z
(9.9)
Integration over the investigation site R aggregates the map variables A i to a scalar
spatial goal function J. Based on this one can formulatea local optimization problem:
Task 9.2 (Localized Problem) For each cell z ∈R estimate Ai(⃗z) (i = 1, 2, . . ., k).
Based on these characteristic functions maximize J (z) →max according to Equa-
tion (9.9).
Note that spatially explicit optimization is simpliﬁed to the estimation of maxima of a
reduced set of characteristic functions A(⃗z)[⃗x,⃗u] that can be evaluated independently
for each cell ⃗z ∈R.
Obviously the solutions from Task 9.2 are different from those of Task 9.1. The goal
function of Task 9.1 neglects any neighborhood relationships in the control variable


OPTIMIZATION AND SPATIALLY EXPLICIT MODELS
185
maps. The question is, how large are the differences in the solutions, or do these
solutions have more in common than one would expect? The next section will show
that the numerical effort for the estimation of solutions for Task 9.2 is orders of
magnitudes lower compared to Task 9.1.
How is this achieved? The second basic idea related to the solution of the localized
problem is that reducing the global performance criterion to a localized problem for
each grid cell allows us to neglect the spatial explicitness of the control variables.
We can assume constant maps of control variables ui(⃗z) = ui for all ⃗z ∈R. Searching
through all possible combinations of control is reduced by applying the control input
homogeneously to the entire study area.
Up to this point we have assembled all the important issues that allow us to solve
optimization problems on spatially explicit models. Figure 9.3 summarizes the con-
cept that is derived from this distinction of local and global optimization tasks and
performance criteria, including important additional steps of solution analysis.
The ﬁrst step in this concept is to perform a grid search to identify the characteristic
functions Ai(⃗z) that deﬁne the spatial performance criterion.
9.3.3
Grid Search Strategy on Local Problem
The ﬁrst step is to solve Task 9.2. The implementations described in the following
makes use of the ability of the landscape model formulated within the framework
of the spatial modeling environment to deal with spatially distributed information
and to perform mathematical operations on maps, cf. Sections 1.5.5 and 3.3.3. The
characteristic functions Ai(⃗z) of the local goal function are formulated as maps that
are calculated using the spatially explicit model.
The solution of Task 9.1 performs a grid search through the entire control space
assuming a homogeneous control variable ⃗u(⃗z) for each cell. A series of maps for
different combinations of control variables is generated and fed into the spatially
explicit model. Maximizing J(⃗z) for every grid cell depending on the precalculated
maps of the goal functions Ai(⃗z) solves the optimization problem. The result is a set
of control variables that optimize the local performance criterion.
The computational effort can be estimated from this. In terms of a combinatorial
problem for an optimization based on the local optimization task, kn 1n2 runs of the
spatial explicit model are required, using n1 and n2 as examples for a set of control
variables u1 and u2, see above.
The resulting maps of optimum control variables are then fed into a spatial simulation
again that is used to calculate the global performance criterion, cf. Equation (8.1).
9.3.4
Disturbing a Solution: Monte Carlo Simulation
The results from the local optimization approach can be tested by running a Monte
Carlo simulation based on the optimum control variable maps. This Monte Carlo


186
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
Monte Carlo Simulation
stochastic generation of
f(c), f(c) derived of recent
land use data
p1 = 1
Initial population of
maps “from scratch”
with control variables
Initial population based
on local optimum
solution
1
2
No solution in acceptable time
spatially local perfor-
mance criterion as
function of location
( )
K
r
,2,1
=
i
z
Ai
Monte Carlo Simulation
f(c) derived from local
optimization,
1
0
1 <<
< p
Statistical Analysis:
Information on the variability
of the process, and the
underlying data
Integrated in ArcView Frontend
Grid Search
Run spatially explicit model
for homogeneous control
K
r
,2,1
,
)
(
=
∈
∀
=
i
R
z
U
z
U
i
i
Run spatially explicit
model on optimum solu-
tion
Run spatially explicit
model on optimum solu-
tion
Optimization (GA)
Iterative run of spatially
explicit model
Optimization (GA)
Iterative run of spatially
explicit model
(
)
max!
,
→
= ∫∫
R
dt
z
d
u
x
f
J
λ
,2,1
)
(
*
=
i
z
Ui
,2,1
)
(
*
=
i
z
Ui
spatially explicit optimized
control variables
,2,1
)
(
*
=
i
z
Ui
,2,1
)
(
*
=
i
z
Ui
(
)
max!
,
→
= ∫∫
R
dt
z
d
u
x
f
J
λ
( )
( )
max!
,
2
,1
→
= ∫∑
=
dt
z
A
z
J
i
i
Local Optimization
Estimation of optimum
control maps so that
spatially explicit control
variables
Fig. 9.3
Framework for the estimation of the spatial optimum concept for optimization of
land use patterns and related control variables.
simulation disturbs the optimum solution stochastically and gives an estimate of how
close the local solution is to the unknown optimum.
The set up of a Monte Carlo simulation depends on what is known about the dis-
tribution of the parameter to be varied. If the variable is continuous, a continuous
distribution with a mean and a variance must be deﬁned. Disturbance in this context
means that the mean value is set equal to the derived local optimum value and a
variance value is deﬁned that speciﬁes the range of variation.
If the variables are discrete or categorical, the disturbance of a solution is a two-stage
stochastic process. Let Z1(⃗z) ∈[0, 1] be a random variable. A new value for the
considered control variable u1 is generated randomly if Z1(⃗z) < p1 for cell ⃗z. This is
done by a stochastic variable Z2 such that P Z2(⃗z) = u2(⃗z) | Z1(⃗z) < p1 = f(u2).
For every cell ⃗z the stochastically generated variable u2 follows a distribution which
is deﬁned by a density function f. The density function f is constant for the entire
region and may be generated by a stochastic process, started before generating the
stochastic map. Or, it may be derived from the distribution of a known pattern, for


OPTIMIZATION AND SPATIALLY EXPLICIT MODELS
187
instance the optimum solution. With this set up three different types of Monte Carlo
simulations can be distinguished:
• p1 = 1, f generated stochastically: patterns are generated from scratch,without
any knowledge about a possible spatial pattern;
• p1 = 1, f derived from known patterns such as historic data or optimum local
solutions: patterns are based on reallocations.
• p1 = 0.01x and f(C) derived from optimum solution: patterns are disturbances
of optimum solutions by a certain percentage x.
9.3.5
Genetic Algorithm Solving the Global Problem
As we have seen in the previous sections the global optimization problem cannot
be solved in terms of a combinatorial optimization problem. The application of
iterative procedures, which are usually based on gradient search algorithms, may be
inappropriate since in many cases the derivative can be estimated neither analytically
nor numerically. This is because of the complexity of the ecosystem model and the
combination of discrete and continuous control variables.
Genetic algorithms offer a solution to the optimization problem based on the global
performance criteria. The ﬁrst step of GA is to deﬁne a representation of the control
variables of the optimization problem to a genome. Based on the idea of “survival
of the ﬁttest” a stochastically generated ﬁrst population of a distinct number of indi-
viduals runs through an evolutionary process. GA determines which individuals of
a population should survive, which should reproduce, and which should die. New
individuals are created based on the operations of cross over, mutation, and gene
migration.
Application of GA to an optimization problem requires three steps
1. Deﬁnition of a representation
2. Deﬁnition of the genetic operators
3. Deﬁnition of the goal function
The goal function for the problem in hand is given by Equation (8.1). Common
libraries support the second step. We used a C++ Library of Genetic Algorithm
Components (GALib), see Wall (1996). The ﬁrst step, the representation of the
control variable ⃗u(⃗z) of the spatially explicit model to a genome is deﬁned as follows
• Each controllable cell z ∈R deﬁnes a single gene gk, k = 1, . . ., |R|. The
genome has the length |R|.
• The location of the gene in the 1-dimensional array genome string is identiﬁed
with the location of the cell in the grid map k −→⃗z = (i, j) ∈R.


188
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
• Discrete control variables are an attribute of a cell or gene. Continuous control
variables need to be approximated by a discrete value to be coded by GA. The
control variables are therefore deﬁned by an allele set L = (u1, u2, . . .) for each
gene.
Before starting the genetic algorithm an initial population has to be generated, usually
performed by cloning a given individual. We used different populations derived from
the three stage stochastic process used for the Monte Carlo analysis. The initial
population therefore is based on a stochastic variation of a local optimum land use
and fertilizer pattern parameterized by the probability p 1.
The global optimization problem can be solved by basing it on the GALib library. For
each generation the algorithm creates an entirely new population of individuals by
selecting from the previous population, then mating to produce the new offspring for
the new population. Each new individual of the population requires a run of the entire
spatially explicit simulation model. The “survival of ﬁttest” strategy is implemented
by evaluating the goal function. This process continues until the stopping criteria are
met (determined by the terminator).
Figure 9.3 summarizes the methodological concept described in a ﬂowchart. Two
main branches are used: Branch 1 starts with the estimation of characteristic function
maps, which are the basis for local optimization; Branch 2 shows how to work on the
optimization problem without any knowledge of an appropriate initial guess of the
solution.
9.3.6
Toolbox for Spatially Explicit Optimization
Structure
The frameworkdescribed above is implemented in the Toolbox for Spa-
tially Explicit Optimization2 (TSEO). Parts of this toolbox interact with the spatial
modeling environment, other parts support analysis of the results within the geo-
graphic information system ArcVIEW. The toolbox is structured in three parts:
1. A geographic information system that is used for visualization of the results
and offers a graphical front end for the most important functions of the concept.
2. A spatial explicit dynamic system, that is capable of simulating environmental
processes on a raster-based data structure.
3. Several programs that set up the toolbox for spatially explicit optimization
of dynamic systems. These programs offer the functionality summarized in
Figure 9.3. The TSEO command-line interface supports a simple access to the
programs of the toolbox.
Exchange of data and maps between these three parts is performed within a database
structure using ArcVIEW ASCII raster map format. Spatially explicit simulation
2See p. 279 for availability of software.


OPTIMIZATION AND SPATIALLY EXPLICIT MODELS
189
Fig. 9.4
Screen shot of ArcVIEW front end with the local optimization project.
models that are capable of reading and writing the model output in this format are
therefore applicable in the toolbox.
Graphical Front end ArcVIEW
These concepts require the minimal computa-
tional effort so the steps of local optimization and solution analysis are embedded in
the GIS front end ArcVIEW and the results are presented as a simple visualization.
Figure 9.4 shows a screen copy of the ArcVIEW display with a parameter study of
the land use distribution in the Hunting Creek watershed.
Spatially Explicit Simulation Model
TSEO assumes a predeﬁned spatially ex-
plicit model using a raster-based data structure for the spatial information to be used
in the optimization process.
The desired performance criterion is rarely part of the simulation model. Because
of this, for application of the optimization toolbox, the simulation model has to
be modiﬁed to support the optimization toolbox with required information. This
information relates to the performance criterion to be maximized. Variables used in
the performance criterion are not usually part of the model, as these variables often
calculate aggregatedindicators of the model system, such as integrals or sums of state


190
PREREQUISITES: TEMPORAL HIERARCHIES AND SPATIAL SCALES
variables. Or, these indicators reﬂect on boundary conditions or contraints, which
are to be met during simulation time. In terms of variables introduced above, within
a user code part of the model variables like Ai(⃗z) are to be calculated, cf. Equation
(9.8). At the end of the simulation these maps have to be written to the database.
Functions of Toolbox
The toolbox supports the main functions of the concept.
These are the grid search in local problem, the identiﬁcation of optimum maps based
on grid search, a Monte Carlo analysis, and the global optimization with genetic
algorithms.
The following documentationrefers to the implementation using the spatial modeling
environmentfor spatial modeling, cf. Sections 1.5.5 and 3.3.3. If a different modeling
environment is used, the steps of initialization and run control of the model system
have to be adapted.
Starting from a previously compiled simulation model, the ﬁrst step is to initialize
a database that stores optimization results as well as intermediate information. This
is performed by the declariation of all SME parameters like the name of the project,
the scenario and the path to the database. The command tseo init initialises the
database structure according to the current settings of project, model, scenario.
A solution of the localized optimization problem (Task 9.2) is estimated by ﬁrst
running a grid search of the (simpliﬁed) space of control variables, started by the
command
tseo grid.
The information obtained from the grid search — these are the maps A i(⃗z) — is
intermediatelystored in the database. Solutions of the localized optimizationproblem
can be calculated depending on parameters of the performance criterion, usually
denoted by a weighting scheme ⃗λ = (λ1, . . ., λn). For a solution of Task 9.2 values
for these weights are to be speciﬁed
tseo local [<lambda_1> [...] | loop]
This instruction stores maps of optimum control variables ⃗u ∗(⃗z) into the database that
specify the spatially explicit optimum solution for the given vector of weights of the
performance criterion. Running the spatially explicit model (see next step) uses this
map to study the simulation changes according to the obtained solution.
An analysis function supported at this step of the framework is the analysis of the
solutionsdependingonvariationofacertainweightλ i. Theloop-taginthecommand
line is used to start a sensitivity analysis. The weight λi which is not speciﬁed in the
command line and replaced by the loop-tag is changed according to the information
by a parameter ﬁle. The results of this scenario analysis are graphically displayed
using the command tseo plot.
A Monte Carlo analysis is started by using the commandtseo mc <prob>. Monte
Carlo analysis starts from the previouslycalculated optimum maps of the control vari-
ables. The control variable maps are used and randomly modiﬁed by the probability


SUMMARY
191
given by <prob>. The program started needs to be aborted manually using CTRL-C
key, as Monte Carlo analysis is implemented by an endless loop.
A solution of the global optimization Task 9.1 is calculated using genetic algorithms.
To estimate an initial population optimum maps are identiﬁed for a certain vector of
weights (compare tseo local-instruction). From the optimum maps of control
variables an initial population for GA is stochastically generated by a random modi-
ﬁcation of the probability given by <prob>. The statement for global optimization
is therefore
tseo global [<lambda_1> [...]] <prob>
Note, this is a very time consuming task. One may trace the protocol ﬁle to assess
convergence success. The command may be aborted by CTRL-C.
If maps of control variables were previously calculated (either by local optimization
or by global optimization) these maps are now fed into the model and a spatial
optimization is performed using the command tseo run.
Several other functions are available for database management, edititing of conﬁgu-
ration, and import/export of data. For additional information the reader is referred to
the technical documentation of the toolbox (Seppelt, 2003).
9.4
SUMMARY
The ﬁrst step of identifying a general or generic notation for optimization of optimum
control problems with mathematically heterogeneous models was identiﬁed as the
core problem of applying environmental models in optimization. The formulation of
the task needs to cope with the hybrid structure of an environmental model.
This chapter showed, that general tools for solving environmental management prob-
lems can be developed by combining different tools of numerical mathematics and
by making use of some general properties of environmentalsystems for instance their
hierarchical structure. In the following chapters we will now study applications of
these concepts.


10
Optimum Agroecosystem
Management:
Temporal Patterns
10.1
INTRODUCTION
In this chapter applications of the agroecosystem model, summarized in Chapter 2, to
optimum control theory are presented. The applications consider optimum fertilizer
application,pestcontrol,andcroprotationschemesasadynamiccontrolproblemwith
different time scales. All forcing functions deﬁned in Chapter 2 are used as control
variables and are fed into optimizationprocedures. Several solutions are presented for
a German investigation site. Different assessment scenarios of production schemes
are compared with the tool of optimization.
Managementof agriculturalregions is a good exercise of environmentalmanagement.
Farmers are directly inﬂuencing ecological systems and are mutually dependent on
these systems. Therefore the question of optimizing management strategies arises.
Optimum control theory offers the connection between simulation models, evaluation
of the environmental system states, and anthropogenic management.
Estimation of optimum management strategies of agroecosystems in terms of opti-
mum control theory requires:
• formulation of an appropriate and probably complex spatially explicit simula-
tion model for an agricultural region with the incorporation of farmers man-
agement; and
• deﬁnition of a performance criterion (and — as needed — constraints) which
assesses the observed variables and assigns a set of state variables to values
193


194
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
identiﬁed with “good” or “bad” environmental states, whatever this means in
the considered context.
The ﬁrst item has been presented in Chapter 2 and 3. The second item was discussed
at a theoretical level in Chapter 8. Considering agroecological processes the task is to
deﬁne an appropriateperformancecriterion based on the state and control variables of
the model in Section 2.7. The overall goal is the estimation of optimum management
schemes with respect to ecology and economy (Seppelt, 1999).
10.2
ASSESSING THE STATE OF AN AGROECOSYSTEM
10.2.1
External Cost and Non-measurable Variables
The chosen example of an agroecosystem model is typical for environmental mod-
eling. It shows the solution of two important problems in ecosystem management:
the determination of long term strategies with the use of the temporarily structured
models and regionalized management optimization.
As shown in Chapter 8 performancecriteria have to integrateeconomicand ecological
issues. Economic issues are, for instance, prices for yield, farmers’ income, and
prices for fertilizer, farmers’ expenses — the ﬁrst to be maximized, the latter to be
minimized. Further economic issues may focus on taxation of fertilizer, reduction of
fertilizer input, or to fulﬁll restrictions on fertilizer application in terms of constraints.
The nutrient content in soil or the infestation of pests are examples for the ecological
part of the assessment. Whereas the former economic assessment could be deﬁned
by a monetary unit, it is difﬁcult to identify units for ecological variables. Ecological
and economic issues are difﬁcult to compare.
Considering the issue of the openness of ecological systems in the agroecosystem
model, external costs are the loss of nutrients out of the rooting zone, the loss of
pesticides (either by volatilization, runoff or leaching).
Examples for unmeasurable variables in the agroecosystem are the amount of nitrogen
leachedoutoftheplant-accessiblerootzone. Nutrientoutﬂowintogroundwaterorthe
population of a pest, like the sugar beet cyst nematode, are very difﬁcult to measure.
10.2.2
Performance Criteria
Referring to the generic agroecosystem model (see Section 2.7) the state variables
crop yield WC, plant available nitrogen content N, pesticide in soil C S are used to
assess the state of the system. Additionally the control variables applied fertilizer
F, applied pesticide A, and planted crop α are considered. All state and control
variables are time-dependent. For this reason an aggregation, in mathematical terms
an integration or accumulation of the variables, is required to obtain a single scalar


ASSESSING THE STATE OF AN AGROECOSYSTEM
195
Table 10.1
Overview of the considered scenarios and their performance criteria with the
assessed variables and the weights λi. Weights are set to zero in Equation (10.1) for variables
which are not assessed in a performance criterion, denoted by the missing •. Constraints are
understood as constraint for the entire region, e.g. for all⃗z ∈G. All goal functions are quantiﬁed
by monetary unit per area [e/ha].
Scenario
Assessed variables in Equation (10.1)
Additional constraints
WC
N
CS
F
A
J1
”economic”
•
•
•
J2
”taxes”
•
•
J3
”ecologic”
•
•
•
•
•
J4
”N-limit”
•
•
N(T) < Nmax
J5
”F-limit”
•
•
  F(ti) < Fmax
Weight
λW
λN
λC
λF
λA
value. Referring to the general performance criterion deﬁned in Equation (8.2) the
following performance criterion J can be deﬁned:
J[WC, N,CS , A, F, α]
=
λW(α(t,⃗z))
 R
WC(tend, α(tend,⃗z),⃗z) d⃗z
−
 R
tend
 0
λFF(t,⃗z) + λAA(t,⃗z) dt d⃗z
−
 R
tend
 0
λNklN(t,⃗z) + λCklCS (t) dt d⃗z
(10.1)
Note, an integration is performed in time as well as in space. If a non-regionalized or
not spatially explicit model is considered the integration in space of the investigation
site given by R can be dropped.
The performance criterion in Equation (10.1) additionally incorporated some parts
of the simulation model: the terms klN as well as klCS integrate the amounts of
transported matter our of the rooting zone, assuming a linear ﬂow k l.
10.2.3
Weighting Schemes
With the weights λi the different state and control variables are aggregated to a scalar
performancecriterion. Setting up values for the weights requires answers to the above
stated problems of comparing economic and ecological variables, openness and the
use of measurable and non-measurable variables. Different sets of λ values deﬁne
different assessment scenarios and with this different perspectives to optimality.


196
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
Table 10.2
Weights in performance criterion for different crop growth models.
Crop
Sugar
Spring
Oats
Winter
Winter-
Field
Oil
beet
barley
wheat
barley
beans
radish
Abbr. (α)
sub
spb
oa
ww
wb
fb
or
Crop-dependent parameters of performance criteria
λW
(J2)
17.1
18.4
19.2
18.5
18.5
—
—
[J/kg]
(all other)
0.4
0.32
0.28
0.08
0.07
0
0
[e/kg]
λN
(J3)
15.5
10.5
9.5
10.5
10.5
—
—
[e/kg-N]
Fmax
(J5)
136
124
81
124
158
—
—
[kg-N/ha]
Vegetation period
Sowing in
April
April
April
Nov.
Oct.
May
May
Day of year
91
91
91
284
264
121
121
[d]
tend
188
137
122
280
300
150
120
[d]
λ values for the different criteria
• can be derived from market prices (“economic” criterion);
• may be modiﬁed by taxation of fertilizer (“taxes” criterion);
• are estimated by internalization of external effects. This makes use of the
approach of an assessment relative to non-disturbance (Nilsson & Bergstr ¨om,
1995) (“ecologic” criterion);
• can be supportedby constraints like limitation of total fertilizer input (“F-limit”
criterion) or of nutrient content in soil at harvest time (“N-limit” criterion).
Table 10.1 summarizes these performance criteria. Obviously not all criteria are
based on measurable variables. It is necessary to study the results of these different
optimization criteria.
As these market prices depend on the crop planted, the weighting scheme of the
performance criterion changes as a function of the control variable α (planted crop).
Table 10.2 lists all weights that are derived from market prices of energetic balances.
10.3
AGRICULTURAL OPTIMUM CONTROL PROBLEM
10.3.1
Optimization Task
We are now able to formulate a general optimum control problem based upon the
knowledge of the agricultural process summarized in a simulation model:


AGRICULTURAL OPTIMUM CONTROL PROBLEM
197
Task 10.1 Based on the agroecological model in Section 2.7 estimate a function
of optimum fertilizer input F∗(t,⃗z), of pesticide application A∗(t,⃗z) and a sequence
α∗(ti,⃗z) of planted crop, so that a performance criterion J is maximized.
Note that
• Fertilization and pesticide application are discrete events. It follows that not
only the amounts but also the time of optimum application must be estimated.
• Thespatialdependencyoffertilizer,pesticideapplicationandmodelparameters
complicate the problem tremendously.
• With the speciﬁcation of the control variable planted crop α, a set of model
parameters and also the model structure is changed during simulation.
Temporal patterns of this task are studied in detail in this chapter. Chapter 11 studies
the resulting spatial patterns of the optimization task.
10.3.2
Hierarchical Structure of the Problem
The underlying procedures for solving the numerical optimization problems are de-
rived from the dynamic programming approach, introduced in Section 9.2.
The
algorithm is appropriate for the given problem, as it can cope with the hybrid system
with discrete and dynamic properties. However, to reduce computational effort a
hierarchical structure of the problem is recommended. The hierarchical structure for
this problem can be derived from the different temporal scales used in the model.
The optimum control problem is at ﬁrst structured using the hierarchy in time, which
is deﬁned by the process dynamics. One can distinguish between fast processes like
crop growth, pesticide dynamics, fertilization, and pesticide application and slow
processes like population dynamics and crop rotation design. Additionally, control
variables may be continuous and discrete.
The problem can be structured in the framework of a hierarchical control model.
In a ﬁrst step a local optimum control problem is solved, with the optimization of
fertilizer input in a vegetation period for each crop. These solutions are stored as a
function of initial values and crop identiﬁers. In the second step, the global optimum
control problem is solved and an optimum crop rotation is estimated where every crop
receives its optimum fertilizing scheme. In this step the performance criterion makes
use of the performance criterion of the local problem.
Jn[N, J] =
Q

i=1
Jn[WC, N, F, A,CS] −ΛN
 R
tend
 0
klN(t,⃗z) dt d⃗z
(10.2)
The solution of this global task makes intensive use of the previously stored local
solutions which reduces computational effort and couples a discrete and continuous
optimum control solution.


198
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
Table 10.3
Comparison of optimal fertilizing strategies from different performance criteria
and crops. The last column shows literature values of expected yield and recommended fertil-
izer (Niesel-Lessenthin, 1988). Total amounts of applied fertilizer from J3 printed in italics are
used as Fmax values for J5. All values in kg/ha. Symbols are: WC(tend) harvest biomass, Ntot
total amount of nitrogen leached from root zone during vegetation period, Ftot total amount of
fertilizer applied (optimized).
J1
J2
J3
J4
J5
Reference
”econ.”
”taxes”
”ecolog.”
”N(tend)–
”Fmax–
values
limit.”
limit.”
Sugar
WC(tend)
18000
13700
13000
17400
12100
13000–26000
beet
Ntot
62
47
21
50
26
Ftot
305
228
136
236
128
140–210
Winter
WC(tend)
10400
9600
9000
10100
8400
7600–14400
wheat
Ntot
67
28
23
35
24
Ftot
208
138
121
160
113
100–210
Winter
WC(tend)
13600
12800
11200
12300
11300
7600–14400
barley
Ntot
67
53
39
48
44
Ftot
290
192
158
179
147
100–210
Spring
WC(tend)
15000
14000
10000
13000
9600
6400–11200
barley
Ntot
36
25
11
22
13
Ftot
294
202
124
178
118
100–170
Oats
WC(tend)
10300
9400
5600
9000
6100
6400–12400
Ntot
33
21
8
19
9
Ftot
241
142
81
130
75
80–170
10.4
SHORT-TERM SOLUTIONS: MANAGING A VEGETATION PERIOD
10.4.1
Optimum Fertilizing Schemes
The estimation of optimum fertilizing schemes to different performance criteria (see
Table 10.1) are derived ﬁrst. Table 10.3 contains the results of total fertilizer appli-
cation, harvest biomass, and leached nitrogen for different crops. Literature values
are added for comparison (Niesel-Lessenthin, 1988). Optimum fertilizing schemes
from “economic” lead to a maximum consumption of fertilizer with a high amount
of nitrogen loss. A reduction of fertilizer input can be achieved with governmental
restrictions. With the use of “taxed” fertilizer (J2) or the limitation of harvest nitrogen
pool N(t) < Nmin = 45 kg/ha (J4), total fertilizer input is reduced by 30%. This leads
to a reduction of nitrogen loss in the same range, while yield reduction is less than
15%.
Introducing external costs into assessment (J3) results in the lowest values of leached
nitrogen after vegetation period: less than 60% of the results of J 1. This fertiliz-


SHORT-TERM SOLUTIONS: MANAGING A VEGETATION PERIOD
199
DC 0-19
DC 20-29 DC 30-49 DC 50-69 DC 70-87
DC 87-
0.0
0.1
0.2
0.3
0.4
0.5
0.6
0.7
„ecologic“ J3
„N-limitation“J4
„taxes“J2
Fig. 10.1
Distribution of optimum fertilizer amounts of grains in the main development
stages for different performance criteria. Standard deviation is calculated based on fertilization
schemes applied to different grains (winter sheat, winter barley, oata, spring barley).
ing scheme incorporates a notable reduction of yield: 25% less than the results of
“economic” assessment.
These calculations use a unmeasurable variable for assessment, due to the nonzero
weight λN. One can ask for an assessment based on these results using measurable
state variables. This problem is solved using J5 for assessment. This limits the
maximum amount of applied fertilizer to F max =
 F∗
i using the optimum fertilizing
schemes F∗calculated on the basis of the “ecological” assessment with J3.
On a closer examination the optimum function F ∗(t) explains the time dependence of
the fertilizer application. For a comparison of the fertilizing schemes the results of
the grain-models are taken for detailed study. A comparable time scale can be deﬁned
using the stages of development denoted by the development code, see Section 6.2.1
and (Zadoks et al.,1974). Figure 10.1 summarizes the distribution of fertilizer (results
of optimumcontrol assessed by J1, J3, J4 in the developmentstages normalizedby the
total amount). This ﬁgure explains why the solution of J 3 attains a 60% reduction of
fertilizer and nitrogen loss with a considerable smaller reduction of yield. Fertilizer
is applied only in the main stages of growth which are DC30 to DC49, see (Zadoks
et al., 1974). The solutions derived by other scenarios (J 2, J4) of assessment lead
to optimum fertilizing schemes, which set up a sufﬁcient amount of fertilizer at the
beginning of the vegetation period. Obviously, this increases the amount of nitrogen
loss.
10.4.2
Optimum Pesticide Application Timing
Figure 10.2 shows the results of optimum pesticide application schemes to the per-
formance criterion of Equation (10.1). The parameter of variation is the initial pest
infestation P(0) and the time, denoted by main development stages. All ﬁgures show
the relative distribution of application amounts A∗(t) with respect to the maximum
application amount of a whole vegetation period and the entire spectrum of initial


200
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
0.24-0.3
0.18-0.24
0.12-0.18
0.06-0.12
0-0.06
0
0.1
0.2
0.5
1
2
5
10
20
30
40
50
60
75
100
0.0
0.2
0.4
0.6
0.8
1.0
0
0.2
1
5
20
40
60
100
0.0-0.05
0.05-0.1
0.1-0.15
0.15-0.2
0.2-0.25
0
0.2
1
5
20
40
60
100
0.0
0.2
0.4
0.6
0.8
1.0
P(0)
DC 0-19
DC 20-29
DC 30-49
DC 50-69
DC 70-87
DC 87-
0
0.1
0.2
0.5
1
2
5
10
20
30
40
50
60
75
100
Distribution of pesticide application A*(t)
P(0)
P(0)
DC 0-19
DC 20-29
DC 30-49
DC 50-69
DC 70-87
DC 87-
Distribution of fertilizer application F*(t)
P(0)
Fig. 10.2
Distribution of pesticide and fertilizer application for control of pest population P
in a vegetation period using criterion J3 (“ecologic”) for assessment.
pest infestations. The left ﬁgures show the distribution function as a density plot
and allow an analysis of time dependence. The right ﬁgures show the accumulated
application amount of fertilizer and pesticide as a function of initial pest population
relative to the maximum amount applied.
The distribution of the fertilizer schemes is shown in the lower ﬁgures. For low
initial pest infestation one can identify the results described in the former paragraph.
Above a critical level of investigation the fertilization scheme changes completely. No
fertilizer is applied at the stages after DC20 and the total amount of applied fertilizer
is less than 20% of the normal amount.
The reason for this optimum fertilizing scheme is that fertilization is not decisive for
the outcome of yield. Yield is controlled only by pest control throughout pesticide
application.
Optimum pesticide application schemes appears as follows:
• The pest populationis controlledat the earliest stages with an optimum amount,
slightly above the critical dose to get response in the pest population. The pest
population shows a high growth rate. To achieve a maximum effect in pest
control with a minimum amount of pesticide getting washed into the upper soil
layer, an early application date is important.


LONG-TERM SOLUTIONS: MANAGING CROP ROTATIONS
201
• For moderate pest populations below the critical level two or three application
events can control the pest population. If more application days are neces-
sary, continuous but small applications of pesticide are optimal. This reduces
pesticide runoff into the upper soil layer.
• Above the critical level of initial pest infestation, the pesticide application
is decisive for the yield amount. The amount of applied pesticide reaches a
maximum. For the control of the pest population an application during the
entire vegetation period becomes necessary.
• With a further increase of the initial pest population it becomes impossible
to maintain a sufﬁcient amount of yield. Optimum application amounts are
reduced for a limitation of pesticide runoff.
10.5
LONG-TERM SOLUTIONS: MANAGING CROP ROTATIONS
Fertilization and crop rotation design are the selected variables for the estimation
of long-term strategies. Figure 10.3 shows an example of a complete solution of
the optimum control problem: An optimum crop rotation (based on
J3) with locally
optimum fertilized crops (continuation of J 3). The ﬁgure shows a typical crop rotation
of the farming systems in the investigation site: A sequence of sugar beet and winter
wheat/barley with a period length of two to three years. For detailed analysis the
continuation of the local performance criteria J 1 “economic”, J3 “ecologic” and J4
“N-limitation” are chosen.
10.5.1
Nutrient Balance
An important question in the assessment of the nutrient circulation is, whether the
nutrient balance can be equalized observing a vegetation period or a crop rotation.
The weight ΛN in Equation (10.2) incorporates the amount of nitrogen loss into the
assessment of the crop rotation. One can include or exclude the local assessment of ni-
trogen loss with the choice of the local performance criterion. Table 10.4 summarizes
the results of a seven year crop rotation with all possible scenarios.
Only if the local assessment does not restrict the application of fertilizer (like J 1),
can a global assessment of N(t) reduce the amount of nitrogen loss. If a considerable
reduction of fertilizer is achieved in the vegetation period, the resulting amount of
leaching nitrogen cannot be reduced any more, even if N(t) is used in the global
performance criterion.
10.5.2
Pest Control
An important part of a long-term stable agricultural yield in this investigation site is
the control of the sugar beet cyst nematode H. schachtii. Control of this pest can be


202
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
Table 10.4
Total amount of nitrogen leached after a 7 year crop rotation for long-term
performance criteria. The calculation of the average and standard deviation values was carried
out with respect to different initial populations P1(t0).
J1
J3
J4
ΛN = 0
650 (±40)
190 (±45)
275 (±35)
[kg/ha]
ΛN > 0
450 (±45)
180 (±10)
275 (±32)
[kg/ha]
carried out by designing the optimum crop rotation schemes. In the given example
it is the population of H. schachtii which effects the yield of sugar beet, the most
important, most valuable crop. After planting of sugar beets the planting of a non-
host crop can reduce the population of nematodes in a crop rotation. For this reason,
the optimum crop rotation solution in Figure 10.3 consists of a two to three year crop
rotation of sugar beet, with intermediate planting of wheat. Crops like oil radish or
ﬁeld beans may decrease the population of nematodes more efﬁciently — these crops
are catch crops, which enable H. schachtii to hatch but disable the larvae before they
become fertile, see (Schmidt et al., 1993). On the other hand, these crops do not have
a positive effect on farmers’ income.
A general property of all these solutions of the optimum control problem is displayed
in Figure 10.4. The optimum solution consists of two most rapid approaches to a
local and a global optimum path. The local optimum state of nitrogen content in
soil is a content of 50kg/ha or less is reached within the ﬁrst vegetation period with
its optimum fertilizing scheme. All further fertilizing schemes start and end with
an average nitrogen content of approximately 50 kg/ha. This demonstrates that the
assumption for assessment of Section 10.2 is plausible. The global optimum control
path is reached after three vegetationperiods. This path is characterizedby an interval
of 80 to 200 eggs and juveniles in 100 g soil of H. schachtii. Figure 10.4 shows three
different initial conditions (P1(t0) = 10, 100, 1000 e. + j./100g). Note, the optimal
solution leaves this path, if the assessment stops at the end of the simulation interval.
10.6
DISCUSSION
It is well-known that ecological systems are complex and hierarchical systems. As
a consequence ecological simulation models tend to be complex. Because of this,
the analysis of human impact on ecosystems using simulation models in terms of
scenario analysis is limited.
This chapter has shown that a systematic search throughout the policy space of envi-
ronmental impact can be provided by the application of numerical optimum control
theory to environmental models. The approach links ecological process models with
the human impact in a clear manner, distinguishing between state, control, and as-
sessment variables and models.


DISCUSSION
203
       







	
 


   



 















       







	
 



 


          







	
 



  


  
 



 
            Fig. 10.3
Optimum crop rotation of tend = 13 years with optimum fertilizing schemes (hori-
zontal axis shows t in years). State variables: biomass WC(t) (thick line) Nitrogen content in soil
N(t) (thin line upper plot), and Population of H. schachtii P1(ti). Control variables: fertilizer
F(ti) (center plot) and planted crop (α(ti)) notation in upper plot. Initial values: N0 = 50 kg/ha,
P1(t0) = 500 eggs and juveniles per 100 g soil.
Problemsandperspectivesofthisapproachinecologicalsystemsciencearepresented.
The main difﬁculties of this approach, which give hints to further research needs, are
• to model a performance criterion or indicator, which evaluates all important
disciplinary aspects of environmental processes,
• to ﬁnd an appropriate level of model aggregation, and
• to apply a suitable procedure of numerical optimum control.
The analysis of different performance criteria and the related optimum solution is
comparable to the standard approach of scenario analysis is.
A very interesting
outcome of the case studies is to study and compare different views of optimality by
modiﬁcation of the performance criterion. It allows the comparison of different policy
strategies of farm management. The proposed framework permits the analysis of
differentindicators of environmentalassessment and can answer the question whether
environmental variables are aggregated in a suitable way. Facing this, it may also


204
OPTIMUM AGROECOSYSTEM MANAGEMENT: TEMPORAL PATTERNS
10
100
1000
0



⋆
1
2
3
4
5
6
7
8
9
10
11
12
13
P1(ti)

e.+j.
100g

t [a]
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
×
0
20
40
60
80
100
120
140
160
0
20
40
60
80 100 120 140
N(t)
[kg/ha]
t [d]
⋆



(α∗
i ) depending on P0 in [e.+j./100 g]:
P1(t0) = 10:

α∗
i

= (sub, sub, sub, ww, sub, ww, wb, sub, ww, sub, ww, wb, sub)
P1(t0) = 100:

α∗
i

= (sub, ww, wb, sub, ww, sub, ww, wb, sub, ww, sub, ww, sub)
P1(t0) = 1000:

α∗
i

= (spb, ww, ww, wb, sub, ww, wb, sub, ww, sub, ww, wb, sub)
(F∗
i ) depending on N0 in [kg/ha]:
N0 = 50:

F∗
i

= (27, 67, 30, 6, 2, 1)
N0 = 100:

F∗
i

= (0, 63, 30, 6, 2, 1)
N0 = 150:

F∗
i

= (0, 38, 29, 5, 2, 1)
Fig. 10.4
Quantitative characterization of the most rapid iterated approach to an optimum
path of soil nitrogen content (lower left, ﬁrst vegetation period) and population of nematodes
(upper).


DISCUSSION
205
give an answer to the question of how to incorporate externalities into the process
assessment.
Overall, the choice of a simulation model on an appropriate level of aggregation
is decisive for the success of the approach. A more complex model may be more
realistic. On the other hand, this may lead to problems of computational effort or of
assessing the process in an appropriate way.
The proposed framework for optimum control and the dynamic programming pro-
cedure with a hierarchical structure of different time scales comes out as a general
concept applicable to a large class of environmental models. Mathematically het-
erogeneous systems like ecosystem models can be treated. On the other hand, the
“dilemma of dimensionality” is an intrinsic property of the underlying procedure.
Approaches to this problem with special respect to environmental models are pre-
sented. However, this problem cannot be eliminated completely. Further research
should focus on robust procedures of optimum control of mathematically heteroge-
neous models with fewer prerequisites on the underlying model.


11
Optimum Agroecosystem
Management:
Spatial Patterns
11.1
INTRODUCTION
This chapter extends the results obtained to a spatial dimension. The focus is on the
spatially explicit estimation of optimum fertilizer input and crop rotation schemes as
a dynamic control problem on different time scales. Besides solution of the optimum
control problems, this chapter focuses on the regionalization of the optimum control
problem. The task is solved by the identiﬁcation of homogeneous units in the ob-
served region by a geographic information system. These maps are set up by a vector
database. The second innovative topic, which enables a regionalized solution of the
optimum control problem, is the estimation of families of optimum solutions param-
eterized by spatial properties. Technical problems concern efﬁcient database access,
which is solved within the GIS Arc/INFO, ArcVIEW. The proposed methodology
supports the process of decision support in precision farming, cf. (Seppelt, 2000).
11.1.1
Site-speciﬁc Agroecological Modeling
An estimation of management strategies in agricultural landscapes needs to incorpo-
rate the spatial variability of soil into decision systems. The technology of precision
farming (or, variable rate technology, site-speciﬁc farming) proposes solutions to this
question (Lu et al., 1997). Precision farming can be represented as incorporating
four main areas of management: spatially referenced data collection, data analysis,
decision making, and variable rate treatment (Usery et al., 1995). Technical solu-
tions exist for the steps “data collection” and “variable rate technology” (Lu et al.,
207


208
OPTIMUM AGROECOSYSTEM MANAGEMENT: SPATIAL PATTERNS
1997). A question still under discussion is how to derive management strategies from
observed ﬁeld properties. Strickland et al. (1998) emphasize the enhancement of en-
vironmental stewardship through accurate and precise application of chemicals and
fertilizer to reduce leaching and runoff. However, the step “decision support” is still
under discussion. Lu et al. describe simulation models as a tool to compare different
management scenarios. A methodological concept for the estimation of management
schemes is still under discussion.
11.1.2
Aims, Scope and Region
The aim is to estimate improved farm management strategies on a regional scale. We
focus on the “Neuenkirchen” investigation site, described in Section 2.2.1 on page
40. The case study is performed on a sub-watershed “Ohebach” of the Neuenkirchen
catchment site, see Section 2.3.1. The entire investigation site with its several layers
of information is displayed in Figure 3.9 on page 86. The solution of the problem
will be based only on publicly accessible databases. In the precision farming context,
this means no GPS-based measured yield maps are used for model input. Map data
is derived from the digital soil map (scale 1:5000). The data documents the soil
properties of the watershed with several parameters. The soil can be characterized as
homogeneous with minor small-scale variations. A 1–2 m layer of loess is topped by
colluvial sediments depnding on the slope (Orthic to Gleyic Luvisols), see Section
2.3.1, p. 40 and (McVoy et al., 1995) for details. The average ﬁeld size is 30 ha. The
typical crop rotation in the region consist of several cereals and fallow land with the
main crop being sugar beets.
Figure 11.1 shows the underlying data set and the pedological homogeneous units
with the ﬁeld capacity. The whole area is mainly homogeneous: the average ﬁeld
capacity is 202 mm and the standard deviation is 58 mm. Pedological units with
a ﬁeld capacity below the average, which are the more permeable units, cover an
area of 19 ha which is 20% of the entire observation site. Application of precision
farming approaches to a homogeneous region like this shows the capability of the
developed methodology: aiming at an optimum spatially explicit management it is
an experimentum crucis.
11.2
OPTIMUM CONTROL IN REGIONALIZED MODELS
11.2.1
Agroecological Simulation Model
In analogy to the foregoing chapter, the agroecological model summarized in Section
2.7 is used in optimum control procedures. For detailed analysis of the regionalized
problem, the processes considered are:
• crop growth of different crops (sugar beet, winter wheat, winter barley, spring
barley, oats, ﬁeld beans and oil radish);


OPTIMUM CONTROL IN REGIONALIZED MODELS
209
eff. fcap (mm)
70 - 140
140 - 170
170 - 220
220 - 260
260 - 300
0
200
400
600
800
1000 Meters
N
Fig. 11.1
Database for spatial referenced optimization of crop rotation and fertilizer appli-
cation: map of effective ﬁeld capacity in the root zone of the catchment area “Ohebach”.
• nutrient cycle (mineralization, N2 ﬁxation, N uptake by crop, etc.);
• population dynamics of the sugar beet cyst nematode H. schachtii.
The main processes that are neglected are the environmental fate of xenobiotica as
well as growth of weed. The vector of state variables can be written as: ⃗x(t,⃗z) =
 WC(t,⃗z), N(t,⃗z), P1(t,⃗z)
T. The control variables are fertilizer input F(t) and crop
rotation (α(ti))i=1,2,... with α(ti) ∈{ sugar beet, winter barley, winter wheat, summer
barley, ﬁeld beans, oil radish, fallow }. Note, the vector ⃗z introduces the spatial
dependency of state and control vector. The model is applied to the investigation site
using the method of regionalization, see Deﬁnition 3.2 and the explanations of this
example in Section 3.3.1.
Without loss of generality the initial nitrogen content N0(⃗z) as well as the initial
population of H. schachtii is equal for all locations of the investigation site ⃗z ∈R.
A second simpliﬁcation is that kl, the percolation velocity of solute nitrogen in the
root zone, is the only model parameter that depends on spatial referenced parameters:
c(⃗z) = kl(⃗z). However, this does not affect the generality of the following concept.
Based on these considerations the general model equation can be written as
⃗x(t,⃗z)
=
M∆t
 ⃗x0,⃗u(⃗z),⃗c(⃗z)



WC(t,⃗z)
N(t,⃗z)
P1(t,⃗z)


=
M∆t




WC(t0)
N(t0)
P1(t0)

 ,
 F(t,⃗z)
α(t,⃗z)

, kl(⃗z)


(11.1)


210
OPTIMUM AGROECOSYSTEM MANAGEMENT: SPATIAL PATTERNS
11.2.2
Optimization Task
The performance criterion used for setting up the spatially referenced optimization
problem follows Equation (10.1). The variables C S and A are not considered in
this task. Note the integration over the investigated region R is very important in
calculating a scalar value from the regionalized model.
The general Task 8.2 deﬁned in Chapter 8 on page 169 is speciﬁed as follows for the
problem in hand:
Task 11.1 Calculate an optimum spatially referenced fertilizer scheme F ∗(t,⃗z) and
crop rotation α∗(t,⃗z) so that the model Equation (11.1) is solved and the spatial
performance criterion, Equation (10.1), is maximized for all ⃗z ∈R.
If this task is to be solved by numerical algorithms, the crucial point is the quantiﬁca-
tion “for all⃗z ∈R”. Precision farming approaches state that a grid of 15 to 30 meters
(Sadler et al., 1998) is necessary for the identiﬁcation of soil properties. Consider an
area of 16 km2, like the investigation site “Neuenkirchen”. This would lead to a grid
of at least N1 = |R| = 4500 points. Secondly, a vector data set and the regionalization
using the ecotope concept leads to a set of more than 3000 units, see Figure 3.9.
This is an enormous computational effort, if that grid is used for an estimation of
management strategies by optimum control theory. It must be drastically decreased
by appropriate methodology and intelligent database management.
11.3
CONCEPT OF OPTIMUM SPATIAL CONTROL
One has to remember that dynamic programming can be used to calculate a set
or family of optimum solutions. Developing the concept of hierarchical dynamic
programming(HDP)(seeSection9.2)madeuseofstoringthesesolutionsasafunction
oftheinitialcondition⃗u∗[⃗x0]. Thebasicideaforaregionaloptimizationwhichfollows
from this, is to estimate a set or a family of optimum control solutions depending on
initial conditions and different spatial parameters ⃗u∗[⃗x0,⃗z]. The important steps to
make the concept of HDP available for a regionalized model, are:
• to associate the model parameters ⃗c to a map that speciﬁes the regionalization
of the model: the ecotope map S hom, and
• to associate the control variable ⃗u to a map that deﬁnes the spatial scale on
which the system can be managed. Let us denote this map by S field, assuming
that we want to estimate optimum spatially localized agricultural management
on the ﬁeld scale.
However S hom is set up by different layers of spatial information, for example maps
with different soil parameters, S soil. These parameters may be used for a parameter-
ization of the family of optimum control solutions derived by DP/HDP.


CONCEPT OF OPTIMUM SPATIAL CONTROL
211
Spatial dependency for simulation and optimization
Input data
s ∈S soil, |S soil| = 61
control variables: F(s, t)
model parameter: kl(s)
42
5
41
53
35
52
54
28
7
61
10
29
30
23
15
57
9
49
8
26
27
22
62
46
40
50
13
18
16
60
56
34
f ∈S field, |S field| = 85
control variables: α( f, t)
278
275
253
245
283
244
273
287
147
243
242
284
572
254
279
246
286
282
292
207
277
134
97
135
208
139
210
206
548
Intersection including split polygon removal
Data base for optimization
e ∈S hom, |S hom| = 220
control variables: F(e), α( f )
model parameter: kl(e)
initial values: W(e), N(e)
Fig. 11.2
DatabaseconceptinGIS:theunderlyingdata setsconsistof geometricinformation,
a decomposition of the region by irregular polygons (left column) and the associated attribute
tables for soil properties and ﬁeld identiﬁers (mid column). Dependencies on the simulation
model and the optimum control problems are noted in the right column. Associations between
units of the input maps are derived from the intersection map, shown in the bottom row.
Using vector based maps each map S is a tessellation of s ∈S polygons, see Sec-
tion 3.3.1. One or more attributes gi are associated to each polygon s ∈S . The
spatial dependence can be denoted by gi(s) as s ∈S denotes a homogeneous area
with respect to g. Two maps are used here for a solution of Task 11.1:
• The digital soil map (1:5000) S soil with the attribute “ﬁeld capacity” g1(s) in
[mm] and “rootingdepth” g2(s) [cm] (s ∈S soil). The model parameterleaching
rate c(s) = kL(s) is set up by these soil-properties.
• The land use map S field with the ﬁeld borders. Each ﬁeld s ∈S field is identiﬁed
by a unique number g3(s) ∈, s ∈S field.
Based on this data structure one can access the soil map, the ﬁeld map and the ecotope
map by unique identiﬁers stored in the GIS atabase. Figure 11.2 shows this technique:


212
OPTIMUM AGROECOSYSTEM MANAGEMENT: SPATIAL PATTERNS
Input data consists of the geometric information and the associated database with soil
properties and ﬁeld identiﬁers. The right column summarizes which model variables
depend on this spatial information. Simulation and optimization is based on the
intersected maps shown in the last row. In the observed region the intersection map
consists of N2 = |S hom| = 315 homogeneous units. For each of these units a simulation
is performed and all results are aggregated and visualized by the GIS. Note that the
database table of the ecotope-map includes all identiﬁers for the access of the soil,
ﬁeld and ecotope map, as well as the modeling results, see Figure 11.2 middle of last
row.
The calculation of intersection polygons leads to geometric units called silver poly-
gons (Breunig, 1996) with an area less than 100 m 2 in this case, but with large length
or extent. For instance, silver polygons appear along linear strictures like pathways
or ditches. These shapes appear, for instance if two polygons show an approximately
parallel but not identical border. These polygonsare deleted or joined to larger shapes
manually after visual control. This reduces the element of S hom from N2 = 315 to
N2 = 220.
Technical aspects of the model integration are summarized as follows: Data pre-
processing is performed using GIS Arc/INFO. Model integration and optimization is
done using ArcVIEW Desktop GIS.
• Based on the maps generated within Arc/INFO, a list of identiﬁers is derived
from which the associations between S i (i = 1, 2, . . .) can be retrieved.
• For each simulation/optimizationrun, a master script ﬁle generatesan appropri-
ate parameter ﬁle for the model using the parameters derived from the database
by their identiﬁers and a prototype parameter ﬁle. The step depends on the
considered regionalization solution, see next section.
• The optimization procedure of iterated dynamic programmingchecks, whether
it is necessary to start an optimization process, or if a previously calculated or
optimum control function can be used. This is done by comparing the pedotope
identiﬁer with all previously calculated solutions.
• Simulation results ﬁles are rearranged and provided with the necessary identi-
ﬁers for visualization in GIS.
A regionalization is performed based on this data set of optimum solutions and the
identiﬁer given in the ecotope map S hom. Efﬁciency increases with an increase of ac-
cess to pre-calculatedresults with equal pedologicalproperties, e.g. equal g 1(s), g2(s).
The basic innovation of this approach is a careful separation between spatial area
with distinct properties. A simulation and optimization is only performed for regions
with new or distinct properties. This distinguishes this solution from all grid-based
modeling approaches.


OPTIMIZATION AND SIMULATION EXPERIMENTS
213
11.4
OPTIMIZATION AND SIMULATION EXPERIMENTS
11.4.1
Types of Spatial Solutions
The results of the study are understood in terms of a simulation experiment. The
experiment is separated into three steps of regionalization
1. Regional scale: Assumption of a homogeneous region.
2. Field scale: Calculation of optimum management strategies for each ﬁeld,
using the properties of the pedological unit, that covers the largest part of the
ﬁeld.
3. Below ﬁeld scale: Calculating an optimum crop rotation for a ﬁeld together
with optimum fertilizing strategy for each pedological unit.
The ﬁrst step in the simulation experiment is taken as a reference solution. This pure
simulation run uses coarse information. All optimization results in the following
steps should improve yield, diminish nitrogen loss or decrease fertilizer input. The
last step, can be understood as precision farming simulation experiment. It should
improve ecological conditions of the observed area.
Solution 11.1 (Regional Reference Solution) Let p ∈S soil denote that pedological
unit, which covers the largest area of the observation site R. A solution of Task 11.1
is derived as follows:
1. Optimization: Calculate ⃗u∗so that
⃗x(t)
=
Mt
 ⃗x0,⃗u∗,⃗c(p)

J[⃗x,⃗u∗]
≥
J[⃗x,⃗u]
for all t ∈[0, T],⃗u ∈U
(11.2)
2. and perform a regional simulation using ⃗x(e, t) = Mt
 ⃗x0,⃗u∗,⃗c(e)

for all e ∈
S hom.
Step 1 has to be run once, and step 2 N2 = 220 times. The results of this op-
timization solution fall into line with the results in discussed in Section 10.5 and
the observed management of the region (McVoy et al., 1995). The crop rotation
α(ti) = (sugar beet, wheat, barley, sugar beet, wheat, barley, sugar beet) is calcu-
lated with a total fertilizer amountof 1503kg/ha. As nitrogendynamics are calculated
for each pedological unit, the amount nitrogen loss vary from 459 kg/ha to 650 kg/ha
with an average of 477 kg/ha.
Solution 11.2 (Optimum Plot Management) A solution of Task 11.1 is estimated
for each ﬁeld f ∈S field.


214
OPTIMUM AGROECOSYSTEM MANAGEMENT: SPATIAL PATTERNS
1. Let p f ∈S hom identify that pedological unit, which covers the large area of the
ﬁeld f
max
e∈S hom,e⊆f area(e) = area(p f).
Calculate ⃗u∗(p) so that
⃗x(p f, t)
=
Mt
 ⃗x0,⃗u∗(p f),⃗c(p f)

J[⃗x(p f),⃗u∗(p f)]
≥
J[⃗x(p f),⃗u(p f)]
for all t ∈[0, T],⃗u(p f) ∈U
(11.3)
2. The regional simulation is performed for each ecotope e ∈S hom using
⃗x(t, e) = Mt
 ⃗x0,⃗u∗(p f),⃗c(e)

with e ⊆f.
Step 1 has to be run N3 = |S soil| = 52 times, and step 2 N2 = 220 times. In comparison
to the ﬁrst “reference” solution,the total amount of applied fertilizer slightlydecreases
to 1464kg/ha and nitrogen loss increases to 485kg/ha. The average assessment of
all estimated optimum management strategies is improved by 4%.
A spatial application of optimum control theory to the smallest homogeneous area,
as requested in the introducing section, needs a more precise deﬁnition of spatial
dependency with the control variables: fertilization depends on pedological units,
crop rotation scheme depends on the ﬁeld.
Solution 11.3 (Precision Farming) Calculate ⃗u∗(e, f), so that
⃗x(e, t)
=
Mt
 ⃗x0,⃗u∗(e, f),⃗c(e)

J[⃗x(e),⃗u∗(e, f)]
≥
J[⃗x(e),⃗u(e, f)]
with t ∈[0, T],⃗u(e, f) ∈U (11.4)
for all e ∈S hom and all f ∈S field, with the speciﬁcation
⃗u(e, f) =

F(e)
α(f)

⃗u depends with the ﬁrst element on each ecotope. For a given f it is u 2(f) = α(e) =
constant for all e ⊆f that intersect the ﬁeld f.
For detailed analysis, the underlying algorithm of this solution is summarized in
Figure 11.3. The main loop estimates solutions for all ﬁelds f i ∈S field in the following
way. All homogeneous units of the ﬁeld fi are collected in a list S ′ and sorted with
the largest (area) ecotope ﬁrst. The ﬁrst step of optimization determines the optimum
fertilizer scheme and an optimum crop rotation. Soil-dependent optimum fertilizer
schemes using this crop rotation are estimated in all other steps. Every time a new
optimum control solution is requested, the database be questionedfor a pre-calculated
solution to equal soil properties.
The calculation effort of this solution is estimated as follows: optimization procedures
are started for each p ∈S soil. The effort of calculating optimum fertilizing schemes


OPTIMIZATION AND SIMULATION EXPERIMENTS
215
Regionalized HDP — Regionalized Hierarchical Optimum Control
Repeat for each ﬁeld fi ∈S field
Perform within ArcVIEW environment
Set up S ′ = {e ∈S hom|e ⊂fi}
Sort S ′ with respect to area size of ei (e1 has maximum area in S ′)
Perform within the HDP framework
    yes
Exists a previously calculated solution to a pedological unit
p′ ∈S soil of the Task 11.1?




no
Derive the solution of Task 11.1 from the
calculated family of solutions, using
p1 ⊂p′: ⃗u∗
 ⃗x0(p′), p′

Calculate the optimum solution, by
hierarchical dynamic programming.
Result: Family of solutions ⃗u∗
 ⃗x0(p′), p′

.
Repeat for j = 2, . . . , |S ′|
Perfom within HDP framework
    yes
Exists a previously calculated solution to a pedological unit
p′ ∈S soil of the Task 11.1?




no
Calculate the optimum solution, by hierarchical dynamic
programming.
Result: Family of solutions ⃗u∗
 ⃗x0(p′), p′

.
Derive the solution to Task 11.1 from the calculated family of solutions. Use α∗
from the solution to e1
Result: F∗
 ⃗x0(p′), p′

Fig. 11.3
Flowchart of calculation procedure for regionalized optimum control Solution
11.3. The entire algorithm is implemented in script ﬁles started from the GIS ArcVIEW.
The headline printed in italic denotes the environment the following steps are derived from;
hierarchical dynamic programming, or GIS ArcVIEW.


216
OPTIMUM AGROECOSYSTEM MANAGEMENT: SPATIAL PATTERNS
177
177
178
177
177
178
183
N
60
0
60
120 Meter
Investigation site "Ohebach"
Field 278
Area =  93 ha
eff.  fcap.= 127 to 268 mm
Improvement in optimization 
criterion value J (%)
0
0-7.5
7.5-10
10-
fertilizer scheme F(t) (kg/ha)
U(t)
labels specify the total 
amount of fertilizer (kg/ha)
Fig. 11.4
Zoom into “Field 278” of investigation site “Ohebach”. The 93 ha ﬁeld is set up
by 7 pedological units. The total amount of fertilizer applied is labeled.
for each e ∈S hom is equal to the estimation of simulation results. Therefore the effort
of this solution is equal to that of Solution 11.2. Results from this solution improve
the performance criterion results by 1% compared to Solution 11.2. The total amount
of fertilizer applied (1464kg/ha) and nitrogen loss (490kg/ha) does not differ very
much from the previous results.
11.4.2
Results
The results obtained cannot be discussed using average values of the whole area.
The calculation of averages or total amounts neglects any spatial variability. There-
fore, more precise analysis of the achieved results needs inspection of the spatial
distribution of fertilization, nitrogen loss, and crop rotation design.
For an analysis of nitrogen applications we focus on a single vegetation period of one
crop (winter wheat) on a given ﬁeld. Figure 11.4 shows the intensive investigation
“Field 278” of the “Ohebach” region. The ﬁeld consists of seven homogeneous
pedological units with an effective ﬁeld capacity of 127 up to 268mm.
The grey shading shows that management can be improved by precision farming
(Solution 11.3) up to 10% in comparison to the Solution 11.2. This is performed by
an optimum allocation of fertilizer to the stages of crop development, qualitatively
displayed with the bar charts.
In Figure 11.5 nitrogen loss is mapped for the whole area as a result from Solution
11.2 (right) and Solution 11.2 (left). Pedological units with low nitrogen retention


DISCUSSION
217
nitrogen loss (kg/ha)
150 - 210
210 - 270
270 - 310
310 - 420
420 - 650
0
200
400
600
800 1000 Meters
609 kg/ha
265 kg/ha
Fig. 11.5
Amounts of nitrogen loss in Solution 11.3 (left) and Solution 11.2 (right) in a
7-year crop rotation. High amounts of nitrogen loss can be found (see arrows), if local areas
with low ﬁeld capacity are fertilized equal to the neighboring areas.
potential are identiﬁed and optimum fertilizer application schemes are adapted. For
instance, nitrogen loss can be decreased from 609kg/ha to 265 kg/ha at a pedological
unit: the “hot spot” of “Field 278” shown in Figure 11.4.
Figure 11.6 completes these results. The whole observation region “Ohebach” is
shown, with the results of year three to seven of the optimum crop rotation from the
precision farming Solution 11.3. The upper part of the ﬁgure shows the population
density of H. schachtii and the lower part shows the planted crop. Note that different
optimum crop rotations are estimated for minimization of nitrogen loss and pest
control. Exemplary two crop rotations are noted for ﬁelds A and B below the maps.
Fallow crops are used as catch crops for H. schachtii, see (Schmidt et al., 1993).
Moreover, less nutrient demanding crops are planted in the more permeable regions
of the investigation site (north-western part).
11.5
DISCUSSION
Precision farming aims at incorporatinglocal spatial variability into agricultural man-
agement. The application of optimum control theory connects spatial properties with
agroecological simulation models and questions of management assessment. The
results can only be discussed properly with their spatial attributes. Regional aver-


218
OPTIMUM AGROECOSTEM MANAGEMENT: SPATIAL PATTERNS
Fig. 11.6
Regional optimum crop rotation in investigation site “Ohebach”. Optimum crop
rotation including precision farming solution of optimum fertilizer input. For detailed study,
two crop rotation solutions are noted below the maps.
ages show no improvement by precision farming (Solution 11.3) in comparison to
the reference Solution 11.1.
The most interesting results in the context of precision farming are that the fertilizer
scheme is not the only factorthat shouldbe estimated and applied foreach pedological
unit. There is also a spatial dependencein the allocation of the optimum crop rotation.


DISCUSSION
219
The proposed methodological framework offers a theoretical base for the application
of optimum control for spatial problems in agroecological modeling. GIS comes out
as a framework, which enables agroecological simulation models to be coupled with
spatial databases. GIS-functions and robust optimization procedures decrease the
numerical effort, so that there are no differences between the calculation effort of the
standard optimization Solution 11.2 and the precision farming Solution 11.3.
Overall, the case study shows that agroecological process models with regionalized
parameter ﬁelds integrated in numerical optimum control procedures may support the
decision process in precision farming systems.
The proposed methodology can be used for further development, which may focus
on
• the integrationof more detailed agroecologicalprocess models, includingmod-
els for solute transport in soil, with speciﬁcations from pedo transfer functions,
which uses more attributes from soil and yield maps.
• the stepwise integration of information. This means, starting from the past (and
known) climatic parameters and conditions and the current state of ﬁelds we can
estimate the optimummanagementstrategyfor the rest of the vegetationperiod.
A typical problemto be solved within the frameworkof dynamicprogramming,
as these solutions do not need any further numerical effort.


12
Changing Landscapes:
Optimum Landscape
Patterns
12.1
INTRODUCTION
Spatially explicit ecosystem models allow water and matter dynamics in a landscape
to be calculated as functions of spatial localization of habitat structures and matter
input, see Section 3.3.3. The operation of several ecosystem services as a function
of different management schemes for a mainly agricultural region is studied in this
chapter. Optimization tasks are formulated for this purpose.
Section 3.3.3 gave a short summary of the investigation area. Figure 3.14 (p. 92)
presented a map of the region. The focus is on the Hunting Creek Watershed which
is located entirely within Calvert County in Maryland, USA. The 78 km 2 study area
belongs to the drainage basin of the Patuxent river (2356 km 2) which is one of the
major tributaries of Chesapeake Bay. Main land uses of the watershed are forest and
agricultural habitats. Rapid population growth, development and change in land use
and land cover have become obvious features of the landscape.
The application of the spatially explicit model follows a hierarchical concept. Most
of the investigations are made for the Hunting Creek watershed model 200 m grid,
the focal level. A smaller sub-watershed is chosen to test certain functions of the
framework developed, cf. Section 9.3. Finally the results are transferred to the Patux-
ent landscape model with a 1 km grid and compared on different spatial scales, see
Figure 12.1.
The task is to calculate optimum land use maps and fertilizer application maps. The
framework for optimization of spatially explicit models discussed in Section 9.3.6 is
used for numerical optimization using this generic landscape model. The results are
221


222
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
38°35'
38°35'
76°40'
76°40'
76°35'
76°35'
360000
360000
4270000
4270000
Dover
Chester
Trenton
Norfolk
Baltimore
Annapolis
Harrisburg
Philadelphia
D.C.
A t l a
n t i c
O c e
a n
C
h
e
s a p
e
a k
B
a
y
-77
-77
-76
-76
-75
-75
37
37
38
38
39
39
40
40
38°19'59"
38°19'59"
38°39'58"
38°39'58"
38°59'57"
38°59'57"
39°19'56"
39°19'56"
77°00'03"
77°00'03"
76°40'04"
76°40'04"
76°20'05"
350000
350000
4250000
4250000
4300000
4300000
4350000
4350000
Location of Patuxent Watershed
Patuxent Watershed and 
Hunting Creek Study Area
Open Water
Land
Urban and Residential Areas
Rivers & Creeks
Patuxent Watershed
UTM 1983
Zone 18
Water & Wetland
Forest
Resident
Urban
Agriculture
Study Area Hunting Creek (1km grid)
Study Area Sub-Watershed (200m grid)
Land Use 1990 (right maps)
Study Areas
2356km²
77,8km²
20,5km²
General
Legend
Hunting Creek and Subwatershed
Fig. 12.1
Location of Patuxent river within the catchment of the Chesapeake Bay region and
the hierarchical structure of the three study areas.
tested within the tool set using Monte Carlo simulation, which is based on different
stochastic generators for the independent control variables. Gradient free optimiza-
tion procedures (Genetic Algorithms) are used to verify the simplifying assumptions.
The results are studied with respect to varying climatic conditions. Additionally,
spatially explicit comparisons of the resulting spatial patterns are performed and the


PERFORMANCE CRITERIA FOR LANDSCAPE OPTIMIZATION
223
results are compared with recent land use in the investigation area, cf. (Seppelt &
Voinov, 2002).
12.2
PERFORMANCE CRITERIA FOR SPATIALLY EXPLICIT
LANDSCAPE OPTIMIZATION
12.2.1
Economic–Ecologic Assessment
The observed region is denoted by a set of discrete grid points⃗z ∈R. Seven different
land use types are considered: soybeans, winter wheat, corn, fallow, forest, cities and
rural areas. c(⃗z) denotes the land use (or habitat type) in cell⃗z. Controllable cells are
L = {soybeans, winter wheat, corn, fallow, forest}. Rc = {⃗z ∈R | c(⃗z) ∈L} denotes
the grid points with controllable cells c(⃗z) ∈L.
Without loss of generality focus is on the estimation of the total required amount of
fertilizer, similar to the problems discussed in Chapter 10. In this case we need to
set up a spatially explicit performance criterion. Our goal is to ﬁnd out what is the
optimum land use pattern and what should be the spatially explicit strategy of fertilizer
application to reduce nutrient outﬂow from the watershed and increase yield? For a
deﬁnition of a performance criterion one has to take into account crop yield, fertilizer
application and nutrient outﬂow.
• The ﬁrst variable of the economic part of the performance criterionis the harvest
biomass H(c,⃗z) in [kg/m2] is the yield of crop c (if any) harvested from cell ⃗z.
• The second economic variable F(⃗z, t) in [kg/m 2] is related to the cost of agri-
cultural production and considers the amount of fertilizers applied at cell ⃗z for
the habitat type c(⃗z) at time t. As time of fertilization is a crucial parameter
for reduction of nitrogen leached, we use results of optimum fertilizer timing
derived from the optimum control solution in Section 10.4. These are in accor-
dance with the best management practice recommendations for the temporal
allocation of the total fertilizer amount of the investigation sites.
• Ecological aspects are taken into account by the variable nutrient outﬂow out
of a grid cell with horizontal ﬂows of surface and subsurface water: N(⃗z) in
[kg/m2]. This can be interpreted as overconsumptionof retention capability of
the ecosystem, an eutrophication.
The ﬁrst two factors are easier to compare if we operate in terms of prices. The
economic yield Y(⃗z) of an agricultural site⃗z— farmers’ income — can be calculatedas
the difference of market price for the harvested biomass of crop minus the production
costs given by the cost of fertilizers applied. The revenue from the yield over the
whole study area is
A =
R
pH(c)H(c,⃗z) d⃗z
(12.1)


224
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
where pH(c) is the current market price of crop c. The price of fertilizers applied is
then
B = pF
R
tend
0
F(⃗z, t) dt d⃗z,
(12.2)
where pF is the unit price of nitrogen fertilizer. Obviously A is to be maximized while
B is to be minimized, which means that Y = A −B is to be maximized. Y denotes the
economic part of the goal function.
There are different ways of modeling the ecological part of the performance criterion.
One possibility is to take into account the total amount of nutrients generated by all
the cells in the study area,
C =
R
tend
0
N ⃗z, t
dt d⃗z
(12.3)
This is the distributed nutrient leaching. More realistic, and comparable to measure-
ments of gaugingstations, is to consider the amount of nitrogenin the outlet cell of the
watershed ⃗z0. This case takes into account the compensation mechanisms of uptake
along the pathways of nitrogen while it travels across the watershed and estimates the
actual water quality in the river estuary:
C =
tend
0
N(⃗z0, t) dt
(12.4)
In both cases C is to be minimized. The crucial problem is to integrate the ecological
part C and the economic part Y to a scalar goal function. For this purpose C is to be
expressed in units that can be compared with the monetary measure that we derived
in Y. Without going into any further details at this point, let us simply assume a
weighting coefﬁcient λ, and formulate the goal function as
J = Y −λC
(12.5)
The optimization task is:
Task 12.1 Based on the spatially explicit landscape model described in Section 3.3.3
identify maps of optimum land use c∗and the related optimum fertilizer application
amounts F∗which maximize J →max according to Equation (12.5).
This task is an example for a global optimization problem in spatially explicit models
(Task 12.1) as introduced in Section 9.3. Numerical solution of this task requires a
enormous computational effort.


PERFORMANCE CRITERIA FOR LANDSCAPE OPTIMIZATION
225
12.2.2
Localization of Optimization Problem
A second approach is to derive a local performance criterion in each grid cell that
allows a local optimization problem to be formulated as deﬁned by Task 9.2. Let us
analyze how the performance criterion from Equation (12.5) may be reformulated in
this context: The goal function is deﬁned for every grid cell⃗z, as a function of⃗z. The
economic yield Y can simply be assessed on a grid scale level by
Y(⃗z) = pH(c)H(c,⃗z) −pF
tend
0
F(⃗z, t) dt
(12.6)
The amount of nitrogen leaving the watershed can be approximated by estimating the
net amount of nitrogen loss from every grid cell.
C(⃗z) =
tend
0
N(⃗z, t) dt
(12.7)
This is the amount of nitrogen leaching produced locally and that can possibly be
transported to the watershed mouth. Y(⃗z) and C(⃗z) are now calculated for a speciﬁc
cell. They do not incorporate integration over the entire study area. Based on this the
local goal function for every cell is then:
J(⃗z) = Y(⃗z) −λNC(⃗z)
(12.8)
The optimizationproblem is now reduced to the optimizationof land use and fertilizer
application for every grid cell. This approach neglects any neighborhood effects and
can be written in terms ofa localoptimizationtask. The general localized performance
criterion in Equation (9.8) in Section 9.3.2 (p. 184) can be applied by setting
A1(⃗z)
=
Y(⃗z)
A2(⃗z)
=
λNC(⃗z)
(12.9)
Task 12.2 Based on the spatially explicit landscape model described in Section 3.3.3
estimate c∗(⃗z) ∈L and F∗(⃗z) for each cell ⃗z ∈Rc, which maximize: J ⃗z →max ac-
cording to Equation (12.8) using the deﬁnition in Equation (12.9) and Equation (9.8).
We have to study the relationship of the global and the local solutions of the optimum
control problem. Task 12.2 formulates a worst case scenario. Considering the nutrient
outﬂow the goal function from Task 12.1 takes into account the capability of the
retention function of an ecosystem, which models the through ﬂow of nutrients more
precisely. The goal function of Task 12.2 on the other hand performs a worst case
upper estimate of the net nutrient outﬂow. In this contribution we will study the
methodological framework in more theoretical detail. Finally we should be aware of
getting multiple solutions to the problem.


226
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
12.2.3
Multi-criteria Assessment of Ecosystem Functions
For a more general analysis, more environmental factors are taken into account. The
following ecosystem functions can be quantiﬁed by state variables, or derived from
a set of state variables assumed in the ecosystem model:
• Basic ecosystem productivity given by the total rate of net primary produc-
tion NPP(⃗z) [kg/m2]. This also indirectly represents the retention capability
of nutrients (nitrogen) and the uptake of greenhouse gas CO 2, and has been
identiﬁed as an important indicator of overall ecosystem services provided by
a land use type (Costanza et al., 1997).
• Nutrient outﬂow out of a grid cell with horizontal ﬂows of surface and sub-
surface water: N(⃗z) [kg/m2]. This can be interpreted as overconsumption of
retention capability of the ecosystem, eutrophication, see above.
• The amount of surface water baseﬂow in the streams: Q B(⃗z) [m3/d] calculated
as the total of the 50% of the minimal daily ﬂow values. This identiﬁes how
land use change affects the hydrologic conditions in the area. In most cases
lower baseﬂow is associated with increased vulnerability to drought and peak
ﬂooding, which makes it an important characteristic of the landscape and the
health of associated ecosystems.
For these ecosystem functions the simulation model dynamically calculates the re-
quired state variables. We may further expand the number of functions that are taken
into account in the performance criterion. For example, it would make perfect sense
to include the value of land used for recreation or for housing, in which case agricul-
tural or forested habitat will become residential. However, methodologically it will
be the same and we do not want to make the calculations any more complex at this
time.
A performance criterion aggregates state variables, which represent the considered
ecosystem functions. For optimization purposes we need to deﬁne the performance
criterion, which aggregates the three ecological variables listed above and the eco-
nomic variables into a scalar function. However these variables are not compatible in
terms of units. To match the units among the different elements in the performance
criterion, we introduce a vector of weighting factors ⃗λ. N has to be minimized, while
all other variables are to be maximized. This leads to the following performance
criterion:
J(⃗z)
=
Y(⃗z) + λQBQB(⃗z) + λNPPNPP(⃗z) −λNN(⃗z)
=
Y(⃗z) + λQB, λNPP, −λN ·
QB(⃗z)
NPP(⃗z)
N(⃗z)
= Y(⃗z) + ⃗λT · ⃗x(⃗z)
(12.10)
Compared to the performance criterion in Equation (12.8) we now have a vector
of weights ⃗λ =
λN, λQB, λNPP
T. The speciﬁcation of J is a multi-dimensional


PERFORMANCE CRITERIA FOR LANDSCAPE OPTIMIZATION
227
problem. Our other problem is that the performance criterion is formulated in terms
of global landscape conditions: we are concerned with the water quality and quantity
at the outlet of the drainage area, we are considering the total NPP of the area and
the total proﬁts from the agricultural crops. However, to apply the localized spatial
optimization algorithm, we need to formulate these goals in term of local variables
that can be traced for each individual cell. As we will see below this may not be
always possible.
The local performance criterion is quite identical to the global one for the economic
part and for NPP. Both these variables are additive, therefore if we maximize NPP
or agricultural proﬁts for each individual cell, we will be also maximizing the total
proﬁt and total NPP from the watershed. Accounting for water quality and quantity
is not that straightforward, since these variables are not additive and undergo much
change and transformation on their way between the localized (individual cell) and
the drainage point of the watershed. Yet, for now we will assume that the water
quality can be described globally by the water quality in each cell and, similarly, that
the baseﬂow at the drainage point (calculated as the total of the 50% of the minimal
daily ﬂows) is related to the total of the less-than-averagesurface water stages in cells.
In the following we will analyze how the optimization results are inﬂuenced bythe dif-
ferent weighting of the ecosystem functions in the performance criterion. Essentially
the weights in this formulation are the dollar values that we assign to the different
ecosystem functions.
12.2.4
Numerical Effort
A simulation period of 551 days is considered. It covers the growth periods of all
crops, starting with soybeans and ending with the harvest of winter wheat. Before
planting and after harvesting a crop, fallow is assumed to be the land use type of the
cell. 20 minutes processor time is required for one simulation run of the entire model
on a Sparc Ultra 10 Workstation. It is evident that a simple search through the entire
control space of Task 12.1 is not practicable.
Tasks 12.1 and 12.2 can be classiﬁed as a combinatorial optimization problem. Refer-
ring to Section 9.3.1 a precise estimation of the computation effort can be given. We
are to sort through all the possible combinations of six available land use types over
the study area. Assuming a homogeneous land use and discrete stages of possible
total fertilizer input, for say six stages F ∈{0, 25, 50, 75, 100, 150 kg/ha}, Task 12.2
leads to I2 < |F| |L| = 36 combinations. Considering that no fertilization takes place
for c ∈{forest, fallow} we get I2 = 26 combinations.
The number of possible combinations for Task 12.1 depends on the size of the study
area I1 = |F||L| |Rc|. For example, for the Hunting Creek watershed, which is repre-
sented by |Rc| = 1681 controllable cells of 200 m2, there are I1 = 3.2 · 1064 different
land use patterns. For a smaller sub-watershed that covers 25% of the total area and
|Rc| = 483 controllable cells there are still I1 = 4.7 · 1053 possible land use patterns.


228
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
12.3
VALIDATION OF CONCEPT: RESULTS FOR HUNTING CREEK
WATERSHED
12.3.1
Local Optimization
We focus on the methodological aspects of the proposed framework ﬁrst using the
performance criterion in Equation (12.8) to maximize farmers’ income against nitro-
gen loss of the watershed. The results in terms of landscape ecological issues will
be brieﬂy described in the following section. The solution of Task 12.1 performs
a grid search through the entire control space assuming homogeneous land use and
identical fertilizer amounts for each cell. A series of maps for different combina-
tions of crops and fertilizer application rates are generated and stored. Maximizing
J(⃗z) for every grid cell, depending on the pre-calculated maps of the goal functions
Y(⃗z) and C(⃗z), solves the optimization problem. The result is a pair of land use and
fertilizer maps that optimize the local performance criterion. This pair is then fed
into a spatial simulation that is used to calculate the global performance criterion,
cf. Equation (12.5).
We start the analysis of the results with Branch 1 in the ﬂow chart of Figure 9.3.
Homogeneous control variables for each possible land use type and a certain fertilizer
amount are set up: c(⃗z) = c0 ∈L, F(⃗z) = F0 for all ⃗z ∈Rc. Running simulations
within SME for all possible combinations in the step ”grid search”, we derive maps
Y(⃗z) and C(⃗z) which are used to estimate the local optimum solution.
The estimation of local optimum land use maps does not require any computational
effort. It sorts through all possible combinations in the maps Y(⃗z),C(⃗z). This easily
allows parameter studies for the weighting parameter λ N. Figure 12.2 shows the
results of a parameter study for the Hunting Creek watershed in an aggregated way:
the number of different land use types is plotted as a function of λ N. Figure 12.3
shows 3 maps of optimum land use derived from this parameter study: optimum land
use patterns are displayed for the λN values 0.0 (upper left), 0.1 (upper right), and 5.0
(lower left).
• A zero value of λN leads to a pathologic solution: the optimum solution is to
plant the most valuable crop in the entire study area. Only villages, urban area
and open water remains the same (non-controllable cells).
• An increase of λN introduces forest into the land use pattern. The more nutrient
outﬂow is “punished” by an increase of λ , the higher is the fraction of forest
in the study area.
• With an increase of λN agricultural cells change to crops with a better nutrient
up-take/yield-efﬁciency. This depends on the market prices of the crop.


VALIDATION OF CONCEPT: RESULTS FOR HUNTING CREEK WATERSHED
229
0
500
1000
1500
0.01
0.1
1
10
100
λN
corn
soyb.
wheat
fallow
forest
0
5
10
15
20
0.01
0.1
1
10
100
λN
F(⃗z) d⃗z [kg/ha]
Fig. 12.2
Results of parameter study of optimum land use maps. The number of forest,
fallow, soybean, corn and wheat cells in the Hunting Creek watershed are plotted against λN.
12.3.2
Monte Carlo Simulations
An analysis of these results can be performed by a Monte Carlo simulation. Figure
9.3 shows Monte Carlo simulations in two boxes in the mid column:
• Monte Carlo simulation “from scratch” correspond to the ﬁrst box of Branch 2,
compare ﬁrst item in section above. It performs an analysis of the variability of
the entire process and sets up an initial population for the genetic programming
algorithm.
• The step after local optimization, which corresponds to the reallocation p 1 = 1
or the disturbance of an optimum solution p 1 < 1, item 2 and 3 of previous
section.
For the given problem of land use and fertilization optimization, the algorithm can
be described mathematically by a two-stage stochastic process. Let Z 1(⃗z) ∈[0, 1]
be a random variable. A new land use is generated randomly if Z 1(z) < p1 for cell


230
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
Water & Wetland
Forest
Resident
Urban
Corn
Wheat
Soybean
Fallow
0 1 2 3 4 km
0
)
a
=
N
λ
1.0
)
b
=
N
λ
15
.0
)c
=
N
λ
5.0
)
d
=
N
λ
0.5
)e
=
N
λ
Fig. 12.3
Optimum land use maps derived for optimization using the weighting λN = 0 (a),
λN = 0.1 (b), λN = 0.13 (c), λN = 0.5 (d), and λN = 5.0 (e). Lower areas near rivers and creeks
can be identiﬁed by the contour lines.
⃗z. This is done by a stochastic variable Z2 ∈{corn, soybeans, wheat, fallow, forest}
such that P Z2(⃗z) = c(⃗z) | Z1(⃗z) < p1 = f(c).
For every cell ⃗z the stochastically generated land use c follows a distribution which
is deﬁned by a density function f(c). The density function f(c) is constant for the
entire region and may be generated by a stochastic process, started before generating
the stochastic land use map. Otherwise it may be derived from the distribution of a
known land use pattern, for instance the optimum solution, cmp. Section 9.3.4.


VALIDATION OF CONCEPT: RESULTS FOR HUNTING CREEK WATERSHED
231
0.95
0.97
0.99
1.1 1.02
J
10
20
30
40
50
x= 0.97
2
0.00013
1.0
1 =
p
01
.0
1 =
p
0.1
opt
local
from
)
(
1 =
p
c
f
0.1
)
(
stochastic
1 =
p
c
f
0.995
1.
1.005
1.01
J
5
10
15
20
x
0.99
2
0.000016
8.45 8.5 8.55 8.6 8.65 8.7
H
5
10
15
20
25
x
8.56
2
0.0021
8.1
8.2
8.3
8.4
8.5
8.6
H
5
10
15
20
x
8.26
2
0.011
0.45 0.5
0.55 0.6
0.65
J
5
10
15
20
x
0.50
2
0.0027
2.
3.
4.
5.
6.
7.
H
5
10
15
20
x
3.75
2
1.12
0.35 0.4 0.45 0.5 0.55 0.6 0.65 0.7
J
5
10
15
20
x
0.52
2
0.0043
2.
3.
4.
5.
6.
7.
8.
H
5
10
15
20
x
4.21
2
1.37
Fig. 12.4
Resulting distribution of goal function values (left column) and total harvest
biomass (right column) of Monte Carlo simulations for different stochastic processes (rows).
Figure 12.4 summarizes the results of several Monte Carlo runs. Using the smaller
sub-watershed(seeFigure12.1)allowstogeneratemorerealizations. Theﬁrstcolumn
in Figure 12.4 shows histograms of the global goal function results according to
Equation (12.5). The goal function values are normalized by the goal function value
derived by the local optimization. Values below unity denote simulation runs where
the global goal function returns values below the local optimization. Values above
unity denote that the local solution was improved. The second column shows the
histogram of the yield in the study area in US-$/m2 for comparison.
Row one can be identiﬁed as Monte Carlo simulation from scratch: the distribution
of land use types f(c), the land use type, and the fertilizer amount for each grid cell
are randomly generated. The second row derived f(c) from the local optimization
distribution. Rows three and four ofFigure 12.4disturbthelocal optimizationlanduse


232
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
Table 12.1
Correlation analysis of local optimization solution with underlying spatial data.
Porosity
Inﬁltration
rate
Field capacity
Percolation
rate
Hydrologic
conductivity
Elevation
Aspect
Slope
c(⃗z)
λN = 0.0
c(⃗z) corr.
0.046
-0.28
0.2
-0.44
-0.34
-0.20
0.071∗
0.052
1.0
sign.
0.057
0.25
0.42
0.073
0.16
0.42
0.003
0.031
F(⃗z) corr.
-0.027
0.045
-0.035
0.11†
0.2†
-0.075†
-0.044
-0.049∗
0.18†
sign.
0.27
0.067
0.15
0.0
0.0
0.002
0.069
0.044
0.0
λN = 0.1
c(⃗z) corr.
0.13†
-0.16†
0.13†
-0.18†
-0.2†
0.11†
-0.001
0.028
1.0
sign.
0.0
0.0
0.0
0.0
0.0
0.0
0.97
0.25
F(⃗z) corr.
0.10†
-0.14
0.087†
-0.95†
-0.15†
-0.001
-0.031
-0.036
0.19†
sign.
0.0
0.0
0.0
0.0
0.0
0.98
0.21
0.146
0.0
λN = 0.2
c(⃗z) corr.
0.25†
-0.33†
0.26†
-0.32†
-0.58†
0.089†
-0.60∗
-0.67†
1.0
sign.
0.0
0.0
0.0
0.0
0.0
0.0
0.014
0.006
F(⃗z) corr.
0.17†
-0.21†
0.17†
-0.21†
-0.23†
0.021
-0.003
-0.08†
0.37†
sign.
0.0
0.0
0.0
0.0
0.0
0.39
0.89
0.001
0.0
λN = 1.0
c(⃗z) corr.
0.41†
-0.47†
0.41†
-0.47†
-0.38†
-0.011
-0.046
-0.041
1.0
sign.
0.0
0.0
0.0
0.0
0.0
0.67
0.061
0.089
F(⃗z) corr.
0.16†
0.016†
0.14†
0.17†
-0.09†
-0.08†
0.017
-0.01
0.21†
sign.
0.0
0.0
0.0
0.0
0.0
0.001
0.49
0.69
0.0
† signiﬁcant correlation according 2-sided signiﬁcance level 0.01 (Spearman–Rho)
∗signiﬁcant correlation according 2-sided signiﬁcance level 0.05 (Spearman–Rho)
pattern with the probability p1 = 0.1 and p1 = 0.01. Obviously, stochastic generation
of land use patterns has limitations for identifying a map, which is optimum in terms
of the performance criterion. From the last two rows of Figure 12.4 it can be shown,
that an increase in the probability p1 immediately leads to solutions which are far
from the solution derived from local optimization. The local optimization approach
seems to be very close to a global optimum. However, there are land use patterns
which are “better” in terms of the global optimization. Are these land use patterns the
ones that take into account the neighborhood relationships of the control variables?
12.3.3
Statistical Analysis
What are the driving parameters for the optimum solutions? The question can be
answered by a simple bivariate correlation analysis based on the resulting land use
and fertilizer maps and the spatial input data of the model. Table 12.1 summarizes
the results of 4 correlation analysis studies of the optimum solutions to the set of
weights λN = 0.0, 0.1, 0.2 and 1.0. However, the sample size is high (1690) we


VALIDATION OF CONCEPT: RESULTS FOR HUNTING CREEK WATERSHED
233
used non-parametric correlation according to Spearman–Rho (Davis, 1984), because
normal distribution of the resulting parameters cannot be assumed. Input data maps
are the soil map and the elevation map. Parameters of the soil map are porosity [m 3
pore space per m3 sediment], inﬁltration rate [m/day], ﬁeld capacity [m pore space
per m sediment], percolation rate [m/day], horizontal hydraulic conductivity [1/day].
From the elevation map the aspects and slope are derived using GIS functions.
Setting λN = 0.0 neglects any ecological issues of agricultural production and fertil-
ization. The optimum solution is a land use map with the most valuable crop and a
high fertilizer amount. The correlation analysis shows that hardly any the important
parameters for nutrient transport in soil are responsible for the land use map. One
more general result is that the fertilizer application always correlates with the habitat
type: each crop gets its speciﬁc optimum amount of fertilizer.
An increase of the λ value shows signiﬁcant correlation to the parameters of the soil
map. For λ = 1.0 land use c∗(⃗z) and fertilization F∗(⃗z) show signiﬁcant correlation
with all parameters of the soil map. Weak correlations are also identiﬁed to the
parametersoftheelevationmap,especiallytoaspectandslope. Thisshowsthatspatial
relationships (to neighborhood cells) ﬁnd their interpretation in the locally optimum
solution from the spatially explicit model. Note, due to the large sample size, a small
sample set is sufﬁcient for a signiﬁcant correlation. In general all correlation values
are low. However, statistical analysis gave a validation of the derived results.
12.3.4
Genetic Algorithms
The only way to answer the question on the importance of neighborhood relation-
ships in the control variable maps is to set up an optimization procedure that uses
Equation (12.8) for assessment. As we have seen from the results of the Monte Carlo
simulation, the application of GA based on an initial population from scratch will fail,
because the variability of a population from scratch is much too broad. GA needs
too many iterations to converge to the solution we derived by the local optimization
approach, compare to Figure 9.3 upper right.
The smaller sub-watershed of the Hunting Creek is once again used for a detailed
study of this behavior. Figure 12.5 displays the convergenceprocess of a GA run from
scratch and the GA run from local optimum (smaller graph). It takes 300 generations
(4500 simulation runs) to achieve 80% of the goal function value. For this reason
the local optimum solution is used for the generation of the initial population, see
Figure 9.3 (lower part, mid column).
From the former results we can generate certain rules for the parameterization: too
large variations in the initial population take us away from the optimum. We set
p1 = 0.01 for the stochastic generation of the initial population. This has to be
assured within each step when generating a new population: mutation probability
should be much smaller than p1, cross-over probability should be equal to zero. To
enable modiﬁcations in the population we set migration probability to a high value
(0.9). The graph in Figure 12.5.b shows the results of the GA run started from the


234
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
100
200
300
400
500
generation
0.4
0.5
0.6
0.7
0.8
0.9
J
no prev. knowledge
5
10
15
20
25
30
35
40
0.96
0.98
1
1.02
1.04
initialpopulationby localoptimization
(a)
(b)
Fig. 12.5
Development of global performance criteria values during Genetic programming
process. (a) the GA process "from scratch". (b) the GA process started from a local optimum
solution with a stochastically "disturbed" of "mutated" population.
local optimum solution. The GA process clearly separates from the initial population
and improves the optimum solution by 2%.
What are the changes compared to the local optimum solution? Two maps are com-
piled to show the differences in each grid cell based on the best generation of GA set
up by 15 individuals. Figure 12.6 shows the results. The map in Figure 12.6.a shows
the average fertilizer difference. The map in Figure 12.6.b presents the modiﬁed land
use cells.
Only a small number of cells are changed: 43 out of 513 cells (8%). The distribution
of land use types remained the same. The global optimization by GA performed a
reallocation of habitats. We expected a couple of solutions, which can improve the
local solution. A complex problem like this might have multiple solutions. This
would have led to various examples (of habitat and fertilization maps) which change
different cells compared to the initial solution from the local optimization. However,
the map b) shows that nearly all of the individuals in the best generation modiﬁed the
same grid cells. Most of the modiﬁed cells belong the class where more than 13 out
of 16 individual changed the cell in the same way.
It is difﬁcult to derive an explanation as to why these are the crucial cells by statistical
approaches, however that would allow further improvement of spatial optimization.
The broad spectrum of spatial input data and the very complex network of dynamic
and spatial process in the simulation model, mean that no signiﬁcant correlation can
be identiﬁed. Using principle componentanalysis is not possible to reduce state space


RESULTS OF MULTI-CRITERIA OPTIMIZATION
235
No. of cells with habitat type
different to local optimum solution
0
1 - 3
4 - 6
6 - 12
13 - 15
Contours
Amount of fertilizer (kg/ha)
different to local optimum solution
25 - 50
50 - 75
75 - 100
100 - 125
125 - 150
Contours
(a)
(b)
Fig. 12.6
Analysis of GA results. The maps show the difference from one generation (15
individuals) of the GA to the local optimum maps for the sub-watershed: a) fertilizer amounts.
b) this map counts how many individuals of the population have a different land use type than
the local optimum solution. The small map in the center displays the extent and location of the
sub-watershed within the Hunting Creek watershed.
for analysis. A possible approach is to perform a bivariate correlation of c(⃗z 0) and
F(⃗z0) to the neighborhood cells, (north-east, north,..., south-west c(⃗z 0)). Two topics
make us expect illusory correlations: ﬁrst, analysis of the entire region, using every
grid cell (and its neighbors)as a repetitionjust gives a general answer, which is mainly
driven by a global aspect of the global slope of the catchment. Second, the landscape
model uses linkages between cells which are not direct neighbors for the hydrological
sub-module (Voinov et al., 1999).
12.4
RESULTS OF MULTI-CRITERIA OPTIMIZATION
12.4.1
General Results for Optimum Land Use Patterns
In the ﬁrst analysis the optimization results can be investigated using the habitat
distribution of the entire investigation area. If we use only one dimension of the
vector of weights ⃗λ in the performance criterion, these results can be summarized as


236
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
follows: neglecting all ecological concerns and focusing on economic proﬁts only,
⃗λ = 0, the optimum land use, is to plant soybean (70%) and corn (30%). The entire
study area changes to agricultural use only. Introducing ecological aspects in the
performance criterion makes forest an optimum habitat. In detail:
• Focusing on NPP, forest (70%) and corn (30%) become the dominant land use;
• Prioritizing N-output, a distribution of land use assuming 70% forest and 12%
soybean and 12% corn is most efﬁcient;
• Considering baseﬂow QB most important, one would expect forest to cover
most of the area, since it seems to be the kind of habitat that is most favorable
to increase water retention, cf. for example (Pattanayak & Kramer, 2001).
However, optimization results show fallow dominating the landscape, which is
quite suspicious.
Two questions result from this preliminary analysis:
1. How do these results change if scenarios of assessment are combined, e.g. if
the weights of ecosystem function values given by λ are modiﬁed?
2. Which regions are effected by a change of land use and how is this related to
the current data for land use distribution in the study area?
The second step in analysis of the results is the estimation of optimum land use
distributions as a function of different weighting schemes. This requires a broad
range of optimization runs with varied ⃗λ values. This can be performed without
much computational effort due to the separation of local and global optimization
methodologies.
A graphical representation of the habitat distribution as a function of the multi-
dimensional weighting space ⃗λ is hardly possible. Nevertheless, Figures 12.7 and
12.8 give an idea about how the changes in the optimum land use distribution in the
Hunting Creek area are driven by different weighting schemes. Figure 12.7 shows
how optimization results of habitat distributions change with a variationof the weights
λN (plot a), λQB (plot b) and λNPP (plot c). All three ﬁgures support the above men-
tioned general conclusion, that forest becomes an important part of the landscape,
if ecological issues are taken into account in the performance criterion. Depending
on the ecosystem function stressed by the weighting in the multi-dimensional perfor-
mance criterion, for the remaining area different habitat types are chosen. Focusing
on net primary production, corn is an important habitat. Corn and wheat are chosen,
if nutrient outﬂow is considered in the goal function.
Note that for the x-axis a logarithmic scale is chosen. We get different results of
optimum land use distribution changing λ N and λQB within 5 orders of magnitude.
Whereas the optimized land use distribution changes with a variation of λ NPP in the
interval λN = 1, . . ., 10. These results can be interpreted as a sensitivity analysis of


RESULTS OF MULTI-CRITERIA OPTIMIZATION
237
0
500
1000
1500
0.01
0.1
1
10
100
1000
λN
a) Variation λN
corn
soyb.
wheat
fallow
forest
500
1000
1500
1
10
100
1000
10000
100000
λQB
b) Variation of λQB
corn
soyb.
wheat
fallow
forest
0
500
1000
1500
1
2
4
8
λNPP
c) Variation of λNPP
corn
soyb.
wheat
fallow
forest
Fig. 12.7
Optimum land use distribution as a function of weighting coefﬁcients λN, λQB
and λNPP. Plot a) shows the response of the optimum land use distribution to a variation of
λN (λQB = λNPP = 0), c) the response to λQB (λN = λNPP = 0) and the lower plot c) to λNPP
(λN = λQB = 0).


238
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
0
500
1000
1500
0.01
0.1
1
10
100
1000
λN
a) λQB = 10, λNPP = 2.5
corn
soyb.
wheat
fallow
forest
500
1000
1500
0.01
0.1
1
10
100
1000
λN
b) λQB = 10, λNPP = 0.5
corn
soyb.
wheat
fallow
forest
500
1000
1500
0.01
0.1
1
10
100
1000
λN
c) λQB = 100, λNPP = 0.5
corn
soyb.
wheat
fallow
forest
Fig. 12.8
Optimum land use distribution as a function of weighting coefﬁcient λN.


RESULTS OF MULTI-CRITERIA OPTIMIZATION
239
a parameterized multi-criteria analysis. This provides a basis to choose weighting
scenarios for more detailed studies.
Figure 12.8 shows three similar graphs. For selected values of λ NPP and λQB the
land use distribution is plotted as a function of λN. Forest is an important habitat
in the landscape covering more than 50%, if net primary production or baseﬂow is
considered in the performance criterion. Also fallow may be an optimal land use, if
baseﬂow is stressed and nutrient outﬂow is neglected.
Based on the general behavior of the model derived from the sensitivity analysis in
Figure 12.7, one could hardly infer the plots presented in Figure 12.8. The general
conclusion is that, although the performance criterion is simple and linear, there
are essentially nonlinear changes in the optimal landscape patterns. We know from
former work that these patterns are caused by a highly complex network of spatially
distributed parameters and processes in the underlying simulation model.
12.4.2
Scenarios of Optimized Land Use Patterns
Next six weighting schemes of ⃗λ are selected for more detailed analysis.
Table
12.2 lists the selected values for the weighting vector ⃗λ in the upper part. Note,
with the exception of Scenario 2, all economic elements of the weighting vector
are set according to recent prices for crops and prices of fertilizer.
This means
that optimization of ecosystem functions can be interpreted in economic values. In
Scenario 2 Y(⃗z) is neglected, i.e. set to zero. With this scenario a closer look is taken
at the interrelationship between the three ecosystem functions in the optimization
results with respect to the attributes of the study area, e.g. soil properties, elevation,
etc.
Table 12.2 summarizes the optimization results in an aggregated way, listing habitat
distribution and the total amount of fertilizer applied in each of the 6 optimization
solutions. For comparison, recent land use (1990) shows 70% forest and 30% agri-
cultural habitats for all controllable cells, that is open water, rural and urban areas are
neglected in the comparison.
These optimized habitat maps and optimal fertilizer maps are now fedintothe Hunting
Creek model and full spatially explicit simulations on these so-called optimization
scenarios are run. Results can be then analyzed with respect to spatial properties
as well as with respect to the overall performance measures, such as total nutrient
outﬂow from the entire watershed.
In addition we can compare the results with some of the information available from
other published sources, cf. for instance the ECOTOX database (Jørgensen et al.,
2000). It was encouraging to ﬁnd that most of the results of our simulation, like NPP,
have the same order of magnitude as reported in literature, cf. Table 12.2 lower part.
Surface water and nutrient concentration in the basin outlet cell are important aggre-
gated indicators for numerous spatial hydrologic processes and for the nutrient cycle.
The drainage cell connects to the Patuxent river, which then drains into Chesapeake


240
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
Bay. To analyze the nutrient balance three scenarios are chosen for Figure 12.9:
Scenario 1, 2 and 4. These scenarios cover the range of variation for all scenarios.
The ﬁgures display the last year of simulation from July to June, t ∈[186, 551].
In the upper plot, Figure 12.9.a, the surface water level is displayed. The resulting
simulations based on optimization Scenarios 1 and 4 show water levels twice as high
as the result from Scenario 2. Considering the chosen weight, cf. Table 12.2 this
result is somewhat contradictory to the optimization goal. A higher value for λ QB
should result in a higher baseﬂow, which should result in a higher average water level
and lower peaks of the surface water level in the outlet cell.
One may hypothesize that it is most likely that by maximizing the amount of surface
water in each cell, actually the baseﬂow is decreased, since more water on the surface
means more water available for immediate runoff, higher evaporation, and as a result
less water in saturated layer, that feeds the stream network during dry periods. The
performance criterion can be modiﬁed to make it better represent the baseﬂow in the
Table 12.2
Deﬁnition of weighting scheme ⃗λ for optimization Scenarios 1 to 6 (upper part of
table) and aggregated optimization results of the control variables land use and fertilizer input.
Last column shows recent distribution of agricultural and forest area and literature values for
selected state variables of performance criterion.
Scen. 1
Scen. 2
Scen. 3
Scen. 4
Scen. 5
Scen. 6
Unit
Remarks
Speciﬁcation of performance criterion
λY
pH, pF
0
pH, pF
pH, pF
pH, pF
pH, pF
λY a
λN
0.05
0.01
1.5
0.0
50.0
0
λNPP
0.0
0.5
0.5
0.0
2.5
2.5
λQB
0.0
100
10
100000
1000
0
Resulting control variables
Percentage of land use H(⃗z)
Corn
10.5
21.1
13.7
22.4
13.3
37.8
%
Soybean
79.2
1.8
36.8
38.6
1.9
12.8
%
Wheat
9.9
5.7
13.2
4.4
14.2
0.1
%
Fallow
0.1
9.1
0.8
14.2
0.3
0
%
70.9 %b
Forest
0.2
60.5
35.5
20.5
66.9
49.5
%
29.1 %c
Applied fertilizer
F(⃗z)
5.58
2.14
2.79
2.61
0.65
4.62
g/m2
Resulting state variables
NPP
148
635
442
265
699
667
g/m2/y
650d
N(⃗z0)
2.05
0.84
0.91
2.24
0.37
0.69
g/m2
aλY denotes the prices for fertilizer and harvest biomass deﬁning Y(⃗z) = pHH(⃗z) + pFF(⃗z).
bTotal agricultural area, Hunting Creek, 1990
cForest Area Hunting Creek 1990
dcf. (Jørgensen et al., 2000, Table 2-202)


RESULTS OF MULTI-CRITERIA OPTIMIZATION
241
1
2
3
4
5
6
7
8
9
10
11
July
Aug.
Sept.
Oct.
Nov.
Dec.
Jan.
Feb. March April
May
June
Surface Water [m]
Time t
a) Surface water
Scenario 1
Scenario 2
Scenario 4
0
5
10
15
20
25
July
Aug.
Sept.
Oct.
Nov.
Dec.
Jan.
Feb. March April
May
June
N(z0) [g/m2]
Time t
b) Nitrogen load in surface water at watershed mouth ⃗z0
Scenario 1
Scenario 2
Scenario 4
Fig. 12.9
Time series of surface water level (plot a) and nitrogen load (plot b) both taken at
the watershed outlet cell⃗z0. Results from the Scenarios 1, 2 and 4 display the overall variation
of all six scenarios.
stream. Instead of surface water in the cells, of inﬁltrated water is calculated. In
Equation (12.10) QB is replaced by the accumulated amount of inﬁltrated water, the
weighting coefﬁcient is denoted by λI.
In this optimization one obtains a displacement of corn by forest in the landscape
(Figure 12.10), but further on, with even higher weights attached to the baseﬂow, one
ﬁnds that it is fallow that displaces soy beans, not forest. Even though the inﬁltration
coefﬁcient per se is three times higher for forests than for fallow, apparently now
the inﬁltration capacity starts to play the most important role. The amount of water
inﬁltrated depends not only upon the inﬁltration rate, but also on the amount of pore
space in the unsaturated zone, that can take water in, in the inﬁltration process. For


242
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
0
500
1000
1500
0.01
0.1
1
10
100
1000
λI
corn
soyb.
wheat
fallow
forest
Fig. 12.10
Optimum land use distribution as a function of weighting coefﬁcient λI of the
performance criterion adding yield and accumulated inﬁltrated water.
fallow, evaporation from the unsaturated layer is assumed to be ten times higher than
in forests. As a result one gets more inﬁltration capacity in fallow, and, hence, more
water inﬁltrated.
If baseﬂow is calculated globally one still achieves the highest results for mostly
forested landscapes. The ﬁnal conclusion from this is that optimization for baseﬂow
is not achieved with the chosen methodology of local optimization, e.g. simplifying
the spatially explicit problem. There seems to be no good way to express baseﬂow (a
global feature) in terms of some local variables and processes. Processes that show
high spatial interaction are hard to treat with this local optimization methodology.
Performance criteria and optimization algorithms need to be formulated on a global
or at least regional scale.
On the other hand, minimization of nutrient outﬂow is achieved by local optimization.
Figure 12.9.b displays the time series of the nitrogen load in the outlet cell. Scenario 1,
which almost neglects any ecological aspects, results in higher nutrient concentration.
Scenario 2 and Scenario 4 result in lower nitrogen concentrations. Note that this is
an outcome of spatial allocation of land use type only, the climatic conditions (most
importantly precipitation and atmospheric N input) as well as fertilizer application
are constant, cf. Table 12.2.
These two results may sound contradictory, since nutrient ﬂow is strongly related to
hydrology. Apparently nutrient ﬂow is more spatially buffered and has less spatial
variability, so the local performance criterion captures the effects that play the most
important role globally.
Figure 12.11 gives an overview of the 1990 land use in the Hunting Creek region.
The watershed area is shared between urban, rural, open water, forest and agriculture
habitats. No distinction for different crops is made in that map. Figure 12.11 also
offers detailed maps of a small region near the creek. These areas near rivers and
creeks were identiﬁed as crucial in terms of optimization for the nutrient balance in the


RESULTS OF MULTI-CRITERIA OPTIMIZATION
243
Scenario 4
Scenario 1
Scenario 2
Scenario 5
Scenario 3
Scenario 6
Hunting Creek 
Landuse 1990
Grid cell size: 200m
Water & Wetland
Forest
Resident
Urban
Agriculture
Corn
Wheat
Soybean
Fallow
Fig. 12.11
Resulting land use patterns of the six optimization scenarios.
region. These pattern are clearly endogenous as these are derived from the processes
coded in the model together with the application of the model in the optimization
task, cf. Section 3.1.3.
The map from Scenario 1 shows that neglecting ecosystem functions and ecological
impacts of agricultural production results in an optimum with agricultural habitat
occupying the entire study area. All other weightings result in more heterogeneous
optimal landscape patterns. Two issues should be noted. First, cells selected for
agricultural production show similar patterns independent of the chosen weighting
scheme. Only the crop variety planted depends on the ecosystem function(s) chosen
in the performance criterion. Second, the cells allocated for agricultural production
seem to be the same, perhaps shifted by some grid cells, as in the current land use
for agriculture in Hunting Creek. One may derive the hypothesis that the history


244
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
of agricultural production in Hunting Creek developed towards a somewhat optimal
landscape. The question is raised how one can compare the recent land use with the
results derived from the optimization procedure.
12.5
CLIMATIC VARIABILITY AND OPTIMUM LAND USE PATTERNS
Allresultsuptothispointarebasedsolelyonclimaticconditionsoftwoyears1990/91.
An important question is, how do optimum land use pattern depend on climatic
variation? Does the methodology respond sensitively to changing precipitation or
radiation?
These questions can be answered either by a sensitivity analysis in the related param-
eters or by application of the methodology to several consecutive years. Based on
the Hunting Creek model an optimization study was performed calculating optimized
land use and fertilizer maps. We focus on the problem of optimizing land use patterns
with respect to nitrogen outﬂow and economic yield as introduced in Section 12.2.1.
Figure 12.12 displays the land use distributions (plot a) and the optimum fertilizer
amounts (plot c) as a function of the weighting coefﬁcient λ N for the eleven years
1985 to 1995. The variation through the years is quantiﬁed by the derived plots of
standard deviation of land use (plot b) and fertilization (plot d).
From these results one can derive, that approximately 10% of the controllable cells
depend on the climatic situation of the considered year. Additionally, standard devi-
ations vary as a function of λN. Second, standard deviation for the fertilizer amounts
is below 50 kg/ha. Extreme scenarios, like very small and very large values of λ N
lead to higher standard deviation values for the optimum fertilizer amounts.
12.6
MULTI-SCALE ANALYSIS OF LANDSCAPE PATTERNS
The comparison of landscapes required the comparison of habitat patterns. Two
approaches of pattern comparison come to mind, if one considers grid-based maps
with discrete attributes. The coarsest approach is to compare the distribution of
habitats in the entire area. This neglects any spatial patterns. The ﬁnest approach is
to compare cell by cell, or pixel by pixel and to count the number of matches. This
may be much too strict as patterns may appear transposed, rotated or slightly shifted
in any two maps. We would still call these landscapes similar if we were visually
comparing them. What we need is a distance measure, which allows a merger of
both approaches. There are different procedures of multi-scale map comparison in
development using different methodologies, for example fuzzy logic as presented by
Hagen (2003).


MULTI-SCALE ANALYSIS OF LANDSCAPE PATTERNS
245
0
500
1000
1500
0.01
0.1
1
10
100
a) Optimum land use distribution from year 1985–1995
corn
soyb.
wheat
fallow
forest
0
25
50
75
100
0.01
0.1
1
10
100
b) Standard deviation of optimum land use distribution
0
25
50
75
100
0.01
0.1
1
10
100
c) Average optimum fertilizer amounts
F(⃗z) d⃗z [kg/ha]
0
50
100
0.01
0.1
1
10
100
λN
d) Variance of optimum fertilizer amounts σ2
F(⃗z) d⃗z [kg/ha]
Fig. 12.12
Results of optimum land use pattern to climatic variation. Optimization results
base on the simulation in the consecutive year 1985 to 1995. Plot a) and b) display the habitat
distribution for the 11 runs (a) and the derived variance. Plot c) and d) analogously plot the
average fertilizer amount.


246
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
12.6.1
Distance Measure of Discrete Maps
Habitat maps show discrete attributes, for instance soybean (1), corn (2), urban (3)
etc., which may be summarized by an integer attribute H(⃗z) ∈{1, 2, . . .} = S . The
number of attributes of classes — here habitat types — is given by |S |. The attribute
of a certain grid cell ⃗z is denoted by H(⃗z).
The basic idea for the comparison of two habitat maps H 1 and H2 goes back to the
multi-scale approach from Costanza (1989) supported by some analytical considera-
tions. Using a moving window with the edge length w ≥1 the number of cells in the
window, belonging to a certain class, i is compared for each habitat map H 1 and H2.
Let us denote this moving window at cell ⃗z ∈R and the width and length w ≥1 by
Uw(⃗z).
Let gi(H ∩Uw(⃗z)) denote the number of cells with the attribute i in a window U w(⃗z)
at location ⃗z on map H. Then
ρw(H1, H2) = 1
2
1
size(R)
1
size(H1 ∩Uw(⃗z)) ⃗z∈R
|S |
i=1
gi(H1 ∩Uw(⃗z)) −gi(H2 ∩Uw(⃗z))
deﬁnes a function which measures the distance between map H 1 and map H2 using a
moving window of size w2. The function size(·) denotes the size of considered map
in the argument given in numbers of grid cells.
Function ρw is very intuitive and has all the essential features of a distance measure:
1. ρw(H, H) = 0 for an arbitrary w ≥1: the distance between two identical maps
is zero.
2. If ρw(H1, H2) is divided by size(R) the function is normalized to unity for
entirely different maps: ρw(H1, H2) = 1 for each w ≥1 if and only if H1(⃗z) 
H2(⃗z) for all ⃗z ∈R.
Setting the maximum value of ρw equal to unity is an arbitrary deﬁnition.
Neglecting this normalization is a reasonable choice, too. This might allow us
to compare maps with different shapes. However, using the normalized value,
the following properties of ρw become valid.
3. ρ1(H1, H2) denotes the difference between H1 and H2 in grid cell scale. This
means 1 −ρ1 is the fraction of cells which are identical.
4. Let L deﬁne the maximum diameter of the study area or the given map H:
L = max diam(H). The diameter is given by length of the largest of all possible
cross-sections of a map. Then ρ∞(H1, H2) = ρL(H1, H2) denotes the distance if
the moving window covers the entire study area R. In that case the distribution
of attributes in the maps H1 and H2 is compared. That means that 1 −ρ∞
denotes the fraction of attributes with an equal distribution in both maps.


MULTI-SCALE ANALYSIS OF LANDSCAPE PATTERNS
247
For an overall assessment of the map distance ρ(H1, H2) = 1
L
L
0 ρw(H1, H1)dw may
be calculated. The upper limit of integration is given by the maximum diameter
of the study area. A second integrative measure derived from ρ w is ρ0(H1, H2) =
min
w=1,...,L ρw(H1H2) together with the w0 value, for which ρw equals its minimum. These
two values indicate the similarity or distance of two maps H1 and H2 as well as the
scale or distance at which most patterns ﬁt.
Additionally, one can prove that ρ, ρ∞, ρ0 and ρ1 are distance measures in a mathe-
matical sense. It holds true, that
(i) ρ(A, A) = 0
(ii) ρ(A, B)  0 ⇔A  B
(iii) ρ(A,C) ≤ρ(A, B) + ρ(B,C)
12.6.2
“Correlation”-analysis of Landscape Patterns
This approach of map comparison is now applied to the results of the landscape
optimization Scenarios 1 to 6. Similar to correlation analysis, Table 12.3 displays the
ρ0 values and the window sizes w0, for which ρw is minimal.
This clearly shows that habitat maps from Scenarios 1 are different from all other
habitat maps in terms of their similarity to other maps (ρ0 > 0.65). Compared to
Scenarios 2 to 6 this scenario is characterized by very low values for ecosystem
functions. However, minimum values of ρw are reached for w = 3, . . ., 9. To explain
this one should recall that non-controllable cells presenting urban, open water and
rural areas are also taken into account for map comparison. In this case spatial patterns
of these cells dominate the map comparison values.
All other comparisons lead to smaller ρ0 values. In these cases the w0 value is a good
indicator of what may be causing this similarity. If w0 is close to the study area size
L = 58, similarity is mainly caused by the agricultural habitat distribution over the
entire study area. Smaller values of w0, e.g. for comparisons of Scenarios 2 vs. 9,
3 vs. 8 and 6 vs. 9, show that certain more local landscape patterns cause similarity.
Comparing these results with weighting schemes of ⃗λ in Table 12.2 we arrive at a
surprising result: the ⃗λ vectors for these scenarios are not close to each other in the 3-
dimensional weighting space. This again makes clear that the underlying processes
incorporated into the spatially explicit simulation model are highly nonlinear with
respect to dynamics and to spatial dynamics of material ﬂuxes.
With the map distance measure developed one can answer the question raised in the
previous section. How similar is the recent land use compared to the maps resulting
from the optimization procedure? Table 12.3 shows map distance measures for the
recent land use and the maps resulting from the optimization scenarios. Note that in
this application of the distance measure only the habitat types for forest, agriculture,
open water, urban and rural are taken into account to match the categories on the
underlying data set of the 1990 land use map.
As expected the optimized map from Scenarios 1 is different from the 1990 land use
map (ρ = 0.59). However, some similarities are identiﬁed for a 3-cell-wide moving


248
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
Table 12.3
Map comparison of optimum habitat maps H for the Scenarios 1 to 6 and com-
parison with recent land use. The table displays the ρ0 values of two optimized habitat maps
Hi and Hj (i = 1, . . . , 6;
j = 1, . . . , i) and the associated w0 values. The table is to be read like
a correlation matrix, see text.
1990 land use
1
2
3
4
5
1
0.59 (3)
2
0.1 (9)
0.72 (7)
3
0.31 (5)
0.35 (9)
0.38 (27)
4
0.46 (6)
0.37 (52)
0.41 (9)
0.26 (24)
5
0.04 (15)
0.66 (5)
0.14 (38)
0.32 (6)
0.54 (9)
6
0.17 (7)
0.65 (3)
0.19 (57)
0.34 (33)
0.41 (9)
0.27 (56)
window. Results from Scenarios 3 and 4 seem to be closer to the 1990 land use map.
The maps resulting from the optimal Scenarios 2 to 4 are almost identical to the 1990
map. The similarity is caused by similar patterns at the scale of 5 to 7-cell-wide
windows. This proves the hypothesis from the previous section: the resulting maps
from the optimization are similar to the recent land use map. Note that this holds only
for a distinction between aggregated agricultural and forest cells as this is the level
of detail the data land use map offers.
12.6.3
Optimization Results on Differing Scales
The methodologicalframework presented can easily be transfered to different regions
without any increase of computational effort as long as is it possible to apply the local
optimization approach. This was performed for the entire Patuxent watershed, a
region 2359 km2 in size. The spatial data set for a spatially explicit application of the
generic landscape model (see Section 3.3.3) in this case is set up by a grid cells of
1km2 size, see Figure 12.1. Additionally the results of optimum habitat distribution
are displayed for the small sub-watershed within the Hunting Creek catchment.
We focus on the problem of optimizing land use patterns with respect to nitrogen
outﬂow and economic yield, see Section 12.2.1. Figure 12.13 displays the results of
land use distribution of the study areas Hunting Creek (b) and Patuxent (a) as well as
the smaller sub-watershed (c). Figure (b) is equal to Figure 12.2. Note, relative land
use distributions are plotted as both areas have different numbers of controllable cells
Rc: sub-watershed |Rc| = 485, Hunting Creek |Rc| = 1652, and Patuxent |Rc| = 2133.
The striking result of this multi-scale analysis of optimization results with three em-
bedded study areas and two different granularities (cells sizes) is, that the resulting
function of land use distribution are very similar. The calculation of the correla-
tions coefﬁcients for Patuxent and Hunting Creek leads to an overall correlation of
r2 = 0.87. Calculating correlation coefﬁcients for land use habitats separately lead
to: corn r2 = 0.61, wheat r2 = 0.89, soybean r2 = 0.94 and forest r2 = 0.97. These


MULTI-SCALE ANALYSIS OF LANDSCAPE PATTERNS
249
0
1
0.01
0.1
1
10
λN
a) Patuxent Watershed
corn
soyb.
wheat
fallow
forest
0
1
0.01
0.1
1
10
λN
b) Hunting Creek Watershed
corn
soyb.
wheat
fallow
forest
0
1
0.01
0.1
1
10
λN
c) Subwatershed
corn
soyb.
wheat
fallow
forest
Fig. 12.13
Comparison of optimum land use distribution optimizing economic yield against
nutrient loss for Patuxent study area (a), Hunting Creek watershed (b) and the sub-watershed
(c) based on climate data from 1990/91.
values aggregate the results too much, as no spatial patterns are taken into account.
However, one can state that the endogenous pattern derived and identiﬁed from the
Hunting Creek study appears in the Patuxent Landscape Model, too. Second, exoge-
nous pattern such as different soil type results in slightly different optimum habitat.
For instance wheat is a more frequently chosen habitat for Patuxent than it is for
Hunting Creek. Figure 12.14 display three different optimum habitat maps of the
Patuxent watershed for selected values of λN.


250
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
Fig.12.14
LocaloptimumlandusemapsforPatuxentwatershedusingλN = 0.5(a), λN = 1.0
(b) and λN = 10.0 (c).
12.7
SUMMARY AND OUTLOOK
12.7.1
Methodological Aspects
Building upon the backgroundof the spatial modeling environment the application of
the proposed framework presented in Section 9.3.6 is capable of answering different
questions of landscape management. Run-time solutions for optimization problems
can be derived (for example in the ArcVIEW front end) if it is possible to set up a
local optimization criterion and if a global solution is not required. In this case the
computational effort does not signiﬁcantly depend on the size of study area. On the
other hand, the use of GA for global optimization offers the ability of parallelization
in the optimization process. In summary, this framework seems to be applicable to
a large class of problems in landscape ecology. It enables integration of simulation
models and environmental management.
Theonlysimpliﬁcation,whichwasintroducedtoderiveasolutiontothisverycomplex
optimization task, was to assume a weak dependency of the single parameters of the
control variable maps upon the neighborhood. This allows a characteristic function
to be set up for each grid cell of the model. We focus on simple goal functions that
assess the state of a certain grid cell only. The core question which lies behind this
consideration of neighborhoodrelationships of the control variable mapis,how strong
is the synergistic effect of land use change for a given watershed? It is an exciting
question to be investigatedin the frameworkof optimization, see for example(M ¨uller,
1998; Wolfert et al., 2002).


SUMMARY AND OUTLOOK
251
As the modeling and optimization approach presented incorporates aspects of topol-
ogy and connectivity of cells, statistical analysis applied to multi-dimensional spa-
tially explicit models is limited. The methodology of map comparison presented
extends analysis of multivariate statistics. With the use of landscape pattern compari-
son we are able to show how much optimizationresults differin terms of local patterns
for global (whole watershed) land use distribution. Additionally, invariant patterns
can be identiﬁed and the spatial scale of the invariant patterns can be quantiﬁed.
invariant property
12.7.2
Optimization Results as Multi-stage Decision Process
There are several major results of this study. First, on a global scale the optimization
problem is based on a multi-dimensional performance criterion and leads to optimum
land use patterns, which support certain ecosystem functions. These patterns can be
studied as a function of weighting coefﬁcients in the performance criterion. Second,
with an adequate map comparisonmethodologyone can show that certain patterns are
invariant to different weightings of ecosystem functions in the performance criterion.
invariant property
One may summarize these results qualitatively in the following way, which may be
interpreted as a multi-stage decision-making process.
1. If only economic considerations are taken into account in the performance
criterion, cells that are optimal for agricultural production are identiﬁed;
2. If ecosystem functions are considered (one of λ NPP, λQB, λN > 0) less fertile
sites and cells crucial for the regional nutrient balance are identiﬁed;
3. Depending on particular weighting schemes for λ NPP, λQB, λN a certain com-
bination of fertile and less fertile cells are allocated for agriculture;
4. The remaining cells are allocated for forest habitats.
12.7.3
Application of Results
Comparison to Real World Data
These studies may be viewed as model ex-
periments of spatial change in land use allocation in the landscape. In this context
it is interesting to see that some optimized habitat maps are fairly close to maps of
the existing landscape. We can conclude that in some sense the existing landscape in
the Hunting Creek watershed is optimal, at least in terms of some of the assessment
scenarios.
Second, an important result that advocates an application to more realistic spatially
explicitmanagementproblemsisthevariationoftheoptimizationresultsunderchang-
ing climatic conditions. This suggest an application of the concept in the framework
of climate change scenarios for different investigation sites. A possible concept would


252
CHANGING LANDSCAPES: OPTIMUM LANDSCAPE PATTERNS
be to use stochastically generated climatic conditions driven by an increase of mean
temperature and precipitation together with a spatially explicit population dynamic
model for different vegetation types.
Experiments on a Landscape Scale
It is difﬁcult to design, implement and
perform experiments that allow the results obtained in these studies to be tested. This
is neither a disadvantage nor should this impede an implementation of the derived
management strategies to a landscape. First, models enable us to do investigations and
simulationsstudiesaspresentedinthischapter, becausetheyallowtobestudiedresults
without effecting a real world landscape. Second, real world landscape management
problems show a larger spectrum of constraints.
One has to keep in mind this fact when studying publications on experiments on this
landscape ecological issue. Li et al. (2002), for example, derived that only 10% of
the nutrient reduction is caused by spatial conﬁguration of habitats. On the other
hand, Kuusemets & Mander (2002) performed an experimental analysis on nutrient
ﬂow management in a 378 ha watershed in Estonia and advocate establishment of
buffer zones at the banks of the stream, that would remove 2000 to 2640 kg nitrogen
a year. Naiman and D´ecamps (1997) as well as Malard et al. (2002) state more
qualitatively that riparian zones play an essential role in water and landscape planning
and in restoration of aquatic systems. The spatial arrangement of surface-subsurface
exchange patches affects heterogeneity in stream nutrient concentration,surface water
temperature and colonization of dry reaches by invertebrates.
This is in accordance with the results of the landscape optimization results studied in
this chapter, albeit, only a limited view of the mentioned aspects of the ﬁeld experi-
ments were considered in the landscape model. One important result can be derived
from these considerations. An application of landscape management patterns and
scenarios to real world management problems can be supported by the consideration
of real boundary conditions in the optimization task.
12.7.4
Patterns and Processes
Several results were obtained in the studies that offer a deep insight in the relationship
of landscape pattern and the spatially explicit processes responsible. First, important
areas with high retention capabilities — buffer zones — were identiﬁed and fertilizer
maps were set up depending on soil properties. This shows that optimization methods
even in complex simulation models can be a useful tool for a systematic analysis of
management strategies of ecosystem use.
Second, the results speak in favor of the statement that the developed methodology
gives robust optimization solutions based on complex ecosystem models. They ex-
tend the previous analysis for multi-dimensional performance criteria and show how
to identify important regions or groups of cells, which support certain ecosystem
functions.


SUMMARY AND OUTLOOK
253
Third, the results are likely to be scale invariant. Typical patterns of optimum land
use distributions as a function of a weighting coefﬁcient of the performance crite-
rion are similar for the three embedded study areas as well as for landscape models
regionalized using a different granularity.
Fourth, the results show superposition of endogenous and exogenous patterns. It is
difﬁcult to identify which are mostly caused by endogenous processes and which pat-
terns are caused by external driving forces. The statistical analysis (Section 12.3.3)
could prove that not all patterns are caused by site conditions. The concept of map
comparison helps to identify similarities in the resulting patterns. However a rela-
tionship to determining processes is hardly possible. These questions can only be
answered by a more detailed analysis of the underlying model together with dif-
ferent parameterizations of the performance criterion. The processes model, which
is embedded in the optimization framework, builds the connection of patterns and
processes.
12.7.5
Outlook
The approach may be extended by the integration of the neighborhood of a given
grid cell Uw(⃗z) with w > 1. The proposed framework is capable of dealing with
goal functions deﬁned on all ⃗z ∈Uw(⃗z0). This allows the assessment of habitat
structures in the goal functions. Habitat suitability of certain species determined by
patch conﬁguration may be assessed with this extension.
Besides this, some methodological requirements could be derived. In these studies
we identiﬁed processes that could not be handled within the localized optimization
methodology. Two directions for further research can be derived from those results.
First, criteria should be deﬁned that characterize sub-models with their appropriate
spatial optimization strategy. Second, methodology for global or at least regional
scale spatial optimization must be developed or improved.
Finally, possible extensions to this concept are to integrate economic models into
the landscape model to achieve a more detailed description of the anthropogenic pro-
cesses. There are models of urban growth, and modelinginterrelations with economic
models, as suggested by Irwin & Geoghegan (2001).


13
Conclusions, Perspectives
and Research Demands
13.1
RETROSPECTION
It is difﬁcult to distill a few important topics from an entire book which itself is a
distillation of numerous publications. A few general statements, however, should be
given at the end to answer the questions about what we have learned from this text.
First of all, I have tried to clarify, that modeling is not a mystery, nor an art, it is
a science. Fundamental statistics as well as criteria from scientiﬁc theory should
be applied to assess performance of simulation models. It is a general rule that
environmental models should be based on physical processes and derived from ﬁrst
principles wherever possible. We learned that the scale of interest, the focal level,
often deﬁnes the mathematical structure, and that nonlinearities are introduced by
implementing processes from different spatial and temporal scales to the focal level.
Nonlinearities are a result of movingacross scales duringthe modelingprocess. These
are ﬁrst answers to some of the questions Wu & Hobbs (2002)raised in their overview
paper.
Additional recommendations for environmental modeling are to understand models
as a toolbox, to assure reusability of models or sub-models, and to aim at integration
of present models, because modeling from scratch is rarely appropriate for solving
and assessing environmental problems. Firstly, because the resource time is limited
because ﬁnancial support may be limited and secondly because data availability on
the considered process may be insufﬁcient. By applying spatially explicit models to
a real landscape (either by the use of highly aggregated partial differential equations
or by using integrated model systems) we have achieved a methodological link be-
tween functioning of ecosystems and landscape patterns. Based on this, endogenous
255


256
CONCLUSIONS, PERSPECTIVES AND RESEARCH DEMANDS
patterns could be separated from exogenous patterns. And, in any real world land-
scape endogenous and exogenous patterns are superimposed. Assessing landscape
patterns by simply applying landscape metrics may be insufﬁcient. This has been
identiﬁed as research a demand in environmental science and landscape ecology by
several authors (Turner et al., 2001; Opdam et al., 2002). By the use of physically
based spatially explicit models we are able to study ecological ﬂows in landscape
mosaics. We may relate landscape metrics to ecological processes and may identify
causes, processes and consequences of land use and land cover change, see again (Wu
& Hobbs, 2002). This can be a ﬁrst step for further theoretical studies in landscape
ecology as demanded by Bastian (2001). Simulation models undoubtedly play an
important part in environmental science as these enable us to move the focus from
qualitative analysis of ecological issues to quantitative research.
13.2
CONCLUSIONS
Finally, in their idiosyncratic synthesis of recent research demands in landscape ecol-
ogy Wu & Hobbs identify the need of integration of human activities into landscape
ecology as well as the optimization of landscape patterns as important research topics
in the coming decades (Wu & Hobbs, 2002). These issues have been discussed in
detail throughout the third part of this text.
Scenario analysis is a common tool for model analysis and for assessing different de-
velopment pathways. But scenario analysis is limited, if model complexity growth,
the number of driving forces increase and spatially dependency is introduced. Ap-
plications of environmental models in terms of optimum control theory are a very
promising branch of ecological system theory.
This methodology offers a link between anthroposphere and biosphere processes. It
introduces economics into ecological modeling and is therefore an important part
of ecological economics. If the performance criterion is deﬁned following these
considerationsof ecologicaleconomics, which introducecosts for ecosystem services
or ecosystem damage, we can study human impact on the environment by economic
considerations. This may increase awareness of ecosystems functions and provide us
with informationon the environmentalcosts of our impact (Costanza, 2000; Costanza
et al., 1997; Scheffer et al., 2000). This is possible because economic considerations
always aim at maximizing yield, which is in accordance to the optimization approach.
A second important analogy in nature of the optimization approach is that nature
does not waste available energy. Using the evolutionary concept of maximizing
information and function by using a minimum of free energy, is a second valuable
approach for the optimization concept (Jørgensen et al., 1998; M ¨uller, 1998).
Applications of optimization and optimum control enable us to study dependencies
of the driving forces of a system to environmentaloutcomes. Of course, the computa-
tional effort is tremendous. However a considerable spectrum of possible application
of control theory to environmental model is presented in this book. Anyway, one


PERSPECTIVES
257
should not forget the increasing power of computers in the future. This is why op-
timization using environmental models should ﬁnd its way into the application of
decision support systems for environmental management.
13.3
PERSPECTIVES
Heterogeneity has been a point of discussion throughout this text. One reason for this
diversity in environmental models is that models come from a multitude of different
origins, see Part I. This pluralism of approaches make environmental modeling a
fascinating and very promising branch of science. We need this pluralism to solve
recent environmental problems in an acceptable time. It is neither understandable by
decision makers nor helpful for the environment to spent much time on model de-
velopment, testing and verifying before offering possible solutions. Increasing pop-
ulation growth will intensify human impact on nature. Resources will be withdrawn
from the environment more quickly and time for suggesting alternative strategies for
a sustainable use of environmental resource, let it be water, food or space, will be
reduced.
Environmental modeling research should therefore concentrate on the modularity,
reusability and transferability of models. It is not appropriate to start modeling from
scratch, even if “modelingis also fun” (Pahl-Wostl, 1995). One should aim at viewing
environmental models as a toolbox. This can be supported by mathematics in all
related environmental scientiﬁc disciplines like biology, ecology, landscape ecology
etc. Mathematics can act as a common language. My wish is, that this text supports
environmental research with a methodological foundation and is a stimulus for new
ideas, exciting approaches and further applications of integratingapplied mathematics
to environmental sciences.


References
Adler, R., Amiran, D.H. K., Eliakim, H., Gilead, M.H., Hinberger, Y., Kadmon, N.,
Kantor, M., Shachar, A., & Tsameret, R. 1985. Atlas of Israel — Cartography,
Physical and Human Geography. 3rd edn. Tel-Aviv: Survey of Israel.
Alonso-Sanz, R. 2003. Reversible cellular automata with memory: two-dimensional
patterns from a single site seed. Physica D, 175, 1–30.
Altmann-Dieses, A.E., Schl¨oder, J.P., Bock, H.G., & Richter, O. 2002. Optimal
experimental design for parameter estimation in column outﬂow experiments.
Water Resources Research, 38(10), 1186–1197.
Anderson, K., & Neuhauser, C. 2002. Patterns in spatial simulations — are they real?
Ecological Modelling, 155, 19–30.
Anderson, M.P., & Woessner, W.W. 1992. Applied Groundwater Modelling. Toronto:
Academic Press. Inc.
Angel, E., & Bellman, R.E. 1972. Dynamic Programming and Partial Differential
Equations. Academic Press, New York.
Apel, H., Paudyal, M.S., & Richter, O. 2003. Evaluation of treatment strategies of the
late blight Phytophthora infestans in Nepal by population dynamics modelling.
Environmental Modelling & Software, 18, 355–364.
Appelt, M. 1996. Elements of population vulnerability of the bluewinged grasshop-
per Oedipoda caerulescens. Pages 320–323 of: Settele, J., Margules, C. R.,
259


260
REFERENCES
Poschlod, P., & Henle, K. (eds), Species Survival in Fragmented Landscapes.
The GeoJournal Library, vol. 35. Dordrecht, Netherlands: Kluwer Academic
Publishers.
Appelt, M., & Poethke, H. J. 1997. Metapopulation dynamics in a regional popula-
tion of the bluewinged grasshopper (Oedipoda caerulescens; Linnaeus, 1758).
Journal of Insect Conservation, 1, 205–214.
Arrowsmith, D.K., & Place, C.M. 1994. Dynamische Systeme. Spektrum Akademis-
cher Verlag, Heidelberg.
Azar, C., Holmberg, J., & Lindgren, K. 1996. Socio-ecological indicators for sus-
tainability. Ecological Economics, 18, 89–112.
Baer, J., & Verruijt, A. 1987. Modelling Groundwater ﬂow and Pollution. Dordrecht,
Holland: D. Reidel Publishing Company.
Band, L.E., Peterson, D.L., Coughlan, J., Lammers, R., Dungan, J., & Nemani, R.
1991. Forest ecosystem processes at the watershed scale: basis for distributed
simulation. Ecological Modelling, 56, 171–196.
B¨arlund, I., & Tattari, Sirkka. 2001. Ranking of parameters on the basis of their
contribution to model uncertainty. Ecological Modelling, 142, 11–23.
Bastian, O. 2001. Landscape ecology — towards a uniﬁed discipline? Landscape
Ecology, 16, 757–766.
Bear, J., & Bachmat, Y. 1990. Introduction to Modelling of Transport Phenomena
in Porous Media. Dordrecht, Boston, London: Kluwer Academic Publishers.
Beddington, J., Botkin, D., & Levin, S.A. 1981. Mathematical models and resource
management. In: (Vincent & Skowronski, 1981), 1–5.
Begon, M., Harper, J.L., & Townsend, C.R. 1986. Ecology. Oxford, London, Edin-
burgh: Blackwell Scientiﬁc Publications.
Bellman, R., & Kalaba, R. 1960. On k–th best policies. Journal of the Society for
Industrial and Applied Mathematics, 8, 582–588.
Bellman, R.E. 1957. Dynamic Programming. Princeton University Press, Princeton.
Bellman, R.E., & Dreyfus, S.E. 1962. Applied Dynamic Programming. Princeton
University Press, Princeton.
Benz, J. 2003. WWW-Server for Ecological Modelling. URL: http://eco.wiz.
uni-kassel.de/ecobas.html. May, 2003.
Benz, J., & Knorrenschild, M. 1997.
Call for a common model documentation
etiquette. Ecological Modelling, 97, 141–143.


REFERENCES
261
Benz, J., Hoch, R., & Gabele, T. 1997. Documentation of mathematical models in
ecology — an unpopular task. ECOMOD, 1–8.
Berger, U., & Hildenbrandt, H. 2000. A new approach to spatially explicit modelling
of forest dynamics: spacing, ageing and neigbourhoodcompetition of mangrove
trees. Ecological Modelling, 132, 287–302.
Beven, K., Freer, J., Hankin, B., & Schulz, K. 2001. The Use of Generalised Like-
lihood Measures for Uncertainty Estimation in High-Order Models of Environ-
mental Systems. Pages 115–151 of: Fizgerald, W.J., Smith, R.L., Walden, A.T.,
& Young, P. (eds), Nonlinear and Nonstationary Signal Processing. Cambridge:
Cambridge University Press.
Beven, K.J. (ed). 1997. Distributed Modelling in Hydrology: Applications of TOP-
MODEL. Chichester: Wiley.
Beven, K.J., & Kirkby, M.J. 1979. A physically based, variable contributing area
model of basin hydrology. Hydrological Sciences Bulletin, 24(1), 43–69.
Bevers, M., Hof, J., Uresk, D.W., & Schenbeck, G.L. 1997. Spatial optimization of
prairie dog colonies for black-footed ferret recovery. Operations Research, 45,
495–507.
Bock, H.G. 1983. Recent Advances in Parameter Identiﬁcation Technique for ODE
Systems. Progress in Scientiﬁc Computing, vol. 2. Boston: Birkh ¨auser.
Bormann, H., Diekkr¨uger, B., Renschler, C., & Richter, O. 1999. Regionalization
scheme for the simulation of regional water balances using a physically based
model system. Physics and Chemistry of the Earth (B), 24(1–2), 43–48.
Boumans, R., Costanza, R., Farley, J., Wilson, M.A., Portela, R., Rotmans, J., Villa,
F., & Grasso, M. 2002. Modeling the dynamics of the integrated earth system
and the value of global ecosystem services using the GUMBO model. Ecological
Economics, 41(3), 529 – 560.
Boumans, R.M., Villa, F., Costanza, R., Voinov, A., Voinov, H., & Maxwell, T.
2001. Non-spatialcalibrationsofageneralunitmodelforecosystemsimulations.
Ecological Modelling, 146, 17–32.
Breunig, M. 1996. Integration of Spatial Information for Geo-Information Systems.
Lecture Notes in Earth Sciences, vol. 61. Springer, Berlin.
Bulirsch, R., & Kraft, G. (eds). 1994. Computational Optimal Control. International
Series of Numerical Mathematics, vol. 115. Birkh ¨auser, Basel.
Bulirsch, R., Miele, A., Stoer, J., & Well, K.H. (eds). 1993. Optimal Control —
Calculus of Variations, Optimals Control Theory and Numerical Methods. In-
ternational Series of Numerical Mathematics, vol. 111. Birkh ¨auser, Basel.


262
REFERENCES
Burke, I.C., Schimel, D.S., Yonker, C.M., Parton, W.J., Joyce, L.A., & Lauenroth,
W. K. 1990. Regional modeling of grassland biogeochemistry using GIS. Land-
scape Ecology, 4(1), 45–54.
Cabelguenne, M., Debaeke, P., & Bouniols, A. 1999. EPICphase, a version of the
EPIC model simulating the effects of water and nitrogen stress on biomass and
yield, taking account of developmental stages: validation on maize, sunﬂower,
sorghum, soybean and winter wheat. Agricultural Systems, 60, 175–196.
Chouikha,M.1999. Designofdiscrete-continouscontrolsystems,modelling,analysis
and synthesis by hybrid Petri nets. German Engeneering Society, Series, vol.
797. VDI, D¨usseldorf.
Chouikha, M., & Schnieder, E. 1998. Modelling continuous-discrete systems with
hybrid Petri nets. Pages 606–612 of: IEEE-MC Multiconference on Computa-
tional Engineering in Systems Applications.
Clark, C.W. 1976. Mathematical Bioeconomics. John Wiley & Sons, New York.
Clark, C.W., Clarke, F.H., &Munro, G.R.1979.Theoptimalexploitationofrenewable
resource stocks: problems of irreversible investment. Econometrica, 47(1), 23–
47.
Cohen, Y. 1987a. Application of optimal impulse control to optimal foraging prob-
lems. Lecture Notes in Biomathematics, 73, 39–52.
Cohen, Y. 1987b. Optimal reproductive strategies in annual plants. Lecture Notes in
Biomathematics, 73, 19–37.
Comsol AB. 2001. FEMLAB User and Reference Manual.Tegn ´ergatan 23,SE–11140
Stockholm, Schweden.
Congleton, W.R., Pearce, B.R., & Beal, B.F. 1997. A C++ implementation of an
individual/landscape model. Ecological Modelling, 103, 1–17.
Cornwell, C.F., Wille, L.T., Wu, Y., & Sklar, F.H. 2001. Parallelization of an eco-
logical landscape model by functional decomposition. Ecological Modelling,
144, 13–20.
Costanza, R.1989. Modelgoodnessofﬁt: amultipleresolutionprocedure.Ecological
Modelling, 47, 199–215.
Costanza, R. 2000. Social goals and the valuation of ecosystem services. Ecosystems,
3, 4–10.
Costanza, R., & Maxwell, T. 1991. Spatial ecosystem modelling using parallel pro-
cessors. Ecological Modelling, 58, 159–183.
Costanza, R., & Voinov, A. 2001. Modeling ecological and economic systems with
STELLA: Part III. Ecological Modelling, 143, 1–7.


REFERENCES
263
Costanza, R., Sklar, F.H., & White, M.L. 1990. Modeling coastal landscape dynamics.
Bioscience, 40(2), 91–107.
Costanza, R., Wainger, L., Folke, C., & M¨aler, K.-G. 1993. Modeling complex
ecological economic systems. Bioscience, 43(8), 545–555.
Costanza, R., d’Arge, R., deGrot, R., Farber, S., Grasso, M., Hannon, B., Limburg,
K., Naeem, S., O‘Neill, R.V., Paruelo, J., Raskin, R.G., Sutton, P., & van den
Belt, M. 1997. The value of the world’s ecosystem services and natural capital.
Nature, 387, 253–260.
Costanza, R., Voinov, A., Boumans, R., Maxwell, T., Villa, F., Wainger, L., & Voinov,
H. 2001. Case Study: Patuxent River Watershed, Maryland. Boca Raton, Lewis.
Pages 179–232.
Cressie, N.A.C. 1991. Statistics for Spatial Data. New York: John Wiley & Sons
Inc.
Curtiss, P.S., & Rabl, A. 1996. Impacts of air pollution: general relationships and
site dependance. Atmospheric Environment, 30(19), 3331–3347.
Davis, J.C. 1984. Statistical Data Analysis in Geology. New York: John Wiley &
Sons.
de Haes, U., & Owens, J.W. (eds). 1998. Evolution and development of conceptual
framework and methodologyof life cycle impact assessment. Summary of SETAC
and SETAC-Europework groups on life cycle impact assessment. Pensacola, FL:
Society of Environmental Toxicology and Chemistry.
deGee, M., & Grasman, J. 1998. Sustainable yields from seasonally ﬂuctuating
biological populations. Ecological Modelling, 109, 203–212.
Deutsch, C.V., & Journel, A. G. 1992. GSLIB - Geostatistical Software Libary and
Users Guide. New York: Oxford University Press.
Diekkr¨uger, B., & Arning, M. 1995.
Simulation of water ﬂuxes using different
methods for estimating soil parameters. Ecological Modelling, 81, 83–96.
Diekkr¨uger, B., N¨ortersh¨auser, P., & Richter, O. 1995. Modeling pesticide dynamics
of loam site using HERBSIM and SIMULAT. Ecological Modelling, 81, 111–
120.
Diekmann, O., VamGils, S.A., Lunel, S.M.V., & Walther, H.O. 1995. Delay Equa-
tions: Functional-, Complex-, and Nonlinear Analysis. New York: Springer.
Doherty, J. 1994. PEST — Model-Independent Parameter Estimation. Corinda,
Australia: Watermark Computing.
Doherty Jr., P.F., Marschall, E.A., & Grubb Jr., T.G. 1999. Balancing conservation
and economic gain: a dynamic programming approach. Ecological Economics,
29(3), 349–358.


264
REFERENCES
Draper, N.R., & Smith, H. 1966. Applied Regression Analysis. New York: John
Wiley & Sons.
Ermentrout, G.B., & Edelstein-Keshet, L. 1993. Cellular automata approaches to
biological modelling. Journal of Theoretical Biology, 160, 97–133.
Ewing, B., Yandell, B.S., Barbieri, J.F., Luck, R.F., & Forster, L.D. 2002. Event-
driven competing risks. Ecological Modelling, 158, 35–50.
Eyre, S.R. 1968. Vegetation and Soils - A World Picture. London: Edward Arnold
Ltd.
Falkovitz, M.S., & Feinerman, E. 1994. Minimum leaching scheduling of nitrogen
fertilization and irrigation. Bulletin of Mathematical Biology, 56(4), 665–686.
Fisher, B.E.A., & Smith, R. 1987. Expandingbox models for the long-rangetransport
of chemical reacting airborne material. Atmospheric Environment, 21(1), 195–
199.
Fitz, H.C., DeBellevue, E.B., Costanza, R., Boumans, R., Maxwell, R., Wainger, L.,
& Sklar, F.H. 1996. Development of a general ecosystem model for a range of
scales and ecosystems. Ecological Modelling, 88, 263–295.
Foley, P. 2000. Problems in extinction model selection and parameter estimation.
Environmental Management, 26, 55–73.
Formsgaard,I.S. 1997. Modelling the mineralization kinetics of low concentrations of
pesticides in surface and subsurface soil. Ecological Modelling, 102, 175–208.
Forrester, J.W. 1968. Principles of Systems. 2. edn. Fifth Printing.
Gallop´ın, G.C. 1997. Indicators and their use: information for decision-making.
Vol. 58 of (Moldan et al., 1997). Chap. 1, pages 13–27.
Gold, Chr.M., Remmele, P.R., & Ross, T. 1997. Voronoi Methods in GIS. Vol. 1340
of (van Kreveld et al., 1997). Chap. 2, pages 21–36.
Grennfelt, P., Eliassen, A., Hov, O., Berkovicz, R., & Nordlund, G. 1987. Atmo-
spheric Chemistry, Transport and Deposition of Nitrogen Oxides. Kopenhagen:
Working Group on Nitrogen Oxides within ECE’s Convention on Long-Range
Transboundary.
Gronewold, A., & Sonnenschein, M. 1998. Event-based modelling of ecological
systems with asynchronous cellular automata. Ecological Modelling, 108, 37–
52.
Gubbins, S., & Gilligan, C.A. 1996. Population dynamics of a parasite and hyperpar-
asite in a closed system: model analysis and parameter estimation. Proceedings
of the Royal Society of London, 263, 1071–1078.


REFERENCES
265
Guisan, A., & Zimmermann, N.E. 2000. Predictive habitat distribution models in
ecology. Ecological Modelling, 135, 147–186.
Gundersen, P. 1992. Mass balances approach for establishing critical loads for nitro-
gen in terrestrial ecosystems. Pages 55–109 of: Grennfelt, P., & Th ¨ornel¨of, E.
(eds), Critical Loads For Nitrogen — A Workshop Report. Kopenhagen: Nordic
Council of Ministers.
Gurney, W. S. C., Nisbet, R.M., & Lawton, J.H. 1983. The systematic formulation of
tractable single-species population models incorporating age-structure. Journal
of Animal Ecology, 52, 479–495.
Haag, D., & Kaupenjohann, M. 2001. Parameters, prediction, post-normal science
and the precautionary principle — a roadmap for modelling decision-making.
Ecological Modelling, 144, 45–60.
Hagen, A. 2003. Fuzzy set approach to assessing similarity of categorial maps.
International Journal of Geographical Information Science, 17(3), 235–249.
Hairer, E., & Wanner, G. 1980. Solving Ordinary Differential Equations. Vol. 2.
Springer–Verlag.
Hairer, E., Nørsett, S.P., & Wanner, G. 1980. Solving Ordinary Differential Equations.
Vol. 1. Springer–Verlag.
Haken, H. 1983. Advanced Synergetics. Springer–Verlag, New York.
Hall, C.A.S. 1988. An assessment of several of the historical most inﬂuencing theoret-
ical models used in ecology and of the data provided in their support. Ecological
Modelling, 43, 5–31.
Hargrove, W.W., Gardner, R.H., Turner, M.G., Romme, W.H., & Despain, D.G.
2000. Simulating ﬁre patterns in heterogeneous landscapes. Ecological Mod-
elling, 135, 243–263.
Harz, K. 1975. Die Orthopteren Europas. Vol. 2. The Hague: W. Junk.
Heller, U., & Struss, P. 1997. Conceptual Modelingin the EnvironmentalDomain. In:
Modellingand AppliedMathematics. 15th IMACS World Congress on Scientiﬁc
Computation, Berlin.
Henson, S.M. 1999. A continuos, age-structured insect population model. Journal
of Mathematical Biology, 39, 217–243.
Heuvelink, G.B.M. 1998. Uncertainty analysis in environmental modelling under a
change of spatial scale. In: Finke, P., Bouma, J., & Hoosbeek, M.R. (eds), Soil
and Water Quality at Different Scales. Kluwer.
Hoch, R., Gabele, T., & Benz, J. 1998. Towards a standard for documentation of
mathematical models in ecology. Ecological Modelling, 113(1–3), 3–12.


266
REFERENCES
Hof, J., &Bevers, M.1998.Spatialoptimizationformanagedecosystems.Complexity
in Ecological Systems. New York: Columbia University Press.
Hof, J., Sieg, C.H., & Bevers, M. 1999. Spatial and temporal optimization in habitat
placement for a threatened plant: the case of the western prairie fringed orchid.
Ecological Modelling, 115, 61–75.
Hulbert, L., Peterson, S., Wallis, J., & Richmond, B. 2000. Stella Research Software
Manual. Hanover, USA: MM High Performance System Inc.
Hunsaker, C., Graham, R., Turner, R.S., Ringold, P.L., Holdren, G.R., & Strickland,
T.C. 1993. A national critical loads framework for athmospheric deposition
effects assessment: II. deﬁning assessmend end points, indicatos, and functional
subrigions. Environmental Management, 17(3), 335–341.
Irwin, E.G., & Geoghegan, J. 2001. Theory, data, methods: developing spatially
explicit cconomic models of land use change. Agriculture, Ecosystems & Envi-
ronment, 85, 7–23.
ISO. 1997. International Standard 14040 - Environmental Mangement - Life Cycle
Assessment - Principles and Framework. International Organisation for Stan-
dardization, Brussels.
Jakeman, A.J., & Letcher, R.A. 2003. Integratedassessment and modelling: features,
principles and examples for catchment management. Environmental Modelling
& Software, 18, 491–501.
J´avor, A. 1995. Petri nets and AI in modelling and simulation. Mathematics and
Computers in Simulation, 39, 477–484.
Jørgensen, L.A., Jørgensen, S.E., & Nielsen, S.N. 2000. ECOTOX — Ecological
Modelling and Ecotoxicology. Amsterdam, The Netherlands: Elsevier Science
B.V.
Jørgensen, S.E. (ed). 1979. State-of-the-Art in Ecological Modelling. International
Society for Ecological Modelling.
Jørgensen, S.E., & Bendoricchio, G. 2001. Fundamentals of Ecological Modelling.
3rd edn. Development in Environmental Modelling, vol. 21. Amsterdam, The
Netherlands: Elsevier Science B.V.
Jørgensen, S.E., Mejer, H., & Nielsen, S.N. 1998. Ecosystem as self-organizing
critical systems. Ecological Modelling, 111, 261–268.
Kelly, J.R., & Harwell, M.A. 1989. Indicators of Ecosystem Response and Recovery.
New York: Springer-Verlag. Pages 9–35.
Kelpin, F.D.L., Kirkilinois, M.A., & Kooi, B.W. 2000. Numerical methods and
parameter estimation of a structured population model with discrete events in
life history. Journal of Theoretical Biology, 207, 217–230.


REFERENCES
267
Kishimoto, K. 1982. The diffusive Lotka–Volterra system with three species can have
a stable non-constant equilibrium solution. Journal of Mathematical Biology,
16, 103–112.
Kluwe, M., Krebs, V., Lunze, J., & Richter, H. 1995. Qualitative modelling based
on rules, Petri nets, and differential equations. Mathematics and Computers in
Simulation, 39, 485–489.
Knorrenschild, M., Lenz, R., Herderich, C., & Forster, E. 1996. UFIS: a database of
ecological models. Ecological Modelling, 86, 141–144.
Kolar, J. 1990. Stickstoffoxide und Luftreinhaltung - Grundlagen, Emissionen, Trans-
mission, Immissionen, Wirkungen. New York: Springer Verlag.
Krewitt, W., Mayerhofer, P., Truckenm ¨uller, A., & Friedrich, R. 1998. Application
of the impact pathway analysis in the context of LCA. International Journal of
LCA, 3(2), 86–94.
Kr¨uger, O., & Graßl, H. 1994. Unterst¨utzung der EMEP-Modellrechnungen: Eu-
ropaweite Deposition schwefel- und stickstoffhaltiger Verbindungen als Folge
der Emissionen von Schwefel, Stickoxiden und Ammoniak. Geesthacht: GKSS-
Forschungszentrum Geesthacht GmbH.
Krysanova, V., & Haberlandt, U. 2002. Assessment of nitrogen leaching from arable
land in large river basins. Part I. Simulation experiments using a process-model.
Ecological Modelling, 150, 255–275.
Krysanova, V., Meiner, A., Roosaare, J., & Vasilyev, A. 1989. Simulation modelling
of coastal waters pollution from agricultural watershed. Ecological Modelling,
49, 7–29.
Kuang, Y. 1993. Delay Differential Equations with Applications in Population Dy-
namics. San Diego: Academic Press.
Kurz, A.A., Beukema, J.J., Klenner, W., Greenough, J.A., Robinson, D.C.E., Sharpe,
A.D., & Webb, T.M. 2000. TELSA: The tool for exploratory landscape scenario
analysis. Computers and Electronics in Agriculture, 27, 227–242.
Kuusemets, V., & Mander, ¨U. 2002. Nutrient ﬂows and management of a small
watershed. Landscape Ecology, 17(1), 59–68.
Kuylensstierna, J.C.I., Cambridge, H., Cinderby, S., & Chadwick, M.J. 1995. Terres-
trial Ecosystem Sensitivity to Acidic Deposition in DevelopingCountries. Pages
2319–2324 of: Grennfeld, P., Rodhe, H., Th ¨ornel¨of, E., & Wisniewski, J. (eds),
Acid Reign ’95? 5th International Conference on Acidic Deposition: Science
& Policy. G¨oteborg: Kluwer Academic Publishers.
Levin, S.A. 2000. Multiple scales and the maintenance of biodiversity. Ecosystems,
3, 498–506.


268
REFERENCES
Levine, S.H. 2000. Products and ecological models. Journal of Industrial Ecology,
3(2–3), 47–63.
Li, X., Jongman, R., Xiao, D., Harms, W.B., & Bregt, A.K. 2002. The effect of
spatial pattern on nutrient removal of a wetland landscape. Landscape and
Urban Planning, 60, 27–41.
Lischke, H., Lotter, A.F., & Fischlin, A. 2002. Untangling a holocene pollen record
with forest model simulations and independent climate data. Ecological Mod-
elling, 150, 1–21.
Liu, L., & Du, S. 2003. A computationally efﬁcient particle-puff model for concen-
tration variance from steady releases. Environmental Modelling & Software, 18,
25–33.
Loague, K., & Green, R.E. 1991. Statistical and graphical methods for evaluating
solute transport models: overview and application. Journal of Contaminat Hy-
drology, 7, 51–73.
Loehle, C. 2000. Optimal control of spatially distributed process models. Ecological
Modelling, 131, 79–95.
Longley, P.A., Goodchild, M.F., Maguire, D.J., & Rhind, D.W. 2001. Geographic
Information Systems and Science. Chichester: Wiley & Sons, Ltd.
Lu, Y.-C., Daughtry, C., Hart, G., & Watkins, B. 1997. The current state of precision
farming. Food Review International, 13(2), 141–162.
Ludwig, B. 1998. Fuzzy logic applications in technologyassessment studies. Journal
of Intelligent and Fuzzy Systems, 6, 375–388.
Luria, M., David, T., & Peleg, M. 1985. Five year air quality trends in Jerusalem,
Israel. Atmospheric Environment, 19(5), 715–726.
MacArthur, R.H., & Wilson, E.O. 1963. An equilibrium theory of insular zoogeog-
raphy. Evolution, 17(4), 373–387.
MacDonald, N.1989.BiologicalDelaySystems: LinearStabilityTheory. Cambridge:
Cambridge University Press.
Makowski, D., Hendrix, E.M.T., van Ittersum, M.K., & Rossing, W.A.H. 2000. A
framework to study nearly optimal solutions of linear programming models
developed for agricultural land use exploration. Ecological Modelling, 131,
65–77.
Malard, F., Tocker, K., Dole-Oliver, M.-J., & Ward, J.V. 2002. A landscape perspec-
tive of surface-subsurfacehydrological exchanges in river corridors. Freshwater
Biology, 47, 621–640.


REFERENCES
269
Marsili-Libelli, S. 1992. Parameter estimation of ecological models. Ecological
Modelling, 62, 233–358.
Martinez-Falero, E., Trueba, I., Cazorla, A., & Alier, J. L. 1998. Optimization of
spatial allocation of agricultural activities. Journal of Agricultural Engineering
Resources, 69, 1–13.
Maxwell, T., & Costanza, R. 1997a. A language for modular spatio–temporal simu-
lation. Ecological Modelling, 103, 105–113.
Maxwell, T., & Costanza, R. 1997b. An open geographic modeling environment.
Simulation Journal, 68(3), 175–185.
McIntosh, B.S. 2003. Qualitative modelling with imprecise ecological knowledge: a
framework for simulation. Environmental Modelling & Software, 18, 295–307.
McVoy, C.W., Kersebaum, K.C., Arning, M., Kleeberg, P., Othmer, H., & Schr ¨oder,
U. 1995. A data set from north Germany for the validation of agroecosystem
models: documentation and evaluation. Ecological Modelling, 81, 265–300.
Moldan, B., Billharz, S., & Matravers, R. 1997. Sustainability Indicators. Scientiﬁc
Commitee on Problems of the Environment — SCOPE, vol. 58. John Wiley &
Sons.
Mualem, Y. 1976. A new model for predicting the hydraulic conductivity of unsatu-
rated porous media. Water Resources Research, 12, 513–522.
Muetzelfeld, R., & Massheder, J. 2003. The Simile visual modelling environment.
European Journal of Agronomy, 18, 345–358.
M¨uller, F. 1997. State-of-the-art in ecosystem theory. Ecological Modelling, 100,
135–161.
M¨uller, F. 1998. Gradients in ecological systems. Ecological Modelling, 108, 3–21.
Naiman, R.J., & D´camps, H. 1997.
The ecology of interfaces: riparian zones.
Annu. Rev. Ecol. Syst., 28, 621–658.
Naveh, Z., & Lieberman, A.S. 1984. Landscape Ecology. Springer, New York.
Nevo, A., & Garcia, L. 1996. Spatial optimization of wildlife habitat. Ecological
Modelling, 91, 271–281.
Niesel-Lessenthin, B. 1988. Faustzahlen f¨ur Landwirtschaft und Gartenbau. 11. edn.
Landwirtschaftsverlag, M¨unster.
Nievergelt, J., & Widmayer, P. 1991. Spatial data structures: concepts and design
choices. Vol. 1340 of (van Kreveld et al., 1997). Chap. 6, pages 153–197.


270
REFERENCES
Nilsson, J. 1986. Summary and Conclusions. Pages 6–32 of: Critical Loads for Ni-
trogen and Sulfur — Report from a Nordic Working Group. Stockholm: Nordisk
Ministerrad.
Nilsson, J., & Bergstr¨om, S. 1995. Indicators for the assessment of ecological and
economic consequences of municipal policies for resource use. Journal of Eco-
logical Economics, 14, 175–184.
Nisbet, R.M., & Gurney, W.S.C. 1983. The systematic formulation of population
models for insects with dynamically varying instar duration. Theoretical Popu-
lation Biology, 23, 114–135.
Novozhilov, K.V., Petrova, T.M., Semenova, N.N., & Solomina, T.V. 1995. Modeling
of foliar uptake and degredationof pesticides using crop growth model. Archives
of Phytopathology and Plant Protection, 30, 165–181.
Noy-Meir, I., & Harpaz, Y. 1977. Agro-ecosystems in Israel. Agro-Ecosystems, 4,
143–167.
Odum, H.T. 1983. Systems Ecology: An Introduction. John Wiley & Sons, New
York.
Opdam, P., Foppen, R., & Vos, C. 2002. Bridging the gap between ecology and
spatial planning in landscape ecology. Landscape Ecology, 16, 767–779.
Oreskes, N., Shrader-Frechette, K., & Belitz, K. 1994. Veriﬁcation, validation, and
conﬁrmation of numerical models in earth sciences. Science, 263, 641–646.
Owens, J.W. 1996. LCA impact assessment categories — technical feasibility and
accuracy. International Journal of LCA, 1(3), 151–158.
Pahl-Wostl, C. 1995. The Dynamic Nature of Ecosystems. John Wiley & Sons.
Pattanayak, S.K., & Kramer, R.A. 2001. Pricing ecological services: willingness
to pay for drought mitigation from watershed protection in eastern Indonesia.
Water Resources Research, 37(3), 771–778.
Plentiger, M.C., & de Vries, F.W.T. Penning (eds). 1997. Rotation Model for Ecolog-
ical Farming. Wageningen, Netherlands: PE and AB-DLO, for CAMASE/PE
Workshop Report, Quantitative Approaches in System Analysis No. 10.
Plentinger, M.C., & de Vries, F.W.T. Penning. 2001.
CAMASE Register of
Agroecosystems Models.
URL: http://www.bib.wau.nl/camase/
srch-cms.html. May, 2003.
Pohl, C., Ros, M., Waldeck, B., & Dinkel, F. 1996. Imprecision and Uncertainity in
LCA. Birkh¨auser Verlag. Pages 51–68.
Pollex, A., Krug, D., McVoy, C.W., Sponagel, H., Diekk ¨uger, B., & Richter, O.
1995. Soil–water behaviour in a push terminal moraine: comparison of one-


REFERENCES
271
and two-dimensional simulations based on intensive regional ﬁeld observations.
Geoderma, 69, 249–263.
Posch, M. 1993. Guidelines for the Computation and Mapping of Critical Loads and
Exceedances of Sulphur and Nitrogen in Europe. Bilthoven CoordinationCenter
for Effects - National Institute of Public Health and Environmental Protection.
Pages 25–38.
Press, W.H., Flannery, B.P., Teukolsky, S.A., & Vetterling, W.T. 1988. Numerical
Recipes in C. Cambridge: Cambridge University Press.
Randhir, T.O., Lee, J.G., & Engel, B. 2000. Multiple criteria dynamic spatial opti-
mizationtomanagewaterqualityonawatershedscale.TransactionsofAmerican
Society of Agricultural Engineers, 43(2), 291–299.
Rao, M.N., Waits, D.A., & Neilsen, M.L. 2000. A GIS-based modeling approach
for implementation of sustainable farm management practices. Environmental
Modelling & Software, 15, 745–753.
Richter, O. 1998. Pesticides, Environmental Fate. John Wiley & Sons, Inc. Pages
3484–3505.
Richter, O., & S¨ondgerath, D. 1990. Parameter Estimation in Ecology. VCH, Wein-
heim.
Richter, O., Spickermann, U., & Lenz, F. 1991. A new model for plant growth.
Gartenbauwissenschaft, 56(3), 99–106.
Richter, O., Diekkr¨uger, B., & N¨ortersheuser, P. 1996. Environmental Fate Modelling
of Pesticides. VCH Verlagsgesellschaft, Weinheim.
Richter, O., Seppelt, R., & S¨ondgerath, D. 2001. Computer modeling. Encyclopedia
of Envirometrics, 1, 402–411.
Rodrigo, R.D., & Nicholls, M.G. 1998. Modelling real world industrial systems: an
inter-disciplinary approach based on Petri nets. Mathematics and Computers in
Simulation, 44, 587–597.
Russell, A.G. 1988. Mathematical Modelling of the Effect of Emission Sources on
Atmospheric Pollutant Concentrations. Washington D.C.: National Academy
Press. Pages 161–206.
Sadler, E.J., Busscher, W.J., Bauer, P.J., & Karlen, D.L. 1998. Agronomic models.
Spatial scale requirementsfor presision farming: a case study in the southeastern
USA. Agronomy Journal, 90, 191–197.
Salski, A. 1992. Fuzzy knowledge-based models in ecological research. Ecological
Modelling, 63, 103–112.


272
REFERENCES
Sanders, G.E., Sk¨arby, L., Ashmore, M.R., & Fuhrer, J. 1995. Establishing critical
levels for the effects of air pollution on vegetation. Water, Air and Soil Pollution,
85(1), 189–200.
Sasowsky, C.K., & Gardner, T.W. 1991. Watershed conﬁguration and geographic
information system parameterization for SPUR model hydrologic simulations.
Water Resources Bulletin, 27(1), 7–18.
Savill, N.J., & Hogeweg, P. 1999. Competition and dispersal in predator–preywaves.
Theoretical Population Biology, 56, 243–263.
Scheffer, M., Brock, W., & Westlay, F. 2000. Socioeconomicmechanisms preventing
optimum use of ecosystem services: an interdisciplinary theoretical analysis.
Ecosystems, 3, 451–471.
Schellnhuber, H.-J. 1998. Earth System Analysis — The Scope of the Challenge.
Chap. 1, pages 3–182 of: Schellnhuber, H.-J., & Wenzel, V. (eds), Earth System
Analysis. Springer, Berlin.
Schittkowski, K. 1980. Nonlinear Programming Codes. Lecture Notes in Economics
and Mathematical Systems, vol. 183. Heidelberg: Springer.
Schittkowski, K. 1983. On the convergence of a sequential quadratic programming
method with an augmented Lagrangian search direction. Mathematische Oper-
ationsforschung und Statistik, 14, 197–216.
Schittkowski, K. 1994.
Parameter estimation in systems of nonlinear equations.
Numerische Mathematik, 69, 129–142.
Schmidt, K., Sikora, R.A., & Richter, O. 1993. Modelling the population dynamics
of the sugar beet cyst nematode Heterodera schachtii. Crop Protection, 12(7),
490–496.
Schraut, B.K. 2001. Degradation of Sulfonyl Urea Herbicide Idosulfuron–Methyl-
Natrium and Metsulfuron-Methyl in Soil and Soil Solute: Inﬂuence of Different
ParametersandMathematicalModels. Ph.D.thesis, Georg–August–Universit ¨at,
G¨ottingen. In German.
Schr¨oder, U., & Richter, O. 1993. Parameter estimation in plant growth models at
differentlevelsofaggregation.ModellingGeo-BiosphereProcesses,2, 211–226.
Schr¨oder, U., & S¨ondgerath, D. 1995. The concept of biological time for computing
the switching points of a growth model for winter wheat. Ecological Modelling,
88, 1–8.
Schr¨oder, U., Richter, O., & Velten, K. 1995. Performanceof the plant growth models
of Special Collaborative Project 179 with respect to winter wheat. Ecological
Modelling, 81, 243–250.


REFERENCES
273
Seber, G.A.F., & Wild, C.J. 1989. Nonlinear Regression. New York: John Wiley &
Sons.
Seinfeld, J.H., & Pandis, S.N. 1998. Atmospheric Chemistry and Physics: From Air
Pollution to Climate Change. New York: John Wiley & Sons.
Seppelt, R. 1997. Strategies for sustainable agriculture: applicationof control theory
to long term bio-economic processes. Landscape Ecology and Environmental
Research, vol.26.InstitutofGeoecology, TechnicalUniversityofBraunschweig.
In German.
Seppelt, R. 1999. Applications of optimum control theory to agroecosystem mod-
elling. Ecological Modelling, 121(2–3), 161–183.
Seppelt, R. 2000. Regionalised optimum control problems for agroecosystem man-
agement. Ecological Modelling, 131(2–3), 221–232.
Seppelt, R. 2001. Hierarchical dynamic programming and applications in ecosystem
management. Environmental Modelling & Software, 16(3), 377–386.
Seppelt, R. 2003. TSEO: toolbox for spatially explicit optimization. URL: http://
www.tu-bs.de/institute/igg/ag-aus/forsch/optlu/.
May,
2003.
Seppelt, R., & Temme, M.-M. 2001. Hybrid low level Petri nets in environmental
modelling: development platform and case studies.Pages 181–200 of: Matthies,
M., Malchow, H., & Kriz, J. (eds), Integrative Systems Approaches to Natural
and Social Sciences. Springer.
Seppelt, R., & Voinov, A. 2002. Optimization methodology for landuse patterns using
spatially explicit landscape models. Ecological Modelling, 151(2–3), 125–142.
SETAC. 1993. A Conceptual Framework for Life-Cycle Impact Assessment. Pen-
sacola: Society of Environmental Toxicology and Chemistry.
SETAC (ed). 1993. Guidelines for Life Cycle Assessment: A "Code of Practice" -
From the SETAC Workshop held at Sesimbra, Portugal 31 March - 3 April 1993.
Br¨ussel: Society of Environmental Toxicology and Chemistry Europe.
SETAC. 1997.
Life-Cycle Impact Assessment: The State-of-the-Art. Pensacola:
Society of Environmental Toxicology and Chemistry.
Simpson, D., Perrin, D.A., Varey, J.E., & Williams, M.L. 1990. Dispersion modelling
of nitrogen oxides in the united kingdom. Atmospheric Environment, 24A(7),
1713–1733.
Sklar, F.H., Costanza, R., & Jr., J.W. Day. 1985. Dynamicspatial simulation modeling
on coastal wetland habitat succession. Ecological Modelling, 29, 261–281.


274
REFERENCES
Soetart, K., deClippele, V., & Herman, P. 2002. FEMME, a ﬂexible environment for
mathematically modelling the environment. Ecological Modelling, 151, 177–
193.
Stoer, J., & Bulirsch, R. 1983. Introduction to Numerical Analysis. Springer–Verlag.
Strickland, R.M., Ess, D.R., & Parsons, A.D. 1998. Precision farming and precision
pest management: the power of new crop production technologies. Journal of
Nematology, 30(4), 431–435.
Struss, P., & Heller, U. 1998. Process-oriented modeling and diagnosis: revising and
extending the theory of diagnosis from ﬁrst principles. In: Working Notes of the
9th International Workshop on Principles on Diagnosis.
Stull, R.B. 1988.
An Introduction to Boundary Layer Meteorology.
Dordrecht:
Kluwer Academic Publisher.
Tarp, P., & Helles, F. 1997. Spatial optimization by simulated annealing and linear
programming. Scandinavial Journal of Forest Research, 12, 390–402.
Thiel, Chr., Seppelt, R., M¨uller-Pietralla, W., & Richter, O. 1999. An integrated
approach for environmental assessments. Linking and integrating LCI, environ-
mental fate models and ecological impact assessment. International Journal of
Life Cycle Assessment, 4(3), 151–160.
Thulke, H.-H., Grimm, V., M¨uller, M.S., Staubach, C., Tischendorf, L., Wissel, C., &
Jeltsch, F. 1999. From pattern to practice: a scaling-down strategy for spatially
explicit modelling illustrated by the spread and control of rabies. Ecological
Modelling, 117, 179–202.
Tietje, O., & Tapkenhinrichs, M. 1993. Evaluation of pedo-transfer functions. Soil
Science Society American Journal, 57, 1088–1095.
Tischendorf, L. 1997. Modelling individualmovementsin heterogeneouslandscapes:
potentials of new approach. Ecological Modelling, 103, 33–42.
Tolle, D.A. 1997. Regional scaling and normalizationin LCIA. InternationalJournal
of LCA, 2(4), 197–208.
Tuljapurkar, S., & Caswell, H. (eds). 1997. Structured-populationModels in Marine,
Terrestrial, andFreshwaterSystems. PopulationandCommunityBiologySeries.
New York: Chapman & Hall.
Turner, M.G., Gardner, R.H., & O’Neill, R.V. 2001. Landscape Ecology in Theory
and Practice. Pattern and Process. New York: Springer.
Tyre, A.J., Possingham, H.P., & Lindenmayer, D.B. 2001. Inferring Process from
Pattern: Can Territory Occupancy Provide Information About Life History Pa-
rameters? Ecological Applications, 11(6), 1722–1737.


REFERENCES
275
Umgiesser, G., Canu, D.M., Solidoro, C., & Ambrose, R. 2003. A ﬁnite element eco-
logical model: a ﬁrst application of the Venice lagoon. EnvironmentalModelling
& Software, 18, 131–145.
United States Environmental Protection Agency. 1995 (April). Conceptual Frame-
work to Support Development and Use of Environmental Informationin Decision
Making. Document Number 239-R-95-012, Washington, DC.
Usery, E.L., Pocknee, S., & Boydell, B. 1995. Precision farming data management
usinggeographicinformationsystems.PhotogrammetricEngineering&Remote
Sensing, 61(11), 1383–1391.
USGS. 1995. Maryland NWIS-W Data Retrieval. Tech. rept. USGS. http://
waterdata.usgs.gov/nwis-w/MD.
USGS. 1997. Maryland Surface-Water Data Retrieval. Tech. rept. USGS. http:
//h20.usgs.gov/swr/MD.
van Dyne, G.M., Fayer, W.E., & Bledsoe, L.J. 1970. Some Optimization Techniques
and Problems in Natural Ressource Sciences. Pages 95–124 of: Symposium on
Optimization, Philadelphia.
van Genuchten, M.Th. 1980. A closed-form equation for predicting the hydraulic
conductivity of unsaturated soils. Soil Science Society of American Journal, 44,
892–898.
van Kreveld, M., Nievergelt, J., Roos, Th., & Widmayer, P. (eds). 1997. Algorithmic
Foundations of Geographic Information Systems. Lecture Notes in Computer
Science, vol. 1340. Springer.
Velten, K., & Richter, O. 1993. Optimal maintenance investment of plants and its
dependence on environmental conditions. Bulletin of Mathematical Biology,
55(5), 953–971.
Velten, K., & Richter, O. 1995. Optimal root/shoot-partitioning of carbohydrates in
plants. Bulletin of Mathematical Biology, 57(1), 99–107.
Villa, F. 2001. Integrating modelling architecture: a declarative framework for multi-
paradigm, multi-scale ecological modelling. Ecological Modelling, 137, 23–42.
Vincent, T.L., & Skowronski, J.M. (eds). 1981. Renewable Resource Management.
Lecture Notes in Biomathematics, vol. 40. Springer–Verlag, Berlin.
Vink, J.P.M., N¨ortersheuser, P., Richter, O., Diekkr ¨uger, B., & Groen, K.P. 1994.
Modelling the microbial breakdown of pesticides in soil using a parameter esti-
mation technique. Pesticide Science, 40, 285–292.
Vogel, C. 2002. Spatially explicit model for population dynamics of Carabidae based
on habitat suitability. Landscape Ecology and Environmental Research, vol. 40.
Institut of Geoecology, Technical University of Braunschweig. In German.


276
REFERENCES
Voinov, A., Fitz, C., & Costanza, R. 1998. Surface water ﬂow in landscape models:
1. Everglades case study. Ecological Modelling, 108(1–3), 131–144.
Voinov,A., Voinov, H., & Costanza, R. 1999. Surface water ﬂow in landscape models:
2. Patuxent watershed case study. Ecological Modelling, 119(2–3), 211–230.
Voinov, A.A., Costanza, R., Wainger, L., Boumans, R., Villa, F., Maxwell, T., &
Voinov, H. 1999. Patuxent landscape model: integrating ecological economic
modelling of a watershed. Environmental Modelling & Software, 14, 473–491.
Volterra, V. 1927. Variazioni et ﬂuttuazioni del numero d’individui in specie animali
conviventi. R. Comitato Talassograﬁco Memoria, 131, 1–142.
Walker, A. 1997. ModelMaker. Oxford: Cherwell Scientiﬁc Publishing.
Wall, M. 1996. A C++ Library of Genetic Algorithm Components. Cambridge, USA:
Massachusets Institute of Technology, Mechanical Engineering Department.
Wang, Q.J. 1997. Using genetic algorithms to optimize model parameters. Environ-
mental Modelling & Software, 12(1), 27–34.
Weibel, R. 1997. Generalization of spatial data: principles and selected algorithms.
Vol. 1340 of (van Kreveld et al., 1997). Chap. 5, pages 99–152.
Williams, J.R., Dyke, P.T., & Jones, C.A. 1983. EPIC: a model for assessing the
effects of erosion on soil productivity. Pages 553–572 of: W.K. Laurenroth et
al. (ed), State-of-the-Art in Ecological Modeling. Elsevier, Amsterdam.
Winograd, M. 1997. Vertical and horizontal linkages in the context of indicators
of sustainable development. Vol. 58 of (Moldan et al., 1997). Chap. 2, pages
92–95.
Wolfert, H.P., Hommerl, P.W.F.M., Prins, A.H., & Stam, M.H. 2002. The forma-
tion of natural levees as a disturbance process signiﬁcant to the conservation of
riverine patures. Landscape Ecology, 17(Suppl. 1), 47–57.
Wolfram, S. 1999. Mathematica Book, 4th Edition. Cambridge University Press.
Woodbury, P.B., Beloin, R.M., Swaney, D.P., Gollands, B.E., & Weinstein, D.A.
2002. Using the ECLPSS software environment to build a spatially explicit
component-basedmodel of ozone effects on forest ecosystems. Ecological Mod-
elling, 150, 211–238.
Wu, J., & David, J.L. 2002. A spatially explicit hierarchical approach to modeling
complex ecological systems: theory and applications. Ecological Modelling,
153, 7–26.
Wu, J., & Hobbs, R. 2002. Key issues and research priorities in landscape ecology:
an idiosyncratic synthesis. Landscape Ecology, 17, 355–365.


REFERENCES
277
Wu, J., & Levin, S.A. 1997. A patch-based spatial modeling approach: conceptual
framework and simulation scheme. Ecological Modelling, 101, 325–346.
Wu, J., & Marceau, D. 2002. Modeling complex ecological systems: an introduction.
Ecological Modelling, 153, 1–6.
Yacoubi, S. El, Jai, A. El, Jacewicz, P., & Pausas, J.G. 2003. LUCAS: an original tool
for landscape modelling. Environmental Modelling & Software, 18, 429–439.
Yager, R.R., & Zadeh, L.A. 1992. An Introduction to Fuzzy Logic Applications in
Intelligent Systems. Boston: Kluwer Academic Publishers.
Zadeh, L.A. 1965. Fuzzy sets. Information and Control, 8, 338–353.
Zadoks, J.C., Chang, T.T., & Konzak, C.F. 1974. A decimal code for the growth of
cereals. Journal of Weed Research, 14, 415–421.
Zhang, Z., & Grifﬁth, D.-A. 1997. Developing user-friendly spatial statistical analysis
modules for GIS: an example using ArcVIEW. Computers, Environment and
Urban Systems, 21(1), 5–29.


Additional References
Web Resources
Additional resources to the material of this book may be obtained from the URL
http://www.wiley-vch.de/books/info/3-527-30732-X/.
Animation and Video Files
are available from the above noted URL, which
illustrate the spatially explicit simulations discussed in Chapters 3 and 6, see Figures
3.3 (p. 77), 3.7 (p. 82), 3.8 (p. 84), and 6.8 (p. 134).
Software and Libraries
The following software tools and numerical libraries are
currently available free of charge to educational and non-proﬁt organizations from
the above mentioned URL.
• The development platform for hybrid low level Petri nets (hPEN), see Section
5.3 (p. 115);
• The library for hierarchical dynamic programming (LibHDB),see Section9.2.3
(p. 180);
• The toolbox for spatially explicit optimization (TSEO), see Section 9.3.6 (p.
188).
Any publications of work based upon experiments that use the above mentioned
software must include a suitable acknowledgment.
279


280
REFERENCES
Copyrights and Sources
The aerial photography of the cover page was taken by Kircher & Wolf Consult
GmbH, Hildesheim, Germany. Reproduction is permitted by district administration
Braunschweig, Germany, No. BRG 50/428. It shows the northeast part of the in-
vestigation site with the small town Neuenkirchen in the right upper corner of the
picture.
Parts of Chapters 2, 8 through 12 are reprinted from (Seppelt, 1999; Seppelt, 2000;
Seppelt, 2001; Seppelt & Voinov, 2002) with permission from Elsevier, Ltd.
ResultsinthiscontributionswereobtainedusingtheGAlibgeneticalgorithmpackage,
written by Matthew Wall at the Massachusetts Institute of Technology (Wall, 1996).
Quotations
Introduction, page xvii Charles Lutwidge Dodgson (1832 – 1898) better known as
Lewis Carroll: Alice’s Adventures in Wonderland.
Part I, page 1 Augusta Ada Byron (1815 – 1852), was a woman ahead of her time.
For the next hundred years she would be known as the daughter of Lord Byron
the poet. Only in this century would she become known as the ﬁrst “computer
programmer”. This is her comment on the Analytical Engine designed (but
never built) by Charles Babbage.
Part II, page 97 Alan Alexander Milne (1882 – 1956). Chapter 6 of Winnie–the–
pooh . . . in which Eeyore has a birthday and gets two presents.
Part III, page 157 Berthold Brecht (1898– 1956): Three Penny Opera, 1931Berlin,
Schiffbauerdamm: Aye, make yourself a plan // They need you at the top! //
Then make yourself a second plan // Then let the whole thing drop.


Index
A
Adjacence matrix, 6
Age-structured population, 57, 60
Aggregated model, 19, 73, 84, 133
Analytic model, 19
Arrhenius law, 53
Assessment
environment, 162
life cycle, 137
Atmospheric transport, 145
Available energy, 167
B
Baseﬂow, 226, 236, 242
Biological time, 37
Black-box model, 5, 104
Boundary condition, 10–11, 76
Box-model, 65, 146
conceptualization, 5
transport, 145
Buffer zones, 252
Buffering capacity, 141, 151–152
Building block, 133
C
CA, 22
Calibration, 15
Cartographic modeling, 21
Cation exchange capacity, 152
CDE, 75, 78
Cellular automaton, 22, 90, 103, 112
Characteristic time, 7, 65, 176
Chesapeake Bay, 93, 221, 239
Coefﬁcient, 11
Complex model, 18–19
Complexity, 9
Computer ﬂow chart, 13
Conceptual model, 3, 103–104, 148
agroecosystem, 4, 35
insect life cycle, 4
Conﬁrmation, 14
Consistency, 101
Constraints, 10, 196
Context, 10
Control
problem, 160, 169
variable, 12, 20, 66, 160, 169
Convection dispersion equation, 75, 78
Correlation coefﬁcient, 17
Correlation matrix, 23
Crop growth, 36–37, 41, 43–44, 46, 48–50, 57–58,
123, 135, 208
Crop rotation, 193, 197, 201, 210, 213–214, 216
Cross-validation, 16
D
DAE, 9
281


282
INDEX
Darcy law, 74
DDE, 9
Dead Sea, 144
Delay differential equation, 9, 60
Development code, 124, 199
Development platform, 24, 115
Dispersal, 78
Distributed model, 19
Domain, 7–8, 14, 103
DP, 175
Driving force, 10
Dynamic programming, 174–175
E
EASYFIT, 33
ECOBAS MIF, 108
Ecosystem function, 167, 226, 239, 243, 251
Ecosystem service, 167, 221
Ecotope, 21, 85, 184, 214
Effective parameter, 19, 39, 53
Eigenvalue, 8, 177
Elbe river, 79, 91
Elementary landscape, 21
Endogenous pattern, 72, 83, 90, 243, 249, 253
Energy circuit diagram, 5
Energy norm, 168
Energy, 167
Entropy, 167
Environmental conditions, 141
Environmental
fate modeling, 138, 140
impact assessment, 138, 151
Eutrophication, 151–152, 223, 226
Event, 197
Exogenous pattern, 72, 76, 249
Expert system, 23
EXTEND, 28, 31
External costs, 166
External effects, 194, 196
F
Farmers’ income, 202
Feedback dynamics, 5
Feedback model, 65
FEMLAB, 26, 29
Fertilizer application, 193, 197–198, 233
Field capacity, 88, 208, 211, 233
Flux, 174
Focal level, 9, 221
Forcing function, 12, 160
Functional decomposition, 184
Fuzzy logic, 89, 141, 244
G
GA, 23
Gal´apagos archipelago, 128
General model equation, 102
Genetic algorithm, 23, 28, 32–33, 187, 233, 250
GIS, 21, 69, 71, 85–86, 93, 96, 129–131, 140, 188,
212, 233
Global optimum solution, 175
GLUE, 18
GME, 102
Goal function, 162, 224
Goodness of models, 14
Granularity, 7, 103, 248, 253
Grasshopper tracking, 133
Gravimetric potential, 75
Ground water, 91
H
Habitat suitability, 67, 78, 85, 128, 166
Habitat type, 93, 223
Harvest biomass, 198
HDP, 173, 177
HDS, 176
Hierarchical dynamic programming, 177
Hierarchical dynamic system, 176
Hierarchy, 176, 221
Holism, 101
Hunting Creek
model, 93, 239
river, 221
Hybrid model, 100, 123, 133, 138
Hydraulic conductivity, 75, 233
Hydraulic potential, 75
Hydrotope, 21
I
IMA, 109
Indicator, 160, 162, 203
Inﬁltration rate, 233
Initial condition, 11
Inner consistency, 101
Input/output model, 5
Integrated model, 20
Integrating modeling toolkit, 109
Interspeciﬁc competition, 39, 46
Intrinsic veriﬁcation, 14–15
Invariant property, 15, 117, 135, 251, 253
Island biogeography, 128
J
Jordan river, 152
L
Land use, 223, 226, 228, 242
optimal, 224
value, 226
LCA, 137
LCI, 137
LCIA, 137


INDEX
283
Life cycle assessment, 137
Life cycle inventory, 137–139, 143
Ljapunov diagram, 59
Local optimization criterion, 250
Local optimum control problem, 197
Lower Saxony, 40
Lumped model, 19
M
MADONNA, 28
Magnesium production, 144
Management model, 20
Map intersection, 85–87
MATHEMATICA, 25, 27
Mathematical heterogeneity, 24, 35, 100, 182
Mathematical model, 11
MATLAB, 25, 27, 108
Matrix model, 7, 57, 60
Matrix potential, 75
Meta-modeling, 105, 107, 117
Meta-population, 128
Michaelis–Menten function, 10, 49, 51
MML, 108
Model
aggregated, 19, 73, 84, 133
analysis, 14
analytic, 19
autonomous, 18, 90
black-box, 5
box-, 5
complex, 19
conceptual, 3
distributed, 19
documentation, 104, 117
efﬁciency, 17
general equation, 102
hybrid, 123, 133, 138
input/output-, 5
integrated, 20
language, 24, 110
mathematical, 11
matrix, 7, 57, 60
numerical, 19
picture-, 5
regionalized, 72, 208
rule-based, 13, 23, 142
spatially explicit, 72, 76, 80, 83, 95, 130, 221
support, 67
white-box, 5
word-, 5
MODELMAKER, 23, 28, 30
Modular modeling language, 108
Modularity, 29, 66
Monte Carlo analysis, 16, 18, 24, 104, 136, 185,
191, 221, 229
Moore neighborhood, 90
Most sustainable yield, 122, 159
MSY, 122
Multi-criteria optimization, 168
Multi-paradigm model, 100
N
NAPL, 74
Net primary production, 36, 226
Network, 5
Neuenkirchen, 40, 87, 208
Nitrogen loss, 166, 194, 198–199, 201, 213–214,
216–217, 224–225, 228
Nitrogen uptake, 88
Numerical model, 19
Nutrient cycle, 35, 51, 93, 209
O
O’Neill function, 37, 54, 124
ODE, 9
Open systems, 7, 194
Optimal policy, 174
Optimization, 160–161
general task, 169
global, 170
gradient-free, 32–33
hierarchical approach, 173
local, 170
regionalized task, 169
Optimum control, 161
Outer consistency, 101
Over-parameterization, 18
P
PAR, 39
Parameter, 11
effective, 39, 53
estimation, 15, 23–24, 39, 41, 44, 53, 124
PARFIT, 33
Particle tracking, 132
Pattern
endogenous, 72, 83, 90, 243, 249, 253
exogenous, 72, 76, 249
Patuxent landscape model, 93, 248
Patuxent river, 93, 221, 239, 248
PDE, 9
Performance criterion, 161–163, 166, 168, 174,
183, 195, 226, 243
Pest control, 193, 217
Pest infestation, 55, 200
Pesticide application, 53, 197
Pesticide degradation, 52, 54
Pesticide loss, 194
Petri net, 112, 119
development platform, 115
spatially explicit, 130
Photosynthesis, 36, 124


284
INDEX
Photosynthetically-active radiation, 39–40, 48
Picture model, 5
Plant damage, 151
Population dynamics, 55, 78, 112, 117, 119, 132,
209, 216
Population index, 90
Porosity, 74, 233
POWERSIM, 28, 30
Precision farming, 207
Predator–prey model, 60, 82, 118–119
Predictive power, 14, 16, 49
Q
Q-stage process, 174
Qualitative reasoning, 16
R
Raster data, 21, 70
Reductionism, 101
Regionalization, 21, 72, 85, 87, 207
Regionalized model, 72, 208
Regionalized optimization, 169
Regression, 23
REM, 105
Representative elementary volume, 74
Research model, 20
Residual sum of squares, 17
Retention capability, 226
REV, 74
Richards equation, 74
RK, 18
Rooting depth, 211
Rule-based model, 13, 23, 142
Runge–Kutta formulae, 18, 31, 120, 180
S
Sandau, 79, 90
SAS, 23
Scale, 7, 103, 176
invariance, 253
spatial, 8
temporal, 7, 176
Scenario analysis, 12, 16, 159, 161–162
Scheyern, 40
Sensitivity analysis, 15–16, 18, 24, 59, 190, 236
SETAC, 137
Signed digraph, 5
Silver polygons, 87
SIMILE, 26, 30
SIMULINK, 29, 31, 108
Site-speciﬁc management, 207
Slavery principle, 176
Slope, 233
SME, 26, 29
Soil
acidiﬁcation, 151
saturated, 93
unsaturated, 69, 73, 93
Spatial modeling environment, 26, 29, 108, 185,
188, 190, 228
Spatial scale, 7–8, 221
Spatially explicit model, 72, 76, 80, 83, 95, 130,
221
Spectrum, 8, 177
SPSS, 23
State variable, 10
STELLA, 28, 30, 108
Stepping stones, 128, 136
Stiffness, 8, 31
Support, 19, 21, 68, 74, 85
System
analysis, 2–3, 15, 66, 120
boundary, 7, 12, 20, 166
openness, 7, 166, 194
stiff, 8
unintended behavior, 66, 120
T
Temporal scale, 7, 176, 197
Tessellation, 87, 211
Test data, 15, 49
Topology, 5–6, 15
Training data, 15, 49
Transfer function, 23
TSEO, 188
U
UFIS, 105
Uncertainty, 17–18, 65, 139, 141, 164
UNCSAM, 18
Unsaturated soil zone, 68, 73–74, 91–92
V
Validation, 14, 93
Variable
control, 12, 20, 66, 160, 163, 169
state, 10
Vector data, 21, 71, 207, 210
VENSIM, 29, 31
Veriﬁcation, 14
of development tools, 24
VonNeuman neighborhood, 90
W
Water content, 74–75
Water ﬂow model, 12
Weed growth, 39, 46
White-box model, 5
Wolfsburg, 138, 144
Word model, 5
