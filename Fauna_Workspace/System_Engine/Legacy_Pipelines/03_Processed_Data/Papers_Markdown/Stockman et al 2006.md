--- 
source: Stockman et al 2006.pdf
--- 

Diversity and Distributions, (Diversity Distrib.) (2006) 12, 81–89
BIODIVERSITY
RESEARCH
© 2006 The Authors
DOI: 10.1111/j.1366-9516.2006.00225.x
81
Journal compilation © 2006 Blackwell Publishing Ltd
www.blackwellpublishing.com/ddi
ABSTRACT
One of the primary goals of any systematic, taxonomic or biodiversity study is the
characterization of species distributions. While museum collection data are important
for ascertaining distributional ranges, they are often biased or incomplete. The
Genetic Algorithm for Rule-set Prediction (GARP) is an ecological niche modelling
method based on a genetic algorithm that has been argued to provide an accurate
assessment of the spatial distribution of organisms that have dispersal capabilities.
The primary objective of this study is to evaluate the accuracy of a GARP model to
predict the spatial distribution of a non-invasive, non-vagile invertebrate whose
full distributional range was unknown. A GARP predictive model based on seven
environmental parameters and 42 locations known from historical museum records for
species of the trapdoor spider genus Promyrmekiaphila was produced and subsequently
used as a guide for ground truthing the model. The GARP model was neither a
signiﬁcant nor an accurate predictor of spider localities and was outperformed by
more simplistic BIOCLIM and GLM models. The isolated nature of Promyrmekiaphila
populations mandates that environmental layers and their respective resolutions
are carefully chosen for model production. Our results strongly indicate that, for
modelling the spatial distribution of low vagility organisms, one should employ a
modelling method whose results are more conducive to interpretation than models
produced by a ‘black box’ algorithm such as GARP.
Keywords
Araneae, conservation, ecological niche modelling, Mygalomorphae, predicting
species occurrences, Promyrmekiaphila.
INTRODUCTION
Understanding and delineating species distributions are an important
tool used to address numerous issues in ecology, biogeography
and evolution (Guisan & Thuiller, 2005) and are fundamental to
the conservation of biodiversity (Samways, 2005). Often, because
of ﬁnancial and political pressures, areas set aside for protection
are small and located away from urban centres (Balmford et al.,
2002); therefore, it is crucial to rigorously identify areas most
worthy of protection when resources are limited. Sites afforded
protection are often chosen because they harbour a high level of
species richness or contain endangered species (Myers, 1990;
Scott et al., 1993). The spatial distributional pattern of many
taxa may be highly fragmented with populations representing
evolutionary signiﬁcant units (Ryder, 1986; Avise & Nelson,
1989); thus, the full distributional ranges of the species deserve
conservation consideration to maximize the retention of genetic
and adaptive diversity. This is particularly important when
designing reserves to protect low vagility organisms, such as
small invertebrates, which can be highly susceptible to localized
extirpations due to environmental perturbation (Murphy et al.,
1990). Moreover, selection of a network of habitat fragments for
conservation must be prudently chosen, as some conﬁgurations
are more prone to extinction than others (Gilpin, 1987;
Neuhauser, 1998; Hanski, 2001).
While knowledge of species distributional ranges is clearly
necessary if effective measures are to be taken to preserve bio-
diversity (Brooks et al., 2004), the range limits of many species
remain largely unknown or are incomplete. Collections records
may be biased, resulting in an inaccurate assessment of the
species ranges (Nelson et al., 1990; Graham et al., 2004). There
are several reasons why the full range of a species may be unclear.
Foremost, many regions remain unsampled for a given taxonomic
group. The time and expense necessary to conduct an exhaustive
Department of Biology, East Carolina 
University, Howell Science Complex — N211, 
Greenville, North Carolina, 27858 USA 
Corresponding author. Amy K. Stockman, 
Department of Biology, East Carolina University, 
Howell Science Complex — N211, Greenville, 
North Carolina, 27858 USA. 
E-mail: aks0126@mail.ecu.edu
Blackwell Publishing, Ltd.
An evaluation of a GARP model as 
an approach to predicting the spatial 
distribution of non-vagile invertebrate 
species
Amy K. Stockman, David A. Beamer and Jason E. Bond


A. K. Stockman et al.
82
© 2006 The Authors
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
sampling over a large area often preclude such endeavours. Even
in areas where a concerted effort has been made to sample the
regional fauna and ﬂora, progress has often been hampered
by poor access (i.e. private property, no trails or roads, etc.).
Additionally, many species are small, cryptic, or otherwise easy
to overlook and require special sampling techniques to detect.
Finally, many taxa are known from only a few specimens
encountered incidentally by non-scientists, and as such, tend to
come from highly populated areas. In the absence of complete
distributional records and sampling, ecological niche modelling
using Geographical Information Systems (GIS) data provides an
approach that can potentially overcome some of the hurdles
discussed above (Raxworthy et al., 2003).
Numerous studies have employed a GIS spatial analysis
approach, the Genetic Algorithm for Rule-set Prediction (GARP
— Stockwell & Peters, 1999), to locate suitable niches of an
assortment of vertebrate taxa, including birds (Peterson et al.,
2002a), rodents (Anderson et al., 2002), and ﬁsh (Wiley et al.,
2003). GARP has even uncovered new species when presumed
sister taxa were used to generate the model (Raxworthy et al.,
2003). However, we see three major problems with the GARP
approach. First, it is what is often characterized as a ‘black box’
technique. For example, there is no way to analyse the respective
contributions of individual predictor variables to the model.
Second, on only one occasion have models produced by GARP
been evaluated by ground truthing (Raxworthy et al., 2003),
and third, non-vagile organisms potentially present a special
problem with regard to modelling their distribution using GARP
(or potentially any other technique), in particular, problems
associated with the resolution (i.e. GIS spatial scale and layer
resolution) of the modelled area and selection of appropriate
environmental layers.
In this study, we used GARP to create a model to predict the
spatial distribution of a genus of trapdoor spiders using a limited
set of museum collections records. First, we want to know
whether a model produced by GARP can be used to accurately
assess the spatial distribution of a taxa based on limited, and
perhaps biased, collections records. As a direct result of our
exhaustive sampling efforts in 2005, we now consider the dis-
tribution of Promyrmekiaphila to be well deﬁned; prior to our
investigation, the full extent of this spider’s range was unknown.
The ability to characterize an organism’s spatial distribution using
only museum data can save vast amounts of time, energy, and
money necessary to engage in formal collecting expeditions
(Graham et al., 2004), facilitate the delineation of areas for
preservation (Ferrier et al., 2002), and guide collecting efforts
for population, phylogeographical, and systematic studies. We
also provide a limited comparison of the performance of the
GARP model with two ‘simple’ modelling approaches, a climatic
envelope model and a generalized linear model (GLM). Finally,
we present a GARP model based solely on recently, formally
collected data for comparison with the original GARP model.
To our knowledge, there is a single published study evaluating
the efﬁcacy of GARP models to predict the spatial distribution of
a taxon, using actual ground truthing (i.e. going into the ﬁeld
and rigorously testing the accuracy and precision of the model)
(Raxworthy et al., 2003). The accuracy of GARP models has
heretofore been analysed generally for species whose distribu-
tions are already known (e.g. Anderson et al., 2002, 2003, e.g.,
Peterson et al., 2002a; Loiselle et al., 2003). Furthermore, this
paper will provide a limited comparative analysis of GARP with
other predictive methods. GARP models have been assumed to
perform better than GLM or BIOCLIM models because GARP
includes logistic regression and range envelopes as two of the
four methods employed by default in the algorithm (Anderson
et al., 2002; Stockwell et al., 1999; Peterson et al., 2002b); how-
ever, few comparative analyses have been published to support
this postulate. Stockwell and Peterson (2002) claimed that GARP
produced more accurate models than logistic regression, but
other studies have shown no signiﬁcant differences in model
accuracy between GARP, BIOCLIM, and GLM models (Elith,
2000; Loiselle et al., 2003).
Finally, this will mark the ﬁrst neutral assessment of GARP in
predicting the occurrence of not only a non-vagile organism, but
also a non-invasive invertebrate. Often overlooked in conservation
considerations, invertebrates represent the vast majority of the
biological diversity on the planet. Indeed, arthropods comprise
over 80% of all extant animal taxa (Ruppert et al., 2004), yet,
sadly, remain largely ignored in conservation efforts (Wilson,
1987).
METHODS
The trapdoor spider genus Promyrmekiaphila Schenkel, 1950, is
the focal taxon of this study (shown in Fig. 1). Three nominal
species currently compose the genus, and all are endemic to the
California Floristic Province, a Biodiversity Hotspot (Cincotta
et al., 2000). Members of this genus are small- to medium-sized
trapdoor spiders belonging to the spider infraorder Mygalo-
morphae and are known to be found in mesic areas of northern
and central California (Bond & Opell, 2002). They construct
and inhabit silk-lined burrows, typically located on steep banks,
which are covered by a hinged silken-soil trapdoor thought to
have a protective function and known to assist in prey capture.
Figure 1 Map of California showing the study area and a live 
Promyrmekiaphila specimen.


Modelling spatial distributions of non-vagile invertebrates
© 2006 The Authors
83
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
They are fossorial, rarely travelling far from their burrow (as evi-
denced by multigenerational burrow aggregations), except when
males wander short distances in search of females during mating
season. As with most mygalomorph spider species they have
limited means of dispersal (Maine, 1982; Coyle, 1983), and are
slow to reach sexual maturity — all characteristics which render
them highly susceptible to both environmental perturbation and
urban encroachment.
We employed a geospatial analysis that uses an artiﬁcial intel-
ligence method, GARP (available online, www.lifemapper.org/
desktopgarp), in concert with the Geographic Information
Systems software package,   GIS 9.0 (ESRI, 2004). GARP
infers correlations between environmental layers representing
known species localities and a set of biotic and abiotic parameters.
GARP is a genetic algorithm that produces predictive models for
species distribution; however, because GARP is non-deterministic,
multiple optimal models are produced, and subsequent runs
using the same data will produce slightly different results. GARP
may be useful when only presence data are available because true
absence data are not utilized as input. Pseudo-absences are
created in GARP by resampling from points within the study area
where the species has not been designated as present; however,
because these points are not true absence points, these points
potentially contain the species (Guisan & Zimmermann, 2000).
The initial GARP model was based on specimens obtained on
loan from museums and private collections. The least accurate
specimen localities were removed to minimize the amount of
heterogeneity in location accuracy, and, in order to control some
of the bias inherent in natural collections records, some of the
points were removed where multiple specimens were located within
a relatively small area (Guisan & Thuiller, 2005). The locality
data associated with the 42 remaining museum specimens were
georeferenced using United States Geological survey 1 : 25,000
topographic maps (Maps a la carte, Inc.).
Seven map layers were used in the GARP analysis representing
parameters that, based on our collective 15 years of ﬁeld experi-
ence, we know to inﬂuence the survival of these spiders. These
environmental coverages were all obtained from various sources
online and include elevation, aspect, soil texture, minimum
temperature in January, maximum temperature in July, historic
vegetation, and average annual precipitation (Table 1). All data
layers were clipped in  using a mask of our study area. The
study area in northern California was deﬁned roughly by
Monterey County in the south, the California/Oregon border in
the north, the Paciﬁc Ocean to the west, and the Sierra Nevada
Mountains to the east (Fig. 1). Most environmental layers were
obtained as rasters; vector data layers were converted to rasters in
 with the Feature to Raster Conversion Tool. An execut-
able, ___ (VanDerWal), was employed to
project all layers to the Universal Transverse Mercator coordinate
system North American Datum 1983 and equalize the cell sizes to
one arc-second resolution (approximately 30 m2), as well as
convert all layers to ASCII format — all prerequisites for GARP.
We set GARP to perform 20 runs per specimen with a conver-
gence limit of 0.01 and 1000 maximum iterations. All four rule
types (atomic, range, negated range, and logistic regression) were
employed as well as the best subset feature of GARP. Under these
settings, GARP produced a total of 420 models in which all cells
are predicted either present (1) or absent (0). We then used the
Summation feature in the Raster Calculator of  to make a
ﬁnal, cumulative predictive map.
Two additional predictive models were created based on the
same museum data. A BIOCLIM model was created using
– version 5.1.0.1 (Hijmans et al., 2001). The BIOCLIM
model is based on all 19 available climatic variables and a 30 arc-
second resolution. The GLM was created using binary logistic
regression analysis in  version 12.0. GLMs require presence
and absence data as input, so random pseudo-absence points
were created in –. The categorical variables — soil texture
and vegetation — could not easily be included in the analysis;
elevation and minimum temperature in January, the two most
signiﬁcant of the remaining layers according to the backward
stepwise method, were included in the model.
The GARP predictive map was used as a guide for ﬁeld collec-
tion efforts during a 1-week trip to the study area in March 2005
and 5 weeks in May and June 2005. We divided the map values
into four classes: predicted absent, and low, medium, and high
probability of presence. We attempted to collect spiders ran-
domly throughout the study area, as well as across two transects.
We identiﬁed two roads that traversed all four probability levels
— Stewart Point Skaggs Springs Road in Sonoma County and
Orr Springs Road in Mendocino County. Both roads run in a
general east–west direction. The GARP model shows the prob-
ability of species presence increases, in general, towards the coast.
We sampled at regular intervals of six miles along both transects
and gathered presence and absence data at each stop.
Table 1 Layer data used in GARP analyses
 
GIS data layers
Source
Elevation
National elevation data, United States Geological Survey, http://seamless.usgs.gov/
Aspect
Derived from elevation data in 
Maximum temperature in July
WorldClim, http://biogeo.berkeley.edu/worldclim/worldclim.htm
Minimum temperature in January
WorldClim, http://biogeo.berkeley.edu/worldclim/worldclim.htm
Rainfall
California Spatial Information Library, United States Geological Survey, http://gis.ca.gov/
Soil texture
State Soil Geographic (STATSGO) database, Natural Resources Conservation Service,
http://www.ncgc.nrcs.usda.gov/products/datasets/statsgo/


A. K. Stockman et al.
84
© 2006 The Authors
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
The presence and absence locality data associated with
specimens we collected in the ﬁeld were subsequently used as
independent test data to examine the performance of the three
models produced above. One measure of accuracy was found
using a comparison of each data point with its corresponding
GARP model prediction value (Anderson et al., 2002). Further
statistical assessments were derived from a confusion matrix and
include χ 2 and Kappa statistics and commission and omission
errors. Receiver operating characteristic (ROC) plots were
obtained to provide a threshold-independent measure of overall
accuracy and to compare the predictive ability of the GARP,
BIOCLIM, and GLM models.
Upon return from our two collecting trips, we created a ﬁnal
GARP model using the same parameters and settings, but based
solely on localities where we had collected from March–June
2005 to test whether data which have been formally collected,
and hence are less susceptible to sampling bias, would greatly
alter the predicted spatial distribution of the spiders. Further-
more, the locality data associated with our ﬁeldwork, obtained
through the use of a GPS unit, may be more accurate than some
of the historical descriptions associated with the museum
specimens.
RESULTS
The GARP model utilizing the 42 locality data points from
museum specimens is shown in Fig. 2(a). Areas where GARP
predicts the highest probability of presence are predominantly in
the immediate vicinity of the museum specimen records, but
moderate to high levels of probability are also deﬁned in areas
where Promyrmekiaphila have not been previously collected, for
example, in the northern part of the state near Eureka and the
Figure 2 Ecological niche distribution models for Promyrmekiaphila. Tan represents areas of predicted absence; green, light blue, and dark blue 
represent increasing probability levels of presence. (a) GARP map based on 42 locations from museum collections records; red dots represent 
museum specimens (scale bar = 35 km). (b–e) Red dots represent material collected from March–June 2005; crosses represent areas of absence: 
(b) GARP map based on museum localities; (c) GARP map based on recent material; (d) logistic regression map; and (e) BIOCLIM map. 
(f–g) Close-up of the predictive GARP models showing collection results along two transects (red dots indicate presence, crosses represent 
absence; scale bar = 10 km): (f) map based on museum specimens; (g) map based on recently collected material.


Modelling spatial distributions of non-vagile invertebrates
© 2006 The Authors
85
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
midsection of the Oregon/California border, the eastern slopes
surrounding the Central Valley, and the Sutter Buttes — the
remnants of a dormant volcano in the middle of the Central
Valley. From March–June 2005, we collected Promyrmekiaphila at
80 newly discovered localities and determined that the spiders
were absent at 49 different localities (Fig. 2b). Of those 129 points,
the GARP model predicted 61 cells present with spiders and 68
absent. These values were incorporated into a confusion matrix
(Table 2), which was used to calculate various measures of accu-
racy and error (Table 3).
Results of the χ 2 test demonstrate that the discrepancy
between observed and expected frequencies is too large to be
attributed to chance alone (χ 2 = 11.23, d.f. = 1, P < 0.001).
Because our expected data were taken from the GARP model, the
χ 2 test suggests that the proportion of cells actually observed
present and absent, respectively, do not match the proportions
predicted from the GARP model. Results show moderately high
degrees of both extrinsic commission error (false positives) and
omission error (false negatives). Out of the 80 points positively
identiﬁed as present, 39 were mistakenly predicted by the GARP
model to be absent. Out of the 49 points identiﬁed as absent, 20
were falsely predicted as present.
The χ 2 test evaluates GARP model signiﬁcance but does not
actually indicate the accuracy of the model. Although the GARP
model was not a signiﬁcant predictor of Promyrmekiaphila pres-
ence, in some instances non-signiﬁcant models may nonetheless
show a high degree of accuracy (Anderson et al., 2002). This dis-
crepancy is due to the difference between comparing proportions
in a signiﬁcance test and comparing each data point with its
corresponding GARP prediction value in a test for accuracy
(Anderson et al., 2002). For our data, only half of the collection
points (41 out of 80) fell into areas of predicted presence. Predic-
tivity of absence in the GARP model fared only slightly better,
with 29 (out of 49) of the localities determined to be lacking
Promyrmekiaphila falling into cells of predicted absence. Along
the transects, the observed state of the localities often did not
correspond to the predicted state; however, we did detect a
general trend of decreasing spider abundance as we travelled
eastward — a pattern exhibited in the GARP model.
The Kappa statistic is often used as a measure of overall accu-
racy because it incorporates all of the information contained
within the confusion matrix (Fielding & Bell, 1997). Based on the
assessment by Landis and Koch (1977) that K < 0.4 is poor, the
Kappa value calculated from our collection data suggests that
the GARP model performed very poorly (K = 0.097). According
to the ROC plot (Fig. 3), the area under the curve (AUC) for the
GARP model was 0.556, suggesting that using the model is no
better than simply guessing or ﬂipping a coin. Alternatively, the
BIOCLIM and GLM models (Fig. 2d–e) not only displayed
greater AUCs than the GARP model, but they were also signiﬁc-
ant predictors of the spatial distribution of Promyrmekiaphila
(Table 4).
The GARP model based solely on localities where we had col-
lected from March–June 2005 is shown in Fig. 2(c), and displays
an overall effect of range reduction — a further restriction of the
area considered to be a suitable habitat, although the model does
exhibit an increase in the probability of occurrence in many cells
in the immediate vicinity of the collection sites along the
Table 2 Confusion matrix created from material collected from 
March–June 2005
 
 
Prediction
Observed
Present
Absent
Total
Present
41
20
61
Absent
39
29
68
Total
80
49
129
Table 3 Measurements of accuracy derived from the confusion 
matrix presented in Table 2
 
 
Measure
Value
Commission index
0.408
Omission error
0.488
Kappa
0.097
Figure 3 ROC plots of GARP, BIOCLIM, and GLM models based 
on museum records, evaluated using recently collected material.
Table 4 Measurements associated with the ROC plots displayed in 
Fig. 3
 
 
Model
AUC
Std. error
Asymptotic sig.
BIOCLIM
0.699
0.046
0.000
GARP
0.556
0.053
0.287
LOG_REG
0.662
0.052
0.002


A. K. Stockman et al.
86
© 2006 The Authors
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
transects, as would be expected (Fig. 2f–g). However, we suspect
that the environmental conditions are similar to the north and
south of the transects — areas where GARP showed only a mod-
erate increase in the number of cells of predicted presence, even
after the addition of the March–June data. The addition of the
new data did convert the areas of moderate probability of species
occurrence near the eastern end of the transects to areas of pre-
dicted absence. Although no true absence data were employed in
the GARP models, we did not ﬁnd Promyrmekiaphila in those
locations.
Locality data for Promyrmekiaphila collected from March–
June 2005 can be accessed at www.mygalomorphae.org.
DISCUSSION
Compared to the other more computationally simplistic
approaches (BIOCLIM and GLM) examined for our data, the
GARP-produced model failed miserably in its ability to accu-
rately reconstruct the distribution of Promyrmekiaphila through-
out northern and central California. Because the BIOCLIM and
GLM models were produced using a slightly different set of pre-
dictive variables, conclusions that can be drawn from compari-
sons to the GARP model are obviously limited. Nevertheless,
these simpler models are not as computationally intensive and
are much easier to produce — qualities that would be attractive
to systematists not specializing in spatial modelling.
We attribute the failure of the GARP model to a number of
issues related to the restricted spatial distribution of the study
taxon and other issues related to the opaque nature of the GARP
algorithm. Primarily, resolution, or spatial scale, and predictor
variables are two components that must be prudently chosen
when constructing any distributional model. Organisms, like
Promyrmekiaphila, with low vagility and poor dispersal capabilit-
ies may further complicate these decisions due to their inherent
isolation. Problems associated with resolution of spatial data in
GIS analyses can be particularly pervasive when parcels of suit-
able habitat are disjunct. The area that a small, non-vagile species
inhabits may be only a few meters or less; thus, ﬁner resolution
usually provides better predictive ability in models (Guisan &
Thuiller, 2005). Thus, an increase in data resolution is one of the
primary factors necessary to increase model prediction accuracy,
particularly for areas with microtopographic variation (Guisan
& Zimmermann, 2000). Such a complex landscape deﬁnes our
study area in northern California. Guisan and Thuiller (2005)
argue that, for sessile organisms, not only must the combination
of all suitable conditions be present within a cell, but they must
all be present at the same speciﬁc location within the cell. This
requirement probably extends to highly non-vagile species as
well. The ecological GIS data sets (e.g. layers) used for modelling
are available at various resolutions, but even the highest resolu-
tion data sets can belie the heterogeneity of the landscape.
Consequently, modelling programs tend to identify large tracts
as suitable (or unsuitable) although the habitat is actually hetero-
geneous (Cowley et al., 1999).
Aside from issues of scale, which can overlook the isolated
nature of suitable habitat, isolation clearly presents other difﬁ-
culties especially for non-vagile species. This difﬁculty stems
from the fact that the actual species range can potentially be
overpredicted. Ecological niche models deﬁne areas that are
ecologically suitable for a species, but many factors may be respon-
sible for the absence of the species in such an area. Biotic inter-
actions (e.g. predators or competitors) may have precluded a
species from an otherwise suitable area. Historical geological
factors may have hampered dispersal to certain areas and poten-
tially represent a severe limiting factor in predictive models
because they are not accounted for in the model (Guisan &
Zimmermann, 2000). Or perhaps, the species has gone extinct as the
result of natural events or, more likely, of recent human activities.
All of the aforementioned factors intersect to form the species
realized niche (Soberón & Peterson, 2005). That said, it is import-
ant to note that there is some debate about whether spatial dis-
tribution models deﬁne a species fundamental niche or realized
niche. Guisan and Thuiller (2005) state that most of the literature
assumes, without proper evidence, that spatial models represent
the realized niche of the species, because their observed distribu-
tions are already constrained by biotic interactions and limiting
resources. A limited degree of information regarding biotic inter-
actions and accessibility (a function of historical geological fac-
tors and dispersal capabilities) may be introduced indirectly into
GARP via the pseudo-absences (Soberón & Peterson, 2005). The
realized niche may be signiﬁcantly smaller than the fundamental
niche if the degree and inﬂuence of biotic interactions are large.
For Promyrmekiaphila, we suspect that biotic interactions do not
play an overwhelming role in delimiting distribution. These
spiders are generalist predators known to occur frequently along-
side other burrowing spiders, and they themselves have few
predators, primarily parasitic pompilid wasps, which, based on
extensive ﬁeld observations, do not decimate populations. Acces-
sibility to suitable habitat, however, is expected to be a major
factor that severely constrains the realized niche as a much smaller
portion of the fundamental niche due to the fossorial nature
and limited dispersal capabilities of these spiders. In addition,
the genus may not have had time to reach a state of equilibrium
with its environment (Guisan & Thuiller, 2005). Animals with
adequate dispersal capabilities are often able to reach isolated
patches of suitable habitat, but highly non-vagile species are
more constrained, and even in relatively continuous areas of suit-
able habitat, they may not have been present long enough to have
dispersed throughout the area. Although some work has been
done with plants which incorporates dispersal capabilities into the
model (Iverson et al., 1999; Dullinger et al., 2004), we know of no
GIS layers that could incorporate this information; therefore,
some degree of overprediction is expected.
Overprediction, also called commission error or false posi-
tives, is desirable to some extent. Whereas areas predicted as
absent may be falsiﬁed by the discovery of the species at that
location, areas designated as absent of spiders can never truly
be proved as such, even after extensive searching. For this reason,
the commission error is often referred to, more correctly, as a
commission index. Extremely low commission index means the
data have been overﬁtted — essentially, the model only predicts
the species to occur in and around the original presence localities


Modelling spatial distributions of non-vagile invertebrates
© 2006 The Authors
87
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
used as training points in the model. Areas of overprediction are,
theoretically, places of suitable habitat. Although all of the areas
of predicted presence will not be occupied, these fragments of
predicted occurrence can potentially be used to test evolutionary
hypotheses regarding vicariant speciation. For instance, some
areas of intermediate habitat may have acted as corridors
between areas of currently occupied habitat. Overprediction has
also been used to predict the potential distributions of invasive
species including several invertebrate species (Ganeshaiah et al.,
2003; Soberon et al., 2001; Roura-Pascual et al., 2005). However,
one of the deﬁning characteristics of any invasive species is the
ability to disperse easily and widely (Richardson et al., 2000). For
any organism, dispersal from one area of suitable habitat to
another may be prevented by unfavourable environmental con-
ditions in the intermediate area which act as ecological barriers.
However, overprediction becomes a major factor with non-vagile
species because the degree of isolation becomes increasingly
larger as the vagility of an organism decreases. This may result in
too many false positives, in which case, the model is rendered a
failure.
Many of the areas determined to be overpredicted as a result of
our recent collection efforts in the ﬁeld did not match our expecta-
tions of suitable habitat. We made numerous stops in Siskiyou
County, at the northern reaches of the study area, from which
Promyrmekiaphila is not known, but predicted to occur by the
GARP model. The absence of Promyrmekiaphila at those loca-
tions could be due to the inability of these spiders to disperse
over great distances, or the presence of uninhabitable niches
lying intermediate between the areas in Siskiyou and the north-
ernmost area from which they are known (near Redding, Shasta
County). However, because the areas in Siskiyou County where
the GARP model predicted high probabilities of occurrence
appeared to us to be too rocky and lacking in the amount of soil
necessary to constitute suitable Promyrmekiaphila habitat, we
suspect that these overpredicted areas are an artefact of model
failure, due perhaps to the lack of necessary soil information
contained in the environmental layers.
Not including the factors critical to delimiting species distribu-
tions may cause GARP models to fail. The underlying premise
of these models is that predictable relationships exist between
the occurrence of a species and the environment. However,
for many species, especially fossorial invertebrate taxa, very
little is known with regards to their habitat requirements. This
is the case for Promyrmekiaphila, a genus for which very little
habitat data have been published. For our analyses we selected
environmental parameters that we believe play an important
role in delimiting the spatial distribution of these spiders.
However, it is possible that a critical environmental factor was
omitted. Guisan and Thuiller (2005) suggest that ﬁne-scale
resolution, as exhibited in Promyrmekiaphila, is controlled by
a patchy distribution of resources that are assimilated by the
species, such as water. Because these organisms are sedentary
burrowers, it is possible that speciﬁc soil features that were not
captured in our soil data are critical. The addition of environ-
mental layers such as water holding capacity of the soil may
improve the model.
Outside of this study, most of our collecting efforts are focused
on areas that appear to offer suitable habitat. In contrast, during
our ﬁeldwork in 2005, we directed much of our collecting efforts
to areas of predicted absence because the degree to which our
collecting efforts in areas of predicted absence conform to the
model provides us with a gauge of model accuracy (Anderson
et al., 2003). Although the vast majority of the absence points fell
into cells of predicted absence, the GARP models did exhibit a
high degree of omission error — almost half of the total points
identiﬁed as present upon observation had been misidentiﬁed by
the GARP model as absent. Although the relative costs of com-
mission and omission errors will vary according to the particular
aim of the model, omission error is particularly egregious when
using distribution models in the determination of areas for con-
servation consideration, because the omission of areas that actu-
ally contain populations may make the species susceptible to the
loss of genetic diversity (Fielding et al., 1997). Stockwell and
Peterson (2002) suggest that too many classes within an environ-
mental layer may result in high omission error. One way to min-
imize this could be to combine some of the classes within the
categorical layers.
Another potential problem with GARP modelling occurs
when the phylogeny of the study organism is unresolved.
Currently, three nominal sibling species compose the genus
Promyrmekiaphila, but the correct taxonomic position of these
species is unknown. If the species are closely related sister
taxa, speciation arose via vicariance, and the niche is conserved,
then the model should predict all species equally well. Con-
versely, if the niche is not conserved, then it may not perform
well. In our study there are three areas that differ signiﬁcantly
from the redwood and mixed hardwood forests from which most
of the specimens are known. This might also suggest areas of
secondary contact where the predicted range between two
species overlaps.
In the future, generalized additive models, GAM, could be used
to generate a model from presence-only data and computer-
generated pseudo-absences. This approach, although not as
accurate as using true presence/absence data, has been shown to
provide signiﬁcantly predictive models (Ferrier & Watson, 1997;
Zaniewski et al., 2002) with results that are easy to read and easy
to interpret (Guisan & Thuiller, 2005). This approach could pro-
vide a useful alternative to GARP when the spatial distribution of
a species is desired, but exhaustive sampling is not feasible.
CONCLUSION
A GARP model created from historical museum collections
records of a genus of trapdoor spiders proved to be an unreliable
guide for collecting in the ﬁeld and did not provide an adequate
representation of their true present-day spatial distribution. We
suspect that the extremely sedentary nature of trapdoor spiders
and absence of signiﬁcant environmental layers are the primary
culprits causing the inaccuracy of the GARP model produced in
our study. These spiders do not require large tracts of suitable
habitat, and the small patches where they are often located are
too ﬁne-scale to be represented in the currently available


A. K. Stockman et al.
88
© 2006 The Authors
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
environmental data sets. The GARP model exhibits a large
degree of overprediction, somewhat expected and not necessarily a
negative attribute of the models, as discussed earlier. However,
despite the large degree of overprediction, the GARP model failed to
predict spiders in several large-scale areas where spiders were
present. For organisms of low vagility, most currently available
data sets are at a resolution too course to provide accurate predic-
tions. GARP models may perform better at a courser resolution;
however, this would provide only an ‘extent of occurrence’ map.
These maps represent a gross geographical scale and, because the
organism is unlikely to inhabit all areas within the extent of
occurrence, primarily delineate the extreme boundaries of the
distributional range. A more realistic depiction of the actual
range are represented by ‘areas of occupancy’, a network of some-
times disjunct patches of habitat of various levels of suitability
(Gaston, 1994).
GARP models have previously been used to characterize the
distribution of more vagile taxa and are alleged to be useful in
predicting future distributions of invasive species, as well as in
modelling potential habitat translocations due to climate change.
However, based on the results of our study, our comparisons to
other modelling approaches, and the current unavailability of
data at an appropriate resolution, we do not recommend that
GARP be used as an approach to modelling species distributions
of non-vagile trapdoor spiders and suspect that this recommen-
dation should be extended, at a minimum, to all non-vagile
invertebrate species. Moreover, we do not recommend GARP as
a ﬁrst approach to modelling species distributions for system-
atists because, as demonstrated, models generated by simpler
methods with fewer variable types perform better. GARP, unlike
BIOCLIM or GLM, is more difﬁcult to implement, is computa-
tionally intensive, and, because it is a ‘black box’ approach,
algorithm outcomes are virtually impossible to interpret and
troubleshoot.
ACKNOWLEDGEMENTS
Brent Hendrixson and three anonymous reviewers made useful
comments on an earlier draft of this paper. This work was sup-
ported by National Science Foundation Grant DEB 0315160.
REFERENCES
Anderson, R.P., Gómez-Laverde, M. & Peterson, A.T. (2002)
Geographical distributions of spiny pocket mice in South
America: insights from predictive models. Global Ecology and
Biogeography, 11, 131–141.
Anderson, R.P., Lew, D. & Peterson, A.T. (2003) Evaluating
predictive models of species’ distributions: criteria for selecting
optimal models. Ecological Modelling, 162, 211–232.
Avise, J.C. & Nelson, W.S. (1989) Molecular genetic relationships
of the extinct dusky seaside sparrow. Science, 243, 646–648.
Balmford, A., Bruner, A., Cooper, P., Costanza, R., Faber, S.,
Green, R.E., Jenkins, M., Jefferiss, P., Jessammy, V., Madden, J.,
Munro, K., Myers, N., Naeem, S., Paavola, J., Rayment, M.,
Rosendo, S., Roughgarden, J., Trumper, K. & Turner, R.K.
(2002) Economic reasons for conserving wild nature. Science,
297, 950–953.
Bond, J.E. & Opell, B.D. (2002) Phylogeny and taxonomy of the
genera of south-western North American Euctenizinae
trapdoor spiders and their relatives (Araneae: Mygalomorphae,
Cyrtaucheniidae). Zoological Journal of the Linnean Society,
136, 487–539.
Brooks, T.M., da Fonseca, G.A.B., & Rodrigues, A.S.L. (2004)
Protected areas and species. Conservation Biology, 18, 616.
Cincotta, R.P., Wisnewski, J. & Engelman, R. (2000) Human
population in the biodiversity hotspots. Nature, 404, 990–
992.
Cowley, M.J.R., Thomas, C.D., Thomas, J.A. & Warren, M.S.
(1999) Flight areas of British butterﬂies: assessing species
status and decline. Proceedings of the Royal Society of London.
Series B: Biological Sciences, 266, 1587–1592.
Coyle, F.A. (1983) Aerial dispersal by mygalomorph spiderlings
(Araneae, Mygalomorphae). Journal of Arachnology, 11, 283–
286.
Dullinger, S., Dirnbock, T. & Grabherr, G. (2004) Modelling
climate change-driven treeline shifts: relative effects of temper-
ature increase, dispersal and invasibility. Journal of Ecology, 92,
241–252.
Elith, J. (2000) Quantitative methods for modelling species
habitat: comparative performance and an application to
Australian plants. Quantitative methods in conservation biology
(ed. by S. Ferson and M.A. Burgman). Springer, New York.
ESRI (2004) ARCGIS. Environmental Systems Research Institute,
Inc., Redlands, California.
Ferrier, S. & Watson, G. (1997) An evaluation of the effectiveness
of environmental surrogates and modeling techniques in pre-
dicting the distribution of biological diversity. Environment
Australia, Canberra. http://www.ea.gov.au/biodiversity/
publications/technical/surrogates/pubs/surrogates.pdf.
Ferrier, S., Watson, G., Pearce, J. & Drielsma, M. (2002)
Extended statistical approaches to modelling spatial pattern in
biodiversity in northeast New SouthWales. Biodiversity and
Conservation, 11, 2275–2307.
Fielding, A.H. & Bell, J.F. (1997) A review of methods for the
assessment of prediction errors in conservation presence/
absence models. Environmental Conservation, 24, 38–49.
Ganeshaiah, K.N., Barve, N., Nath, N., Chandrashekara, K.,
Swamy, M. & Shanker, R.U. (2003) Predicting the potential
geographical distribution of the sugarcane woolly aphid using
GARP and –. Current Science, 85, 1526–1528.
Gaston, K.J. (1994) Rarity. Chapman & Hall, London.
Gilpin, M. (1987) Spatial structure and population vulnerability.
Viable populations for conservation (ed. by M. Soule), pp. 125–
139. Cambridge University Press, Cambridge.
Graham, C.H., Ferrier, S., Huettman, F., Moritz, C. & Peterson, A.T.
(2004) New developments in museum-based informatics and
applications in biodiversity analysis. Trends in Ecology and
Evolution, 19, 497–503.
Guisan, A. & Thuiller, W. (2005) Predicting species distribution:
offering more than simple habitat models. Ecology Letters, 8,
993–1009.


Modelling spatial distributions of non-vagile invertebrates
© 2006 The Authors
89
Diversity and Distributions, 12, 81–89, Journal compilation © 2006 Blackwell Publishing Ltd
Guisan, A. & Zimmermann, N.E. (2000) Predictive habitat
distribution models in ecology. Ecological Modelling, 135,
147–186.
Hanski, I. (2001) Spatially realistic theory of metapopulation
ecology. Naturwissenschaften, 88, 372–381.
Hijmans, R.J., Guarino, L., Cruz, M. & Rojas, E. (2001) Computer
tools for spatial analysis of plant genetic resources data: 1.
-. Plant Genetic Resources Newsletter, 127, 15–19.
Iverson, L.R., Prasad, A. & Schwartz, M.K. (1999) Modeling
potential future individual tree-species distributions in the
eastern United States under a climate change scenario: a case
study with Pinus virginiana. Ecological Modelling, 115, 77–93.
Landis, J.R. & Koch, G.C. (1977) The measurement of observer
agreement for categorical data. Biometrics, 33, 159–174.
Loiselle, B.A., Howell, C.A., Graham, C.H., Goerck, J.M., Brooks,
T., Smith, K.G. & Williams, P.H. (2003) Avoiding pitfalls of
using species distribution models in conservation planning.
Conservation Biology, 17, 1591–1600.
Maine, B.Y. (1982) Adaptations to arid habitats by mygalomorph
spiders. Evolution of the ﬂora and fauna of arid Australia (ed. by
W.R. Barker and P.J.M. Greensdale), pp. 273–284. SA Peacock
Publishing Co., Frewville, Adelaide, Australia.
Maps a la carte, Inc. North Chelmsford, Massachusetts. http://
www.topozone.com.
Murphy, D.D., Freas, K.E. & Weiss, S.B. (1990) An environment-
metapopulation approach to population viability analysis for a
threatened invertebrate. Conservation Biology, 4, 41–51.
Myers, N. (1990) The biodiversity challenge: expanded hot-spots
analysis. Environmentalist, 16, 243–256.
Nelson, B.W., Ferreira, C.A.C., Silva, M.F. & Kawasaki, M.L.
(1990) Endemism centres, refugia and botanical collection
density in Brazilian Amazonia. Nature, 345, 714–716.
Neuhauser, C. (1998) Habitat destruction and competitive
coexistence in spatially explicit models with local interactions.
Journal of Theoretical Biology, 193, 445–463.
Peterson, A.T., Ball, L.G. & Cohoon, K.P. (2002a) Predicting dis-
tributions of Mexican birds using ecological niche modelling
methods. Ibis, 144, E27–E32.
Peterson, A.T., Stockwell, D.R.B. & Kluza, D.A. (2002b) Dis-
tributional prediction based on ecological niche modeling of
primary occurrence data. Predicting species occurences: issues of
accuracy and scale (ed. by J.M. Scott, P.J. Heglund, M.L. Morrison,
J.B. Hauﬂer, M.G. Raphael, W.A. Wall and F.B. Samson),
pp. 617–623. Island Press, Washington, D.C.
Raxworthy, C.J., Martinez-Meyer, E., Horning, N., Nussbaum,
R.A., Schneider, G.E., Ortega-Huerta, M.A. & Peterson, A.T.
(2003) Predicting distributions of known and unknown reptile
species in Madagascar. Nature, 426, 837–841.
Richardson, D.M., Pysek, P., Rejmanek, M., Barbour, M.G.,
Panetta, F.D. & West, C.J. (2000) Naturalization and invasion
of alien plants: concepts and deﬁnitions. Diversity and Distri-
butions, 6, 93–107.
Roura-Pascual, N., Suarez, A., Gómez, C., Pons, P., Touyama, R.,
Wild, A.L. & Peterson, A.T. (2005) Geographic potential of
Argentine ants (Linepithema humile Mayr) in the face of global
climate change. Proceedings of the Royal Society of London.
Series B: Biological Sciences, 271, 2527–2535.
Ruppert, E.E., Fox, R.S. & Barnes, R.D. (2004) Invertebrate zoology:
a functional evolutionary approach. 7th edn. Thomson Learning,
Belmont, California.
Ryder, O.A. (1986) Species conservation and systematics: the
dilemma of subspecies. Trends in Ecology and Evolution, 1, 9–
10.
Samways, M.J. (2005) Insect diversity conservation. Cambridge
University Press, Cambridge.
Scott, J.M., Davis, F., Csuti, B., Noss, R., Butterﬁeld, B., Groves, C.,
Anderson, H., Caicco, S., D’erchia, F., Edwards, Jr, T.C., Ulliman,
J. & Wright, R.G. (1993) Gap analysis: a geographic approach
to protection of biodiversity. Wildlife Monographs, 123, 1–41.
Soberon, J., Golubov, J. & Sarukhan, J. (2001) The importance
of Opuntia in Mexico and routes of invasion and impact of
Cactoblastic cactorum (Lepidoptera: Pyralidae). Condor, 103,
599–605.
Soberón, J. & Peterson, A.T. (2005) Interpretation of models of
fundamental ecological niches and species’ distributional
areas. Biodiversity Informatics, 2, 1–10.
Stockwell, D. & Peters, D. (1999) The GARP modelling system:
problems and solutions to automated spatial prediction. Inter-
national Journal of Geographical Information Science, 13, 143–
158.
Stockwell, D.R.B. & Peterson, A.T. (2002) Effects of sample size
on accuracy of species distribution models. Ecological Model-
ling, 148, 1–13.
VanDerWal, J. ___, Windsor, Ontario.
http://www.uwindsor.ca/plantecology.
Wiley, E.O., McNyset, K.M., Peterson, A.T., Robins, C.R. &
Stewart, A.M. (2003) Niche modeling and geographic range
predictions in the marine environment using a machine-
learning algorithm. Oceanography, 16, 120–127.
Wilson, E.O. (1987) The little things that run the world (the
importance and conservation of invertebrates). Conservation
Biology, 1, 344–346.
Zaniewski, A.E., Lehmann, A. & Overton, J.M. (2002) Predicting
species spatial distributions using presence-only data: a case
study of native New Zealand ferns. Ecological Modelling, 157,
261–280.
