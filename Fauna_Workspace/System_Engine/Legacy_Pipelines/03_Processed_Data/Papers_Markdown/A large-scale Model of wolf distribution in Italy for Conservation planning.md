--- 
source: A large-scale Model of wolf distribution in Italy for Conservation planning.pdf
--- 

Society for Conservation Biology
A Large-Scale Model of Wolf Distribution in Italy for Conservation Planning
Author(s): Fabio Corsi, Eugenio Duprè, Luigi Boitani
Source: Conservation Biology, Vol. 13, No. 1 (Feb., 1999), pp. 150-159
Published by: Blackwell Publishing for Society for Conservation Biology
Stable URL: http://www.jstor.org/stable/2641574
Accessed: 16/08/2010 08:44
Your use of the JSTOR archive indicates your acceptance of JSTOR's Terms and Conditions of Use, available at
http://www.jstor.org/page/info/about/policies/terms.jsp. JSTOR's Terms and Conditions of Use provides, in part, that unless
you have obtained prior permission, you may not download an entire issue of a journal or multiple copies of articles, and you
may use content in the JSTOR archive only for your personal, non-commercial use.
Please contact the publisher regarding any further use of this work. Publisher contact information may be obtained at
http://www.jstor.org/action/showPublisher?publisherCode=black.
Each copy of any part of a JSTOR transmission must contain the same copyright notice that appears on the screen or printed
page of such transmission.
JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of
content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms
of scholarship. For more information about JSTOR, please contact support@jstor.org.
Blackwell Publishing and Society for Conservation Biology are collaborating with JSTOR to digitize, preserve
and extend access to Conservation Biology.
http://www.jstor.org


A 
Large-Scale 
Model 
of 
Wolf 
Distribution 
in 
Italy 
for 
Conservation 
Planning 
FABIO CORSI,* EUGENIO DUPRE,t AND LUIGI BOITANItt 
*Istituto Ecologia Applicata, Via L. Luciani 41, 00197-Roma, Italy 
tDip. Biologia Animale e Uomo, Viale Universita 32, 00185-Roma, Italy 
Abstract: The 400-500 wolves currently living in the Apennine range of peninsular Italy are slowly recolo- 
nizing the Alps and are expected to move northward. A nationwide management plan for the Italian wolf 
population is being prepared, and a zoning system with connecting corridors has been suggested. We devel- 
oped a large-scale probabilistic model of wolf distribution as a contribution to the planning process. Thirteen 
environmental variables related to wolf needs and human presence were analyzed in 12 well-studied wolf 
territories and in 100 areas where the species has been absent for the past 25 years. These two areas were 
used as a training set in a discriminant analysis to evaluate potential wolf presence throughout the entire 
country. We used the Mahalanobis distance statistic as an index of environmental quality, calculated as the 
distance from the average environmental conditions of the wolf territories. Based on the Mahalanobis dis- 
tance statistics, we constructed an actual and potential spatial distribution of the wolffor all ofpeninsular It- 
aly. The jackknife procedure was used to assess the stability of the distance model and showed good confi- 
dence in our model (coefficient of variation ? 13%). Distance from the wolf territories' centroid as an index 
of environmental quality for the wolf was tested using 287 locations where wolves have been found dead in 
the past 25 years as a consequence of human action (poison, shotgun, car accidents). A useful contribution to 
conservation planning resulted from comparing the frequency distribution of the Mahalanobis distance of 
the dead wolf locations with the percentage of study area within each distance class. This showed how the 
number of wolf casualties would greatly decrease with protection of only a minor part of the study area and 
indicated the usefulness of our approach for evaluation of other conservation options, such as core areas and 
corridor identification. 
Modelo de Larga Escala de la Distribuci6n de Lobos en Italia para la Planeaci6n de la Conservaci6n 
Resumen: Los 400-500 lobos que viven en el rango Apennine de la Italia peninsular estan recolonizando 
lentamente los Alpes y se espera que se muevan hacia el Norte. Se ha preparado un plan de manejo nacional 
para la poblaci6n de lobos en Italia y se ha sugerido un sistema de zonaci6n con corredores conectivos. De- 
sarrollamos un modelo probabilistico de gran escala de la distribuci6n de lobos como una contribuci6n al 
proceso de planeaci6n. Trece variables ambientales relacionadas con las necesidades de los lobos y la presen- 
cia de humanosfueron analizadas en 12 bien estudiados territorios de lobos y en 100 areas donde la especie 
ha estado ausente en los ultimos 25 afnos. Estas dos areasfueron usadas como prueba en un analisis discrim- 
inantepara evaluar elpotencial de la presencia de lobos a lo largo de todo elpais. Utilizamos la distancia es- 
tadistica de Mahalanobis como un indice de calidad ambiental, calculada como la distancia de las condi- 
ciones ambientales medias de los territorios de lobos. En base a la distancia estadistica de Mahalanobis, 
construimos la distribuci6n espacial actual y potencial de la distribuci6n de los lobos para toda Italia penin- 
sular. El procedimiento de jacknife fue usado para evaluar la estabilidad de la distancia modelo y mostr6 
una confidencia buena en nuestro modelo (CV ? 13%). Se evalu6 la distancia del centroide de los territorios 
de lobos como un indice de calidad ambiental empleando 287 localidades donde algunos lobos han sido en- 
tAddress correspondence to L. Boitani, email boitani@Xpan. 
bio. uniromal. it 
Paper submitted July 7, 1997; revised manuscript accepted May 1, 1998. 
150 
Conservation Biology, Pages 15S0-15 9 
Volume 13, No. 1, February 1999 


Corsi et al. 
Large-Scale 
Model of Wolf Distribution 
151 
contrados muertos en los ultimos 25 a/los como consecuencia de activadades humanas (envenenamiento, 
caza, atropellamiento). Una contribuci6n valiosa para la planeaci6n de la conservaci6n result6 de la com- 
paraci6n de distribuci6nes de frecuencias de las distancias Mahalanobis de localidades con lobos muertos 
con elporcentaje de area de estudio dentro de cada de distancia. Esto mostr6 como el nu.mero de lobos muer- 
tos podria disminuir grandementre con la protecci6n de tan s6lo una parte pequefna del area de estudio e in- 
dic6 lo valioso de nuestra aproximnaci6n para la evaluaci6n de otras opciones de conservaci6n, como lo son 
la identificaci6n de areas centrales y corredores. 
Introduction 
The wolf (Canis lupus) once ranged throughout most of 
western Europe, but by the end of the last century it was 
reduced to only a few small, isolated populations in the 
Iberian peninsula, Italy, and the Balkans (Promberger & 
Schroder 1993). In Italy the population is believed to 
have reached its minimum in the early 1970s, when 
about 100 wolves were estimated, mostly in the central 
and southern portion of the peninsula (Zimen & Boitani 
1975). After full legal protection was established in 
1976, increased acceptance of wolves and a significant 
increase in wild ungulate populations favored a numeri- 
cal increase of the wolf and recolonization of large areas 
of the former distribution range (Boitani 1992). Currently, 
there are 400-500 animals ranging along the Apennines 
from the French border to the southern tip of Italy, but 
distribution is discontinuous and density varies (Boitani 
& Ciucci 1993; Fig. 1). The natural recolonization of the 
Italian and French Maritime Alps started in 1992 and is 
likely to extend northward to the central Alps in the 
near future (Boitani & Ciucci 1993). In spite of the ex- 
panding trend, population viability of the wolf is still 
threatened by small population size and significant adult 
mortality caused by illegal hunting (estimated at 15-20% 
of the total population [Boitani & Ciucci 1993]), and the 
species has recently been confirmed as "endangered" 
(Pinchera et al. 1997). 
The recolonization of areas where the wolf had been 
absent for many years has increased conflicts between 
wolves and humans and has revealed the need for a na- 
tional management plan (Boitani & Ciucci 1993). As 
pointed out by Noss (1992), a landscape approach in the 
range of i04-i05 km2 is likely to be the most adequate 
for integrating management of viable populations of 
wide-ranging animals, and it is evident that an effective 
management plan for the wolf in Italy should consider 
all of Italy except its islands (about 250,000 km2). 
The most recent developments in population viability 
analysis have shown the usefulness of spatially explicit 
computer simulation and the integration of demographic 
and dispersal data with a detailed knowledge of the land- 
scape geometry (Lamberson et al. 1992; McKelvey et al. 
1992; but see Harrison et al. 1993; Harrison 1994). Only 
a few studies have modeled spatial factors that deter- 
mine wolf distribution. Mladenoff et al. (1995) built a 
multiple logistic regression model to assess the impor- 
tance of landscape-scale factors in defining favorable 
wolf habitat in the northern Great Lakes region of the 
United States and found that road density and fractal di- 
mension were the most correlated variables. The model 
was also applied to the northeastern United States to 
predict favorable wolf habitats (Mladenoff & Sickely 1998). 
A similar result for road density had previously been ob- 
tained through simple correlation analyses (Thiel 1985; 
Mech et al. 1988; Fuller et al. 1992). These studies all 
aim to define the best habitat descriptor and predictor 
variables. 
We developed a method that uses multivariate analysis 
of geographic information system data to provide a spa- 
tially explicit model of wolf distribution that is applica- 
ble when country-wide information is limited. We wanted 
our model to emphasize spatial patterns rather than hab- 
0 
000 
0 
0 
0 
0 O 
0 
00 
100 km 
0~~~~~~~ 
0 
00 
0 
0 
0~~~~~ 
0 
* 
o 
0~~~~~~ 
00 
0~~~0 
0 
* 
Known wolf territories (WA) 
0 
0 
0 
Non-wolf area samples 
(NWA) 
** 
Areas where wolf presence was 
reported in the last 25 years 
Figure 1. Area of current wolf presence, wolf territo- 
ries and nonwolf sample areas used in the discrimi- 
nant analysis. 
Conservation Biology 
Volume 13, No. 1, February 1999 


152 
Large-ScaleModelof WolfDistribution 
Corsi et al. 
itat suitability and to contribute to the design of a coun- 
try-wide conservation plan for the wolf by (1) providing 
a basis for more advanced spatial and habitat analyses, 
(2) identifying the broad fragmentation patterns of the 
wolf distribution, and (3) providing insights into the 
wolf s likely recolonization of the Alps, an area where 
the wolf is expected to extend its range in the next few 
years. 
Methods 
Our methodology is based on two paradigms. First, 
given a set of environmental variables that potentially in- 
fluence wolf distribution, a training set can be built us- 
ing two groups, one of known wolf territories and the 
other of areas where the wolf is absent. A model can 
thus be built, in the multivariate space defined by the 
variables, that maximizes the difference between the 
two groups. Second, given an adequate sample of areas 
where the wolf is found, it is possible to build a "signa- 
ture" that best describes (and predicts) the areas where 
the wolf lives, based on the available environmental vari- 
ables. The results can be used to identify all areas of the 
country where the environmental conditions are most 
similar to those of the known territories and to evaluate 
to what extent each portion of the study area departs 
from the optimal conditions as defined by those of the 
territories. 
The model, however, is not suitable for analyzing hab- 
itat use because no absolute value of the contribution of 
each environmental variable to the model is obtained. In 
fact, in changing the set of environmental data or the 
training sets the relative contribution of each variable is 
expected to change, whereas the model is expected to 
maintain overall stability in defining large-scale response 
(e.g., use of space). 
Our study area was all of continental Italy. The coun- 
try is characterized by a variety of landscapes and eco- 
logical features. This is a consequence of the country's 
north-south extension, the mild coastal climate versus 
the more continental climate of internal and northern re- 
gions, the elevation variation from sea level to 4800 m, 
and the intense habitat modification produced over 
thousands of years by human activity. 
Data Sets 
Constrained by the limited country-wide information 
available, our data set was composed of three main sub- 
sets: data on wolf presence and absence, the environ- 
mental variables to be correlated to wolf presence, and a 
list of 287 locations where dead wolves were collected 
during the past 25 years. 
Conservation Biology 
Volume 13, No. 1, February 1999 
WOLF PRESENCE AND ABSENCE 
To define our training set, two groups of samples were 
used to describe the environmental features of the wolf 
areas (WAs) and the nonwolf areas (NWAs). The WAs 
were obtained using 12 wolf territories previously stud- 
ied by radio tracking (7) and/or intensive snow tracking 
(5) in various parts of the wolf range (Zimen 1978; 
Boitani 1986; Ciucci 1994; L.B., P. Ciucci, and F. Francisci, 
unpublished data; Fig. 1). A basic assumption is that the 
diversity of environmental conditions within these terri- 
tories represents the best average conditions for a stable 
presence of the wolf in the Apennines, including human 
influence: all 12 territories were found within areas 
where wolves either have always been present or have 
recently (in the last 10 years) and permanently colo- 
nized. 
Using all available records (direct and indirect signs of 
wolf presence), we identified any area where no evi- 
dence of stable wolf presence had been gathered in the 
last 25 years (Fig. 1) as a NWA. Considering only the por- 
tion of Italy south of the Po River and given the size and 
shape of the Italian peninsula, it is reasonable to assume 
that any location within a NWA is within the reach of 
dispersing wolves (<100 km). Because these areas have 
not been recolonized in the last 20 years when wolves 
were expanding their range, it can be assumed that most 
of the habitat in the NWAs is unsuitable. Therefore, ran- 
dom samples taken within the NWAs south of the Po 
River should provide samples of areas in which the val- 
ues of the environmental variables are mostly unsuitable 
for the wolf. To minimize the risk that this group could 
include points of suitable wolf habitat and to account for 
the diversity of habitat conditions, we oversampled the 
NWA and produced 100 non-overlaying circular areas 
(Fig. 1) by randomly sampling the centers of the circles 
within the NWA south of the Po River. The surface of 
each area (106 kM2) was equal to the average size of the 
12 known wolf territories. 
Of these 100 samples, 96 (8 times the number of avail- 
able territories) were chosen randomly. The remaining 
four were selected at the site of the major icefields in 
the Alps in order to account for the different topo- 
graphic conditions of the Apennines and the Alps, the 
latter exhibiting higher elevations and icefields, which 
are absent in the Apennines. These differences can con- 
ceal the real relationship between an environmental 
variable and wolf presence. 
ENVIRONMENTAL 
VARIABLES 
The second data set was used to describe the environ- 
mental characteristics of the training set and to extrapo- 
late the result of the analysis to the entire study area. 
The 13 variables used (Table 1) to define the multidi- 
mensional environmental space were selected not only 


Corsi et al. 
Large-ScaleModelof WolfDistribution 
153 
Table 1. The 13 environmental variables used in the analysis. 
Used in 
Variable 
final model 
Origin and resolution of data 
Farmland 
x 
land-use maps (1962-1986), scale 1:200,000 
Forest 
x 
land-use maps (1962-1986), scale 1:200,000 
Pasture 
land-use maps (1962-1986), scale 1:200,000 
Bare soil or water 
land-use maps (1962-1986), scale 1:200,000 
Urban settlement 
x 
urban settlement contours (Ente Nazionale Energia Elettrica [ENEL] 1971), scale 1:25,000 
Elevation 
Italy's Ministry of Environment, resolution 250 m 
Human density 
x 
130 National Census of the Population (Istituto Centrale Statistica 1991), aggregated 
by comune 
Road density 
x 
maps of the Italian Touring Club, scale 1:200,000 
Shannon diversity index 
x 
land-use maps (1962-1986), scale 1:250,000 
Shannon dominance index 
x 
land-use maps (1962-1986), scale 1:250,000 
Dumping site density 
x 
census of the Ministry of Agriculture and Forests (1990), aggregated by region 
Sheep density 
40 National Census of Agriculture (Istituto Centrale Statistica 1990), aggregated 
by comune 
Number of ungulate species 
x 
species' distribution maps (Ministry of Environment 1993), scale 1:1.250,000 
to account for our best knowledge of the basic wolf 
needs of space, food, and cover, but also with respect to 
their availability in digital form and degree of national 
coverage. Although the full influence of each of the 13 
variables on wolf distribution cannot be obtained, we as- 
sumed that they describe fairly well the high diversity of 
ecological conditions to which the wolf is known to 
adapt (Mech 1970; Boitani & Ciucci 1993). Wolf distri- 
bution in Italy appears to be influenced primarily by hu- 
man presence, food availability, and, consequently, type 
of land use (Boitani & Fabbri 1983). The wolf in Italy has 
been reported to feed on wild ungulates, livestock, and 
garbage at dump sites (Boitani 1982; Ciucci 1994; Me- 
riggi & Lovari 1996). Therefore, the selected set of vari- 
ables included densities of sheep, number of ungulate 
species present (densities were not available), and den- 
sity of dumping sites. 
Cover was described in terms of percentage of land- 
use classes (five variables: farmland, forest, pasture, bare 
soil or water, and urban). Indices of diversity and domi- 
nance of land use were included to account for the over- 
all landscape structure. Elevation was also included and 
interpreted as an ancillary variable highly correlated to 
both human disturbance and cover availability. Human 
pressure is probably the most important factor affecting 
wolf distribution, especially in Italy, where human im- 
pact on the environment is substantial (Boitani 1982). 
Additional variables such as human population and road 
densities were selected as habitat components to ac- 
count for human disturbance. 
All variables were obtained directly as digital thematic 
maps from various governmental sources and stored in a 
geographic information system (GIS) (ArcInfo, ESRI 1992). 
Some of the data sets were used directly for analysis, such 
as the land-use map in scale 1:200,000, whereas others 
were derived from the original digital thematic map by 
means of basic analyses (e.g., road density was computed 
from the original road network with a cell grid 10 X 10 
km). Human population and sheep densities Istituto Cen- 
trale Statistica 1990, 1991) were aggregated by comune 
(municipality), the median size of which is 21.5 km2. A 
digital terrain model with a square cell size of 250 m was 
used to derive information on elevation, whereas the di- 
versity and dominance indices were calculated using a 
cell grid 10 X 10 km, following the Shannon-Weaver for- 
mula. The maps of dumping-site density and number of 
ungulate species were available at a broader scale (about 
1:1,000,000). 
Because data quality and homogeneity were a major 
concern, all original data sets underwent editing, and all 
discrepancies were corrected. The final layers were then 
converted to raster format with a cell size of 250 m. 
We characterized the 12 territories and the 100 NWAs 
by performing simple overlay with the 13 layers and cal- 
culating basic statistics (percentage of coverage, mean 
values, etc.) depending on the type of environmental 
variable. In order to extend the result of the modeling 
based on these training sets to the entire study area, map 
algebra focal functions (Tomlin 1990) were used to rep- 
licate the same statistics over the entire study area. Each 
raster of 13 variables was processed by assuming each 
pixel to be the center of a hypothetical wolf territory 
and assigning to that pixel the same statistics used to 
characterize the training set, and each was calculated 
within a window of 23-pixel radius. This radius gives an 
area of 103.8 kM2, the best approximation to the aver- 
age dimension of the 12 wolf territories (106 km2) ob- 
tainable with a cell size of 250 m. 
DEAD WOLF LOCATIONS 
The data set of 287 dead wolf locations was obtained by 
pooling all information collected by various Italian of- 
fices and scientists on wolves found dead in the past 25 
Conservation Biology 
Volume 13, No. 1, February 1999 


154 
Large-Scale 
Model of WolfDistribution 
Corsi et al. 
years. About half of the sample was collected by L.B. Ev- 
idence of human-related cause of death (e.g., poison, 
shotgun, car or train accident) was available for at least 
70% of the sample, whereas cause of death for the re- 
maining 30% of the locations was presumed through in- 
direct ancillary information. Although only a portion of 
the total number of illegally killed wolves was recovered 
and the collection was not organized through a pre- 
defined procedure, the sample can be assumed to reflect 
the gross spatial distribution of killed wolves. In Italy, a 
wolf killed illegally or (more rarely) found dead is still an 
event, and the news is immediately spread; local author- 
ities usually recover the body and file a formal statement. 
The sample may not accurately represent regional varia- 
tion in the recovery system and the temporal distribu- 
tion of killed wolves, but this does not affect the sample 
utilization in our analysis. The data set on locations of 
dead wolves was used to explore the correspondence of 
dead wolf locations to areas of marginal environmental 
quality, thus providing a tool with which to validate the 
model and to enhance its conservation interpretation. 
Data Analysis 
We analyzed the data in three steps. First, to identify the 
most important areas of wolf presence (actual and po- 
tential), we used discriminant function analysis (DFA). 
This statistical method, although constrained by its in- 
herent limitations, has been applied widely to define a 
binary use of space-in 
our case, wolf and nonwolf ar- 
eas (Verbyla & Litvaitis 1989; Dubuc et al. 1990; Living- 
ston et al. 1990). Similar results could be obtained with 
logistic regression and less rigorous statistical assump- 
tions, but we preferred to normalize the variables through 
various transformations (see below) and to use a DFA 
because of its similarity to the methods adopted in the 
second step of our analysis (i.e., the Mahalanobis dis- 
tance). We performed a forward stepwise canonical dis- 
criminant analysis on 13 variables, 2 groups, and 112 ob- 
servations (12 WAs and 100 NWAs). Density of dumping 
sites and number of ungulate species were normalized 
with logarithmic transformation, forest and pasture ex- 
tension with the Freeman and Tukey transformation, 
and the remaining 9 variables with the Box-Cox transfor- 
mation with different values (Sokal & Rohlf 1995). 
The analysis was run with F = 0.6 (F, the probability 
value of the F statistics) to determine how significant the 
contribution of a variable to the regression had to be in 
order to be added to the discriminant function. The DFA 
results were used to classify the entire study area. The 
classification was calculated as the posterior probability 
of each pixel belonging to one of the groups 
exp (-O. 5D 2(X)) 
p(tlx) 
= 
exp(-0.5D 
5(x)) 
(1) 
Ylt exp (-O. 5Dt (x)) 
Conservation Biology 
Volume 13, No. 1, February 1999 
where x is the vector containing the values of environ- 
mental characteristics for each pixel. The Dt is the gen- 
eralized squared distance of each pixel from the t group, 
in which 
Dt(x) 
= (x-mt)'St 
(x-mt), 
(2) 
where St represents the within-group covariance matrix 
and mt the vector of the means of the variables of the t 
group. Equality of covariance matrices was tested by 
means of the Box M test (Davis 1986). The generalized 
squared distance (SAS Institute 1985) was used instead 
of the simple Mahalanobis distance because it accounts 
for differences in the variance-covariance matrix of the 
two groups. The a priori probabilities were considered 
equal, with the threshold set at 50% probability. 
In the second step, independently calculated from the 
previous one, we sought to describe potential intercon- 
nections between the areas of wolf presence, and we 
used the Mahalanobis distance statistic as an index of en- 
vironmental quality, distance from the best environmen- 
tal conditions for wolves. The Mahalanobis distance sta- 
tistic has been used as a multivariate index to rank 
habitat suitability in GIS raster maps (Clark et al. 1993; 
Knick & Dyer 1997) and avoids many difficult require- 
ments of discriminant function and logistical regression, 
particularly those involving incorrect classification of 
used versus unused habitats (Clark et al. 1993). We used 
wolf territories rather than a series of animal locations 
(radio locations, Clark et al. 1993; sightings, Knick & 
Dyer 1997); our small number of "observations" should 
be compensated partly by their higher ecological signifi- 
cance (large, stable areas). 
We calculated a surface of actual and potential use of 
space for the entire study area. The environmental centroid 
of the WAs group represented our best description of the 
optimal environmental conditions for the wolf; thus, we 
built an index of environmental quality based on the envi- 
ronmental Mahalanobis distance of any given location from 
the WAs centroid (the smaller the distance the more similar 
the environmental conditions of that location to the wolf's 
ecological profile). The environmental distance was calcu- 
lated for a continuous raster covering the entire study area. 
The third step served as validation of the previous two 
and as support for their conservation interpretation; it 
was based on the overlay of the locations of dead wolves 
to the models produced by the previous analyses. 
We evaluated the relationship between the distance 
from the WAs centroid and the probability of wolf oc- 
currence using the location of dead wolves. For each lo- 
cation the environmental distance from optimal wolf 
conditions was calculated through interpolation from the 
continuous surface. The resulting frequency distribution 
was fitted with different probability density functions to 
interpret changes in wolf distribution in response to 
variation in the environmental distances from WAs. 


Corsi etal. 
Large-Scale 
Model of WolfDistribution 
155 
To determine if an increase in population was related 
to expansion of wolf populations into areas of lower en- 
vironmental quality, we looked for differences in the en- 
vironmental quality levels of the areas where dead 
wolves were found in different time periods. All casual- 
ties were ordered chronologically and then grouped in 
sets of 10, 20, 30, 40, 50, 60, and 70 consecutive loca- 
tions. Each set was tested for normality and analyzed by 
analysis of variance, the hypothesis being that if a den- 
sity-dependent pattern of recolonization is applicable to 
the wolf in Italy, then the distribution should show a 
shift toward an increasing number of dead wolves in 
lower-quality environments. 
Finally, a tentative model for wolf management was 
produced by extrapolating from the distance raster a 
new raster in which the pixel values represented the ex- 
pected percent decrease of dead wolves (due to casual- 
ties) that would be achieved if all areas falling within the 
pixel's ecological distance were effectively protected. 
The index was obtained using the cumulative probabil- 
ity density function derived from the ecological dis- 
tances of dead wolf locations. Comparing on the same 
plot the cumulative frequency distribution of areas of in- 
creasing ecological distance and the cumulative proba- 
bility density function of dead wolf locations, the curves 
represent, for any given value of ecological distance, the 
percentage of territory that should be protected to achieve 
an expected percent reduction of wolf casualties. Obvi- 
ously, this model was applied only to the portion of Italy 
south of the Po River. The stability of the environmental 
distance model was assessed by means of jackknife pro- 
cedures (Cressie 1993; Sokal & Rohlf 1995). 
In analyzing the results, we divided the study area into 
a portion south of the Po River including the peninsular 
part of continental Italy (Apennines), where most of the 
current wolf range is, and a portion north of the Po 
River including the Alps, where the wolf is currently ex- 
panding its range. 
Results 
Areas of Importance for Wolf Presence 
Nine of the 13 variables were selected by the stepwise 
discriminant analysis (WiLks' lambda = 0.567, F = 8.64, 
p = 0.0001). The 100 NWAs appeared well separated 
from the 12 WAs on the first canonical variates, with 
only a few NWAs within the pertinence of the WAs. The 
12 wolf territories were correctly classified; the overall 
probability of belonging to the wolf group was over 
90%. Only 3 of the 96 random NWAs were assigned to 
the wolf distribution, whereas the 4 nonrandom NWAs 
were classified, as expected, into the NWAs group. 
By applying the classification criterion to the entire 
study area, we obtained locations of the areas most im- 
portant for wolf presence (Fig. 2). About 14,200 km2 
(about 5.7% of continental Italy) with an a posteriori prob- 
ability of more than 50% were found in this category. Of 
these, 11,300 km2 are in the peninsular portion of the 
country (Apennines), whereas 2900 km2 are located in 
the Alpine region. These areas of optimal environmental 
conditions could be considered the core of the wolf dis- 
tribution (actual and potential) and should be expected 
to act as a source of wolves for less suitable areas. 
Index of Environmental Quality and Surface of Actual and 
Potential Use of Space 
The values of the raster of the distances range from 0 to 
2933 (mean = 297, SD = 301). These absolute values 
have no specific meaning per se and are of interest only 
when considered in relation to another variable such as 
the dead wolves' locations. The frequency distribution 
of these locations fitted a log-normal density function 
(mean = 3.9068, SD = 0.8644, Kolmogorov-Smirnov d = 
0.0124403, not significant; Fig. 3). The right side of the 
distribution (the decreasing part) indicates density de- 
pendence; that is, as we move away from the areas of 
high environmental quality, wolf numbers and, conse- 
quently, deaths tend to decrease. As for the left side, tak- 
ing into account that all deaths are due to human-related 
causes, there are several possible explanations: (1) inter- 
actions between humans and wolves tend to be less fre- 
quent in areas of high environmental quality (lower hu- 
V. 
^; 
~'100 
km 
.%A~~S 
vd~K 
Wolf "core" 
distribution areas 
) 
; 
Figure 2. Wolf core distribution areas as obtained 
from the discriminant analysis model (i.e., with a pos- 
teriori probability over 50%). 
Conservation Biology 
Volume 13, No. 1, February 1999 


156 
Large-Scale 
Model of WolfDistribution 
Corsi etal. 
Figure 3. Log-norrnal distribution fitted to the envi- 
ronmental 
distances of dead wolf locations. 
The bisto- 
grams s*ow t*e observed distribution; 
t*e line s*ows 
tbefitted log-normal distribution 
(mean = 3.9068, 
SD = 0.8644; Kolmogorov-Smirnov 
d = 0. 0124403, 
not significant). 
man population density, higher availability of wild prey); 
(2) the interactions do not cause any casualty (better or 
more cover availabflity); and (3) the casualties that result 
from these interactions are not included in our sample. 
The first two hypotheses 
are similar because both re- 
10~~~~~~~~~~10t 
50 
Figure 3. 
LSognal 
distribution 
of 
the 
env- 
ronmentaleroedistnce of dhaeadswofrloations.t Teahito 
gramd-se casho (Theabserved distaindbution;ltin the 
ln 
hw 
thultie 
fiterog-orabliyasctewt 
ac 
distanuiocmane3.08 
mans oulto 
de nsity,ohighelgn rmaalpoabilityofunwidpry) 
mored covter avaloiabldisty;ande 
(3) 
the lcasatiens 
thtoesl 
frmtes 
nercin 
aent 
nldd 
nor 
ape 
Th fis 
w 
yohssaesmlrbcuebt 
e 
__~~~~~~~~~~~I 
_ 
m 
20 _ 
a. 
Fiur 4Sptaditiuinothpecnrecin 
Fittred to Sptheeooical 
distancesio of the lrcatins 
reutof 
dea wolv auates. 
ta 
ol 
ea*ee 
*og 
Vladume 13,lo.s1 
Febrarye 1999 
tindbcluatn* 
Table 2. Expected 
percent reduction in wolf casualties that would 
be achieved through fuli protection of the areas pertaining 
to 
different classes of environmental 
quality. 
Percent of 
Expected reduction 
study area* 
of casualties 
(%o) 
Area (km2) 
2.4 
<20 
6,060 
8.9 
20-35 
16,157 
18.0 
35-50 
22,661 
30.6 
50-65 
31,618 
50.2 
65-80 
49,173 
100.0 
>80 
124,516 
*Percentages of study area are given as cumulative figures to the 
upper limit of the probability class. 
duce the number of casualities. The third should be re- 
jected because the patterns of relatively high human 
presence throughout the country make it unrealistic to 
postulate lower efficiency in recovering dead wolves in 
the best wolf areas. 
The results of the conversion of the ecological dis- 
tances based on the probability density function of the 
ecological distances of the dead wolves' locations are 
shown in Fig. 4. For management purposes, the conver- 
sion can best be read from a map of the percent reduc- 
tion in wolf casualties that would be achieved through 
full protection of the areas with different levels of envi- 
ronmental quality (Fig. 4; Table 2). 
Based on the cumulative frequency distribution of dis- 
tance classes throughout continental Italy (Fig. 5), differ- 
ent conservation scenarios can be analyzed by means of 
a cost-benefit approach. For example, the point of maxi- 
0.94 
, 0.8 1. 
' 0.7 4. 
0.6 
* 0.5 t 
/. 
, 
054t 
E0.4 
002 
0.1 / 
U , - 
v 
! 
0 
- 
- 
0 
0 
( 0--- 
to 
CD 
co 
m) 
N 
co 
- 
<) 
CD 
el 
l) 
O 
D 
- 
t-_ 
N 
CD 
mf 
t 
O 
U 
_ 
_ 
N 
C<) 
c) 
t 
1 
Mahalanobis distance 
Figure 5. Comparison of the cumulative log-normal 
distribution of the probability of wolf casualties (solid 
line) with the cumulativefrequency distribution of the 
environmental distance classes in the study area (lim- 
ited to the portion south of the Po River; dashed line). 
The two lines can also be used as a model of expected 
percent decrease of wolf casualties with increasing 
size of areas of effective wolfprotection. The solid line 
indicates the expected percent reduction of casualties 
when increasing quantities of areas of different envi- 
ronmental quality (from best to poor) are effectively 
protected. 


Corsi et al. 
Large-Scale 
Model of WolfDistribution 
157 
mum "gain" occurs at an environmental distance of 109, 
where the number of casualties would decrease by more 
than 80%. Less than 40% of the study area would need to 
be protected to achieve maximum gain. 
Model Validation and Stability 
If the pattern of space use in relation to the environmen- 
tal distances has remained constant in the past 25 years, 
then wolf densities in the areas included within any 
given distance level should not have changed over time, 
and the wolf population should have increased mainly 
through an increase in its area of occupancy. The results 
of the analysis of variance applied to groups of sets of 
10, 20, 30, 40, 50, 60, and 70 consecutive locations sup- 
ported this hypothesis: all groupings but the first (with 
sets of 10 locations each) showed no significant differ- 
ences among their sets. None of the tests gave signifi- 
cant results (p > 0.5). The low significance of the group- 
ing with 10 locations (p < 0.1) may be explained as the 
result of local, random effects (i.e., the temporary occu- 
pancy of areas of lower environmental quality during 
the dispersal phase) due to the excessive subdivision of 
the sample. 
As for the overall stability of the models, the jackknife 
process showed an expected high variability (coeffi- 
cients of variation of over 1000%) in the pixel values of 
the raster of environmental distances. This is not surpris- 
ing because the relative contribution of the environmen- 
tal variables varies according to the subset of samples 
used for the analysis. With the same 12 rasters obtained 
from the jackknife, we also calculated the probability 
density function of the dead wolves' locations, and from 
these we calculated a probability raster for each of the 
12 runs of the jackknife. In this last case, the coefficient 
of variation of each pixel dropped drastically (? 13%) in 
accordance with an expected stability of the distance 
values when considered as a relative measure of environ- 
mental quality. 
Discussion 
There are at least two main reasons for adopting a large- 
scale approach to conservation of the Italian wolf meta- 
population (spatially structured; Harrison 1994). First, a 
large-scale approach is needed to manage fragmentation 
of suitable habitat and the inevitable metapopulation 
structure of the resulting population (May 1994), and 
hence to manage conflicts with human economies and 
illegal hunting. Second, the future of the wolf in Italy, as 
well as that of most large carnivores elsewhere, ulti- 
mately will depend on our ability to designate a zoning 
system of areas and connecting "corridors" where the 
wolf will be managed in ways appropriate to local eco- 
logical and economic conditions (Boitani 1982; Mech 
1995; Noss et al. 1996; Weaver et al. 1996). An "inte- 
grated landscape management" (Saunders et al. 1991; 
Turner et al. 1995; Wiens 1996) appears to be the only 
rational approach to ensure the survival of a mobile and 
adaptable species like the wolf, particularly in a highly 
fragmented landscape mosaic such as Italy (and Europe). 
We have explored a method for obtaining a spatial 
model of wolf distribution as a contribution to the prep- 
aration of a conservation plan. Model building is a de- 
ductive-inductive process, with model formulation and 
validation occurring iteratively (Stormer & Johnson 1986; 
Clark et al. 1993) and developing through a feedback 
process with field studies (Price & Gilpin 1996). Good 
models are the key to good conservation management 
(Gilpin 1996), yet real-world data are rarely adequate for 
complex and robust simulations (Dunning et al. 1995). 
Our method is an example of integration of the induc- 
tive and the deductive modeling approaches (Stoms et 
al. 1992) to maximize the utility of limited data. 
The model's predictions for the Alps may not be fully 
justified due to substantial ecological differences and 
should be taken only as a first indication of potential 
wolf distribution. Nevertheless, our model is based on 
the best current knowledge, and it provides a first in- 
sight into the likely evolution of wolf presence in that 
area. We emphasize that the method is more suited to 
identifying spatial patterns than critical habitat factors 
for wolf distribution because a variety of habitat combi- 
nations can produce identical distance values. 
Even though the human attitude toward wolves is 
probably one of the most important factors determin- 
ing wolf distribution (Boitani & Ciucci 1993; Mladenoff 
et al. 1995), it is not a simple variable and its distribu- 
tion cannot be mapped. Our method assumes that hu- 
man attitude is hidden in the other variables (e.g., road 
density and land use), as suggested by Thiel (1985), 
Mech et al. (1988), and Mladenoff et al. (1995). This 
approach implies that human disturbance is a density- 
dependent variable (i.e., it increases linearly with hu- 
man density). This is a weak assumption because the 
human attitude toward wolves can greatly modify this 
relationship. 
Although the GIS and statistical method are becoming 
more widespread in the ecological literature, we recog- 
nize the limits of the interpretations of our results. The 
core wolf areas as obtained from the discriminant analy- 
sis and the 12 wolf territories were characterized by 
means of the environmental distance surface, showing a 
conservative effect of the results of discriminant analy- 
sis. The average distance from the wolf optimal areas 
was 16.78 (SD = 6.08) for the core wolf areas and 31.09 
(SD = 19.68) for the 12 territories. The high patchiness 
of these areas is expected in a highly fragmented land- 
scape, but their interpretation as a source of wolves for 
less suitable areas is constrained by the particular defini- 
tion of core area. 
Conservation Biology 
Volume 13, No. 1, February 1999 


158 
Large-ScaleModelof WolfDistribution 
Corsi et al. 
Caution should also be observed in interpreting the 
optimal areas as obtained from the means and the vari- 
ance-covariance matrix of the 12 territories: the defini- 
tion refers to the statistical method rather than to an 
analysis of biological factors. Although the jackknife pro- 
cess used to assess the variability of the environmental 
distance model justifies our good confidence in its statis- 
tical stability, the model's best utilization is as a concep- 
tual guide for further insight into the biological and land- 
scape reality of its results. 
The output of the environmental distance model 
should never be interpreted as an absolute value. The 
high variability evidenced by the jackknife indicates that 
there is no direct functional relationship between these 
values and an absolute index of environmental quality. 
The jackknife, however, also shows that the relative mea- 
sure of these distances appears to remain constant, allow- 
ing their use as a relative index of environmental quality. 
The environmental distance raster can be interpreted as 
the relative expectation of wolves being at a given loca- 
tion, lower distances indicating higher expectation. 
The general level of spatial fragmentation (i.e., frag- 
ment size) appears within the order of magnitude of 
wolf territory size, allowing for future simulation of the 
effect of the territorial behavior on interpatch dynamics 
(Gutierrez & Harrison 1996). The fragmentation pattern 
in the Alps should be re-analyzed when similar data are 
available for neighboring countries because ecological 
continuity may be ensured through management of ar- 
eas across Italian borders. 
The calculations of the percent reductions in wolf ca- 
sualties achieved through area protection allow for pre- 
liminary analysis of various conservation scenarios on a 
cost-benefit basis, although the results should be viewed 
with caution due to the simplicity of the model. Assum- 
ing that the patterns shown by the frequency distribu- 
tion of dead wolf locations in the Apennines can be ex- 
trapolated to the Alps, we may infer the percentage of 
area that should be fully protected in order to expect a 
corresponding percent decrease in the number of dead 
wolves (Table 2). The distance raster, when analyzed in 
conjunction with available GIS functions, can be used to 
address important conservation issues such as areas of 
occupancy, core areas, areas of least conflict with hu- 
man activities, conservation options between areas of 
different quality (source-sink), and the identification of 
corridors. 
Within the limits of the practical utilization of metapop- 
ulation conceptual models (Gutierrez & Harrison 1996), 
our model is currently being used to support the diffi- 
cult technical and political process of preparing a con- 
servation and zoning plan for the wolf in Italy. Without a 
critical analysis of their inherent limitations (Price & 
Gilpin 1996), we strongly support the call for caution in 
using the appealing predictions of computer models to 
make real-life decisions. 
Conservation Biology 
Volume 13, No. 1, February 1999 
Literature Cited 
Boitani, L. 1982. Wolf management in intensively used areas of Italy. 
Pages 158-172 in F. H. Harrington and P. C. Paquet, editors. Wolves 
of the world: perspectives of behaviour, ecology and conservation. 
Noyes Publishing, Park Ridge, New Jersey. 
Boitani, L. 1986. Dalla parte del lupo. Giorgio Mondadori, Milan. 
Boitani, L. 1992. Wolf research and conservation in Italy. Biological 
Conservation 61:125-132. 
Boitani, L., and P. Ciucci. 1993. Wolves in Italy: critical issues for their 
conservation. Pages 74-90 in C. Promberger and W. Schr6der, edi- 
tors. Wolves in Europe: status and perspectives. Munich Wildlife 
Society, Ettal, Germany. 
Boitani, L., and M. L. Fabbri. 1983. Strategia nazionale di conservazione 
per il lupo (Canis lupus). Ricerche Biologia Selvaggina (Bologna, 
Italy) 72:1-3 1. 
Ciucci, P. 1994. Movimenti, attivita e risorse del lupo (Canis lupus) in 
due aree dell'Appennino centro-settentrionale. Ph.D. dissertation. 
University of Rome, Rome. 
Clark, J. D., J. E. Dunn, and K. G. Smith. 1993. A multivariate model of 
female black bear habitat use for a geographic information system. 
Journal of Wildlife Management 57:519-526. 
Cressie, N. A. C. 1993. Statistics for spatial data revised edition. Wiley 
& Sons, New York. 
Davis, J. C. 1986. Statistics and data analysis in geology. 2nd edition. 
Wiley & Sons, New York. 
Dubuc, L. J., W. B. Krohn, and R. B. Owen, Jr. 1990. Predicting occur- 
rence of river otters by habitat on Mount Desert Island, Maine. 
Journal of Wildlife Management 54:594-599. 
Dunning, J. B., Jr., D. J. Stewart, B. J. Danielson, B. R. Noon, T. L Root, 
R. H. Lamberson, and E. E. Stevens. 1995. Spatially explicit popula- 
tion models: current forms and future uses. Ecololgical Applica- 
tions 5:3-11. 
ESRI. 1992. ArcInfo user's manual. Version 6.1. Redlands, California. 
Fuller, T. K., W. E. Berg, G. L. Radde, M. S. Lenarz, and G. B. Joselyn. 
1992. A history and current estimate of wolf distribution and num- 
bers in Minnesota. Wildlife Society Bulletin 20:42-55. 
Gilpin, M. 1996. Metapopulations and wildlife conservation: ap- 
proaches to modeling spatial structure. Pages 11-28 in D. R. Mc- 
Cullough, editor. Metapopulations and wildlife conservation. Island 
Press, Washington, D.C. 
Gutierrez, R. J., and S. Harrison. 1996. Applying metapopulation the- 
ory to Spotted Owl management: a history and critique. Pages 167- 
186 in D. R. McCullough, editor. Metapopulations and wildlife con- 
servation. Island Press, Washington, D.C. 
Harrison, S. 1994. Metapopulations and conservation. Pages 111-128 
in P. J. Edwards, R. M. May, and N. R. Webb, editors. Large-scale 
ecology and conservation biology. Blackwell Scientific Publica- 
tions, Oxford, United Kingdom. 
Harrison, S., A. M. Stahl, and D. Doak. 1993. Spotted Owl update: U.S. 
judge rejects Forest Service plan. Conservation Biology 7:1-4. 
Istituto Centrale Statistica. 1990. 40 Censimento generale dell'agricol- 
tura. Rome. 
Istituto Centrale Statistica. 1991. 130 Censimento generale della popo- 
lazione. Rome. 
Knick, S. T., and D. L. Dyer. 1997. Distribution of black-tailed jackrab- 
bit habitat determined by GIS in southwestern Idaho. Journal of 
Wildlife Management 61:75-85. 
Lamberson, R. H., K. McKelvey, B. R. Noon, and C. Voss. 1992. A dy- 
namic analysis of Northern Spotted Owl viability in a fragmented 
forest landscape. Conservation Biology 6:505-512. 
Livingston, S. A., C. S. Todd, W. B. Krohn, and R. B. Owen. 1990. Habi- 
tat models for nesting Bald Eagle in Maine. Journal of Wildlife Man- 
agement 54:644-653. 
May, R. M. 1994. The effects of spatial scale on ecological questions 
and answers. Pages 1-17 in P. J. Edwards, R. M. May, and N. R. Webb, 


Corsi et al. 
Large-ScaleModelof WolfDistribution 
159 
editors. Large-scale ecology and conservation biology. Blackwell 
Scientific Publications, Oxford, United Kingdom. 
McKelvey, K., B. R. Noon, and R. H. Lamberson. 1992. Conservation 
planning for species occupying fragmented landscapes: the case of 
the Northern Spotted Owl. Pages 424-450 in P. M. Kareiva, J. G. 
Kingsolver, and R. B. Huey, editors. Biotic interactions and global 
change. Sinauer Associates, Sunderland, Massachusetts. 
Mech, L. D. 1970. The wolf: the ecology and behavior of an endan- 
gered species. Natural History Press, Doubleday, New York. 
Mech, L. D. 1995. The challenge and opportunity of recovering wolf 
populations. Conservation Biology 9:270-278. 
Mech, L. D., S. H. Fritts, G. L. Radde, and W. J. Paul. 1988. Wolf distri- 
bution and road density in Minnesota. Wildlife Society Bulletin 16: 
85-87. 
Meriggi, A., and S. Lovari. 1996. A review of wolf predation in south- 
ern Europe: does the wolf prefer wild prey to livestock? Journal of 
Applied Ecology 33:1561-1571. 
Mladenoff, D. J., and T. A. Sickely. 1998. Assessing potential gray wolf 
restoration in the northeastern United States: a spatial prediction of 
favorable habitat and potential population levels. Journal of Wild- 
life Management 62:1-10. 
Mladenoff, D. J., T. A. Sickley, R. G. Haight, and A. P. Wydeven. 1995. 
A regional landscape analysis and prediction of favorable gray wolf 
habitat in the northern Great Lakes region. Conservation Biology 9: 
279-294. 
Noss, R. S. 1992. Issues of scale in conservation biology. Pages 240- 
250 in P. L. Fiedler and S. K. Jain, editors. Conservation biology the 
theory and practice of nature conservation, preservation and man- 
agement. Chapman and Hall, New York. 
Noss, R. F., H. B. Quigley, M. G. Hornocker, T. Merril, and P. C. Paquet. 
1996. Conservation biology and carnivore conservation in the 
Rocky Mountains. Conservation Biology 10:949-963. 
Pinchera F., L. Boitani, and F. Corsi. 1997. Application to terrestrial 
vertebrates of Italy of a system proposed by IUCN for a new classi- 
fication of national Red List categories. Biodiversity and Conserva- 
tion 6:959-978. 
Price, M. V., and M. Gilpin. 1996. Modelers, mammologists, and meta- 
populations: designing Stephens' kangaroo rat reserves. Pages 217- 
240 in D. R. McCullough, editor. Metapopulations and wildlife con- 
servation. Island Press, Washington, D.C. 
Promberger, C., and W. Schroder, editors. 1993. Wolves in Europe: sta- 
tus and perspectives. Munich Wildlife Society, Ettal, Germany. 
SAS Institute, Inc. 1985. SAS user's guide: statistics. Version 6.04. Cary, 
North Carolina. 
Saunders, D. A., R. J. Hobbs, and C. Margules. 1991. Biological conse- 
quences of ecosystem fragmentation: a review. Conservation Biol- 
ogy 5:18-32. 
Sokal, R. R., and F. J. Rohlf. 1995. Biometry. W. H. Freeman, New York. 
Stoms, D. M., F. W. Davis, and C. B. Cogan. 1992. Sensitivity of wildlife 
habitat models to uncertainties in GIS data. Photogrammetric Engi- 
neering & Remote Sensing 58:843-850. 
Stormer, F. A., and D. H. Johnson. 1986. Introduction: biometric ap- 
proaches to modeling. Pages 159-160 in J. Verner, M. L. Morrison, 
and C. J. Ralph, editors. Wildlife 2000: modeling habitat relationships 
of terrestrial vertebrates. University of Wisconsin Press, Madison. 
Thiel, R. P. 1985. The relationship between road densities and wolf 
habitat suitability in Wisconsin. American Midland Naturalist 113: 
404-407. 
Tomlin, C. D. 1990. Geographic information systems and cartographic 
modelling. Prentice-Hall, London. 
Turner, M. G., G. J. Arthaud, R. T. Engstrom, S. J. Hejl, J. Liu, S. Loeb, 
and K. McKelvey. 1995. Usefulness of spatially explicit population 
models in land management. Ecological Applications 5:12-16. 
Verbyla D. L., and J. A. Litvaitis. 1989. Resampling methods for evaluat- 
ing classification accuracy of wildlife habitat models. Environmen- 
tal Management 13:783-787. 
Weaver, J. L., P. C. Paquet, and L. F. Ruggiero. 1996. Resilience and 
conservation of large carnivores in the Rocky Mountains. Conser- 
vation Biology 10:964-976. 
Wiens, J. A. 1996. Wildlife in patchy environments: metapopulations, 
mosaics and management. Pages 53-84 in D. R. McCullough, edi- 
tor. Metapopulations and wildlife conservation. Island Press, Wash- 
ington, D.C. 
Zimen, E. 1978. Der Wolf, Mythos und Verhalten. Meyster Verlag, Wien, 
Austria. 
Zimen, E., and L. Boitani. 1975. Number and distribution of wolves in 
Italy. Zeitschrift fur Saugetierkunde 40:102-112. 
Conservation Biology 
Volume 13, No. 1, February 1999 
