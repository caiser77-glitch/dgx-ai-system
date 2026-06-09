--- 
source: Landscape responses of the Siberian Flaying squirrel in Notrthern Finland.pdf
--- 

LANDSCAPE RESPONSES OF 
THE SIBERIAN FLYING 
SQUIRREL (PTEROMYS VOLANS) 
IN NORTHERN FINLAND
The effect of scale on habitat patterns and species incidence
PASI
REUNANEN
Department of Biology,
University of Oulu
OULU 2001


PASI REUNANEN
LANDSCAPE RESPONSES OF THE 
SIBERIAN FLYING SQUIRREL 
(PTEROMYS VOLANS) IN NORTHERN 
FINLAND
The effect of scale on habitat patterns and species 
incidence
Academic Dissertation to be presented with the assent of
the Faculty of Science, University of Oulu, for public
discussion in Kuusamonsali (Auditorium YB210),
Linnanmaa, on October 12th, 2001, at 12 noon.
OULUN YLIOPISTO, OULU 2001


Copyright © 2001
University of Oulu, 2001
Manuscript received 14 September 2001
Manuscript accepted 20 September 2001
Communicated by
Professor Thomas C. Grubb, Jr.
Ass. Professor Per Angelstam
ISBN 951-42-6496-7
(URL: http://herkules.oulu.fi/isbn9514264967/)
ALSO AVAILABLE IN PRINTED FORMAT
ISBN 951-42-6495-9
ISSN 0355-3191
(URL: http://herkules.oulu.fi/issn03553191/) 
OULU UNIVERSITY PRESS
OULU  2001


Reunanen, Pasi, Landscape responses of the Siberian flying squirrel (Pteromys volans)
in northern Finland  The effect of scale on habitat patterns and species incidence
Department of Biology, University of Oulu, P.O.Box 3000, FIN-90014 University of Oulu, Finland 
2001
Oulu, Finland
(Manuscript received 14 September 2001)
Abstract
Spatial structure of habitats has been found to affect the species  abundance and distribution patterns
in heterogeneous environments. In this  thesis, I studied landscape responses of the Siberian flying
squirrel in a  boreal forest context in northern Finland. Studies were conducted at  several spatial
scales in order to identify landscape characteristics that  are associated with the species occurrence at
a local scale and its  distribution patterns at a regional scale. Data on species presence and  absence
in forest areas were collected in the field. Habitat patterns in  landscapes were analysed from satellite
images and landscape metrics  concerning landscape structure were quantified in Geographic
Information  Systems (GIS).
Results of this study are in agreement with the general landscape  ecological theory and findings
in the field. In northern Finland, the  distribution of the Siberian flying squirrel primarily follows the
spatial  extent of spruce-dominated forests but that its actual occurrence is  dependent on the scale of
observation and the habitat structure. At a home  range scale the abundance of deciduous trees in old
spruce forest  increases the probability that a forest site is occupied by the species,  whereas at a local
scale the amount of such spruce forests and linkages  between habitat patches play an important role.
At a regional scale, an  increase in open areas and the dominance of pine makes the habitat  unsuitable
and restricts the presence of the species.
Findings of the present research forward practical forest management  planning at a large scale
and may help set general conservation goals for  the Siberian flying squirrel. When managing the
species in a complex  network of habitat patches in heterogeneous landscapes, spatial dispersion  of
potential habitat patches as well as connecting habitat and their  temporal development should be
considered carefully. For this purpose,  remote sensed images and GIS are valuable and useful tools.
Satellite-image based landscape analysis is presently developing rapidly  and hopefully this
methodology will soon become a common practice in  landscape ecological research and everyday
forest management planning.
Keywords: landscape ecology, remote sensing, GIS


Step by step 
up summer mountain −  
suddenly the sea 
− Kobyashi Issa 


 Acknowledgements 
First of all, I have to mention that this thesis is not a result of a long and lonely work in 
an ivory tower but rather a product of collaboration and interactions among many people. 
My task was to elaborate ideas, develop suggestions, implement recommendations 
presented by these people and, of course, formulate all this in a scientific way in order to 
communicate with other researchers in the field. Unfortunately, I am not able to thank 
everybody personally in this connection, but I must refer to the ones who had a major 
contribution to realisation of my thesis.  
Mikko Mönkkönen was a key person in this process, not only as an advisor, but also as 
a friend. He inspired me to study the Siberian flying squirrel in old forests of northern 
Finland. By doing so, he opened me the gates to the realm of landscape ecology. This also 
formed a fruitful starting point for an intensive learning process and harmonious planning 
of research where all emergent problems were discussed equally. He had always time to 
eagerly discuss any idea I ever came up with although, I knew it very well, he was busy 
himself, too. What a burden I must have been sometimes.  
Ari Nikula’s support for my work was of crucial importance in many ways. First of all, 
he is a GIS expert and has excess to unique data bases that I was privileged to use with 
his patient help in my study. Secondly, I cannot help admiring his enthusiasm and interest 
in ecology and the readiness to apply the potential of the GIS tool in ecological questions. 
Ari never got too tired to motivate and encourage me. I always enjoyed long discussions 
on ecology and scientific issues we had. Also Vesa Nivala contributed significantly to 
more detailed spatial pattern analysis by coding sophisticated algorithms for any purpose 
I needed. His expertise and straightforward attitude was required to solve many 
programming problems in the course of the studies. 
I had the pleasure to work with three ambitious master students: Petri Suorsa, Satu 
Lampila, and Eija Hurme. During the long hours in the field with them we faced and 
worked out many practical problems together and answered unexpected questions. At the 
same time I had a good opportunity to learn a lot of new aspects from them I was not so 
familiar with before. They all have many individual qualities I wish I would also have. 
It is self-evident that social life is a fundamental part of ones everyday life and it very 
much contributes to the quality of life. Frequent interactions among friends and 
colleagues at the university and in the spare time have been essential fuel to me during 


 
 
these years. Jukka Forsman and Jouko Inkeröinen were the ones who helped me to 
orientate in the world of research. Their assistance in the field and outside office hours 
has been irreplaceable. Mari Katvala, Claudia Siffczyk, Lluís Brotons, Folmer Bokma, 
and Eduardo Belda have regularly followed my undertakings during these years. We have 
shared an office, coffee breaks (often pretty long ones), worries, discussions on what so 
ever issue etc. These jolly fellows and their humorous attitude toward life (and me) made 
even the darkest winter day a delightful experience. The staff of the Zoo supplied me a 
big number of scientific devices such as traps and nestboxes to attract flying squirrels. I 
never had to compromise with them. They delivered the products what I ever ordered. 
Petri Kärkkäinen assisted me in the field under demanding winter conditions. When harsh 
temperatures (-38ºC) switched me (and the car) out of operation he kept rushing around 
after a distant signal in a dark, nocturnal winter forest. In all, people at the Department of 
Biology and more specifically at the Zoological Museum form a pleasant working 
community and facilities there provide an ideal and tranquil atmosphere for scientific 
work. 
During these years, I was accompanied by enormous many foreign exchange students 
in the field. This unusual opportunity gave the project an international flavour and 
enabled a regular and intensive interchange of culture, customs, and experiences. Their 
company made fieldwork feel like summer holidays or an excursion abroad. 
I need to mention especially two persons I had a delight to meet on my way. Aki 
Vanhala and Ralf Wistbacka participated in my projects unselfishly and without any 
financial demands. Their interest in flying squirrels and deep relationship to nature and its 
phenomena were the driving forces of their action day or night. I solemnly admire their 
working philosophy. I was lucky to meet them and I enjoyed every minute in their 
company. 
This study was partly financed by the Finnish Forest and Park Service. Major part of 
the funding was received from Maj and Tor Nessling Foundation. Our project was 
included in the Finnish Biodiversity Research Programme (FIBRE). A considerable 
financial support for an extensive field study was granted by EU’s Syöte-LIFE project. 
I want to thank and express my gratitude to all the persons who directly or indirectly 
contributed to my thesis or had any influence on my way to see landscape ecology in 
practise. I am indebted to my supervisors Mikko and Ari for their help, encouragement, 
and understanding. I thank all my friends, colleagues at the department, Aki and Ralf, 
people at the Zoo, as well as my foreign field helpers for their no matter big or small 
support and assistance. You were the most important of all. Bohdan Sklepkovych kindly 
revised and carefully edited the language in the introduction, for which he is cordially 
thanked. Finally, I thank the Finnish Forest and Park Service, Maj and Tor Nessling 
Foundation, and Syöte-LIFE project for providing me a solid financial basis for the 
period I needed to complete my thesis. 
 
Oulu September 2001 
 
 
 
 
 
     Pasi Reunanen


 List of original papers 
This thesis is based on the following publications, which are referred to in the text by 
their roman numerals. 
I  
Mönkkönen M, Reunanen P, Nikula A, Inkeröinen J & Forsman J (1997) Landscape 
characteristics associated with the occurrence of the flying squirrel Pteromys volans in 
boreal forests of northern Finland. Ecography 20: 634–642. 
II  Reunanen P, Mönkkönen M & Nikula A (2000) Managing boreal forest landscapes 
for flying squirrels. Conservation Biology 14: 218–226. 
III  Reunanen P, Nikula A & Mönkkönen M (2001) Regional scale landscape patterns 
and the distribution of the Siberian flying squirrel (Pteromys volans L.) in northern 
Finland. Manuscript (accepted). 
IV  Reunanen P, Mönkkönen M & Nikula A (2002) Habitat requirements of the Siberian 
flying squirrel in northern Finland: comparing field survey and remote sensing data. 
Annales Zoologici Fennici 39 (in press). 
V  Reunanen P, Mönkkönen M, Nikula A, Hurme E & Nivala V (2001) Predicting the 
occupancy of the Siberian flying squirrel in old-growth forest patches in northern 
Finland. Manuscript (submitted). 
Papers I, II and IV were reprinted with the kind permission from the publishers. 
Copyrights: 
I Nordic Ecological Society Oikos (Lund University, 223 62 Lund, Sweden) 
II Blackwell Science Ltd (Osney Mead, Oxford OX2 0EL, UK) 
IV Finnish Zoological and Botanical Publishing Board (POB 17, 00014 University of 
Helsinki, Finland) 
 


 Contents 
Abstract 
Acknowledgements 
List of original papers 
Contents 
1 Introduction....................................................................................................................13 
1.1 Landscape ecology − a developing discipline ......................................................... 13 
1.2 The domain of landscape ecology........................................................................... 13 
1.2.1 The appropriate level of observation: the dilemma of scale ........................... 14 
1.3 Theoretical and modelling approaches in landscape ecology.................................. 15 
1.4 Boreal forest landscape: the setting of the study..................................................... 17 
1.4.1 Human land use history and antropogenic landscape patterns........................ 18 
1.5 Siberian flying squirrel as a landscape ecological object........................................ 19 
1.6 Thesis objectives ..................................................................................................... 20 
2 Material and methods.....................................................................................................21 
2.1 Pellets on the ground − signature of the species presence....................................... 21 
2.1.1 Presence/absence data in ecological research................................................. 22 
2.2 Landscape pattern analysis in GIS .......................................................................... 22 
2.3 Landscape variables and statistical analysis of landscape data ............................... 23 
3 Results and discussion ...................................................................................................25 
3.1 Landscape structure around old-growth forest areas in Kainuu (I) ......................... 25 
3.2 Local scale habitat structure in Koillismaa (II) ....................................................... 26 
3.3 Distribution of the Siberian flying squirrel in northern Finland (III) ...................... 27 
3.4 Are large-scale landscape patterns visible at a home range scale? (IV) .................. 28 
3.5 Is the presence of the Siberian flying squirrel in a habitat patch predictable? (V).. 29 
4 Conclusions....................................................................................................................31 
4.1 Landscape structure and the Siberian flying squirrel .............................................. 31 
4.1.1 Spruce dominated forest patch: a basic landscape element for the Siberian 
flying squirrel in northern Finland........................................................................... 31 
4.1.2 Landscape connectivity at a local scale .......................................................... 32 
4.1.3 Landscape configuration of habitat patches.................................................... 33 
4.2 Spatial scaling for the Siberian flying squirrel........................................................ 34 


 
 
12
4.3 Theoretical aspects.................................................................................................. 34 
4.4 Management of the forest landscapes for the Siberian flying squirrel .................... 35 
5 Concluding remarks.......................................................................................................37 
References 
Original papers 


1 Introduction 
1.1  Landscape ecology − a developing discipline 
Short history of landscape ecology as an established discipline within ecological sciences 
dates back to the early 1980’s. The origin of the landscape ecology, however, is much 
older having its roots in long European tradition of land use planning, and practical 
organisation and sound exploitation of natural resources (Naveh 1982, Golley 1994). The 
concept of landscape ecology was adapted by American ecologists and soon after the 
field began to develop towards more ecologically-orientated phrasing of questions and 
methodologies typical of modern ecological research. Contrary to the applied and 
descriptive approach in the European tradition, the American approach focused on 
fundamental and conceptual details in landscape pattern and function. Additionally, in 
America landscape ecological research was directed to natural landscapes whereas in 
Europe landscape ecology had routinely stressed questions regarding human dominated 
and strongly modified environments (Hersberger 1994). 
1.2  The domain of landscape ecology 
Landscape ecology is an interdisciplinary branch of science that owes much to e.g. 
community ecology, biogeography, and population ecology. It grew on the coattails of 
conservation biology, but instead of focusing on single topics, such as small population 
problematics or insularization and area effect per se (e.g. Soulé 1980, 1985), landscape 
ecology directs attention toward issues of spatial characteristics in various environments 
and the scale of ecological processes in space and time. Landscape ecological studies 
attempt to define the interactions between organisms and their immediate environments, 
i.e. how ecological systems deal with spatial heterogeneity. The structure of habitat 
mosaics set constraints for living organisms. For instance, the availability of suitable 
habitat for breeding may be limited spatially, population interactions between adjacent 
areas or colonisation of entirely novel areas can be hindered by structural characteristics 


 
 
14
in the landscape. To what degree the physical structuring of a landscape (pattern) affects 
dynamic ecological interactions (process) in a complex landscape is the general question 
that landscape ecological research attempts to answer (Hansson 1977, Risser et al. 1984, 
Urban et al. 1987, Turner 1989, Pickett & Cadenasso 1995). 
The basic concepts in landscape ecology are structure, function, and change. Structure 
refers to the spatial characteristics of the landscape elements and function denotes the 
ecological processes that take place in that space. Landscape change implies the temporal 
dimension of the space and, thus, the continuous dynamic development in spatial 
structure and function in time (Forman 1995). Landscape structure is further divided into 
composition, configuration, and connectivity, which determine the structural 
characteristics of the space in more detail (Taylor et al. 1993, Merriam 1995, Bennet 
1998). Composition describes the proportion of qualitatively different landscape elements 
in space without any reference to their location. Comparatively configuration explicitly 
locates landscape elements in a spatial context and fixes the location and dimension of 
one element with respect to all other elements (Kozová 1983, Dunning et al. 1992). 
Connectivity characterises processes in a landscape that contribute to a functional 
demographic unit (Merriam 1984). Thus, landscape connectivity depends on the 
composition and configuration of landscape elements but, also, on an organism’s ability 
to perceive and discriminate between landscape elements and cross boundaries when 
selecting habitat for breeding or dispersing among preferred landscape elements (Wiens 
et al. 1985, Stamps et al. 1987, Addicot et al. 1987, Hansen & di Castri 1992, Zollner 
2000). 
Heterogeneous landscapes constitute habitats having different qualities and ecological 
properties. According to these characteristics they can be structured as habitat patches 
(Forman 1995). Habitat patches are homogenous areas that comprise similar ecological 
properties and deviate in this respect from adjacent habitat patches or the surrounding 
habitat i.e. the landscape matrix (Forman & Godron 1981). The number and 
characteristics of landscape elements in space are basically determined by regional 
climatic conditions and underlying edaphic factors (Wiens et al. 1985, Zonneveld 1989). 
A third landscape element that is often included in landscape ecological examination is 
the consideration of landscape corridors. Corridors are distinct strips of particular habitat 
that link other habitat patches in space. However, the concept of ecological corridors can 
be included in landscape connectivity i.e. as a probability that an individual will traverse 
the space between habitat patches and colonise habitat patches in a landscape (Taylor et 
al. 1993, Bennet 1998). Population responses to heterogeneous mosaics of landscape 
elements result from species-specific habitat affinities (e.g. habitat selection and dispersal 
abilities) that can either be invariable throughout the life-history of an individual or 
variable when certain habitat is required only during one particular stage of a life-cycle 
(Wiens 1976, Haila 1990, Pearson et al. 1996, Andrén et al. 1997). 
1.2.1  The appropriate level of observation: the dilemma of scale 
Ecological characteristics of a habitat patch do not solely determine the ecological state 
and dynamics of a single patch, but processes and interactions between other habitat 


 
 
15
patches in the surrounding environment may also influence its state. This dynamic and 
the influence of larger areas on local conditions imply the importance of the scale and 
scale-dependence in ecological phenomena. Scale is characterised by invariable patterns 
and processes within the extent of a particular scale. Changes and increasing variation in 
pattern and processes indicate the transition from one domain of a scale to another 
(Wiens 1989, Haila 1990, Bellehumeur & Legendre 1998). In general, for animal 
ecological studies, usually three domains of scale are discriminated: home range, local, 
and regional scales. Single individuals operate at the level of a home range, whereas 
dispersal and population processes occur at the local scale, and between-population 
interactions and patterns within a species geographic range are distinguished at regional 
scales of observation (Wiens et al. 1986, Kotliar & Wiens 1990, Fig. 1). Hence, during 
their life-history individuals respond to landscape characteristics that are apparent at 
multiple scales. Hierarchical properties of an ecological scaling strongly suggest that 
domains of scales are species-specific and, thus, the scale of investigation must be based 
on a species’ ability to perceive and respond to its environment (Wiens 1989, Pearson et 
al. 1996). Spatial scaling also proposes that generalisations across scales or among 
species are likely to be misleading. Therefore, detailed knowledge regarding a species 
biology is an important prerequisite to appropriately distinguishing the correct scale of 
observation (Lima & Zollner 1996). In addition to spatial scaling, the temporal scale of 
biological events such as forest patch dynamics, generation length, population cycles and 
dynamics, or even evolutionary adaptation to changing environmental conditions are 
relevant time spans to consider (Orians & Wittenberger 1991, Fahrig 1992). Time scale of 
observation is often shorter than many of these processes. Since ecological processes 
generally occur over time frames far beyond research potential, short-term studies and 
temporal snapshots may fail to detect essential details or the range of variation in pattern 
under study (Wiens et al. 1986).  
1.3  Theoretical and modelling approaches in landscape ecology 
Landscape modelling has been much encouraged by ongoing intensive management of 
natural environments and accelerating loss of habitats (Franklin & Forman 1987). It is 
widely agreed that the current development has had several negative consequences to 
biological diversity and ecological processes. This has raised the question of how much 
original habitat should be left and how it should be embedded in an otherwise altered 
landscape matrix (e.g. Diamond 1975, Fahrig & Merriam 1994). The theory of island 
biogeography already suggested that the area of oceanic islands and their spatial 
arrangement had an effect on species numbers on islands (MacArthur & Wilson 1967). 
Subsequent research on land bridge islands showed that a progressive decrease in island 
size due to rising see level after the ice age and the following breakdown of the mainland 
leads to a reduction in mammal and avian species numbers (Wilcox 1980). The effect of a 
reduction in species numbers generates a time lag during which the species pool relaxes 
to lower level of species diversity (Diamond 1972, Tilman et al. 1994). The insularization 
process on mainland and terrestrial ecosystems deviates from the oceanic seascapes 
because of a completely different matrix quality. Surrounding sea composes a hostile 


 
 
16
matrix element for terrestrial animals but continental landscapes often constitute a 
heterogeneous and dynamic habitat mosaic of less hostile matrix characteristics.  
Landscape ecological modelling approaches have provided important information on 
how structure in space developes and changes with the varying amount of suitable 
habitat. In neutral landscape models (neutral percolation models) spatial structure in 
model landscapes results from a random process in which all other physical and 
biological factors are excluded (Gardner et al. 1987). These simulations have 
demonstrated that in landscape development there are different stages that have dissimilar 
quantitative characteristics. After certain threshold values in the proportion of a suitable 
habitat landscapes lose their permeability and connections along original habitat across 
the space cease. The average size of habitat patches reduces rapidly, and their mean 
interpatch distances increase continuously (Turner & Gardner 1991). If neutral random 
models are made more complicated by affecting the explicit spatial location of habitat 
patches (e.g. fractal models) the same landscape patterns and trends prevail, but critical 
threshold levels change (With et al. 1997). For instance, the largest patch that still 
expands from one edge to the other and, thus, bridge the model landscape in random 
percolation models, breaks down when 59 % of original habitat is left, whereas in fractal 
models the same threshold is reached at 20−30 % level of remaining original habitat 
(With & Crist 1995).  
Another important finding of the modelling approaches and analysis of empirical data 
is that although habitat loss (decrease in the amount of habitat) is normally causing the 
fragmentation of the landscape (subdivision of a uniform area into fragments) habitat loss 
effect and fragmentation effect have to be kept separate and studied as different 
characteristics of a functional space in terms of species existence and survival (Saunders 
et al. 1991, Andrén 1994, Fahrig 1997, Bender et. al. 1998). It seems that much of the 
decline in biological diversity can be explained by habitat loss alone i.e. it is a pure area 
effect. However, after a certain threshold value, landscape configuration or spatial spacing 
of habitat patches have an additional effect and species richness and population densities 
tend to decrease faster than predicted by the area alone (Andrén 1994, 1996). Empirical 
studies suggest that the threshold for fragmentation effect in birds and mammals lies 
between 10−30 % of the amount of original habitat (Andrén 1994). Fahrig (1998) 
suggested that fragmentation effect influences the species persistence in a landscape 
under very narrow and limited conditions and the habitat loss effect is overwhelmingly 
more important than fragmentation effect. Nevertheless, the histories and qualities of real 
landscapes vary conspicuously from model approaches and species landscape responses 
cover extremely many ecological conditions that have not been included in theoretical 
models. Models are important for formulating new questions and to set preferences for 
empirical research (With 1997, With & King 1997), but more data on real landscape 
patterns and processes are still urgently needed to understand fragmentation problematics 
in a variety of taxa and under various ecological conditions (Robinson et al. 1992, 
Harrison & Bruna 1999, see also Tischendorf 2001). Recent studies on the role of the 
matrix habitat and its quantitative characteristics such as the gap structure indicate that 
the colonisation of habitat patches cannot be estimated precisely by examining habitat 
patch structure simply because colonisation probabilities of habitat patches in a landscape 
are matrix dependent (With & King 1999). 


 
 
17
The patch-matrix concept in landscape ecology has much in common with dynamic 
population models (see Hanski 1999) in terms of how they divide space into units of 
interest and intervening area that separates them from each other. However, in landscape 
ecology, focal habitat is surrounded by a matrix i.e. other habitat types, whereas in 
population models, locations that are occupied by a population are separated by isolation. 
Nonetheless, both theoretical approaches define explicitly habitat patches or locations of 
populations in space. These approaches, however, differ in how they characterise 
intervening space. In landscape ecology, the matrix is quantified in more detail and the 
matrix quality is an important factor in a landscape pattern analysis (e.g. With & King 
1999). In population models, the distance between two populations implicitly includes 
matrix quality and its implications for population dynamics in the system. A successful 
synthesis of these two approaches depends much on the importance of landscape matrix 
and its role in population processes. The fact that landscape responses of species vary 
considerably raises an interesting question: which taxa are constrained by matrix quality 
and which ones by pure isolation. In order to understand ecological properties of 
landscape context it is necessary to have a greater body of knowledge on landscape 
associations for a variety of species. 
Despite of the recent progress and development in landscape ecological research, most 
of the landscape ecological studies are yet, to large extent, empirical and descriptive. 
Because of the short history of landscape ecology as a sovereign discipline and the 
complexity of spatial systems, landscape ecology still lacks a general body of theory 
(Zonneveld 1990, Wiens 1992). Due to the weak theoretical background rigorous 
hypothesis testing and experimentation have not yet been carried out in landscape 
ecology. However, long temporal and large spatial scales do not often enable controlled, 
replicated experiments (Hargrove & Pickering 1992). The body of theory of landscape 
ecology is developing presently (Bissonette 1997, Wiens 1995). Perhaps the fruitful 
combination of landscape ecology and metapopulation theory will bring new insights for 
formulating a theory of spatially and temporally dynamic landscapes which also 
incorporates hierarchical properties of ecological processes. 
1.4  Boreal forest landscape: the setting of the study 
In landscape ecological studies it is of great importance to consider the history and 
natural characteristics of a study area, but also the extent and intensity of human 
influence in that particular landscape. For forest-dwelling species northern boreal forest 
landscape is by no means a homogenous large block of forest with uniform, predictable 
landscape structure. On the contrary, northern taiga forest is literally a vast mosaic of 
several landscape elements that are in a constant dynamic state of change (Sousa 1984, 
Pickett & White 1985). Some elements such as water bodies and wetland areas are 
practically permanent parts in this mosaic, but forested land is dynamic and under 
repeated disturbance and recovery processes (Esseen et al. 1997). Common disturbances 
in boreal taiga range from forest fires and storm winds that operate at a large scale to 
small scale patch dynamics (White 1979). Subsequent forest succession in a disturbed 
area follows patterns that are typical of regional climatic conditions and local soil 


 
 
18
characteristics (Bonan & Shugart 1989). These recovery processes result in a spatially 
heterogeneous mixture of different forest types and seral stages in a forest landscape. This 
dynamic framework forms a starting point to studies on all organisms that have adapted 
to boreal forest setting (Tiebout & Anderson 1997). The important outcome of the 
dynamics in boreal forest ecosystem is that at a large scale taiga forest landscape is 
regularly fragmented by natural non-forested areas and, secondly, forested habitats such 
as late seral forest patches, for instance, are spatially segregated and their location tend to 
change in time. 
1.4.1  Human land use history and antropogenic landscape patterns 
In northern Finland, man has interacted with his immediate environment ever since the 
first settlers invaded the large tracts of forest. In the course of history, human influence in 
terms of the exploitation of forests has become more extensive and intensive (Kimmins 
1997). Before modern times human induced changes in boreal forest ecosystem were 
subtle and local. Compared with natural disturbances, they tended to have a minor effect 
on overall landscape structure. At a forest stand level, household harvesting or slash-and-
burn-cultivation altered profoundly only forest stand structure but, on the other hand, at 
the same time these activities were a source of e.g. deciduous-rich forest sites (Aarnio 
2001). When forest harvesting in Finland was organised in the middle of the 1800’s and 
forests became an important raw material reserve for the growing saw and paper industry, 
systematic forest management began at a larger scale (e.g. Cajander 1910). In the 20
th 
century, forest practises were pursued throughout the forestland in Finland and harvesting 
operations were extended to the Finnish Lapland. However, although forestry now 
operated at a large scale and the whole forest landscape was subject to human influence, 
“old-fashioned” forest harvesting did not bring about dramatic changes in landscape 
structure. The age structure of stands was mostly affected by selective cutting of large 
diameter timber, but composition of forest types and their configuration or large scale 
connectivity in forest landscapes altered only relatively little. Since the 1950’s, in parallel 
with the modernisation of forest harvesting methods, intensity and efficiency of forest 
practises became a new paradigm (Leikola 1983). New methods such as clear-cutting, 
regeneration of stands by pine plantations, suppression of broad-leaved trees, and soil 
preparation shaped the forest landscape in a new fashion. Gradually, but inevitably 
modern forestry altered landscape structure and converted it into economic forest 
landscape (Franklin & Forman 1987, Hunter 1990). A consequence of this trend was that 
landscape composition on public land turned towards pine dominance and homogenous 
even-aged forest stand structure (Anon. 1998). Landscape configuration resulted from 
rational forest planning and natural landscape connectivity was often decimated by large 
clear-cuts and dense sapling stands that fragmented previously continuous forest blocks 
(Mykrä et al. 2000). The present day landscape structure is largely a product of relatively 
short-term intensive forest planning and management and it is likely that this will have an 
impact on ecological processes in forest landscapes still in the future (Rolstad 1991).  


 
 
19
1.5  Siberian flying squirrel as a landscape ecological object 
The Siberian flying squirrel (Pteromys volans) is distributed through the Eurasian boreal 
taiga zone from Hokkaido, Japan, to the Baltic countries and Finland (Ognev 1940, 
Wilson & Reader 1993, Dobson 1994). In Finland, the species range extends from 
southern country to southern parts of the Finnish Lapland. In the south the range seems to 
be rather continuous, whereas in northern Finland the species is more common in western 
Kainuu and Koillismaa than along the eastern border of the country. There are no recent 
documented observations of the species from northern Ostrobothnia (Reunanen 1998). 
No permanent populations appear to have been established on the Swedish side of the 
Tornioriver, although some historical observations from Finnish Lapland exist (Hokkanen 
et al. 1982).  
The Siberian flying squirrel is a nocturnal arboreal species. The species prefers mature 
mixed spruce forests and tends to favour forest sites that are conspicuously rich in 
deciduous trees, especially aspen (Populus tremula), and distinctively large spruces 
(Picea abies; Hanski 1998). The species is omnivorous, but its diet principally constitutes 
of leaves in summer and catkins and buds of alder (Alnus sp.) and birch (Betula sp.) in 
winter. Supplementary food items, such as seeds and buds of conifers, are consumed 
frequently (Mäkelä 1996, own observations). Hence, food availability does not seem to be 
a limiting factor restricting its space use in forest landscapes. The Siberian flying squirrel 
is predated mainly by large owls and the goshawks (Accipiter gentilis), and to some 
extent by martens (Martes martes). However, due to relatively low population densities of 
the species, it appears to be of minor importance to predators and only occurs 
occasionally as a prey item in their diet (see e.g. Huhtala et al. 1976), unlike North 
American flying squirrels that are an important prey for some avian predators (Carey et 
al. 1992). The occupied forest sites apparently provide the species sufficient food 
reserves and cavities for safe breeding and roosting. Also, red squirrel dreys are 
frequently used for roosting (Hanski et al. 2000, own observations). In addition to forest 
habitats, the Siberian flying squirrel also occurs in cultural environments in southern 
Finland (see Sulkava et al. 1994, Wistbacka et al. 1996). 
Home range sizes differ remarkably between the sexes. Mean home range size for 
males is close to 60 hectares and this area contains several separate habitat patches that 
are visited regularly. Females are more site tenacious and concentrate their activities 
principally on one habitat patch. The average home range size for females is 8.3 hectares. 
Home ranges for females do not overlap and they inhabit their own habitat patches; in 
comparison, males frequently include more that one female in their range and, therefore, 
move regularly among sometimes rather distant habitat patches (Hanski 1998, Hanski et 
al. 2000, own observations). Juveniles disperse in late summer and establish their own 
home ranges within a mean distance of two kilometres. However, some individuals, more 
often females, disperse distances of up to eight kilometres (Selonen & Hanski 2000). 
During the dispersal they can cross open areas up to 100−150 meters (own observations). 
The Siberian flying squirrel has been listed as an endangered species in Finland (Rassi et 
al. 2000). Public and game inquiries in the late 1970’s indicated that the decline of the 
species has apparently been continuous since the 1950’s (Hokkanen et al. 1982). This 
negative population trend was recently documented also in smaller, more intensively 


 
 
20
studied areas in southern Finland (Anon. 2001). The decline of the species was attributed 
to habitat loss and general degradation of remaining habitat patch quality. Also, 
fragmentation of forest areas was seen as a process that creates unfavourable landscape 
patterns for the local long-term persistence of the species (Hokkanen et al. 1982, Rassi et 
al. 2000). 
1.6  Thesis objectives 
The aim of this study was to examine landscape responses of the Siberian flying squirrel 
in northern Finland where the species occurs at the north-westernmost limit of its global 
range. In order to characterise landscape patterns quantitatively three functionally 
different habitat types were in focus: first, mature spruce dominated habitat patches 
preferred by the species, second, areas that act as connecting habitat for the species, and, 
third, unsuitable habitats, such as sapling stands and treeless open areas. Spatial structure 
of these landscape elements was investigated empirically in Kainuu and Koillismaa 
regions to detect which landscape patterns are associated with the occurrence of the 
species and to find relative priorities of landscape characteristics (I, II, III). Moreover, in 
these studies, the spatial resolution ranged from home range (IV) to local (I, II) and 
regional scales (III) (Fig. 1). In order to gain more accurate information on how the 
spatial structure of these functionally different landscape elements correlates with the 
occurrence of the species at a local scale, presence/absence data sets from well-defined 
study areas in Koillismaa were analysed (V). These studies also yield information on the 
relevancy of remote sensed images and the applicability of GIS techniques in specific 
ecological and conservation issues. The practical outcome of this research suggests some 
general guidelines for forests management planning and single-species conservation 
efforts. 


2 Material and methods 
2.1  Pellets on the ground − signature of the species presence 
The occupancy pattern of the Siberian flying squirrel in larger forest areas or its 
presence/absence in single habitat patches was determined by searching for visible signs 
of the species in the field. This species is nocturnal and rather difficult to observe, thus, 
faecal pellets at the base of prominent spruces and foraged leaves under large canopy 
deciduous trees provide a means to track its presence in the wild (Skarén 1978). Field 
signs are fairly reliable in confirming the presence of the species, but its absence is more 
difficult to ascertain. Radio-tracking of the individuals has suggested that forest sites that 
are clearly marked with droppings normally belong to central parts of the home range and 
are also permanently occupied (own observations). This applies particularly to female 
home ranges. Males that regularly visit several habitat patches may remain undetected, 
especially if the habitat patch is not occupied by a female. Therefore, some good quality 
forest sites that are in fact occupied may be extremely difficult to identify in the field as 
occupied by looking for the pellets only. Foraged leaves found on the ground indicate the 
actual presence of the species. However, some habitat patches of seemingly lower quality 
may have been in temporary use or traversed by dispersing juveniles, but one can easily 
find pellets there and label that particular patch as occupied.  
Another source of error comes from forest management practices. After logging some 
stands formerly suitable for the Siberian flying squirrel become deserted and individuals 
colonise remaining nearby remnants of forest that are of lower quality (Taulman et al. 
1998). Temporal inaccuracies depend on the forest site properties because the decay rate 
of droppings vary from one to three years and, thus, entail a considerable time lag in 
patch occupancy (Putman 1984). Therefore, a recent occupancy of a habitat may still be 
discovered after a few years, which is likely to have an influence on very short-term 
studies by overestimating the number of inhabited habitat patches. However, most of the 
occupied habitat patches were clearly occupied (judged by the number of recent 
droppings) at the time of observation. The occupancy status of only a few habitat patches 
was based on very small number or single pellets. The proportion of those habitat patches 
was around 10 %.  


 
 
22
2.1.1  Presence/absence data in ecological research 
The advantage of presence/absence data is that it is easy to collect and enables to extend 
the scale of the study because habitat sampling is not so time consuming. The data are 
quantitatively neutral and characterise essentially the qualitative occupancy status of the 
habitat patch. Thus, all habitat patches despite of their size or other ecological attributes 
are of the same value and ranked equally. Any population density estimate classifies 
patches and gives quantitative information on habitat patches (Raivio 1992). 
Presence/absence data sets are often temporal snapshots and contain no information on 
variation in time or turnover times in occupancy pattern. Therefore, long-term studies 
help distinguish habitat patches that are permanently occupied from the ones that are 
most of the time vacant, but by chance can be occupied at the time of observation.  
Incidence data have often been used in predictive models to account for species habitat 
preferences or occurrence patterns (see e.g. Rita & Ranta 1993, Boyce & McDonald 
1999). Results of predictive models should always be validated with an independent data 
set and the fit of the model must be carefully considered. The examination of the source 
of prediction errors and the origin of false positive and/or false negative predictions must 
be analysed to assess the accuracy and generality of the model (Fielding & Bell 1997, 
Araújo & Williams 2000). Although predictive models are conventionally intended to 
allow broader generalisations within the limits of their domain they tend to be specific 
and apply only to a well-defined group of species (Cherill et al. 1995, Miller et al. 2000). 
However, species’ landscape responses may further vary even among congeners 
(Lindenmayer et al. 1999). At a large continental scale, estimates of primary productivity 
or rough habitat type classification can be used to predict very general species richness 
patterns (Danell et al. 1996). This further suggests that it is crucial to measure 
independent habitat and landscape variables at correct scales. Variables measured at the 
regional scale can confuse the interpretation of local scale processes and most likely 
result in a lack of true landscape responses of the species (McDonalds et al. 1996, 
Cardillo et al. 1999).  
2.2  Landscape pattern analysis in GIS 
The rise of landscape ecology coincides roughly with the development of commercially 
available remote sensing techniques (accurate aerial photographs and digitised satellite 
images) and advanced geographic information systems (GIS). These new methods 
provide certain evident advances allowing the examination of larger scale landscape 
patterns and provide tools capable of handling and processing large multiscale data sets. 
They further facilitate the computation of landscape metrics and the analysis of often 
complex landscape structure (Pukkala 1985, Star & Estes 1990, Haines-Young 1993). 
Large-scale changes in a landscape structure in time can also be analysed by comparing 
images from different time periods (Johnson 1990). Modern satellite images are 
reasonable high in resolution allowing the detection of landscape responses of species at 
rather small scales, that is, if habitat characteristics are discernible from the images and 
classification of satellite images is correct, relevant, and precise. 


 
 
23
This study exploits Landsat TM 5 satellite images. Land use and forest resource data 
were derived from Finnish national forest inventories (NFI; Tomppo 1991, 1993, Tomppo 
et al. 1998). The interpretation of satellite images is based on comparisons of nearest 
neighbouring ground study plots to adjust the reliable classification of images (Tomppo 
& Katila 1993). The resolution, i.e. pixel size, of the system is 25 x 25 meters. Digital 
maps were utilised to distinguish non-forested landscape classes (fields, wetlands, 
settlement etc.) from forested ones. In this system, up-to-date forest stand age and timber 
volume estimates for all main tree species can be produced. This classified satellite image 
can further be reclassified in GIS to analyse landscape patterns.  
GIS procedures are prone to two types of error: positional and attribute accuracy of the 
satellite data (Mattila 1993). Positional accuracy refers to the spatial shape, size, and 
exact location of an element. In this data this error has been estimated to be 0.5−1.0 
pixels, which is unlikely to have any significant effect on larger scale landscape responses 
of organisms. However, in small-scale studies, the relevancy of this error must be 
considered carefully and its effect on results clearly understood. Attribute accuracy deals 
with the system’s ability to discriminate different habitat types. Definition of focal habitat 
is basically subjective and is premised on the understanding of the species ecology. In 
heterogeneous landscapes the boundaries of habitat patches are often subtle and diffuse, 
that is why they are sometimes difficult to identify from habitat mosaics (Gustafson & 
Gardner 1996, Knight & Morris 1996). Therefore, inaccuracies in landscape classification 
and habitat patch identification may confound landscape effects or even bias results. For 
instance, coniferous trees (pine and spruce) are more accurately separated when either 
species clearly dominates the canopy, but estimates for mixed stands are less precise. 
Deciduous trees are to large extent discriminated from conifers, but different broad-
leaved tree species cannot be discriminated (Tomppo & Katila 1993). Transition zones 
between habitat types or pixels that are located at the edge of water bodies are a constant 
source of error and become frequently misclassified (Kalliola & Syrjänen 1991, Tomppo 
et al. 1998). Nonetheless, forest management has increased the contrast between 
landscape elements and created sharp landscape boundaries, which facilitates the 
discrimination of habitat patches and reduces the risk of misclassifications. Generally, the 
smaller the scale of observation the larger error limits one has to accept. In present 
studies, classification error has to be examined at two levels. At larger scale studies (I, II, 
III) classification inaccuracies cannot be controlled completely. However, this error is 
systematic and misclassified habitat patches are in principal small in size. At smaller 
scale studies (IV, V), this source of error can be controlled by excluding human caused 
changes in a landscape structure and by checking habitat patches from aerial photographs 
and in the field. 
2.3  Landscape variables and statistical analysis of landscape data 
Landscape structure is characterised by variables that describe a single habitat patch and 
the spatial distribution of this habitat type in space or landscape structure in general. The 
measurement of landscape metrics was carried out in GIS by employing FRAGSTATS 
software (McGarical & Marks 1995). Several variables that quantify the landscape 


 
 
24
structure were calculated. Variables were continuous, but they are often strongly 
intercorrelated and do not always distribute normally. The number of variables that are 
easily available and their statistical properties, hence, require attention in statistical 
analysis. The selection of appropriate variables is of foremost importance during early 
stages of a study. It is not necessary to accept all the variables of seeming relevancy, but 
only the minimum set of variables should be considered to make the analysis of large data 
sets simple. The variables have to be straightforward to interpret and firmly linked with 
the ecology of the focal species or the process of interest. Most criticism directed to the 
commonly used landscape metrics concern correlations between variables and the range 
of their utility (Schumaker 1996, Hargis et al. 1998). Deviations from normality are 
mainly due to frequent zero values in data and the fact that, for example, habitat patch 
sizes in human modified landscapes are skewed to smaller size classes. Strongly 
correlated explanatory variables are undesirable, but, if they clearly express distinct and 
separate landscape characteristics, it is justified to include these variables in the statistical 
analysis. Correlations and the lack of normality call for non-parametric statistics (Sokal 
& Rohlf 1995). Multivariate statistical methods are appropriate for the analysis of 
multivariate landscape data sets. Multivariate statistics enable the compression and 
simplification of often complex data and helps to detect structural patterns in the data 
(Jongman et al. 1987, James & McCulloch 1990). For data sets where the dependent 
variable is binary, i.e. presence/absence data, logistic regression methods provide an 
convenient statistical modelling tool for multivariate landscape data. 


3 Results and discussion 
3.1  Landscape structure around old-growth forest areas in Kainuu (I) 
In Kainuu, landscape characteristics of occupied and unoccupied old-growth forest areas 
were compared to investigate which landscape patterns account for the presence/absence 
of the species in relative large and continuous forest areas. Twenty old-growth areas in 
Kainuu were systematically selected and checked to examine the occupancy of the 
Siberian flying squirrel. Because the number of observed occupied forest sites per study 
forest areas ranged from total absence to several observations they were classified into 
two categories: first, forest areas that host a population and, second, the ones that lack the 
species or where population densities are likely to be very low. Landscape analysis 
included seven landscape classes and the landscape structure was studied at seven spatial 
scales (Fig. 1). 
The main result of this study was that old-growth forest areas that were unoccupied by 
the Siberian flying squirrel were surrounded more often by open areas. This habitat type 
was proportionally more dominant and patches of open area were larger in size and their 
nearest neighbour distances were shorter than in occupied forest areas. The quality of the 
matrix is likely to decrease the probability of occupancy so that even large areas of 
suitable habitat remain uncolonised if open habitats (lakes, wetlands, clear cuts, or fields) 
constitute a significant portion. The other interesting result of the study was that the 
small-scale variation at the level of home range within forest areas promotes the species 
occurrence. This may be caused by small openings in the forest canopy and the 
regeneration of deciduous trees in the vicinity of these canopy gaps. The dominance of 
mixed pine-spruce forest at the home range scale in unoccupied forest areas indicates the 
role of some qualitative aspects of the forest area. It suggests that the shift from spruce 
dominated to more pine dominated forest habitats may be unfavourable to the Siberian 
flying squirrel. Therefore, the abundance of pine-dominated forests is likely to influence 
the habitat selection process of the species at the forest site scale and colonisation rates at 
larger scales. The observed absence of the species from eastern parts of Kainuu further 
suggests that there may be a regional-scale gradient in habitat quality, which affects the 
species distribution. The size of old-growth fragments does not seem to play a role in 


 
 
26
occupancy patterns, which is quite expected, for all forest areas were large (often >>1 
km
2) and could easily include several individual home ranges or even host a local 
population. 
Far reaching conclusions on the basis of this data set cannot be drawn because of the 
broad landscape classification. At larger scales of observation, variation in the landscape 
types tends to increase. However, for the habitat classification at larger scales many 
landscape classes must be combined and, therefore, some of them lose their identity in 
the analysis. For example, in this study landscape matrix included several ecologically 
discrete landscape elements e.g. sapling stands whose role was masked by the 
classification. Also the amount of pine in the pine-spruce landscape class can vary 
between 20 and 80 %. At the large scale (r>5 km), the proportion of matrix habitat 
becomes overwhelming and the variation between examined landscapes disappears i.e. 
landscapes become similar in terms of a landscape structure. However, at smaller scales 
(r<5 km) landscape classification performs sufficiently well and points out important 
landscape responses of the Siberian flying squirrel at these particular scales. 
3.2  Local scale habitat structure in Koillismaa (II) 
In order to examine local scale patterns in habitat patch occupancy of the Siberian flying 
squirrel in Koillismaa the distribution of the species and the location of occupied forest 
sites were mapped in the field. Landscape structure around occupied forest sites was 
examined to characterise patterns in landscape composition and connectivity that are 
associated with the presence of the species. Landscape structure around occupied forest 
sites at scales of one and three kilometres were compared to randomly drawn locations on 
forestland to yield a reference landscape structure (Fig. 1). The landscape was classified 
into ten landscape categories but they were handled as three functionally different 
landscape classes: breeding, dispersal habitat and unsuitable open areas.  
Forest landscapes where the Siberian flying squirrel was present contained more 
breeding habitat and were better connected to other habitat patches by suitable habitat for 
movement than other landscapes. Landscape structure around random locations consisted 
of smaller habitat patches and higher patch densities, which indicate a more fragmented 
landscape structure (Turner & Gardner 1991). This suggests that landscape graininess 
turns from coarse in occupied landscapes to finer grain size in random landscapes (see 
Rolstad & Wegge 1989). For persistence of the Siberian flying squirrel coarse graininess 
at a local scale is likely to be beneficial if not necessary. At the scale of one kilometre, the 
proportion of dispersal habitat in occupied landscapes covers over 50 % of the area but 
decreases to 40 % when the scale is widened to three kilometres. 
In this study occupied landscapes were compared with random and thus the general 
landscape pattern. The use of random locations as a null landscape structure may not 
entail important landscape characteristics that contribute to the absence of the species. 
Hence, landscape patterns that are linked with the occurrence of the species are only of 
indicative importance for the presence of the species. The actual comparison does not 
provide information on which characteristics are harmful or even detrimental for the 
spatial distribution of the species and, thus, gives no clue to account for the absence of the 


 
 
27
species. For practical forest management information on landscape characteristics that 
promote species presence is as important to understand as the ones that are unsustainable 
and disadvantageous for the species. 
3.3  Distribution of the Siberian flying squirrel in northern Finland 
(III) 
Till the mid 1990’s the distribution of the Siberian flying squirrel in northern Finland was 
basically unknown and it was generally based on single observations of the species over 
this vast area. Hokkanen et al. (1982) even predicted that the northern populations of the 
species will go extinct in the near future. Nevertheless, biodiversity inventories in old-
growth fragments in the early 1990’s (Rassi et al. 1996) and systematic mapping of the 
species in Kainuu and Koillismaa (I, II) showed that the Siberian flying squirrel still 
occurs in natural forest areas in northern Finland. However, the present range appeared to 
be irregular and suggests that the species is rather common only in the western parts of 
Kainuu and Koillismaa. In Pohjanmaa the species seems to be absent and rather rare in 
eastern Kainuu. In this survey, landscape structure at regional scale was described to 
account for the observed distribution of the Siberian flying squirrel in northern Finland. 
Large-scale habitat patterns of seven landscape classes and their spatial arrangement were 
investigated and landscape patterns were compared between three regions (Fig. 1). 
Additionally, natural fragmentation was separated from human caused subdivision of 
forest landscapes. This was estimated by comparing the present overall landscape 
structure to habitat structure in protected nature reserves. 
Results of this study suggest that the presence of spruce dominated forests at a large 
scale contribute to the presence of the species whereas an increasing proportion of 
peatlands i.e. unsuitable habitat correlates with the species absence. The gradient from 
more luxuriant forest types in the western parts of Kainuu to poor soil types and pine 
dominated forests in the east, as already suggested in (I), seem to account for irregular 
patterns in occupancy and, probably also, lower population densities. It was assumed in 
the study that existing nature reserves present more original habitat structure than the 
present managed forest landscapes. Comparisons of landscape patterns among nature 
reserves and regional landscapes show clear differences in habitat composition and stand 
age class distribution. Because the actual occurrence of the Siberian flying squirrel in all 
sampled nature reserves and landscape squares is not known, any threshold proportion of 
spruce forests cannot be determined from the present study design. 
The division of the north Finnish forest landscape into three subregions was basically 
subjective because exact boundaries of the range of the Siberian flying squirrel in 
northern Finland could not be outlined. The boundary between Pohjanmaa and 
Koillismaa is rather sharp due to geological factors and follows the highest shoreline after 
the ice age (Anon. 1992). The limit that demarcates Koillismaa from Kainuu is diffuse 
and extremely difficult to identify. However, regional scale landscape patterns seem to 
influence the distribution of the Siberian flying squirrel. Surveys of biodiversity values in 
Russian Karelian natural forests did not document a single sighting of the species 
(Pyykkö 1996). Long term inventories on mammal fauna in Kostamuksha nature reserve 


 
 
28
just opposite to Kainuu in Russian Karelia report only occasional findings (Pozdnyakov 
1997). Habitat type mapping in Russian Karelia shows that large forest areas on the 
Russian side of the border are pine dominated and spruce forests cover approximately 
from 10 to 30 % of the area (Gromtsev 1996, Pyykkö 1996). This result also suggests 
likelihood that the Siberian flying squirrel colonised northern Finland from the south and 
not from the east. The result also gives a hint why the species is still missing from the 
fauna of Sweden. 
3.4  Are large-scale landscape patterns visible at a home range scale? 
(IV) 
Habitat selection of an organism depends on necessary resources for foraging and 
breeding and it ultimately takes place at a relatively small scale. Therefore, habitat 
composition analysis within a home range of an individual is fundamental information for 
understanding landscape responses of a species. In a field survey, forest structure in forest 
sites that were actively used by the Siberian flying squirrel was characterised and 
compared to randomly chosen forest sites in old-growth forest area. In addition, habitat 
composition in home ranges of radio-collared individuals was analysed from satellite 
images (Fig. 1). Results from these two approaches were compared to determine which 
habitat characteristics were in common and more interestingly discernible from satellite 
images in GIS. 
Data from field surveys showed that occupied sites are distinctively situated in forest 
sites where timber volume of spruces is higher than on average in the stand, and that 
deciduous trees comprised a marked proportion of these forest sites. Large aspens seem 
to be well represented. Satellite imagery data agree to a large extent with field 
observations. Intensively used locations in home range tended to have higher timber 
volume estimates, especially that of spruce, than on average for home ranges. There was a 
tendency to avoid pine dominated forest sites suggesting a marginal role of pine for 
breeding and foraging when other better quality habitats were available. However, 
although deciduous trees were an important component in forest structure in the field 
study they were not pronounced in GIS analysis. 
It has been previously documented that deciduous trees are important habitat 
constituents of forest sites occupied by the Siberian flying squirrels (e.g. Hanski 1998). 
Therefore, the proportion of deciduous trees and their spatial dispersion in forest habitat 
patches is an evident measure of the quality of that habitat patch. Empirical findings 
showed that broad-leaved trees were firmly linked with the occurrence of the species in 
northern Finland. Failure to detect deciduous trees in mixed forest in GIS analysis is 
mainly due to inaccurate discrimination of broad-leaved trees from satellite images but 
also due to the resolution i.e. pixel size (Tokola & Heikkilä 1997). However, the number 
of sampled individuals and pixels in the resampling analysis were relative low and 
probably insufficient to draw substantial conclusions.  


 
 
29
3.5  Is the presence of the Siberian flying squirrel in a habitat patch 
predictable? (V) 
In order to have more detailed information on species’ landscape responses other than 
general correlative spatial patterns at local or regional scales, research should be 
conducted at the habitat patch level. These studies have to include data on habitat patch 
characteristics and its spatial context as well as the status of the species, i.e. its 
presence/absence or population density, in that particular habitat patch. Therefore, habitat 
patch occupancy of the Siberian flying squirrel was investigated at the scale of discrete 
habitat patches to build a predictive landscape model for occupancy patterns at a local 
scale (Fig. 1). Suitable forest habitat patches were sampled in four study areas to 
determine the presence/absence pattern of the Siberian flying squirrel in habitat patches. 
Landscape data on habitat patch quality, structure of the surrounding landscape, and 
landscape connectivity were gathered to correlate observed presence/absence pattern with 
landscape characteristics.  
Logistic regression modelling suggested that habitat patch quality (size and proportion 
of deciduous trees) seems to be the most important single factor that affects the 
probability of occupancy in a habitat patch. However, structural connectivity in a 
landscape increased the probability of species occurrence; even lower quality well 
connected habitat patches were occupied. The amount of habitat patches in the 
surrounding landscape seems to have a minor effect on occupancy. Predictions of the 
landscape model were tested with an independent data set. The landscape model, 
however, predicted the occurrence of the species in habitat patches in the test data set 
worse than in the training data set. In addition, the model predicted the absence of the 
species better than its presence. 
Results of this study suggest that generalisations even in the same region can be risky 
and require careful consideration. The failure in predicting the presence of the species 
better rises some questions of underlying ecological processes i.e. turnover dynamics 
and/or recent changes in the landscape structure such as forest harvesting that affect the 
pattern in patch occupancy. The use of principal component analysis further conceals the 
effect of single variables and prevents the estimation of their independent contribution to 
the probability of patch occupancy. In large-scale studies where a habitat patch is used as 
a sampling unit, the importance of correct classification of habitat patches is a 
precondition to detailed habitat structure analysis and plausible landscape responses of 
the species in interest. 


 
 
30
 
Fig. 1. Hierarchy of scales for the Siberian flying squirrel. Different hierarchical levels 
indicate ecological patterns from individuals at a home range level to local dynamic 
population and groups of populations at a large regional scale. Roman numerals refer to 
research papers in the thesis. 
Regional scale
Species distribution
 III, (I)
Local scale
Dispersal
I, II, V
Home range scale
Breeding
IV, V


4 Conclusions 
4.1  Landscape structure and the Siberian flying squirrel 
4.1.1  Spruce dominated forest patch: a basic landscape element for the 
Siberian flying squirrel in northern Finland 
Boreal taiga landscapes are diverse and heterogeneous in habitat types and their spatial 
and temporal patterns. Despite this general heterogeneity, forest habitat patches in 
landscapes are dominated by a few tree species. In northwestern Europe, boreal forests 
are mainly dominated by spruce and pine while broad-leaved trees occur principally on 
more nutrient rich soil types. Deciduous trees are also abundant during early stages of 
forest succession and in southern parts of boreal forest vegetation zone. The Siberian 
flying squirrel inhabits spruce and spruce-dominated forest habitats in Finnish boreal 
taiga and, therefore, the grain of the landscape for the species is delineated by individual 
spruce-dominated forest patches (sensu Wiens 1989, II, IV, V). Although the species 
seems to have accepted rural and semi-urban habitats in southern Finland, the extent of its 
distribution in northern Finland is determined by the amount of spruce forest and its 
spatial dispersion (Wiens 1989, I, III). At the habitat patch scale, the Siberian flying 
squirrel responds to the internal structure of a spruce forest patch (IV, V). The occurrence 
of the species in habitat patches has been shown to be associated with deciduous trees 
(Eronen 1996, Hanski 1998). Deciduous trees provide food and cavities for safe nesting 
and roosting, resources considered necessary for the species (Hanski et al. 2000). 
Deciduous forest sites are patchily located in natural forests and they are relatively small 
in size in the north of Finland. The size of a spruce forest patch and the amount of 
deciduous habitat inside the spruce forest determine the quality of the habitat patch, and 
affect the probability that the habitat patch is occupied in northern Finland (V) (Table 1).  
But are spruce-dominated forest habitat patches the smallest landscape units to which 
the species is responding? Radiotracking studies have shown that adult individuals move 
among habitat patches and males especially visit even remote habitat patches frequently 


 
 
32
(Hanski et al. 2000, own observations). This suggests that a single habitat patch as such 
might not be a sufficient landscape unit for individuals in landscapes where habitat 
patches are in general small in size, but instead a group of habitat patches forms an 
ecologically functional unit for persistence. Individuals may complement and/or 
supplement (sensu Dunning et al. 1992) necessary resources (nutrition, nests, mates etc.) 
that are spatially and temporally dispersed among habitat patches. 
4.1.2  Landscape connectivity at a local scale 
In order to estimate landscape connectivity, landscape structural characteristics that 
promote the movement of a focal species in a landscape matrix need to be identified. Also 
information on functional characteristics such as immigration and emigration rates from 
habitat patches and survival probabilities of individuals in a matrix during movements 
should be available (Tischendorf & Fahrig 2000a, b). Because these data are seldom 
obtainable, landscape connectivity in empirical studies refers in practice to structural 
characteristics in landscapes. The lack of demographic data on the Siberian flying squirrel 
does not allow to fully incorporate the functional aspect of connectivity into landscape 
connectivity measures.  
At a local scale, landscapes that contain occupied habitat patches are structured in a 
coarse grain manner and they are less fragmented i.e. there are fewer but larger habitat 
patches for movement than in northern Finnish forest landscapes on average (c.f. Rolstad 
& Wegge 1987). Coarse graininess enhances landscape connectivity by providing larger 
uniform landscape units for movement. Habitat edges and the increase in contrast 
between habitat patches are likely to lower the probability of crossing the boundary 
(Wiens et al. 1985, Åberg et al. 1995). Sharp edges will block the movement of the 
Siberian flying squirrel if moving by gliding from tree to tree is prevented. However, 
narrow gaps are not likely to affect the space use of the species if open areas can be 
crossed by gliding (own observations). The effective landscape use at the local scale is 
enhanced if breeding habitat patches are embedded in the matrix of habitat where 
interpatch distances can be traversed along more or less forested habitat (V). Thus, at this 
scale, landscape connectivity for the Siberian flying squirrel is principally a matrix effect 
and the quality of matrix determines the degree of connectivity in a landscape (Table 1). 
However, individuals are unlikely to move along the shortest distance between two 
habitat patches, instead they tend to move along closed canopy forest habitat and cross 
narrow gaps. Therefore, interpatch distances should not be measured by using shortest 
Euclidean distance but by using landscape structural characteristics as a clue of landscape 
connectivity. This, however, provides good ecological knowledge on the species ecology. 
The dispersal potential of the Siberian flying squirrel ranges up to nine kilometres 
(Selonen & Hanski 2000), but some individuals are likely to disperse even further. The 
maximum dispersal distances normally cover several small and a few large habitat 
patches in northern Finnish forest landscapes where the species is rather abundant. Within 
the average dispersal distance of two kilometres there are always suitable habitat patches 
for the Siberian flying squirrel. Nevertheless, the role and proportion of long distance 
dispersers in population dynamics is not known (see Fahrig & Paloheimo 1988). 


 
 
33
4.1.3  Landscape configuration of habitat patches 
Habitat patch configuration has been considered an important structural characteristic in a 
landscape, but, for mammals and arboreal species in particular, landscape configuration is 
linked further to landscape connectivity. For the Siberian flying squirrel interpatch 
distances of occupied habitat patches tended to be shorter than what was observed for 
unoccupied ones (V). The proportion of open areas surrounding large old-growth 
remnants was connected to lower probabilities in occupancy (I). However, the 
composition of the surrounding landscape at local scales seemed to be rather similar for 
occupied and unoccupied habitat patches and had no significant effect on their occupancy 
probabilities (V). This suggests that the effect of physical arrangement of habitat patches 
is masked by other landscape characteristics or classification criteria of landscape 
elements. This may also indicate that landscape configuration was perhaps measured at 
the wrong spatial scale. At a local scale, structural connectivity, and the fact that most of 
the patches are within the dispersal range of the Siberian flying squirrel, are far more 
important than configuration (Table 1). Regional scale studies (I, III) did not detect any 
patterns in the intervening landscape, which is most likely a result of too coarse a 
classification or too large a spatial scale. Moreover, there are no unambiguous and 
satisfactory quantitative measures to characterise the dispersion and juxtaposition of 
habitat patches in a spatial context. Indices that describe spatial dispersion of landscape 
elements have often been developed in model landscapes and are therefore difficult to 
interpret in real landscape situations (Schumaker 1996, Hargis et al. 1998). Quantification 
of spatial arrangement of landscape elements would be important to illustrate landscape 
configuration more accurately. In boreal forest landscapes, local scale habitat patch 
configuration seems not to be very important for the Siberian flying squirrel, but at a 
regional scale the spatial spacing of larger landscape units such as old-growth forest areas 
or nature reserves is likely to have an effect on regional scale population dynamics. This 
suggests further that landscape configuration may be determined by long-distance 
dispersers and, thus, by occasional but regular interchange of individuals between 
subpopulations. 
 
Table 1. Landscape characteristics at multiple scales and their importance for the 
Siberian flying squirrel in northern Finland. 
 
Scale 
 
Landscape 
characteristic 
Home 
 
Local 
Regional 
Study 
Graininess 
Very 
important 
Important 
Less important 
II, (IV), V 
Composition 
Very 
important 
Important 
Important 
I−V 
Connectivity 
Important 
Very important 
Less important 
II, III, V 
Configuration 
Less 
important 
Important 
Very important 
II, III, V 


 
 
34
4.2  Spatial scaling for the Siberian flying squirrel 
Siberian flying squirrels may respond to habitat and landscape structure at three 
hierarchical levels. The amount of spruce forest habitat in a landscape is likely to 
correlate with the spatial distribution of the species (III). However, the density of the 
species may depend more on the qualitative characteristics of the habitat patches (IV, V). 
Home ranges typically consist of one or more deciduous-rich forest sites on which the 
activity of individuals is concentrated during the breeding season (IV). This particular 
habitat provides required resources for successful breeding and survival and, therefore, 
constitutes the lowest scale for the species. At a local scale, the annual habitat use of 
individuals varies and they exploit a variety of forested habitats but roosting and seasonal 
foraging patches are located most frequently in spruce dominated habitat patches 
(Selonen et al. 2001, own observations). This indicates the next scale of perception for 
the Siberian flying squirrel. Dispersal ability of the species determines the scale of 
population interactions and avoidance of mating with closely related individuals. The 
extent of this scale is influenced by the landscape structure (I, III). Short-distance 
dispersers are likely to be responsible for local population dynamics, whereas long-
distance dispersal entails the exchange of individuals and genes between spatially 
separate subpopulations. 
4.3  Theoretical aspects  
Patterns in randomly fragmented neutral model landscapes have exemplified the process 
of habitat loss and its consequences to landscape structure. Independent of the criteria of 
how model landscapes are subdivided, three main stages in fragmentation process are 
common. First, structural connectivity breaks down, then the patch sizes decrease and 
their number increases rapidly, and, finally, the isolation of patches is a direct 
consequence of the reduced patch sizes. Because neutral models eliminate all biological 
interactions and natural processes in order to produce a random pattern (Caswell 1976), 
they serve as an important reference background to real landscape studies (With & King 
1997). Real landscapes, however, are often naturally fragmented in terms of target habitat 
and, therefore, e.g. the estimation of critical thresholds in proportion of the original 
habitat or in habitat isolation is difficult to conclude from the basis of neutral models 
only. The original pattern and landscape composition in real landscapes should be 
incorporated in these neutral models as a starting point to determine thresholds for the 
landscape structure. However, this presumes that the observed landscape structure 
supports a dynamic population under natural conditions. These conclusions are, on the 
one hand, species-specific and have to be assessed on the basis of species ecology and 
plasticity to respond to spatial changes in the landscape structure.  
The boreal forest landscape is structurally heterogeneous and from the perspective of 
the Siberian flying squirrel it is naturally fragmented to some degree. The species inhabits 
forest sites that are temporary in boreal forest ecosystem (Spies & Franklin 1996) and it 
encounters habitats that are unsuitable for breeding or dispersing at a local scale (see 
Tiebout & Anderson 1997). This suggests that the Siberian flying squirrel has adapted to 


 
 
35
live in a habitat mosaic and use the landscape matrix for colonising novel forest areas. 
Habitat loss and the amount and extent of totally useless habitat types, however, pose a 
risk to its local and regional persistence. Habitat loss effect is obvious, but the role of 
pure isolation effect remains relative. If habitats are isolated by wide open areas or 
sapling stands, isolation may be effective, but in case habitat patches are connected by 
forested habitat (Henein & Merriam 1990, III) even long interpatch distances are 
traversed and habitat patch networks function as an operative demographic unit. 
4.4  Management of the forest landscapes for the Siberian flying 
squirrel 
More than one third of the total number of endangered species in Finland is dependent on 
forest habitat (Rassi et al. 2000). This being the case, management of biological diversity 
in forests or even a single forest-dwelling species has shown to be a difficult task for 
conservationists and landscape managers. This is mainly due to a limited knowledge on 
species ecology, their regional distribution, and local abundances. It is also clear that very 
detailed guidelining can hardly be provided because landscape patterns and ecological 
conditions 
change 
significantly 
among 
regions 
and, 
therefore, 
management 
recommendations tend to be general by nature. Yet, one has to bear in mind that if there is 
no long-term data on population fluctuation or trends in the region, conclusions 
concerning practical rules for management have to be drawn with caution. For instance, if 
a population is declining and management recommendations are based only on one 
season study, the results may be spurious providing limited use as a sound basis for 
sustainable management.  
This study suggests some general, but presumably applicable instructions for forest 
managers. The main findings emphasise the importance of the landscape structure and 
context at separate spatial scales as a whole: the entire landscape being a management 
unit not just single stands as discrete entities (see also Åberg 2000). The use of satellite 
images enables the visualisation of the spatial dispersion of potential habitat patches for 
the Siberian flying squirrel and provides an estimate of their quality. Knowledge 
regarding species ecological requirements and landscape models help to rank habitat 
patches and, hence, to set preferences for strategic planning. Because of failing to predict 
the presence of the Siberian flying squirrel accurately, forest stands need to be checked in 
the field prior to forest cutting. Landscape connectivity can be mapped and likely 
dispersal routes illustrated. Spatio-temporal development of connecting habitat type, 
which often consists of managed stands can be foreseen from forest stand files. 
Landscape management can be directed to improve landscape connectivity and forested 
linkages among habitat patches or to avoid harvesting existing routes. In forest 
management coarse grain structure should be preferred to subdivision of the remaining 
old-growth areas into small fragments. These studies propose that a forest landscape 
where the Siberian flying squirrel persists in northern Finland should contain 20−40 % 
habitat suitable for dispersal. The spatial arrangement of this habitat is important for 
landscape connectivity and it should physically bridge spruce-dominated forest patches. 
Proportion of spruce-dominated forests is more difficult to estimate due to different 


 
 
36
classification criteria used in the present studies. Nevertheless, the proportion of this 
habitat should range from 15 to 20 %. In regions where the Siberian flying squirrel is 
relatively abundant in northern Finland, the amount of deciduous-tree-rich habitat ranges 
between 2−4 % (Table 2). Given proportions are always relative to the landscape context 
in that particular region. This type of study, however, does not provide any unambiguous 
clue for operative planning as to how to manage deciduous forest sites at stand level in 
northern Finnish boreal forests. But it suggests that these, often relatively small habitats, 
should be preserved as key biotopes not only for the Siberian flying squirrel, but also 
because of their overall biodiversity values. 
 
Table 2. Landscape composition and spatial context of different habitat types that are 
necessary for the persistence of the Siberian flying squirrel at a local scale in northern 
Finland. 
Habitat type 
Amount of 
habitat (%) 
Spatial context 
Breeding habitat 
2−4 
Within spruce-dominated forest habitat patches 
Spruce-dominated forest 
habitat 
15−20 
Embedded in dispersal habitat 
Dispersal habitat 
20−40 
Should structurally connect suitable forest habitat 
patches 


5 Concluding remarks 
In the era of sophisticated remote sensing methodology and advanced GIS techniques the 
applicability of this potential in ecological research is an interesting challenge. For this 
kind of landscape ecological study, the Siberian flying squirrel seems to be an optimal 
guinea pig. The species’ habitat use and appropriate landscape patterns are to a great 
extent detectable from satellite images. This was partly confirmed by tracking radio-
collared individuals. The species is neither a specialist nor a generalist in habitat use, 
which is an advantage in using satellite imagery data. Spruce-dominated habitat patches 
can be distinguished in managed forest landscapes and qualitative aspects inside these 
habitat patches even at a home range scale are possible to discriminate. However, detailed 
small-scale information on habitat characteristics are beyond the highest resolution of 
these techniques. At a local and regional scale the resolution is accurate enough to 
distinguish functionally important landscape characteristics. 
Findings of these studies are ecologically meaningful and in line with more detailed 
studies on habitat and landscape use of radio-collared individuals. The advantage of using 
satellite images and GIS in landscape ecological research is that the scale of observation 
can be expanded over large areas and it allows the examination of landscape patterns of 
different habitat types simultaneously. Additionally, landscape patterns can be mapped 
and visualised for practical forest management and biodiversity conservation planning. 
However, a more detailed quantification of a landscape structure in landscape ecological 
research requires a more accurate discrimination of deciduous trees from satellite images 
than in present study. Also, new landscape metrics are needed to quantify the spatial 
arrangement of habitat patches in heterogeneous environments. 
Future prospects of the landscape ecological research of the Siberian flying squirrel 
call for direct or undirect methods to assess the density of the species in a habitat patch or 
in a forest area, but also estimates of temporal dynamics in patch occupancy patterns are 
needed. Instead of correlating presence/absence data with a number of landscape 
variables, density estimates would provide more information regarding the role of 
particular habitat patches. This, however, presumes relative large-scale sampling of 
habitat patches to derive reliable population density estimates. In order to understand 
large-scale patch dynamics and the role of spatial characteristics for the Siberian flying 
squirrel in the long term, structurally different landscapes should be compared along a 


 
 
38
gradient to test whether the findings proposed in this thesis are valid. The advantage of 
modern remote sensing techniques and GIS methods in landscape ecological study and 
management of overall biodiversity are undeniable. An important future challenge in this 
field will be to broaden the domain of this approach and develop its use as an everyday 
tool for ecologists and landscape managers. 


 References 
Aarnio J (2001) Maankäytön historiaa Syöte Life -alueella. Metsähallituksen 
luonnonsuojelujulkaisuja sarja A, in press. 
Addicott JF, Aho JM, Antolin MF, Padilla DK, Richardson JS & Soluk DA (1987) 
Ecological neighborhoods: scaling environmental patterns. Oikos 49: 340–346. 
Andrén H (1994) Effects of habitat fragmentation on birds and mammals in landscapes 
with different proportion of suitable habitat: a review. Oikos 71: 355–366. 
Andrén H (1996) Population responses to habitat fragmentation: statistical power and the 
random sample hypothesis. Oikos 76: 235–242. 
Andrén H, Delin A & Seiler A (1997) Population responses to landscape changes depends 
on specialization to different landscape elements. Oikos 80: 193–196. 
Anonymous (1992) Suomen kartasto, Vihko 123–126, Geologia. Maanmittaushallitus, 
Helsinki. 
Anonymous (1998) Finnish statistical yearbook of forestry. Painatuskeskus Oy, Helsinki. 
Anonymous (2001) Liito-oravan (Pteromys volans) biologia ja suojelu Suomessa. 
Suomen Ympäristö 459: 1–130. 
Araújo MB & Williams PH (2000) Selecting areas for species persistence using 
occurrence data. Biol Cons 96: 331–345. 
Bellehumeur C & Legendre P (1998) Multiscale sources of variation in ecological 
variables: modelling spatial dispersion, elaborating sampling designs. Landsc Ecol 13: 
15–25. 
Bender DJ, Contreras TA & Fahrig L (1998) Habitat loss and population decline: a meta-
analysis of the patch size. Ecology 79: 517–533. 
Bennett AF (1998) Linkages in the landscape – the role of the connectivity in wildlife 
conservation. IUCN, Gland, Switzerland and Cambridge. 
Bissonette JA (1997) Scale sensitive ecological properties: historical context, current 
meaning. In: Bissonette JA (ed) Wildlife and landscape ecology. Springer Verlag, New 
York, p 3–31. 
Bonan GB & Shugart HH (1989) Environmental factors and ecological processes in 
boreal forest. Annu Rev Ecol Syst 20: 1–28. 
Boyce MS & McDonald LL (1999) Relating populations to habitats using resource 
selection functions. Trends Ecol Evol 14: 268–272. 


 
 
40
Cajander AK (1910) Metsiemme uudistushakkaukset toisiinsa verrattuna. In: Grotenfelt 
G, Enckell K, Suuronen P, Nylander H & Cajander E (eds) Maanhenki – 
maataloudellinen tietokirja. Otava, Helsinki, p 584–635. 
Cardillo M, MacDonald DW & Rushton SP (1999) Predicting mammal species richness 
and distributions: testing the effectiveness of satellite-derived land cover data. Landsc 
Ecol 14: 423–435. 
Carey AB, Horton SP, Biswell BL (1992) Northern spotted owl: influence of prey base 
and landscape character. Ecol Monogr 62: 223–250. 
Caswell H (1976) Community structure: a neutral model analysis. Ecol Monogr 46: 327–
354. 
Cherill AJ, McClean C, Watson P, Tucker K, Rushton SP & Sanderson R (1995) 
Predicting the distributions of plant species at the regional scale: a hierarchical matrix 
model. Landsc Ecol 10: 197–207. 
Danell K, Lundberg P & Niemelä P (1996) Species richness in mammalian herbivores: 
patterns in the boreal zones. Ecography 19: 404–409. 
Diamond JM (1972) Biogeographic kinetics: estimation of relaxation times for avifaunas 
of Southwest Pacific islands. Proc Nat Acad Sci USA 69: 3199–3203. 
Diamond JM (1975) The island dilemma: lessons of modern biogeographic studies for 
the design of natural reserves. Biol Cons 7: 129–146. 
Dobson M (1994) Patterns of distribution in Japanese land mammals. Mammal Rev 24: 
91–111. 
Dunning JB, Danielson BJ & Pulliam HR (1992) Ecological processes that affect 
populations in complex landscapes. Oikos 65: 169–175. 
Eronen P (1996) Liito-oravan (Pteromys volans) elinympäristöt Etelä- ja Keski-Suomessa 
ja niiden riittävyys ja sopivuus lajille. WWF Finland Reports 8: 21-25. 
Esseen P-A, Ehnström B, Ericson L & Sjöberg K (1997) Boreal forests. Ecol Bull 46: 16–
47. 
Fahrig L (1992) Relative importance of spatial and temporal scales in a patchy 
environment. Theor Pop Biol 41: 300–314. 
Fahrig L (1997) Relative effects of habitat loss and fragmentation on population 
extinction. J Wildl Manag 61: 603–610 
Fahrig L (1998) When does fragmentation of breeding habitat affect population survival? 
Ecol Model 105: 273–292. 
Fahrig L & Paloheimo J (1988) Determinants of local population size in patchy habitats. 
Theor Pop Biol 34: 194–213. 
Fahrig L & Merriam G (1994) Conservation of fragmented populations. Cons Biol 8: 50–
59. 
Fielding AH & Bell JF (1997) A review of methods for assessment of prediction errors in 
conservation presence/absence models. Env Cons 24: 38–49. 
Forman RTT (1995) Land mosaics – the ecology of landscapes and regions. Cambridge 
University Press, Cambridge. 
Forman RTT & Godron M (1981) Patches and structural components for a landscape 
ecology. BioScience 31: 733–740. 
Franklin JF & Forman RTT (1987) Creating landscape patterns by forest cutting: 
ecological consequences and principles. Landsc Ecol 1: 5–18. 


 
 
41
Gardner RH, Milne BT, Turner MG & O'Neill RV (1987) Neutral models for the analysis 
of broad scale landscape pattern. Landsc Ecol 1: 19–28. 
Golley FB (1994) Development of landscape ecology and its relation to environmental 
management. In: Jensen ME & Burgeron PS (eds) Volume II: ecosystem management: 
principles and applications. USDA Forest Service, General Techical Report PNW-
GTR-318, p 34–41. 
Gromtsev AN (1996) Landscape pattern of structural-dynamic organisation of taiga 
forests (the case of north-west Russian taiga zone). PhD thesis, Saint Petersburg Forest 
Academy. 
Gustafson EJ & Gardner RH (1996) The effect of landscape heterogeneity on the 
probability of patch colonisation. Ecology 77: 94–107. 
Haila Y (1990) Toward an ecological definition of an island: a northwest European 
perspective. J Biogeogr 17: 561–568. 
Haines-Young R, Green DR & Cousins SH (1993) Landscape ecology and GIS. Taylor & 
Francis, London. 
Hansen AJ & di Castri F (eds) (1992) Landscape boundaries – consequences for biotic 
diversity and ecological flows. Springer-Verlag, New York. 
Hanski I (1999) Metapopulation ecology. Oxford University Press, New York. 
Hanski IK (1998) Home range and habitat use in the declining flying squirrel Pteromys 
volans in managed forests. Wildl Biol 4: 33–46. 
Hanski IK, Stevens P, Ihalempiä, P & Selonen V (2000) Home range size, movements and 
nest site use in the Siberian flying squirrel Pteromys volans. J Mammal 81: 798–809. 
Hansson L (1977) Landscape ecology and stability of populations. Landsc Plann 4: 85–
93. 
Hargis CH, Bissonette JA & David JL (1998) The behavior of landscape metrics 
commonly used in the study of habitat fragmentation. Landsc Ecol 13: 167–186. 
Hargrove WW & Pickering J (1992) Pseudoreplication: a sine qua non for regional 
ecology. Landsc Ecol 6: 251–258. 
Harrison S & Bruna E (1999) Habitat fragmentation and large-scale conservation: what 
do we know for sure? Ecography 22: 225–232. 
Henein K & Merriam G (1990) The elements of connectivity where corridor quality is 
variable. Landsc Ecol 4: 157–170. 
Hersberger AM (1994) Landscape ecology and its potential application to planning. J 
Plann Lit 9: 1–25. 
Hokkanen H, Törmälä T & Vuorinen H (1982) Decline of the flying squirrel Pteromys 
volans L. populations in Finland. Biol Cons 23: 273–284. 
Huhtala K, Finnlund M & Korpimäki E (1976) Huuhkajan pesimäaikaisesta ravinnosta 
Vaasan läänissä. Suomenselän Linnut 11: 4–13. 
Hunter ML Jr (1990) Wildlife, forests, and forestry – principles of managing forests for 
biological diversity. Regents/Prentice Hall, New Jersey. 
James FC & McCulloch CE (1990) Multivariate analysis in ecology and systematics: 
panacea or Pandora’s box? Annu Rev Ecol Syst 21: 129–166. 
Johnson LB (1990) Analyzing spatial and temporal phenomena using Geographical 
Information Systems. Landsc Ecol 4: 31–34. 
Jongman RHG, ter Braak CJF & van Tongeren OFR (1987) Data analysis in community 
and landscape ecology. Pudoc, Wageningen. 


 
 
42
Kalliola R & Syrjänen K (1991) To what extent are vegetation types visible in satellite 
imagery? Ann Bot Fenn 28: 45–57. 
Kimmins JP (1997) Forest biology – a foundation for sustainable management. Prentice 
Hall, Upper Saddle River, New Jersey. 
Knight T-W & Morris DW (1996) How many habitats do landscapes contain. Ecology 77: 
1756–1764. 
Kotliar NB & Wiens JA (1990) Multiple scales of patchiness and patch structure: a 
hierarchical framework for the study of heterogeneity. Oikos 59: 250–260. 
Kozová M (1983) Spatial arrangement of landscape elements and possibilities of its 
expression. Ecology (CSSR) 2: 397–406. 
Leikola M (1983) “Metsää älköön autioksi hävitettäkö” – avohakkuiden aatehistoriaa. In: 
Elo K (ed) Tämä vihreän kullan maa. Suomen Luonnonsuojelun Tuki Oy, Helsinki, p 
6-12. 
Lima SL & Zollner PA (1996) Towards a behavioral ecology of ecological landscapes. 
Trends Ecol Evol 11: 131–135. 
Lindenmayer DB, Cunningham RB, Pope ML & Donnelly CF (1999) The response of 
arboreal marsupials to landscape context: a large scale fragmentation study. Ecol Appl 
9: 594–611. 
MacArthur RH & EO Wilson (1967) The theory of island biogeography. Princeton 
University Press, Princeton. 
MacDonald DW, Mitchelmore F & Bacon PJ (1996) Predicting badger sett numbers: 
evaluating methods in East Sussex. J Biogeogr 23: 649-655. 
Mattila E (1993) Paikkatietojärjestelmien virhelähteistä. Metsäntutkimuslaitoksen 
Tiedonantoja 479: 27–41. 
McGarigal K & Marks BJ (1995) FRAGSTATS – spatial pattern analysis for quantifying 
landscape structure. U.S. Forest Service, general technical report in Forest Sciences 
PNW 351. 
Merriam G (1984) Connectivity: a fundamental ecological characteristic of landscape 
pattern. In: Brandt J & Agger P (eds) Methodology in landscape ecological research 
and planning. Roskilde Universitetsforlag GeuRuc, Roskilde, Denmark, p 5–15. 
Merriam G (1995) Movement in spatially divided populations: responses to landscape 
structure. In: Lidicker WZ Jr (ed) Landscape approaches in mammalian ecology and 
conservation. University of Minnesota Press, Minneapolis, p 64–77. 
Miller DA, Leopold BD, Hurst GA & Gerard PD (2000) Habitat selection models for 
Eastern wild turkeys in central Mississippi. J Wildl Manag 64: 765–776. 
Mykrä S, Kurki S & Nikula A (2000) The spacing of mature forest habitat in relation to 
species-specific scales in managed boreal forests in NE Finland. Ann Zool Fenn 37: 
79–91. 
Mäkelä A (1996) Liito-oravan (Pteromys volans L.) ravintokohteet eri vuodenaikoina 
ulosteanalyysin perusteella. WWF Finland Reports 8: 54–58. 
Naveh Z (1982) Landscape ecology as an emerging branch of human ecosystem science. 
Adv Ecol Res 12: 189–237. 
Ognev SI (1940) Mammals of the U.S.S.R. and adjacent countries. Vol. VI. Israel 
program for scientific translations, Jerusalem. 
Orians GH & Wittenberger JF (1991) Spatial and temporal scales in habitat selection. Am 
Nat 137 Suppl: 29–49. 


 
 
43
Pearson SM, Turner MG, Gardner RH & O'Neill RV (1996) An organism-based 
perspective of habitat fragmentation. In: Szaro RC & Johnston DW (eds) Biodiversity 
in managed landscapes. Oxford University Press, New York, p 77–95. 
Pickett STA & Cadenasso ML (1995) Landscape ecology: spatial heterogeneity in 
ecological systems. Science 269: 331–334. 
Pickett STA & White PS (1985) The ecology of natural disturbance and patch dynamics. 
Academic Press Inc, San Diego. 
Pozdnyakov SA (1997) Notes on the mammal fauna of the Kostamuksha nature reserve. 
Suomen Ympäristö 124: 195–201. 
Pukkala T (1985) Metsän kaukokartoituksen perusteet. Silva Carelica 4: 1–166. 
Putman RJ (1984) Facts of faeces. Mammal Rev 14: 79–97. 
Pyykkö J (ed) (1996) Survey in Russian Karelian natural forests in Vienansalo. WWF 
Finland Report, Helsinki. 
Raivio S (1992) Bird communities in fragmented coniferous forests: the importance of 
quantitative data and adequate scaling. PhD thesis, University of Helsinki. 
Rassi P, Itkonen P, Lindholm T & Salminen P (1996) Vanhojen metsien suojelu Pohjois-
Suomessa. Suomen Ympäristö 30: 1–111. 
Rassi P, Alanen A, Kanerva T & Mannerkoski I (eds) (2000) Suomen lajien uhanalaisuus 
2000. 
Ministery 
of 
the 
Environment, 
Helsinki. 
http://www.vyh.fi/luosuo/lumo/lasu/uhanal/uhanal.htm. 
Reunanen P (1998) Laji levinneisyytensä laidalla – Pohjois-Suomen liito-oravat. Luonnon 
Tutkija 102: 29–30. 
Risser PG, Karr JR, & Forman RTT (1984) Landscape ecology – Directions and 
approaches. Illinois Natural History Survey Special Publication No. 2, Champaign. 
Rita H & Ranta E (1993) On analysing species incidence. Ann Zool Fenn 30: 173–176. 
Robinson GR, Holt RD, Gaines MS, Hamburg SP, Johnson ML, Fitch HS & Martinko EA 
(1992) Diverse and contrasting effects of habitat fragmentation. Science 257: 524–
526. 
Rolstad J (1991) Consequences of forest fragmentation for the dynamics of bird 
populations: conceptual issues and evidence. Biol J Linn Soc 42: 149–163. 
Rolstad J & Wegge P (1987) Distribution and size of capercaillie leks in relation to old 
forest fragmentation. Oecologia 72: 389–394. 
Rolstad J & Wegge P (1989) Capercaillie Tetrao urogallus populationsand modern 
forestry – a case study for landscape ecological studies. Finnish Game Res 46: 43–52. 
Saunders DA, Hobbs RJ & Margules CR (1991) Biological consequences of ecosystem 
fragmentation: a review. Cons Biol 5: 18–32. 
Schumaker NH (1996) Using landscape indices to predict habitat connectivity. Ecology 
77: 1210–1225. 
Selonen V & Hanski IK (2000) Natal dispersal in the Siberian flying squirrel (Pteromys 
volans). Proceedings of the 80
th Annual Meeting of American Society of 
Mammalogists, Durham, USA. 
Selonen V, Hanski IK, Stevens P (2001) Space use of the Siberian flying squirrel 
Pteromys volans in fragmented landscapes. Ecography, in press. 
Skarén U (1978) Liito-oravan esiintymisestä ja talviravinnosta Pohjois-Savossa. Luonnon 
Tutkija 5: 171–173. 


 
 
44
Sokal RR & Rohlf FJ (1995) Biometry: the principles and practice of statistics in 
biological research. Freeman, San Francisco. 
Soulé ME (eds) (1980) Conservation biology: an evolutionary-ecological perspective. 
Sinauer Assosiates, Inc. Publishers, Sunderland, Massachusetts. 
Soulé ME (1985) What is conservation biology? BioScience 35: 727–734. 
Sousa P (1984) The role of disturbance in natural communities. Annu Rev Ecol Syst 15: 
353–391. 
Spies TA & Franklin JF (1996) The diversity and management of old-growth forests. In: 
Szaro RC & Johnston DW (eds) Biodiversity in managed landscapes. Oxford 
University Press, New York, p 298–314. 
Stamps JA, Buechner M & Krishnan VV (1987) The effect of edge permeability and 
habitat geometry on emigration from patches of habitat. Am Nat 129: 533–552. 
Star J & Estes J (1990) Geographic Information Systems – an introduction. Prentice Hall, 
New Jersey. 
Sulkava R, Eronen P & Storrank B (1994) Liito-oravan esiintyminen Helvetinjärven ja 
Liesjärven kansallispuistoissa sekä ympäröivillä valtionmailla 1993. Metsähallituksen 
luonnonsuojelujulkaisuja sarja A 18: 1–29.  
Taulman JF, Smith KG & Thill RE (1998) Demographic and behavioral responses of the 
southern flying squirrel to experimental logging in Arkansas. Ecol Appl 8: 1144–1155. 
Taylor PD, Fahrig L, Henein K & Merriam G (1993) Connectivity is a vital element of 
landscape structure. Oikos 68: 571–572. 
Tiebout HM & Anderson RA (1997) A comparison of corridors and intrinsic connectivity 
to promote dispersal in transient successional landscapes. Cons Biol 11: 620–627. 
Tilman D, May RM, Lehman CL & Nowak MA (1994) Habitat destruction and the 
extinction debt. Nature 371: 65–66. 
Tischendorf L (2001) Can landscape indices predict ecological processes consistently? 
Landsc Ecol 16: 235–254. 
Tischendorf L & Fahrig L (2000a) On the usage of landscape connectivity. Oikos 90: 7–
19. 
Tischendorf L & Fahrig L (2000b) How should we measure landscape connectivity. 
Landsc Ecol 15: 633–641. 
Tokola T & Heikkilä J (1997) Improving satellite image based forest inventory by using a 
priori site quality information. Silva Fennica 31: 67–78. 
Tomppo E (1991) Satellite image-based National Forest Inventory of Finland. Int Arch 
Phot Rem Sens 28: 419–424. 
Tomppo E (1993) Multi-source National Forest Inventory of Finland. The Finnish Forest 
Research Institute, Research Papers 444: 52–59. 
Tomppo E & Katila M (1993) Satelliittipohjainen valtakunnan metsien inventoinnin 
tietotuotanto. Metsäntutkimuslaitoksen tiedonantoja 479: 21–26. 
Tomppo E, Katila M, Mäkelä J & Peräsaari J (1998) Kunnittaiset metsävaratiedot 1990–
94. Folia Forestalia 4B: 619–839. 
Turner MG (1989) Landscape ecology: the effect of pattern on process. Annu Rev Ecol 
Syst 20: 17–197. 
Turner MG & Gardner RH (eds) (1991) Quantitative methods in landscape ecology. 
Springer Verlag, New York. 


 
 
45
Urban DL, O´Neill RV & Shugart HH (1987) Landscape ecology – a hierarchical 
perspective can help scientists understand spatial patterns. BioScience 37: 119–127. 
White PS (1979) Pattern, process and natural disturbance in vegetation. Bot Rev 3: 229–
299. 
Wiens JA (1976) Population responses to patchy environments. Annu Rev Ecol Syst 7: 
81–120. 
Wiens JA (1989) Spatial scaling in ecology. Funct Ecol 3: 385–397. 
Wiens JA (1992) What is landscape ecology, really? Landsc Ecol 7: 149–150. 
Wiens JA (1995) Landscape mosaics and ecological theory. In: Hansson L, Fahrig L & 
Merriam G (eds) Mosaic landscapes and ecological processes. Chapman & Hall, 
London, p 1–26. 
Wiens JA, Crawford CS & Gosz JR (1985) Boundary dynamics: a conceptual frame work 
for studying landscape ecosystems. Oikos 45: 421–427. 
Wiens JA, Addicott JF, Case TJ & Diamond J (1986) Overview: The importance of 
spatial and temporal scale in ecological investigations. In: Diamond J & Case TJ (eds) 
Community ecology. Harper & Row. Publishers, New York. 
Wilcox BA (1980) Insular ecology and conservation. In: Soulé ME (ed) Conservation 
biology: an evolutionary-ecological perspective. Sinauer Assosiates, Inc. Publishers, 
Sunderland, Massachusetts, p 95–117. 
Wilson DE & Reeder DM (1993) Mammal species of the world – a taxonomic and 
geographical reference. Smithsonian Institution Press, Washington. 
Wistbacka R, Köykkäri S, Jakobsson R & Nyman B (1996) Flygekorrens förekomst och 
biotopval i Jakobstad och Larsmo 1989-1993. WWF Finland Reports 8: 26–34. 
With KA (1997) The application of neutral landscape models in conservation biology. 
Cons Biol 11: 1069–1080. 
With KA & Crist TO (1995) Critical thresholds in species responses to landscape 
structure. Ecology 76: 2446–2459. 
With KA & King AW (1997) The use and misuse of neutral models in ecology. Oikos 79: 
219–229. 
With KA & King AW (1999) Dispersal success on fractal landscapes: a consequence of 
lacunarity thresholds. Landsc Ecol 14: 73–82. 
With KA, Gardner RH & Turner MG (1997) Landscape connectivity and population 
distribution in heterogeneous environments. Oikos 78: 151–169. 
Zollner PA (2000) Comparing the landscape level perceptual abilities of forest sciurids in 
fragmented agricultural landscapes. Landsc Ecol 15: 523–533. 
Zonneveld IS (1989) The land unit – a fundamental concept in landscape ecology, and its 
applications. Landsc Ecol 3: 67–86. 
Zonneveld IS (1990) Scope and concepts of landscape ecology as an emerging science. 
In: Zonneveld IS & Forman RTT (eds) Changing landscapes: an ecological 
perspective. Springer-Verlag, New York, p 5–20. 
Åberg J, Jansson G, Swenson JE & Angelstam P (1995) The effect of matrix on the 
occurrence of the hazel grouse (Bonasa bonasia) in isolated habitat fragments. 
Oecologia 103: 265–269. 
Åberg J (2000) The occurrence of hazel grouse in the boreal forest – effects of habitat 
composition at several spatial scales. PhD thesis, Swedish University of Agricultural 
Sciences.
