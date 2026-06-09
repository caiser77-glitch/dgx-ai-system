--- 
source: Landscape and Urban Planning 1999 Kliskey.pdf
--- 

Simulating and evaluating alternative resource-use strategies
using GIS-based habitat suitability indices
A.D. Kliskeya,*, E.C. Lofrothb, W.A. Thompsonc, S. Brownd, H. Schreierd
aDepartment of Geography, University of Canterbury, Christchurch, New Zealand
bWildlife Branch, BC Environment, Victoria, B.C., Canada
cForest Economics and Policy Analysis, University of British Columbia, Vancouver, B.C., Canada
dResource Management and Environmental Studies, University of British Columbia, Vancouver, B.C., Canada
Received 17 February 1999; accepted 23 October 1999
Abstract
Geographic information system (GIS) based models were developed for mapping the habitat suitability of pine marten
(Martes americana) and woodland caribou (Rangifer tarandus) using habitat suitability indices (HSI). Habitat suitability was
simulated for four timber harvesting strategies. These included an existing harvesting strategy and three alternative strategies
targeted speci®cally at maintenance of wildlife habitat and wilderness protection. The alternative strategy that restricted
harvesting from some mature-age stands provided the optimal performance in balancing caribou habitat protection and marten
habitat protection when compared using multiple accounts analysis. However, the alternative strategy that maximised caribou
habitat retention provided the optimal performance in balancing both wildlife and timber objectives when compared using
multiple accounts analysis. The approach demonstrates how the use of HSI models can be extended from simple habitat
mapping to scenario testing and, coupled with GIS, can assist in the prediction of the outcomes of alternative resource-use
scenarios. # 1999 Elsevier Science B.V. All rights reserved.
Keywords: Geographic information systems; Habitat suitability index; Simulation modeling; Timber harvesting; Wildlife
1. Introduction
The demands for forest harvesting and wildlife pro-
tection are a common source of resource con¯ict in
natural landscapes (Rochelle, 1994; Lindenmayer and
Franklin, 1997). Efforts to address such con¯ict have
given rise to various conceptual approaches to resource
management, such as, sustainable land management
(Hurni, 1997), ecosystem management (Slocombe,
1993), and integrated environmental management
(Born and Sonzogni, 1995). Geographic information
systems (GIS) have an invaluable role in addressing
resource decisions (Franklin, 1994). Attempts to
incorporate wildlife resources along with other activ-
ities for resource management on a spatial scale have
included the use of GIS to develop habitat suitability
models (Donovan et al., 1987), and the implementation
of bioclimatic analysis (Lindenmayer et al., 1991).
Habitat suitability index (HSI) models are widely
used in North America and allow wildlife to be
represented with other natural resource information
Landscape and Urban Planning 45 (1999) 163±175
* Corresponding author. Tel.: 64-3-3642987; fax: 64-3-
3642907.
E-mail address: andyk@geog.canterbury.ac.nz (A.D. Kliskey)
0169-2046/99/$20.00 # 1999 Elsevier Science B.V. All rights reserved.
PII: S 0 1 6 9 - 2 0 4 6 ( 9 9 ) 0 0 0 5 6 - 0


by recording or predicting the response of a species to
its environment (Schamberger and O'Neil, 1986).
Various factors beside habitat may determine animal
presence or abundance, and measures of habitat suit-
ability may include only a limited number of factors
that determine population levels. HSI models attempt
to quantify habitat quality using habitat attributes
considered important to the wildlife species. An
HSI provides a 0.0±1.0 index of habitat suitability
determined by aggregating one or more suitability
scores for life-requisite components, such as food
requirements (Lancia et al., 1982). The HSI for a
species at a location indicates relative habitat quality
rather than actual population levels. HSI models are
based on the assumptions that a species will select and
use areas that are best able to satisfy its life requisites,
and consequently, that greater use will occur in higher
quality habitat (Schamberger and O'Neil, 1986).
Limitations of HSI models include the lack of
linearity between wildlife density and individual habi-
tat parameters, the inferiority of simple indices to
those based on multivariate analysis, the variability
of habitat use regardless of life stage or season,
inadequacy of a species' observed density as an
indicator of habitat quality, and, the effect of predators
on the abundance of their prey (Van Horne, 1983;
Laymon and Barrett, 1986). Robel et al. (1993), for
example, found poor correlation between HSI values
and ground counts of beaver (Castor canadensis)
colonies. More recently Bender et al. (1996) suggest
that habitat modeling should account for variability in
HSI scores and demonstrate a bootstrapping approach
to evaluating con®dence intervals for habitat suitabil-
ity models.
Spatially explicit HSI models permit wildlife to be
considered along with other resource activities for
watersheds, landscapes and regions. GIS databases
provide a source of habitat information for developing
spatial HSI models. Aspinall and Veitch (1993) review
the use of spatial analysis and GIS overlay functions to
produce habitat suitability indices. Over small areas
numerous habitat variables can be measured and
included in a spatial model, but over larger areas
fewer variables are usually available so that general-
izations about species habitat requirements must be
made (Donovan et al., 1987). The application of GIS
in wildlife habitat analysis has become extensive
(Pereira and Itami, 1991) with spatial models pro-
duced for various avian and mammalian species. GIS-
based habitat analyses of avian species include wood
stork (Mycteria americana) (Hodgson et al., 1988),
sandhill crane (Grus canadensis tabida) (Herr and
Queen, 1993), scrub jay (Aphelocoma coerulescens
coerulescens) (Breininger et al., 1991; Duncan et al.,
1995), sage grouse (Centrocercus urophasianus)
(Homer et al., 1993), ruffed grouse (Bonasa umbellus)
(Rickers et al., 1995), curlew (Numenius arquata)
(Aspinall and Veitch, 1993), kestrel (Falco sparverius)
(Lyon, 1983), and cowbirds (Molothrus ater) (Coker
and Capen, 1995). Mammalian studies include bobcat
(Felis rufus) (Lancia et al., 1982), white-tailed deer
(Odocoileus
virginianus)
(Ormsby
and
Lunetta,
1987),
black-tailed
deer
(Odocoileus
hemionus)
(Chang et al., 1995), moose (Alces alces) (Laperriere
et al., 1980), woodland caribou (Rangifer tarandus)
(Brown et al., 1994), black bear (Ursus americanis)
(Clark et al., 1993; Rudis and Tansy, 1995), red
squirrel (Tamiasciurus hudsonicus) (Pereira and Itami,
1991), and the eastern barred bandicoot (Perameles
gunni) (Reading et al., 1996). While these studies
highlight the widespread development of GIS-based
HSI models, their use for representing wildlife values
in resource management remains largely untapped in
North America.
In Australia distribution mapping, based on biocli-
matic analyses, has been used to support species
management
including
for
Leadbeater's
possum
(Gymnobelideus leadbeateri) (Lindenmayer et al.,
1991), eastern grey kangaroo (Macropus giganteus),
western grey kangaroo (M. fuliginosus), red kangaroo
(M. rufus) (Skidmore et al., 1996), greater glider
(Petauroides volans) (Lindenmayer et al., 1995),
and helmeted honeyeater (Lichenostomus melanops
cassidix) (Pearce and Lindenmayer, 1998). Notwith-
standing the usefulness of such other spatial mapping
techniques for wildlife, this paper focuses on the
application of HSI which are in common use in North
American natural resource and wildlife agencies
(Rickers et al., 1995).
By extending the use of HSI models from simple
habitat mapping to scenario testing GIS can assist in
the prediction of the outcomes of alternative resource-
use strategies in ecosystem studies (Ball, 1994). Rick-
ers et al. (1995) demonstrate the application of a GIS-
based HSI model for a single species using a single
resource-use strategy. That work illustrates the ability
164
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


to predict the impact on wildlife habitat resulting from
a future management activity. In this paper, we apply
pine marten (Martes americana) and woodland car-
ibou (Rangifer tarandus) HSI models for scenario
testing of multiple resource-use strategies in the North
Columbia Mountains of British Columbia.
2. Methodology
Spatially explicit HSI models were developed using
GIS for pine marten and woodland caribou. Woodland
caribou is a threatened species that is potentially at
risk from loss of habitat resulting from forestry activ-
ities (Simpson et al., 1996; Seip, 1998). The North
Columbia Mountains have been identi®ed as a key
area for the maintenance of the Southern Selkirk
woodland caribou population. Marten are an integral
member of the forest community, and because of their
status as a climax forest species are an important
indicator of forest health and stability (Ruggiero
et al., 1994), being sensitive to habitat alterations
and adversely affected by diminishing old-growth
(Buskirk et al., 1994). Four alternative resource-use
strategies (timber harvesting plans) were modeled and
marten and caribou habitat simulated for each strategy.
Each strategy was evaluated by its ability to balance
recognised wildlife and forestry goals (Gunton, 1998).
In this study wildlife goals were de®ned by the land
area of marten and caribou habitat maintained, while
timber harvesting goals were de®ned by the average
volume of timber harvested annually and the value of
that timber.
2.1. An HSI model for pine marten
The habitat suitability model developed for marten
in the North Columbia Mountains was based on the
United States Fish and Wildlife Service HSI for
marten (Allen, 1982), the species-habitat relationship
for marten in the Southern Interior Eco-province of
British Columbia (Ritcey et al., 1988), and the pro-
posed HSI for marten in the Sub-boreal Spruce Bio-
geoclimatic Zone of British Columbia (Lofroth and
Bianci, 1991). An ideal HSI model has a direct linear
relationship between the index and carrying capacity
(United States Fish and Wildlife Service, 1981). In
reality this is rarely attained, thus criteria for accep-
table model outputs must be de®ned. The marten HSI
model outputs were considered acceptable where suit-
ability ratings for marten habitat were `reasonable',
considering knowledge of the ecology of the species
(United States Fish and Wildlife Service, 1981), and
suitability ratings correspond to actual levels of mar-
ten habitat use as indexed by track counts or other
indices. The model described the life requisites for
marten and the structural features of the forest (or
habitat variables) which help to meet those life requi-
sites. The model de®ned year round habitat suitability
for marten but speci®cally accounted for winter habi-
tat requirements which have been identi®ed as critical
for the species (Raine, 1983). Habitat variables can not
always be mapped for a spatially explicit model,
therefore surrogate or model variables were used to
predict habitat (Table 1). The model variables were
chosen on the premise that `if modi®ed they would be
expected to affect the capability of the habitat to
support the evaluation species' (United States Fish
and Wildlife Service, 1981). Thus, the model variables
must be related to the capability of the habitat to
support the species, there must be a basic understand-
ing of the variables to the species' habitat needs, and
the variables should be practical to measure within the
constraints of model application.
Identi®able life requisites for marten include food,
resting sites, foraging sites, cover, and maternal den
site requirements. Each of the ®ve life requisites was
de®ned by one or more of six habitat variables, where
each habitat variable was in turn de®ned by one or
more of ®ve mapped model variables (Table 1). The
reasoning for the selection of habitat and model vari-
ables for each life requisite is as follows:
1. Small mammals such as voles (Clethrionomys spp.
and Microtus spp.) have commonly been identi®ed
as primary prey items for marten although
snowshoe hare is also known to be important
(Buskirk and MacDonald, 1984; Hargis and
McCullough, 1984). Site productivity (and there-
fore moisture regime), low shrub cover, and coarse
woody debris are important habitat variables in
determining their abundance (Ritcey et al., 1988).
Surrogate or model variables used to represent
these habitat variables are seral stage, site class
and dominant species (Lofroth and Bianci, 1991).
2. Marten require resting sites to meet their thermo-
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
165


regulatory requirements (Brown and Lasiewski,
1972). These sites are associated with coarse
woody debris, snags, and large trees (Buskirk,
1984; Buskirk et al., 1989) which provide crucial
access to subnivian (below snow) sites (Corn
and Raphael, 1992). This requisite is met by three
model variables Ð seral stage, site class, and
dominant species (Ritcey et al., 1988).
3. Foraging sites for prey are also generally sub-
nivian, and access to these sites for marten
provided by coarse woody debris, snags, and
canopy closure (Steventon and Major, 1982;
Bateman, 1986). These habitat variables are
characterised by seral stage, site class and canopy
closure (Ritcey et al., 1988).
4. Avoidance of mammalian and avian predators
may be provided by availability of trees for escape
and overhead canopy cover (Buskirk and Rug-
giero, 1994) and is represented by two model
variables Ð canopy closure and biogeoclimatic
zone (Ritcey et al., 1988).
5. Female marten show preferential use of dense,
mature softwood stands for natal den sites and
also utilise logs and snags (Steventon and
Major, 1982; Wynne and Sherburne, 1984). This
requisite is largely met by habitat measures of
coarse woody debris and snags which are
characterised by seral stage and site class (Ritcey
et al., 1988).
The relative importance of model variables in meeting
life requisites for marten were combined into a single
equation (Table 2) that calculated a suitability index
for marten habitat (Table 3). Habitat suitability was
scaled to produce an index value between 0.0 (unsui-
table habitat) and 1.0 (optimal habitat) (Table 3). This
combined into one HSI equation the HSI relationships
for each life requisite as defined by model variables
(Lofroth and Bianci, 1991) using the approach
adopted by United States Fish and Wildlife Service
(1981). Geometric or arithmetic means used in these
equations depend on whether the relationships of the
variables used in the equations are compensatory or
additive (United States Fish and Wildlife Service,
1981). The model variables were considered to be
compensatory in terms of their relationship to each
Table 1
Habitat and model variables providing life requisites for marten (based on Lofroth and Bianci, 1991)
Life requisite
Habitat variable
Model variable
Food
Coarse woody debris
Seral stage
Site class
Low shrub cover
Dominant species
Site class
Soil moisture
Site class
Resting site
Coarse woody debris
Seral stage
Site class
Snag density
Seral stage
Site class
Tree size
Seral stage
Site class
Dominant species
Security (cover)
Coniferous canopy cover
Biogeoclimatic zone
Canopy closure
Foraging site
Coarse woody debris
Seral stage
Site class
Snag density
Seral stage
Site class
Coniferous canopy cover
Biogeoclimatic zone
Maternal Den site
Coarse woody debris
Seral stage
Site class
Snag density
Seral stage
Site class
166
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


other and their value to marten, and were consequently
described using a geometric mean (Table 2).
HSI models are validated by testing variability
of the model with ®eld data (United States Fish and
Wildlife Service, 1981), ideally representing actual
levels of marten habitat use as indexed by track
counts.
Due
to
time
and
®nancial
constraints,
existing fur harvest trapping data for adult marten
in the study area were used to validate the marten
model. Trap capture data over two seasons (1993/
1994, 1994/1995) for 32 trapsets along two traplines
in the Tangier watershed were used as a measure
of actual habitat use and compared to the suitability
ratings computed using the model (i.e., comprising
model variables as detailed in Tables 2 and 3). A
Spearman rank correlation coef®cient was calculated
(r  0.75, p < 0.001) between the marten HSI and
catch rates at trap locations indicating a positive
correlation between the model and actual use as
measured by trap data.
2.2. An HSI model for woodland caribou
The caribou suitability evaluation model for the
North Columbia Mountains was based on the Wood-
land Caribou Cumulative Effects Analysis Model
(Summer®eld et al., 1985) and incorporated species-
habitat relationships that were observed in the area
(Rominger and Oldemeyer, 1989; Servheen and Lyon,
1989; Terry et al., 1996). The model emphasised key
topographic and vegetative factors that are of impor-
tance to caribou during the limiting periods of early
winter, late winter, and spring. The suitability evalua-
tion method was similar to that for the pine marten but
used an arithmetic mean and is detailed by Brown
et al. (1994). Validation of the caribou HSI model was
performed using radio telemetry data for woodland
caribou over two seasons (Brown et al., 1994).
2.3. Model implementation Ð study area
The study area for the scenario-testing was the
Tangier River watershed (28 748 ha) in the North
Columbia Mountains of British Columbia. The lower
slopes (<1300 m) of the watershed comprise the Inter-
ior Cedar Ð Hemlock biogeoclimatic zone, the mid to
upper slopes (1300±1800 m) comprise the Englemann
Spruce±Subalpine Fir biogeoclimatic zone, while the
highest elevations (>1800 m) comprise the Alpine
Tundra biogeoclimatic zone. A spatial database for
the Tangier watershed was assembled using digital
topographic data sets at 1 : 20 000 scale (British
Columbia
Ministry
of
Environment
and
Parks,
1988) to provide topography, hydrology and road
network information. Forest resource inventory data
Table 2
Marten HSI equation for North Columbia Mountains (based on
Lofroth and Bianci, 1991)
Habitat suitability index:
HSI 

3SRBSZ  SRSC  SRDS
6

 SRCC  SRCC
2


s
Habitat suitability ratings for model variables:
SRBSZ  habitat suitability rating for biogeoclimatic zone
SRSC  habitat suitability rating for site class
SRDS  habitat suitability rating for dominant species
SRCC  habitat suitability rating for canopy closure
SRCC  habitat suitability rating for seral stage
Table 3
Model variables for marten habitat (based on Ritcey et al., 1988)
Variable
Habitat suitability
High
Moderate
Low
Nil
Biogeoclimatic zone
Engelmann spruce±subalpine fir
Interior cedar±Hemlock
±
Alpine Tundra
Site class
Hygric
Mesic
Xeric
Very xeric
Dominant species
Engelmann spruce
W. Red cedar
Birch
Other species
True firs
Hemlock
Aspen
Douglas fir
Lodgepole pine
Seral stage
Old growth >150 years
Mature 80±150 years
Young 40±80 years
Other<40 years
Canopy closure
30±69%
20±29%
<20%
0%
70±80%
>80%
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
167


was obtained from BC Ministry of Forests digital
forest cover and inventory ®les (British Columbia
Ministry of Forests, 1990), also at 1 : 20 000 scale.
These companion datasets are the largest scale of
digital mapping available at provincial level in British
Columbia providing good quality topographic and
silvicultural data for watershed analysis.
To determine the habitat suitability, a forest man-
agement theme was used within the GIS incorporating
the cut-blocks, and management units outside the
operable forest. Utilizing GIS overlay techniques,
biogeoclimatic and structural characteristics were
assigned to each forest management unit from topo-
graphic data. The GIS database enables the HSI for
each forest management unit to be calculated, and
subsequently habitat suitability determined across the
entire watershed.
2.4. Modeling resource-use scenarios Ð timber
harvesting strategies
Timber harvesting was modeled using forest growth
and harvest models developed for the North Columbia
Mountains. These were based on a spatial planning
approach for the Revelstoke Forest District (Price and
Blake, 1993), and are detailed by Thompson et al.
(1994). A harvest layout was used where cut-blocks
were identi®ed based on standing timber, site and
growing conditions. The Tangier watershed was
divided into 500 productive forest cut-blocks and
300 non-forested management units ranging from 1
to 20 ha in area. Dominant species and site quality for
each unit were obtained from the forest cover data
(British Columbia Ministry of Forests, 1990). Simula-
tion modeling of forest dynamics was generated using
a forest stand growth model (Thompson et al., 1995)
based on timber supply guidelines for the Revelstoke
Timber Supply Area (British Columbia Ministry of
Forests, 1993; Price and Blake, 1993). The forest
dynamics were modeled for a 120-year rotation using
a spatially explicit timber supply model (Nelson,
1993) to maintain adjacency constraints. Adjacency
constraints were combined with a 20 year green-up
period restriction to ensure no cutblock was harvested
while any of its neighbors are under 20 years of age.
This was solved using a Monte±Carlo sampling heur-
istic and as such solutions being utilized were not
necessarily optimal. This harvest strategy incorpo-
rated the basic timber harvesting guidelines and was
the baseline strategy against which other harvest
strategies were compared. The constraints of this
baseline strategy re¯ected the operational harvesting
constraints used in British Columbia.
In addition to the baseline strategy three harvesting
strategies were developed to re¯ect resource-use alter-
natives under a range of wildlife constraints (Table 4).
The primary management input to the strategies was
the choice of a harvesting schedule, including the
option to exclude areas from harvest. Each strategy
included a restriction on cutting any block of timber
when any adjacent block was <20 years of age.
An old growth retention strategy modi®ed the base-
line strategy by maintaining at least 60% of the current
old growth forest (stands aged 120 years or greater)
through time (Table 4). Nearly 50% of the existing old
growth is outside the commercial forest. Slightly over
20% (1000 ha) of the old growth within the com-
mercial forest must be maintained at any one time.
This was accomplished by scheduling the harvest of
these areas on an even ¯ow basis for a 120-year
rotation.
A caribou management strategy was designed to
protect critical winter habitat for caribou. Early winter
habitat was selected since the baseline strategy
showed that logging had the greatest impact on car-
ibou habitat in the early winter, while late winter and
spring habitats were impacted little (Brown et al.,
1994). The caribou management strategy was devel-
Table 4
Four alternative timber harvest strategies
Strategy
Objective
Condition
Baseline
Timber volume
Greenup and adjacency
Old growth
Retention of old growth forest
Minimum 60% stands aged 120 years or older excluded
Caribou
Maintenance of high quality habitat
Minimum 600 ha early winter caribou habitat excluded
Park
Wilderness park scenario
83% of watershed preserved
168
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


oped using a tabu search heuristic (Glover and
Laguna, 1995) that maximized the timber volume
harvested, while maintaining a minimum of 600 ha
of early winter caribou habitat (Table 4). Tabu search
is a computational technique for seeking near-optimal
solutions that imposes constraints to avoid speci®ed
conditions (Glover and Laguna, 1995), and which
have become widely accepted in timber harvest appli-
cations (Bettinger et al., 1997).
A park strategy was designed to exclude harvesting
within a proposed wilderness park boundary, Serenity
Peaks, encompassing the northern 83% (23 636 ha) of
the Tangier watershed (Table 4). No timber harvesting
or road building would be allowed in this area. The
remaining 17% of the watershed would be harvested
under the baseline strategy.
Habitat suitability was modeled for both marten and
caribou under each strategy by applying the respective
HSI models to the changing forest conditions as
simulated by each alternative timber harvest schedule
over a 120-year rotation. The alternative resource-use
scenarios were evaluated in terms of their contribution
to wildlife and timber objectives using multiple
accounts analysis (Thompson et al., 1994) where
the outcome for each scenario is plotted as a point
on an n-dimensional graph, with each dimension
corresponding to one account. The accounts consid-
ered in this study were minimum high quality marten
habitat,
minimum
high
quality
caribou
habitat,
volume of timber harvested, and net present value
of timber harvested (at 5% real discount rate). Each
strategy was evaluated by ranking the performance
across the multiple accounts for all scenarios.
3. Results
The Tangier watershed was classi®ed for marten
habitat suitability. Given the different life requisite
constraints, the watershed provides 7804 ha of high
quality habitat for marten representing 27% of the
watershed. Habitat suitability mapping for woodland
caribou was used to compare habitat between species,
high quality caribou habitat accounting for 4180 ha or
15% of the watershed.
The coincidence of marten and caribou habitat was
determined by overlaying the habitat suitability map-
ping for each species (Fig. 1). Areas of both high
quality marten and resultant caribou habitat comprise
12% of the watershed, while 15% of the watershed is
good marten habitat but lower quality caribou habitat,
and only 4% of the area is high quality caribou and
lower quality marten habitat. The area of coincidence
between high quality marten and caribou habitat is
located predominantly on the mid-slopes of the valley
in the east and northeast of the watershed. This
represents 45% of high quality marten habitat, and
85% of high quality caribou habitat, in the watershed.
Marten and caribou habitat suitabilities were mod-
elled for each harvest strategy over the 120 year
rotation (Figs. 2 and 3). Early winter caribou habitat
was examined over time since the caribou manage-
ment strategy maintains habitat for this critical season.
The baseline strategy reduced high quality marten
habitat over 70 years, while high quality caribou
habitat was reduced over 50 years (Figs. 2 and 3).
The old growth strategy reduced caribou habitat over
the ®rst 30 years, recovering after 90 years, while
marten habitat was maintained at a consistently high
level (Figs. 2 and 3). The caribou strategy maintained
early winter caribou habitat at close to 600 ha or
greater throughout the planning period as it was
designed to do (Fig. 3). Under the same scenario
Fig. 1. Interaction between simulated marten and caribou habitat
in the Tangier watershed.
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
169


marten habitat showed a steady decline over the 120-
year rotation (Fig. 2). The park strategy initially
reduces caribou habitat over 30 years but increases
retention of habitat after 90 years (Fig. 3). Marten
habitat was maintained at a consistent level under the
park strategy (Fig. 2). Comparing minimum area of
marten habitat retained during each harvest schedule,
the baseline and caribou strategies performed least
well while the park strategy maximized habitat reten-
tion. Comparing retention of caribou habitat during
each harvest schedule, the baseline strategy performed
least well while the old growth strategy maximized
caribou habitat retention.
The comparison between habitat change for each
species over the harvest rotation provides an indica-
tion of how well each resource-use scenario performs
with respect to wildlife habitat. In particular, it is
possible to assess this performance over the full
duration of the rotation. Each scenario has a different
impact on habitat for marten and caribou. Multiple
accounts analysis provides a comparison of the mini-
mum area of marten habitat and the minimum area of
caribou habitat retained under each scenario over the
120 year rotation (Fig. 4 and Table 5). The baseline
strategy provides minimal retention of habitat for both
Fig. 2. Retention of simulated high quality marten habitat under
four timber harvest strategies.
Fig. 3. Retention of simulated high quality caribou habitat under
four timber harvest strategies.
Fig. 4. Trade-off between marten habitat and caribou habitat under
four timber harvest strategies.
Table 5
Multiple accounts comparison of alternative timber harvest strategies
Strategy
Minimum marten
habitat (ha)
Minimum caribou
habitat (ha)
Mean annual timber
harvest (`000m3)
Timber value
($'000,000)
Baseline
4825
3690
16.3
2.8
Old growth
6033
4100
13.1
2.2
Caribou
4945
4050
16.4
2.4
Park
7161
4045
5.9
0.2
170
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


species while the park strategy retains the greatest area
of habitat for both species (Fig. 4). Although the
caribou strategy maximizes retention of crucial early
winter habitat for caribou it provides only moderate
retention of marten habitat (Fig. 4). This suggests that
managing for caribou may not necessarily be mutually
bene®cial to marten. However, the old-growth strategy
appeared to optimize the trade-off between marten and
caribou habitat retention at moderate areas of habitat
for each species (Fig. 4).
Multiple accounts analysis of the contribution of
each scenario to wildlife and forestry objectives
(Fig. 5 and Table 5) shows the mean annual harvest
volume of timber and the minimum area of high
quality marten habitat for each scenario. On these
two axes a trade-off frontier is created with the base-
line strategy at one extreme, providing maximum
timber harvest and minimal marten habitat, and the
park strategy at the other extreme, providing minimum
timber harvest and maximum marten habitat (Fig. 5).
The caribou strategy provides a similar trade-off
between timber harvest and marten habitat to the
baseline strategy, while the old-growth strategy pro-
vides a balance between these objectives with
13 100 m3 of timber and a minimum of 6000 ha of
high quality marten habitat (Fig. 5).
The strategies are evaluated by ranking the perfor-
mance of each strategy (Table 5) with respect to each
account (Table 6). Thus, the park strategy performs
best for marten habitat (account 1), the old growth
strategy performs best for caribou habitat (account 2),
the caribou strategy performs best for timber harvest
(account 3), and the baseline strategy performs best for
timber value (account 4). The old-growth strategy
demonstrates the best performance of the management
scenarios for the joint wildlife objectives (accounts 1
and 2) (Table 6). Both the old growth and caribou
strategies perform similarly for the combined wildlife
and timber harvest objectives (accounts 1±3) (Table
6). Overall, the caribou strategy demonstrates the best
performance for all four wildlife and timber objectives
(accounts 1±4) (Table 6). Choice of scenario is ulti-
mately determined by priority placed on each manage-
ment objective.
4. Discussion
The development and application of GIS-based
habitat suitability mapping demonstrates simulation
modeling that allows scenario testing of multiple-use
management alternatives. Habitat suitability mapping
of wildlife species provides a representation of the
wildlife resource for comparison with other resource
activities such as forestry. In the North Columbia
Fig. 5. Trade-off between marten habitat and timber volume under
four timber harvest strategies.
Table 6
Multiple accounts performance of alternative timber harvest strategies
Strategy
Ranked performance of accountsa
1: Marten
habitat
2: Caribou
habitat
3: Timber
harvest
4: Timber
value
Accounts
1 and 2
Accounts
1±3
Accounts
1±4
Baseline
4
4
2
1
4 (8)
3 (10)
3 (11)
Old growth
2
1
3
3
1 (3)
1  (6)
2 (9)
Caribou
3
2
1
2
3 (5)
1  (6)
1 (8)
Park
1
3
4
4
2 (4)
2 (8)
3 (12)
a Figures in brackets denote sum of rankings for individual accounts.
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
171


Mountains example wildlife has been depicted by two
representative species, which are considered critical
and represent pressure at different levels in the eco-
system. Ideally, it would be useful to model the whole
ecosystem and to examine changes in that system
under various management scenarios. The use of
geographic information systems (GIS) has been cru-
cial in integrating key spatial information compo-
nents. Both
the habitat
suitability index (HSI)
models and the forest management models were
loosely coupled using spreadsheet modeling and
GIS. Thus, habitat and forest modeling were per-
formed externally to GIS and subsequently linked
to the geographic database using forest management
units as the spatial identi®er. This provides for ¯exible
and sophisticated modeling, somewhat at the expense
of usability.
The use of HSI models is subject to various limita-
tions as noted in the introduction. The marten HSI
model was validated using available harvest trapping
data. This is considered a reasonable and useful ®rst
test of the model. However, it is acknowledged that
this is not a particularly robust test and the model
should be subject to more rigorous validation. The use
of bootstrapping methods (Verbyla and Litvaitis,
1989; Bender et al., 1996) for evaluating the con®-
dence intervals for HSI would be a useful next step in
this work. This could be achieved by collecting tele-
metry and track count data. While not rigorously
tested the HSI models applied in this paper do ful®ll
the purpose of demonstrating simulation modelling for
resource planning.
Further improvements to the HSI modelling could
be achieved by inclusion of forest inventory measures
for volume of coarse woody debris, basal area of
snags, and herbaceous cover so that habitat variables
can be included in the spatial model directly without
the need for model variables. Cade (1997) recom-
mends the use of basal area rather than canopy cover to
estimate tree cover as a measure in habitat models.
However, canopy cover is the only available measure
of tree cover in existing forest inventory databases that
can be used for watershed or landscape level evalua-
tions of habitat for species such as marten with large
area requirements. Unfortunately, resource managers
often work within tight time constraints and restricted
budgets that limit their ability to gather new data for
managing habitat. Therefore, it is useful that an HSI
model be tied to currently available data such as forest
cover, biogeoclimatic, and biophysical mapping as has
been demonstrated in this paper.
The techniques used for timber harvest modelling
are also subject to further improvement. The heuristic
programming technique (Tabu search) used to model
the caribou strategy is considered well suited to this
type of constraint scheduling (Bettinger et al., 1997).
However, the technique has been shown to be less
successful in certain agricultural models for which
other methods, such as simulated annealing, are now
being tested (Mayer et al., 1998).
Habitat mapping, simulating change to habitat, and
scenario testing is dependent on the availability, qual-
ity and scale of topographic and forest inventory map
data. The example of the Tangier watershed in the
North
Columbia
Mountains
represents
a
single
watershed of 287 km2. The West Kootenay land use
region, which includes the North Columbia Moun-
tains, comprises 170 such watersheds or land units
(British Columbia Commission on Resources and the
Environment, 1994). A considerable GIS database and
computing power would be necessary so that resource
mapping and resource use scenario testing could be
performed for the whole region, thereby providing
stakeholders and resource managers with the tools to
make informed assessments and decisions. The
strength of the approach used here has been the scale
of modeling used, that is, at watershed level. Applying
a similar approach to an entire land-use region using
smaller scale databases would represent a substantial
departure from the detail that has been achieved and
that is considered necessary for sound decision-mak-
ing. A smaller scale would also lead to greater general-
izations
being
made
about
species
habitat
requirements and further subject the approach to the
limitations of HSI models (Laymon and Barrett,
1986). The scale of mapping and modeling adopted,
and the level of detail at which the spatial HSI can
operate are crucial to the application of this approach
in resource management.
The marten and caribou habitat mapping presented
here are intended to demonstrate the potential of
modeling the impacts of a range of resource-use
scenarios upon wildlife. By simulation modeling it
is possible to project changes in habitat conditions and
as a result provisions can be made to maintain or
improve conditions for selected wildlife species. The
172
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


use of a GIS-based scenario framework enables trade-
offs between wildlife and timber harvesting to be
assessed more effectively. This approach could use-
fully be applied to other resource-uses, for example,
furbearer harvesting or winter recreation use, allowing
sophisticated multiple resource scenarios to be simu-
lated and evaluated.
Acknowledgements
The authors appreciate the insightful comments on
the earlier drafts made by David Verbyla and Saphida
Wairimu, and two anonymous reviewers.
References
Allen, A.W., 1982. Habitat suitability index models: marten.
Publication FWS/OBS-82/10.11, USDI Fish and Wildlife
Service.
Aspinall, R., Veitch, N., 1993. Habitat mapping from satellite
imagery and wildlife survey data using a bayesian modeling
procedure in a GIS. Photogram. Eng. Remote Sens. 59, 537±
543.
Ball, G.L., 1994. Ecosystem modeling with GIS. Environ. Manage.
18, 345±349.
Bateman, M.C., 1986. Winter habitat use, food habits and home
range size of marten in Western Newfoundland. The Can. Field
Nat. 100, 58±62.
Bender, L.C., Roloff, G.J., Haufler, J.B., 1996. Evaluating
confidence intervals for habitat suitability models. Wildl. Soc.
Bull. 24, 347±352.
Bettinger, P., Sessions, J., Boston, K., 1997. Using Tabu search to
schedule timber harvests subject to spatial wildlife goals for big
game. Ecol. Modelling 94, 111±123.
Born, S.M., Sonzogni, W.C., 1995. Integrated environmental
management: strengthening the conceptualization. Environ.
Manage. 19, 167±181.
British Columbia Commission on Resources and the Environment,
1994. West Kootenay Ð Boundary land use plan, Commission
on Resources and the Environment, Victoria, British Columbia.
British Columbia Ministry of Environment and Parks, 1988.
Specifications and Guidelines 1 : 20 000 Digital Mapping,
British Columbia Ministry of Environment and Parks, Surveys
and Resource Mapping Branch, Victoria, British Columbia.
British Columbia Ministry of Forests, 1990. Standards and
Procedures for the Acquisition of Forest Inventory Data,
British Columbia Ministry of Forests, Resource Inventory
Section, Victoria, British Columbia.
British Columbia Ministry of Forests, 1993. Revelstoke TSA
timber supply analysis, British Columbia Ministry of Forests,
Integrated Resource Branch, Victoria, British Columbia.
Breininger, D.R., Provancha, M.J., Smith, R.B., 1991. Mapping
florida scrub jay habitat for purposes of land-use management.
Photogram. Eng. Remote Sens. 57, 1467±1474.
Brown, J.H., Lasiewski, 1972. Metabolism of weasels the cost of
being long and thin. Ecology 53, 939±943.
Brown, S., Schreier, H., Thompson, W., Vertinsky, I., 1994. Linking
mutiple accounts with GIS as decision support system to
resolve forestry/wildlife conflicts. J. Environ. Manage. 42,
349±364.
Buskirk, S.W., 1984. Seasonal use of resting sites by marten in
south-central Alaska. J. Wildl. Manage. 48, 950±953.
Buskirk, S.W., MacDonald, S.O., 1984. Seasonal food habits of
marten in south-central Alaska. Can. J. Zool. 62, 944±950.
Buskirk, S.W., Ruggiero, L.F., 1994. American marten. In: Buskirk,
S.W., Harestad, A.S., Raphael, M.G., Powell, R.A. (Eds.), The
Scientific Basis for Conserving Forest Carnivores; American
Marten, Fisher, Lynx and Wolverine in the Western United
States, General Technical Report RM-254, USDA Forest
Service, Rocky Mountain Forest and Experiment Station, Fort
Collins, CO, pp. 7±37.
Buskirk, S.W., Forrest, S.C., Raphael, M.G., Harlow, H.J., 1989.
Winter resting site ecology of marten in the central Rocky
Mountains. J. Wildl. Manage. 53, 191±196.
Buskirk, S.W., Harestad, A.S., Raphael, M.G., Powell, R.A. (Eds.),
1994. Martens, sables, and fishers: biology and conservation.
Cornell University Press, Ithaca and London, 486 pp.
Cade, B.S., 1997. Comparison of tree basal area and canopy cover
in habitat models: subalpine forest. J. Wildl. Manage. 61, 326±
335.
Chang, K., Verbyla, D.L., Yeo, J.J., 1995. Spatial analysis of
habitat selection by Sitka black-tailed deer in Southeast Alaska
USA. Environ. Manage. 19, 579±589.
Clark, J.D., Dunn, J.E., Smith, K.G., 1993. A multivariate model of
female black bear habitat use for a geographic information
system. J. Wildl. Manage. 57, 519±526.
Coker, D.R., Capen, D.E., 1995. Landscape-level habitat use by
brown-headed cowbirds in Vermont. J. Wildl. Manage. 59,
631±637.
Corn, J.G., Raphael, M.G., 1992. Habitat characteristics of marten
at subnivean access sites. J. Wildl. Manage. 56, 442±448.
Donovan, M.L., Rabe, D.L., Olson, C.E., 1987. Use of geographic
information systems to develop habitat suitability models.
Wildl. Soc. Bull. 15, 574±579.
Duncan, B.W., Breininger, D.R., Schmaizer, P.A., Larson, V.L.,
1995. Validating a Florida scrub jay habitat suitability model,
using demography data on Kennedy Space Center. Photogram.
Eng. Remote Sens. 61, 1361±1370.
Franklin, J., 1994. Developing information essential to policy,
planning, and management decisions: the promise of GIS. In:
Sample, V.A. (Ed.), Remote Sensing and Gis in Ecosystem
Management, Island Press, Washington, DC, pp. 18±24.
Glover, F., Laguna, M., 1995. Tabu search, In: Reeves, C.R. (Ed.),
Modern Heuristic Techniques for Combinatorial Problems,
McGraw-Hill, London, pp. 70±150.
Gunton, T., 1998. Forestry land use policy in British Columbia: the
dynamics of change. Environments 25, 8±13.
Hargis, C.D., McCullough, D.R., 1984. Winter diet and habitat
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
173


selection of marten in Yosemite National Park. J. Wildl.
Manage. 48, 140±146.
Herr, A.M., Queen, L.P., 1993. Crane habitat evaluation using GIS
and remote sensing. Photogram. Eng. Remote Sens. 59, 1531±
1538.
Hodgson, M.E., Jensen, J.R., Mackey, H.E., Coulter, M.C., 1988.
Monitoring wood stork foraging habitat using remote sensing
and geographic information systems. Photogram. Eng. Remote
Sens. 54, 1601±1607.
Homer, C.G., Edwards, T.C., Ramsey, R.D., Price, K.P., 1993. Use
of remote sensing methods in modelling sage grouse winter
habitat. J. Wildl. Manage. 57, 78±84.
Hurni, H., 1997. Concepts of sustainable land management. ITC J.
1997, 210±215
Lancia, R.A., Douglas, S.D., Adams, D.A., Hazel, D.W., 1982.
Validating habitat quality assessment: an example. Trans. Nth.
Amer. Wildl. Nat. Res. Conf. 47, 96±110.
Laperriere, A.J., Dent, P.C., Gassaway, W.C., Nodler, F.A., 1980.
Use of LANDSAT data for moose habitat analyses in Alaska. J.
Wildl. Manage. 44, 881±887.
Laymon, S.A., Barrett, R.H., 1986. Developing and testing habitat-
capability models: pitfalls and recommendations. In: Verner, J.,
Morrison, M.L., Ralph, C.J. (Eds.), Wildlife 2000: Modeling
Habitat Relationships of Terrestrial Vertebrates, University of
Wisconsin Press, Madison, WI, pp. 87±91.
Lindenmayer, D.B., Franklin, J.F., 1997. Managing stand structure
as part of ecologically sustainable forest management in
Australian mountain ash forests. Conserv. Biol. 11, 1053±1068.
Lindenmayer, D.B., Nix, H.A., McMahon, J.P., Hutchinson, M.F.,
Tanton, M.T., 1991. The conservation of Leadbeater's possum,
Gymnbelideus leadbeateri McCoy: a case study of the use of
bioclimatic modelling. J. Biogeog. 18, 371±383.
Lindenmayer, D.B., Ritman, K., Cunningham, R.B., Smith, J.D.B.,
Horvath, D., 1995. A method for predicting the spatial
distribution of arboreal marsupials. Wildl. Res. 22, 445±456.
Lofroth, E.C., Bianci, V., 1991. Marten habitat suitability research
project Ð working plan, Wildlife Working Report No. WR-50,
British Columbia Ministry of Environment, Wildlife Branch,
Victoria, British Columbia, 27 pp.
Lyon, J.G., 1983. Landsat-derived land-cover classifications for
locating potential kestrel nesting habitat. Photogram. Eng.
Remote Sens. 49, 245±250.
Mayer, D.G., Belward, J.A., Burrage, K., 1998. Tabu search not an
optimal choice for models of agricultural systems. Agric. Syst.
58, 243±251.
Nelson, J., 1993. Spatial Analysis of harvesting guidelines in the
Revelstoke timber supply area. In: Le Forestier, G. (Ed.), Eyes
on the Future Ð Proceedings of GIS'93 Symposium, Forestry
Canada and BC Forests, Vancouver, British Columbia, pp. 203±
208.
Ormsby, J.P., Lunetta, R.S., 1987. Whitetail deer food availability
maps from thematic mapper data. Photogram. Eng. Remote
Sens. 53, 1081±1085.
Pearce, J., Lindenmayer, D., 1998. Bioclimatic analysis to enhance
reintroduction biology of the endangered helmeted honeyeater
Lichenostomus melanops cassidix in southeastern Australia.
Restor. Ecol. 6, 238±243.
Pereira, J.M., Itami, R.M., 1991. GIS-based habitat modeling: a
study of the Mt. Graham red squirrel. Photogram. Eng. Remote
Sens. 57, 1475±1486.
Price, L., Blake, J., 1993. GIS-based multi-resource analysis in
Revelstoke timber supply area. In: Le Forestier, G. (Ed.), Eyes on
theFuture ÐProceedingsofGIS'93Symposium,ForestryCanada
and BC Forests, Vancouver, British Columbia, pp. 227±239.
Raine, R.M., 1983. Winter habitat use and responses to snow cover
of fisher and marten in southeastern Manitoba. Can. J. Zool. 61,
25±34.
Reading, R.P., Clark, T.W., Seebeck, J.H., Pearce, J., 1996. Habitat
suitability index model for the Eastern Barred Bandicoot,
Perameles gunni. Wildl. Res. 23, 221±235.
Rickers, J.R., Queen, L.P., Arthaud, G.J., 1995. A proximity-based
approach to assessing habitat. Landsc. Ecol. 10, 309±321.
Ritcey, R., Low, D., Harestad, A., Campbell, R., Harcombe, A.P.,
1988. Wildlife habitat handbooks for the Southern Interior
Ecoprovince, Species-Habitat relationship models for mammals
vol. 5, Wildlife Habitat Research WHR-32, Wildlife Report No.
R-19. British Columbia Ministry of Environment, Wildlife
Branch, Victoria, British Columbia, 245 pp.
Robel, R.J., Fox, L.B., Kemp, K.E., 1993. Relationship between
habitat suitability index values and ground counts of beaver
colonies in Kansas. Wildl. Soc. Bull. 21, 415±421.
Rochelle, J.A., 1994. Maintenance of late-successional ecosystem
values in the Pacific Northwest. In: Sample, V.A. (Ed.), Remote
Sensing and Gis in Ecosystem Management. Island Press,
Washington, DC, pp. 43±47.
Rominger, E.M., Oldemeyer, J.L., 1989. Early-winter habitat of
woodland caribou Selkirk Mountains British Columbia. J.
Wildl. Manage. 53, 238±243.
Rudis, V.A., Tansy, J.B., 1995. Regional assessment of remote
forests and black bear habitat from forest resource surveys. J.
Wildl. Manage. 59, 170±180.
Ruggiero, L.F., Aubry, K.B., Buskirk, S.W., Lyon, L.J., Zielinski,
W.J. (Eds.), 1994. The scientific basis for conserving forest
carnivores: American marten, fisher, lynx and wolverine in the
western United States. General Technical Report RM-254,
USDA Forest Service, Rocky Mountain Forest and Range
Experiment Station, Fort Collins, CO, 184 pp.
Schamberger, M.L., O'Neil, L.J., 1986. Concepts and constraints of
habitat-model testing. In Verner, J., Morrison, M.L., Ralph, C.J.
(Eds.), Wildlife 2000: Modeling Habitat Relationships of
Terrestrial Vertebrates. University of Wisconsin Press, Madi-
son, WI, pp. 5±10.
Seip, D.R., 1998. Ecosystem management and the conservation
of caribou habitat in British Columbia. Rangifer 10, 203±211.
Servheen, G., Lyon, L.J., 1989. Habitat use by woodland caribou in
the Selkirk Mountains. J. Wildl. Manage. 53, 230±237.
Simpson, K., Kelsall, J.P., Leung, M., 1996. Integrated manage-
ment of mountain caribou and forestry in Southern British
Columbia. Rangifer 9, 153±158.
Skidmore, A.K., Gauld, A., Walker, P., 1996. Classification of
kangaroo habitat distribution using three GIS models. Int. J.
Geog. Info. Syst. 10, 441±454.
Slocombe, D.S., 1993. Implementing ecosystem-based manage-
ment. BioScience 43, 612±622.
174
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175


Steventon, J.D., Major, J.T., 1982. Marten use of habitat in a
commercially clear-cut forest. J. Wildl. Manage. 46, 175±182.
Summerfield, B., Escano, R., Donnelly, B., 1985. Woodland
caribou cumulative effects analysis model. Research Paper,
USDA Forest Service, Intermountain Forest and Range
Experiment Station, Ogden, UT.
Terry, E., McLellan, B., Watts, G., Flaa, J., 1996. Early winter
habitat use by mountain caribou in the north Caribou and
Columbia mountains British Columbia. Rangifer 9, 133±140.
Thompson, W.A., Brown, S., Schreier, H., Kliskey, A.D., van
Kooten, G.C., Vertinsky, I., 1994. Accounting for forestry/
wildlife conflicts in a multiple accounts framework, In:
Proceedings of Decision Support Ð 2001, Resource Technol-
ogy 94 Symposium and the 17th Annual Ontario Geographic
Information Seminar. 12±16 September 1994, Toronto, Ontario,
pp. 518±529.
Thompson, W., Halme, M., Brown, S., Vertinsky, I., Schreier, H.,
1995. Timber harvest scheduling subject to wildlife and
adjacency constraints, In: Management systems for a global
economy with global resource concerns Ð Proceedings of the
1994 symposium on systems analysis in forest resources,
Society of American Foresters, Washington, DC, pp. 261±269.
United States Fish and Wildlife Service, 1981. Standards for the
development of habitat suitability index models, Ecological
Service Manual 103, Div. of Ecol. Serv., Washington, DC.
Van Horne, B., 1983. Density as a misleading indicator of habitat
quality. J. Wildl. Manage. 47, 893±901.
Verbyla, D.L., Litvaitis, J.A., 1989. Resampling methods for
evaluating classification accuracy of wildlife habitat models.
Environ. Manage. 13, 783±787.
Wynne, K.M., Sherburne, J.A., 1984. Summer home range use by
adult marten in northwestern Maine. Can. J. Zool. 62, 941±943.
Andrew [Andy] D. Kliskey is an assistant professor in the
Department of Geography at the University of Canterbury, New
Zealand. He is an applied geographer who teaches environmental
applications of GIS. His research interests are in the development
and application of GIS methodologies for solving environmental
management problems, particularly in wildlife management and
wilderness management.
Andy spent 4 years as a postdoctoral fellow at the University of
British Columbia's Resource Management and Environmental
Studies Centre, and at the Arctic Institute of North America's
Kluana Lake Base in the Yukon Territory. He trained as a surveyor,
planner, and geographer at the University of Otago, New Zealand
(B. Surv., M. RRP, Ph.D) where he undertook an innovative inter-
disciplinary Ph.D that developed a GIS-based approach to mapping
wilderness perceptions.
Eric Lofroth is a wildlife biologist with the Wildlife Branch in
British Columbia. His primary interest is in furbearer biology.
He completed a B.Sc at the University of Victoria, Canada and a
M.Sc. at Simon Fraser University, Canada.
Hanspeter [Hans] Schreier is a professor in the Institute for
Resources and Environment at the University of British Columbia.
His teaching and research focuses on land use-water resource
issues including watershed management, soil and water pollution,
non-point source pollution and the application of GIS in land
evaluation, watershed management and environmental assessment.
William [Bill] A. Thompson is an adjunct professor in the Forest
Economics and Policy Analysis Unit at the University of British
Columbia. His research interests are in forest yield modelling and
ecology.
A.D. Kliskey et al. / Landscape and Urban Planning 45 (1999) 163±175
175
