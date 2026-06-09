--- 
source: Biological Conservation 2003 Márcia Barbosa.pdf
--- 

Otter (Lutra lutra) distribution modeling at two resolution scales
suited to conservation planning in the Iberian Peninsula
A. Ma´ rcia Barbosa*, Raimundo Real, Jesu´ s Olivero, J. Mario Vargas
Departamento de Biologı´a Animal, Facultad de Ciencias, Universidad de Ma´laga, 29071 Ma´laga, Spain
Received 5 June 2002; received in revised form 8 January 2003; accepted 6 February 2003
Abstract
We used the results of the Spanish Otter Survey of 1994–1996, a Geographic Information System and stepwise multiple logistic
regression to model otter presence/absence data in the continental Spanish UTM 1010-km squares. Geographic situation, indi-
cators of human activity such as highways and major urban centers, and environmental variables related with productivity, water
availability, altitude, and environmental energy were included in a logistic model that correctly classiﬁed about 73% of otter pre-
sences and absences. We extrapolated the model to the adjacent territory of Portugal, and increased the model’s spatial resolution
by extrapolating it to 11-km squares in the whole Iberian Peninsula. The model turned out to be rather ﬂexible, predicting, for
instance, the species to be very restricted to the courses of rivers in some areas, and more widespread in others. This allowed us to
determine areas where otter populations may be more vulnerable to habitat changes or harmful human interventions.
# 2003 Elsevier Ltd. All rights reserved.
Keywords: Otter distribution; Spatial modeling; GIS; Conservation; Iberian Peninsula
1. Introduction
The Eurasian otter (Lutra lutra L., 1758) is a semi-
aquatic territorial carnivore which feeds mainly on
aquatic prey and whose habitat is usually linked to the
existence of relatively clean freshwater, available shelter
(riparian vegetation, rocky structures and others) and
abundant prey (Vega and Valladares, 1996; Ruiz-Olmo
and Delibes, 1998; Trindade et al., 1998). The otter’s
worldwide distribution has shown a sharp decline in the
last decades (Elliot, 1983; MacDonald and Mason,
1983), although a general recovery has been noted in
recent years (Ruiz-Olmo and Delibes, 1998). The spe-
cies’ conservation status has justiﬁed its inclusion in the
List of Rare and Threatened Mammals of the Council
of Europe, in Appendix II of the Berne Convention, in
Appendices II and IV of the Habitat Directive of the
European Union, in Appendix I of the CITES and in
the 2000 IUCN Red List of Threatened Species (Hilton-
Taylor, 2000), where it is classiﬁed as vulnerable.
Iberian otters have some diﬀerences in comparison
with the ones from the rest of Europe: They are smaller
(Valladares et al., 1996; Vega and Valladares, 1996;
Ruiz-Olmo et al., 1998) and, at least in some regions,
have a lower mean number of cubs per litter (Ruiz-
Olmo, 1994). Nevertheless, these diﬀerences do not jus-
tify that they be considered as a separate sub-species
(Delibes, 1990). The otter is classiﬁed as vulnerable in
the Red Book of the Vertebrates of Spain (Blanco and
Gonza´ lez, 1992) and included in Appendix II (species of
special interest) of the Royal Decree 439/90, which reg-
ulates the National Catalogue of Threatened Species. In
Portugal, the otter is classiﬁed as data deﬁcient in the
Red Book of the Vertebrates (S.N.P.R.C.N., 1990);
however, the Portuguese otter survey of 1995 (Trindade
et al., 1998) showed that its situation is very favorable,
its distribution being practically generalized throughout
the country. The Portuguese population of otters is
presently considered one of the most viable in Europe
(Trindade et al., 1998).
Traditionally, investigation on the factors that aﬀect
otter conservation in Spain has been based on small-
scale studies or on local factors such as habitat features
(e.g. Elliot, 1983; Nores et al., 1990, 1991; Bueno and
0006-3207/03/$ - see front matter # 2003 Elsevier Ltd. All rights reserved.
doi:10.1016/S0006-3207(03)00066-1
Biological Conservation 114 (2003) 377–387
www.elsevier.com/locate/biocon
* Corresponding author. Tel.: +34-952-132383; fax: +34-952-
131668.
E-mail address: ambarbosa@uma.es (A.M. Barbosa).


Bravo, 1998). However, as Ricklefs (1987) and Levin
(1992) pointed out, local populations are also likely
aﬀected by historical and environmental processes that
act on a regional or continental scale. The study of
regional-scale processes is, therefore, important to
complement ecological studies carried out on more local
scales (Vaughn and Taylor, 2000).
The large-scale modeling of species’ distributions is
becoming a fundamental tool for ecosystem manage-
ment and biological conservation, as it provides a
broader geographic perspective that works as a context
for local studies. Spatial modeling underwent a great
advance in the last years with the progresses in spatial
statistics and the generalization of the use of Geo-
graphic Information Systems (GIS). These systems,
designed to acquire, store, manipulate, transform, com-
bine, analyze and represent geographically referenced
data, allow for a greater scope and precision in fore-
casting the presence of species in several kinds of geo-
graphical units. With the help of GIS and large-scale
distribution models, conservation programs may have
more satisfactory results as the factors that aﬀect, on a
larger scale, the survival of populations are taken into
account (Corsi et al., 1999).
Two nation-wide otter surveys have been previously
carried out in Spain, the ﬁrst one in 1984–1985 (Delibes,
1990) and the second in 1994–1996 (Ruiz-Olmo and
Delibes, 1998). Barbosa et al. (2001) analyzed the results
of this second survey, assessing the relative contribution
of spatial, environmental and human factors on the
proportion of positive sites of otter in each Spanish
province, but such a study is too coarse to infer the
eventual impact of the construction of a dam or a
transportation infrastructure, for example, on a parti-
cular otter population. Otter surveys can, however, be
used to elaborate distribution models based on presence
probabilities that, when extrapolated to a ﬁner resolu-
tion scale, allow a more detailed knowledge of the spe-
cies’ potential distribution. In this way, conservation
planning might incorporate the identiﬁcation of areas
where otter populations could be more vulnerable to
habitat destruction or fragmentation.
Our aims are to model the distribution of the Eurasian
otter in continental Spain using the UTM 1010-km
squares as territorial units, to check the behavior of the
model when extrapolated to continental Portugal, and to
extrapolate it to a deductive model of otter distribution in
11-km squares in the whole Iberian Peninsula.
2. Methods
2.1. Study area
The Iberian Peninsula, situated at the extreme south-
west of Europe, covers an area of approximately
580,000 km2 and includes the continental territories of
Spain and Portugal. Most of its main mountain ranges
have a marked longitudinal component, so that the
main rivers ﬂow longitudinally to the Atlantic Ocean
and to the Mediterranean Sea. The Mediterranean
watershed is narrower and most of its rivers have a sea-
sonal regimen, whereas the Atlantic watershed is wider
and its rivers have a more abundant and permanent
ﬂow (Bosque and Vila` , 1989). The climate of the Penin-
sula is heterogeneous, with a longitudinal gradient of
precipitation and a latitudinal gradient of both pre-
cipitation and temperature (Capel, 1981). It has a
marked peninsular character, since the isthmus that
connects it with the rest of the continent is relatively
narrow (about two-ﬁfths of its northern boundary) and
is crossed by the Pyrenees, which hinders the biotic and
abiotic interactions with the adjacent territories.
2.2. Distribution data
We recorded otter presence/absence data for each of
the 5187 continental Spanish and 1000 continental Por-
tuguese UTM 1010-km squares. Data on otter dis-
tribution in Spain are the result of the national otter
survey carried out in 1994–1996 (Ruiz-Olmo and
Delibes, 1998) and were converted into presence/
absence data in UTM squares. Data on otter distribu-
tion in Portugal are the result of the national otter sur-
vey carried out by Trindade et al. (1998) in 1995, where
each UTM square was surveyed. Surveyors looked for
otter signs in all kinds of aquatic habitats, including
river and lake shores, narrow streams, drainage ditches,
and dams, for example. The distribution data obtained
are shown in Fig. 1.
2.3. Independent variables
We recorded variables related to environmental con-
ditions, human activity and spatial situation to induce
the factors that aﬀect otter presence. Given that the
processes that account for species’ distribution patterns
are frequently diﬀerent on diﬀerent scales, we only used
a set of variables that hypothetically act on a 11-km
scale as well as on a 1010-km one. We therefore
excluded variables related to habitat heterogeneity or
land roughness such as the altitude range. Surface area
was not considered because the deductive model was to
be based on equal-area 11-km squares. We also cared
not to include variables whose range on a 11-km scale
signiﬁcantly exceeded its range on a 1010-km one, as
was the case of mean slope. The 25 variables used and
their sources are listed in Table 1.
Spatial autocorrelation, which is present in the indepen-
dent variables as well as in the distribution data, can lead
to loss of power of the model as it violates the assumption
of most standard statistical tests that observations are
378
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387


independent (Legendre and Fortin, 1989; Legendre,
1993). Some authors choose to ignore spatial auto-
correlation (Romero and Real, 1996; Brito et al., 1999;
Teixeira et al., 2001), while others attempt to minimize
it by using subsets of non-adjacent samples within the
study area (e.g. Brito et al., 1999). However, Legendre
(1993) argued that spatial structuring should be included
in the models as it is functional in ecosystems, and that the
use of subsets leads, additionally, to a signiﬁcant loss of
information. In the present study, we used all the UTM
1010-km squares in the study area and included spatial
variables in the analysis to take into account the possible
spatial structuring of the distribution data.
We digitized the variables using the CartaLinx 1.2
software and processed them using the Idrisi GIS soft-
ware. Continuous climatic variables were interpolated
from isoline maps with the Idrisi32 TIN and TINSURF
modules performing parabolic bridge and tunnel edge
removal. We then obtained mean values of the variables
for each UTM 1010-km square, using the digital
UTM grid maps obtained from the A´ rea de Defensa
Contra Incendios Forestales (DGCN, Ministerio de
Medio Ambiente) (Spain) and the Laborato´ rio de Car-
tograﬁa Biolo´ gica da Universidade de E´ vora (Portugal).
2.4. Statistical analyses
The potential distribution area of a species relates its
presence to certain conditioning factors (Bustamante,
1997). Several methods allow for the determination of
potential distribution areas, some of them in terms of
probability of occurrence of the species in each geo-
graphic unit (Brito et al., 1999; Teixeira et al., 2001). In
the present work we used multiple logistic regression
(Hosmer and Lemeshow, 1989), a technique widely used
in the spatial modeling of species’ distributions (e.g. Dec-
arie et al., 1995; Romero and Real, 1996; Franco et al.,
2000; Kleinschmidt et al., 2000), including the otter
(Kemenes and Demeter, 1994; Madsen and Prang, 2001).
It produces a probabilistic model that predicts a binary
dependent variable, as is the case of presence/absence
data, from a set of discrete or continuous independent
variables. The logistic regression model has the form
P ¼
ey
1 þ ey
ð1Þ
where P is the probability of occurrence of the species, e
is the basis of the Napierian logarithm, and y is a
regression equation in the form
Fig. 1. Otter Lutra lutra distribution based on UTM 1010-km squares in Spain (A) and in Portugal (B). Black squares represent otter presences.
(A: source data taken from Ruiz-Olmo and Delibes, 1998; B: adapted from Trindade et al., 1998).
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387
379


y ¼ 0 þ 1x1 þ 2x2 þ . . . þ nxn
ð2Þ
where 0 is a constant and 1, 2, . . ., n are the coeﬃ-
cients of the n independent variables x1, x2, . . ., xn that
signiﬁcantly aﬀect the probability of occurrence of the
species (Tabachnick and Fidell, 1996).
By deﬁnition, the logistic function is symmetric and
its inﬂection point corresponds to a P value of 0.5,
which is usually used as a cut-oﬀpoint, or probability
threshold, above which to assume the species’ presence.
In this way, we can classify a square as presence or
absence according to the model. Misclassiﬁcation can
happen due to reduced sensitivity or speciﬁcity of the
model, sensitivity being the ability of the model to cor-
rectly classify the species’ presences, and speciﬁcity
referring to the correct classiﬁcation of absences (Brito
et al., 1999). However, when the number of presences in
the study area is diﬀerent from that of absences, the
logistic regression within the function’s domain is not
symmetrical, but rather deviates towards the extreme
that presents a greater number of cases. In these situa-
tions, there is a disagreement between the logistic func-
tion and the species’ response to the environmental
conditions (Rojas et al., 2001). The value 0.5 is indeed
the probability threshold above which the species is
more likely to be present than it is to be absent, but does
not necessarily correspond to the environmental thresh-
old above which the species is more likely to be present
than expected at random (i.e. than expected considering
the proportion of presences in the study area).
We represented the correct classiﬁcation rates (CCR)
for presences and for absences at all possible cut-oﬀ
points between 0 and 1 with intervals of 0.1, so obtain-
ing two graphics that cross at the threshold where the
same proportion of presences and absences are correctly
classiﬁed. We could also represent the CCR for all the
squares, regardless of whether they are presences or
absences, and choose the probability threshold where
this percentage is highest (Brito et al., 1999; Franco et
al., 2000). However, the total CCR of a model is more
aﬀected by the CCR of the predominant class, in this
case absences, and this does not take into account that
sensitivity should be given more importance than speci-
ﬁcity, since presences have been conﬁrmed while absen-
ces can be due to incomplete or ineﬀective sampling. We
opted for representing the average between sensitivity
and speciﬁcity and choosing, as the probability thresh-
old, its highest value among the ones that correctly
classify at least as much presences as absences (Rojas et
al., 2001). We also evaluated the validity of the model in
Portugal by checking its sensitivity and speciﬁcity in this
country at this probability threshold.
Table 1
Variables used to model otter distribution in Spain
Code
Variable
HJN
Mean relative air humidity in January at 07:00 h (%) (1)
HJL
Mean relative air humidity in July at 07:00 h (%) (1)
HR
Annual relative air humidity range (%) (= HJN-HJL
j
j)
PET
Mean annual potential evapotranspiration (mm) (1)
AET
Mean annual actual evapotranspiration (mm) (=min[PET, P])
I
Mean annual insolation (h/year) (1)
SR
Mean annual solar radiation (kwh/m2/day) (1)
TJN
Mean temperature in January (C) (1)
TJL
Mean temperature in July (C) (1)
T
Mean annual temperature (C) (1)
TR
Annual temperature range (C) (=TJL-TJN)
DF
Mean annual number of frost days (minimum temperature 40 C) (1)
DP
Mean annual number of days with precipitation 50.1 mm (1)
P
Mean annual precipitation (mm) (1)
MP24
Maximum precipitation in 24 h (mm) (1)
RMP
Relative maximum precipitation (=MP24/P)
PI
Pluviometric irregularity (2)
RO
Mean annual run-oﬀ(mm) (3)
SP
Soil permeability (3)
A
Mean altitude (m) (4)
DH
Distance to the nearest highway (km) (5)
D100
Distance to the nearest town with more than 100,000 inhabitants (km) (5)
D500
Distance to the nearest town with more than 500,000 inhabitants (km) (5)
LA
Mean latitude (N) (5)
LO
Mean longitude (W) (5)
Sources: (1) Font (1983). (2) Spain: Montero de Burgos and Gonza´ lez-Rebollar (1974). (3) Spain: I.G.M.E. (1979), Portugal: http://snig.cnig.pt/snig/
framemg.htm; (4) http://www.etsimo.uniovi.es/feli/data/datos.html(5) I.G.N. (1999). Data on the number of inhabitants of the urban centers were
taken from the Instituto Nacional de Estadı´stica (http://www.ine.es) for Spain and from the Enciclope´ dia Universal (http://www.universal.pt) for
Portugal.
380
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387


The regression equation was then introduced in the
Idrisi Image Calculator and used to create an image
representing otter presence probability for the whole
Iberian Peninsula in 11-km squares, since the inde-
pendent variables were represented with approximately
this spatial resolution.
3. Results and discussion
3.1. Fit of the model to the observed distribution
Otter presence probability values in each continental
Spanish UTM 1010-km square, according to the
logistic function obtained (Fig. 2), are represented in
Fig. 3. As can be seen by comparing Figs. 1 and 3, the
predictions of the model closely match the distribution
data available for Spain, since neither high probabilities
were predicted in large areas where otters are absent
from nor low probabilities appear in areas with con-
spicuous otter presence. The sensitivity and speciﬁcity of
the classiﬁcations at each cut-oﬀpoint are presented in
Fig. 4. The best cut-oﬀpoint corresponds to the P value
0.29, where approximately 73% of the presences and
absences are correctly classiﬁed.
When extrapolated to Portugal (Fig. 5), the Spanish
model has, at the 0.29 probability threshold, a high
sensitivity (approximately 98%) and a low speciﬁcity
(ca. 8%; Fig. 6), i.e. otters are predicted to be present in
the vast majority of the continental Portuguese UTM
1010-km squares. Consequently, otter absences in
Portugal are probably due to non-analyzed factors such
as water pollution or food availability.
3.2. The selected factors
For an eﬀective conservation strategy, it is essential to
determine which factors may be aﬀecting the present
populations of otters on a broad scale (MacDonald and
Mason, 1983; Antu´ nez and Mendoza, 1992). The model
obtained seems to hold a high predictive potential,
which probably indicates that most of the important
factors are taken into account. However, as this is a
statistical model that was not designed to select between
alternative explanatory hypotheses of otter distribution,
some of the included variables (Table 2) might act as
surrogates of other important factors not explicit in the
logistic function. Factors such as water pollution or
food availability, for example, were not available on
UTM 1010-km squares, but the eﬀects of distance to
main cities or water availability could be partially
explained by them.
Spatial autocorrelation seems to be important in the
distribution of the otter in the Spanish UTM 1010-km
squares, since geographic longitude is the ﬁrst variable
to enter the model, with the highest partial correlation
coeﬃcient with otter presence, and latitude is also
included (Table 2). The longitudinal gradient in the dis-
tribution of the otter in Spain was noted by Elliot (1983)
and by Delibes and Rodrı´guez (1990), who found that
otters are more common in the western than in the
eastern half of the country. This trend continues
towards Portugal, where otter presence was conﬁrmed
in nearly 90% of the UTM 1010 km squares (Trin-
dade et al., 1998; Fig. 1).
Spatial autocorrelation in the distribution of a species
may result from the inﬂuence of environmental and
human factors that are also spatially autocorrelated
(Legendre and Fortin, 1989; Borcard et al., 1992), or
from processes that are inherent to its own population
dynamics (e.g. contagious biotic processes such as
reproduction,
migration,
and mortality) (Legendre,
1993). Barbosa et al. (2001) found that 45.6% of the
variation in the proportion of positive sites of otter in
the Spanish provinces was explained by geographic
longitude, and attributed 18% of this variation to pure
longitudinal structuring related to otter population
dynamics. According to this interpretation, an otter
population can only expand to its surrounding area,
whereas areas with adequate conditions for the species
will not be naturally colonized if there are no otter
populations nearby (Ruiz-Olmo and Delibes, 1998),
thus producing a purely spatial structuring in otter dis-
tribution. The mainly longitudinal character of this
spatial structure may be due to the fact that most of the
main Iberian rivers ﬂow westward.
The increase of otter presence probability with the
distance to major urban centers and to highways points
to the negative inﬂuence of these indicators of human
activity on this species. The proximity to major towns is
often suggested as harmful for otters, especially due to
the water contamination they generate downstream
(Delibes and Rodrı´guez, 1990; Ruiz-Olmo and Delibes,
1998). This urban contamination included PCBs, which
are industrially-used organochlorine compounds (Jeﬀ-
Fig. 2. Logistic function resulting from stepwise regression of otter
presence/absence data in the UTM 1010-km squares of continental
Spain on the variables listed in Table 1. P: otter presence probability;
y: regression equation whose variables and coeﬃcients are shown in
Table 2.
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387
381


eries and Hanson, 2002) and have been reported to
contribute to the otter decline in Spain (Ruiz-Olmo and
Delibes, 1998; Ruiz-Olmo et al., 2002).
The use of organochlorine pesticides in agriculture
has also been reported as a major cause of the decline in
otter populations (Gutleb, 2002; Jeﬀeries and Hanson,
2002; Ruiz-Olmo and Delibes, 1998; Ruiz-Olmo et al.,
Fig. 3. Otter presence probability in each UTM 1010-km square of continental Spain, according to the logistic regression model obtained.
Fig. 4. Correct classiﬁcation rates (CCR) for the model applied to the
Spanish territory at all possible cut-oﬀpoints at 0.1 intervals.
Fig. 5. Otter presence probability in UTM 1010-km squares of con-
tinental Portugal, according to the logistic regression model obtained
for Spain.
382
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387


2002). The inclusion of variables more directly related
to this factor, such as arable land and density of live-
stock, would perhaps be desirable. However, such vari-
ables are not available at a national scale neither in
1010-km nor in 11-km squares. In any case, Barbosa
et al. (2001), using administrative provinces as territor-
ial units, included cropland area and pasture area in a
stepwise regression procedure that did not select any of
these among a set of human-related variables. This
could indicate that in Spain industrial rather than agri-
cultural contamination aﬀects otter distribution, which
is in accordance with the ﬁndings of Lo´ pez-Martı´n and
Ruiz-Olmo (1996) that the mainly industrially-used
PCBs reach higher concentration levels in Spanish otter
tissues than other agriculturally used organochlorines.
The negative association with highways can be due
not only to road casualties suﬀered by the species, but
also to indirect eﬀects such as air and water pollution,
noise, habitat destruction and fragmentation, and arti-
ﬁcial lighting, for example (see Spellerberg, 1998). Bar-
bosa et al. (2001) found that highway density explained
28.1% of the variance in the proportion of positive sites
of otter in the Spanish provinces.
Actual
evapotranspiration
indicates
simultaneous
availability of water and energy, thus being a good pre-
dictor of productivity (Major, 1963; Rosenzweig, 1968;
Wright, 1983), which seems to have a positive inﬂuence
on otter distribution. July temperature may also be
related to this factor, since high values of temperature in
ecosystems with high water availability during summer,
such as those in the Atlantic watershed, allow a greater
productivity (Rosenzweig, 1968), which usually leads to
greater food availability. On the other hand, in Medi-
terranean environments, where most rivers usually dry up
in summer leaving only spaced pools, relatively high tem-
peratures lead to a moderate eutrophy allowing a relative
abundance of crayﬁsh, amphibians, insects, and some
species of cyprinids that can temporarily provide food for
the otter (Jime´ nez and Delibes, 1990; Ruiz-Olmo and
Delibes, 1998). Gue´ gan et al. (1998) found that net pri-
mary productivity strongly inﬂuences global-scale species
richness of riverine ﬁsh, the otter’s main prey item.
The positive relation of otter presence with mean
January temperature indicates that, once we have taken
into account the factors previously included in the
model, otter presence probability is higher in areas with
cold winters. January temperature may be a surrogate
for other factors that have a more direct inﬂuence on
otter distribution: low January temperatures usually
correspond to regions with snowy winters; snow can
work as a natural regulator of streams, as the defrosting
assures water availability when temperature increases,
even in the absence of precipitation. The positive inﬂu-
Fig. 6. Correct classiﬁcation rates (CCR) for the Spanish model
applied to continental Portugal at all possible cut-oﬀpoints at 0.1
intervals.
Table 2
Variables included in the model and their coeﬃcients (), standard errors (S.E.), partial correlation coeﬃcients (R), Wald test values (Wald, 1943)
and signiﬁcance (P). The variables are ranked according to their order of entrance in the model. Variable codes as in Table 1
Variable

S.E.
R
Wald
P
LO
	0.2705
0.0191
	0.1780
200.7216
0.0000
D100
0.0034
0.0014
0.0241
5.6296
0.0177
AET
0.0039
0.0004
0.1261
101.7620
0.0000
TJN
	0.1637
0.0503
	0.0370
10.5924
0.0011
DH
0.0112
0.0018
0.0757
37.9469
0.0000
A
	0.0010
0.0002
	0.0455
14.9769
0.0001
SR
0.0170
0.0023
0.0908
53.7026
0.0000
LA
0.2664
0.0588
0.0544
20.5307
0.0000
D500
0.0031
0.0008
0.0489
16.9962
0.0000
P
0.0006
0.0002
0.0422
13.1742
0.0003
SP
	00.1353
0.0489
	0.0300
7.6473
0.0057
HJL
0.0267
0.0065
0.0484
16.7091
0.0000
TJL
0.1483
0.0364
0.0482
16.5676
0.0000
T
	0.1301
0.0599
	0.0208
4.7109
0.0300
Constant
	25.5063
3.6186
–
49.6849
0.0000
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387
383


ence of annual precipitation and July air humidity and
the negative inﬂuence of soil permeability on otter
presence probability also point to the importance of
water availability for this species. Both precipitation
and permeability were previously related by other
authors with otter distribution in Spain: Delibes and
Rodrı´guez (1990), analyzing the results of the Spanish
otter survey of 1984–1985, suggested a relationship
between otter distribution and mean annual precipita-
tion; Nores et al. (1991) in the province of Asturias
(Northern Spain) and Barbosa et al. (2001) found that
the proportion of otter presences was signiﬁcantly
higher in areas located on impermeable than on perme-
able substrate, which they attributed to the diﬀerence in
superﬁcial freshwater availability. The abundance of
water does not only mean better habitat conditions or
greater food availability. Pollutant concentrations in
water, and hence their detrimental eﬀect on otter popu-
lations, also depend on the amount of water available.
PCBs were considered not to have been major causal
agents in the otter decline in Britain (Jeﬀeries and Han-
son, 2001), where the climate is wet, but they were repor-
ted
to have
had
strong negative eﬀects on
otter
distribution in eastern Spain (Ruiz-Olmo and Delibes,
1998; Ruiz-Olmo et al., 2002), where water is scarce espe-
cially during summer.
The negative relation of otter presence probability
with altitude can be due to the lack of prey in the oli-
gotrophic high mountain waters, as Ruiz-Olmo and
Delibes (1998) suggested.
Solar radiation is an indicator of energy availability. Its
positive relation with otter presence probability might
indicate that otter populations are favored in areas with
high values of environmental energy, where it might be
easier to satisfy their physiological requirements (see
Hutchinson, 1959; Brown, 1981; Wright, 1983). The nega-
tive relation of mean annual temperature with otter pre-
sence probability may indicate a marginal inﬂuence of
climatic stress on this species, which may act as a coun-
terbalance for the positive eﬀect of energy availability.
Fig. 7. Otter presence probability in 11-km squares in the Iberian Peninsula, according to the model obtained for continental Spain.
384
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387


3.3. Extrapolation to a 11-km resolution
The extrapolation of the model to 11-km squares
provided a much higher spatial resolution in the pre-
dictions about otter distribution (Fig. 7). In Fig. 8 we
represent, with more detail, four diﬀerent regions of the
Peninsula. As can be seen in Fig. 8A, which represents
the northern Iberian plateau (mean elevation >700 m)
and its surroundings, otter presence probability increa-
ses in mountainous areas regardless of whether they are
more (as in Spain) or less elevated (as in Portugal) than
the plateau. This could be due, among other causes, to
the usual increase in precipitation and scarcity of
human activity in mountainous environments. In some
mountain ranges the probability map reproduces the
courses of rivers, i.e. the model predicts higher occur-
rence probabilities along them than in their surround-
ings. In Figs. 8B and C we represent the regions
corresponding to the central Pyrenees (northeast) and
the mountains of Ronda (S Spain), where the prob-
ability along rivers stands out against that of their
adjacent areas. The same model predicts, on the other
hand, that in the northwestern section of the Peninsula
(Fig. 8D) otters are more widespread, apparently not
being limited to the courses of the main rivers. During
the Spanish otter survey of 1994–1996, this region had,
in fact, the most widespread distribution of positive sites
of otter (see Ruiz-Olmo and Delibes, 1998). This can be
due to the abundance of superﬁcial freshwater in this
part of the Peninsula, where small streams are common
all over the territory.
3.4. Applications for conservation
Presence probability values can be used to deﬁne
favorable or unfavorable areas for a species, which
could be taken into account when implementing speciﬁc
conservation programs. For example, areas where the
Fig. 8. Otter presence probability in 11-km squares in four diﬀerent regions of the Peninsula. A: Northern Iberian plateau and its surroundings; B:
Central Pyrenees; C: Mountains of Ronda; D: Northwest of the Peninsula.
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387
385


probability of presence is four times higher than that of
absence could be considered as environmentally favor-
able and areas where the probability of absence is four
times higher than that of presence could be considered
as environmentally unfavorable for a species. Deter-
mining a cut-oﬀpoint above which the species is more
likely to be present than expected at random can be
useful to correct the probability thresholds deﬁning
these favorable or unfavorable areas (Rojas et al.,
2001). The fact that the cut-oﬀpoint for the otter is
lower than 0.5 indicates that it is probably necessary to
lower the probability values considered for determining
favorable or unfavorable areas for this species in Spain.
The use of GIS for the modeling of otter distribution
on a 11-km resolution starting from presence/absence
data on 1010-km squares allowed for a substantial
increase in detail in the knowledge on this species’
potential distribution. This has implications in the
management of ecosystems and the planning of the
construction of infrastructures potentially harmful for
otter populations, such as industrial, urban or tourist
settlements, transportation infrastructures, and dams,
for example. Since otters are territorial, an otter popu-
lation needs a considerable longitude of suitable habitat
to keep a number of individuals large enough to main-
tain its viability. In areas where otter presence is
restricted to the main course of a river and there is no
connection with a nearby suitable territory, any inter-
vention in the river is more likely bound to fragment the
local otter population and could make it become non-
viable. On the other hand, in regions where otter pre-
sence probability is also high outside the main courses
of rivers, otters are predicted to have a greater mobility
along the territory. An obstacle in the river would,
therefore, cause less damage to the local population, as
the individuals would still be able to keep in contact and
dislodged individuals would have a better chance of
getting to another suitable habitat.
Acknowledgements
We are grateful to P. Segurado and S. Weykam for
sending us the digitized UTM 1010-km grids of Por-
tugal and Spain, to A.M. Felicı´simo for the transformed
DEM of the Iberian Peninsula, and to C. Nores, J.
Ruiz-Olmo, R. Sa´ nchez and H. Sainz Ollero for their
valuable suggestions. A. M. Barbosa received support
(grant SFRH/BD/4601/2001) from Fundac¸ a˜ o para a
Cieˆ ncia e a Tecnologia, Portugal.
References
Antu´ nez, A., Mendoza, M., 1992. Factores que determinan el a´ rea de
distribucio´ n geogra´ ﬁca de las especies: conceptos, modelos y me´ to-
dos de ana´ lisis. In: Vargas, J.M., Real, R., Antu´ nez, A. (Eds.),
Objetivos y Me´ todos Biogeogra´ ﬁcos. Aplicaciones en Herpetologı´a,
Monogr. Herpetol. 2, pp. 51–72.
Barbosa, A.M., Real, R., Ma´ rquez, A.L., Rendo´ n, M.A., 2001. Spa-
tial, environmental and human inﬂuences on the distribution of
otter (Lutra lutra) in the Spanish provinces. Diversity and Distribu-
tions 7, 137–144.
Blanco, J.C., Gonza´ lez, J.L. (Eds.), 1992. Libro Rojo de los Verteb-
rados de Espan˜ a. Coleccio´ n Te´ cnica, Ministerio de Agricultura,
Pesca y Alimentacio´ n/ICONA, Madrid.
Borcard, D., Legendre, P., Drapeau, P., 1992. Partialling out the
spacial component of ecological variation. Ecology 73, 1045–
1055.
Bosque, J., Vila` , J. (Eds.), 1989. Geografı´a de Espan˜ a. Planeta, Bar-
celona.
Brito, J.C., Crespo, E.G., Paulo, O.S., 1999. Modelling wildlife dis-
tributions: Logistic Multiple Regression vs Overlap Analysis. Eco-
graphy 22, 251–260.
Brown, J.H., 1981. Two decades of homage to Santa Rosalia: toward
a general theory of diversity. American Zoologist 21, 877–888.
Bueno, F., Bravo, C., 1998. Comentarios sobre la evolucio´ n de las
poblaciones de nutria (Lutra lutra) en dos zonas del centro de
Espan˜ a. Galemys 10 (NE), 151–159.
Bustamante, J., 1997. Predictive models for lesser kestrel Falco nau-
manni distribution, abundance and exctinction in southern Spain.
Biological Conservation 80, 153–160.
Capel, J.J., 1981. Los climas de Espan˜ a. Oikos-Tau, S.A.—ediciones,
Barcelona.
Corsi, F., Dupre` , E., Boitani, L., 1999. A large-scale model of wolf
distribution in Italy for conservation planning. Conservation Biol-
ogy 13, 150–159.
Decarie, R., Morneau, F., Lambert, D., Carriere, S., Savard, J.P.L.,
1995. Habitat use by brood-rearing waterfowl in sub-arctic Quebec.
Arctic 48, 383–390.
Delibes, M., 1990. Introduccio´ n a la problema´ tica de la nutria en
Espan˜ a. In: Delibes, M. (Ed.), La Nutria (Lutra lutra) en Espan˜ a.
Serie Te´ cnica, Ministerio de Agricultura, Pesca y Alimentacio´ n /
ICONA, Madrid, pp. 5–7.
Delibes, M., Rodrı´guez, A., 1990. La situacio´ n de la nutria en Espan˜ a:
una sı´ntesis de los resultados. In: Delibes, M. (Ed.), La Nutria
(Lutra lutra) en Espan˜ a. Serie Te´ cnica, Ministerio de Agricultura,
Pesca y Alimentacio´ n / ICONA, Madrid, pp. 157–167.
Elliot, K.M., 1983. The otter (Lutra lutra) in Spain. Mammal Review
13, 25–34.
Font, I., 1983. Atlas clima´ tico de Espan˜ a. Instituto Nacional de
Meteorologı´a, Madrid.
Franco, A.M.A., Brito, J.C., Almeida, J., 2000. Modelling habitat
selection of common cranes Grus grus wintering in Portugal using
multiple logistic regression. Ibis 142, 351–358.
Gue´ gan, J.-F., Lek, S., Oberdorﬀ, T., 1998. Energy availability and
habitat heterogeneity predict global riverine ﬁsh diversity. Nature
391, 382–384.
Gutleb, A.C., 2002. The role of pollutants in the decline of the otter.
In: Conroy, J.W.H., Yoxon, P., Gutleb, A.C. (Eds.), Proceedings of
the First Otter Toxicology Conference. Journal of the International
Otter Survival Fund, No 1. Skye, September 2000. International
Otter Survival Fund, Broadford, Scotland, pp. 29–40.
Hilton-Taylor, C. (compiler), 2000. 2000 IUCN Red List of Threa-
tened Species. IUCN, Gland, Switzerland and Cambridge, UK.
Hosmer, D.W., Lemeshow, S., 1989. Applied Logistic Regression.
John Wiley and Sons, Inc, New York.
Hutchinson, G.E., 1959. Homage to Santa Rosalia. or why are there
so many kinds of animals? American Naturalist 93, 145–159.
I.G.M.E, 1979. Mapa hidrogeolo´ gico Nacional. Explicacio´ n de los
mapas de lluvia u´ til, de reconocimiento hidrogeolo´ gico y de sı´ntesis
de los sistemas acuı´feros, 2a ed. Instituto Geolo´ gico y Minero de
Espan˜ a, Madrid.
I.G.N., 1999. Mapa de carreteras. Penı´nsula Ibe´ rica, Baleares y
386
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387


Canarias. Instituto Geogra´ ﬁco Nacional/Ministerio de Fomento,
Madrid.
Jeﬀeries, D.J., Hanson, H.M., 2002. The role of dieldrin in the decline
of the otter (Lutra lutra) in Britain: the analytical data. In: Conroy,
J.W.H., Yoxon, P., Gutleb, A.C. (Eds.), Procceedings of the First
Otter Toxicology Conference. Journal of the International Otter
Survival Fund, No 1. Skye, September 2000. International Otter
Survival Fund, Broadford, Scotland, pp. 95–143.
Jime´ nez, J., Delibes, M., 1990. Causas de la rariﬁcacio´ n. In: Delibes,
M. (Ed.), La Nutria (Lutra lutra) en Espan˜ a. Serie Te´ cnica, Minis-
terio de Agricultura, Pesca y Alimentacio´ n / ICONA, Madrid, pp.
169–177.
Kemenes, I., Demeter, A., 1994. Uni- and multivariate analyses of the
eﬀects of environmental factors on the occurrence of otters (Lutra
lutra) in Hungary. Annls hist.-nat. Mus. natn. hung 86, 133–138.
Kleinschmidt, I., Bagayoko, M., Clarke, G.P.Y., Craig, M., Lesueur,
D., 2000. A spatial statistical approach to malaria mapping. Inter-
national Journal of Epidemiology 29, 355–361.
Legendre, P., 1993. Spacial autocorrelation: trouble or new paradigm?
Ecology 74, 1659–1673.
Legendre, P., Fortin, M.-J., 1989. Spatial pattern and ecological ana-
lysis. Vegetatio 80, 107–138.
Levin, S.A., 1992. The problem of pattern and scale in ecology. Ecol-
ogy 73, 1943–1967.
Lo´ pez-Martı´n, J.M., Ruiz-Olmo, J., 1996. Organochlorine residue
levels and bioconcentration factors in otters (Lutra lutra L.) from
North-East Spain. Bulletin of Environmental Contamination and
Toxicology 57, 532–535.
MacDonald, S.M., Mason, C.F., 1983. Some factors inﬂuencing the
distribution of otters (Lutra lutra). Mammal Review 13, 1–10.
Madsen, A.B., Prang, A., 2001. Habitat factors and the presence or
absence of otters Lutra lutra in Denmark. Acta Theriologica 46,
171–179.
Major, J., 1963. A climatic index to vascular plants activity. Ecology
44, 485–498.
Montero de Burgos, J.L., Gonza´ lez-Rebollar, J.L., 1974. Diagramas
bioclima´ ticos. ICONA, Madrid.
Nores, C., Herna´ ndez-Palacios, O., Garcı´a-Gaona, J.F., Naves, J.,
1990. Distribucio´ n de sen˜ ales de nutria (Lutra lutra) en el medio
riberen˜ o Canta´ brico en relacio´ n con los factores ambientales.
Revista de Biologı´a de la Universidad de Oviedo 8, 107–117.
Nores, C., Garcı´a-Gaona, J.F., Herna´ ndez-Palacios, O., Naves, J.,
1991. Distribucio´ n y estado de conservacio´ n de la nutria (Lutra
lutra) en Asturias. Ecologı´a 5, 257–264.
Ricklefs, R.E., 1987. Community diversity: relative roles of local and
regional processes. Science 235, 167–171.
Rojas, A.B., Cotilla, I., Real, R., Palomo, L.J., 2001. Determinacio´ n
de las a´ reas probables de distribucio´ n de los mamı´feros terrestres en
la provincia de Ma´ laga a partir de las presencias conocidas. Gal-
emys 13 (NE), 217–229.
Romero, J., Real, R., 1996. Macroenvironmental factors as ultimate
determinants of the distribution of common toad and netterjack
toad in the south of Spain. Ecography 19, 305–312.
Rosenzweig, M.L., 1968. Net primary productivity of terrestrial com-
munities: prediction from climatological data. American Naturalist
102, 67–74.
Ruiz-Olmo, J., 1994. Reproduccio´ n y observacio´ n de grupos de nutria
(Lutra lutra L.) en el Norte de Espan˜ a. Miscel.la` nia Zoolo` gica 17,
225–229.
Ruiz-Olmo, J., Delibes, M., Zapata, S.C., 1998. External morpho-
metry, demography and mortality of the Otter Lutra lutra (Linneo,
1758) in the Iberian Peninsula. Galemys 10 (NE), 239–251.
Ruiz-Olmo, J., Delibes, M. (Eds.), 1998. La nutria en Espan˜ a ante el
horizonte del an˜ o 2000. Sociedad Espan˜ ola para la Conservacio´ n y
Estudio de los Mamı´feros, Ma´ laga, Spain.
Ruiz-Olmo, J., Lafontaine, L., Prignioni, C., Lo´ pez-Martı´n, J.M.,
Santos-Reis, M., 2002. Pollution and its eﬀects on otter populations
in South-Western Europe. In: Conroy, J.W.H., Yoxon, P., Gutleb,
A.C. (Eds.), Procceedings of the First Otter Toxicology Conference.
Journal of the International Otter Survival Fund, No 1. Skye, Sep-
tember 2000. International Otter Survival Fund, Broadford, Scot-
land, pp. 63–82.
S.N.P.R.C.N., 1990. Livro Vermelho dos Vertebrados de Portugal.
Volume I: Mamı´feros, Aves, Re´ pteis e Anfı´bios. Secretaria de
Estado do Ambiente e Defesa do Consumidor, Lisbon.
Spellerberg, I., 1998. Ecological eﬀects of roads and traﬃc: a literature
review. Global Ecology and Biogeography Letters 7, 317–333.
Tabachnick, B.G., Fidell, L.S., 1996. Using multivariate analysis, third
ed.. HarperCollins College Publishers, Northridge CA.
Teixeira, J., Ferrand, N., Arntzen, J.W., 2001. Biogeography of the
golden-striped salamander, Chioglossa lusitanica: a ﬁeld survey and
spatial modelling approach. Ecography 24, 618–623.
Trindade, A., Farinha, N., Floreˆ ncio, E., 1998. A distribuic¸ a˜ o da lon-
tra Lutra lutra em Portugal—situac¸ a˜ o em 1995. ICN, Lisbon.
Valladares, M.A., Ruiz-Olmo, J., Vega, I., 1996. Rios vivos para a
lontra. Perfecto bioindicador dos nosos rios. Natureza Galega 26,
10–18.
Vaughn, C.C., Taylor, C.M., 2000. Macroecology of a host-parasite
relationship. Ecography 23, 11–20.
Vega, I., Valladares, M.A. (Eds.), 1996. Rı´os vivos para la nutria.
WWF/Adena, Madrid.
Wald, A., 1943. Tests of statistical hypotheses concerning several
parameters with applications to problems of estimation. Transac-
tions of the American Mathematical Society 54, 426–482.
Wright, G.H., 1983. Species-energy theory: an extension to species-
area theory. Oikos 41, 496–506.
A.M. Barbosa et al. / Biological Conservation 114 (2003) 377–387
387
