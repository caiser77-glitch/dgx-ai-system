--- 
source: landscape genetics and least-cost path analysis reveral unexpected dispersal routes in the .pdf
--- 

Molecular Ecology (2009) 18, 1365–1374
doi: 10.1111/j.1365-294X.2009.04122.x
© 2009 Blackwell Publishing Ltd
Blackwell Publishing Ltd
Landscape genetics and least-cost path analysis reveal 
unexpected dispersal routes in the California tiger 
salamander (Ambystoma californiense)
IAN J. WANG, WESLEY K. SAVAGE† and H. BRADLEY SHAFFER
Department of Evolution and Ecology and Center for Population Biology, 1 Shields Avenue, University of California, Davis, 
CA 95616, USA
Abstract
A major goal of landscape genetics is to understand how landscapes structure genetic vari-
ation in natural populations. However, landscape genetics still lacks a framework for quan-
tifying the effects of landscape features, such as habitat type, on realized gene flow. Here,
we present a methodology for identifying the costs of dispersal through different habitats for
the California tiger salamander (Ambystoma californiense), an endangered species restricted
to grassland/vernal pool habitat mosaics. We sampled larvae from all 16 breeding ponds in
a geographically restricted area of vernal pool habitat at the Fort Ord Natural Reserve,
Monterey County, California. We estimated between-pond gene flow using 13 polymorphic
microsatellite loci and constructed GIS data layers of habitat types in our study area. We then
used least-cost path analysis to determine the relative costs of movement through each habitat
that best match rates of gene flow measured by our genetic data. We identified four measur-
able rates of gene flow between pairs of ponds, with between 10.5% and 19.9% of larvae having
immigrant ancestry. Although A. californiense is typically associated with breeding ponds
in grassland habitat, we found that dispersal through grassland is nearly twice as costly as
dispersal through chaparral and that oak woodland is by far the most costly habitat to traverse.
With the increasing availability of molecular resources and GIS data, we anticipate that these
methods could be applied to a broad range of study systems, particularly those with cryptic
life histories that make direct observation of movement challenging.
Keywords: gene flow, GIS, landscape genetics, least-cost path analysis, microsatellite, population
structure
Received 6 June 2008; revision received 13 January 2009; accepted 22 January 2009
Introduction
The accurate assessment of how genes flow in real popula-
tions across real landscapes is a key element of ecological
and conservation genetics. Gene flow significantly affects
population genetic differentiation in the majority of animal
species in nature (Bohonak 1999) and plays an important
role in evolution both as a constraint (by preventing local
adaptation) and by promoting the spread of beneficial alleles
(Slatkin 1987). Gene flow is inherently tied to dispersal and
represents a key link between ecological traits, local environ-
ment, and micro-evolution.
Examining the role that landscapes play in dispersal and
gene flow can reveal much about the effect of environmental
variation on the distribution of genetic variation in natural
populations (Arnaud 2003; Manel et al. 2003; Geffen et al.
2004; Funk et al. 2005; Spear et al. 2005; Stevens et al. 2006;
Storfer et al. 2007). The developing field of landscape genetics
has provided a framework for this activity. Although sub-
stantial progress has been made, efforts have largely focused
on analyses dealing with linear distance correlations (Storfer
1999; Manel et al. 2003; Spear et al. 2005) and spatial auto-
correlation (Smouse & Peakall 1999; Barbujani 2000; Tren-
ham et al. 2001; Manel et al. 2003; Storfer et al. 2007). While this
isolation-by-distance approach has been useful, it ignores
landscape heterogeneity that may play an important role in
Correspondence: Ian J. Wang, Fax: 1 (530)752-1449; 
E-mail: ijwang@ucdavis.edu
†Present address: Department of Biological Sciences, Lehigh
University, Bethlehem, PA 18015, USA.


1366 I. J. WANG, W. K. SAVAGE and H. B. SHAFFER
© 2009 Blackwell Publishing Ltd
the way that habitats are actually traversed in nature. Land-
scape features and habitat connectivity are known to influ-
ence dispersal patterns and genetic structure among natural
populations (Michels et al. 2001; Spear et al. 2005; Giordano
et al. 2007). Especially for animals that interact continuously
with their environments, such as small vertebrates, the distri-
bution of landscape features can substantially influence how
these animals move across a landscape (Schippers et al.
1996; Cushman et al. 2006). Thus, accounting for landscape
heterogeneity and the precise distribution of features on a
landscape can contribute critical insights into our understand-
ing of gene flow and population structure (Spear et al. 2005;
Cushman et al. 2006; Giordano et al. 2007; Storfer et al. 2007).
Unfortunately, for many species, direct observation of indi-
viduals moving among patches of suitable breeding habitat
may be virtually impossible, especially for those that are
small, nocturnal, seasonally limited, subterranean, or other-
wise difficult to mark, track, and observe. An alternative
approach for these taxa lies in the integration of GIS-based
tools with population genetic analyses (Spear et al. 2005;
Cushman et al. 2006; Storfer et al. 2007). Although GIS data
are the most sophisticated and informative landscape data
available, few studies in landscape genetics have fully inte-
grated GIS technology (Spear et al. 2005; Storfer et al. 2007).
GIS cost-weighted analyses, such as least-cost path analysis
(LCPA), which account for variation in the ease of movement
across regions of a heterogeneous landscape, are particularly
promising as a way of evaluating the most likely paths by
which genes flow across landscapes (Storfer et al. 2007). In
LCPA, ‘costs’ are assigned to different landscape features,
such as habitat type or elevation. These ‘costs’ generally
reflect some understanding of resistance or mobility through
a landscape feature for a species, but other factors associated
with movement (for example thermal stress, predation risk,
or energy expenditure) can also contribute to the ‘cost’ of
traversing a landscape. The landscape is then searched for
the path between two points that minimizes the total cumu-
lative cost of moving between those points (Storfer et al. 2007).
Several studies have shown that some form of least-cost
path distance fits patterns of genetic structure more closely
than geographic distance (Michels et al. 2001; Coulon et al.
2004; Stevens et al. 2006), demonstrating the value of the cost-
weighted approach. However, in these and other studies,
costs were predetermined based upon observational records
and a priori expectations, and the ways in which landscape
quality is perceived by a particular species may not corre-
spond to our assumptions (With et al. 1997; Wiens 2001;
Cushman et al. 2006). So what can we do if we have no
expectation, or want to explicitly test our expectations, for
the costs of movement through different habitats? Spear et al.
(2005) take a major step by utilizing least-cost path analysis,
but discuss the difficulty of developing cost parameters for
habitat types when no data are available for determining
cost assignments.
In this study, we explore a strategy that utilizes a genetic
assignment method of estimating gene flow between popu-
lations, GIS landscape data to construct least-cost paths of
dispersal between those sites, and a model fitting process to
infer the costs of traversing each habitat type. Using this
approach, we can make qualitative comparisons of cost
schemes (as in Michels et al. 2001; Coulon et al. 2004; Stevens
et al. 2006, and Cushman et al. 2006) but we can also use gen-
otype data and the distribution of habitat types on a land-
scape to quantitatively inform us of the costs of movement
through these habitats. We present our analysis of gene flow
between breeding ponds and the relative costs of movement
through different habitat types in the federally endangered
California tiger salamander, Ambystoma californiense. Amphi-
bians are especially suitable for studies of landscape genetics
because they often form metapopulations around breeding
ponds, have easily distinguishable cohorts, and have fairly
low vagility (Beebee & Rowe 2000; Newman & Squire 2001;
Jehle & Arntzen 2002; Funk et al. 2005; Smith & Green 2005;
Spear et al. 2005; Stevens et al. 2006; Zamudio & Wieczorek
2007). In many cases, little knowledge exists about upland
habitat use in amphibians, and the behaviour of many species
(Spear et al. 2005), including the California tiger salamander
(Trenham & Shaffer 2005; Searcy & Shaffer 2008), makes direct
observation of habitat use extremely challenging.
Several studies have demonstrated the importance of
retaining connectivity among amphibian breeding pond
networks (Newman & Squire 2001; Jehle & Arntzen 2002;
Andersen et al. 2004; Trenham & Shaffer 2005; Stevens et al.
2006), and others have identified the need to understand
the effects of habitat fragmentation and the distribution of
habitat patches on gene flow to understand the requirements
for population persistence (Gibbs 1998; Guerry & Hunter
2002; Funk et al. 2005; Spear et al. 2005; Rittenhouse &
Semlitsch 2006). Because amphibians are often sensitive to
anthropogenic habitat alteration (Guerry & Hunter 2002)
and are facing local and global declines (Fisher & Shaffer 1996;
Collins & Storfer 2003), studies providing information
on the importance of different habitat types to sustaining
amphibian communities also play a critical role in conserva-
tion strategies (Zamudio & Wieczorek 2007).
We use our methodology to determine the importance of
different habitats in retaining population connectivity. Our
goals were to estimate gene flow between populations based
on microsatellite genotypic data, to use these estimates to
measure the costs of dispersal through three habitat types
(grassland, chaparral, and oak woodland), and to identify
the likely dispersal corridors on the landscape using least-
cost path analysis. Finally, we examined whether the inferred
habitat costs matched expectations based upon natural-
history observations. Our results quantify the ecological impor-
tance of habitat heterogeneity to a species for which little is
known about the costs of movement through these three
fundamental habitat types and suggest that our approach


LANDSCAPE GENETIC INFERENCE OF DISPERSAL COSTS 1367
© 2009 Blackwell Publishing Ltd
can shed light on habitat-associated dispersal in other taxa
for which direct observation is difficult.
Materials and methods
Study system
The California tiger salamander, Ambystoma californiense, is
a federally listed, pond-breeding amphibian endemic to
central California (Loredo et al. 1996; Shaffer & Trenham 2005).
Ambystoma californiense breed in seasonal and permanent ponds
that are free of fish and other introduced predators (Shaffer
& Trenham 2005). Aquatic larvae grow in these pools for 3–
6 months, at which time they metamorphose and disperse
onto the surrounding terrestrial landscape. Adult and juvenile
salamanders routinely travel at least 1 km from breeding
ponds (Trenham et al. 2001; Trenham & Shaffer 2005; Searcy
& Shaffer 2008); except for a few weeks of breeding activity,
they are primarily fossorial. They reside in small mammal
(primarily California ground squirrel, Spermophilus beecheyi
and Botta’s pocket gopher, Thomomys bottae) burrows for
most of their lives, which provide protection against preda-
tion and dessication (Loredo et al. 1996; Shaffer & Trenham
2005; Trenham & Shaffer 2005; Searcy & Shaffer 2008).
Although A. californiense may live for up to 11 years, they
generally breed only once or twice during their lifetimes
(Trenham et al. 2000). The single long-term mark–recapture
study available indicates that interpond dispersal occurred
regularly, on a relatively xeric landscape in central California
(Hastings Reservation); approximately 30% of first-time
breeders migrated to a different breeding pond from where
they were born, and about 30% of second-year breeders
moved to a new breeding pond (Trenham et al. 2001).
We conducted our research at the Fort Ord Natural Reserve,
in Monterey County, California. Fort Ord is a protected area
managed by the University of California that contains an
intact set of natural vernal pools, many of which are used as
breeding sites by A. californiense. There are three distinct veg-
etation types surrounding the vernal ponds on this reserve:
grassland, maritime chaparral, and oak woodland. The
grasses in the reserve are a mixture of California natives
and invasives, including ryegrasses (Leymus spp.), needle-
grasses (Nassella spp.) and hair-grasses (Deschampsia spp.).
The Monterey Bay maritime chaparral is a distinctive com-
munity dominated by manzanitas (Arctostaphylos spp.) and
California lilac (Ceanothus spp.). The oak woodland contains
stands of coast live oaks (Quercus agrifolia) with toyon (Heter-
omeles arbutifolia) and western poison oak (Toxicodendron diver-
silobum) in the understory (Hickman 1993). A dozen breeding
ponds in the northern part of the reserve are separated from
four southern ponds by a low range of hills. However, within
each of these two regions, the total vertical displacement
does not exceed 25 m (National Elevation Dataset, http://
ned.usgs.gov/). The northern Fort Ord breeding ponds
comprise a relatively isolated set of vernal pools that form a
closed network covering approximately 10 km2, with no addi-
tional known breeding sites to the north, west or east; the four
breeding ponds to the south are largely introgressed with
non-native invasive Ambystoma tigrinum genes (Fitzpatrick
& Shaffer 2007) and are isolated by both distance (~4 km)
and elevation from the northern pools at our study site.
Population sampling and pond characterization
California tiger salamander populations were sampled from
all 16 vernal pools at the Fort Ord Natural Reserve during
June 2004 (Fig. 1; Table 1). Tissues were collected as tail-clips
from larval salamanders and were preserved in 95% ethanol.
Because California tiger salamanders are primarily ter-
restrial as adults and breed more or less synchronously in
Table 1 Geographical coordinates of breeding
ponds in the Fort Ord Natural Reserve,
Monterey County, CA. Acronyms correspond
to those used in the figures; N represents
the number of samples included in micro-
satellite genotyping for each population
Population
Acronym
Latitude
Longitude
N
Ostracod Pond
OC
36.6386
–121.7529
46
Henniken West Pond
HW
36.6449
–121.7594
23
Henniken East Pond
HE
36.6460
–121.7564
46
Lower Machine Gun Flats
LM
36.6379
–121.7432
46
Upper Machine Gun Flats
UM
36.6355
–121.7461
45
Leslie Pond
LE
36.6427
–121.7508
45
West Twin Pond
WT
36.6466
–121.7478
44
East Twin Pond
ET
36.6460
–121.7454
46
Far East Pond
FE
36.6457
–121.7389
47
Chaparral Pond
CH
36.6340
–121.7662
23
Mudhen Lake
MH
36.6288
–121.7317
10
10α Vernal Pool
TA
36.6263
–121.7656
23
Impossible Rd × Mercury Rd
IM
36.5957
–121.7599
10
Riso Rd × Eucalyptus Rd
RE
36.5960
–121.7794
25
Barloy Canyon
BC
36.6057
–121.7467
24
Laguna Seca
LS
36.5923
–121.7664
11


1368 I. J. WANG, W. K. SAVAGE and H. B. SHAFFER
© 2009 Blackwell Publishing Ltd
vernal pools from November to May (Shaffer & Trenham
2005), our samples constitute a single breeding cohort at
each pond.
To ensure that ponds were of similar quality, we counted
small mammal burrows along 100-m transects extending
from the pond edges in each of the four cardinal directions.
Density of small mammal burrows is the only metric of pond
quality that has correlated with A. californiense abundance in
previous studies (Trenham 2001; Trenham & Shaffer 2005).
We performed chi-squared tests on each pair of ponds,
comparing the number of burrows observed by each to the
number expected if burrows were distributed evenly
between the two ponds.
Genotyping
Tissues were digested in lysis buffer with Proteinase K, and
genomic DNA was purified using a standard ethanol pre-
cipitation. Extracted samples were diluted to 10 ng/μL and
used as template in polymerase chain reactions (PCRs) for 13
tetranucleotide microsatellite loci (AcalB136, AcalB142,
AcalB148, AcalD019, AcalD021, AcalD032, AcalD036, AcalD065,
AcalD071, AcalD073, AcalD082, AcalD098, AcalD108, Savage,
2008). Forward primers for each PCR were labelled with
a 5’ fluorescent tag (6-FAM, NED, or HEX) for visualiza-
tion. We amplified loci individually and ran PCR products, in
sets of three loci, on an ABI 3100 Capillary Electrophoresis
Genetic Analyzer (Applied Biosystems) at the UC Davis
College of Biological Sciences DNA Sequencing Facility
(http://dnaseq.ucdavis.edu/). Fragments were sized with
ROX-500 size standard and collected with GeneScan version
3.1, and scoring and binning was performed with Genotyper
version 2.5 (Applied Biosystems). We used Micro-Checker
version 2.2.3 (van Oosterhout et al. 2004) to check for potential
scoring errors and the presence of null alleles.
Population detection
We investigated the number of genetic clusters in our
sampled landscape using baps version 4.14 (Corander et al.
2003). baps is distinct from other population identification
software in that it treats populations, instead of individuals,
as units. Thus, baps determines which populations have
different allele frequencies, rather than partitioning indi-
viduals based upon Hardy-Weinberg equilibrium. Addition-
ally, baps can accommodate geographic data associated
with sampling as prior information (Pearse & Crandall 2004;
Corander et al. 2008). We performed the ‘admixture based
on pre-defined populations’ analysis in baps, using the popu-
lation of sample origin as prior information. Although the
name suggests that population assignments are static, baps
can merge two predefined populations into one if it fails to
Fig. 1 Satellite image of the Fort Ord UC
Natural Reserve, Monterey County, Cali-
fornia, with localities for 16 California tiger
salamander breeding ponds sampled for
this study. Population acronyms correspond
to those used in Table 1.


LANDSCAPE GENETIC INFERENCE OF DISPERSAL COSTS 1369
© 2009 Blackwell Publishing Ltd
detect significant allele frequency differences. We used 1000
iterations to estimate the admixture coefficient for each
sample and 10 iterations to estimate the admixture coefficient
for 20 reference individuals. We then used the genetic clusters
identified in baps in an analysis of molecular variance
(amova) implemented in GenAlEx version 6.3 (Peakall &
Smouse 2006) to quantify the fraction of the total genetic
variance among the genetic populations.
Gene flow estimation
We used a genetic assignment method, implemented in
BayesAss+ version 1.3 (Wilson & Rannala 2003), to identify
larvae with immigrant ancestry among our breeding popu-
lations. Unlike coalescent-based estimates of gene flow,
genetic assignment methods are suitable for estimating
recent rates of gene flow (Berry et al. 2004; Pearse &
Crandall 2004). BayesAss+ uses Markov chain Monte
Carlo resampling to estimate asymmetrical rates of gene
flow between populations and also calculates a confidence
interval for results that would be returned from unin-
formative data (Wilson & Rannala 2003; Pearse & Crandall
2004). Genetic assignment methods are a common tool in
landscape genetics and have been shown to deliver accurate
results when sampling sufficient individuals across a
range of unlinked loci (Paetkau et al. 2004), even when
interpopulation dispersal is common (Berry et al. 2004).
We averaged the results from three independent runs with
6 million generations each, discarding 2 million as burn-in,
sampling the chain every 2000 generations, and using
default parameter settings. Because we sampled larvae,
which do not disperse, the results of these analyses repre-
sent estimates of true gene flow, or dispersal followed by
successful breeding; in this study, we use the term dispersal
to describe individual interpopulation movements which
result in gene flow.
Least-cost path analysis
We performed a GIS least-cost path analysis to identify
dispersal corridors and determine the cost of movement
through different habitat types (grassland, chaparral, oak
woodland). To infer the appropriate costs for each habitat
type, we calculated least-cost distances over a range of values
and compared them to those predicted by our genetic
analyses. There were essentially three steps to our analysis:
(i) assign hypothetical costs to each habitat type, (ii) calculate
the least- cost distances between ponds using those costs, and
(iii) compare these least-cost distances to those predicted
by gene flow estimates. We performed the matching analysis
[step (iii)] under the logical assumption that the rate of gene
flow between two populations is inversely proportional to
the cost of moving between them (i.e. when the cost is high,
gene flow should be low).
First, we constructed a detailed habitat map based upon
satellite imagery and field surveys. This raster covered the
area surrounding the northern 12 ponds, including all of
those for which measurable rates of gene flow were detected.
We excluded the southern four ponds because we did not
want to sacrifice map resolution and because no gene flow
was detected among them or with northern ponds. The final
habitat raster was constructed by scoring each cell with a
value corresponding to either vernal pool or one of the three
habitat types: grassland, chaparral, or oak woodland. The
raster contained square cells with 1-m dimensions, which
should adequately capture fine-scale patterns of habitat
distribution. We excluded elevation as a layer in our GIS
analysis because the resolution (30-m horizontal resolution
and 10-m vertical resolution) and error (7–15 m in elevation)
in the available data are high relative to the overall range
in elevation (National Elevation Dataset, available: http://
ned.usgs.gov).
Using the Spatial Analyst extension in ArcGIS version
9.2 (ESRI), we performed a least-cost path analysis. In the
LCPA, a ‘cost raster’ was first created by assigning values
to each of the three habitat types. A ‘cost distance raster’
was then created by giving a value to each cell equal to the
cumulative cost of reaching it from the source. From this
cost distance raster, ArcGIS then identifies the path resulting
in the lowest cost to reach a target pond from the source.
We recorded this path and the total cost of moving along it,
which is known as the least-cost path distance.
We conducted LCPAs on a wide range of cost combina-
tions. Because costs are relative, one habitat type was always
set to 1 and the other two were assigned every combina-
tion, in 0.1 unit increments, from 1 to 10 (low to high). This
resulted in a total of 24 843 least-cost path analyses run on
different combinations of costs. Our goal was to find com-
binations of cost values that would result in least-cost path
distances predicted by the gene flow estimates. Essentially,
we assumed that the rates of gene flow inferred from our
genetic data reflected the cost of movement between different
breeding ponds such that higher rates of gene flow indicated
relatively less costly dispersal. For instance, if a pair of ponds
(A1–A2) had twice the interpond gene flow of another pair
(B1–B2), then we would expect the least-cost distance between
pond-pair A1–A2 to be half that between pond-pair B1–B2.
We found the relative rates of gene flow between pairs of
ponds from the estimates in our molecular analysis. Because
BayesAss+ (Wilson & Rannala 2003) provides a 95% con-
fidence interval in addition to the mean of gene flow between
ponds, we were able to establish the 95% confidence interval
of relative rates predicted from our molecular data.
For each of the 24 843 LCPAs, we took the least-cost path
distances and compared them to the distances expected by
the rates of gene flow resulting from our molecular analysis.
If all of the least-cost distances fell within their expected
ranges, based on the 95% confidence interval, then we


1370 I. J. WANG, W. K. SAVAGE and H. B. SHAFFER
© 2009 Blackwell Publishing Ltd
accepted the habitat cost values used to generate those paths
as reflecting biologically accurate costs of dispersal. This
resulted in a range of values for which the habitat costs
matched expectations.
As a hypothetical example, consider the scenario in which
the confidence intervals for the rates of gene flow detected
between two pairs of ponds are 0.10 to 0.15 (A1–A2) and
0.20 to 0.30 (B1–B2). We would expect the cost of dispersing
in A1–A2 to be greater than in B1–B2, because the rate of gene
flow is lower. Thus, the least-cost distance between A1–A2
could be as high as 3times (0.30/0.10 = 3.00) or as low as
1.33 times (0.20/0.15 = 1.33) the least-cost distance between
B1–B2. If there are two habitat types on this landscape (X
and Y), we can assign hypothetical costs to these habitats
until we find a range of values that fit our expectations for
least-cost distances. If we set X =1 and Y = 2, the least-cost
distance between A1–A2 might equal 16 and between B1–B2
might equal 8. This would result in a relative least-cost
distance of 2 (16/8= 2), which falls within our confidence
interval for expected relative distances of 1.33 to 3. Thus,
we would accept X = 1 and Y = 2 as realistic values for hab-
itats X and Y. If, on the other hand, values of X = 2 and
Y = 1 resulted in least-cost distances of 5 for A1–A2 and 6 for
B1–B2, then we would reject these values because they
result in a relative distance (5/6 = 0.83) outside of the con-
fidence interval.
To visually and geographically identify dispersal corridors
between breeding ponds, we then plotted the least-cost paths
on our habitat map. This enabled us to identify the partic-
ular routes used in interpond dispersal. Our approach is
summarized by a flow chart showing the intersection of
molecular genetic and GIS techniques in Fig. 2.
Results
Genotypic data
All 13 of our microsatellite loci were highly polymorphic,
ranging from 7 to 19 alleles, with an average of 11.6 alleles,
at each locus (Table 2). Micro-Checker did not indicate the
presence of null alleles or scoring error. We were unable to
unambiguously score 2.1% of the genotypes and coded these
as missing data.
Population detection
baps results recognize a large number of individuals with
admixed ancestry, but support the presence of 15 separate
populations (Fig. 3). baps recognized 15 of 16 sampling
Fig. 2 Flow chart showing the steps in our methodology for esti-
mating the costs of dispersal across different landscape features.
The technique integrates molecular genetic analyses and GIS least-
cost path analyses.
Fig. 3 Population assignment based on Bay-
esian population clustering implemented
in baps version 4.14 (Corander et al. 2003).
Each vertical bar represents an individual,
and bars are divided into proportions based
upon the probability of assignment to each
population. Individuals are clustered by coll-
ecting locality. baps recognized 15 sub-
populations, corresponding to the original
collecting localities
Table 2 Number of alleles at each microsatellite locus used in
genotyping
Locus
No. of alleles
B1-42
7
D036
11
D071
13
B1-36
7
D098
19
D108
12
D073
10
D082
14
D019
10
D065
14
B1-48
12
D021
13
D032
9


LANDSCAPE GENETIC INFERENCE OF DISPERSAL COSTS 1371
© 2009 Blackwell Publishing Ltd
ponds as largely differentiated, and collapsed the Riso ×
Eucalyptus (RE) population into others, primarily Impossible
× Mercury (IM). Thus, both visually and statistically, baps
recognized our 16 ponds as somewhat admixed, but with
sufficient fine-scale differences between breeding ponds to
recognize 15 separate subpopulations. Consistent with the
baps results, our amova test of these 15 subpopulations
attributed 12% of the total molecular variance to among-
population variation and 88% to within-population variation.
Gene-flow estimation
Genetic assignment in BayesAss+ indicated that most of the
interpond rates of gene flow in our analysis are indisting-
uishable from those generated by uninformative data. How-
ever, for four breeding pond pairs (HE–WT, HE–ET, WT–
LM, and LE–UM), the estimated dispersal rate fell outside
of the confidence interval provided for comparison with
uninformative data. These represent ‘significant’ or ‘measur-
able’ dispersal rates given our genotypic data and are the
four interpond dispersal rates used in our LCPA (Table 3).
These four rates are relatively high, ranging from 10.5 to
19.9% of the target population explained by gene flow from
the source, indicating that interpond movement can be
common. We found no significant differences in the density
of small mammal burrows around each pond for each pair
(P > 0.20 in all cases), suggesting that gene flow was not
substantially related to this important component of pond
quality. We did not survey burrow density across the entire
study area. If burrow density varied in the different habitat
types, then any benefit that it provided to  Ambystoma
californiense would have been factored into the overall cost
of traversing that habitat type.
Least-cost path analysis
Our least-cost path analysis indicates that dispersal through
chaparral is the least costly to  A. californiense, and that move-
ment through grassland is approximately twice, and through
oak woodland roughly five times as costly as movement
through chaparral (Table 4). A small range of costs values
(1.7–2.2 for grassland and 4.6–5.30 for oak woodland)
produced cost distances that fell within the 95% confidence
interval inferred from our genetic data (Table 4). The inferred
dispersal corridors are plotted on our habitat map as least-
cost paths in Fig. 4.
Discussion
Population structure and gene flow
Our finding of subtle differences in allele frequencies between
breeding ponds of Ambystoma californiense appears consistent
with similar results of population substructure in other
ambystomatid salamanders (Spear et al. 2005; Giordano
et al. 2007; Zamudio & Wieczorek 2007). Both for the micro-
satellites discussed here and for regional variation in mito-
chondrial DNA (Shaffer et al. 2004), substantial variation
exists among ponds at a local level (12% for microsatellites
data in this fine-scale study, and 18–31% for mitochondrial
DNA at a larger regional level). Despite this variation, key
differences between breeding sites remain. baps analysis,
which included prior information on population of origin,
identified 15 distinct subpopulations in our network of
16 breeding ponds. Thus, this system is an interesting
case where gene flow maintains connectivity between popu-
lations, but does not overwrite genetic signatures of among-
pond differentiation.
Given the observed moderate-low degree of microsatellite
variation between ponds, our observations of fairly high
levels of gene flow (nearly 20% in one case) between certain
ponds appear reasonable. Another study of a relatively
distantly related ambystomatid salamander (Zamudio &
Table 3 Relative gene flow, direct distances, and cost distances between the four breeding ponds used in the least-cost path analysis. All
measures are set relative (rate or distance = 1.00) to the shortest distance or lowest rate. ‘Cost distance’ is the expectation that would result
from the given dispersal rates if interpond dispersal is a reflection of the relative ease of movement across a landscape. For dispersal rate
and cost distance, the mean value is first and the 95% confidence interval is in parentheses. Population acronyms correspond to those used
in Table 1
HE–WT
HE–ET
UM–LE
WT–LM
Gene flow
1.25 (0.82–1.60)
1.00 (0.80–1.23)
1.90 (1.39–2.60)
1.17 (0.88–1.52)
Cost distance
1.52 (0.77–3.19)
1.90 (1.00–3.256)
1.00 (0.473–1.15)
1.62 (0.81–2.96)
Direct distance
1.00
1.35
1.23
1.31
Table 4 Inferred costs of dispersal through different habitat types,
resulting from least-cost path analysis. All costs are relative to
dispersal through chaparral, which is measured to be least costly.
Values are the relative costs of movement over equivalent distances
between different habitat types
Grassland
Chaparral
Woodland
Lower bound
1.7
1.0
4.6
Upper bound
2.2
—
5.3


1372 I. J. WANG, W. K. SAVAGE and H. B. SHAFFER
© 2009 Blackwell Publishing Ltd
Wieczorek 2007) found similarly high levels (up to 25%) of
gene flow across a larger, more mesic landscape. California,
with its Mediterranean climate of hot, dry summers may
appear to be a difficult place for overland amphibian
dispersal, but several field studies on California tiger sala-
manders indicate that overland dispersal among ponds
600 m apart is fairly common (Trenham et al. 2001) and that
individuals may move at least 1 km, and perhaps up to 3 km
from breeding sites (Trenham & Shaffer 2005; Searcy &
Shaffer 2008). Clearly, geographically proximate breeding
ponds form important interconnected networks, and under-
standing the landscape factors promoting or limiting gene
flow is critical to understanding the viability of populations
on a landscape (Shaffer et al. 2000; Trenham et al. 2001; Couvet
2002; Spear et al. 2005; Stevens et al. 2006; Zamudio & Wiec-
zorek 2007).
Costs of dispersal through different habitats
Our least-cost path analysis returned the surprising result
that dispersal through grassland is nearly twice as costly to
A. californiense as dispersal through chaparral. Ambystoma
californiense is typically associated with grassland habitat,
where it uses small mammal burrows for protection from
predators and temperature extremes (Loredo et al. 1996;
Trenham 2001; Trenham et al. 2001; Shaffer & Trenham 2005;
Trenham & Shaffer 2005). However, while chaparral is often
regarded as being a harsh, difficult habitat for movement,
our results indicate that this may not be the case. In fact, our
results are broadly compatible with a study in the related
blotched tiger salamander, Ambystoma tigrinum (Spear et al.
2005), which found that open shrub habitat (a habitat that
is structurally similar to chaparral) was correlated with
decreased population differentiation in the dry, mountainous
region of Yellowstone National Park. Our observation of a
fivefold greater cost of traversing oak woodland compared to
chaparral was also initially surprising, given the open canopy
and grassland understory of California oak habitat. Whether
these differential costs reflect biological differences in vegeta-
tion, microhabitat humidity, predator accessibility, small
mammal burrow density, or a number of other factors are
intriguing hypotheses that will require additional field studies.
Although our results disagree with the natural-history
expectation that grassland should be the preferred habitat
of A. californiense, they do not directly contradict any empir-
ical data on habitat costs or movement preferences for this
species. Although there are substantial data suggesting that
A. californiense prefer to reside in grassland, there are no data
on the habitat preferences that these salamanders have when
moving between ponds (Trenham 2001; Trenham et al. 2001;
Trenham & Shaffer 2005). Animals may prefer different
habitats for residence vs. dispersal, during different times
in their life cycles, or during different season. In addition,
the single radio-tracking study for this species (Trenham
2001) found that upland habitat use by California tiger
salamanders in the drier, less coastal habitat of Hastings
Reserve preferentially overexploited grassland and isolated
oaks compared to continuously wooded oak patches. Al-
though the data of Trenham (2001) are based on the frequency
of adult salamanders in their terrestrial retreats and ours
reflect gene flow between breeding sites, both indicate that
oak woodland is avoided (more costly) compared to grass-
land (unfortunately, there was no chaparral in the habitat
followed by Trenham 2001).
Obviously, the extent to which our method and results
can, and should, play a part in conservation management
Fig. 4 Habitat map showing least-cost paths
between breeding ponds for four interpopu-
lation dispersal corridors. The least-cost
paths shown are those that most closely fit
the relative mean dispersal rates. The paths
were calculated as having one cell width,
but are drawn as wider for visualization.
Population acronyms correspond to those
used in Table 1.


LANDSCAPE GENETIC INFERENCE OF DISPERSAL COSTS 1373
© 2009 Blackwell Publishing Ltd
will depend on the local landscape and the repeatability of
our results across the range of the species. As in any system,
corroborating evidence from multiple sources, including
direct field observations and measurements, are necessary
to understand the effects of different habitats to dispersal in
A. californiense and to truly test the efficacy of our proposed
methodology. Additionally, the possibility remains that spa-
tial differences at an even finer scale, such as subtle terrain
contours, contribute to the cost of traversing a landscape.
We hope that with increasingly detailed spatial data, these
fine-scale patterns can be fully resolved, just as the presently
available advances in GIS data have enabled detailed studies
of habitat differences on a landscape such as this. At the least,
our data indicate the importance of considering habitat types
to understanding the movement of animals across landscapes.
Conclusions
Traditionally, landscape genetics approaches have examined
landscapes as uniform space (Storfer 1999; Barbujani 2000;
Manel et al. 2003; Storfer et al. 2007). However, a deeper
understanding of the processes governing the movement of
genes on landscapes necessitates the use of both complex
landscape and genetic data (Barbujani 2000; Manel et al.
2003; Spear et al. 2005; Cushman et al. 2006; Storfer et al.
2007). Our results join a small set of empirical analyses that
demonstrate the feasibility and importance of incorporating
landscape characteristics into a richer understanding of
population genetic processes. Furthermore, our least-cost
path analysis methodology considers the specific distri-
bution of landscape features and their relation to natural
movement among populations, allowing us to make precise
inferences about the value of different habitat types and the
particular dispersal corridors that exist on a landscape.
With the increasing availability of GIS data and the ability
of users to generate their own, site-specific layers, the meth-
ods discussed here could become broadly applicable to a
wide range of taxa in the very near future. These methods
can be easily adapted to utilize a variety of other landscape
features, including geological formations, humidity levels,
the presence of roads or rivers, urban structures, tempera-
ture, and elevation, for the eventual development of fully
detailed, three-dimensional landscape data. Finally, if genetic
data are unavailable for dispersal rate estimates, or if ongo-
ing gene flow using assignment-based methods cannot be
estimated, mark–recapture data may serve in their place.
With the knowledge that organisms interact in intricate
ways with their landscapes (Slatkin 1987; Trenham et al.
2001; Spear et al. 2005), the incorporation of detailed land-
scape data into landscape genetic analyses seems like a
logical step. Landscape genetics is playing an increasingly
important role in population genetics by providing a frame-
work for quantitatively modelling the effects of landscapes
on gene flow, population substructure, and genetic vari-
ation (Manel et al. 2003; Storfer et al. 2007), and least-cost
path analysis provides an important tool for improving our
understanding of landscape effects.
Acknowledgements
We thank S. Worcester, B. Travers, and K. McNulty for field survey
data, B. Delgado and the Fort Ord Natural Reserve for field access
and support, D. Dittrich-Reed and L. Gray for laboratory assistance,
the UC Davis Division of Biological Sciences Sequencing Facility
for microsatellite genotyping support, and the Shaffer laboratory
group, K. Aquilino, and K. Edwards for comments on this project.
We thank the California Department of Fish and Game (permits
SC-2480 and SC-8439) and US Fish and Wildlife Service (permit
TE094642-0) for granting the permits that made our field collec-
tions possible. This work was funded by grants from California
Department of Transportation (CalTrans), the US Bureau of Recla-
mation/US Fish and Wildlife Service, the National Science Foun-
dation (grants DEB 0516475 and DEB 0213155), the US Department
of Agriculture (grant 04XN022), the University of California (UC)
Davis Agricultural Experiment Station (to H.B.S.) and a National
Science Foundation Graduate Research Fellowship and the UC
Davis Center for Population Biology (to I.J.W.).
References
Andersen LW, Fog K, Damgaard C (2004) Habitat fragmentation
causes bottlenecks and inbreeding in the European tree frog
(Hyla arborea). Proceedings of the Royal Society B: Biological Sciences,
271, 1293–1302.
Arnaud JF (2003) Metapopulation genetic structure and dispersal
pathways in the land snail Helix aspersa: influence of landscape
heterogeneity. Landscape Ecology, 18, 333–346.
Barbujani G (2000) Geographic patterns: how to identify them and
why. Human Biology, 72, 21.
Beebee TJC, Rowe G (2000) Microsatellite analysis of natterjack
toad Bufo calamita Laurenti populations: consequences of
dispersal from a Pleistocene refugium. Biological Journal of the
Linnean Society, 69, 367–381.
Berry O, Tocher MD, Sarre SD (2004) Can assignment tests measure
dispersal? Molecular Ecology, 13, 551–561.
Bohonak AJ (1999) Dispersal, gene flow, and population structure.
The Quarterly Review of Biology, 74, 21–45.
Collins JP, Storfer A (2003) Global amphibian declines: sorting the
hypotheses. Diversity and Distributions, 9, 89–98.
Corander J, Waldmann P, Sillanpaa MJ (2003) Bayesian analysis of
genetic differentiation between populations. Genetics, 163, 367–374.
Corander J, Sirén J, Arjas E (2008) Bayesian spatial modeling of
genetic population structure. Computational Statistics, 23, 111–129.
Coulon A, Cosson JF, Angibault JM et al. (2004) Landscape con-
nectivity influences gene flow in a roe deer population inhabiting
a fragmented landscape: an individual-based approach.
Molecular Ecology, 13, 2841–2850.
Couvet D (2002) Deleterious effects of restricted gene flow in frag-
mented populations. Conservation Biology, 16, 369–376.
Cushman SA, McKelvey KS, Hayden J, Schwartz MK (2006) Gene
flow in complex landscapes: testing multiple hypotheses with
causal modeling. The American Naturalist, 168, 486–499.
Fisher RN, Shaffer HB (1996) The decline of amphibians in Califor-
nia’s great central valley. Conservation Biology, 10, 1387–1397.


1374 I. J. WANG, W. K. SAVAGE and H. B. SHAFFER
© 2009 Blackwell Publishing Ltd
Fitzpatrick BM, Shaffer HB (2007) Introduction history and habitat
variation explain the landscape genetics of hybrid tiger sala-
manders. Ecological Applications, 17, 598–608.
Funk WC, Blouin MS, Corn PS et al. (2005) Population structure of
Columbia spotted frogs (Rana luteiventris) is strongly affected by
the landscape. Molecular Ecology, 14, 483–496.
Geffen ELI, Anderson MJ, Wayne RK (2004) Climate and habitat
barriers to dispersal in the highly mobile grey wolf. Molecular
Ecology, 13, 2481–2490.
Gibbs JP (1998) Distribution of woodland amphibians along a for-
est fragmentation gradient. Landscape Ecology, 13, 263–268.
Giordano AR, Ridenhour BJ, Storfer A (2007) The influence of altitude
and topography on genetic structure in the long-toed salamander
(Ambystoma macrodactulym). Molecular Ecology, 16, 1625–1637.
Guerry AD, Hunter ML (2002) Amphibian distributions in a land-
scape of forests and agriculture: an examination of landscape
composition and configuration. Conservation Biology, 16, 745–754.
Hickman JC (1993) The Jepson Manual: Higher Plants of California.
University of California Press, Berkeley, California.
Jehle R, Arntzen JW (2002) Review: microsatellite markers in
amphibian conservation genetics. Herpetological Journal, 12, 1–9.
Loredo I, Vuren DV, Morrison ML (1996) Habitat use and dispersal
behavior of the California tiger salamander. Journal of Herpeto-
logy, 30, 282–285.
Manel S, Schwartz MK, Luikart G, Taberlet P (2003) Landscape
genetics: combining landscape ecology and population genet-
ics. Trends in Ecology & Evolution, 18, 189–197.
Michels E, Cottenie K, Neys L, de Gelas K, Coppin P, de Meester L
(2001) Geographical and genetic distances among zooplankton
populations in a set of interconnected ponds: a plea for using
GIS modelling of the effective geographical distance. Molecular
Ecology, 10, 1929–1938.
Newman RA, Squire T (2001) Microsatellite variation and fine-
scale population structure in the wood frog (Rana sylvatica).
Molecular Ecology, 10, 1087–1100.
van Oosterhout C, Hutchinson WF, Wills DPM, Shipley P (2004)
Micro-Checker: software for identifying and correcting genotyping
errors in microsatellite data. Molecular Ecology Notes, 4, 535–538.
Paetkau D, Slade R, Burden M, Estoup A (2004) Genetic assign-
ment methods for the direct, real-time estimation of dispersal
rate: a simulation-based exploration of accuracy and power.
Molecular Ecology, 13, 55–65.
Peakall ROD, Smouse PE (2006) GenAlEx6: genetic analysis in
Excel. Population genetic software for teaching and research.
Molecular Ecology Notes, 6, 288–295.
Pearse DE, Crandall KA (2004) Beyond FST: analysis of population
genetic data for conservation. Conservation Genetics, 5, 585–602.
Rittenhouse TAG, Semlitsch RD (2006) Grasslands as movement
barriers for a forest-associated salamander: migration behavior
of adult and juvenile salamanders at a distinct habitat edge. Bio-
logical Conservation, 131, 14–22.
Savage WK (2008) Tandem repeat markers for population genetic
studies of the protected California tiger salamander. Conservation
Genetics, 9, 1707–1710.
Schippers P, Verboom J, Knaapen JP, van Apeldoorn RC (1996)
Dispersal and habitat connectivity in complex heterogeneous
landscapes: an analysis with a GIS-based random walk model.
Ecography, 19, 97–106.
Searcy CA, Shaffer HB (2008) Calculating biologically accurate
mitigation credits: insights from the California tiger salamander.
Conservation Biology, 22, 997–1005.
Shaffer HB, Trenham PC (2005) California tiger salamanders. In:
Amphibian Declines: The Conservation Status of United States Spe-
cies (ed. Lannoo M), pp. 605–608. University of California Press,
Berkeley, California.
Shaffer HB, Fellers GM, Magee A, Voss SR (2000) The genetics of
amphibian declines: population substructure and molecular
differentiation in the Yosemite toad, Bufo canorus (Anura, Bufonidae)
based on single-strand conformation polymorphism analysis
(SSCP) and mitochondrial DNA sequence data. Molecular Ecology,
9, 245–257.
Shaffer HB, Pauly GB, Oliver JC, Trenham PC (2004) The molecular
phylogenetics of endangerment: cryptic variation and historical
phylogeography of the California tiger salamander, Ambystoma
californiense. Molecular Ecology, 13, 3033–3049.
Slatkin M (1987) Gene flow and the geographic structure of natural
populations. Science, 236, 787–792.
Smith MA, Green DM (2005) Dispersal and the metapopulation par-
adigm in amphibian ecology and conservation: are all amphibian
populations metapopulations? Ecography, 28, 110–128.
Smouse PE, Peakall R (1999) Spatial autocorrelation analysis of
individual multiallele and multilocus genetic structure. Heredity,
82, 561–573.
Spear SF, Peterson CR, Matocq MD, Storfer A (2005) Landscape
genetics of the blotched tiger salamander (Ambystoma tigrinum
melanostictum). Molecular Ecology, 14, 2553–2564.
Stevens VM, Verkenne C, Vandewostijne S, Wesselingh RA, Baguette
M (2006) Gene flow and functional connectivity in the natterjack
toad. Molecular Ecology, 15, 2333–2344.
Storfer A (1999) Gene flow and population subdivision in the
streamside salamander, Ambystoma barbouri. Copeia, 1999, 174–181.
Storfer A, Murphy MA, Evans JS et al. (2007) Putting the ‘land-
scape’ in landscape genetics. Heredity, 98, 128–142.
Trenham PC (2001) Terrestrial habitat use by adult California tiger
salamanders. Journal of Herpetology, 35, 343–346.
Trenham PC, Shaffer HB (2005) Amphibian upland habitat use
and its consequences for population viability. Ecological Applica-
tions, 15, 1158–1168.
Trenham PC, Bradley Shaffer H, Koenig WD, Stromberg MR (2000)
Life history and demographic variation in the California tiger
salamander (Ambystoma californiense). Copeia, 2000, 365–377.
Trenham PC, Koenig WD, Shaffer HB (2001) Spatially auto-
correlated demography and interpond dispersal in the salamander
Ambystoma californiense. Ecology, 82, 3519–3530.
Wiens JA (2001) The landscape context of dispersal. In: Dispersal
(eds Clobert J, Danchin E, Dhondt AA, Nichols JD), Oxford
University Press, Oxford, UK.
Wilson GA, Rannala B (2003) Bayesian inference of recent disper-
sal rates using multilocus genotypes. Genetics, 163, 1177–1191.
With KA, Gardner RH, Turner MG (1997) Landscape connectivity
and population distributions in heterogeneous environments.
Oikos, 78, 151–169.
Zamudio KR, Wieczorek AM (2007) Fine-scale spatial genetic
structure and dispersal among spotted salamander (Ambystoma
maculatum) breeding populations. Molecular Ecology, 16, 257–274.
Ian Wang studies the role of landscapes and environments on
population structure, gene flow, and adaptation in amphibians.
Brad Shaffer and his laboratory group have maintained a long-
standing interest in the evolution, ecology, and conservation biology
of ambystomatid salamanders, with a strong recent focus on long
term studies of the endangered California tiger salamander.
