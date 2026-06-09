--- 
source: Ecological Modelling 2006 Romero-Calcerrada.pdf
--- 

ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
available at www.sciencedirect.com
journal homepage: www.elsevier.com/locate/ecolmodel
Habitat quality assessment using Weights-of-Evidence
based GIS modelling: The case of Picoides tridactylus as
species indicator of the biodiversity value of the
Finnish forest
Raul Romero-Calcerrada a, Sandra Luque b,∗
a School of Engineering Science and Technology, Universidad Rey Juan Carlos, Calle Tulip´an s/n, E-28933 M´ostoles Madrid, Spain
b METLA–Finnish Forest Research Institute, Helsinki Research Centre, Unioninkatu 40 A, FIN-00170 Helsinki, Finland
a r t i c l e
i n f o
Article history:
Received 8 April 2005
Received in revised form 12
December 2005
Accepted 1 February 2006
Published on line 29 March 2006
Keywords:
Habitat quality modelling
Landscape monitoring
Biodiversity indicators
National Forest Inventory
Bayesian statistics
a b s t r a c t
Biodiversity issues have gained importance in forestry as a result of the increased aware-
ness of forest landscape changes, but still there is much to do before forest management
meets reasonable goals for forest protection and renewal of biodiversity. In this work, we
focus on boreal forest landscapes, using Finland as a case study, and taking advantage
of a valuable database—the National Forest Inventory (NFI). We explore a multicriteria
approach by using a predictive habitat suitability model for three-toed woodpecker (Picoides
tridactylus) based on Weights-of-Evidence (WofE) and a combination of remote sensing and
ﬁeld data derived from the Multisource Finnish National Forest Inventory (MS-NFI). The
WofE model is a quantitative method used for combining evidence to examine the support
for a given hypothesis. WofE involves the estimation of a response variable (favourability
for certain habitat occurrence) and a set of predictor variables (e.g. GIS layers containing
environmental variables). WofE is based on a log-linear form of Bayes’ rule and uses the prior
probability distribution and the likelihood of the data to generate a posterior probability
distribution.
Very few examples exist of WofE being used to predict the spatial distribution of species or
communities using biophysical descriptors. This work explores WofE as a tool for rapid biodi-
versity assessment using georeferenced species information. Since the method is dependent
of the indicator species used as a surrogate of biodiversity value it can be applied for assess-
ing biodiversity conditions of both managed and protected areas to help decision-making
concerning protection of valuable habitats. Thus, the map of habitat suitability, represented
as a range of probabilities of occurrence, offers an objective framework for evaluating the
outcomes of different scenarios. Similarly, an objective assessment of habitat suitability pro-
vides a rational basis for management decisions incorporating impact on species habitat.
© 2006 Elsevier B.V. All rights reserved.
∗Corresponding author. Present address: CEMAGREF Groupement de Grenoble 2, rue de la papeterie, BP 76 F-38402 St. Martin-d’H`eres
cedex, France. Tel.: +33 476762827; fax: +33 476513803.
E-mail addresses: raul.romero.calcerrada@urjc.es (R. Romero-Calcerrada), Sandra.luque@cemagref.fr (S. Luque).
0304-3800/$ – see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.ecolmodel.2006.02.017


ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
63
1.
Introduction
In Europe, a wide variety of national and international
legal
mechanisms
(e.g.
EU-Habitats
Directive
(Directive
92/43/CEE) and EU-Bird Directive (Directive 79/409/CEE) and
agri-environment measures of EU Common Agricultural Pol-
icy) have been established to protect the environment, ensure
sustainable use of natural resources and maintain an accept-
able level of biodiversity. Nonetheless, in order to achieve efﬁ-
cient monitoring systems that focus on the understanding of
changes and its linkage to ecological processes, a thorough
detailed-spatial knowledge of the landscape is vital (Spence,
2001). In this context, there is a need to develop indicators
that simplify complexity in natural systems but still are well
supported by high quality data. The problem in biodiversity
monitoring and conservation is that usually exist vast gaps
in available information on the spatial distribution of biodi-
versity that poses a major challenge for the development of
biodiversity indicators and regional conservation planning. In
order to improve ecological monitoring at the landscape level,
it is possible to develop operational indicators from countries
having detailed data on forest structure derived from National
Forest Inventories (NFIs), not only to monitor forest conditions
but also to assess the status of forest protection and valuable
habitats (Luque et al., 2004a,b). It is becoming evident that
new strategies of planning in the framework of sustainable
development and within the framework of an integral/whole
perspective are needed (Miller and Lanou, 1995; Soul´e and
Sanjayan, 1998; Gutzwiller, 2002). In this context, the habitat
quality assessment and species distribution modelling could
play an important role into regional planning. Within this
rationality this work explores a rapid biodiversity assessment
method using spatial analysis and existing datasets.
In the present work, we discuss a multicriteria approach
by using a predictive habitat suitability model for three-toed
woodpecker (Picoides tridactylus) based on Weights-of-Evidence
(WofE) and a combination of remote sensing and ﬁeld data
derived from the Multisource Finnish National Forest Inven-
tory (MS-NFI). WofE is an effective tool that combines spatial
data to describe and analyse interactions and to provide sup-
port for decisions makers. The WofE model is a quantitative
method used for combining evidence to examine the support
for a given hypothesis. The model involves the estimation of a
response variable (favourability for certain habitat occurrence)
and a set of predictor variables (e.g. GIS layers containing envi-
ronmental variables, thematic maps of forest type, soil prop-
erties, etc.). Most of the published applications of WofE are
within the ﬁeld of geology for mapping mineral potential due
to its capability to combine patterns in maps in order to pre-
dict the probable distribution of point objects (Bonham-Carter,
1994; Bonham-Carter and Agterberg, 1999). Our aim is to test
how appropriate WofE can be to create spatial habitat–species
occurrence relationships.
Habitat quality assessment and habitat suitability maps
can help to design management plans to expand pro-
tected areas or create new ones in order to protect certain
species or habitats of particular importance in managed for-
est to improve regional planning (Romero-Calcerrada, 2002;
Rautj¨arvi et al., 2004). Other than supporting program resource
management, maps of habitat suitability, may as well ﬁnd
an application in evaluating a variety of land use change
or other scenarios. For example, mapped habitat suitability
allows the prediction of areas which may become occupied or
unoccupied if the distribution of a species expands or con-
tracts (Aspinall, 1992; Aspinall and Veitch, 1993). However,
such changes will have biological or environmental causes and
require additional information for accurate prediction. A map
of habitat suitability, represented as a range of probabilities
of occurrences, offers an objective framework for evaluating
the outcomes of different scenarios (Aspinall, 1992). Similarly,
an objective assessment of habitat suitability provides a ratio-
nal basis for management decisions incorporating impacts on
species habitat.
In Finland, a high proportion of commercial forests is
within the sphere of woodlot-speciﬁc forest planning, which
enables the use of a forest decision support system as a link
between ecological knowledge and practical forestry (Store
and Jokimaki, 2003; Nuutinen et al., 2001). In order to improve
this existing forest management planning, it is essential that
the decision alternatives be assessed with respect to a combi-
nation of expert knowledge and habitat models. A challenge
is to develop methods and practices of locating and evaluating
suitable sites for threatened species. The problem is that in the
case of biodiversity conservation empirical evaluation models
based on real ﬁeld data for all species of interest cannot be
expected to become available. One way of dealing with this
problem, as proposed in this work, is to use indicator species
and predictive models to identify possible causal relationships
between species distribution, environmental data, and ecolog-
ical conditions. The model proposed in this work is relatively
easy to interpret and to use and constitutes an effective tool
that combines spatial data to describe and analyse interac-
tions while providing support for decisions makers.
2.
Materials
2.1.
Lammi region as habitat for three-toed
woodpeckers
The structure of Fennoscandian boreal forest is relatively
homogeneous due to the low tree species diversity (Essen et
al., 1997). The study area – Lammi region – used in the present
study is located in the south boreal zone according to the
vegetation scheme developed by Ahti et al. (1968). The area
selected within this region encompass 145,895 ha in Southern
Finland (Fig. 1), dominated by coniferous forest, mostly Nor-
way spruce. To the north the area remained wilderness-like
because of stony and rough terrain, which is difﬁcult to access
and unﬁt for agriculture. More intensive use of the land can
be seen towards a gradient to the south where agricultural
land (14% of the total study area) dominates the landscape
and clear cuts are more intense. To the north there are also
several forest areas protected under different status includ-
ing peatlands areas, which contrast with the more intensive
land pressures to the south (Fig. 2). The landscape is dom-
inated by forest land (71%) scattered with water bodies and
lakes; urban areas are rather low (1.5%). Some of the freshwa-
ter habitats, within the area, are listed according to Annex 1 of


64
ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
Fig. 1 – Location of the study area in southern Finland
(window size 145,895 ha). Bird census area (61◦15′N;
25◦00′E) sampled within a central area within the region
that consists of 35,268 ha (dark grey area).
Fig. 2 – Location of nesting sites in relation to protected
areas of different status. Shaded areas indicate Natura 2000
sites.
the EU-Habitat Directive (Directive 92/43/CEE); mostly Natural
dystrophic lakes and ponds also Raised bogs and mires and
fens (active raised bogs and degraded raised bogs still capa-
ble of natural regeneration). In terms of Forest habitats there
are areas representative of Western Ta¨ıga and Bog woodland.
In general, the region is considered of high biodiversity value,
mostly due to the abundance of herb-rich forests and dead
wood values higher than the national average (>3 m3/ha).
2.2.
Finnish National Forest Inventory (NFI) data and
remote sensing data
The thematic maps that were used as the input layers of the
habitat model were derived from two types of Finnish National
Inventory data. The multisource thematic maps that represent
the volume of growing stock (m3/ha), stand age and poten-
tial productivity of the site were further processed. The pixel
level predictions were produced to wall to wall forest charac-
teristics in the Multisource Finnish National Inventory (MS-
NFI) based on k-nearest-neighbour (k-nn) estimation and its
improved version (Tomppo, 1991; Tomppo and Halme, 2004).
MS-NFI procedure assigns ﬁeld data of forest inventory to all
satellite image pixels using a multisource approach version
(Tomppo, 1991; Tomppo and Halme, 2004). Digital maps are
used to delineate forest land from other land use classes.
Satellite images, together with ﬁeld data measurements, are
used to estimate forestry parameters for the areas of inter-
est (for more details, see: Tomppo, 1991; Tomppo and Halme,
2004). An essential property of this method is that all inven-
tory variables measured in the ﬁeld can be estimated at the
same time for computation units. Another advantage is that
area statistics and thematic maps are produced by the same
method (Tomppo, 1991; Tomppo et al., 1997). For this study we
used data derived from the 9th Finnish National Forest Inven-
tory (NFI9) (ﬁeld measurements during 1996–2003). The plot
design is systematic and clustered with the distance between
two tracts varying from south to north. Over 150 variables
were measured in the ﬁeld in NFI9 (Tomppo et al., 1998);
stand age and volumes by tree species were employed, among
other relevant variables extracted from MS-NFI database such
as potential productivity of the site (Tomppo, 1992). For-
est structure was based on mean volume of the growing
stock by tree species (m3/ha) in the groups’ Scots pine (Pinus
sylvestris), Norway spruce (Picea abies), birch (Betula spp.) and
other broad-leaved trees, mainly aspen (Populus tremula) and
alder (Alnus spp.). For the purposes of the study, tree species
were assigned to four groups: pine, spruce, birch and other
broadleaved.
2.3.
Bird data
At the present in Finland, approximately 95% of the forest
land is managed (Ministry of Environment, 1999). Manage-
ment applied to forest stands has substantially changed local
forest properties, mostly in terms of tree species composi-
tion and the amount of coarse woody debris (Kouki, 1994;
Essen et al., 1997; Kouki and Niemel¨a, 1997; L¨ofman and
Kouki, 2001). Also, regional characteristics, such as the spa-
tial structure of forest landscapes, have been changed (Kouki
and L¨ofman, 1998; Luque et al., 2004a). As a result of these


ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
65
Table 1 – Input layers (after reclassiﬁcation) for evidential theme maps, where VOL is stand volume, AGE is stand age,
PROD is potential productivity of the site, D-WATER is distance to water bodies, D-ROAD is distance to roads, D-URB is
distance to urban areas
Code
VOL (m3/ha)
AGE (years)
PROD (m3/ha/year)
D-WATER (m)
D-ROAD (m)
D-URB (m)
1
1–20
1–20
0
0–100
0–25
0–300
2
21–40
21–40
1–2
101–200
26–50
301–600
3
41–60
41–60
2.1–3
201–300
>50
601–900
4
61–80
61–80
3.1–4
301–400
>900
5
81–120
81–100
4.1–5
401–500
6
121–160
101–120
5.1–6
501–600
7
161–200
121–140
601–700
8
201–240
>141
701–800
9
>240
801–900
10
901–1000
11
1001–1100
12
>1100
changes, almost 700 forest-dwelling species are considered as
threatened in Finland, mostly due to forestry practices during
the twentieth century (Ministry of Environment, 1992; Finnish
Environmental Institute, 2005).
The three-toed woodpecker (P. tridactylus) is considered
as an important indicator species in coniferous-dominated
natural forests. The species responds quite rapidly to forest
changes – spatial and structural – which makes it a good
indicator for temporal and spatial landscape changes. The
three-toed woodpecker is thought to be an indicator of natu-
ral forests, owing to its association with dead and dying trees
(Derleth et al., 2000; Pechacek and d’Oleire-Oltmanns, 2004,
p. 333). Three-toed woodpecker has strongly declined in Fin-
land since the middle of the 1970s but seem nowadays to
show an apparent stability of its population at a much lower
density which represents about the 27% of European (with-
out Russia) breeding population (BirdLife International, 2005).
Three-toed woodpecker habitat requirements, clearly conﬂict
with commercial forestry activities (Pechacek and d’Oleire-
Oltmanns, 2004). Habitat modelling generated using spatial
statistics and GIS can help in the characterizations of habitat
requirements and the localization of suitable habitats (Guisan
and Zimmermann, 2000).
An example using three-toed woodpecker (P. tridactylus) as
species indicator (census bird data provided by Timo Pakkala
– Finnish Museum of Natural History) in southern Finland
is used to test the model. Bird data is based on territory
mapping and consists of 212 territory sites of the three-toed
woodpecker sampled within a central area of the study site
that consists of 35,268 ha located at 61◦15′N; 25◦00′E (see
Figs. 1 and 2). The census is based on observations during the
period 1999–2002 for males, females and pairs detected. Only
centroids recorded for pairs detected as a measure of breeding
birds were used from the database provided, details on three-
toed woodpecker census data can be found in Pakkala et al.
(2002).
2.4.
Data input
Data preparation, input, subsequent map operations, and spa-
tial data analyses up to date have been carried out by ArcGIS
8.3, ArcView 3.3, and Erdas Imagine 8.6, in addition to in-house
software (developed at NFI-METLA). The software developed
by METLA was used mostly for NFI data handling and par-
ticular computations in relation to MS-NFI data. Probability
of suitable habitat was derived using Arc-WofE (Kemp et al.,
1999). All evidential theme maps derived from MS-NFI were
grouped by classes according to different threshold values
(see Table 1). In addition, distance-buffers from roads, agri-
cultural areas, and populated regions were used in the model.
The rationality of the buffers was to learn about the negative
impact of human pressures on the distribution of three-toed
woodpecker. Distance to water bodies was computed to learn
about the importance – in a positive way – of the proximity to
water resources for nesting sites.
3.
Method
The application of Bayesian inference to ecological questions
has blossomed since the publication in 1996 of a series of
papers on Bayesian inference for ecological research and envi-
ronmental decision making (Dixon and Ellison, 1996). Bayesian
methods have been used most widely in population and com-
munity ecology (see Table 1 in Ellison, 2004), in which there
are many competing models to explain ecological phenom-
ena (Hilborn and Mangel, 1997), the parameter values of the
models have high levels of uncertainty, and the reporting
of this uncertainty (as standard errors or conﬁdence inter-
vals) is common. Bayesian inference is used extensively to
model dynamics of single species, forecast population dis-
persal, growth, and extinction, and predict changes in meta-
population structure on fragmented landscapes (see Ellison,
2004 for examples).
Inductive spatial modelling based on Bayes’ theorem, as
applied in this work to the distribution of Woodpecker in
Lammi region in Finland, is one of a number of methods which
can be used to predict distribution on the basis of map data.
However, the Bayesian approach, as implemented here, does
have a number of speciﬁc advantages, particularly when oper-
ated within the context of a GIS. These are related to the
process by which the probability model is developed and the
output is produced. Some of the main advantages that can
be mention are as follows: (i) the inductive spatial modelling
provides a search method whereby hypotheses relating the
distribution of a mapped feature to possible explanatory data


66
ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
sets can be generated; (ii) the inputs to the model and the
hypotheses generated are derived through automated analy-
sis of relationships between the distribution to the modelled
and the predictor data sets. Avoiding, this way, the genera-
tion of subjective relationships; (iii) the approach incorporates
a procedure for assessing statistical signiﬁcance of relation-
ships between each predictor data set and the distribution
being modelled; (iv) the map output includes the predictive
model and estimates of error and relative error. This allows
conﬁdence in the model results to be objectively expressed
and its geographical variation quantiﬁed.
Statistical models combined with GIS are commonly
used to create potential distribution maps (Guisan and
Zimmermann, 2000). Habitat suitability models or predictive
distribution models are probability maps that depict the likeli-
hood of occurrence of a species (Store and Kangas, 2001). Habi-
tats/species distribution maps are particularly welcomed in
the design of natural protected areas, design of management
plans of threat areas, assessment of human impacts on biodi-
versity, or as a tool in the conservation management of threat-
ened species (Larson et al., 2004; Weclaw and Hudson, 2004;
Jerina et al., 2003; Duffy et al., 2001; Guisan and Zimmermann,
2000).
Despite the advantages of the approach, Bayesian inference
has not been widely use for estimating species occurrences
or species richness from geographically or logistically con-
strained samples, or in response to environmental change.
In the particular case of published applications of Weights-
of-Evidence (WofE), most of the work is concerned with the
ﬁeld of mapping mineral potential (Bonham-Carter et al., 1988,
1989; Agterberg et al., 1990; An et al., 1992; Goodacre et al., 1993;
Bonham-Carter, 1994; Bonham-Carter and Agterberg, 1999). As
mentioned, few examples exist of WofE being used to predict
the spatial distribution of species or communities using bio-
physical descriptors (Skidmore, 1989; Aspinall, 1992; Aspinall
and Veitch, 1993; Wintle et al., 2003; Ellison, 2004).
3.1.
The Weights-of-Evidence (WofE)
The Weights-of-Evidence (WofE) is a data-driven and discrete
multivariate statistical method that uses conditional proba-
bilities to determine the relative importance of a phenom-
ena “evidence”. WofE offers a measure of spatial association
between multiclass and/or binary maps – evidence maps –
and known point data (e.g. woodpecker nesting sites). WofE
is based on a log-linear form of Bayes’ theorem to combine
patterns in maps in order to predict the probable distribu-
tion of point objects (Bonham-Carter, 1994; Bonham-Carter
and Agterberg, 1999).
The advantage of using the loglinear model over the ordi-
nary probability expression is that the weights are easier to
interpret than probability factors. Because a positive weight
implies that the (evidential theme-training points) association
is greater than would be expected due to chance, it is relatively
easy to understand the results. The calculation of the posterior
logit is easy to follow (and program) because adding weights
together is similar to the intuitive approach for combining evi-
dence based on common sense.
As mentioned in the introduction, WofE involves the esti-
mation of a response variable (favourability for certain habi-
tat occurrence) and a set of predictor variables (e.g. GIS lay-
ers containing environmental variables, socio-economic vari-
ables, climatic variables, soils and vegetation characteristics).
In the case of the potential distribution of wildlife, a series of
binary maps are created for species occurrences. The species’
location is treated as point data. The evidence layers consist
of a set of spatial environmental datasets and forest struc-
ture thematic maps (e.g. categorical maps) considered as pre-
dictor variables for the present study. The weights are esti-
mated, using a statistical method based on Bayesian rules,
from the measured association between environmental vari-
ables (e.g. soils and vegetation characteristics) and a map of
species occurrence maps, known as well as response vari-
ables (e.g. bird species nesting sites). The evidence layers
are combined using Bayesian Rule in a multi-map overlay
operation, where the prior probability (P{D}) of an occurrence
is updated by the addition of predictor variables and their
weights to produce a single posterior probability (P{D|¯B} and
P{D|B}) map of occurrence. Based on the signiﬁcant spatial
associations in the evidential maps selected, the ﬁnal result
is a predictive map. The posterior probability map is based on
species’ potential distribution that reﬂects the spatial distribu-
tion of known occurrences, and predicts the distribution of yet
unidentiﬁed occurrences (Milne et al., 1989; Skidmore, 1989;
Aspinall, 1992; Aspinall and Veitch, 1993; Tucker et al., 1997;
Guisan and Zimmermann, 2000). For a more detailed descrip-
tion of the mathematical basis of the Bayesian Weights-of-
Evidence model, see Agterberg et al. (1990), Bonham-Carter
(1994), Bonham-Carter and Agterberg (1999), Kemp et al. (1999).
WofE model has been implemented in ArcView GIS 3.3
(Kemp et al., 1999, 2001). We used WofE to produce a predictive
model of woodpecker habitat quality. The GIS-based potential
habitat mapping process has ﬁve main steps:
1. calculating weights for each predictive map or evidence
map;
2. generalizing the evidential theme;
3. applying of conditional independence test;
4. creating a posterior probability theme (i.e. combination of the
evidence themes to predict the habitat quality map);
5. model evaluation.
3.2.
Calculating weights for each predictive map or
evidence map
One set of point occurrences locations (observed woodpecker
pairs) is used to calculate the weights for each evidential
theme, one weight per class, using the overlap relationships
between the points and the various classes on the theme.
Three approaches for calculating weights are possible: cate-
gorical weights (i) are used for themes where the attributes val-
ues are unordered (e.g. Land cover map) and for themes with
ordered values (e.g. volume of pine (m3/ha), thematic map);
cumulative weights are used in proximity analysis (e.g. distance
to rivers and lakes map, distance buffers were computed). In
cumulative ascending weights (ii), the class of evidential theme
near in space of the training points is the most predictive;
cumulative descending weights (iii) work in the opposite direc-
tion, therefore is applicable for points associated mainly with


ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
67
Table 2 – Approaches used to calculate weights
Evidential themes
Type of calculated weights
Type of data
Volume (m3/ha) of pine
Categorical weights
Ordinal variable
Volume (m3/ha) of spruce
Categorical weights
Ordinal variable
Volume (m3/ha) of Betula
Categorical weights
Ordinal variable
Volume (m3/ha) of broad leaf (rest of deciduous spp.)
Categorical weights
Ordinal variable
Stand age (years)
Categorical weights
Ordinal variable
Potential productivity of the site (m3/ha/year)
Categorical weights
Ordinal variable
Distance (m) to water (rivers, lakes, etc.)
Cumulative ascending weights
Ordinal variable
Distance (m) to roads
Cumulative descending weights
Ordinal variable
Distance (m) to urban areas
Cumulative descending weights
Ordinal variable
high distance values or when the class of evidential theme is
far away from the training point.
We used the type of calculated weights and the type of data
described in Table 2 to calculate weights for our study, based on
information available from the observed location(s) of wood-
pecker pairs and the evidence themes.
A WofE analysis results in a set of statistically measures –
weights (W+ and W−), contrast (C) and Studentized value of
C (CS) – that each reﬂect the spatial association between the
evidence maps and the training points.
The weights, W+ and W−, represent measures of the spa-
tial association between the observed occurrences (three-toed
woodpecker nesting areas) and the given evidence map (e.g.
volume of spruce). If more occurrences occur within a pattern
than would be expected by chance, then W+ is positive and W−
is negative. Conversely, W+ is negative and W−is positive when
fewer points occur within a pattern than would be expected
by chance. The sign W+ will always be opposite that of W–.
The contrast “C” (Eq. (1)) provides a measure of spatial asso-
ciation between a set of occurrence points and an evidence
pattern.
C = W+ −W−
(1)
A larger C value indicates a strong spatial association between
the occurrences and the evidence map. A breakpoint in a plot
of the contrast also can be used to identify a signiﬁcant thresh-
old, dividing the data into different classes (Harris et al., 2001).
For a positive spatial association, C is positive, usually in the
range 0–2 (Bonham-Carter et al., 1989); for a negative associ-
ation, C is negative in a similar range. C can be calculated in
order to obtain an optimum cut-off for classifying continuous
patterns into a binary (i.e. presence/absence) pattern. Under
normal conditions, the maximum value of C gives the cut-off
at which the predictive accuracy of the resulting pattern is
maximized (Bonham-Carter et al., 1988). Based on this rule, C
is used to select the cut-off for dividing continuous variables
into binary patterns (Bonham-Carter et al., 1989; Harris and
Pan, 1999; Harris et al., 2000).
In the case of a large area and a large number of occur-
rences, the maximum contrast often gives the best measure
of spatial correlation with the occurrence points (Asadi and
Hale, 1999; Carranza and Hale, 1999, 2000; Asadi and Hale,
2001; Carranza and Hale, 2002). However, where a small area
is being considered and there is only a small number of occur-
rence points, the uncertainty of the weights could be large
and C can be meaningless. The Studentized value of C (CS) is
a useful measure in this latter case (Bonham-Carter, 1994). CS
is calculated as the ratio of C to its standard deviation:
CS =
C
(C)
(2)
CS serves as an approximate test of the spatial association
between the occurrence point and a test domain or as an infor-
mal test that C is signiﬁcantly different from zero, or so the
contrast is likely to be “real” (Bonham-Carter, 1994; Asadi and
Hale, 1999; Carranza and Hale, 1999, 2000; Carranza and Hale,
2002). Values of CS greater than 1.96 indicate that the hypoth-
esis that C = 0 can be rejected at ˛ = 0.05 (Bonham-Carter et al.,
1989). The CS is also helpful and more useful than C for choos-
ing cut-off because it shows the contrast relative to the cer-
tainty or uncertainty due to the contrast “C” (Bonham-Carter,
1994).
3.3.
Generalizing the evidential themes
After considering the weights, contrast and CS for each class
into evidential, theme, we have decided on the appropriate
breaks to generalize each evidential themes. Reducing the
number of classes, often to just two classes (binary maps),
enhances the statistical robustness of the weights. However,
multiclass evidential themes are allowable and sometimes
desirable (Kemp et al., 1999), especially for environmental phe-
nomena where most of the boundaries are fuzzy rather than
clear linear boundaries.
We have considered in this study the multiclass evidential
themes and used different value of CS as the cut-off point for
the grouping process. As it was unclear whether we had ‘small’
or ‘large’ areas or occurrences, we adopted a conservative atti-
tude using CS. For a positive spatial association, CS will have
a positive value. High positive values of CS means high pre-
dictive power, and values close to zero mean lower predictive
power. We used the following criteria for grouping:
- Group W0 for CS < 1.96;
- Group W1 for 1.96 ≤CS < 3;
- Group W2 for 3 ≤CS < 4;
- Group W3 for 4 ≤CS < 5;
- Group W4 for CS ≥5.
This generalization rule is repeated for each theme that will
be used as evidence. In this process, the CS is also used for
testing the hypothesis that C is signiﬁcantly greater than zero.


68
ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
3.4.
Applying test of conditional independence
The predictive maps must assume the conditional indepen-
dence of the evidence maps. Then various measures are
applied to test the conditional independence assumption.
Conditional independence is tested to identify the maps that
will be accepted or rejected from the combination procedure.
Violation of this condition can result in an over- or under-
estimation of the weights. Statistical validation of the result-
ing predictive maps is examined, using a contingence table
between all pairs of maps (Kemp et al., 1999, 2001). If the Pair-
wise Conditional Independence Test indicates that some theme
pairs are strongly correlated, one theme should be discarded
or otherwise they should be combined.
The validity of the independence assumption is also exam-
ined by applying an Overall Test of Conditional Independence (see
Bonham-Carter, 1994). The number of predicted points is the
product of area and posterior probability added over each
unique condition. The test is a ratio calculated by dividing the
actual number of training points input to the model by the
predicted number of points (Kemp et al., 1999). This value will
always be between 0 and 1. A value of 1 (which never occurs in
practice) indicates conditional independence among the evi-
dence themes used in the model (Kemp et al., 1999). Values
much smaller than 1 indicate a violation of the conditional
independence assumption.
3.5.
Combining the evidential themes to create a
posterior probability theme
The weighted evidence maps are combined to create a
response theme or a ﬁnal predictive map, expressed in poste-
rior probabilities. This is generated by combining the Weights-
of-Evidence of signiﬁcant statistically maps. The resulting
predictive map is classiﬁed into four predictive categories as
described bellow (Carranza and Hale, 1999, 2000):
1. High predictive: when the ratio of the posterior probability to
prior probability is above 5 and the “Studentized” posterior
probability (posterior probability/Total) is more than 1.5.
2. Moderate predictive: when the ratio ranges from 1 to
5 and the “Studentized” posterior probability (posterior
probability/Total) is more than 1.5.
3. Low predictive: when the ratio is less than 1 and the “Stu-
dentized” posterior probability (posterior probability/Total)
is more than 1.5.
4. High uncertainty: no prediction possible, because the “Stu-
dentized” posterior probability (posterior probability/Total)
is less than 1.5, indicating too much uncertainty (Bonham-
Carter et al., 1989).
3.6.
Model evaluation
The model evaluation is an important step in modelling
and, ideally, models should be tested with independent data
(Fielding and Bell, 1997; Guisan and Zimmermann, 2000).
There are several measures for assessing model perfor-
mance, several authors (Fielding and Bell, 1997; Guisan and
Zimmermann, 2000; Hastie et al., 2001) agreed on two conven-
tional ways for model validation: (i) the ﬁrst approach is to
use a single data set to calibrate the model and then evaluate
it by k-fold cross-validation, leave-one-out Jack-Knife, or bootstrap
methods; (ii) the second approach is to use two independent
data sets, one for calibrating and another for evaluating the
model. When both data sets result from the splitting of an
originally single data set, it is called the split-sample approach.
The most promising method for model validation may be the
use of holdout sample to check the model and its predictive
ability (Hooten et al., 2003).
We use split-sample approach to evaluate the predictive
model of woodpecker. The 36 woodpecker pairs observed were
divided into two subsets of points drawn at random. One sub-
set of 75% of the observed woodpecker pairs was used to
develop the model. The other subset of 25% of the observed
woodpecker pairs was used to evaluate the predictive model
and therefore considered as a group of “control” or “undiscov-
ered” occurrencies; these centroids were selected randomly
from the total amount of points in the dataset. For a more
convincing evaluation, we assume that this test set of “control
occurrences” is useful for determining if the predictive map is
able to identify them.
4.
Results
WofE
model
was
proven
suitable
to
generate
spatial
habitat–species occurrence relationships. It constitutes an
effective tool that combines spatial data to describe and anal-
yse interactions while providing support for decisions makers.
The habitat characterization and forest structure thresholds
obtained from an indicator species provided helpful infor-
mation to improve forest management practices in order to
restore and maintain forest biodiversity.
Table 1 shows the spatial associations between the dif-
ferent environmental layers used and the mapped wood-
pecker pairs observed. The ﬁnal result is a predictive map of
favourable areas or habitat quality for woodpecker based on
the appropriate quantiﬁed spatial associations.
4.1.
Calculating weights for each predictive map
WofE depicts the statistically calculating measures (W+, W−,
C and CS) of the spatial association between the occurrences
for each predictive map. These statistical values are useful to
analyse and understand the particular habitat characteristics
of the Woodpecker nesting areas in the study region.
All the high CS values for the volume (m3/ha) of spruce
are between 121 and 200 m3/ha, and mainly in the group of
161–200 m3/ha (Table 3 and Fig. 3). The  of the C within this
group is one of the lowest overall, implying that the spatial
association with presence of Woodpecker is statistically sig-
niﬁcant at this volume (˛ = 0.05). The high CS indicates that
the spatial association is most signiﬁcant statistically and C
is less uncertain for a volume of 161–200 m3/ha. The weights
(W−and W+) of the favourable range are between 1 and 2, indi-
cating highly predictive values. Further, W+ and C are negative
and W−is positive at lower volumes (between 0 and 60 m3/ha).
This implies that, at locations in this range, fewer woodpecker
occurrences are present than would be expected by chance.
It also implies a negative spatial association between wood-


ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
69
Table 3 – Summary of weights, contrast and Studentized C for volume (m3/ha) of spruce
Map Class
W+
(W+)
W−
(W−)
C
(C)
CS
0
0
0
0
0
0
0
0
0–20
−0.95
0.58
0.22
0.21
−1.17
0.62
−1.90
21–40
−0.34
0.58
0.05
0.21
−0.39
0.62
−0.63
41–60
−0.37
0.71
0.04
0.20
−0.40
0.74
−0.54
61–80
0
0
0
0
0
0
0
81–120
0
0
0
0
0
0
0
121–160
1.35
0.37
−0.27
0.23
1.62
0.44
3.69
161–200
1.76
0.38
−0.30
0.23
2.06
0.45
4.59
201–240
0.88
0.73
−0.05
0.20
0.93
0.76
1.22
>240
0.97
1.04
−0.02
0.20
0.99
1.06
0.94
Fig. 3 – Generalization of spruce volume (m3/ha), based on the Studentized C value.
pecker occurrence and a class or group of classes within an
evidence theme.
For spruce data, the presence (W+ = 1.35 and 1.76) of a high
volume of spruce has much more inﬂuence than its absence
(W−= −0.27 and −0.29). However, for the broad leaf, there is
about the same contribution to C from the presence (W−) as
from the absence (W+). This denotes a relatively moderate pre-
dictive value of the variable, probably due to the low volumes
of broad leaf existing in the region under study. While the vol-
ume of spruce is a clear indicator of woodpecker presence.
In relation to stand age, the values of CS become positive for
forest stand ages greater than 60 years old (Table 4 and Fig. 4).
However, the statistically signiﬁcant groups (˛ = 0.05) are found
from 81 to 120 years old. The weights of the favourable age
range are above 1, which is a highly predictive value. The rel-
ative size of the weights shows that the presence (W−) of old
forest (81–100 years old) has much more inﬂuence than its
absence W+. This suggests that the woodpeckers prefer old
growth forests as nest sites, probably due to the amount of
dead wood present in them.
Distance-buffers from Waterbodies show signiﬁcant values
up to 100 m. The presence of woodpecker nesting sites around
rivers, lakes and other water bodies is found up to 400 m, but
the optimum buffer threshold is at 100 m. In this ﬁrst group,
Table 4 – Summary of weights, contrast and Studentized C for stand age (years)
Map class
W+
(W+)
W−
(W−)
C
(C)
CS
1–20
0
0
0
0
0
0
0
21–40
−2.04
1.00
0.30
0.20
−2.34
1.02
−2.29
41–60
−0.40
0.45
0.12
0.22
−0.52
0.50
−1.03
61–80
0.37
0.31
−0.19
0.25
0.57
0.40
1.43
81–100
1.24
0.35
−0.30
0.24
1.54
0.42
3.64
101–120
2.26
1.14
−0.03
0.20
2.29
1.15
1.99
121–140
0
0
0
0
0
0
0
>140
0
0
0
0
0
0
0


70
ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
Fig. 4 – Generalization of stand age (years) based on the Studentized C value.
the presence of W+ at small distances to water has much more
inﬂuence than the absence of W−. The trend is reversed from
distances over 400 m. In this second group, the presence (W−)
at small distances to water has much less inﬂuence than the
absence (W+). These values suggest that the woodpeckers have
a high dependence on access and availability of water.
Distance to urban areas analysis shows that woodpecker
prefers to nest in areas with certain distance from built-up
and urban areas. The high values of the CS conﬁrm this. The
class above 900 m distance shows that the presence (W+ = 1.24)
has much more inﬂuence in the contrast than the absence
(W−= −0.63) of nesting sites; while at a shorter distance the
trend is reversed.
Bonham-Carter et al. (1989) indicated that if CS is greater
than 1.96 the value of C is statistically signiﬁcant (at the ˛ = 0.05
level), and indicates poor conﬁdence in the signiﬁcance of the
contrast. In this particular study CS values less than 1.96 were
found for pine, Betula and distance from road maps. In the
case of pine forest, results conﬁrm the low biodiversity value
of the young and dense homogeneous managed forest stands.
The problem with Betula as explained is the low volumes in
the region. While in the case of distance to roads became clear
that a closer distance to the variable constitutes a negative
factor for the species. Methodologically it is important to note
how the method allows rejecting from the modelling process
these layers at an earlier stage. But as seen in this case a good
understanding of the variables and its causes for rejection in
the model are needed.
4.2.
Testing the conditional independence assumption
The statistical validity of the resulting predictive maps is
examined by considering a contingency table based on all
pairs of maps, using a chi-squared test. In our case, the null
hypothesis of the conditional independence is not rejected
at the 95% signiﬁcance level for any of the six pairs of maps
(Table 5).
The result of Overall Test of Conditional Independence was
0.96.
Thus, Pairwise Conditional Independence Test and Overall
Test of Conditional Independence tests suggest that the pre-
dictive maps are statistically valid.
4.3.
Combining the evidential themes to create a
posterior probability theme
Based on the results shown in Table 6, we can have a high
degree of statistical conﬁdence in all six evidence maps. We
Table 5 – Probability values for testing pairwise conditional independence
Broad leaf
Potential
productivity of the
site (m3/ha/year)
Stand age (years)
Water
Urban areas
Spruce
0.93; 2 = 0.15, d.f. = 2
0.57; 2 = 1.11, d.f. = 2
0.30; 2 = 4.91, d.f. = 4
0.65; 2 = 0.88, d.f. = 2
0.80; 2 = 1.64, d.f. = 4
Broad leaf
0.89; 2 = 0.02, d.f. = 1
0.38; 2 = 1.92, d.f. = 2
0.40; 2 = 0.71, d.f. = 1
0.53; 2 = 1.28, d.f. = 2
Potential productivity
of the site
(m3/ha/year)
0.77; 2 = 0.53, d.f. = 2
0.72; 2 = 0.13, d.f. = 1
0.88; 2 = 0.26, d.f. = 2
Stand age (years)
0.93; 2 = 0.15, d.f. = 2
0.91; 2 = 1.01, d.f. = 4
Water
0.74; 2 = 0.60, d.f. = 2
Probability values >0.05 indicate conditional independence.


ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
71
Table 6 – Summary of Weights-of-Evidence statistics for combining the evidential maps
Evidential themes
Classes of evidential maps grouping
W0
W1
W2
W3
Contrast
Conﬁdence
Spruce (m3/ha)
−0.76
1.35
1.76
2.53
5.15
Broad leaf (m3/ha)
−0.48
0.56
1.04
2.62
Potential productivity of the site (m3/ha/year)
−0.80
0.96
1.76
4.23
Stand age (years)
−0.36
2.26
1.24
2.62
2.25
Water
−1.84
0.23
2.07
2.02
Urban areas
1.24
0.25
−1.10
2.34
4.76
See Section 3.2 for explanation of W0–W3.
generalized the six evidence themes and calculated the Stu-
dentized C value (CS) of each class; as shown in Figs. 3 and 4.
The volume of spruce is the most important predictive vari-
able with a conﬁdence value of 5.15. High volumes of spruce
(between 120 and 200 m3/ha) seem to be a good biodiversity
indicator of valuable old growth spruce forest. Results also
show a good relationship with potential productivity of the
site within the class 5–6 m3/ha. The volume of spruce and the
surrogate for site fertility are clear indicators of old growth
spruce forest in herb rich sites mostly found in protected areas
in Finland. Stand age conﬁrm these observation showing the
majority of the woodpecker nesting areas around old growth
forest with an age between 80 and 120 years old.
We show the predictive map of preferred areas for wood-
pecker nesting habitat (Fig. 5) as the ratio of the posterior prob-
ability to prior probability. On the basis of this analysis, only
4% of the study area is considered to be highly favourable for
woodpecker nesting areas, and 2.2% has a medium value for
woodpecker nesting site favourability.
4.4.
Model evaluation
The predictive model was compared with all observed occur-
rences of woodpecker pairs (Table 7). Only 17 of the 27 (63%)
woodpecker centroids fall correctly within high favourable
areas. However, for those woodpecker occurrences that were
missed, 29% fall within 25 m of a high favourable area. While
the rest is more than 25 m away from a favourable area. In
the overall, 70% of the areas of woodpecker pairs observed
fall within in or near to a highly favourable habitat area as
identiﬁed for woodpecker. This geo-information suggests that
the predicted favourable areas are good exploration targets for
ﬁnding high quality woodpecker sites that are favourable for
nesting.
The ability and usefulness of the predictive maps to
delineate zones of unknown woodpecker pairs observed were
validated by comparing them with the “control” or “undiscov-
ered” data subsets. We determine the number of “unknown”
occurrences falling within areas of low, medium or high
Fig. 5 – Detail of predictive map of preferred areas for woodpecker nesting sites (high quality habitat in dark grey).


72
ecological modelling 1 9 6 ( 2 0 0 6 ) 62–76
Table 7 – Results from the response map for favourable habitat domain
Nesting potential areas
Known occurrences (75%)
Control occurrences (25%)
Predictive map
Buffer 25 ma
Predictive map
Buffer 25 ma
Num. (%)
Num. (%)
Num. (%)
Num. (%)
High uncertainty
9 (33.33)
8 (29.63)
5 (55.56)
1 (11.11)
Low predictive
0 (0)
0 (0)
0 (0)
0 (0)
Medium predictive
1 (3.7)
0 (0)
1 (11.11)
0 (0)
High predictive
17 (62.96)
19 (70.37)
3 (33.33)
8 (88.89)
a Centroids within 25 m buffer area of a nearest high potential areas.
potential. Three of the nine centroids fall correctly within
high favourable areas. While the rest of centroids (89%) falls
less than a pixel (25 m) away from the nearest high favourable
area. We adopted a conservative attitude, according to
Carranza and Hale (2000), and we consider the usefulness of
the predictive map if it succeed on identifying at least 70% of
the occurrences that were necessary to develop the map and
at least 50% of the “undiscovered” occurrences. Our results in
Table 7 suggest that the predictions of the model are valid.
5.
Discussion
The habitat suitability model developed for woodpecker is
determined by several environmental variables as well as vari-
ables related to human pressures. Then certain factors acts as
pressures affecting negatively woodpecker nesting areas.
Overall, the population is cluster around the best quality
areas in terms of resources and forest structural characteris-
tics (Fig. 2 and see also Luque et al., 2006). These areas are
in general under a certain protection status. Also areas found
with a high predictive value were located at distances further
than 50 m from roads and at more than 600 m away from any
populated centre. These ﬁndings are in conformity with grow-
ing evidence that roads built-up and other human activities
negatively impacts on woodpeckers. Despite the preference
for areas close to water bodies, showed by the results, dis-
tance to water is not considered a good indicator to predict the
presence of woodpecker because of the low conﬁdence value
of 2.02. Still the relation to water bodies may be an indirect
effect of the presence of beaver that produces high volumes
of dead wood. Three toed woodpeckers feed mainly on dead
conifers (mostly spruce), and they can found their main prey
items (bark beetles, bark beetle larvae and other insects) read-
ily available in beaver habitats.
It has been shown that the presence of old-growth forest
(>80 years old) is one of the most important variables in the
distribution of woodpecker nesting areas. In particular, sig-
niﬁcant high volumes typical of old forest stands were found
for dominant spruce forest (121–200 m3/ha). Our results are in
accordance to Imbeau and Desrochers (2002), who indicated
that in managed forests, the number of three-toed woodpeck-
ers is directly related to the area of residual old-growth forest
shreds retained. Results of this study show as well that high
quality areas for three-toed woodpeckers have also high val-
ues of site productivity for Finland. Potential productivity of
the site map, used here as a surrogate for quality of the site,
show as the most favourable sites for woodpecker nesting
area, the ones with 5.1–6 m3/ha/year. These values are consid-
ered as a typical indicator value of fertile herb rich old growth
forest (W+ = 0.83).
Changes found in forest structure in the area are mostly
due to forest management for timber production (Luque et al.,
2006; V¨ais¨anen et al., 1996; Linder and Ostlund, 1998). Forest
management produces a constant dynamics due to continu-
ous cuttings and growth. Old forests areas are quite dissected
within the landscape mosaic as shown by the small average
patch size (0.6–0.2 ha) in relation to the number of patches
for more than 80 years old forests. While old growth forest is
fragmented, younger forest patches (61–80 years old) show an
evident cohesion (Fig. 6). Regrettably the new forest structure
of young, dense forest stands with low or no dead wood is not
suitable for the maintenance of the indicator species studied.
As a primary cavity excavator and as habitat specialist,
the woodpecker has preference for a large diameter trees
as nesting sites. When the nesting sites are abandoned it
provides cover and breeding opportunities for a variety of
other species. Then the preference for mature, often mixed or
conifer-dominated forest (spruce and pine), is related as well
with high volumes of dead wood (Fayt, 1999; Pakkala et al.,
2002; Jumppanen et al., 2003). In Lammi study area, we found
that remnants of old growth forest protected areas are key
to the maintenance of the population of woodpecker within
the managed forest mosaic. We believe then that, in heavy
managed forests like in Finland, larger patches of old growth
forests need to be protected in order to reach reasonable levels
for the maintenance of biodiversity.
Fig. 6 – Number of patches and mean patch size by stand
age.


ecological modelling
1 9 6
( 2 0 0 6 ) 62–76
73
5.1.
Advantages of the Bayesian approach
The main advantages we see in the use of WofE for ecolog-
ical applications is that it combines spatial data to describe
and analyse interactions at the same time that it provides
support for decisions makers and makes possible to develop
predictive models. In all, WofE is an effective tool for identi-
fying, understanding and quantifying relationships between
features as occurrences and evidential themes. WofE allows a
rapid identiﬁcation of possible causal relationships between
species distribution and environmental data. The method is
objective, especially in the choice of weighting factors. And
such weights are more easily interpreted than regression coef-
ﬁcients (e.g. multiple regression analysis) (Bonham-Carter et
al., 1988).
Despite of its multiple advantages, as other data-driven
methods it is advisable to apply the method only in regions
where the response variables are fairly well known. Based
on our experience, we found WofE model not suitable for
applications in poorly known regions with only a small
number of known occurrences, if this is the case then results
must be interpreted with caution. This problem is common
with all models using predictor variables derived from GIS
layers (Gibson et al., 2004), because the input layers are
constrained by the availability data that approximate the
ecological requirements of the study species (Osborne et al.,
2001; Austin, 2002). Despite this limitation it could be used
as well to identify potentially new areas that could subse-
quently be sampled in order to improve the datasets in target
areas.
The usefulness of the method is also in applications
for relatively large regions, examples exist that showed a
good effectiveness in the study of species distribution at
the landscape level (Jaberg and Guisan, 2001; Osborne et al.,
2001). Predictive success can be improved by the inclusion
of more detailed data (Osborne et al., 2001; Gibson et al.,
2004) or by the use of a multiscale approach (i.e. landscape
and on ground variables) to habitat modelling (Hay et al.,
2002).
6.
Conclusion
We assumed that certain environmental characteristics and
given vegetation are correlated with high probabilities of pres-
ence of woodpecker nesting areas. Based on this assumption,
we explored this postulate as a measure of habitat suitability.
From a landscape scale perspective, our analysis successfully
predicted the occurrence of woodpecker at the municipality
level of Lammi Area (Finland) from a smaller sampled area
where species census data existed (68% of the total study
area). This is another comparative advantage of the method
since nowadays biodiversity inventories, cartography, distri-
bution modelling, habitat quality assessment, etc., are limited
by time and money. In this sense most, if not all, modelling
inevitably has to be based on data collected from the ﬁeld.
The other problem is that good models and in particular good
forecasting models are dependent on good quality data. Given
the expense of undertaking data collection, many data sets
are collected over small areas. We found then, that the use
of existing good quality ﬁeld data when combined with spa-
tial analysis and georeferenced species indicator data can be
turned into a powerful tool for monitoring biodiversity for
larger areas than the original sample size. Thus, the proba-
bility maps of Woodpeckers presence can be used to identify
other suitable sites were bird distribution is unknown. Also,
this model can be used to predict the likely effects of future
changes in land use (Rushton et al., 2000; Smart et al., 2000).
Furthermore, the tools developed can be applied in assessing
biodiversity value of both managed and protected forest areas
to help decision-making concerning the protection of valuable
habitats.
Results have important implications for forest managers,
planners and ecological researchers. Not only because we
focus on boreal forest landscapes, but also because of the use
of a valuable existing database (i.e. National Forest Inventory)
that is available to many other countries. Our analysis shows
relationships between breeding bird’s distribution and some
coarse predictors easily derived from forest Inventories. The
WofE model developed generated reasonable accurate predic-
tions providing then a good tool not only to analyse habitat
characteristics of the species but also to use these charac-
teristics to explain distribution patterns of bird populations
nesting areas.
We adopted a conservative attitude in our model and ruled
out all evidence maps statistically insigniﬁcant. We conﬁrmed,
as supported by Carranza and Hale (2000), that using only evi-
dence patterns whose spatial association with occurrences are
statistically signiﬁcant tends to produce a probabilistic map
with higher predictive strength.
The ﬁnal product is a predictive map that shows the loca-
tions of known woodpecker pairs observed, as well as new
target areas of suitable habitat. For management purposes,
maps of Natural Protected Areas could be overlaid by maps of
predicted ﬁne scale distributions in order to assess the level
of protection that is needed for a particular species based on
site and habitat characteristics (Cowley et al., 2000).
We stress then the beneﬁts to develop WofE models from
National Forest Inventory data and species distribution infor-
mation in order to identify potentially suitable habitats of
key species at regional scales. We also encourage the use
of this method to evaluate biodiversity value at the regional
level.
Acknowledgements
We are grateful to Timo Pakkala and the Finnish Museum
of Natural History for providing the three-toed woodpecker,
census data. As well we thank T. Pakkala for sharing his expe-
rience in the ﬁeld with us. Support for this work has been
provided in part by Academy of Finland, National Technol-
ogy Agency in Finland and Finnish Forest Industries Feder-
ation. We also thank George Perry and James Millington for
their valuable comments and editing of an earlier draft of
the paper. Two anonymous reviewers provided valuable com-
ments that helped improve the paper. The Regional Govern-
ment of Madrid (Spain) granted a Postdoctoral Fellowship to
R. Romero-Calcerrada to carry out this research.


74
ecological modelling
1 9 6
( 2 0 0 6 ) 62–76
r e f e r e n c e s
Ahti, T., H¨amet-Ahti, L., Jalas, J., 1968. Vegetation zones and
their sections in northwestern Europe. Ann. Bot. Fenn. 5,
169–211.
Agterberg, F.P., Bonham-Carter, G.F., Wright, D.F., 1990.
Statistical pattern integration for mineral exploration. In:
Gaal, G., Merriam, D.F. (Eds.), Computer Applications in
Resource Estimation: Prediction and Assessment for Metals
and Petroleum. Pergamon Press, Oxford, pp. 1–21.
An, P., Moon, W.M., Bonham-Carter, G.F., 1992. On
Knowledge-based Approach Of Integrating Remote Sensing,
Geophysical And Geological Information. In: Geoscience and
Remote Sensing Symposium, IGARSS’92 International, pp.
34–38.
Asadi, H.H., Hale, M., 1999. A predictive GIS model for potential
mapping of gold and base metal mineralization in Takab
area, Iran. In: Diaz, J., Tynes, R., Caldwell, D., Ehlen, J. (Eds.),
Fourth International Conference on GeoComputation Mary
Washington College Fredericksburg. GeoComputation
CD-ROM, Virginia, USA, p. 14.
Asadi, H.H., Hale, M., 2001. A predictive GIS model for mapping
potential gold and base metal mineralization in Takab area,
Iran. Comput. Geosci. 27, 901–912.
Aspinall, R., 1992. An inductive modelling procedure based on
Bayes’ theorem for analysis of pattern in spatial data. Int. J.
Geogr. Inf. Syst. 6, 105–121.
Aspinall, R., Veitch, N., 1993. Habitat mapping from satellite
imagery and wildlife survey data using a Bayesian modeling
procedure in a GIS. Photogramm. Eng. Remote Sens. 59,
537–543.
Austin, M.P., 2002. Spatial prediction of species distribution: an
interface between ecological theory and statistical
modelling. Ecol. Modell. 157, 101–118.
BirdLife International, 2005. Species factsheet: Picoides tridactylus.
Downloaded from http://www.birdlife.org on 9/20/2005.
Bonham-Carter, G.F., 1994. Geographic Information Systems for
Geoscientists, Modelling with GIS. Computer Methods in
Geosceinces, vol. 13. Pergamon, Tarrytwon, New York, 398
pp.
Bonham-Carter, G.F., Agterberg, F.P., 1999. Arc-WofE: A GIS Tool
for Statistical Integration of Mineral Exploration Datasets.
The 52 Session of the International Statistical Institute.
Bulletin of the International Statistical Institute, Helsinki,
Finland, p. 4.
Bonham-Carter, G.F., Agterberg, F.P., Wright, D.F., 1988.
Integration of geological datasets for gold explotation in
Nova Scotia. Photogramm. Eng. Remote Sens. 54, 1585–1592.
Bonham-Carter, G.F., Agterberg, F.P., Wright, D.F., 1989. Weights
of evidence modelling: a new approach to mapping mineral
potential. In: Agterberg, F.P., Bonham-Carter, G.F. (Eds.),
Statistical Applications in the Earth Science. Geological
Survey of Canada, pp. 171–183.
Carranza, E.J.M., Hale, M., 1999. Geologically-constrained
probabilistic mapping of gold potential, Baguio District,
Philippines. In: Diaz, J., Tynes, R., Caldwell, D., Ehlen, J.
(Eds.), Fourth International Conference on GeoComputation
Mary Washington College Fredericksburg. GeoComputation
CD-ROM, Virginia, USA, p. 14.
Carranza, E.J.M., Hale, M., 2000. Geologically constrained
probabilistic mapping of gold potential, Baguio District,
Philippines. Nat. Resour. Res. 9, 237–253.
Carranza, E.J.M., Hale, M., 2002. Where are porphyry copper
deposits spatially localized? A case study in Benguet
Province, Philippines. Nat. Resour. Res. 11, 45–59.
Cowley, M.J.R., Wilson, R.J., Leon-Cortes, J.L., Gutierrez, D.,
Bulman, C.R., Thomas, C.D., 2000. Habitat-based statistical
models for predicting the spatial distribution of butterﬂies
and day-ﬂying moths in a fragmented landscape. J. Appl.
Ecol. 37, 60–72.
Derleth, P., B ¨utler, R., Schlaepfer, R., 2000. Le Pic tridactyle
(Picoides tridactylus): un indicateur de la qualit´e ´ecologicue
de l’´ecosyst`eme forestier du Pays-d’Enhaut (Pr´ealpes
suisses). Schweizerische Z. Forstwesen 151, 282–289.
Dixon, P., Ellison, A.M., 1996. Introduction: ecological
applications of Bayesian inference. Ecol. Appl. 6, 1034–1035.
Duffy, S.B., Corson, M.S., Grant, W.E., 2001. Simulating land-use
decisions in the La Amistad biosphere reserve buffer zone
in Costa Rica and Panama. Ecol. Modell. 140, 9–29.
Ellison, A.M., 2004. Bayesian inference in ecology. Ecol. Lett. 7,
509–520.
Essen, P.A., Ehnstr¨om, B., Ericson, L., Sj¨oberg, K., 1997. Boreal
forests. Ecol. Bull. 46, 16–47.
Fayt, P., 1999. Available insect prey in bark patches selected by
the three-toed Woodpecker Picoides tridactylus prior to
reproduction. Ornis Fenn. 76, 135–140.
Fielding, A.H., Bell, J.F., 1997. A review of methods for the
assessment of prediction errors in conservation
presence/absence models. Environ. Conserv. 24, 38–49.
Finnish Environmental Institute, University of
Helsinki/Department of Biological Sciences, Finnish Forest
Research Institute, MTT Agrifood Research Finland, 2005.
Evaluation of the Finnish National Action Plan 1997–2005
for Biodiversity. Downloaded from
http://www.ymparisto.ﬁ/default.asp?node=8410&lan=en on
10/2005.
Gibson, L.A., Wilson, B.A., Cahill, D.M., Hill, J., 2004. Spatial
prediction of rufous bristlebird habitat in a coastal
heathland: a GIS-based approach. J. Appl. Ecol. 41, 213–
223.
Goodacre, A.K., Bonham-Carter, G.F., Agterberg, F.P., Wright,
D.F., 1993. A statistical analysis of the spatial association of
seismicity with drainage patterns and magnetic anomalies
in western Quebec. Tectonophysics 217, 285–305.
Guisan, A., Zimmermann, N.E., 2000. Predictive habitat
distribution models in ecology. Ecol. Modell. 135, 147–186.
Gutzwiller, K.J., 2002. Applying landscape ecology in biological
conservation. Springer, New York, 518 pp.
Harris, D.A., Pan, R., 1999. Mineral favorability mapping: a
comparison of artiﬁcial neural networks, logistic regression,
and discriminant analysis. Nat. Resour. Res. 8, 93–109.
Harris, J.R., Wilkinson, L., Grunsky, E.C., 2000. Effective use and
interpretation of lithogeochemical data in regional mineral
exploration programs: application of Geographic Information
Systems (GIS) technology. Ore Geol. Rev. 16, 107–143.
Harris, J.R., Wilkinson, L., Heather, K., Fumerton, S., Bernier,
M.A., Ayer, J., Dahn, R., 2001. Application of GIS processing
techniques for producing mineral prospectivity maps—a
case study: mesothermal Au in the Swayze Greenstone Belt,
Ontario, Canada. Nat. Resour. Res. 10, 91–124.
Hastie, T., Tibshirani, R., Friedman, J., 2001. The Elements of
Statistical Learning: Data Mining, Inference, and Prediction.
Springer Series in Statistics. Springer-Verlag, New York, 533
pp.
Hay, G.J., Dub´e, P., Bouchard, A., Marceau, D.J., 2002. A
scale-space primer for exploring and quantifying complex
landscapes. Ecol. Modell. 153, 27–49.
Hilborn, R., Mangel, M., 1997. The Ecological Detective:
Confronting Models with Data. Princeton University Press,
Princeton, NJ.
Hooten, M.B., Larsen, D.R., Wikle, C.K., 2003. Predicting the
spatial distribution of ground ﬂora on large domains using a
hierarchical Bayesian model. Landsc. Ecol. 18, 487–502.
Imbeau, L., Desrochers, A., 2002. Area sensitivity and edge
avoidance: the case of the three-toed Woodpecker (Picoides
tridactylus) in a managed forest. Forest Ecol. Manage. 164,
249–256.


ecological modelling
1 9 6
( 2 0 0 6 ) 62–76
75
Jaberg, C., Guisan, A., 2001. Modelling the distribution of bats
in relation to landscape structure in a temperate mountain
environment. J. Appl. Ecol. 38, 1169–1181.
Jerina, K., Debeljak, M., Dzeroski, S., Kobler, A., Adamic, M.,
2003. Modeling the brown bear population in Slovenia: a
tool in the conservation management of a threatened
species. Ecol. Modell. 170, 453–469.
Jumppanen, J., Kurttila, M., Pukkala, T., Uuttera, J., 2003. Spatial
harvest scheduling approach for areas involving multiple
ownership. Forest Pol. Econ. 5, 27–38.
Kemp, L.D., Bonham-Carter, G.F. and Raines, G.L., 1999. WofE:
Arcview extension for weights of evidence mapping.
http://ntserv.gis.nrcan.gc.ca/wofe.
Kemp, L.D., Bonham-Carter, G.F., Raines, G.L. and Looney, C.G.,
2001. Arc-SDM: Arcview extension for spatial data modelling
using weights of evidence, logistic regression, fuzzy logic
and neuronal networks analysis.
http://ntserv.gis.nrcan.gc.ca/sdm/.
Kouki, J., 1994. Biodiversity in the Fennoscandian boreal forests:
natural variation and its management. Ann. Zool. Fenn. 31,
1–217.
Kouki, J., Niemel¨a, P., 1997. The biological heritage of Finnish
forests. In: Opas, L.L. (Ed.), Finnish Forests. University of
Joensuu, Joensuu, pp. 13–33.
Kouki, J., L¨ofman, S., 1998. Forest fragmentation: processes,
concepts and implications for especies. In: Dover, J.W.,
Bunce, R.G.H. (Eds.), Key Concepts of Landscape Ecology.
IALE (UK), Preston, pp. 187–203.
Larson, M.A., Thompson III, F.R., Millspaugh, J.J., Dijak, W.D.,
Shiﬂey, S.R., 2004. Linking population viability, habitat
suitability, and landscape simulation models for
conservation planning. Ecol.l Modell. 180, 103–
118.
Linder, P., Ostlund, L., 1998. Structural changes in three
mid-boreal Swedish forest landscapes, 1885–1996. Biol.
Conserv. 85, 9–19.
Luque, S., Joenssu, J.J., Romero-Calcerrada R., Tomppo, E., 2006.
Changes in the Finnish forest landscape: a multicriteria
biodiversity assessment approach. Landsc. Urban Plann., in
press (Special Issue on Biodiversity Indicators).
Luque, S., Riutta, T., Joensuu, J., Rautj¨arvi, N., Tomppo, E.,
2004a. Multi-source forest inventory data for biodiversity
monitoring and planning at the forest landscape level. In:
Marchetti, M. (Ed.), Monitoring and Indicators of Forest
Biodiversity in Europe—From Ideas to Operationality. EFI,
IUFRO, pp. 430–444.
Luque, S., Riutta, T., Joensuu, J., Tomppo, E., 2004b. Spatial
analysis and remote sensing for biodiversity monitoring and
planning at the forest landscape level. In: Actes
Hermes-science CASSINI’04, 7`eme Conference GDR SIGMA,
G´eomatique et Analyse Spatiale, pp. 149–155.
L¨ofman, S., Kouki, J., 2001. Fifty years of landscape
transformation in managed forests of southern Finland.
Scand. J. For. Res. 16, 44–53.
Miller, K.R., Lanou, S.M., 1995. National biodiversity planning:
guidelines based on early experiences around the world. In:
World Resources Institute; United Nations Environment
Programme; World Conservation Union, Washington, USA;
Nairobi; Gland, Switzerland.
Milne, B.T., Johnston, K.M., Forman, R.T.T., 1989.
Scale-dependent proximity of wildlife habitat in a
spatially-neutral Bayesian model. Landsc. Ecol. 2, 101–110.
Ministry of Environment, 1992. Uhanalaisten el¨ainten ja
kasvien seurantatoimikunnan mietint¨o—Bet¨ankande av
komissionen f¨or ¨overvakning av hotade djur och v¨axter
(Report on the monitoring of threatened animals and plants
in Finland). Komiteanmietint¨o—Commitee Report 1991:
3019.2.1992. Ymp¨arist¨oministeri¨o—Helsinki (In Finnish with
Swedish and English summaries).
Ministry of Environment, 1999. Metsien suojelupinta-alat.
Suojelupinta-alaprojektin raportti.
Ymp¨arist¨oministeri¨o—Helsinki. 43 pp. (In Finnish).
Nuutinen, T., Anola-Pukkila, A., Haara, A., K¨arkk¨ainen, L.,
Lempinen, R., Muinoven, E., Redsven, V., Hirvel¨a, H.,
H¨ark¨onen, K., Salminen, O., Siitonen, M., Teuri, M., Lappi, J.,
2001. Team report from Finnish Forest Research Institute,
MELA Team. In: Nordic Trends in Forest Inventory,
Management Planning and Modelling Proceedings of SNS
Meeting, Slovalla, Finland, April 17–19, pp. 21–28.
Osborne, P.E., Alonso, J.C., Bryant, R.G., 2001. Modelling
landscape-scale habitat use using GIS and remote sensing: a
case study with great bustards. J. Appl. Ecol. 38, 458–
471.
Pakkala, T., Hanski, I., Tomppo, E., 2002. Spatial ecology of the
three-toed Woodpecker in managed forest landscapes. Silva
Fenn. 36, 279–288.
Pechacek, P., d’Oleire-Oltmanns, W., 2004. Habitat use of the
three-toed woodpecker in central Europe during the
breeding period. Biol. Conserv. 116, 333–341.
Rautj¨arvi, N., Luque, S., Tomppo, E., 2004. Mapping spatial
patterns from National Forest Inventory data: a regional
conservation planning tool. In: GGRS Proceedings: G¨ottingen
GIS and Remote Sensing Days: Environmental Studies,
GGRS, G¨ottingen, Germany.
Romero-Calcerrada, R., 2002. Metodolog´ıa para la planiﬁcaci´on
y desarrollo sostenible en espacios naturales protegidos
europeos: las zonas de especial protecci´on para las aves.
GeoFocus (Art´ıculos), 2: 1–32. www.geo-focus.org.
Rushton, S.P., Barreto, G.W., Cormack, R.M., Macdonald, D.W.,
Fuller, R., 2000. Modelling the effects of mink and habitat
fragmentation on the water vole. J. Agric. Sci. 37, 475–490.
Skidmore, A.K., 1989. An expert system classiﬁes eucalypt
forest types using Thematic Mapper data and a digital
terrain model. Photogramm. Eng. Remote Sens. 55,
1449–1464.
Smart, S.M., Firbank, L.G., Bunce, R.G.H., Watkins, J.W., 2000.
Quantifying changes in abundance of food plants for
butterﬂy larvae and farmland birds. J. Appl. Ecol. 37,
398–414.
Soul´e, M., Sanjayan, M., 1998. Conservation targets: do they
help? Science 279, 2060–2061.
Spence, J.R., 2001. The new boreal forestry: adjusting timber
management to accommodate biodiversity. Trends Ecol.
Evol. 16 (11), 591–593.
Store, R., Kangas, J., 2001. Integrating spatial multi-criteria
evaluation and expert knowledge for GIS-based habitat
suitability modelling. Landsc. Urban Plann. 55, 79–93.
Store, R., Jokimaki, J., 2003. A GIS-based multi-scale approach
to habitat suitability modeling. Ecol. Modell. 169, 1–15.
Tomppo, E., 1991. Satellite image-based National Forest
Inventory of Finland. Int. Arch. Photogramm. Remote Sens.
28, 419–424.
Tomppo, E., 1992. Satellite image aided forest site fertility
estimation for forest income taxation purposes. Acta For.
Fenn. 229, 70.
Tomppo, E., Varjo, J., Korhonen, K., Ahola, A., Ihalainen, A.,
Heikkinen, J., Hirvel¨a, H., Mikkel¨a, H., Mikkola, E., Salminen,
S., Tuomainen, T., 1997. Country Report for Finland. In:
Study on European Forestry Information and
Communication Systems. Reports on forestry inventory and
survey systems, vol. 1. European Commission, pp. 145–226.
Tomppo, E., Henttonen, H., Korhonen, K.T., Aarnio, A., Ahola,
A., Heikkinen, J., Ihalainen, A., Mikkel¨a, H., Tonteri, T.,
Tuomainen, T., 1998. Etel¨a-Pohjanmaan mets¨akeskuksen
alueen mets¨avarat ja niiden kehitys 1968–97. Julkaisussa:
Etel¨a-Pohjanmaa. Mets¨avarat 1968–97,
hakkuumahdollisuudet 1997–2026. Mets¨atieteen
aikakauskirja—Folia Forestalia 2B/1998: 293–374.


76
ecological modelling
1 9 6
( 2 0 0 6 ) 62–76
Tomppo, E., Halme, M., 2004. Using coarse scale forest variables
as ancillary information and weighting of variables in k-NN
estimation: a genetic algorithm approach. Remote Sens.
Environ. 92, 1–20.
Tucker, K., Rushton, S.P., Sanderson, R.A., Martin, E.B., Blaiklock,
J., 1997. Modelling bird distributions—a combined GIS and
Bayesian rule-based approach. Landsc. Ecol. 12, 77–93.
V¨ais¨anen, R., J¨arvinen, O., Rauhala, P., 1996. How are extensive,
human-caused habitat alterations expressed on the scale of
local bird populations in boreal forests? Ornis Scand. 17,
282–292.
Weclaw, P., Hudson, R.J., 2004. Simulation of conservation and
management of woodland caribou. Ecol. Modell. 177, 75–
94.
Wintle, B.A., McCarthy, M.A., Volinsky, C.T., Kavanagh, R.P.,
2003. The use of Bayesian model averaging to better
represent uncertainty in ecological models. Conserv. Biol.
17, 1579–1590.
