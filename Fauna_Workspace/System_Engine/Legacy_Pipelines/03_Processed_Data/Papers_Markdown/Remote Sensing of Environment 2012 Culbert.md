--- 
source: Remote Sensing of Environment 2012 Culbert.pdf
--- 

Modeling broad-scale patterns of avian species richness across the Midwestern
United States with measures of satellite image texture
Patrick D. Culbert a,⁎, Volker C. Radeloff a, Véronique St-Louis b, Curtis H. Flather c,
Chadwick D. Rittenhouse a, Thomas P. Albright d, Anna M. Pidgeon a
a Department of Forest and Wildlife Ecology, University of Wisconsin, Madison, WI 53706, USA
b Department of Fisheries, Wildlife, and Conservation Biology, University of Minnesota, St. Paul, MN 55108, USA
c USDA, United States Forest Service, Rocky Mountain Research Station, Ft. Collins, CO 80526, USA
d Department of Geography, University of Nevada, Reno, NV 89557, USA
a b s t r a c t
a r t i c l e
i n f o
Article history:
Received 11 March 2011
Received in revised form 16 November 2011
Accepted 17 November 2011
Available online 17 December 2011
Keywords:
Biodiversity
Birds
Species richness
Habitat structure
Texture
Multiple linear regression
Landsat
NLCD
Avian biodiversity is threatened, and in order to prioritize limited conservation resources and conduct effec-
tive conservation planning a better understanding of avian species richness patterns is needed. The use of
image texture measures, as a proxy for the spatial structure of land cover and vegetation, has proven useful
in explaining patterns of avian abundance and species richness. However, prior studies that modeled habitat
with texture measures were conducted over small geographical extents and typically focused on a single
habitat type. Our goal was to evaluate the performance of texture measures over broad spatial extents and
across multiple habitat types with varying levels of vertical habitat structure. We calculated a suite of texture
measures from 114 Landsat images over a study area of 1,498,000 km2 in the Midwestern United States,
which included habitats ranging from grassland to forest. Avian species richness was modeled for several
functional guilds as a function of image texture. We subsequently compared the explanatory power of
texture-only models with models ﬁtted using landscape composition metrics derived from the National
Land Cover Dataset, as well as models ﬁtted using both texture and composition metrics. Measures of
image texture were effective in modeling spatial patterns of avian species richness in multiple habitat
types, explaining up to 51% of the variability in species richness of permanent resident birds. In comparison,
landscape composition metrics explained up to 56% of the variability in permanent resident species richness.
In the most heavily forested ecoregion, texture-measures outperformed landscape metrics, and the two types
of measurements were complementary in multivariate models. However, in two out of three ecoregions
examined, landscape composition metrics consistently performed slightly better than texture measures,
and the variance explained by the two types of measures overlapped considerably. These results show that
image texture measures derived from satellite imagery can be an important tool for modeling patterns of
avian species richness at broad spatial extents, and thus assist in conservation planning. However, texture
measures were slightly inferior to landscape composition metrics in about three-fourths of our models.
Therefore texture measures are best considered in conjunction with landscape metrics (if available) and
are best used when they show explanatory ability that is complementarity to landscape metrics.
© 2011 Elsevier Inc. All rights reserved.
1. Introduction
Avian biodiversity is under severe threat from human-caused hab-
itat loss and fragmentation (Gaston et al., 2003). The identiﬁcation of
high-value habitat is critical for maintaining avian biodiversity, given
that the resources available for habitat conservation are limited
(Turner et al., 2003). While some broad-scale mapping of biodiversity
has been conducted (Buckton & Ormerod, 2002; Myers et al., 2000),
the spatial resolution of these maps is often too coarse to be directly
relevant to resource managers and land use planners. Therefore,
alternative approaches that can provide maps of avian species rich-
ness at a ﬁner spatial resolution are needed for land management
and biogeography alike. However, surveying avian species richness
exhaustively is not feasible, and it is not clear which approaches can
best explain and predict broad-scale avian species richness patterns
while retaining a high level of detail.
Modeling and mapping of broad-scale patterns of biodiversity great-
ly beneﬁts from the use of remotely sensed data (Kerr & Ostrovsky,
2003). A major advantage of remotely sensed data over ﬁeld data is
the availability of high spatial and temporal resolution data over very
broad extents (Innes & Koch, 1998; Roy, 2003). Remote sensing-based
Remote Sensing of Environment 118 (2012) 140–150
⁎ Corresponding author at: Department of Forest and Wildlife Ecology, 226 Russell Labs,
1630 Linden Drive, Madison, WI 53706, USA. Tel.: +1 608 265 9219; fax: +1 608 262
9922.
E-mail address: pdculbert@wisc.edu (P.D. Culbert).
0034-4257/$ – see front matter © 2011 Elsevier Inc. All rights reserved.
doi:10.1016/j.rse.2011.11.004
Contents lists available at SciVerse ScienceDirect
Remote Sensing of Environment
journal homepage: www.elsevier.com/locate/rse


approaches have played a major role in many recent studies attempting
to understand and map patterns of biodiversity (Nagendra, 2001;
Turner et al., 2003). Remote sensing approaches fall into three main
categories: (1) direct mapping of individuals or assemblages of individ-
uals, (2) indirect mapping based on inference derived from models
based on habitat maps (such as landcover classiﬁcations) and observed
species distribution patterns, or (3) indirect mapping based on relation-
ships between spectral radiance information obtained from unclassiﬁed
imagery and species distribution (Nagendra, 2001).
In order to infer biodiversity patterns from remotely sensed data,
it is important to understand which environmental factors drive bio-
diversity. Three of the hypothesized primary drivers of biodiversity
are climatic stability, productivity, and habitat structure (MacArthur,
1972). Of these three, remotely-sensed measures of climate and pro-
ductivity are standardized and freely available over broad spatial ex-
tents such as PRISM (Daly et al., 2008) temperature and precipitation
data, MODIS land surface temperature data (Wan et al., 2002), AVHRR
NDVI and MODIS leaf area index data (Myneni et al., 2002, 1997),
vegetation indices (Huete et al., 2002), and net primary productivity
(Turner et al., 2006). In contrast, there are no standardized measures
of habitat structure for broad extents. For the purpose of our study,
we deﬁne habitat structure as both the vertical structure of vegetation
(such as the vertical conﬁguration of vegetation layers in a forest) as
well as horizontal vegetation structure (such as the existence of canopy
gaps in a forest).
Habitat structure inﬂuences biodiversity, particularly in birds
(Clawges et al., 2008; Luoto et al., 2004; MacArthur & MacArthur,
1961; MacArthur et al., 1966; Tews et al., 2004; Wiens, 1974;
Willson, 1974), as greater variety in habitat leads to greater variety
in species (Rosenzweig, 1995; Tews et al., 2004). Birds can ﬁnely par-
tition foraging areas (MacArthur, 1958). Thus, more structure may
support a higher number of foraging niches or support a larger food
supply (such as insects) allowing for more species (Cody, 1981).
Direct ﬁeld measurements of habitat structure, while effective in
explaining avian distribution patterns, are time consuming and im-
practical to conduct at a state-wide or regional scale (Bergen et al.,
2009), which are the very scales at which conservation planning
and land management is conducted. LiDAR (light detection and rang-
ing) technology has proven very effective at remotely measuring veg-
etation structure, especially in relation to patterns of avian abundance
and biodiversity (Bergen et al., 2009; Clawges et al., 2008; Goetz et al.,
2007; Lesak et al., 2011; Seavy et al., 2009). Unfortunately, operation-
al LiDAR sensors have only recently become widespread, and most
areas of the United States have not been imaged by LiDAR, or areas
have been imaged by different types of sensors, complicating ana-
lyses. Therefore, broad-scale studies involving measurement of habi-
tat structure by LiDAR remain impractical.
Landscape metrics derived from land cover classiﬁcations can also
serve as habitat structure measures when explaining biodiversity pat-
terns (Atauri and De Lucio, 2001; Donovan and Flather, 2002; Farina,
1997; Kondo and Nakagoshi, 2002). However, metrics are based on
land cover classiﬁcations, which remove within-class heterogeneity.
One promising alternative for characterizing habitat structure using
remotely sensed data are image texture measures derived from remote-
ly sensed imagery. Texture measures can capture both between-habitat
and within-habitat structures, providing a potential advantage over
landscape metrics.
Remotely sensed images are composed of both tone (spectral
variation) and texture (spatial variation) (Baraldi & Parmiggiani,
1995; Haralick, 1979). Texture measures quantify spatial heterogene-
ity which is valuable for both land cover classiﬁcation (Coburn &
Roberts, 2004; Franklin et al., 2000, 2001) and habitat modeling
(Estes et al., 2008; Hepinstall & Sader, 1997; Tuttle et al., 2006). One
of the most promising applications of texture measures is the charac-
terization of habitat structure, such as forest structure (Kayitakire et
al., 2006; Wunderle et al., 2007), woody plant encroachment of
savanna (Hudak & Wessman, 1998), and leaf area index (Wulder et
al., 1998).
The most commonly used measures of texture are divided into two
groups: ﬁrst-order (occurrence) and second-order (co-occurrence)
(Haralick et al., 1973). First-order measures are summary statistics,
such as mean and standard deviation, calculated from the spectral
values of pixels in a deﬁned neighborhood, typically implemented as a
moving window. Second-order texture measures take into account
the spatial distribution and dependencies of spectral values (Coburn &
Roberts, 2004). Second-order measures are derived from a gray-level
co-occurrence matrix (GLCM) (Haralick et al., 1973). The GLCM is a
symmetric n-by-n matrix, where n is the number of possible gray-
tone values. Entries Pij in the matrix, represent the relative frequency
of pixels with tone levels i and j co-occurring adjacent to one another
(Haralick et al., 1973). The GLCM is also calculated for a neighborhood,
typically a moving window. Haralick, Shanmuga, and Dinstein (1973)
originally proposed 14 texture measures derived from the GLCM. Many
of these original second-order measures have been found to be highly
correlated, and a subset of six measures is considered most useful for re-
mote sensing analysis: angular second moment (ASM), contrast, correla-
tion, homogeneity, variance, and entropy, with the ﬁrst three being the
least correlated (Baraldi & Parmiggiani, 1995; Kayitakire et al., 2006).
Broadly speaking, most second-order texture measures either mea-
sure homogeneity or heterogeneity in the digital numbers (DNs) of
pixels within a speciﬁed neighborhood (Baraldi & Parmiggiani, 1995;
Haralick et al., 1973). Measures of homogeneity include homogeneity
and angular second moment. Homogeneity is high when adjacent
pixels have similar reﬂectance DNs. Angular second moment measures
“uniformity” meaning that certain pairs of DN values occur adjacent to
one another in the image very frequently. An image where all pixels
have the same DN would have high uniformity, but so would a regular
checkerboard image as the white–black adjacency would occur very
frequently. Measures of heterogeneity include entropy, contrast, and
variance. Entropy measures disorder. The highest entropy values
occur when the GLCM is uniform, indicating a perfectly random ar-
rangement of DNs in the original image. Contrast has high values
when adjacent pixels have a very large difference in DNs. Variance mea-
sures the amount of variability in the GLCM, and is very highly correlat-
ed with ﬁrst-order variance. Correlation measures the correlation in DN
of pixel pairs. For this reason, either a very homogenous image or a very
heterogenous image could exhibit strong correlation.
The properties of different texture measures explain how they
relate to what is visible in a satellite image. A given landcover class,
e.g., a deciduous forest, will exhibit homogeneity if adjacent pixels
have similar reﬂectance values. A more heterogeneous forest may in-
clude tree species with different spectral properties, or canopy gaps
resulting in shadows which will tend to have different reﬂectance
values and texture measures capturing heterogeneity will be higher.
Textural features of course also depend on heterogeneity and homo-
geneity among landcover classes. For example, a patchwork of agri-
cultural ﬁelds planted to different crops or at different stages (e.g.,
bare soil versus mature crop) would have high within-ﬁeld homoge-
neity, but high between-ﬁeld heterogeneity. Similarly, sharp transi-
tions among different land cover classes, such as between forest and
pasture, will increase measures of heterogeneity, such as sum of
squares variance or contrast.
Given that image texture measures can characterize habitat struc-
ture (Franklin et al., 2001; Kayitakire et al., 2006), texture measures
have been used successfully to map habitat of species as varied as the
mountain bongo (an endangered antelope species) (Estes et al., 2008,
2010), the redtail monkey (Stickler & Southworth, 2008), and avian
communities. In Maine, for example, texture measures derived from
remotely sensed imagery proved useful in bird presence/absence
models (Hepinstall & Sader, 1997). In Argentina, texture measures cap-
tured meaningful variation within grasslands, improving habitat suit-
ability models for the Greater Rhea (Bellis et al., 2008). In a desert
141
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


scrub ecosystem of the Chihuahuan Desert of New Mexico, texture mea-
sures derived from Landsat imagery and 1-m resolution digital aerial
photographs explained patterns of avian species richness well (St-
Louis et al., 2009, 2006). Similarly, texture measures derived 0.5-m
resolution photographs were successful in explaining avian species
richness in prairies and savannas in western Wisconsin (Wood et al.,
2007).
These studies show the promise of texture measures for mapping
patterns of biodiversity but also present questions for further re-
search. The ecosystems where most of these studies took place (i.e.,
Grassland, desert scrub, and prairie savanna) have little vertical struc-
ture. The ability to characterize the lower strata of structurally com-
plex, closed-canopy habitats, such as forests, is a potential limitation
of texture measures derived from passive remote sensing imagery
(Estes et al., 2008; Gottschalk et al., 2005). Furthermore, most of the
studies investigating the use of image texture for biodiversity model-
ing were conducted at relatively small spatial extents (4782 km2,
Bellis et al., 2008; 250 km2, Wood et al., 2007; 2800 km2, St-Louis et
al., 2009, 2006). A study modeling avian species occurrence over
a much larger study area, i.e., the state of Maine (91,600 km2)
(Hepinstall & Sader, 1997), showed that texture was effective, but
considered only ﬁrst-order texture measures. Thus, it remains unclear
whether image texture is equally useful in explaining avian species
richness at broader spatial extents and in areas with more vertically
complex habitat structure, such as forests.
Our overall goal was to evaluate the ability of satellite image tex-
ture measures to explain avian species richness. We were speciﬁcally
interested in understanding: 1) whether measures of image texture
can explain patterns of avian species richness across broad regions
that include vertically complex habitats such as forests, and 2) if mea-
sures of image texture compare favorably with landscape composi-
tion metrics derived from land cover classiﬁcations, such as the
proportion of speciﬁc land cover classes, for modeling patterns of
avian species richness.
Our predictions were that:
1. The ability of image texture to explain patterns of species richness
over small extents will scale-up to broad extents.
2. Measures of image texture will better explain patterns of avian
species richness in habitats with simple vertical structure, such
as grasslands, than in habitats with complex vertical structure,
such as forests.
3. Measures of image texture will better explain avian species richness
patterns than landscape composition metrics, because landscape
metrics ignore within-habitat variability while texture measures
capture both between-habitat and within-habitat variability. How-
ever, these two groups of measures will be complementary in multi-
variate models.
4. Because texture measures are associated with landcover and vege-
tation, which relate to habitat type, they will hold higher explana-
tory power for habitat-based avian guilds than migratory guilds.
2. Methods
2.1. Study area
Our study area encompassed three ecoregions at the province
level (hereafter ecoregions) totaling 1,498,000 km2 of the Midwest-
ern United States: ecoregion 251 (Prairie Parkland, Temperate) and
most of ecoregions 212 (Laurentian Mixed Forest) and 222 (Eastern
Broadleaf Forest, Continental) (Bailey, 1995) (Fig. 1). The Prairie Park-
land ecoregion was historically composed of prairie alternating with
deciduous trees. Today, it is dominated by agriculture, with remnant
patches of prairie and small groves and strips of deciduous forest.
The Eastern Broadleaf Forest ecoregion is composed primarily of de-
ciduous broadleaf forests, mixed with agriculture. We included the
portion of this ecoregion from approximately the state of Michigan
and westward. (It should be noted that the Eastern Broadleaf Forest
included roughly half of our data points, thereby weighting our full-
study-area analysis to this ecoregion.) The Laurentian Mixed Forest
is in the transition area between broadleaf deciduous forest zones
and the boreal forest. The ecoregion is composed of pure stands of
deciduous trees, pure stands of conifers, and mixed stands. We
included the areas of this ecoregion in Minnesota, Wisconsin, and
Michigan, while excluding areas east of Michigan in order to maintain
a contiguous study area.
In order to quantify differences in landcover composition (and in-
ferred vertical habitat structure) between ecoregions, we calculated
the proportion of forest, agriculture, grassland, and shrubland sur-
rounding the Breeding Bird Survey routes included in our analysis
(Table 1). The Laurentian Mixed forest was dominated by forest, indi-
cating the highest level of vertical habitat structure. The Eastern
Broadleaf Forest was heavily in agriculture, but with a signiﬁcant
component in forest. The Prairie Parkland was clearly agriculture-
dominated, reﬂecting the lowest level of vertical habitat structure.
2.2. Bird data
We calculated species richness (our measure of biodiversity) from
the North American Breeding Bird Survey (BBS), an annual survey of
approximately 3000 routes across the U.S. (Fig. 1). A typical BBS sur-
vey consists of recording all birds observed or heard at 50 regularly
spaced 3-min point counts along a 39.4-km route (USGS Patuxent
Wildlife Research Center 2008). We centered our analysis on the
year 2000, calculating the mean species richness of each BBS route
from 1998 to 2002. We included only BBS routes that fall entirely
within one of the three ecoregions of study. The BBS data were pre-
processed to remove route-years collected by ﬁrst year observers, or
those carried out in suboptimal weather (e.g., high wind or rain). A
total of 586 BBS routes fulﬁlled our criteria, including 161 in Prairie
Parkland, 113 in Laurentian Mixed Forest, and 312 in Eastern Broad-
leaf Forest. Because we did not expect all bird species to respond uni-
formly to measures of textures, we calculated overall species richness
as well as richness within three migratory guilds: permanent resi-
dents, short-distance migrants (i.e., species that spend the non-
breeding season primarily in the southern portion of the U.S.), and
Neotropical migrants (Peterjohn & Sauer, 1999; Pidgeon et al., 2007;
Rappole, 1995). We also calculated species richness of avian guilds
organized by the structural form of habitat they are commonly asso-
ciated with: forest, shrubland, and grassland (Peterjohn & Sauer,
1999; Pidgeon et al., 2007).
To adjust for detection probability bias (i.e., the problem that not all
bird species are uniformly detectable at a given site), it is recommended
that a correction be applied to raw count data to adjust the species
richness estimate (Kéry & Schmid, 2004). We used the software pro-
gram COMDYN (Hines et al., 1999) to adjust our species richness esti-
mates. COMDYN considers the raw BBS route richness data from a
capture–recapture model perspective and uses a jackknife estimator
to calculate estimated species richness (Nichols et al., 1998).
2.3. Image texture data
We acquired 114 Landsat TM/ETM+ scenes (Fig. 2A) from the
LEDAPS database (Masek et al., 2006), a collection of atmospherically
corrected Landsat images based on the GeoCover dataset (Tucker et
al., 2004). We selected scenes from approximately the year 2000, to
temporally coincide with our species richness data. All images were
acquired during the growing season, however due to the extent
of study, it was not possible to obtain all images for the same phenolog-
ical stage. Therefore, some extraneous phenological variability in the
texture measures was likely present (Culbert et al., 2009). For
each image, a suite of ﬁrst- and second-order texture measures were
142
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


calculated using Matlab® R2010a (The MathWorks, 1984–2010), with
scripts adapted from St-Louis et al. (2006) (Table 2). First-order mean
and standard deviation were calculated for TM bands 1, 2, 3, 4, 5, and
7, with 5×5 and 21×21 moving windows. We also calculated second-
order angular second moment (ASM), contrast, correlation, entropy,
homogeneity (Fig. 2B), and sum of squares variance (SSVar). Among
all second-order texture measures, these six are considered the most
useful for remote sensing analyses, and angular second moment, con-
trast, and correlation are the three least correlated measures (Baraldi
& Parmiggiani, 1995; Kayitakire et al., 2006). We expected this set of
texture measures would adequately characterize vegetation structure
and therefore be an appropriate set with which to relate avian species
richness. We quantized the imagery to 64 values to limit the size of
the GLCM and avoid matrices that are too sparsely populated to provide
robust results. To determine minimum and maximum values for the
quantization, we calculated the 2.5th and 97.5th percentiles for each
band of each image. We then calculated the 2.5th and 97.5th percentile
of these values for each band across all images, and we used these
values as our minimum and maximum digital numbers (DNs) for the
quantization. Second-order textures were calculated using an omni-
directional GLCM (calculated as the mean of the four possible direction-
al GLCMs). Preliminary analysis found strong correlation between
texture measures derived from 5×5 and 21×21 window sizes, so due
to the substantial computational requirements, second-order texture
measures were calculated only with a 5×5 window and only for TM
bands 2, 3, 4, and 5. Bands 1 and 7 were excluded because we expected
band 1 results to be highly correlated with band 2, and band 7 was less
useful than other bands in prior exploratory analysis. This resulted in a
total of 48 texture measures (24 ﬁrst-order and 24 second-order)
(Table 1).
In order to relate our texture measures to individual BBS routes,
we derived 19.7 km-radius (one-half the length of a BBS route) circu-
lar buffers around the centroid of each BBS route (Albright et al.,
2010, 2011; Flather & Sauer, 1996; Rittenhouse et al., 2010). We
chose this radius because it encompasses the entire BBS route, re-
gardless of varying route path, thus resulting in a uniform area and
shape for each route. Furthermore, this distance is comparable to
the median maximum natal dispersal distance (31 km) of 76 avian
species (Sutherland et al., 2000) estimated from body size relation-
ships, and is consistent with the recommendation that landscape
effects on songbirds should be examined over tens of kilometers to
capture dispersal effects (Tittler et al., 2009). For each BBS route, we
calculated the within-buffer mean and standard deviation of each of
the 48 texture measures, yielding 96 explanatory variables total. We
calculated buffer summary statistics from a single Landsat scene
whenever possible. Of the 586 BBS route buffers, 164 did not fall
entirely within a single Landsat footprint. In those cases, the buffer
summary statistics were calculated from mosaics of adjacent Landsat
scenes.
2.4. Land cover data
We derived landscape composition metrics for each BBS route for
comparison with our texture results. Landscape metrics were calcu-
lated from the 2001 National Land-Cover Database (NLCD) (Homer
et al., 2004). Within each BBS route buffer, the relative abundance
was calculated for 13 land-cover classes: developed (NLCD 2001 clas-
ses 21, 22, 23, and 24), barren (31), deciduous forest (41), evergreen
forest (42), mixed forest (43), shrub–scrub (52), grassland (71), pas-
ture (81), cultivated crops (82), woody wetland (90), and herbaceous
wetland (95). Additionally, the total number of landcover classes pre-
sent and the Shannon diversity index (Shannon, 1948) of class distri-
bution were calculated for each buffer.
Fig. 1. Study area, including ecoregion boundaries and Breeding Bird Survey (BBS) routes.
Table 1
Landcover composition of BBS route buffers by ecoregion.
Ecoregion
Laurentian
mixed
forest
Eastern broadleaf
forest
(continental)
Prairie
parkland
(temperate)
All 3
ecoregions
combined
Proportion
forest
0.47
0.29
0.11
0.27
Proportion
agriculture
0.17
0.52
0.69
0.50
Proportion
grassland
0.03
0.02
0.08
0.04
Proportion
shrubland
0.01
0.01
0.00
0.01
Number of BBS
buffers
113
312
161
586
143
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


2.5. Statistical analysis
The Landsat image texture processing generated 96 potential
explanatory variables. Given our sample sizes (161, 113, 312, and
586), this was an unreasonably large pool of explanatory variables.
Furthermore, many texture measures are correlated (Baraldi &
Parmiggiani, 1995) and we also expected there would be correlation
between some of the bands, window sizes, and summary statistics
(mean or standard deviation). We therefore analyzed the correlation
in this variable pool in order to exclude collinear variables (|r|>0.8)
and reduce the number of variables. Additionally, we created a uni-
variate linear model for each combination of texture measure variable
(96) and avian guild (7) for a total of 672 models. We ranked the in-
dividual texture variables based on their R2 value for the “all birds”
guild (results not shown). Rankings of texture measure variables
based on performance for other guilds were similar. Correlation anal-
ysis ﬁrst focused on within-texture measure correlation. For each
texture measure (mean, standard deviation, angular second moment,
contrast, correlation, entropy, homogeneity, and sum of squares vari-
ance), correlations between bands, window sizes, or summary statis-
tics were analyzed. For variable pairs with |r|>0.8, the variable with
the lower univariate R2 ranking was dropped. After within-texture
correlations were accounted for, the remaining between-texture
correlations were then eliminated by dropping the variable with the
poorer univariate R2 rank.
The relationships between texture measures and avian species
richness were explored using multiple linear regression models.
Model selection was implemented with the step function in R (R
Development Core Team, 2009). For each guild, a candidate model
was selected using forward selection, backward selection, and bi-
directional selection starting from both the full and null models. Of
the four candidate models produced by stepwise selection, we select-
ed the model with the lowest Akaike's information criterion (AIC)
value as our best model. This analysis was carried out for the entire
study area, as well as for each ecoregion separately.
In addition to the texture-based models, we modeled avian species
richness as a function of landscape composition metrics only, in order
to have a benchmark with which to compare the performance of
Fig. 2. (A) Landsat (band 4) data for the study area. (B) Second-order homogeneity of band 4.
Table 2
Combinations of texture, window size, and Landsat TM band that were calculated for
the study area.
Order
Texture
Window size(s)
TM bands
1st
Mean
5×5, 21×21
1, 2, 3, 4, 5, 7
1st
Standard deviation
5×5, 21×21
1, 2, 3, 4, 5, 7
2nd
Angular second moment (ASM)
5×5
2, 3, 4, 5
2nd
Contrast
5×5
2, 3, 4, 5
2nd
Correlation
5×5
2, 3, 4, 5
2nd
Entropy
5×5
2, 3, 4, 5
2nd
Homogeneity
5×5
2, 3, 4, 5
2nd
Sum of squares variance (SSVar)
5×5
2, 3, 4, 5
Table 3
Texture variables calculated from Landsat imagery. Based on correlation analysis, 74
variables (marked “–”) were excluded from subsequent analysis, and 22 variables
(marked “X”) were retained.
Texture
Landsat TM band
1
2
3
4
5
7
Mean_5×5_Mean
–
–
–
–
–
–
Mean_21×21_Mean
–
X
–
X
–
–
Mean_5×5_SD
X
–
–
X
–
X
Mean_21×21_SD
X
–
–
X
–
X
SD_5×5_Mean
–
–
–
–
–
–
SD_21×21_Mean
–
–
–
–
–
–
SD_5×5_SD
X
–
–
X
X
–
SD_21×21_SD
–
–
–
–
–
–
ASM_5×5_Mean
–
–
–
–
ASM_5×5_SD
X
–
–
–
Contrast_5×5_Mean
–
–
–
–
Contrast_5×5_SD
–
–
–
–
Correlation_5×5_Mean
–
X
X
X
Correlation_5×5_SD
X
–
–
X
Entropy_5×5_Mean
–
–
–
–
Entropy_5×5_SD
–
–
–
–
Homogeneity_5×5_Mean
–
–
X
X
Homogeneity_5×5_SD
X
–
X
–
SSVariance_5×5_mean
–
X
–
–
SSVariance_5×5_SD
–
–
–
–
144
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


texture measures. Lastly, we were interested in whether texture mea-
sures were complimentary to landscape metrics, so we modeled avian
species richness as a function of both texture and landcover metrics.
3. Results
Correlation analysis of the 96 texture measure variables showed
that 441 (9.7%) of the 4560 unique combinations of variable pairs
exceeded our collinearity threshold (|r|>0.8). Once all correlations
greater than our threshold were addressed, 22 texture variables
remained (Table 3).
Over the full study area, all but the models for short-distance mi-
grant explained at least 26% of the variability of species richness with
an average adjusted R2 value of 0.30 (Table 4). The forest bird and
permanent resident models were the best (as determined by R2),
with adjusted R2 values of 0.42 and 0.40, respectively. Three of the
texture measures, standard deviation of 21×21 band 4 mean, stan-
dard deviation of 5×5 band 2 correlation, and mean of 5×5 band 5
homogeneity were included in six of the seven models.
Model performance in the Laurentian Mixed Forest showed strong
differences compared to the full study area models (Table 4). The
average model adjusted R2 was similar, at 0.24. However, the grass-
land bird model was the strongest model with an adjusted R2 value
of 0.41, while adjusted R2 values for the other six models ranged
from 0.16 (permanent residents) to 0.25 (forest birds). The perma-
nent residents model performed the worst in this ecoregion, though
it was one of the strongest models for the study area as a whole.
The forest bird model also performed more poorly in this ecoregion
(adjusted R2=0.25) than in the full study area (adjusted R2=0.42),
even though the Laurentian Mixed Forest ecoregion is the most heavi-
ly forested of the three ecoregions in our study area. The three texture
measures that were most frequently included in the models were
mean of 5×5 band 4 homogeneity (all seven models), standard devi-
ation of 21×21 band 7 mean (six models), and standard deviation of
5×5 band 2 homogeneity (six models).
The Eastern Broadleaf Forest had the models with the highest ex-
planatory power, with an average adjusted R2 value of 0.32 and top
model R2 values up to 0.46 (permanent residents) and 0.45 (forest
birds) (Table 4). Three texture variables were frequently included in
models: standard deviation of 5×5 band 5 correlation (all seven
models), standard deviation of 5×5 band 2 correlation (six models),
and standard deviation of 21×21 band 4 mean (ﬁve models).
The Prairie Parkland (Temperate) ecoregion had the strongest-
performing single model, with texture measures explaining up to 51%
of the variation in permanent resident species richness (Table 4). The
average adjusted R2 value of the seven models was 0.27. The standard
deviation of 5×5 band 2 correlation (six of seven models), standard de-
viation of 5×5 band 7 mean (ﬁve models), and mean of 5×5 band 5
correlation (ﬁve models) were frequently included in the best models.
For each ecoregion, and for the study area as a whole, the model
selection process was repeated with landscape composition metrics
derived from the NLCD as the explanatory variables. Over the entire
Table 4
Final guild species richness models as determined by stepwise selection using AIC.
Texture measure
All birds
Forest birds
Grassland birds
Shrubland
birds
Neotropical
migrants
Permanent
residents
Short-distance
migrants
Mean_21×21_B2_Mean
A
E
A
E
L
P
A
A
E
P
A
E
Mean_21×21_B4_Mean
L
A
L
A
A
E
L
A
L
E
E
Mean_5×5_B1_SD
E
A
E
A
L
Mean_5×5_B4_SD
A
E
L
P
E
P
A
E
P
E
P
Mean_5×5_B7_SD
L
P
P
A
E
P
A
L
E
P
A
E
P
A
L
Mean_21×21_B1_SD
A
A
A
E
P
Mean_21×21_B4_SD
A
E
A
E
A
L
E
P
A
E
P
A
L
E
P
A
Mean_21×21_B7_SD
L
A
L
A
L
E
P
A
L
E
P
L
A
E
A
L
P
SD_5×5_B1_SD
A
L
E
A
E
E
P
A
E
P
L
SD_5×5_B4_SD
L
E
L
A
E
E
P
L
E
P
A
E
P
SD_5×5_B5_SD
A
A
L
E
E
A
A
E
P
A
ASM_5×5_B2_SD
P
P
E
P
Corr_5×5_B3_Mean
A
A
A
P
E
P
A
A
P
Corr_5×5_B4_Mean
L
L
E
A
L
E
P
L
A
E
P
L
Corr_5×5_B5_Mean
L
E
P
P
A
P
L
P
L
E
P
L
Corr_5×5_B2_SD
A
E
P
A
E
P
L
A
E
P
A
E
P
A
E
P
A
E
P
Corr_5×5_B5_SD
A
E
A
E
E
A
E
E
A
E
A
E
Homog_5×5_B4_Mean
L
L
E
L
P
L
L
E
A
L
A
L
P
Homog_5×5_B5_Mean
A
P
A
E
P
A
A
P
A
P
A
Homog_5×5_B2_SD
L
L
A
L
E
P
L
P
L
E
L
P
Homog_5×5_B4_SD
E
P
P
SSVar_5×5_B3_Mean
E
L
E
P
A
E
A
P
L
E
P
Model adjusted R2
0.29(A)
0.42(A)
0.26(A)
0.28(A)
0.35(A)
0.40(A)
0.07(A)
0.23(L)
0.25(L)
0.41(L)
0.25(L)
0.20(L)
0.16(L)
0.19(L)
0.29(E)
0.45(E)
0.37(E)
0.33(E)
0.24(E)
0.46(E)
0.12(E)
0.19(P)
0.29(P)
0.20(P)
0.32(P)
0.15(P)
0.51(P)
0.24(P)
Number of variables/Degrees of freedom
9/576(A)
10/575(A)
10/575(A)
10/575(A)
9/576(A)
16/569(A)
8/577(A)
9/103(L)
5/107(L)
7/105(L)
8/104(L)
7/105(L)
5/107(L)
8/104(L)
8/303(E)
8/303(E)
10/301(E)
11/300(E)
11/300(E)
13/298(E)
6/305(E)
4/156(P)
4/156(P)
8/152(P)
12/148(P)
9/151(P)
12/148(P)
8/152(P)
A=All three ecoregions together, L=Laurentian mixed forest, E=Eastern broadleaf forest (continental), P=Prairie parkland (temperate).
145
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


study area, models using only landscape metrics almost always
explained more variance than models based on texture measures
(Table 5). Only in the case of permanent residents did the texture-
only model have a higher adjusted R2 value than the landscape
metric-only model. Models including both texture measures and
landscape metrics showed consistent but modest increases in adjust-
ed R2 over models including landscape metrics or texture alone, with
absolute gains of around 0.04 to 0.08.
In the Laurentian Mixed Forest, species richness models including
only texture variables were superior to landscape metric-only models
for every guild (Table 6), with texture-only models outperforming
landscape metric-only models by, on average, an absolute adjusted
R2 difference of 0.09 for a relative improvement of 34%. This was in
sharp contrast to the other ecoregions. When both texture and land-
scape variables were included in the explanatory variable pool, the
resulting models showed strong absolute and relative gains in adjust-
ed R2 values.
In the Eastern Broadleaf Forest (Continental), landscape composi-
tion metrics were superior to texture variables for explaining species
richness (Table 7), but the differences in adjusted R2 values were
small (average adjusted R2 values of 0.36 for landscape metrics-only
models compared to 0.32 for texture-only models for a 0.03 absolute
or 10% relative increase). Models including both landscape composi-
tion metric and texture variables showed modest gains, with an aver-
age absolute increase in adjusted R2 of 0.07 and an average relative
gain of 18%.
In the Prairie Parkland (Temperate), landscape metric-only models
outperformed texture-only models for ﬁve out of seven guilds
(Table 8). On average, texture-only models had an adjusted R2 of
0.27 versus 0.31 for landscape metric-only models, a difference of
0.04. Models including both texture and landscape composition
metric variables showed only marginal gains over models that in-
cluded landscape composition metrics alone, with an average abso-
lute adjusted R2 improvement of 0.04 or a relative improvement of
11%.
Lastly, due to the spatial nature of our study, we expected spatial
autocorrelation may have been present in the data. We therefore gener-
ated semivariograms of the residuals of all 48 of the ﬁnal species rich-
ness models. Inspection of the semivariograms found no evidence of
spatial autocorrelation, and thus no corrective action was necessary.
4. Discussion
We found strong evidence supporting our ﬁrst prediction that image
texture measures can explain the variability in avian species richness
over broad areas. Our results support earlier studies modeling avian
species richness in savanna (Wood et al., 2007) and desert–scrub
ecosystems (St-Louis et al., 2009, 2006), as well as studies modeling
habitat suitability for individual grassland (Bellis et al., 2008) and forest
(Hepinstall & Sader, 1997) bird species. However, our study expanded
texture analysis to a much broader spatial extent (1,498,000 km2)
than previously attempted, and we showed that image texture derived
from Landsat satellite imagery can explain variability in avian species
richness even in habitats with high levels of vertical habitat structure,
such as forests.
The broad-extent texture-only multivariate models that we devel-
oped had similar explanatory power to models developed for smaller
spatial extents (St-Louis et al., 2006; Wood et al., 2007). Our ﬁnal
multivariate models showed that measures of texture can explain up
to 51% of the variability in avian species richness, with most of our
ﬁnal models explaining 20–40% of the variability. In comparison, tex-
ture measures derived from orthophotos within a single habitat type
(savanna) yielded univariate R2 values of up to 0.54 (Wood et al.,
2007). This was a much stronger relationship than in our univariate
models (results not shown), but our multivariate models approached
this level of explanatory power. In a 2820 km2 Chihuahuan Desert land-
scape, multivariate models explained up to 62% of the variability in
avian species richness (St-Louis et al., 2006). This somewhat higher
predictive power supports the theory that habitat structure (and there-
fore texture measures) is more effective at explaining bird species
Table 5
Adjusted R2 and Akaike's information criterion (AIC) values of best models of avian species richness by guild for the models that used texture variables only, NLCD-derived land-
scape composition metrics only, and a combination of both for the entire study area. Bolded R2 and AIC values indicate the superior (texture-only or landscape metric-only) model.
Guild
Texture-only
models
Landscape metric-only
models
Texture and landscape metric
models
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Abs. R2 gain
Rel. R2 gain
All birds
0.29
2844.1
9
0.41
2738.0
6
0.45
2710.2
21
0.039
9%
Forest birds
0.42
2683.3
10
0.51
2579.7
7
0.55
2536.5
18
0.042
8%
Grassland birds
0.26
1018.1
10
0.31
971.1
8
0.39
910.4
20
0.078
25%
Shrubland birds
0.28
1001.2
10
0.31
974.0
3
0.39
913.7
19
0.077
25%
Neotropical migrants
0.35
2426.8
9
0.46
2324.9
7
0.48
2311.2
24
0.025
6%
Permanent residents
0.40
1113.3
16
0.35
1158.9
8
0.46
1058.6
18
0.055
14%
Short-distance migrants
0.07
1302.9
8
0.17
1241.6
4
0.23
1203.3
20
0.070
42%
Average
0.30
1770.0
10.3
0.36
1712.6
6.1
0.42
1663.4
20
0.055
15%
Table 6
Adjusted R2 and Akaike's information criterion (AIC) values of best models of avian species richness by guild for the models that used texture variables only, NLCD-derived land-
scape metrics only, and a combination of both for the Laurentian Mixed Forest. Bolded R2 and AIC values indicate the superior (texture-only or landscape metric-only) model.
Guild
Texture-only
models
Landscape metric-only
models
Texture and landscape metric
models
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Abs. R2 gain
Rel. R2 gain
All birds
0.23
586.7
9
0.15
592.1
3
0.31
576.4
11
0.078
35%
Forest birds
0.25
548.8
5
0.21
555.1
5
0.36
536.3
11
0.110
43%
Grassland birds
0.41
223.9
7
0.38
227.9
5
0.53
208.9
21
0.125
31%
Shrubland Birds
0.24
234.3
8
0.15
242.5
4
0.35
220.7
14
0.118
50%
Neotropical migrants
0.20
490.8
7
0.18
490.7
4
0.31
480.6
14
0.107
53%
Permanent residents
0.16
244.2
5
0.07
253.6
3
0.17
244.0
6
0.008
5%
Short-distance migrants
0.19
328.3
8
0.11
333.7
3
0.25
322.7
11
0.057
30%
Average
0.24
379.6
7
0.18
385.1
3.9
0.33
369.9
12.6
0.086
36%
146
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


richness patterns over small to medium extents than at broader extents
(Hutto, 1985).
Another potential source of the slightly higher explanatory power
of these smaller-extent studies is the ﬁner spatial resolution of imag-
ery used. These studies used 1-m (St-Louis et al., 2006) and 0.5-m
resolution imagery (Wood et al., 2007). At this resolution, individual
trees or large shrubs that have an extent of several pixels can be cap-
tured by the imagery and canopy gaps or variability in the spatial dis-
tribution of shrubs would thus be well sampled. In contrast, our 30-m
resolution imagery is too coarse for a single-tree canopy gap to be
captured in a single pixel. While small features may still be included
in the spectral information, their contribution to image texture is like-
ly weaker than with ﬁne-resolution imagery.
Modeling suitable avian habitat and biodiversity with image tex-
ture measures has been effective in habitats with little vertical struc-
ture such as grassland (Bellis et al., 2008), desert scrub (St-Louis et al.,
2009, 2006), and savanna (Wood et al., 2007). Of the three ecoregions
that we analyzed, the Prairie Parkland had the least vertical habitat
structure while the Laurentian Mixed Forest had the most. Adjusted
R2 values (Table 4) from species richness models were higher in the
Laurentian Mixed Forest for all birds, grassland birds, and Neotropical
migrants. The Prairie Parkland models had superior adjusted R2
values for forest birds, shrubland birds, permanent residents, and
short-distance migrants.
These results refute our second prediction that image texture
would perform better in ecosystems with simple vertical structure.
Models calculated for an ecoregion dominated by agriculture and
grassland performed similarly to models for a forest-dominated ecor-
egion. While satellite imagery cannot characterize the structure of
lower vegetation in forests (Gottschalk et al., 2005), if understory
structural characteristics are correlated with canopy features, then
useful information may be derived (Estes et al., 2008). It is possible
that in our study area understory vegetation features are either less
important in explaining patterns of avian species richness than cano-
py features, or that understory features are sufﬁciently correlated
with the canopy. This is an important ﬁnding, as it indicates that,
in the context of avian species richness modeling, the usefulness of
image texture measures is not limited to habitats with low vertical
habitat structure.
A signiﬁcant shortcoming of landscape metrics is that the land-
cover classiﬁcations on which landscape metrics are based do not re-
tain any information on within-class heterogeneity (Turner et al.,
2001). We therefore expected that texture measures would outper-
form landscape metrics in modeling avian species richness. In addi-
tion, we expected some complementarity; that both approaches
would characterize some unique information useful in explaining
species richness patterns.
Contrary to our third prediction, we found that across our study
area (Table 5), and also in the Eastern Broadleaf Forest (Table 7)
and the Prairie Parkland (Table 8), models of avian species richness
using landscape composition metrics were generally slightly superior
to models based on texture measures. This supports the theory that
habitat structure is more effective at explaining bird species richness
patterns over small to medium extents, and habitat type is more im-
portant at broader extents (Hutto, 1985). The notable exception was
the Laurentian Mixed Forest (Table 6), where texture models yielded
higher adjusted R2 values than landscape metric models for all seven
guilds. We speculate that this is due to the predominance of forest
in the ecoregion (Table 1), which may render within-forest structure
as particularly important in explaining patterns of avian species
richness.
Because landscape metrics ignore within-habitat heterogeneity,
while texture measures do not, our third prediction also stated that
texture measures and landscape metrics would prove complementar-
ity in their ability to explain patterns of avian species richness. For the
overall study area and for all three ecoregions, models generated
using both NLCD-derived landscape composition metrics and texture
measures yielded higher adjusted R2 values than models derived
from only landscape composition metrics or only texture measures.
The ﬁnal joint models included a relatively even mix of texture and
Table 7
Adjusted R2 and Akaike's information criterion (AIC) values of best models of avian species richness by guild for the models that used texture variables only, NLCD-derived land-
scape metrics only, and a combination of both for the Eastern Broadleaf Forest (Continental). Bolded R2 and AIC values indicate the superior (texture-only or landscape metric-only)
model.
Guild
Texture-only
models
Landscape metric-only
models
Texture and landscape metric
models
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Abs. R2 gain
Rel. R2 gain
All birds
0.29
1383.4
8
0.32
1368.3
6
0.37
1351.7
13
0.049
15%
Forest birds
0.45
1311.9
8
0.47
1296.1
7
0.53
1265.6
15
0.061
13%
Grassland birds
0.37
482.0
10
0.40
465.0
9
0.49
421.1
14
0.086
21%
Shrubland birds
0.33
450.4
11
0.39
423.3
10
0.48
383.2
21
0.092
24%
Neotropical migrants
0.24
1206.4
11
0.28
1185.2
5
0.32
1174.6
12
0.039
14%
Permanent residents
0.46
474.0
13
0.46
468.0
8
0.54
434.2
20
0.072
16%
Short-distance migrants
0.12
578.7
6
0.19
557.0
8
0.25
539.9
15
0.060
32%
Average
0.32
841.0
9.6
0.36
823.27
7.6
0.42
795.8
15.7
0.066
18%
Table 8
Adjusted R2 and Akaike's information criterion (AIC) values of best models of avian species richness by guild for the models that used texture variables only, NLCD-derived land-
scape metrics only, and a combination of both for the Prairie Parkland (temperate). Bolded R2 and AIC values indicate the superior (texture-only or landscape metric-only) model.
Guild
Texture-only
models
Landscape metric-only
models
Texture and landscape metric
models
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Adj. R2
AIC
# of vars
Absolute R2 gain
Percent R2 gain
All birds
0.19
728.8
4
0.24
719.0
6
0.27
715.4
9
0.030
12%
Forest birds
0.29
688.9
4
0.36
675.5
7
0.40
673.4
17
0.044
12%
Grassland birds
0.20
200.8
8
0.28
184.1
8
0.30
186.3
15
0.019
7%
Shrubland birds
0.32
255.9
12
0.28
256.4
3
0.36
247.2
13
0.039
12%
Neotropical migrants
0.15
603.9
9
0.23
585.6
7
0.27
584.3
14
0.036
16%
Permanent residents
0.51
316.9
12
0.56
296.3
8
0.59
286.0
9
0.030
5%
Short-distance migrants
0.24
254.7
8
0.19
262.0
4
0.29
244.4
8
0.047
20%
Average
0.27
435.7
8.1
0.31
425.5
6.1
0.35
419.6
12.1
0.035
11%
147
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


landscape variables (results not shown). This indicates some level of
complementarity, but we caution that this could potentially result
from model over-ﬁtting. For the overall study area (Table 5), the Eastern
Broadleaf Forest (Table 7), and the Prairie Parkland (Table 8), the
improvement in adjusted R2 was small, and the joint models were not
very parsimonious (full study region: average of 20.0 variables per
model; Eastern Broadleaf Forest: 17.4 variables per model; Prairie Park-
land: 12.4 variables per model).
However, in the Laurentian Mixed Forest, four of the seven land-
scape and texture models showed absolute improvement in adjusted
R2 greater than 0.10, and six of the seven models had relative adjusted
R2 improvement greater than 30% (Table 6). Gains of this magnitude
cannot be explained by over-ﬁtting alone, and we thus conclude that
at least in the Laurentian Mixed Forest, measures of image texture and
landscape metrics are complementary.
Because measures of image texture characterize spatial heterogene-
ity in landcover and vegetation, two key components of avian habitat,
our fourth prediction was that our texture measure models would
perform better for guilds based on habitat preference compared
with guilds based on migratory habit (Fig. 3). This prediction held
overall with texture models explaining, on average, 32% of the varia-
tion in species richness of habitat guilds and 26% of variation of
migratory guilds. We do note, however, that the strongest model
overall was for species richness of permanent residents, though it
was followed by the three habitat guilds.
We were also surprised to see which habitat guilds showed the
strongest models in certain ecoregions (Fig. 3). Texture measure-
based models explained the most variation in grassland bird species
richness in the Laurentian Mixed Forest (adjusted R2=0.41) followed
by the Eastern Broadleaf Forest (0.37), and the Prairie Parkland
(0.20). Texture measures explained twice as much of the variation
in grassland bird species richness in the most forested region than
in the region with the most agriculture and grassland. Similarly,
models of forest bird species richness were strongest in the Eastern
Broadleaf Forest (adjusted R2=0.45), then the Prairie Parkland
(0.29), then the Laurentian Mixed Forest (0.25). Again, models of
forest bird species richness were strongest in a moderately forested
ecoregion and weakest in the most heavily forested ecoregion. This
suggests that it is easier to model species richness of certain groups
of birds in areas where there is less suitable habitat for them. For
example, in a grassland area with only a few small “islands” of forest,
forest bird richness will be very low in the grassland areas and very
high in the forest area. On the other hand, in a completely forested
area, it will be harder to predict which areas of forest will have the
highest forest bird richness since the entire area is potentially suitable
habitat for forest birds.
An important caveat for this study, as mentioned earlier, is that
while all our satellite images were acquired during the growing sea-
son, they were not all from the same phenological stage. In most
remote sensing analyses, it is ideal for imagery to have the same
acquisition date, as image phenological stage may affect analysis,
including image texture analysis (Culbert et al., 2009). However,
when analyzing very large areas, this is not always possible. This likely
introduced extraneous variability into our texture measurements,
and had all our images been acquired at the same phenological
stage, the relationships between image texture measures and avian
species richness would likely have been even stronger.
The use of image texture measures for habitat and biodiversity
analyses has two potential drawbacks: signiﬁcant computational re-
quirements and difﬁculties in interpreting the ecological relevance of
speciﬁc texture measures. First, calculations of second-order image
texture are computationally much more demanding than other com-
mon remote sensing data analyses. While this challenge will become
less signiﬁcant as computing power continues to increase, it is cur-
rently non-trivial to calculate second-order texture measures over
a broad extent. Second, interpreting the ecological meaning of spe-
ciﬁc texture measures is challenging. Many of the texture measures,
especially second-order measures, are difﬁcult to conceptualize in
terms of what they represent “on the ground”. This means that
texture measures provide only limited additional insights into the
ecology of birds. However, there are many applications, such as con-
servation planning, for which the variables selected may matter
much less than the quality of the output map, and texture metrics
can be valuable for such tasks.
In summary, our study showed that image-texture can be an impor-
tant tool to explain avian species richness patterns over broad areas.
Image texture measures were effective in modeling species richness
for several avian guilds, and over varied habitats, ranging from grass-
land to forest. In particular, texture measures showed superior per-
formance to landscape composition metrics in the most forested
ecoregion, and the two types of measures showed strong comple-
mentarity. However, in about three-fourths of our models, texture
measures had slightly less explanatory power than landscape com-
position metrics. For this reason the simultaneous use of texture
measures and landscape metrics should be considered. The use of
image texture measures is also highly useful when an accurate land-
cover map is unavailable for a given study area, or when the classes
of existing maps do not capture the ecological attributes relevant to
the study. The use of image texture is a valuable approach for charac-
terizing structure from continuous data sources and should therefore
be considered in the spatial modeling of species diversity and habitat
suitability for conservation planning.
Acknowledgments
The Authors would like to thank D. Helmers for technical assis-
tance and G. Thain and the University of Wisconsin-Madison Center
for High-Throughput Computing for substantial data processing as-
sistance. Two anonymous reviews provided feedback, which greatly
improved the manuscript. This work was supported by the NASA Biodi-
versity Program, and a NASA Earth Systems Science Fellowship to P. D.
Fig. 3. Adjusted R2 values of best multivariate models of avian species richness based
on measures of image texture for each avian guild and ecoregion. Circle diameter is
proportional to adjusted R2 value.
148
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


Culbert. T. P. Albright acknowledges support from National Science
Foundation, Cooperative Agreement EPS-0814372.
References
Albright, T. P., Pidgeon, A. M., Rittenhouse, C. D., Clayton, M. K., Flather, C. H., Culbert,
P.D., et al. (2010). Effects of drought on avian community structure. Global Change
Biology, 16, 2158–2170.
Albright, T. P., Pidgeon, A. M., Rittenhouse, C. D., Clayton, M. K., Flather, C. H., Culbert,
P.D., et al. (2011). Heat waves measured with MODIS land surface temperature
data predict changes in avian community structure. Remote Sensing of Environment,
115, 245–254.
Atauri, J. A., & de Lucio, J. V. (2001). The role of landscape structure in species richness
distribution of birds, amphibians, reptiles and lepidopterans in Mediterranean
landscapes. Landscape Ecology, 16, 147–159.
Bailey, R. G. (1995). Description of the ecoregions of the United States. : United States
Department of Agriculture.
Baraldi, A., & Parmiggiani, F. (1995). An investigation of the textural characteristics
associated with gray-level co-occurrence matrix statistical parameters. IEEE
Transactions on Geoscience and Remote Sensing, 33, 293–304.
Bellis, L. M., Pidgeon, A. M., Radeloff, V. C., St-Louis, V., Navarro, J. L., & Martella, M. B.
(2008). Modeling habitat suitability for Greater Rheas based on satellite image tex-
ture. Ecological Applications, 18, 1956–1966.
Bergen, K. M., Goetz, S. J., Dubayah, R. O., Henebry, G. M., Hunsaker, C. T., Imhoff, M. L.,
et al. (2009). Remote sensing of vegetation 3-D structure for biodiversity and
habitat: Review and implications for LiDAR and radar spaceborne missions. Journal
of Geophysical Research-Biogeosciences, 114, G00E06.
Buckton, S. T., & Ormerod, S. J. (2002). Global patterns of diversity among the specialist
birds of riverine landscapes. Freshwater Biology, 47, 695–709.
Clawges, R., Vierling, K., Vierling, L., & Rowell, E. (2008). The use of airborne LiDAR to
assess avian species diversity, density, and occurrence in a pine. Remote Sensing
of Environment, 112, 2064–2073.
Coburn, C. A., & Roberts, A. C. B. (2004). A multiscale texture analysis procedure for im-
proved forest stand classiﬁcation. International Journal of Remote Sensing, 25,
4287–4308.
Cody, M. L. (1981). Habitat selection in birds — The roles of vegetation structure, com-
petitors, and productivity. Bioscience, 31, 107–113.
Culbert, P. D., Pidgeon, A. M., St-Louis, V., Bash, D., & Radeloff, V. C. (2009). The impact
of phenological variation on texture measures of remotely sensed imagery. IEEE
Journal of Selected Topics in Applied Earth Observations and Remote Sensing, 2,
299–309.
Daly, C., Halbleib, M., Smith, J. I., Gibson, W. P., Doggett, M. K., Taylor, G. H., et al. (2008).
Physiographically sensitive mapping of climatological temperature and precipita-
tion across the conterminous United States. International Journal of Climatology,
28, 2031–2064.
Donovan, T. M., & Flather, C. H. (2002). Relationships among north American songbird
trends, habitat fragmentation, and landscape occupancy. Ecological Applications, 12,
364–374.
Estes, L. D., Okin, G. S., Mwangi, A. G., & Shugart, H. H. (2008). Habitat selection by a
rare forest antelope: A multi-scale approach combining ﬁeld data and imagery
from three sensors. Remote Sensing of Environment, 112, 2033–2050.
Estes, L. D., Reillo, P. R., Mwangi, A. G., Okin, G. S., & Shugart, H. H. (2010). Remote sens-
ing of structural complexity indices for habitat and species distribution modeling.
Remote Sensing of Environment, 114, 792–804.
Farina, A. (1997). Landscape structure and breeding bird distribution in a sub-Mediter-
ranean agro-ecosystem. Landscape Ecology, 12, 365–378.
Flather, C. H., & Sauer, J. R. (1996). Using landscape ecology to test hypotheses about
large-scale abundance patterns in migratory birds. Ecology, 77, 28–35.
Franklin, S. E., Hall, R. J., Moskal, L. M., Maudie, A. J., & Lavigne, M. B. (2000). Incorporat-
ing texture into classiﬁcation of forest species composition from airborne multi-
spectral images. International Journal of Remote Sensing, 21, 61–79.
Franklin, S. E., Maudie, A. J., & Lavigne, M. B. (2001). Using spatial co-occurrence texture
to increase forest structure and species composition classiﬁcation accuracy. Photo-
grammetric Engineering and Remote Sensing, 67, 849–855.
Gaston, K. J., Blackburn, T. M., & Goldewijk, K. K. (2003). Habitat conversion and global
avian biodiversity loss. Proceedings of the Royal Society B: Biological Sciences, 270,
1293–1300.
Goetz, S., Steinberg, D., Dubayah, R., & Blair, B. (2007). Laser remote sensing of canopy
habitat heterogeneity as a predictor of bird species richness in an eastern temper-
ate forest, USA. Remote Sensing of Environment, 108, 254–263.
Gottschalk, T. K., Huettmann, F., & Ehlers, M. (2005). Thirty years of analysing and
modelling avian habitat relationships using satellite imagery data: A review. Inter-
national Journal of Remote Sensing, 26, 2631–2656.
Haralick, R. M. (1979). Statistical and structural approaches to texture. Proceedings of
the IEEE, 67, 786–804.
Haralick, R. M., Shanmuga, K., & Dinstein, I. (1973). Textural features for image classi-
ﬁcation. IEEE Transactions on Systems, Man, and Cybernetics, SMC3, 610–621.
Hepinstall, J. A., & Sader, S. A. (1997). Using Bayesian statistics, Thematic Mapper
satellite imagery, and breeding bird survey data to model bird species probability
of occurrence in Maine. Photogrammetric Engineering and Remote Sensing, 63,
1231–1237.
Hines, J. E., Boulinier, T., Nichols, J. D., Sauer, J. R., & Pollock, K. H. (1999). COMDYN:
Software to study the dynamics of animal communities using a capture–recapture
approach. Bird Study, 46, 209–217.
Homer, C., Huang, C. Q., Yang, L. M., Wylie, B., & Coan, M. (2004). Development of a
2001 national land-cover database for the United States. Photogrammetric Engi-
neering and Remote Sensing, 70, 829–840.
Hudak, A. T., & Wessman, C. A. (1998). Textural analysis of historical aerial photogra-
phy to characterize woody plant encroachment in South African savanna. Remote
Sensing of Environment, 66, 317–330.
Huete, A., Didan, K., Miura, T., Rodriguez, E. P., Gao, X., & Ferreira, L. G. (2002). Overview
of the radiometric and biophysical performance of the MODIS vegetation indices.
Remote Sensing of Environment, 83, 195–213.
Hutto, R. L. (1985). Habitat selection by nonbreeding migratory birds. In M. L. Cody
(Ed.), Habitat selection in birds (pp. 455–476). NY: Academic Press.
Innes, J. L., & Koch, B. (1998). Forest biodiversity and its assessment by remote sensing.
Global Ecology and Biogeography, 7, 397–419.
Kayitakire, F., Hamel, C., & Defourny, P. (2006). Retrieving forest structure variables
based on image texture analysis and IKONOS-2 imagery. Remote Sensing of Environ-
ment, 102, 390–401.
Kerr, J. T., & Ostrovsky, M. (2003). From space to species: Ecological applications for
remote sensing. Trends in Ecology & Evolution, 18, 299–305.
Kéry, M., & Schmid, H. (2004). Monitoring programs need to take into account imper-
fect species detectability. Basic and Applied Ecology, 5, 65–73.
Kondo, T., & Nakagoshi, N. (2002). Effect of forest structure and connectivity on bird
distribution in a riparian landscape. Phytocoenologia, 32, 665–676.
Lesak, A. A., Radeloff, V. C., Hawbaker, T. J., Pidgeon, A. M., Gobakken, T., & Contrucci, K.
(2011). Modeling forest songbird species richness using LiDAR-derived measures
of forest structure. Remote Sensing of Environment, 115, 2823–2835.
Luoto, M., Virkkala, R., Heikkinen, R. K., & Rainio, K. (2004). Predicting bird species
richness using remote sensing in boreal agricultural-forest mosaics. Ecological
Applications, 14, 1946–1962.
MacArthur, R. H. (1958). Population ecology of some warblers of Northeastern coniferous
forests. Ecology, 39, 599–619.
MacArthur, R. H. (1972). Geographical ecology: Patterns in the distribution of species. :
Harper & Row.
MacArthur, R. H., & MacArthur, J. W. (1961). On bird species diversity. Ecology, 42,
594–598.
MacArthur, R., Recher, H., & Cody, M. (1966). On the relation between habitat selection
and species diversity. The American Naturalist, 100, 319–332.
Masek, J. G., Vermote, E. F., Saleous, N. E., Wolfe, R., Hall, F. G., Huemmrich, K. F., et al.
(2006). A Landsat surface reﬂectance dataset for North America, 1990–2000. IEEE
Geoscience and Remote Sensing Letters, 3, 68–72.
Myers, N., Mittermeier, R. A., Mittermeier, C. G., da Fonseca, G. A. B., & Kent, J. (2000).
Biodiversity hotspots for conservation priorities. Nature, 403, 858.
Myneni, R. B., Hoffman, S., Knyazikhin, Y., Privette, J. L., Glassy, J., Tian, Y., et al. (2002).
Global products of vegetation leaf area and fraction absorbed PAR from year one of
MODIS data. Remote Sensing of Environment, 83, 214–231.
Myneni, R. B., Nemani, R. R., & Running, S. W. (1997). Estimation of global leaf area
index and absorbed par using radiative transfer models. IEEE Transactions on Geo-
science and Remote Sensing, 35, 1380–1393.
Nagendra, H. (2001). Using remote sensing to assess biodiversity. International Journal
of Remote Sensing, 22, 2377–2400.
Nichols, J. D., Boulinier, T., Hines, J. E., Pollock, K. H., & Sauer, J. R. (1998). Inference
methods for spatial variation in species richness and community composition
when not all species are detected. Conservation Biology, 12, 1390–1398.
Peterjohn, B. G., & Sauer, J. R. (1999). Population status of North American grassland
birds from the North American breeding bird survey, 1966–1996. In P. D. Vickery,
& J. R. Herkert (Eds.), Ecology and conservation of grassland birds of the Western
Hemisphere (pp. 27–44). Camarillo, CA: Cooper Ornithological Society.
Pidgeon, A. M., Radeloff, V. C., Flather, C. H., Lepczyk, C. A., Clayton, M. K., Hawbaker, T.J.,
et al. (2007). Associations of forest bird species richness with housing and land-
scape patterns across the USA. Ecological Applications, 17, 1989–2010.
R Development Core Team. (2009). R: A language and environment for statistical
computing.
Rappole, J. H. (1995). The ecology of migrant birds. Washington, D.C.: Smithsonian Insti-
tute Press.
Rittenhouse, C. D., Pidgeon, A. M., Albright, T. P., Culbert, P. D., Clayton, M. K., Flather,
C.H., et al. (2010). Avifauna response to hurricanes: Regional changes in communi-
ty similarity. Global Change Biology, 16, 905–917.
Rosenzweig, M. L. (1995). Species diversity in space and time. : Cambridge University
Press.
Roy, P. S. (2003). Biodiversity conservation — Perspective from space. National Acade-
my Science Letters — India, 26, 169–184.
Seavy, N. E., Viers, J. H., & Wood, J. K. (2009). Riparian bird response to vegetation struc-
ture: A multiscale analysis using LiDAR measurements of canopy height. Ecological
Applications, 19, 1848–1857.
Shannon, C. E. (1948). A mathematical theory of communication. Bell System Technical
Journal, 27, 379–423 (and 623–656).
Stickler, C. M., & Southworth, J. (2008). Application of multi-scale spatial and spectral
analysis for predicting primate occurrence and habitat associations in Kibale
National Park, Uganda. Remote Sensing of Environment, 112, 2170–2186.
St-Louis, V., Pidgeon, A. M., Clayton, M. K., Locke, B. A., Bash, D., & Radeloff, V. C. (2009).
Satellite image texture and a vegetation index predict avian biodiversity in the
Chihuahuan Desert of New Mexico. Ecography, 32, 468–480.
St-Louis, V., Pidgeon, A. M., Radeloff, V. C., Hawbaker, T. J., & Clayton, M. K. (2006). High-
resolution image texture as a predictor of bird species richness. Remote Sensing of
Environment, 105, 299–312.
Sutherland, G. D., Harestad, A. S., Price, K., & Lertzman, K. P. (2000). Scaling of natal
dispersal distances in terrestrial birds and mammals. Conservation Ecology, 4, 16.
149
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150


Tews, J., Brose, U., Grimm, V., Tielborger, K., Wichmann, M. C., Schwager, M., et al. (2004). An-
imal species diversity driven by habitat heterogeneity. Journal of Biogeography, 31, 79–92.
The MathWorks, I. (1984–2010). Matlab. , R2010a.
Tittler, R., Villard, M., & Fahrig, L. (2009). How far do songbirds disperse? Ecography, 32,
1051–1061.
Tucker, C. J., Grant, D. M., & Dykstra, J. D. (2004). NASA's global orthorectiﬁed landsat
data set. Photogrammetric Engineering and Remote Sensing, 70, 313–322.
Turner, M. G., Gardner, R. H., & O'Neill, R. V. (2001). Landscape ecology in theory and
practice. New York: Springer.
Turner, D. P., Ritts, W. D., Cohen, W. B., Gower, S. T., Running, S. W., Zhao, M., et al.
(2006). Evaluation of MODIS NPP and GPP products across multiple biomes.
Remote Sensing of Environment, 102, 282–292.
Turner, W., Spector, S., Gardiner, N., Fladeland, M., Sterling, E., & Steininger, M. (2003).
Remote sensing for biodiversity science and conservation. Trends in Ecology & Evo-
lution, 18, 306–314.
Tuttle, E. M., Jensen, R. R., Formica, V. A., & Gonser, R. A. (2006). Using remote sensing image
texture to study habitat use patterns: A case study using the polymorphic white-
throated sparrow (Zonotrichia albicollis). Global Ecology and Biogeography, 15, 349–357.
Wan, Z. M., Zhang, Y. L., Zhang, Q. C., & Li, Z. L. (2002). Validation of the land-surface
temperature products retrieved from Terra Moderate Resolution Imaging Spectro-
radiometer data. Remote Sensing of Environment, 83, 163–180.
Wiens, J. A. (1974). Habitat heterogeneity and avian community structure in North-
American grasslands. American Midland Naturalist, 91, 195–213.
Willson, M. F. (1974). Avian community organization and habitat structure. Ecology, 55,
1017–1029.
Wood, E. M., Pidgeon, A. M., & Radeloff, V. C. (2007). Comparing image texture from in-
frared versus panchromatic aerial photographs for predicting avian species rich-
ness in a Midwest prairie savanna. 68th Midwest Fish and Wildlife Conference.
December 9–12, 2007. Madison, WI.
Wulder, M. A., LeDrew, E. F., Franklin, S. E., & Lavigne, M. B. (1998). Aerial image texture
information in the estimation of northern deciduous and mixed wood forest leaf
area index (LAI). Remote Sensing of Environment, 64, 64–76.
Wunderle, A. L., Franklin, S. E., & Guo, X. G. (2007). Regenerating boreal forest structure
estimation using SPOT-5 pan-sharpened imagery. International Journal of Remote
Sensing, 28, 4351–4364.
150
P.D. Culbert et al. / Remote Sensing of Environment 118 (2012) 140–150
