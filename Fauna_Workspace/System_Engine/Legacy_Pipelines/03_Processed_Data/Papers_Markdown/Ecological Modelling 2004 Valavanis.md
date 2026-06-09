--- 
source: Ecological Modelling 2004 Valavanis.pdf
--- 

Ecological Modelling 178 (2004) 417–427
A GIS environmental modelling approach to essential
ﬁsh habitat designation
Vasilis D. Valavanis a,∗, Stratis Georgakarakos b,1, Argyris Kapantagakis a,2,
Andreas Palialexis c,3, Isidora Katara c,3
a Hellenic Centre for Marine Research (Crete Branch), Institute of Marine Biological Resources,
P.O. Box 2214, 71003 Iraklion, Crete, Greece
b Department of Marine Sciences, University of the Aegean, University Hill, 81100 Mytilene, Lesvos, Greece
c Department of Biology, University of Crete, P.O. Box 2208, 71409 Iraklion, Crete, Greece
Received 28 April 2003; received in revised form 23 December 2003; accepted 5 February 2004
Abstract
Proper designation of essential ﬁsh habitat (EFH) is a highly important spatial measure in any management of ﬁshery resources.
EFH is characterised by an aggregation of abiotic and biotic parameters that are suitable for supporting and sustaining ﬁsh
populations during all stages of their life cycle. We propose a multi-parameter model that includes processing and integration
of EFH environmental and biological descriptors under a Geographic Information System. We apply the model to short-ﬁnned
squid population dynamics in the eastern Mediterranean Sea, based on species life history data derived from biological and
genetic research. The model output includes squid monthly EFH designations for the 1997–1998 ﬁshing season and reveals the
spatiotemporal aspect of the biological and ecological squid dynamics in the region.
© 2004 Elsevier B.V. All rights reserved.
Keywords: Fisheries model; Cephalopods; Satellite imagery; Ecological modelling; GIS
1. Introduction
In 1996, the renamed US Magnuson–Stevens Act
mandated the identiﬁcation of essential ﬁsh habitat
(EFH) for ‘quota’ species. The US Congress de-
∗Corresponding author. Tel.: +30-2810-337817;
fax: +30-2810-337822.
E-mail addresses: vasilis@imbc.gr (V.D. Valavanis),
stratisg@aegean.gr (S. Georgakarakos), akap@imbc.gr
(A. Kapantagakis), andreaspal@pathﬁnder.gr (A. Palialexis),
isidora10@yahoo.com (I. Katara).
1 Tel.: +30-22510-36822.
2 Tel.: +30-2810-337816.
3 Tel.: +30-2810-396347.
ﬁned EFH as ‘those waters and substrate necessary
to ﬁsh for spawning, breeding, feeding, or growth
to maturity’, a deﬁnition that includes the physical,
chemical and biological properties of marine areas
and the associated sediment and biological assem-
blages that sustain ﬁsh populations throughout their
full life cycle (DOC, 1997). Under this Act, the des-
ignation of EFH in US waters is based on the best
available science regarding the habitat requirements
of each species. The compilation of the available in-
formation on the distribution, abundance and habitat
requirements for each species in EFH reports com-
prises an extensive survey of the important biological
and genetic literature as well as original analyses of
0304-3800/$ – see front matter © 2004 Elsevier B.V. All rights reserved.
doi:10.1016/j.ecolmodel.2004.02.015


418
V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
ﬁshery-independent datasets documented in species
life history data reports referred to as the EFH source
documents.
Species life history data include information on
current and historic stock sizes, stock assessments,
geographic range and periods and location of major
life history stages. In addition, information on the
habitat requirements is provided for each life history
stage, including the range of habitat and environ-
mental variables that control or limit distribution,
abundance, growth, reproduction, mortality and pro-
ductivity. Speciﬁcally, these data provide information
on species type (e.g., benthic or pelagic), species
preferred living ranges of temperature and salinity,
recruitment periods, spawning periods and character-
istics (e.g., preferred spawning sediment types and
spawning temperature and depth ranges), migration
habits, maximum depth of species occurrence, etc.
Species life history data may be viewed as the start-
ing point for spatial analysis and modelling of EFH
through new technologies such as Geographic Infor-
mation Systems (GIS) and Remote Sensing (RS). GIS
may use species life history data as constraint param-
eters in the analysis of remotely sensed environmental
and surveyed ﬁsheries data, providing integrated out-
put on seasonal areas that are important in various
stages of species life cycles. GIS may reveal the geo-
graphic distribution of species life history and, in com-
bination with results from RS-based oceanographic
GIS analysis, may reveal the dynamic interactions be-
tween species populations and oceanographic features
in a spatiotemporal scale (Meaden, 2000; Valavanis,
2002). Speciﬁc spatial and temporal patterns on
species resources dynamics (e.g., spawning and ag-
gregation locations and abundance geodistribution)
may be examined with the use of GIS.
Several studies are focused to this end. Marine
species population spatiotemporal dynamics are stud-
ied through GIS and associated RS, surveyed and life
history data for the mapping of spawning grounds for
sardine and anchovy (Lluch-Belda et al., 1991), wall-
eye pollock (Varkentin et al., 1999), herring (Brown
and Norcross, 1999), sole (Eastwood et al., 2001),
salmon (Geist and Dauble, 1998), squid (Kiyofuji
et al., 1998; Roberts, 1998; Waluda and Pierce, 1998;
Xavier et al., 1999; Sakurai et al., 2000; Bellido et al.,
2001) and cuttleﬁsh (Pierce et al., 1998; Denis et al.,
2001; Valavanis et al., 2002). Additionally, the distri-
bution of optimum living habitat is modelled through
GIS for tiger prawn (Loneragan et al., 1998), sardine,
anchovy and hake (Yanez et al., 1996; Logerwell and
Smith, 1999), weathervane scallop (Turk, 1999) and
lesser sandeel (Wright et al., 2000). A NOAA web-
site (http://www.fakr.noaa.gov/maps) simpliﬁes the
process for making informed decisions for species
EFH by using both spatial and tabular data over the
Internet. Here various geographic information and
tabular datasets derived from ﬁsheries catch and ob-
server data and known science are organised under an
online GIS environment, which pulls the spatial and
tabular data together providing an easy and powerful
tool for the designation and management of EFH in
the Alaskan region.
Guisan and Zimmermann (2000) reviewed the
modelling efforts used for the prediction of species
habitat distribution. Most approaches use ordinary
multiple regression (e.g., Generalized Linear Models),
neural networks, ordination and classiﬁcation meth-
ods, Bayesian models, locally weighted approaches
(e.g., Generalized Additive Models) or combinations
of these models. Koutsoubas et al. (1999) developed
a GIS on cephalopod resource dynamics in the east-
ern Mediterranean, an application that is based on
the integration of species life history data and envi-
ronmental variables that describe certain oceanic pro-
cesses (upwelling, gyres and fronts). Arvanitidis et al.
(2002) overviewed the biology of the short-ﬁnned
squid in the NE Atlantic and Mediterranean in terms
of species–environment–habitat interactions while
Georgakarakos et al. (2002) developed a model for the
prediction of loliginid and ommastrephid squid stocks
in the eastern Mediterranean based on univariate and
multivariate time series analysis of environmental and
habitat descriptors. Finally, benthic habitat data and
suitability indices of relative abundance across envi-
ronmental gradients are commonly used within GIS
in order to develop Habitat Suitability Index (HSI)
models (e.g., Christensen et al., 1997; Rubec et al.,
1998a,b; Brown et al., 2000). HSI models may help
predict optimal habitat and abundance zones for vari-
ous species, therefore aiding managers in designating
EFH.
With the rise of new powerful statistical techniques
and GIS tools, the development of predictive habitat
distribution models has rapidly increased in ecology
(Guisan and Zimmermann, 2000). Such models are


V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
419
static and probabilistic in nature, since they statisti-
cally relate the geographical distribution of species to
their present environment. Here, we propose a GIS
EFH model that is based on the spatial integration
among vector and raster datasets, including satellite
imagery on sea surface temperature distribution and
chlorophyll concentration, surveyed sea surface salin-
ity distribution, monitored ﬁsheries production and
ﬁshing ﬂeet activity data and bathymetry. Integra-
tions among these EFH descriptors are constrained
by species life history data on optimum (or preferred)
living conditions and maximum depth of species
occurrence. The model is applied to short-ﬁnned
squid, Illex coindetti Verany, 1839 (Cephalopoda,
Omnastrephidae) population dynamics in the east-
ern Mediterranean Sea during the 1997–1998 ﬁshing
season, revealing the spatiotemporal distribution of
species EFH on a monthly basis.
Fig. 1. The study area is located in the eastern Mediterranean Sea. This bathymetry image shows the Aegean Sea and part of the Ionian,
Libyan and Levantine Seas revealing extreme changes in the topography of the region (North Aegean Plateau and trough, Chios Basin,
Cyclades Plateau and Cretan Basin). Major ﬁshing ﬂeet activity occurs on the North Aegean and Cyclades Plateau and in the Antikithira
Strait. Ofﬁcial ﬁsheries data sampling stations and ﬁsheries production statistical rectangles are also shown.
2. Study site, data and model description
The study area includes the Hellenic Seas (East-
ern Mediterranean) comprising four main water bod-
ies, the Aegean and Ionian Seas and the north parts of
the Libyan and Levantine Seas (Fig. 1). The topogra-
phy of the area is characterised by extreme changes
in bathymetry, featuring extensive and smaller shal-
low continental shelves (North Aegean and Cyclades
plateau and Cretan continental shelf) interrupted by
deep trenches (North Aegean trough and Chios and
Cretan basins). The area is well monitored in terms of
monthly satellite imagery and ﬁsheries data (Table 1).
Sea surface temperature distribution (SST) is avail-
able through the German Aerospace Agency’s (DLR)
satellite data archive while sea surface chlorophyll
concentration (Chl-a) is available through NASA’s
Distributed Active Archive Center. Sea surface salinity


420
V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
Table 1
Data variables and their characteristics used for the initiation of the GIS-based EFH model
Data variable
Sensor sampler
Spatiotemporal resolution
Data type
Archive source
Sea surface temperature
(SST)
Advanced very high resolution
radiometer (AVHRR)
1.6 km, monthly, May
1993–December 2000
RASTER
German Aerospace Agency
(DLR)
Sea surface
chlorophyll (Chl-a)
Sea viewing wide ﬁeld of view
sensor (SeaWiFS)
4 km, monthly, September
1997–December 2000
RASTER
Distributed Active Archive
Center (NASA)
Sea surface salinity
(SSS)
Processed historical in situ
measurements
10 km, monthly, decadal
climatology
RASTER
Mediterranean Oceanic
Database (MODB)
Fisheries production
(catch)
Monitored data through ofﬁcial
sampling stations
60 km × 40 km rectangles,
monthly, January
1995–December 2000
VECTOR
Hellenic Fisheries
Management System
(HFMS)
Fishing ﬂeet activity
areas
Monitored data through ofﬁcial
sampling stations
1:100,000, yearly, 1996–2000
VECTOR
Hellenic Fisheries
Management System (HFMS)
Bathymetry
Processed ERS-1, Geostat and
historical depth soundings
Raw data: 10 km, processed
data: 50 m isobaths
VECTOR
Laboratory for Satellite
Altimetry (NOAA)
Coastline
Digitisation of nautical charts
and aerial photography
1:100,000
VECTOR
Hellenic Ministry of
Environment
Species life history
data
Literature research
N/A
ASCII
TEXT
CEPHBASE and ICES
Species life history data refers to short-ﬁnned squid (Illex coindetti) life cycle in Atlantic Ocean and Mediterranean Sea.
distribution (SSS) is available through the Mediter-
ranean Oceanic Database as a decadal climatological
product (Brasseur et al., 1996). Monthly ﬁsheries pro-
duction and ﬁshing activity data are ofﬁcially sampled
through a network of 22 sampling stations operated
by the Hellenic Centre of Marine Research through
the Hellenic Fisheries Management System (HFMS).
Coastline is derived through digitisation of aerial pho-
tography and nautical maps while bathymetry is cal-
culated through processing (kriging) of a point dataset
derived from a blending of depth soundings collected
from ships with detailed gravity anomaly information
obtained from the Geosat and ERS-1 satellite altime-
Table 2
Example of species life history data on the ecology and biology of four cephalopod species in NE Atlantic, organised and provided by
the International Council for the Exploitation of the Sea (ICES)
Species life history
Long-ﬁnned squid
(Loligo vulgaris)
Cuttleﬁsh (Sepia
ofﬁcinalis)
Common octopus
(Octopus vulgaris)
Short-ﬁnned squid
(Illex coindetti)
Benthic/pelagic
Pelagic
Benthic
Benthic
Pelagic
Temperature range
10–25 ◦C
10–30 ◦C
10–30 ◦C
7.5–20 ◦C
Spawn season
December–January
March–July
June–September
Spring/fall
Spawn depth
10–30 m
2–50 m
100 m
Unknown
Substrate type
Hard
Muds/sands
Rocks/sands
Unknown
Bathymetry range
10–100 m
10–300 m
0–500 m
60–350 m
Migration pattern
In > offshore
Off > inshore
Off > inshore
Unknown
Migration scale
200 km
50 km
50 km
Unknown
Life history information on short-ﬁnned squid preferred temperature and bathymetry ranges were used as guide in data integrations through
the proposed EFH model.
try missions (Smith and Sandwell, 1997). Species life
history data (Table 2) on short-ﬁnned squid popula-
tion dynamics are derived from biological and genetic
studies (Boyle, 1983; Raya et al., 1995), CEPHBASE
(Wood et al., 2000) and ofﬁcial reports (Anon. 1996,
1997). All datasets are commonly georeferenced and
organised under a GIS environment in regular grids
and vector coverages of polygon topology (Valavanis
et al., 1998).
The proposed EFH model is based on spatial data in-
tegrations using the Environmental Systems Research
Institute’s ARC/INFO GIS (ESRI, 1994). The model
is linked to a GIS database and it performs extensive


V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
421
Table 3
List of GIS integrations performed by the proposed EFH model among vector and raster datasets constrained by species life history data
for the modelling of Illex coindetti EFH
Integration datasets
GIS analysis type model module
Model result
1. Species total catch coverage (statistical
rectangle system)
Selection for species catch more than
0 kg (stage A)
Geodistribution of species catch
2a. Geodistribution of species catch 2b.
Species maximum depth of occurrence
(bathymetric dataset and species life
history data)
Spatial integration between polygon
coverages (stage A)
Geodistribution of species major
occurrence areas
3a. Geodistribution of species major
occurrence areas 3b. Fishing ﬂeet
major activity areas
Spatial integration between polygon
coverages (stage A)
Geodistribution of species major
concentration areas
4a. Geodistribution of species major
concentration areas 4b. Monthly SST,
Chl-a, SSS
Spatial selection between a polygon
coverage (vector) and monthly grids
(raster) (stage B)
Minimum and maximum values of species
SST, Chl-a, SSS preferences
5a. Minimum and maximum values of
species SST, Chl-a, SSS preferences
per month 5b. SST, Chl-a, SSS
monthly grids
Spatial selection in grids using certain
minimum and maximum values and
conversion of selected areas to polygons
(stage C)
Species preferred areas based on SST,
Chl-a, SSS minimum and maximum values
Final integration: 6a. Species preferred
areas based on SST, 6b. species
preferred areas based on Chl-a, 6c.
species preferred areas based on SSS
Spatial integration among polygon
coverages (stage D)
Modelled monthly EFH based on optimum
habitat environmental descriptors
data integration analyses and modelling among vector
and raster datasets (Table 3). EFH modelling is devel-
oped for short-ﬁnned squid populations in the eastern
Mediterranean for the period September 1997–August
1998. The EFH model consists of four main analytical
stages (Fig. 2):
1. Stage A (species concentration areas): Monitored
ﬁsheries production (catch data) and bathymetry
(maximum depth of species occurrence) are spa-
tially integrated to reveal species major occurrence
areas. The resultant dataset is spatially integrated
with ﬁshing ﬂeet activity data to reveal species
major concentration areas. All integrations are
performed on vector datasets (spatial integration
among polygons).
2. Stage B (environmental integration): The resultant
dataset from stage A (species major concentration
areas) is separately integrated with SST, Chl-a and
SSS (spatial integration among a regular grid and
a polygon coverage). Minimum and maximum val-
ues in these three EFH environmental descriptors
are calculated.
3. Stage C (environmental selection): The resulted
minimum and maximum values from stage B are
applied to satellite imagery for SST and Chl-a and
surveyed salinity dataset in order to reveal areas
that satisfy the derived minimum and maximum
environmental values. This spatial selection in reg-
ular grids results in three grids that show areas de-
scribing EFH in terms of SST, Chl-a and SSS.
4. Stage D (EFH output): The three output grids from
stage C are converted to polygon coverages. The
three vector coverages are integrated into one poly-
gon coverage that describes those areas that com-
monly satisfy species preferred living conditions in
terms of optimum SST, Chl-a and SSS values (mod-
elled EFH, spatial integration among polygons).
3. Results and discussion
The organisation and manipulation of ﬁshery data
through GIS provides new approaches for further data
processing. The integration of monitored ﬁshery catch
data with bathymetry reveals ‘species major occur-
rence areas.’ Such spatial integration is constrained
by life history data on maximum depth of species oc-
currence. In the case of Oﬁllex coindetti, we use a
depth limit of 350 m. This limit is critical mainly for


422
V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
Fig. 2. Architecture of the GIS EFH model. Four main data analysis and modelling stages are linked to a GIS database where remotely
sensed and monitored data, derived from international and national online data archives, are stored. The EFH modelling is a series of
spatial integrations among raster and vector datasets for the spatiotemporal mapping of species optimum living conditions in terms of SST,
Chl-a, SSS and bathymetry.
two reasons: First, the depth of 350 m is the limit Fo-
rillex coindetti occurrence (based on the species life
history). Second, the same limit represents the aver-
age depth of the major ﬁshing tool targeting on Illex
in the area (trawl). In addition, most of the ﬁshery
grounds, where the commercial ﬁshing ﬂeet operates
in the study area, are found below the 350 m bathy-
metric contour (Fig. 1). The resulted ‘species major
occurrence areas’ are integrated with ﬁshing ﬂeet ma-
jor activity areas to reveal ‘species major concentra-
tion areas’ (Fig. 3). We assume here that ‘species ma-
jor concentration areas’ describe Illex-favoured habitat
in a more realistic way than the areas included in the
initial ﬁsheries catch-monitoring grid (60 km × 40 km
sampling ‘rectangles’ shown in Fig. 1). Thus, smaller
‘species major concentration areas’ allow extraction
and calculation of environmental ranges that may be
considered as more compact and robust environmental
descriptors of species habitat.
These data manipulations (stage A of the EFH
model) are highly important for the extraction of
habitat environmental descriptors and the ﬁnal EFH
modelling through the rest of the model’s stages.
The output on ‘species major concentration areas’
is used as the basic spatial extent for the selection
of those environmental ranges that species prefer
as their optimum living habitat. In this integration
between vector and raster datasets, minimum and


V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
423
Fig. 3. Spatial integrations among georeferenced ﬁshery data (EFH model: stage A). Catch distribution (top left) is integrated with
bathymetry (bottom left) to reveal species major occurrence areas (top right), which in turn, is integrated with ﬁshing ﬂeet major activity
areas (bottom left) to reveal species major concentration areas (bottom right). Species concentration areas are used for the extraction of
minimum and maximum SST, Chl-a and SSS ranges that are important for the modelling of the species EFH.
maximum environmental descriptors are calculated
for SST, Chl-a and SSS. Finally, the combined selec-
tion through spatial integration of SST, Chl-a and SSS
minimum and maximum values reveals those regions
that commonly characterise species preferred living
environmental conditions (EFH). Fig. 4 shows the ﬁ-
nal output of the EFH model, which includes modelled
monthly EFH for Illex coindetti during 1997–1998.
From a biological perspective, the resulted GIS
modelling of short-ﬁnned squid EFH in the eastern
Mediterranean reveals the spatiotemporal distribu-
tion of the species life history information on habitat
preferences and migration habits (Fig. 4). During
summer months (June–August, not presented here),
trawling activity is ofﬁcially prohibited throughout
the study area. The fact that no major areas of EFH
are found during this period (although summer data
were included in the EFH model) may be connected
to species decreased growth rate from a limited
food supply (Amaratunga et al., 1980) and species
post-spawning high mortality (Roper et al., 1984).
During fall and winter months, species growth rate
increases and as a highly mobile and opportunistic
species, short-ﬁnned squids migrate offshore to take
advantage of upwelling regions and associated plank-
ton blooms (Boyle, 1983; Valavanis et al., 2002).
Winter offshore upwelling events in the study area
occur at locations around Antikithira Strait and south
of Crete Island (Valavanis et al., 1999), mainly due to
seasonal strong winds and associated gyres in the re-
gion (Theocharis et al., 1993). During spring months
with spring spawning season approaching, species
start their spawning migration in a southward direc-
tion (Amaratunga, 1981; Dawe et al., 1981; Rathjen,
1981) to ﬁnd warmer spawning and egg develop-
ment temperature ranges (Boletzky et al., 1973). A
comparison between temperature ranges preferred
by NE Atlantic (Table 2: 7.5–20 ◦C, ICES data) and


424
V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
Fig. 4. Modelled EFH for short-ﬁnned squid population dynamics in the eastern Mediterranean during the ﬁshing season starting fall 1997
and ending spring 1998 (EFH model: stage D). EFH areas (in black) commonly satisfy species-preferred or optimum living ranges in four
EFH environmental descriptors (SST, Chl-a, SSS and bathymetry). Model stage C-derived environmental values that characterise these
areas are: MinSST: 3 ◦C, MaxSST: 29 ◦C, MinChl-a: 0.30 mg/m3, MaxChl-a: 15.60 mg/m3, MinSSS: 36.12‰, MaxSSS: 38.51‰.
Mediterranean (Fig. 4: 3–29 ◦C, EFH model) squid
populations reveals that Mediterranean squids tolerate
a wider temperature range, a biological pattern that is
well documented (Arkhipkin et al., 2000; Anderson
and Rodhouse, 2001; Machias et al., 2001; Arvanitidis
et al., 2002; Ragonese et al., 2002).
From a GIS modelling perspective, the use of
species life history data on habitat preferences in
terms of environmental descriptors, ﬁshery data and
bathymetry ranges proved adequate for species EFH
simulation. The model allows the constrained in-
tegration of various datasets in order to map the


V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
425
spatial extent of species preferred habitat conditions.
The organisation of habitat variables, important to
species biology and ecology, in a GIS environment
allowed the manipulation of the associated georef-
erenced datasets in order to ‘transform’ species life
history information (document data) to easily inter-
pretable digital maps (spatiotemporal data). This data
transformation provides an important tool for the
comprehending of species population dynamics and
encourages spatial thinking in management efforts
through information-based designation of the spatial
and temporal extent of EFH. The GIS-based EFH
model may be applied to species that are sensitive
to certain environmental and topographic features
throughout their life cycle. According to the life his-
tory data of the targeted species, additional datasets
may be introduced in the model in terms of bottom
substrate types, underwater vegetation assemblages,
dissolved oxygen values, pollutant parameters, etc.
The model is selected for inclusion in the Hellenic
Fisheries Management System (HFMS), which is
an on-going development effort for implementing a
Fisheries GIS infrastructure for Hellenic ﬁshery re-
sources management to be concluded by 2006 (GSRT,
2003). Through HFMS, the model will function in
both local and regional modes on species-speciﬁc or
group-of-species modelling applications, since the
spatial scale of the model output depends on the
resolution of the input datasets while the accuracy
of model results depends on the habitat descriptive
capability of the input variables.
4. Conclusions
A four-stage model for the identiﬁcation and map-
ping of essential ﬁsh habitat (EFH) is proposed,
based on the georeferenced integration of several
EFH environmental descriptors under a GIS envi-
ronment. Parameters that describe EFH are derived
from species life history data, which are used as the
model’s constraint factor. These parameters include
satellite imagery on sea surface temperature distribu-
tion and chlorophyll concentration, sea surface salin-
ity distribution, ﬁsheries production and ﬁshing ﬂeet
activity areas and bathymetry. Integration of these
datasets is constraint by life history data on species
preferred or optimum environmental conditions and
bathymetry ranges. The model output is better suited
to reﬂect theoretical ﬁndings on the spatiotemporal
nature of the species’ response to species-preferred
environmental conditions.
The model is applied to short-ﬁnned squid popula-
tion dynamics in the eastern Mediterranean Sea, based
on the above parameters, however it may be extended
to include more variables depending on the available
life history information of the targeted species. The
proposed EFH model is a useful tool in ﬁsheries man-
agement efforts by contributing as part of GIS-based
decision support systems, especially in the identiﬁca-
tion of species seasonal aggregation regions, the mon-
itoring of the variability of catch in these regions and
ultimately, the design of marine protected areas or sea-
sonally closure areas.
Acknowledgements
The development of the model was funded by two
European Communities research projects on cephalo-
pod resource dynamics in European waters (CEPH-
VAR,
FAIR-PL-1520-DG-XIV/1999–2001
and
CEPHSTOCK,
QOL-2001-5.1.2-FP5/2002–2004).
Authors thank Mr. John Laurijsen (researcher at the
Institute of Marine Biology of Crete, Greece) for
providing ﬁshery data through the HFMS database.
Authors thank the SeaWiFS Project (Code 970.2) and
the Distributed Active Archive Center (Code 902)
at the Goddard Space Flight Center, Greenbelt, MD
20771, for the production and distribution of SeaWIFS
data
(http://seawifs.gsfc.nasa.gov/SEAWIFS.html),
the German Aerospace Agency for the distribution
of AVHRR data through the freely available GISIS
(http://isis.dlr.de/) and the organizers of the Mediter-
ranean Oceanic Database (http://modb.oce.ulg.ac.be/
modb/welcome.html).
References
Amaratunga, T., 1981. Biology and distribution patterns in 1980
for squid, Illex illecebrosus, in Nova Scotian waters. NAFO
SCR, Doc. No. 81/VI/36. No. N318, p. 10.
Amaratunga, T., Rowell, T., Roberge, M., 1980. Summary of joint
Canada/U.S.S.R. research program on short-ﬁnned squid (Illex
illecebrosus). NAFO SCR, Doc. No. 80/II/38, No. N069, 16
February–4 June 1979, p. 36.


426
V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
Anderson, C.I.H., Rodhouse, P.G., 2001. Life cycles, oceanography
and variability: ommastrephid squid in variable oceanographic
invironments. Fish Res. 54, 133–143.
Anon., 1996. Report of the Working Group on Cephalopod
Fisheries and Life History. ICES CM 1996/K:3, Lisbon,
Portugal, 17–19 April 1996.
Anon., 1997. Report of the Working Group on Cephalopod
Fisheries and Life History. ICES CM 1997/K:2, Santa Cruz de
Tenerife, Spain, 7–9 April 1997.
Arkhipkin, A.I., Jereb, P., Ragonese, S., 2000. Growth and
maturation in two successive seasonal groups of the short-ﬁnned
squid,
Illex
coindetii
from
the
Strait
of
Sicily
(central
Mediterranean). ICES J. Mar. Sci. 57 (1), 31–41.
Arvanitidis, C., Koutsoubas, D., Robin, J.P., Pereira, J., Moreno,
A., Cunha, M., Valavanis, V.D., Eleftheriou, A., 2002. An
integrated overview of the biology of the short-ﬁnned squid
Illex coindetii, 1839 (Cephalopoda, Ommastrephidae) in the
Northeastern Atlantic and the Mediterranean. B. Mar. Sci.
71 (1), 129–146.
Bellido, J.M., Pierce, G.J., Wang, J., 2001. Environmental GIS
Modelling on the Scottish Veined Squid Loligoforbesi. ICES
CM 2001/K:03.
Boletzky, S.V., Rowe, L., Aroles, L., 1973. Spawning and
development of the eggs, in the laboratory, of Illex coindetii,
Mollusca Cephalopoda. Veliger 15, 257–258.
Boyle, P.R., 1983. Cephalopod life cycles. Species Accounts, vol.
I. Academic Press, London.
Brasseur, P., Brankart, J.M., Schoenauen, R., Beckers, J.M., 1996.
Seasonal temperature and salinity ﬁelds in the Mediterranean
Sea: climatological analyses of an historical data set. Deep-Sea
Res. 43, 159–192.
Brown, E.D., Norcross, B.L., 1999. Effect of herring egg
distribution and ecology on year class strength and adult
distribution. In: Abstract Proceedings of the 17th Lowell
Wakeﬁeld Fisheries Symposium on Spatial Processes and
Management of Fish Populations, Anchorage, Alaska, October
1999.
Brown, S.K., Buja, K.R., Jury, S.H., Monaco, M.E., Banner,
A., 2000. Habitat suitability index models for eight ﬁsh and
invertebrate species in Casco and Sheepscot Bays. Maine. N.
Am. J. Fish. Manage. 20 (2), 408–435.
Christensen, J.D., Battista, T.A., Monaco, M.E., Klein, C.J., 1997.
Habitat suitability index modelling and GIS technology to
support habitat management: Pensacola Bay, FL case study.
NOAA/NOS Strategic Environmental Assessments Division,
Silver Spring, MD, p. 90.
Dawe, E.G., Beck, P.C., Drew, H.J., Winters, G.H., 1981. Long
distance migration of a short-ﬁnned squid (Illex illecebrosus).
NAFO SCR, Doc. No. 81/VI/24, No. N303, p. 4.
Denis, V., Royer, J., Peries, P., Wang, J., Pierce, G.J., Boyle, P.R.,
Robin, J.P., 2001. French and UK bottom trawl ﬁsheries in
the English Channel: spatial and temporal patterns for ﬁshing
effort and cephalopod catch and integration of ﬂeet components
in the computation of squid and cuttleﬁsh abundance indices.
ICES CM2001/K:08.
DOC, 1997. Department of Commerce. Magnuson–Stevens Act
Provisions: Essential Fish Habitat (EFH). Federal Register, vol.
62, issue 244, pp. 66531–66559.
Eastwood, P.D., Meaden, G.J., Grioche, A., 2001. Modelling spatial
variations in spawning habitat suitability for the sole Solea
solea using regression quantiles and GIS procedures. Mar. Ecol.
Prog. Ser. 224, 251–266.
ESRI, 1994. ARC Macro Language. Environmental Systems
Research Institute Inc, Redlands, CA, USA, pp. 1/3–5/37.
Geist,
D.R.,
Dauble,
D.D.,
1998.
Redd
site
selection
and
spawning habitat use by fall chinook salmon: the importance of
geomorphic features in large rivers. Environ. Manage. 22 (5),
655–669.
Georgakarakos, S., Haralabus, J., Valavanis, V.D., Arvanitidis, C.,
Koutsoubas, D., 2002. Prediction of ﬁshery exploitation stocks
of Loliginid and Ommastrephid squids in Greek waters (Eastern
Mediterranean) using uni- and multivariate time series analysis
techniques. B. Mar. Sci. 71 (1), 269–288.
GSRT, 2003. General Secretariat of Research and Technology,
Hellenic Ministry of Development. Document on funded
national projects 2002–2003. Available online: http://www.
gsrt.gr/ (in Greek).
Guisan, A., Zimmermann, N.E., 2000. Predictive habitat distri-
bution models in ecology. Ecol. Modell. 135 (2–3), 147–186.
Kiyofuji, H., Saitoh, S., Sakurai, Y., 1998. A visualisation of the
variability of spawning ground distribution of Japanese common
squid (Todarades paciﬁcus) using marine GIS and satellite data
sets. Int. Arch. Photogr. Rem. Sen. 32, 882–886.
Koutsoubas, D., Arvanitidis, C., Valavanis, V.D., Georgakarakos,
S., Kapantagakis, A., Magoulas, A., Kotoulas, Y., 1999. Cepha-
lopod resources in the Eastern Mediterranean with particular
emphasis in Greek Seas: present and future perspectives. ICES
CM 1999/G:4.
Lluch-Belda,
D.,
Lluch-Cota,
D.B.,
Hernandez-Vazquez,
S.,
Salinas-Zavala, C., Schwartzlose, R.A., 1991. Sardine and
anchovy spawning as related to temperature and upwelling in
the California current system. CalCOFI Rep. 32, 105–111.
Logerwell, E.A., Smith, P.E., 1999. GIS mapping of survivor’s
habitat of pelagic ﬁsh off California. In: Abstract Proceedings
of the 17th Lowell Wakeﬁeld Fisheries Symposium on Spatial
Processes and Management of Fish Populations, Anchorage,
Alaska, October 1999.
Loneragan, N.R., Kenyon, R.A., Staples, D.J., Poiner, I.R.,
Conacher, C.A., 1998. The inﬂuence of seagrass type on the
distribution and abundance of postlarval and juvenile tiger
prawns (Penaeus esculentus and P. semisulcatus) in the western
Gulf of Carpentaria, Australia. J. Exp. Mar. Biol. Ecol. 228 (2),
175–195.
Machias, A., Vassilopoulou, V., Vatsos, D., Bekas, P., Kallianiotis,
A., Papaconstantinou, C., Tsimenides, N., 2001. Bottom trawl
discards in the northeastern Mediterranean Sea. Fish. Res. 53,
181–195.
Meaden, G.J., 2000. GIS in ﬁsheries management. GeoCoast 1 (1),
82–101.
Pierce, G.J., Wang, J., Bellido, J.M., Waluda, C.M., Robin,
J.P., Denis, V., Koutsoubas, D., Valavanis, V.D., Boyle,
P.R., 1998. Relationships between cephalopod abundance
and environmental conditions in the Northeast Atlantic and
Mediterranean as revealed by GIS. ICES CM 1998/M:20.
Ragonese, S., Jereb, P., Dawe, E., 2002. A comparison of
growth performance across the squid genus Illex (Cephalopoda,


V.D. Valavanis et al. / Ecological Modelling 178 (2004) 417–427
427
Ommastrephidae) based on modelling weight-at-length and age
data. J. Shellﬁsh Res. 21 (2), 851–860.
Rathjen, W.F., 1981. Exploratory squid catches along the Eastern
United States continental slope. J. Shellﬁsh Res. 1, 153–159.
Raya, C.P., Balguerias, E., Fernandez-Nunez, M.M., d Pierce, G.J.,
1995. Maturation pattern and recruitment of the squid Loligo
vulgaris Lamarck, 1798 from North Western African coast.
ICES CM 1995/K: 37.
Roberts, M.J., 1998. The inﬂuence of the environment of chokka
squid Loligo vulgaris reynaudii spawning aggregations: steps
towards a quantiﬁed model. S. Afr. J. Mar. Sci. 20, 267–284.
Roper, C.F.E., Sweeney, M.J.C., Naren, C.E., 1984. Cephalopods
of the world. FAO Fisheries Synopsis, No. 125, vol. 3.
Rubec, P.J., Christensen, J.D., Arnold, W.S., Norris, H., Steele, P.,
Monaco, M.E., 1998a. GIS and modelling: coupling habitats to
Florida ﬁsheries. J. Shellﬁsh Res. 17 (5), 1451–1457.
Rubec, P.J., Coyne, M.S., McMichael
Jr, R.H., Monaco, M.E.,
1998b. Spatial methods being developed in Florida to determine
essential ﬁsh habitat. Fisheries 23 (7), 21–25.
Sakurai, Y., Kiyofuji, H., Saitoh, S., Goto, T., Hiyama, Y.,
2000. Changes in inferred spawning areas of Todarodes
paciﬁcus (Cephalopoda: Ommastrephidae) due to changing
environmental conditions. ICES J. Mar. Sci. 57 (1), 24–30.
Smith, W.H.F., Sandwell, D.T., 1997. Global sea ﬂoor topography
from satellite altimetry and ship depth soundings. Science 277,
1956–1962.
Theocharis, A., Georgopoulos, D., Lascaratos, A., Nittis, K., 1993.
Water masses and circulation in the central region of the Eastern
Mediterranean: Eastern Ionian, South Aegean and Northwest
Levantine, 1986–1987. Deep-Sea Res. II 40 (6), 1121–
1142.
Turk, T.A., 1999. Spatial distribution and habitat preferences
of weathervane scallops (Patinopteron caurinus) in the Gulf
of Alaska. In: Abstract Proceedings of the 17th Lowell
Wakeﬁeld Fisheries Symposium on Spatial Processes and
Management of Fish Populations, Anchorage, Alaska, October
1999.
Valavanis,
V.D.,
2002.
Geographic
Information
Systems
in
Oceanography and Fisheries. Taylor & Francis, London.
Valavanis, V.D., Drakopoulos, P., Georgakarakos, S., 1999. A
study of upwellings using GIS. In: Proceedings of Coast
GIS’99 International Conference on GIS and New Advances in
Integrated Coastal Management, Brest, France, 9–11 September
1999.
Valavanis, V.D., Georgakarakos, S., Haralabous, J., 1998. A
methodology for GIS interfacing of marine data. In: Proceedings
of
GIS
PLANET
98’
on
International
Conference
and
Exhibition on Geographic Information, Lisbon, Portugal, 7–11
September 1998. IMERSIVA CD-ROM.
Valavanis, V.D., Georgakarakos, S., Koutsoubas, D., Arvanitidis,
C., Haralabus, J., 2002. Development of a marine information
system for cephalopod ﬁsheries in the Greek Seas (Eastern
Mediterranean). B. Mar. Sci. 71 (2), 867–882.
Varkentin, A.I., Buslov, A.V., Tepnin, O.B., 1999. Characteristics
of spawning and distribution of walleye pollock eggs and larvae
in Western Kamchatka waters. In: Abstract Proceedings of
the 17th Lowell Wakeﬁeld Fisheries Symposium on Spatial
Processes and Management of Fish Populations, Anchorage,
Alaska, October 1999.
Waluda, C.M., Pierce, G.J., 1998. Squid distribution and abundance
in relation to oceanographic conditions. ICES CM 1997/HH:07.
Wood, J.B., Day, C.L., O’Dor, R.K., 2000. CephBase: testing ideas
for cephalopod and other species-level databases. Oceanogr.
13 (3), 14–20.
Wright, P.J., Jensen, H., Tuck, I., 2000. The inﬂuence of sediment
type on the distribution of the lesser sandeel, Ammodytes
marinus. J. Sea Res. 44, 243–256.
Xavier, J.C., Rodhouse, P.G., Trathan, P.N., Wood, A.G., 1999. A
Geographical Information System (GIS) Atlas of cephalopod
distribution in the Southern Ocean. Antarct. Sci. 11, 61–62.
Yanez, R.E., Catasti, V., Barbieri, B.M.A., Bohm, G.S., 1996.
Relationships between the small pelagic resources distribution
and the sea surface temperatures recorded by NOAA satellites
from Chile central zone. Invest. Mar. 24, 107–122.
