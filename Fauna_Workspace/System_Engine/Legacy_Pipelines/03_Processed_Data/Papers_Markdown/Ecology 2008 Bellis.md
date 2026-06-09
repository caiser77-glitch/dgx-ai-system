--- 
source: Ecology 2008 Bellis.pdf
--- 

Modeling Habitat Suitability for Greater Rheas Based on Satellite Image Texture
Author(s): Laura M. Bellis, Anna M. Pidgeon, Volker C. Radeloff, Véronique St-Louis, Joaquín
L. Navarro and Mónica B. Martella
Reviewed work(s):
Source: Ecological Applications, Vol. 18, No. 8 (Dec., 2008), pp. 1956-1966
Published by: Ecological Society of America
Stable URL: http://www.jstor.org/stable/27645914 .
Accessed: 20/12/2012 01:36
Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at .
http://www.jstor.org/page/info/about/policies/terms.jsp
 .
JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of
content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms
of scholarship. For more information about JSTOR, please contact support@jstor.org.
 .
Ecological Society of America is collaborating with JSTOR to digitize, preserve and extend access to
Ecological Applications.
http://www.jstor.org 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


Ecological Applications, 18(8), 2008, pp. 1956-1966 
? 2008 by the Ecological Society of America 
MODELING HABITAT SUITABILITY FOR GREATER RHEAS BASED ON 
SATELLITE IMAGE TEXTURE 
Laura 
M. 
Bellis,1,4 
Anna 
M. 
Pidgeon,2 
Volker 
C. Radeloff,2 
V?ronique 
St-Louis,2 
Joaqu?n 
L. Navarro,3 
AND MONICA 
B. M ARTELLA3 
1CONICET 
(Consejo Nacional 
de Investigaciones 
Cient?ficas y T?cnicas) 
and C?tedra 
de Ecolog?a, 
Facultad 
de Ciencias Exactas 
F?sicas y Naturales, 
Universidad Nacional 
de C?rdoba, 
Argentina 
2Department of Forest and Wildlife Ecology, 
University of Wisconsin, Madison, 
Wisconsin 
USA 
3CONICET 
(Consejo Nacional 
de Investigaciones 
Cient?ficas y T?cnicas) 
and Centro de Zoolog?a 
Aplicada, 
Universidad Nacional 
de C?rdoba, 
Argentina 
Abstract. 
Many 
wild 
species 
are affected 
by human 
activities 
occurring 
at broad 
spatial 
scales. For 
instance, 
in South America, 
habitat 
loss threatens Greater 
Rhea 
(Rhea 
americana) 
populations, 
making 
it important 
to model 
and map 
their habitat 
to better 
target conservation 
efforts. Spatially 
explicit 
habitat 
modeling 
is a powerful 
approach 
to understand 
and predict 
species 
occurrence 
and 
abundance. 
One 
problem 
with 
this approach 
is that commonly 
used 
land cover 
classifications 
do not capture 
the variability 
within 
a given 
land cover 
class 
that 
might 
constitute 
important 
habitat 
attribute 
information. 
Texture 
measures 
derived 
from 
remote 
sensing 
images 
quantify 
the variability 
in habitat 
features 
among 
and within 
habitat 
types; hence 
they are potentially 
a powerful 
tool to assess 
species-habitat 
relationships. 
Our 
goal was 
to explore 
the utility 
of texture measures 
for habitat 
modeling 
and 
to develop 
a 
habitat 
suitability map 
for Greater 
Rheas 
at the home 
range 
level in grasslands 
of Argentina. 
Greater 
Rhea 
group 
size obtained 
from aerial 
surveys was 
regressed 
against 
distance 
to roads, 
houses, 
and water, 
and 
land cover 
class abundance 
(dicotyledons, 
crops, 
grassland, 
forest, and 
bare 
soil), normalized 
difference 
vegetation 
index (NDVI), 
and 
selected 
first- and 
second-order 
texture measures 
derived 
from Landsat 
Thematic 
Mapper 
(TM) 
imagery. Among 
univariate 
models, 
Rhea 
group 
size was most 
strongly positively 
correlated 
with 
texture variables 
derived 
from near 
infrared 
reflectance measurement 
(TM 
band 
4). The 
best multiple 
regression 
models 
explained 
78% 
of the variability 
in Greater 
Rhea 
group 
size. Our 
results 
suggest 
that texture 
variables 
captured 
habitat 
heterogeneity 
that the conventional 
land cover 
classification 
did not 
detect. We 
used Greater 
Rhea 
group 
size as an indicator 
of habitat 
suitability; 
we 
categorized 
model 
output 
into different 
habitat 
quality 
classes. 
Only 
16% of the study area 
represented 
high-quality 
habitat 
for Greater 
Rheas 
(group 
size >15). 
Our 
results 
stress 
the potential 
of 
image 
texture 
to capture 
within-habitat 
variability 
in habitat 
assessments, 
and 
the necessity 
to 
preserve 
the remaining 
natural 
habitat 
for Greater 
Rheas. 
Key words: 
Argentina; grassland; 
Greater Rhea; 
habitat suitability; remote sensing; Rhea 
americana; 
texture. 
Introduction 
Conservation 
of wildlife 
habitat 
has 
become 
an 
increasing 
imperative 
as 
rates 
of habitat 
destruction 
continue 
to rise (e.g., Nagendra 
2001). 
Considering 
the 
challenges 
for wild 
species, 
there is a clear need 
to better 
understand 
spatial 
distribution 
of wildlife 
populations 
and 
species-habitat 
relationships. 
Conservation 
is most 
effective when 
efforts can be 
focused 
on habitat 
most 
suitable 
for a species 
of concern, 
but the challenge 
is to 
identify high-quality 
habitat 
across 
large areas. 
Identifying 
high-quality 
habitat 
for a given 
species 
can 
be difficult 
both 
because 
of logistical 
constraints, 
and 
Manuscript 
received 
12 February 
2007; 
revised 28 March 
2008; accepted 4 April 2008. Corresponding 
Editor: M. Friedl. 
4 Address 
for correspondence: 
C?tedra 
de Ecolog?a, 
Facultad 
de Ciencias 
Exactas 
F?sicas 
y Naturales, 
Universi 
dad Nacional 
de C?rdoba, 
V?lez 
Sarsfield 
299, CP 
(5000) 
C?rdoba, 
Argentina. 
E-mail: 
lbellis@com.uncor.edu 
because 
of limited knowledge 
of habitat 
requirements. 
Complete 
surveys 
alone 
are 
rarely 
feasible 
when 
mapping 
high-quality 
habitat 
for a large area 
because 
field 
investigations 
are expensive 
(Osborne 
et al. 2001, 
Gibson 
at al. 2004), 
and field data may 
quickly 
become 
outdated 
as habitat 
changes. 
However 
ground 
surveys 
can 
be 
combined 
with 
remotely 
sensed 
data 
to build 
predictive 
models, 
which 
in turn can be applied 
to broad 
areas 
of 
similar 
habitat. 
Spatially 
explicit 
habitat 
modeling, 
i.e., 
the use 
of statistical 
models 
to predict 
the locations 
of suitable 
habitat, 
can also be used 
to test 
ecological 
hypotheses 
regarding 
the response 
of individ 
uals 
to land cover, 
topography, 
and 
land use 
(Guisan 
and Zimmermann 
2000, Ottaviani 
et al. 2004). 
Because 
of their importance 
for both 
science 
and management, 
habitat models 
incorporating 
remotely 
sensed data 
have 
been used 
to predict 
occurrence 
and abundance 
patterns 
for many 
species 
(Elith 
et al. 2006), 
including 
wolves 
(Mladenoff et al. 1995), bustards (Osborne et al. 2001), 
1956 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


December 2008 
IMAGE TEXTURE IN RHEA HABITAT MODELS 1957 
butterflies 
(Luoto 
et al. 
2002), 
bears 
(Posillico 
et al. 
2004), and eagles (Balbontin 2005). 
In many 
habitat 
modeling 
studies, 
species 
presence 
absence 
or abundance 
patterns 
are 
related 
to habitat 
measures 
derived 
from remotely 
sensed 
imagery 
(Turner 
et al. 
2003). 
Commonly, 
a land 
cover 
classification 
is 
generated 
and used 
to predict 
species 
distribution 
based 
on 
land 
cover 
class 
abundance 
and 
landscape 
indices 
(Gottschalk 
et al. 2005). 
The 
application 
of landscape 
indices 
to satellite 
image 
classification 
has 
substantially 
contributed 
to the conservation 
of endangered 
species, 
by 
broadening 
the 
scales 
of 
consideration 
to 
those 
relevant 
to species 
of interest (McAlpine 
and Eyre 
2002). 
However 
the problem 
is that 
land cover 
classifications 
are 
rarely 
based 
on 
the real habitat 
requirements 
of 
specific 
wildlife 
species, 
and 
classifications 
commonly 
aggregate 
habitat 
types, which 
causes 
errors 
in habitat 
models (Hepinstall and Sader 1997, Luoto et al. 2004). 
Another 
limitation 
of land 
cover 
classifications 
is that 
they ignore habitat 
variability 
within 
a given 
land cover 
class, 
an attribute 
which 
may 
strongly 
influence 
habitat 
selection 
and use by wildlife 
species. 
For 
example, 
the 
spatial 
arrangement 
of 
foliage 
height 
diversity 
may 
determine 
the number 
of breeding 
species 
in a local area 
(MacArthur and MacArthur 1961). 
One 
approach 
that 
overcomes 
limitations 
of 
land 
cover 
classifications 
for habitat 
modeling 
is to incorpo 
rate image-based 
measures 
of habitat 
heterogeneity 
into 
habitat 
models 
(St-Louis 
et al. 
2006). 
Image-based 
measures 
do not depend 
on a land cover 
classification, 
but are 
rather derived 
directly 
from the satellite 
image 
(Haralick 
et al. 
1973). 
Image 
texture measures 
are 
a 
group 
of 
indices 
that can 
quantify 
the variability 
of 
vegetation 
as a continuous 
variable. 
As 
such, 
texture 
is 
advantageous 
compared 
to vegetation 
classification 
because 
many 
statistical 
algorithms 
perform 
better with 
continuous 
variables. 
Thus, 
texture measurements 
may 
have 
great 
potential 
in terms 
of 
identifying 
spatial 
habitat 
heterogeneity 
but to date 
only 
few studies 
have 
used 
texture 
to assess 
wildlife-habitat 
relationships. 
Where 
it was 
used, 
texture 
successfully 
predicted 
the 
occurrence 
of forest bird 
species 
(Hepinstall 
and 
Sader 
1997), avian 
species 
richness 
in a semiarid 
ecosystem 
(St 
Louis 
et al. 2006), 
and 
the abundance 
of Horned 
Larks 
(Eremophila 
alpestris), 
Brewer's 
Sparrows 
(Spizella 
breweri), and Sage Sparrows (Amphispiza belli) in Idaho 
(Knick 
and Rotenberry 
2000). 
Texture 
also 
successfully 
differentiated 
territories 
of two morphs 
of a passerine 
species 
(Tuttle 
et al. 2006). 
However, 
we 
are not aware 
of 
any 
studies 
that used 
texture 
to predict 
habitat 
suitability 
for a species 
of conservation 
concern. 
Our 
main 
goal 
was 
to evaluate 
the applicability 
of 
texture measures 
as a potential 
tool for modeling 
habitat 
suitability 
in conjunction 
with 
other ecological 
variables 
using Greater 
Rhea 
(Rhea 
americana) 
as our test species. 
We 
chose 
Greater 
Rhea 
because 
this species 
is threat 
ened 
by habitat 
destruction 
and 
is experiencing 
severe 
population 
declines 
throughout 
its range, 
yet habitat 
suitability 
at broad 
scales 
remains 
poorly 
understood. 
Focused 
conservation 
efforts 
are 
needed 
to prevent 
extirpation 
or even 
extinction 
of Greater 
Rheas. 
The 
Greater 
Rhea 
is a 
charismatic 
bird 
species 
endemic 
to South America 
that has been 
classified 
as a 
near-threatened 
species 
by the International 
Union 
for 
Conservation 
of Nature 
(IUCN 
2007). 
Greater 
Rheas 
mainly 
inhabit 
grassland 
ecosystems, 
one 
of the most 
human-modified 
and 
least protected 
biomes 
in the world 
(Demaria 
et al. 2003). 
In Argentina, 
Greater 
Rheas 
have 
undergone 
substantial 
population 
declines 
largely due 
to 
habitat 
loss 
and 
poaching 
(B?cher 
and Nores 
1988, 
Martella 
and Navarro 
2006). 
However, 
Greater 
Rheas 
can survive 
in agricultural 
areas 
if there is a mix 
of fields 
containing 
alfalfa 
{Medicago 
sativa) 
and clover 
{Melilo 
tus sp), plus 
grasslands 
containing 
some wild 
dicotyle 
dons 
(e.g., 
Plantago 
lanceolata, 
Conyza 
bonariensis, 
Cirsium 
vulg?re, 
Phyla 
canescens; 
Bellis 
et al. 
2004a, 
Herrera 
et 
al. 
2004). 
Unfortunately, 
grassland 
and 
alfalfa 
fields 
are 
increasingly 
converted 
to croplands 
(soybean 
Glycine 
max, 
sunflower Heliantus 
annus, 
corn 
Zea 
mays, 
wheat 
Triticum 
aestivum, 
etc.), 
which 
has 
adversely 
affected 
wild 
populations 
of Greater 
Rheas 
(Bellis 
2004). 
These 
land use 
changes 
occur 
not only 
in 
Argentina 
but 
also 
throughout 
the range 
of Greater 
Rhea 
in the savannas 
and grasslands 
of South America. 
Our 
study had 
two major 
objectives: 
(1) assessing 
the 
potential 
of satellite 
image 
texture measures 
for wildlife 
habitat models, and (2) identifying habitat attributes 
that affect presence 
and 
group 
size of Greater 
Rheas 
{Rhea 
americana) 
at 
the home 
range 
level 
in central 
Argentina 
and 
mapping 
habitat 
quality 
with 
image 
texture. 
Methods 
Study 
area 
Our 
research 
was 
conducted 
in the pampas 
grasslands 
of Argentina, 
located 
in the south-central 
part 
of San 
Luis 
province 
(Fig. 
1). In Argentina, 
most 
of the pampas 
(94%) 
was 
transformed 
in agroecosystems 
(Bertonatti 
and Corcuera 
2000, D?az-Zorita 
et al. 2002); 
however, 
grasslands 
still persist 
in areas 
considered 
unsuitable 
for 
crops. 
The 
San 
Luis 
pampas 
belongs 
to the semiarid 
western 
extreme 
of the pampas 
grassland; 
it is charac 
terized by sandy soils and rolling hills with both fixed 
and 
active 
dunes. 
Climax 
vegetation 
is composed 
of 
native 
grasses 
with 
islets 
of 
tree 
species, 
such 
as 
Goeffroea 
decorticans, 
Prosopis 
caldenia, 
and 
Prosopis 
alpataco. 
The 
dominant 
native 
grass 
species 
is Sorghas 
trum pellitum, 
mixed 
with 
Elyomurus 
muticus, 
Bothrio 
chloa 
springfieldii, 
Chloris 
retusa, 
Schizachyrium 
plumigerum, 
Eragrostis 
lugens, 
Sporobolus 
subinclusus, 
Aristida 
spegazzini, 
Poa 
ligularis, 
and 
Poa 
lanuginosa 
(Anderson 
et al. 
1970, Anderson 
1973). 
In the San Luis 
pampas, 
land 
transformation 
due 
to 
ranching 
is the most 
important 
process 
affecting 
the 
extent 
of this ecosystem; 
crop 
production 
is sporadic 
because 
of low annual 
rainfall 
(<500 
mm; 
Le?n 
et al. 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


1958 
LAURA M. BELLIS ET AL. 
Ecological Applications 
Vol. 18, No. 8 
:.-..! 
-iUJi 
Habitat quality 
High, >15 individuals 
Medium, 
5-15 
individuals 
Low, 1-5 individuals 
Unsuitable, 0 individuals 
I Ponds 
s ;, 
n.%\^ 
Fig. 
1. Habitat 
suitability maps 
for Greater Rheas 
estimated from using group size as an indicator of habitat quality. 
1984). The 
grasslands 
are not uniform, 
partly due 
to the 
conversion 
of native 
grasslands 
through 
introduction 
of 
exotic 
grass 
species 
including 
Eragrostis 
curvula 
and 
Digitaria 
eriantha 
to increase 
grassland 
forage 
quality 
for livestock (Demaria et al. 2003). Four years of study 
in the pampas 
comparing 
the San Luis 
grassland 
with an 
adjacent 
area 
totally 
transformed 
to an agroecosystem 
showed 
that 
agricultural 
expansion, 
especially 
the 
increase 
of 
lands 
devoted 
to crops, 
reduced 
Greater 
Rhea abundance and disrupted the spatial distribution 
of the species (Bellis 2004, Giordano 
et al. 2008). 
Because 
San 
Luis 
pampas 
is the last great 
grassland 
Greater Rhea habitat in Argentina, we focused this 
study on an area of 4782 km2 dominated by grassland 
(55%) with crops and alfalfa fields present in lower 
proportions (15% and 5%, respectively). 
Field survey 
Two 
aerial 
counts were 
conducted 
in the study area 
in 
2004 following the approach developed by Caughley 
(1974), Caughley and Sinclair (1994), and Sutherland 
(1996). The first survey was conducted in May prior to 
the September through November breeding season 
(Bruning 1974, Reboreda and Fern?ndez 1997), and 
the second 
survey was 
conducted 
in December, 
during 
the December 
to February 
post-reproductive 
season. 
Aerial 
counts 
were 
performed 
from 
a Cessna 
182 
airplane flying at an average speed of 120 km/h and an 
average altitude of 100 m. The flight direction was west 
to east 
across 
each 
site, to avoid 
glare. 
The 
sampling 
technique consisted of six strip transects 52 km in length 
spaced 
at regular 
intervals 
of 10.4 km. The 
coordinates 
of the flight path were generated in advance, and the 
pilot carefully followed the survey design using a global 
positioning system (GPS). The navigator determined the 
beginning 
and end of each 
survey 
line. In the scheme 
of 
flight controllable 
sources 
of bias, 
such as strip width, 
altitude and speed (Caughley 1974) were carefully 
monitored, 
and 
these variables 
were 
held 
constant. 
Two observers seated side by side in the Cessna, which 
has high wings, collected the data. Each observer 
scanned a 170 m wide strip of ground delineated by 
streamers 
on 
the 
aircraft's 
wing 
struts. 
Observers 
recorded 
the number 
of Greater 
Rheas, 
at the moment 
they were perpendicular to the aircraft; even if they had 
been 
detected 
in advance; 
therefore, 
counting 
and 
position 
recording 
was 
almost 
simultaneous. 
Observers 
marked Greater Rhea locations with a Garmin 12XL 
GPS (GPS eTrex Legend; Garmin International, Olathe, 
Kansas, USA). The average positional error for the GPS 
locations during our survey was 9.2 m. Visibility within 
the strip transect 
that was 
surveyed 
was 
comparable 
for 
all habitat types. 
Biological 
characteristics 
of the species 
Greater Rhea (see Plate 1) is a non-territorial species 
that commonly lives in flocks in a loosely cohesive social 
system (Bruning 1974, Martella et al. 1995, Reboreda 
and Fern?ndez 1997). The most important components 
of the Greater Rhea diet (90%) are native short-lived 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


December 
2008 
IMAGE TEXTURE IN RHEA HABITAT MODELS 
1959 
Plate 
1. Adult Greater 
Rhea 
{Rhea americana) 
in an experimental 
field near C?rdoba, 
Argentina. 
Photo 
credit: J. L. Navarro. 
forbs 
(Phyla 
canescens, 
Plantago 
lanceolata, 
Conyza 
bonariensis, 
Descurainina 
sp., and Cirsium 
vulg?re) 
and 
alfalfa (Medicago sativa); wild and cultivated gramine 
ous 
species 
(Eragrostis 
sp., Agropyron 
sp., S tipa 
sp., 
Cenchrus 
sp., S?cale 
c?r?ale, 
and Trichloris 
sp.) are eaten 
in lower proportions. 
Greater 
Rheas 
also 
consume 
seeds 
(Zea 
mays, 
Bromus 
sp., 
and 
Sorghum 
sp.), 
fruits 
(Cenchrus 
pauciflorus, 
Argemone 
subfusiformis), 
inverte 
brates 
(pieces 
of teguments 
of several 
insects: Hemip 
tera, Orthoptera, 
and Coleptera), 
and 
small vertebrates 
(Bufo sp., Teius sp.; Yagueddu and Viviani Rossi 1985, 
Martella 
et al. 
1996). Previous 
studies 
have 
shown 
that 
Greater Rheas prefer habitats where dicotyledonous 
species are available (Codenotti and Alvarez 2000, Bellis 
et al. 
2004a, 
Herrera 
et al. 
2004). 
In agroecosystems, 
alfalfa fields are the most commonly used habitat by 
Greater 
Rheas. 
In addition 
to meeting 
foraging 
require 
ments, the open habitat of alfalfa fields facilitates 
vigilance and escape from predators (Codenotti and 
Alvarez 2000, Bellis et al. 2004a). At present, despite 
legal protection of Greater Rheas by the national 
government 
of Argentina, 
humans 
are 
their main 
predator, persecuting and shooting individuals through 
out their range (Martella and Navarro 2006). Behavioral 
studies of the species (Martella et al. 1995, Reboreda 
and Fern?ndez 1997, Fern?ndez et al. 2003) have shown 
that large group size benefits individual Greater Rheas 
by reducing the risk of pr?dation and increasing the time 
available 
for feeding. 
Further, 
research 
showed 
that 
large groups occur in habitat with high food availability. 
The 
number 
of Greater 
Rheas 
at a location, 
i.e., group 
size, can 
thus be used 
as an index for habitat 
quality 
at 
that location. 
Group 
size was 
selected 
over 
abundance 
or density because they have different effects (Estevez et 
al. 2007). Whereas 
the density is determined by the 
number 
of individuals 
per unit of space, 
the group 
size, 
i.e., 
the number 
of 
individuals 
that form 
a group, 
is 
closely associated with behavioral features related to the 
cost-benefit 
balance 
of 
resource 
availability 
(Beau 
champ 
2001, 
Fern?ndez 
et al. 2003). 
However, 
we 
note 
that group 
size is not a measure 
of absolute 
density, 
and 
that our estimates may have been affected by different 
detectability functions of Greater Rhe?s 
in different 
habitats. 
To 
solve 
these 
limitations 
m future studies, we 
recommend 
using 
survey methods 
adjusted 
for incom 
plete detection (Thompson 2002) as a rigorous approach 
in the estimation 
of response 
variable. 
In the case 
of 
gregarious 
species 
such 
as Greater 
Rheas, 
distance 
sampling would be the preferred technique because it 
allows consideration of the group size (ancillary data) 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


1960 
LAURA 
M. 
BELLIS 
ET AL. 
Ecological Applications 
Vol. 18, No. 8 
Table 
1. 
Independent 
variables 
selected for the habitat 
suitability analysis 
of Greater 
Rheas 
in the pampas 
grasslands 
of 
Argentina. 
Habitat 
requirements, 
variables 
Description 
of the variable 
Units 
Food 
Land 
cover 
Water 
NDVI 
Heterogeneity 
of NDVI 
Nesting 
and refuge 
Land 
cover 
Vegetation 
structure 
Texture, first order (TM bands) 
Texture, 
second order (TM bands) 
Additional 
Human 
impact 
grassland, 
crops, forest, bare soil, and dicotyledons 
distance 
to nearest water 
a proxy for vegetative cover and biomass 
coefficient of variation 
(CV) 
grassland, 
crops, forest, bare soil, and dicotyledons 
mean 
(3-4-5-7 ), variance 
(1 to 5) 
mean 
(3-4-7), variance 
(4-5-7), homogeneity 
(7), 
correlation 
(1 to 7), and second moment 
(1 to 7) 
distance 
to nearest house, distance 
to nearest road 
proportion 
km 
index value 
% 
proportion 
index values 
index values 
km 
and 
the number 
of groups 
(clusters) 
per unit of space 
as 
a density measure 
(Buckland 
et al. 2001). 
Habitat 
measures 
Understanding 
factors 
affecting Greater 
Rhea 
forag 
ing and 
survival 
allows 
selection 
of 
relevant 
habitat 
elements 
as model 
inputs 
from among 
those 
that might 
affect Greater 
Rhea 
distribution. 
The main 
ecological 
variables 
known 
to 
influence 
Greater 
Rhea 
habitat 
suitability 
in relation 
to 
food, 
water, 
and 
nesting 
requirements, 
as well 
as human 
disturbance 
are 
sum 
marized 
in Table 
1. 
Water 
bodies, 
roads, 
and 
human 
settlements 
were 
digitized 
from 
a 
topographic 
map 
of 
the 
study 
area 
(1:250 000; Military Geographic Institute, Buenos Aires, 
Argentina). 
Besides 
their 
importance 
as 
a 
source 
of 
drinking 
water, 
plant 
communities 
dominated 
by dicot 
species 
are found 
on the edges 
of water 
bodies 
(Herrera 
et al. 2004), 
and are an important 
source 
of food. Roads 
and 
houses 
were 
selected 
as 
indices 
of human 
distur 
bance. 
The 
digitized 
information 
on water 
bodies, 
roads, 
and houses 
was 
transformed 
into a continuous 
variable 
of distance 
expressed 
in kilometers 
using 
ENVI 
GIS 
(ENVI 
2004). 
Vegetation 
patches, 
normalized 
difference 
vegetation 
index 
(NDVI), 
and 
texture measures 
were 
calculated 
from 
a 
satellite 
image 
(December 
2004 
Landsat 5 TM image, path 230, row 084) using ENVI 
GIS (ENVI 2004). The spatial resolution chosen for our 
analysis 
was 
based 
on the home 
range of the species. 
In 
grassland, 
Greater 
Rhea 
home 
range 
averages 
11 km2 
(Bellis 
et al. 
2004?). 
We 
used 
a 
sampling 
area 
that 
approximates 
20% 
of Greater 
Rhea 
home 
range, 
following the method of Laymon and Barrett (1986) 
and Posillico 
et al. 
(2004). 
Thus 
the spatial 
resolution 
applied 
to the analysis 
was 
a 
1.5 X 
1.5 km moving 
window, 
including 
2500 
pixels. 
The mean 
value 
of all 
pixels 
within 
the window 
was 
calculated 
for 
each 
variable. 
Land 
cover of the study area was 
classified 
based 
on a 
2004 Landsat 5 TM image (path 230, row 084) from the 
summer 
season 
(December). 
Using 
ground 
control 
points from topographic maps (1:250000) the satellite 
image 
was 
georeferenced 
to a Universal 
Transverse 
Mercator projection (zone 20 S, datum WGS 
84). We 
conducted 
a supervised 
maximum 
likelihood 
classifica 
tion using 
training 
sites for which 
land cover was 
known 
from field reconnaissance. 
A post-classification 
accuracy 
assessment 
showed 
an overall 
accuracy 
(calculated 
by 
summing 
the number 
of pixels 
classified 
correctly 
and 
dividing by the total number of pixels used for the 
accuracy 
assessment) 
of 94.6% 
and a kappa 
coefficient = 
0.76 (ENVI 2004). The proportion of each land cover 
class 
was 
summarized 
for each 
1.5 X 
1.5 km moving 
window. 
We 
calculated the NDVI 
(normalized difference 
vegetation 
index; Paruelo 
et al. 
1997, Oesterheld 
et al. 
1998, Posse 
and Cingolani 
2004) 
as an 
indication 
of 
vegetation 
abundance. 
NDVI 
was 
calculated 
using 
the 
following 
formula: 
near-infrared(TM4) 
- 
red(TM3) 
near-infrared(TM4) 
+ red(TM3). 
NDVI 
values 
fall between 
? 1 and +1 
; higher values 
show 
higher 
proportions 
of photosynthetically 
active 
green 
vegetation, 
and 
negative 
values 
indicate 
nonvegetated 
surfaces. 
Also, 
we calculated 
the coefficient 
of variation 
(CV, 
%) 
of 
the NDVI 
as 
a 
surrogate 
measure 
of 
vegetation 
heterogeneity. 
Image 
texture 
is the visual 
effect produced 
by 
the 
spatial 
distribution 
of tonal variation 
in adjacent 
pixels 
(Baraldi 
and 
Parmiggiani 
1995). 
Texture 
analysis 
characterizes 
the 
stochastic 
properties 
of 
the 
spatial 
distribution 
of gray 
levels in an image 
(Dong-Chen 
and 
Wang 
1990). There 
are 
two types of texture measures: 
first-order 
(occurrence) 
and 
second-order 
(co-occur 
rence). 
First-order 
texture measures 
are based 
on 
the 
number 
of occurrences 
of each gray-level 
within 
a given 
processing 
window. 
Second-order 
texture measures 
use a 
gray-tone 
spatial 
dependence 
matrix 
(i.e., co-occurrence 
matrix) 
to calculate 
texture 
values. 
The 
co-occurrence 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


December 2008 
IMAGE TEXTURE IN RHEA HABITAT MODELS 1961 
matrix 
contains 
the relative 
frequencies 
with which 
pixel 
values 
co-occur 
in a given neighborhood 
(Haralick 
et al. 
1973, Dong-Chen 
and Wang 
1990, Baraldi 
and Parmig 
giani 1995, Tso and Mather 
2001). Following 
the 
approach 
of St-Louis 
et al. 
(2006), 
we 
calculated 
four 
first-order 
texture measures 
(mean, 
variance, 
entropy, 
and 
skewness), 
and eight second-order 
texture measures 
(mean, 
variance, 
homogeneity, 
contrast, 
dissimilarity, 
entropy, 
second moment, 
and correlation) 
for each 
1.5 X 
1.5 km moving 
window. 
The 
12 texture 
indices 
were 
calculated 
separately 
for each 
of the six Landsat 
TM 
bands 
with 
30-m 
resolution. 
Texture 
analysis 
was 
conducted in ENVI (ENVI 2004). 
Global 
positioning 
system 
locations 
of each Greater 
Rhea group were implemented into the GIS ENVI 
(ENVI 2004) and checked for accuracy against a GIS 
layer from the Military 
Geographic 
Institute 
of Argen 
tina. The 
error 
detected 
was 
<30 
m 
(i.e., 
1 Landsat 
pixel), 
which 
we 
deemed 
acceptable 
given 
that 
the 
habitat 
analysis 
was 
performed 
at a resolution 
of 1.5 X 
1.5 km. 
Model building 
The 
texture 
analysis 
resulted 
in 72 texture 
variables 
(12 texture measures 
for each 
of the six bands) 
and 
an 
additional 
10 ecological 
variables. 
In order 
to avoid 
colinearity, 
a pairwise 
correlation 
matrix 
of all predic 
tors was 
constructed. 
As many 
texture 
variables 
were 
highly 
correlated 
we chose 
a 0.95 
threshold 
to reduce 
the 
total 
number 
of 
variables 
to a point 
where 
model 
selection 
procedure 
runs 
efficiently. 
The 
correlation 
analysis 
among 
the 82 
independent 
variables 
showed 
high correlations (r > 0.95; P < 0.001) for 45 of the 3321 
pairwise 
comparisons. 
For 
these pairs, 
we 
retained 
the 
variable 
with 
the highest 
r value 
among 
the two and 
eliminated 
the other 
variable 
from further analysis. 
In 
the end, 
a set of 38 independent 
variables 
(28 
texture 
measures 
and 
10 ecological 
variables) 
was 
retained 
for 
further analysis 
(Table 
1). Scatterplots 
of the response 
variable 
and 
the covariates 
did not 
indicate 
a need 
for 
data 
transformation. 
We 
performed 
a 
leaps 
analysis 
using 
the software 
package 
R 
(R Development 
Core 
Team 
2007). 
The 
leaps procedure 
utilizes 
a branch 
and 
bound 
strategy 
for predicting 
the best 
subsets 
of the 
explanatory 
variables 
in linear 
regression 
without 
the 
requirement 
of a link function. 
It scans 
systematically 
through 
all 
subsets 
at the same 
time, 
"leaping" 
over 
those 
nonoptimal 
subsets 
(Furnival 
and Wilson 
1974, 
Miller 2002). Due to our small sample size (36 points), 
the 
regression 
subset 
was 
bounded 
by 
a maximum 
number 
of six explanatory 
variables. 
This 
restriction 
is 
within 
the upper 
edge recommended 
considering 
the size 
of data 
set and 
the number 
of observation 
per variable 
(about 
seven 
in our 
case; 
Neter 
et al. 
1990). We 
examined 
the 
25 
best 
subsets 
including 
two 
to 
six 
predictors, 
for a total of 125 models. 
For 
each 
of these 
125 models, 
adjusted 
R2, 
the corrected 
form of Akaike 
Information 
Criteria 
(AICC), 
and AAIQ 
(i.e., AICC 
- 
min AICC) 
were 
calculated 
to determine 
the best models 
of Greater 
Rhea 
group 
size 
(Hurvich 
and 
Tsai 
1989, 
Whittingham 
et al. 
2006). 
AICC 
is recommended 
for 
small 
sample 
sizes, 
specifically 
when 
the number 
of 
samples {n = 36) divided by the number of parameters (k 
= 4-8 
for the different dimension 
models) 
is smaller 
than 
40. AAICC 
values 
allow 
a quick 
comparison 
and 
ranking 
of candidate 
models. 
As 
a rule of thumb, models 
having 
a AAICC 
with 
values 
varying 
<2 
from 
the best model 
have 
substantial 
support, 
models 
with 
values 
between 
three 
and 
seven 
have 
less 
support, 
and models 
with 
AAICC 
>10 
miss 
some 
important 
explanatory 
variables 
(Burnham 
and Anderson 
2002). We 
used 
a AAICC 
odd 
of four 
for determining 
the models 
that 
are 
equally 
strong 
at predicting 
Greater 
Rhea 
group 
size. 
This 
cutoff was 
chosen 
because 
smaller 
cutoffs 
yielded 
only 
slight differences 
in predictive 
power 
(e.g., difference 
in 
adjusted R2 < 0.01). 
In order 
to examine 
the role of spatial 
dependence 
in 
the final models, 
we 
assessed 
the pattern 
of 
spatial 
autocorrelation 
with 
semivariance 
analysis 
(Legendre 
et 
al. 2002). We 
used 
this analysis 
because 
it is robust, 
it 
allows 
identification 
of 
outliers 
in exploratory 
data 
analysis, 
and 
it is a 
good 
estimator 
to reduce 
the 
sensitiveness 
to 
outliers 
(Sun 
et 
al. 
2003). 
These 
characteristics 
as well 
as the simplicity 
of its estimation 
make 
the semivariogram 
one 
of 
the techniques 
most 
widely 
available 
for use by landscape 
ecologists 
(Meisel 
and 
Turner 
1998). We 
calculated 
a 
semivariogram 
of 
each 
selected 
model, 
plotting 
the 
semivariance 
of 
residuals 
against 
the distances 
between 
pairs 
of points 
and, 
in all 
cases, 
there was 
no 
evidence 
of 
spatial 
dependence. 
The 
predictive 
power 
of models 
was 
evaluated 
by 
means 
of a 
leave-one-out 
cross 
validation 
procedure. 
This 
is an appropriate 
testing method 
when 
the data 
set 
is quite 
small and/or when 
each 
sample 
is likely to have 
unique 
information 
that is relevant 
to the model 
(Guisan 
and 
Zimmermann 
2000, Miller 
2002, 
Ottaviani 
et al. 
2004). 
A model 
was 
developed 
using 
a single observation 
from the original 
sample 
as the validation 
data, 
and 
the 
remaining 
observations 
as the training 
data. 
Using 
the 
model 
estimated 
from the training data 
a prediction 
was 
made 
for that observation. 
This 
procedure 
was 
repeated 
for all 36 observations. 
The 
average 
error was 
computed 
and used 
to evaluate 
the model. 
Finally, 
we 
constructed 
habitat 
suitability 
maps 
for 
Greater 
Rheas 
in our 
study 
area. 
The 
regression 
equation 
of. the best 
selected model 
was mapped 
using 
ENVI GIS 
(ENVI 2004). The resulting map predicted 
different 
habitat 
qualities 
for the species 
at a scale 
of 
home 
range. 
Results 
A 
total of 36 groups 
of Greater 
Rheas 
were 
recorded 
in the 
study 
area 
during 
the 2004 
survey. 
In 
these 
groups, 
we detected 
157 Greater 
Rheas, 
nine as solitary 
individuals 
and 
27 groups 
that ranged 
from 
two to 20 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


1962 
LAURA 
M. 
BELLIS 
ET AL. 
Ecological Applications 
Vol. 18, No. 8 
Table 
2. 
Frequency 
of times each variable was 
incorporated 
in the top 63 models 
for which 
the 
AAICC 
compared 
to the highest ranked model was <4. 
Description, 
independent variables 
Number 
of variables 
in the models 
Second 
order texture 
Variance 
TM 
bandl 
Variance 
TM 
band2 
Variance 
TM 
band3 
Variance 
TM 
band4 
Variance 
TM 
band5 
Mean 
TM 
band3 
Mean 
TM 
band4 
Mean 
TM 
band5 
Mean 
TM 
band7 
Homogeneity 
TM band7 
Correlation 
TM 
band3 
Correlation 
TM 
band4 
Correlation 
TM 
band5 
Correlation 
TM 
band7 
Second moment 
TM bandl 
Second moment 
TM band2 
Second moment TM 
band3 
Second moment TM band4 
Second moment 
TM 
band5 
Second moment TM 
band7 
First order texture 
Variance 
TM 
band4 
Variance 
TM 
band7 
Variance 
TM 
band5 
Mean 
TM 
band4 
Mean 
TM 
band7 
Ecological 
Grassland 
proportion 
Crops 
proportion 
Forest proportion 
Alfalfa proportion 
NDVI 
CV_NDVI (%) 
Number 
of models 
estimated 
Maximum 
R: 
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
0 
0 
0 
0 
0 
0 
0 
0 
Minimum 
R: 
adj 
0.61 
0.61 
0.7 
0.67 
1 
1 
0 
18 
3 
0 
1 
0 
0 
1 
1 
25 
2 
2 
1 
1 
3 
0 
1 
0 
1 
2 
25 
1 
0 
1 
25 
0.72 
0.69 
0.77 
0.75 
0 
6 
3 
12 
1 
25 
10 
0 
1 
6 
0 
25 
0 
0 
2 
1 
3 
0 
0 
1 
5 
0 
0 
15 
1 
4 
4 
0 
0 
25 
0 
25 
0.8 
0.78 
Note: The minimum 
and maximum 
adjusted R 
values obtained 
for this group of models 
are 
shown in the last two rows. 
individuals 
with 
an average 
group 
size of 4.36 
? 
0.7 
individuals (mean ? SE). 
Habitat 
models 
Of the total of 125 models estimated, 63 had a AAICC 
<4 
(Table 2). The best models, which used five or six 
independent 
variables, 
explained 
up 
to 75% 
of 
the 
variability 
in Greater 
Rhea 
group 
size. None 
of them 
included 
variables 
related 
to human 
disturbance 
such as 
proximity 
to roads 
and houses. 
Of 
this 
group 
of models, 
we 
selected 
the most 
parsimonious 
ones, 
which 
included 
five 
predictor 
variables 
(Table 
3). 
In all 
cases, 
the use 
of 
spectral 
information 
including 
multiple 
texture measures 
and 
NDVI 
produced 
the best 
results. 
Texture 
measures 
derived from Landsat TM bands 3 and 4 exhibited the 
highest 
predictive 
power; 
the other 
bands 
captured 
substantially 
less 
or 
no 
variability. 
The 
association 
between 
these variables 
and Greater 
Rhea 
group 
size 
was 
negative 
for texture measures 
derived 
from TM 
bands 
1, 3, and 7 and the NDVI, 
and positive 
for texture 
based 
on TM 
band 
4 (Table 
3). The 
overall 
accuracy 
of 
cross-validation 
procedure 
of these 
seven 
best models 
ranged from 50% to 69% (Table 3). 
The 
regression 
equation 
of the best model 
(model 
1, 
Table 
3) was 
used 
to map 
habitat 
suitability 
across 
the 
entire 
study area. 
The 
resulting 
habitat 
suitability 
map 
predicted 
the group 
size of Greater 
Rheas 
in each 
1.5 X 
1.5 km cell. Based 
on our assumption 
that Greater 
Rhea 
group 
size 
is an 
indicator 
of habitat 
suitability, 
model 
output was 
categorized 
into four habitat 
quality 
classes. 
Areas 
where 
group 
sizes of > 
15 individuals 
were defined 
as high quality, group size of five to 15 individuals was 
considered 
moderate 
quality, 
and one 
to five individuals 
was 
defined 
as 
low quality 
habitat. 
Areas 
with 
zero 
individuals were defined as unsuitable habitats (Fig. 1). 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


December 
2008 
IMAGE TEXTURE IN RHEA HABITAT MODELS 
1963 
Table 
3. Most-parsimonious 
models 
selected for estimating habitat 
suitability of Greater Rheas. 
Model 
AICC 
AAICc 
Rz 
Overall 
accuracy 
{%) 
1) y = 23 + 
(1.68 X variance TM 
band4) 
- 
(5.56 X mean TM 
band3) 
163.98 
0 
0.805 
69.4 
+ 
(4.74 X correlation TM 
band4) + 
(1.92 X mean TM 
band4lst) 
- 
(186.32 X NDVI) 
2) y = 33.45 - 
(5.75 X mean TM 
band3) + 
(4.61 X correlation TM 
band4) 
164.03 
0.06 
0.804 
69.4 
+ 
(0.11 X variance TM 
band4lst) + 
(1.84 X mean TM band4) 
- 
(192.6 X NDVI) 
3)y = 30.06 - 
(5.31 X mean TM 
band3) + 
(4.05 X mean TM 
band4) 
165.49 
1.51 
0.797 
58.3 
+ 
(4.76 X correlation TM band4) 
+ 
(0.12 X variance TM 
band4lst) 
- 
(180.63 X NDVI) 
4) y = 70.67 - 
(6.45 X mean TM 
band3) 
- 
(40.92 X homogeneity TM 
band7) 
166.76 
2.78 
0.789 
69.4 
+ 
(4.96 X correlation TM 
band4) + 
(2.03 X mean TM 
band4lst) 
- 
(218.05 X NDVI) 
5) y = 54.01 - 
(6.91 X mean TM 
band3) + 
(4.59 X correlation TM 
band4) 
166.93 
2.95 
0.788 
50.0 
- 
(26.31 X second moment TM 
bandl) 
+ 
(2.11 X mean TM 
band4lst) 
- 
(232.35 X NDVI) 
6) v - 
33.14 - 
(5.84 X mean TM 
band3) + 
(5.08 X correlation TM 
band4) 
167.16 
3.18 
0.787 
63.9 
- 
(34.03 X second moment TM 
band3) + 
(1.96 X mean TM 
band4lst 
) 
- 
(199.32 X NDVI) 
l)y= 
17.58 + 
(1.77 X variance TM 
band4) 
- 
(4.94 X mean TM 
band3) 
167.75 
3.77 
0.784 
55.6 
+ 
(4.15 X mean TM 
band4) + 
(4.85 X correlation TM 
band4) 
- 
(157.56 X NDVI) 
Notes: 
For these models 
AAICC 
compared 
to the highest ranked model was <4. 
The values of AICC, AAICC, R2, and overall 
accuracy 
of leave-one-out 
cross-validation 
procedures 
are shown. The 
superscript "1st" indicates first-order texture variables. 
Discussion 
Our 
models 
represent 
a 
successful 
first attempt 
to 
predict 
areas 
of different 
habitat 
quality 
for Greater 
Rheas 
in grasslands 
of central Argentina. 
According 
to 
our models, 
Greater 
Rhea 
group 
size was 
related 
to the 
spatial 
heterogeneity 
of habitat 
as measured 
by texture 
variables 
and NDVI. 
The 
selection 
of these variables 
is 
likely due 
to use of these resources 
by Greater 
Rheas 
to 
satisfy basic 
foraging 
requirements. 
Image 
texture was 
a crucial 
element 
in the estimation 
of the habitat 
suitability 
map 
for Greater 
Rheas, 
and 
distinguished 
subtle 
variations 
within 
grasslands. 
Sec 
ond-order 
texture measures, 
especially 
correlation, 
were 
most 
efficient 
at 
quantifying 
habitat 
attributes 
that 
influence 
Greater 
Rhea 
group 
size. 
Correlation 
is a 
measure 
of gray 
tone 
linear dependencies 
in the image 
(Baraldi 
and Parmiggiani 
1995). 
Pixels 
near 
each 
other 
are more 
correlated 
than distant 
ones, 
suggesting 
that 
image 
elements 
are aggregated. 
Mean 
texture value was 
included frequently in the best models (Table 3); this 
measure 
represents 
the average 
distribution 
of gray level 
(Dong-Chen and Wang 
1990), hence high values of 
mean 
indicate more 
bright 
areas 
(such 
as bare 
ground 
and grassland), 
and fewer dark 
areas 
(such as forests or 
shadows) 
in an 
image. 
Second-order 
variance 
was 
also 
included 
frequently 
in the best models; 
this measure 
captures 
the 
spatial 
pattern 
of 
gray 
level 
deviation 
(Baraldi and Parmiggiani 1995), and is a good indicator 
of spatial 
heterogeneity. 
Finally, 
two 
texture 
variables 
poorly 
represented 
in the models 
were 
-angular 
second 
moment 
and homogeneity, 
which 
both 
characterize 
the 
textural 
uniformity 
of the image 
elements 
(Baraldi 
and 
Parmiggiani 
1995, Guo 
et al. 2004). 
Among 
the six TM 
bands, 
texture measures 
based 
on 
the near-infrared 
(NIR, 
TM4) 
band 
had 
the greatest 
explanatory 
power 
in relation 
to Greater 
Rhea 
group 
size. Because 
the NIR 
band 
is sensitive 
to vegetation 
and 
the 
amount 
of 
biomass, 
variations 
in 
the 
textural 
characteristics 
of this band 
likely capture 
difference 
in 
vegetation 
cover. 
In grasslands, 
sites with 
higher 
forb 
cover 
and 
higher 
forb 
species 
richness 
have 
higher 
reflectance in NIR 
(Guo et al. 2000, 2004). 
Wild 
forbs and cultivated 
dicotyledons 
are a preferred 
food 
item for Greater 
Rheas 
(Yagueddu 
and Viviani 
Rossi 
1985, Martella 
et al. 
1996). 
Sites 
with 
dense 
grassland 
vegetation 
may 
also 
exhibit greater 
abundance 
of these plants. 
Thus, 
the discrimination 
power 
of image 
texture 
measures 
may 
be 
very 
useful 
for assessing 
vegetation 
heterogeneity, 
indicative 
of dicotyledons, 
within 
grassland. 
The 
inverse 
relationship 
between 
NDVI 
and Greater 
Rhea 
group 
size is most 
likely related 
to the presence 
of 
bare 
soil 
in the area. 
Although 
our 
study 
area 
was 
dominated by grasslands, 14.4% (688 km2) of the area 
consisted 
of nonvegetation 
patches, 
resulting 
from 
human 
activities. 
Dicotyledons 
are 
the most 
common 
species 
in the vegetation 
gaps 
after 
a disturbance 
in 
grassland 
(Bock 
and 
Bock 
1992, Kinucan 
and 
Smeins 
1992, Edward and Crawley 1999, Bullock et al. 2001, 
Hayes 
and 
Holl 
2003) 
because 
herbaceous 
dicots 
dominate 
the initial 
stage of succession 
(Omacini 
et al. 
1995). 
Consequently, 
the areas 
classified 
as bare 
soil 
patches 
were 
likely 
to contain 
an 
abundance 
of 
the 
feeding 
resources 
that Greater 
Rheas 
prefer. Addition 
ally, the reflectance 
of exposed 
ground 
areas might 
affect 
the response 
of red wavelengths 
(TM3; 
Lawrence 
and 
Ripley 
1998, Weis 
et al. 2004) interfering 
with the 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


1964 
LAURA 
M. BELLIS 
ET AL. 
Ecological 
Applications 
Vol. 18, No. 8 
reflectance 
of TM 
band 
3, 
and 
thus 
changing 
the 
expected 
relationship 
between 
the red wavelengths 
and 
Greater 
Rhea 
group 
size. 
The 
habitat 
preferences 
identified 
in our models 
are 
consistent 
with 
field 
studies 
of Greater 
Rhea 
use 
of 
landscapes. 
In both 
grassland 
and 
agricultural 
lands, 
individual 
Greater 
Rheas 
adjust 
their movements 
and 
home 
range 
size in response 
to food availability 
(Bellis 
et 
al. 2004/?), 
and 
they forage 
preferably 
in habitat 
with 
a 
high proportion of dicots (Codenotti and Alvarez 2000, 
Bellis 
et al. 2004a, 
Herrera 
et al. 2004). 
Human 
disturbance 
affects Greater 
Rheas 
negatively, 
and 
illegal hunting 
in particular 
is a major 
conservation 
concern 
(B?cher 
and Nores 
1988, Bellis 
et al. 2004a, 
Martella 
and Navarro 
2006). 
However, 
contrary 
to our 
expectations, 
the anthropogenic 
variables 
included 
in 
this study were 
not 
strong predictors 
of Greater 
Rhea 
distribution. 
It may 
be 
that 
the variables 
we 
used 
to 
quantify 
human 
impact do not adequately 
represent 
the 
threat Greater 
Rheas 
face from humans. 
The 
prediction 
of high-quality 
habitat 
allows 
identi 
fication 
of 
the most 
critical 
areas 
for Greater 
Rhea 
conservation 
within 
this study area. 
The 
assignment 
of 
habitat 
into high, medium, 
low, and unsuitable 
quality 
classes 
was made 
under 
the premise 
that group 
size of 
Rheas 
is a good 
indicator 
of habitat 
quality. 
Individual 
Greater 
Rheas 
select habitats 
where 
the profitability 
of 
feeding 
is counterbalanced 
by the corresponding 
cost of 
pr?dation 
(Codenotti 
and 
Alvarez 
2000, 
Bellis 
et al. 
2004a). Foraging in large groups benefits individuals by 
reducing 
pr?dation 
risk 
through 
the dilution 
effect 
(Fern?ndez 
et al. 2003). 
Additionally, 
as the opportuni 
ties for feeding 
are more 
frequent 
in large groups 
and 
when 
food occurs 
in clumps 
(Beauchamp 
2001), 
we 
are 
able 
to assume 
that habitats 
with 
high 
food abundance 
or quality 
will 
support 
larger groups 
than areas without 
these characteristics. 
The 
validation 
phase 
is important 
in assessing 
the 
predictive 
capability 
of any habitat 
model 
(Guisan 
and 
Zimmermann 
2000, 
Luck 
2002, 
Ottaviani 
et al. 2004). 
For Greater 
Rheas, 
model 
performance 
was moderately 
good 
(cross-validation 
accuracy 
of 
50-69%). 
Low 
abundance 
of Greater 
Rhea 
groups 
and 
high 
natural 
variance 
in group 
size (which 
can 
reach 
50 individuals; 
Reboreda 
and Fern?ndez 
1997) may 
have 
contributed 
to 
the limited predictive 
power 
of the model. 
Despite 
these 
limitations, 
the habitat 
model 
developed 
here 
is an 
important 
first step, and although 
it can be improved, 
it 
is a very 
good 
approach 
to understand 
the habitat 
requirements 
of Greater 
Rheas 
in grassland 
environ 
ment 
at landscape 
scale. 
In 
future work 
it may 
be 
fruitful 
to consider 
an 
alternative 
to the bounded 
leaps procedure 
in the model 
fitting 
stage. 
For 
analysis 
of small 
data 
sets methods 
known 
to be robust 
to overfitting 
include Beiman 
Cutler 
classifications 
(BCC). 
This 
bootstrap 
aggregation 
meth 
od 
is particularly 
powerful 
when 
there 
are many 
explanatory 
variables 
(Lawrence 
et al. 2006). 
Conservation 
Implications 
The majority 
of the study area was 
identified 
by the 
model 
as poor 
quality 
habitat 
where 
large 
groups 
of 
Greater 
Rhea, 
i.e., >15 
individuals, 
are 
unlikely 
to 
occur. 
Argentine 
grassland, 
like most 
of South 
Amer 
ican grassland, 
has experienced 
strong modification 
due 
to human 
land use. 
In San Luis 
province, 
the conversion 
of natural 
to exotic 
grasslands 
and 
agroecosystems 
is 
widespread 
and 
perhaps 
irreversible 
(Demaria 
et al. 
2003). 
Trends 
of expanding 
land use 
lend urgency 
to the 
need 
to preserve 
the 
remaining 
natural 
habitat 
for 
Greater 
Rhea 
and 
for other 
grassland 
species 
as well. 
Our 
results will 
contribute 
to such conservation 
efforts 
by 
clarifying 
important 
predictors 
of Greater 
Rhea 
habitat quality and through spatial explicit depiction of 
the distribution 
of high-quality 
habitat. 
The 
use 
of 
texture 
variables 
derived 
from 
satellite 
images 
is an 
important 
component 
in studies 
of habitat 
because 
it 
captures 
spatial 
heterogeneity 
within 
a given 
land cover 
class at both broad 
and fine scales 
simultaneously. 
Here, 
we 
recommend 
the use of texture analysis 
as a promising 
tool 
in the modeling 
of habitat 
suitability. We 
consider 
that managers 
can use predictive 
models 
such as those 
derived here to identify areas that will support high 
abundance 
of individuals 
and predict 
the consequences 
of land use on patterns 
of occurrence 
and abundance 
of 
wildlife 
species. 
Acknowledgments 
We 
thank the Comisi?n 
Nacional 
de Actividades 
Espaciales 
(CONAE) 
and staff of Instituto de Altos Estudios 
Espaciales 
"Mario Gulich" 
for providing 
the satellite images and technical 
support. We 
are very grateful to N. Keuler, 
C. Alc?ntara, 
M. 
Morales, 
and T. Sickley, who kindly shared their knowledge 
to 
improve different aspects 
of the work. We 
also 
thank P. E. 
Osborne 
and F. Huettmann 
for their reviews, which 
greatly 
improved the manuscript. 
Financial 
support was provided 
for 
M. 
B. Martella 
and J. L. Navarro 
from Consejo 
Nacional 
de 
Investigaciones 
Cient?ficas 
y T?cnicas 
(CONICET), 
Agencia 
Nacional 
de Promoci?n 
Cient?fica y Tecnol?gica 
(FONCYT), 
and Secretar?a de Ciencia 
y T?cnica 
of the Universidad 
Nacional 
de C?rdoba, 
Argentina 
(SECyT). 
L. M. Bellis was supported by 
postdoctoral 
and training fellowships from CONICET. 
Literature 
Cited 
Anderson, 
D. L. 
1973. La distribuci?n 
de Sorghastrum pellitum 
(Poaceae) 
en 
la provincia 
de San Luis 
y su significado 
ecol?gico. 
Kurtziana 
12:37-45. 
Anderson, 
D. L., J. A. Del ?guila, 
and A. E. Bernardon. 
1970. 
Las 
formaciones 
vegetales 
de 
la provincia 
de San Luis. 
Revista 
de 
Investigaci?n 
Agropecuaria 
INTA, 
Serie 
2, 
Biolog?a 
y Producci?n 
Vegetal 
7:83-153. 
Balbont?n, 
J. 2005. 
Identifying suitable habitat for dispersal 
in 
Bonelli's 
eagle: 
an important 
issue in halting 
its decline 
in 
Europe. 
Biological 
Conservation 
126:74-83. 
Baraldi, 
A., 
and F. Parmiggiani. 
1995. An 
investigation 
of 
textural characteristics 
associated 
with gray level co-occur 
rence matrix 
statistical parameters. 
IEEE 
Transactions 
on 
Geoscience 
and Remote 
Sensing 33:293-304. 
Beauchamp, 
G. 
2001. 
Should 
vigilance 
always 
decrease with 
group size? Behavioral 
Ecology 
and Sociobiology 
51:47-52. 
Bellis, L. M. 
2004. 
Selecci?n 
de habitat 
y productividad 
en 
?and?es. 
Thesis. 
Facultad 
de Ciencias 
Exactas 
F?sicas 
y 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


December 2008 
IMAGE TEXTURE IN RHEA HABITAT MODELS 1965 
Naturales, 
Universidad 
Nacional 
de C?rdoba, 
C?rdoba, 
Argentina. 
Bellis, L. M., M. B. Martella, 
and J. L. Navarro. 
2004?. Habitat 
use by wild and captive-reared 
greater rheas in agricultural 
landscapes. Oryx 38:304-310. 
Bellis, L. M., M. B. Martella, 
J. L. Navarro, 
and P. E. Vignolo. 
2004&. Home 
range of greater and lesser rhea in Argentina: 
relevance to conservation. 
Biodiversity 
and Conservation 
13: 
2589-2598. 
Bertonatti, 
C, 
and 
J. Corcuera. 
2000. 
The 
state of 
the 
environment 
in Argentina. 
Environmental 
situation Argenti 
na 2000. Fundaci?n 
Vida 
Silvestre Argentina, 
Buenos Aires, 
Argentina. 
Bock, 
J. H, 
and C. E. Bock. 
1992. Vegetation 
responses 
to 
wildfire in native versus exotic Arizona 
grassland. 
Journal of 
Vegetation 
Science 
3:439-446. 
Bruning, 
D. 
F. 
1974. 
Social 
structure 
and 
reproductive 
behaviour 
in the Greater 
Rhea. 
Living Bird 
13:251-294. 
B?cher, E. H, 
and M. Nores. 
1988. Present 
status of birds in 
steppes and 
savannas 
of northern and central Argentina. 
Pages 
71-79 
in P. D. 
Gorioup, 
editor. 
Ecology 
and 
conservation 
of grassland 
birds. 
International 
Council 
for 
Bird Preservation 
Technical 
Publication 
Number 
7, Cam 
bridge, UK. 
Buckland, 
S. T., D. B. Anderson, 
K. P. Burnham, 
J. L. Laake, 
D. 
L. 
Borchers, 
and L. Thomas. 
2001. 
Introduction 
to 
distance 
sampling. 
Estimating 
abundance 
of biological 
populations. 
Oxford 
University 
Press, New 
York, 
New 
York, USA. 
Bullock, 
J. M., 
J. Franklin, M. 
J. Stevenson, 
J. Silvertown, S. J. 
Coulson, 
S. J. Gregory, 
and R. Tofts. 
2001. A plant 
trait 
analysis of responses 
to grazing 
in a long-term experiment. 
Journal of Applied 
Ecology 
38:253-267. 
Burnham, K. P., and D. R. Anderson. 
2002. Model 
selection 
and multimodel 
inference: a practical 
information-theoretic 
approach. 
Springer, New York, New York, USA. 
Caughley, 
G. 
1974. Bias 
in aerial 
survey. Journal of Wildlife 
Management 
38:921-933. 
Caughley, G., and A. R. E. Sinclair. 
1994. Wildlife 
ecology and 
management. 
Blackwell 
Scientific, Cambridge, 
Massachu 
setts, USA. 
Codenotti, 
T. L., and F. Alvarez. 
2000. Habitat 
use by Greater 
Rheas 
in an agricultural 
area of Southern Brazil. Revista 
de 
Etologia 
2:77-84. 
Demaria, 
M. R., W. 
J. McShea, 
K. Koy, 
and N. O. Maceira. 
2003. Pampas 
deer conservation 
with respect to habitat 
loss 
and protected 
area considerations 
in San Luis, Argentina. 
Biological 
Conservation 
115:121-130. 
D?az-Zorita, 
M., G. A. Duarte, 
and J. H. Grove. 
2UU2. A review 
of no-till systems and soil management 
for sustainable 
crop 
production 
in the subhumid 
and 
semiarid 
Pampas 
of 
Argentina. 
Soil and Tillage Research 
65:1-18. 
Dong-Chen, 
H, 
and L. Wang. 
1990. Texture 
unit, texture 
spectrum, 
and 
texture analysis. 
IEEE 
Transactions 
on 
Geoscience 
and Remote 
Sensing 28:509-512. 
Edward, 
G. R., 
and M. 
J. Crawley. 
1999. Herbivores, 
seed 
banks and seedling recruitment in mesic grassland. 
Journal of 
Applied 
Ecology 
87:423-435. 
Elith, 
J., et al. 2006. Novel 
methods 
improve prediction 
of 
species1 distributions 
from occurrence 
data. Ecography 
29: 
129-151. 
ENVI. 
2004. Environment 
for visualizing 
images. Version 
4.1. 
Research 
Systems, Boulder, Colorado, 
USA. 
Estevez, 
I., I. L. Andersen, 
and E. Nasvdal. 
2007. Group 
size, 
density and social dynamics 
in farm animals. Applied Animal 
Behaviour 
Science 
103:185-204. 
Fern?ndez, 
G. 
J., A. F. Capurro, 
and J. C. Reboreda. 
2003. 
Effect of group size on individual and collective vigilance 
in 
Greater Rheas. 
Ethology 
109:413-425. 
Furnival, G. M., 
and R. W. Wilson, 
Jr. 1974. Regressions 
by 
leaps and bounds. Technometrics 
16:499-511. 
Gibson, 
L. A., B. A. Wilson, 
D. M. 
Cahill, 
and J. Hill. 
2004. 
Modeling 
habitat 
suitability 
of 
the swamp 
antechinus 
{Antechinus minimus maritimus) 
in the coastal heathlands 
of 
southern Victoria, 
Australia. 
Biological 
Conservation 
117: 
143-150. 
Giordano, 
P. F., L. M. 
Bellis, 
J. L. Navarro, 
and M. 
B. 
Martella. 
2008. 
Abundance 
and 
spatial 
distribution 
of 
Greater 
Rhea 
Rhea 
americana 
in two sites of the pampas 
grasslands 
with 
different 
land 
use. 
Bird 
Conservation 
International 
18:63-70. 
Gottschalk, 
T. K., F. Huettmann, 
and M. Ehlers. 2005. Thirty 
years of analyzing 
and modeling 
avian habitat 
relationships 
using satellite imagery data: 
a review. International 
Journal 
of Remote 
Sensing 26:2631-2656. 
Guisan, 
A., and N. E. Zimmermann. 
2000. Predictive 
habitat 
distribution models 
in ecology. 
Ecological 
Modeling 
135: 
147-186. 
Guo, 
X., K. P. Price, and J. M. 
Stiles. 2000. Biophysical 
and 
spectral characteristics 
of three land management 
practices 
on cool 
and warm 
season 
grasslands 
in eastern Kansas. 
Natural 
Resources 
Research 
9:321-331. 
Guo, 
X., 
J. Wimshurst, 
S. McCanny, 
P. Fargey, 
and P. 
Richard. 
2004. Measuring 
spatial and vertical heterogeneity 
of grassland 
using 
remote 
sensing 
techniques. 
Journal 
of 
Environmental 
Informatics 3:24-32. 
Haralick, 
R. M., 
K. 
Shanmugan, 
and 
I. Dinstein. 
1973. 
Textural 
features for image classification. 
IEEE Transactions 
on System, Man, 
and Cybernetics 
SMC-3:610-621. 
Hayes, G. E., and K. D. Holl. 
2003. Cattle grazing impacts on 
annual 
forbs and vegetation composition 
of mesic grasslands 
in California. 
Conservation 
Biology 
17:1694-1702. 
Hepinstall, 
J. A., 
and 
S. A. 
Sader. 
1997. Using 
Bayesian 
statistics, Thematic Mapper 
satellite imagery, and breeding 
bird data 
to model 
bird species probability 
of occurrence 
in 
Maine. 
Photogrammetic 
Engineering 
and Remote 
Sensing 
63:1231-1237. 
Herrera, 
L. P., V. M. 
Comparatore, 
and P. Laterra. 
2004. 
Habitat 
relations of Rhea americana 
in an agroecosystem 
of 
Buenos 
Aires Province, Argentina. 
Biological 
Conservation 
119:363-369. 
Hurvich, 
C. M., 
and C. L. Tsai. 
1989. Regression 
and 
time 
series model 
selection 
in small samples. Biometrika 
76:297 
307. 
IUCN 
(International 
Union 
for Conservation 
of Nature 
and 
Natural 
Resources). 
2007. 
IUCN 
red 
list of threatened 
species, 
(www.iucnredlist.org) 
Kinucan, 
R. J., and F. E. Smeins. 
1992. Soil seed bank of a 
semiarid Texas 
grassland 
under 
three long-term (36-years) 
grazing regimes. American Midland 
Naturalist 
128:11-21. 
Knick, 
S. T., and J. T. Rotenberry. 
2000. Ghosts 
of habitats 
past: 
contribution 
of landscape 
change 
to current habitats 
used by shrubland birds. Ecology 
81:220-227. 
Lawrence, 
R. L., and W. 
J. Ripley. 
1998. Comparisons 
among 
vegetation 
indices and band wise 
regression 
in a highly 
disturbed, 
heterogeneous 
landscape: 
Mount 
St. Helens, 
Washington. 
Remote 
Sensing of Environment 
64:91-102. 
Lawrence, 
R. L., S. D. Wood, 
and R. L. Sheley. 2006. Mapping 
invasive plants 
using hyperspectral 
imagery and Breiman 
Cutler 
classifications 
(RandomForest). 
Remote 
Sensing 
of 
Environment 
100:356-362. 
Laymon, 
S. A., and S. H. Barrett. 
1986. Developing 
and testing 
habitat-capability 
models: 
pitfalls 
and 
recommendations. 
Pages 
87-92 
in J. Verner, M. 
L. Morrison, 
and C. J. Ralph, 
editors. Wildlife 
2000. Modeling 
habitat 
relationships 
in 
terrestrial vertebrates. University 
of Wisconsin 
Press, Mad 
ison, Wisconsin, 
USA. 
Legendre, 
P., M. 
R. T. Dale, M. 
J. Fortin, 
J. Gurevitch, 
M. 
Hohn, 
and D. Myers. 
2002. The 
consequences 
of spatial 
structure 
for the design 
and 
analysis 
of ecological 
field 
surveys. Ecography 
25:601-615. 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions


1966 
LAURA 
M. 
BELLIS 
ET AL. 
Ecological 
Applications 
Vol. 18, No. 8 
Le?n, 
R. 
J. C, 
G. M. 
Rusch, 
and M. 
Oesterheld. 
1984. 
Pastizales 
pampeanos: 
impacto agropecuario. 
Phytocoenolo 
gia 12:201-218. 
Luck, G. W. 
2002. The 
habitat 
requirements 
of the rufous 
treecreeper (Climacteris 
rufa). 2. Validating 
predictive habitat 
models. 
Biological 
Conservation 
105:395^403. 
Luoto, M., M. Kuussaari, 
and T. Toivonen. 
2002. Modelling 
butterfly distribution 
based on remote sensing data. Journal 
of Biogeography 
29:1027-1037. 
Luoto, M., 
R. Virkkala, 
R. Heikkinen, 
and K. Rainio. 
2004. 
Predicting 
bird 
species 
richness using 
remote 
sensing 
in 
boreal agricultural-forest mosaic. 
Ecological 
Applications 
14: 
1946-1962. 
MacArthur, 
R. H, 
and J. W. MacArthur. 
1961. On bird species 
diversity. Ecology 
42:594-598. 
Martella, 
M. 
B., and J. L. Navarro. 
2006. Proyecto ?and?. 
Manejo 
de Rhea 
americana 
y R. pennata 
en la Argentina. 
Pages 
39-50 
in M. L. Bolkovic 
and D. E. Ramadori, 
editors. 
Manejo 
de Fauna 
en Argentina: 
Proyectos 
de Uso 
Sustent 
able. Direcci?n 
de Fauna 
Silvestre?Secretar?a 
de Ambiente 
y Desarrollo 
Sustentable, 
Buenos Aires, Argentina. 
Martella, 
M. B., J. L. Navarro, 
J. M. G?nnet, 
and S. A. Monge. 
1996. Diet 
of Greater Rheas 
in an agroecosystem 
of central 
Argentina. 
Journal of Wildlife Management 
60:586-592. 
Martella, M. B., D. Renison, 
and J. L. Navarro. 
1995. Vigilance 
in the Greater Rheas: 
effects of vegetation height and group 
size. Journal of Field Ornithology 
66:215-220. 
McAlpine, 
C. A., 
and T. 
J. Eyre. 
2002. Testing 
landscape 
metrics 
as indicators 
of habitat 
loss and fragmentation 
in 
continuous 
eucalypt 
forests (Queensland, 
Australia). 
Land 
scape Ecology 
17:711-728. 
Meisel, 
J. E., and M. G. Turner. 
1998. Scale detection 
in real 
and artificial landscapes 
using semivariance 
analysis. Land 
scape Ecology 
13:347-362. 
Miller, A. J. 2002. Subset 
selection in regression. Monographs 
on Statistics 
and Applied 
Probability 
95. Chapman 
and 
Hall/CRC, 
Boca Raton, 
Florida, USA. 
Mladenoff, 
D. 
J., T. A. 
Sickley, R. G. Haight, 
and A. 
P. 
Wydeven. 
1995. A regional landscape analysis and prediction 
of favorable 
gray wolf habitat 
in the Northern Great 
Lakes 
Region. 
Conservation 
Biology 
9:279-294. 
Nagendra, 
H. 2001. Using 
remote sensing to assess biodiversity. 
International 
Journal of Remote 
Sensing 22:2377-2400. 
Neter, 
J., W. Wasserman, 
and M. Kenter. 
1990. Applied 
linear 
statistical models. 
Irwin, Boston, Massachusetts, 
USA. 
Oesterheld, M., C. M. Dibella, 
and H. Kerdiles. 
1998. Relation 
between NOAA-AVHRR 
satellite data and stocking rate of 
rangelands. 
Ecological 
Applications 
8:207-212. 
Omacini, M., E. J. Chaneton, 
R. J. C. Le?n, 
and W. B. Batista. 
1995. Old-field 
successional 
dynamics on the Inland Pampa, 
Argentina. 
Journal of Vegetation 
Science 6:309-316. 
Osborne, 
P. E., J. C. Alonso, 
and R. Bryant. 2001. Modeling 
landscape-scale 
habitat use using GIS 
and remote sensing: a 
case study with great bustards. 
Journal of Applied 
Ecology 
38:458-471. 
Ottaviani, 
D., 
G. 
J. Lasinio, 
and L. 
Boitani. 
2004. 
Two 
statistical methods 
to validate 
habitat 
suitability models 
using presence-only 
data. Ecological 
Modeling 
179:417-443. 
Paruelo, 
J. M., 
H. 
E. Epstein, W. 
K. 
Lauenroth, 
and 
I. C. 
Burke. 
1997. ANPP 
estimates 
from NDVI 
for the central 
grassland 
region of the U.S. 
Ecology 
78:953-958. 
Posillico, M., A. Meriggi, 
E. Pagnin, 
S. Lovari, 
and L. Russo. 
2004. A habitat model 
for brown bear conservation 
and land 
use planning 
in central Apennines. 
Conservation 
Biology 
118:141-150. 
Posse, G., 
and A. M. 
Cingolani. 
2004. A 
test of the use of 
NDVI 
data 
to predict 
secondary 
productivity. 
Applied 
Vegetation 
Science 7:201-208. 
R Development 
Core 
Team. 
2007. 
R: 
a 
language 
and 
environment 
for statistical 
computing. 
R Foundation 
for 
Statistical 
Computing, 
Vienna, 
Austria. 
(http://www. 
r-project.org) 
Reboreda, 
J. C, 
and G. Fern?ndez. 
1997. Sexual, 
seasonal 
and 
group 
size differences 
in the allocation 
of time between 
vigilance and feeding in the Greater Rhea 
{Rhea americana). 
Ethology 
103:198-207. 
St-Louis, V., A. M. 
Pidgeon, V. C. Radeloff, 
T. J. Hawbaker, 
and M. K. Clayton. 
2006. 
Image 
texture in high-resolution 
remote sensing images as predictor of bird species richness. 
Remote 
Sensing of Environment 
105:299-312. 
Sun, B., S. Zhou, 
and Q. Zhao. 
2003. Evaluation 
of spatial and 
temporal 
changes 
of soil quality 
based 
on geostatistical 
analysis 
in the hill region of subtropical 
China. 
Geoderma 
115:85-99. 
Sutherland, W. 
1996. Ecological 
census 
techniques: 
a hand 
book. Cambridge 
University 
Press, Cambridge, 
UK. 
Thompson, 
W. 
L. 
2002. 
Towards 
reliable 
bird 
survey: 
accounting 
for individuals 
present but not detected. Auk 
119:18-25. 
Tso, B., and P. M. Mather. 
2001. Classification 
methods 
for 
remotely sensed data. Taylor 
and Francis, New York, New 
York, USA. 
Turner, W., 
S. Spector, N. Gardiner, M. Fladeland, 
E. Sterling, 
and M. 
Steininger. 
2003. Remote 
sensing for biodiversity 
science and conservation. 
Trends 
in Ecology 
and Evolution 
18:306-314. 
Tuttle, E. M., R. R. Jensen, V. A. Formica, 
and R. A. Gonser. 
2006. Using 
remote sensing image texture to study habitat 
use patterns: 
a case 
study using 
the polymorphic 
white 
throated sparrow {Zonotrichia 
albicolis). Global 
Ecology 
and 
Biogeography 
15:349-357. 
Weis, 
J. J., D. 
S. Gutzler, 
J. E. Allred Coonrod, 
and C. N. 
Dahm. 
2004. Long-term 
vegetation monitoring 
with NDVI 
in a diverse 
semi-arid 
setting, central New Mexico, 
USA. 
Journal of Arid Environments 
58:248-271. 
Whittingham, 
M. 
J., P. A. Stephens, R. B. Bradbury, 
and R. P. 
Freckleton. 
2006. Why 
do we still use stepwise modelling 
in 
ecology and behaviour? 
Journal of Animal 
Ecology 
75:1182 
1189. 
Yagueddu, 
C, 
and E. Viviani 
Rossi. 
1985. Botanical 
compo 
sition of Greater 
Rhea 
{Rhea americana 
albescens) 
diet in a 
grassland 
of Buenos 
Aires 
pampas. 
Res?menes 
del XI 
Congreso 
Argentino 
de Producci?n 
Animal, 
Corrientes, 
Argentina. 
[In Spanish.] 
SUPPLEMENT 
Raw 
data used in statistical analysis of Greater Rhea 
habitat models 
(Ecological 
Archives AO18-071-SI). 
This content downloaded  on Thu, 20 Dec 2012 01:36:17 AM
All use subject to JSTOR Terms and Conditions
