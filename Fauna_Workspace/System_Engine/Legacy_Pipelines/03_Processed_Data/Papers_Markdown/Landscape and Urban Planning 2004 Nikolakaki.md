--- 
source: Landscape and Urban Planning 2004 Nikolakaki.pdf
--- 

Landscape and Urban Planning 68 (2004) 77–94
A GIS site-selection process for habitat creation:
estimating connectivity of habitat patches
Pantoula Nikolakaki∗
Environmental Services, Oxfordshire County Council, Speedwell House, Speedwell Street, Oxford OX1 1NE, UK
Received 15 October 2002; received in revised form 23 June 2003; accepted 2 July 2003
Abstract
The paper presents a method that addresses the problem of site-selection for habitat creation involving spatial processes on
the landscape scale. It interprets landscape ecological principles, with focus on population dynamics, to speciﬁc information
required to support a particular decision at each stage of the process. The approach focuses on deciduous woodland with
the redstart Phoenicurous phoenicurous as an umbrella species for woodland birds and is illustrated within the fragmented
landscape of the east midlands area of England. The method requires the use of a Geographic Information System (GIS) to
estimate the connectivity of habitat patches. Each patch is assigned a “cost” value that represents the cost of dispersal over a
friction surface. The sites are ranked accordingly and, in combination with the spatial context and size, are prioritised in terms
of their potential for forming cores for habitat creation. Habitat patches with low cost values, a large area of surrounding habitat
and small size were identiﬁed as potential sites for expansion in order to satisfy the minimum requirements of the species.
The approach is generic, applicable to any species, and despite its limitations it can be a useful aid in conservation planning.
© 2003 Elsevier B.V. All rights reserved.
Keywords: Birds; Conservation planning; Connectivity; GIS; Habitat fragmentation; Population dynamics
1. Introduction
Human activities such as agricultural development,
commercial conifer afforestation and urbanisation
have led to habitat fragmentation, namely loss of
the original habitat, reduction in habitat patch size
and increasing isolation of habitat patches (Andrén,
1994). These processes result in heterogeneous land-
scapes, which are composed of more or less isolated,
smaller patches of suitable habitat within a matrix of
less suitable habitat for reproduction or for providing
food and shelter for species conﬁned to the original
∗Present address: 9 Beauchamp Place, Cowley, Oxford OX4
3NE, UK. Tel.: +44-1865-773262.
E-mail address: pantoula@yahoo.co.uk (P. Nikolakaki).
habitat. The process of landscape change as a result of
habitat fragmentation has far-reaching consequences
for species survival. In particular, for area-sensitive
species, the patches of suitable habitat may be too
small to support a breeding pair or a functional so-
cial group (Lambeck, 1997), whereas species with
low dispersal capacity are unable to recolonize the
habitat patches following the extinction of their local
populations (Collinge, 1996).
Empirical evidence suggests that the population
dynamics for a wide range of organisms living in
fragmented landscapes, and particularly for small
mammals, invertebrates and birds, follow a pattern of
stochastic local extinctions and recolonisations, thus
occurring as metapopulations (Opdam et al., 1985;
Opdam, 1991; Hanski, 1994). Landscape ecology
0169-2046/$20.00 © 2003 Elsevier B.V. All rights reserved.
doi:10.1016/S0169-2046(03)00167-1


78
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
provides the context for studying the effects of the
modiﬁed landscape pattern on species’ population
dynamics and hence the distribution and survival of
organisms. It considers the crucial role that movement
plays in the dynamics of many populations and the
importance of habitat connectivity as a determinant
of conservation value. The degree to which local pop-
ulations are functionally connected (connectivity) has
an inﬂuence on the persistence of the metapopulation
(Fahrig and Merriam, 1985).
Forest fragmentation is regarded as one of the most
serious threats to birds today (Willson et al., 1994).
The majority of the investigations on specialised
woodland birds show lower frequency of occurrence
in the smallest and most isolated woods. This paper
presents a methodological spatial approach based on
a Geographic Information System (GIS) that (1) iden-
tiﬁes the optimal habitat patches that have a greater
probability of occupancy and (2) identiﬁes the most
Fig. 1. The Sherwood Forest study area within the boundaries of the County of Nottinghamshire.
effective sites for woodland creation, by selecting
the least isolated patches with a greater probability
of colonisation. Within this context, the method uses
the dispersal model COST and estimates the degree
of isolation or inversely the degree of connectivity of
habitat patches in the landscape. Sites that are located
in a high-connectivity landscape are most suited for
species occupation and therefore are given priority
status for habitat creation. The method interprets land-
scape ecological principles, with focus on population
dynamics, to speciﬁc information required to support
a particular decision at each stage of the process. The
spatial requirements of a locally threatened woodland
bird formed the criteria that informed the procedure.
The approach can be an effective tool in conservation
planning aimed at enhancing habitat for area-sensitive
woodland birds.
There has so far been a plethora of advice for new
planting at the level of the individual site (Forestry


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
79
Authority, 1994). Little or no account has been taken,
in woodland planting schemes in England (e.g. Farm
Woodland Premium Scheme), of the wider landscape
and spatial parameters such as patch size, differing dis-
persal distances of species and habitat density in the
neighbourhood. This approach employs a large-scale
view where habitat patches are not regarded as inde-
pendent and individual sites, but rather as units con-
nected functionally by spatial processes in a landscape.
Site-based physical factors as well as socio-economic
constraints were not involved within the remit of this
work.
The methodology is discussed using the Sherwood
Forest area in England as a case study (Fig. 1).
The study area is 101,227 km2 and much of its na-
tive oak-birch woodland is on Sherwood sandstone
and acidic sandy soils. Intensiﬁcation of agriculture,
large-scale conifer planting and urban growth have
caused fragmentation of the ancient and semi-natural
woodland, reducing its total area to 8.7% and leav-
ing 45.5% of the study area entirely as arable land.
Although the approach refers to a chosen landscape
and to the group of woodland birds, it has general
applicability and is ﬂexible. Furthermore, it does not
focus on the creation of new patches, but on targeting
existing, potential woodland sites for expansion con-
verting arable cropping to deciduous woodland. This
would give greater opportunities for local species
to disperse into the new woodland and for existing
populations to increase.
2. Aspects of population dynamics in
fragmented landscapes
The study is largely based on an extensive literature
review of theoretical and empirical landscape eco-
logical studies, which examined the impact of patch
size, habitat quality and isolation on the survival of
fragmented populations, and of woodland birds in
particular. The results of these studies guided decision
making during the process of site-selection.
Decreasing rate of recolonization with increasing
isolation and decreasing rate of extinction with in-
creasing patch area are very robust ﬁndings applying to
the population dynamics of the vast majority of species
in fragmented landscapes (Hanski, 1994). With respect
to avian populations, it is acknowledged from the
literature that the assemblages of woodland birds and
the dynamics of local populations of many bird species
in these woodland fragments are affected by the size of
the fragments and their degree of isolation or their de-
gree of connectivity. The two latter attributes are often
demonstrated as the distance to other woodland frag-
ments or as their spatial conﬁguration (e.g. the num-
ber of corridors and/or the amount of habitat around a
patch) (Komdeur and Gabrielsen, 1995; Bellamy et al.,
1996a). In particular, the probability of occurrence of
many woodland birds is shown to be positively corre-
lated with the distance to an extensive woodland area
and with the area of the surrounding suitable habi-
tat, often measured within a 2 or 3 km radius of the
boundaries of a woodland patch (Opdam et al., 1985;
Harms and Opdam, 1990; Hinsley et al., 1994a,b).
Immigration from the surrounding landscape may
also beneﬁt local populations by reducing the risk of
extinction, known as the “rescue effect” (Brown and
Kodric-Brown, 1977; Bellamy et al., 1996b).
Moreover, the number of breeding pairs and wood-
land area are strongly correlated, and the probability
of extinction shows a strong negative relationship
with both for most woodland interior birds (Verboom
et al., 1991; Bellamy et al., 1996b). In particular,
the chance of a local population becoming extinct
increases rapidly below a population size of about
3–5 breeding pairs (Bellamy et al., 1996b). The oc-
currence of most woodland birds is dependent upon
a minimal area of critical habitat available in order to
satisfy foraging needs and territory size requirements
(Moore and Hooper, 1975; Lynch and Whigham,
1984; Opdam et al., 1985). It has been suggested
that lack of resources and increased level of preda-
tion in small patches may cause high mortality of
woodland specialists, whereas poor breeding success
would further result in high extinction rates (Sparks
et al., 1994). In particular, it is shown that for many
area-sensitive woodland species the probability of
breeding is strongly positively related to woodland
area, approaching 100% when 10 ha or more (Hinsley
et al., 1994a,b). McIntyre (1995) also found that
there is a threshold of 10 ha, above which inte-
rior species are present and avian diversity is high
and indistinguishable from that in larger contiguous
woodland.
Large habitat patches support large populations
that have a very low probability of extinction and


80
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
can persist for long periods of time, provided there
is an exchange of at least a few individuals per
generation with other populations (Franklin, 1980;
Verboom et al., 1993). These large populations may
act as sources of dispersing individuals that colonise
neighbouring patches, and thus have a stabilising role
for other smaller local populations (Verboom et al.,
1993). Source populations should comprise at least
20–50 breeding pairs to have a good chance of sur-
viving any kind of stochastic events in the long term
(Franklin, 1980).
3. Selection of an umbrella species
Although the approach aimed at the conservation
of a range of woodland birds, in-depth literature
review has emphasised the need for a single-species
approach to address the problem of site-selection.
Species differ in their territory size, their dispersal
ability and their perception of the landscape pattern.
Consequently, they respond differently to the struc-
ture of the landscape even within the same taxonomic
group (Wiens et al., 1997). Species whose popula-
tions are limited by the pattern of landscape attributes
such as habitat area or connectivity are most vulner-
able to habitat fragmentation. Therefore, species with
the most demanding requirements for these attributes,
known as umbrella species, may be selected to deﬁne
the minimum acceptable value for each landscape pa-
rameter (Simberloff, 1998). The umbrella species that
was selected has such habitat requirements that many
other species with lesser or similar requirements and
autecological behaviour were also assumed to beneﬁt
from the selected sites.
The migratory passerine redstart (Phoenicurus
phoenicurus), characteristic of the avian fauna of Sher-
wood Forest, was chosen. The species favours mature,
deciduous woodland but has been experiencing a
population decline in recent years as a result of habi-
tat change and loss in the breeding grounds (Carter,
1995). Research shows that populations of redstarts
are affected by fragmentation, showing strong effects
of area and isolation (Opdam et al., 1985; Cramp,
1988). Loss of woodland habitat has led to the re-
striction of the species in smaller fragments, where
competition for the available tree holes for nesting is
higher.
3.1. Habitat requirements of the redstart
In
addition
to
the
information
about
spatial
processes in avian populations, scientiﬁc literature
ﬁndings and consultation with experts about the be-
haviour of the species provided the framework for the
site-selection procedure. Moore and Hooper (1975),
in their study of British woods, found that there was
a minimum area of about 2.5 ha, below which there
was no likelihood of ﬁnding a breeding pair of red-
starts. However, the greatest occurrence of redstarts
was found between 10 and 100 ha (Winspear, 1991).
Furthermore, empirical studies have shown that the
spatial structure of the surrounding landscape signif-
icantly affects patch occupancy and colonisation by
redstarts. In particular, the probability of occurrence
of the species increased with an increase in the area
of woodland within a 3 km radius of the target wood’s
perimeter (Opdam et al., 1985). It has also been sug-
gested that the redstart has a short dispersal distance
(Wilson, British Trust for Ornithology, personal com-
munication). Taking into account issues of population
dynamics in fragmented landscapes and the habitat
requirements of the redstart, with regard to area and
isolation parameters, a series of decision rules were
formulated:
• Provided the predecline population density in
British woods is approximately 0.6–0.8 pairs/ha
(Cramp, 1988), a minimum size of 5 ha was as-
sumed to be sufﬁcient to support a local population
of 3–5 breeding pairs.
• Likewise, habitat patches of 50 ha and over consist-
ing of mature deciduous woodland could support a
population of 30–50 pairs that would be viable in
the longer term.
• The area of woodland within a 3 km radius of
the target wood’s perimeter is found to be a good
predictor of the degree of isolation.
• During the breeding period, daily movements across
arable land for feeding and breeding purposes range
from only a few hundred metres up to approximately
700 m.
Identiﬁcation of suitable sites for habitat expan-
sion on the basis of the above spatial criteria would
favour the population persistence of threatened red-
starts and prevent them from further decline. Other


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
81
area-sensitive and sedentary species would also
beneﬁt from the suggested sites.
4. Site-selection process
There were three stages involved in the site-selection
process. These were based not only on aspects of
population dynamics but also on the functionalities of
GIS.
1. Identiﬁcation of the source populations: The paper
develops a method for identifying the best po-
tentially suitable habitat patches that can support
breeding populations of redstarts and other species,
and function as permanent sources of dispersal.
It translates a considerable amount of literature
to clearly articulated selection criteria. Habitat
suitability was determined by incorporating the
factors of patch size, habitat quality and spatial
context. Each of these factors was converted to
a GIS map layer. The overlay of the layers com-
posed the feasible area of those habitat patches that
met the necessary conditions for the occurrence
of the species. The results were also validated by
observations of biologists familiar with the area.
2. Estimation of connectivity: The model COST was
used to simulate dispersal from the set of sources
and estimate the potential connectivity of any site
in the landscape. It took into account not only the
distance from the sources but also barriers and the
underlying heterogeneity of the landscape, quanti-
fying their effect on dispersal.
3. Prioritisation of sites for habitat creation: The rela-
tive patch connectivity formed the basis from which
to infer how accessible a woodland patch was from
the set of the source populations. The effect of patch
size on the extinction probability of local popula-
tions as well as the role of dispersal from surround-
ing suitable habitat were further taken into account
to predict the occupancy state of patches, and pri-
oritise them accordingly for habitat creation.
In the face of limited scientiﬁc information, partic-
ularly about distribution of species, it is essential to
provide a rational, explicit basis on which to make
decisions in a planning procedure. The strategy in
this paper was to incorporate as much credible sci-
entiﬁc information as possible to create a model of
spatial habitat value in a GIS format. The resulting
maps of each stage can support decision-making in lo-
cal land-use planning. Besides the model COST, GIS
overlay and classiﬁcation operations were the back-
bone of the analysis. In particular, classiﬁcations based
on Boolean logic were widely used; areas not fulﬁll-
ing the required conditions were excluded from further
consideration, while the remaining areas that satisﬁed
certain criteria established the suitable locations. In ad-
dition, operations for describing the landscape pattern
such as estimation of the area of individual patches and
measurement of the spatial context were carried out.
IDRISI for Windows (version 1.0), a raster-based
software, was used and a 20 m resolution was
deﬁned. Digital data of the land uses, ancient wood-
land and County Wildlife Sites were provided by
Nottinghamshire County Council. Of the land uses
data, the layer of deciduous woodland was isolated
for the purposes of the analysis.
4.1. Identiﬁcation of the sources
4.1.1. Patch size and isolation
Woodland patches of at least 50 ha were the ﬁrst to
be identiﬁed, as they would have a greater likelihood
of being occupied by viable breeding populations of
redstart and would provide a large number of dis-
persing colonists for local recolonizations (Urban
and Shugart, 1986; Knaapen et al., 1992). Such large
woods would most likely support breeding popula-
tions of other woodland specialists (e.g. nuthatch,
treecreeper, marsh tit and long-tailed tit) that require
large patch sizes of woodland habitat (Fuller et al.,
1995). Moreover, patches large enough to sustain a
viable population of a given specialist species should
also have large populations of generalist species (e.g.
chafﬁnch, blackbird and blue-tit) which are less de-
manding in habitat patch size (Fuller and Warren,
1991). These woods were also assumed to comprise a
good habitat, since large patches generally tend to have
a greater diversity of habitats (Bellamy et al., 1997).
Although a larger area is less affected by isola-
tion (Harms and Knaapen, 1988), immigration from
the surrounding landscape to the sources would still
remain important in order to greatly minimise rare
cases of local extinctions (Harms and Opdam, 1990).
Hence, the area of deciduous woodland within a range
of 3 km of the identiﬁed large woods was estimated


82
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
as a variable that determined their degree of isolation.
The probability of persistence of these populations was
taken proportional to the amount of the surrounding
woodland.
4.1.2. Habitat quality and isolation
It has been found that good habitat quality can also
improve the chances of population persistence through
favouring greater reproductive success, reducing mor-
tality, and/or improving the chance of successful settle-
ment by immigrants (Bellamy et al., 1996b). Research
has also shown that habitat quality and area are to a
certain degree compensatory in their effects on bird
occurrence (Whitcomb et al., 1981). Moreover, the
negative impact of a small patch can be offset by good
habitat quality and the total area of suitable woodland
in the region, providing that the patch size is above a
Fig. 2. Steps of the GIS analysis for the identiﬁcation of the sources.
minimum critical area (Lynch and Whigham, 1984).
Hence, remnants of ancient oak-birch woodland ac-
quiring a minimum patch size of 10 ha that would en-
sure a high probability of occurrence of redstarts were
also identiﬁed as potential sources. Likewise, mature
deciduous woods designated as County Wildlife Sites
(CWS), due to their structural and ﬂoristic character-
istics, of minimum 10 ha were also chosen.
Because of the smaller size of these patches, greater
importance was given to the spatial context as a com-
pensatory factor. Thus, only CWS and ancient wood-
land with an amount of surrounding habitat higher
than that estimated for the large woods were regarded
as sources. A larger amount of neighbouring wood-
land would further enhance recolonization, ensuring a
good prospect for these sites to sustain viable redstart
populations.


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
83
4.1.3. GIS approach to the identiﬁcation of the
sources
4.1.3.1. Area measures.
The GROUP model was
used for the layers of deciduous woodland, ancient
woodland and CWS in order to estimate the area of
individual habitat patches. GROUP ﬁnds polygons
in a layer by identifying contiguous groups of cells
holding the same value, and assigns a unique value
to each group. Area analysis gave the size of each
woodland patch by measuring the number of cells of
each of these groups. Polygons with an area smaller
than 50 ha (or 1250 cells) regarding the layer of de-
ciduous woodland, and polygons smaller than 10 ha
regarding the layers of ancient woodland and CWS,
respectively were eliminated (Fig. 2).
4.1.3.2. Spatial context measures.
In order to esti-
mate the amount of woodland within a 3 km radius,
the DISTANCE model was initially applied for each
of the selected potential sources. DISTANCE calcu-
lates the Euclidean distance of each cell to the nearest
of a set of target cells as speciﬁed in a separate layer.
A buffer zone of a 3 km radius was produced around
the selected patch in order to measure the area of the
surrounding woodland (Fig. 3a–c). In estimating the
spatial context, the Euclidean distance was applied
rather than a distance operator that integrates frictional
effects, because relevant studies used the metric dis-
tance in demonstrating the signiﬁcance of the wood-
land area within 3 km as a good predictor of isolation.
A range of values of woodland area in the 3 km
buffer was found for each of the three groups of
sources falling into three categories of low, medium
and high values. In order to ensure a high chance of
colonisation, only sites greater than 50 ha and sur-
rounded by a comparatively larger amount of wood-
land within the 3 km radius, larger than 4000 cells or
160.52 ha, were selected and the rest were rejected
through a Boolean classiﬁcation. The threshold value
is not an absolute ﬁgure, established in the literature,
so it was considered necessary to employ a relatively
high value of woodland area to further secure the
choice of woods as the appropriate ones. The area
value of 4000 cells (at 36% of the maximum value)
was adopted from a wide range of values with a min-
imum of 587 cells up to 11,079 cells. However, a
higher threshold value, of 5000 cells or 200 ha, was
Fig. 3. Stages of estimating the spatial context. (a) Calculation
of the distance of all pixels of the image; distance values are
estimated radially from the edges of the target wood, shown in
black. The rings join areas with the same distance; (b) production
of a buffer of a 3 km radius; (c) production of the buffer zone
containing the deciduous woodland.
chosen for the smaller patches of the County Wildlife
Sites and ancient woodland.
The layers depicting the three kinds of source woods
that satisﬁed the criteria of patch size, habitat quality
and spatial context, respectively, were overlaid to pro-
duce the ﬁnal map representing all deciduous woods
which could function potentially as permanent sources
of dispersing colonists to the surrounding woodland
patches (Fig. 4). The potential occupancy of these
patches is partly or entirely dependent on the distance
from the sources and on the presence of immigrating
individuals (Brown and Kodric-Brown, 1977).
4.2. Estimation of connectivity
Landscape ecological research has shown that land-
scape connectivity should not be expressed solely in


84
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
Fig. 4. Deciduous woods of large size and good habitat quality (ancient woods and County Wildlife Sites) were identiﬁed as “source”
populations of redstart.
terms of physical distance or spatial conﬁguration, but
should also incorporate the effect of the landscape ma-
trix on the dispersal of species (Forman and Godron,
1986; Hof and Flather, 1996). This derives from the
fact that landscapes are heterogeneous, thus encom-
passing various types of landscape elements that pose
different resistance to the dispersal ﬂow. Thus, the
concept of landscape resistance is introduced, which
represents the difﬁculty of crossing a landscape ele-
ment or land use type for the individuals of a species.
In this perspective, connectivity constitutes the degree
of ease with which a species moves through the land-
scape (Taylor, 1997).
Habitats that are less suitable for dispersal have
a higher resistance value. Birds hesitate to ﬂy over
non-habitat, and dispersal mortality can be higher in
open landscapes (Verboom et al., 1991). Opdam et al.
(1984) argued that a small stretch of open land could
restrict the immigration rates of woodland dependent
birds far below the actual distance that they could
cover according to their ﬂying abilities. Regarding lin-
ear landscape elements, Willis (1974) also suggested


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
85
that the width of a major river could be a barrier to
birds; some birds cannot ﬂy even across a small wa-
ter gap. With respect to roads, Bennett (1991) in his
review claimed that a broad highway could constitute
a functional barrier to sedentary woodland birds.
The classiﬁcation of the different types of landscape
elements according to their impedance to dispersal was
carried out on the basis of existing studies (Knaapen
et al., 1992) and knowledge of the ecological require-
ments and behaviour of the redstart. Thus, the suitabil-
ity of each land use and the degree of its resemblance
to the optimal habitat of redstarts provided the context
for assigning landscape resistance values (Table 1).
Hence, deciduous woodland, being the most suitable
and preferred habitat of the redstart and other wood-
land birds, was assigned the least resistance value 1,
while mixed and conifer woodland were attributed the
values 2 and 3, respectively. Arable land was assigned
Table 1
Classiﬁcation of the landscape elements according to expected
landscape resistance value
Landscape elements
Landscape
resistance value
Deciduous woodland
1
Mixed woodland
2
Conifer woodland
3
New plantations
3
Bracken/grass heath with mature trees
4
Rough grassland with mature trees
4
Permanent pasture/meadow with mature trees
4
Amenity grassland
5
Bracken/grass heath with scrub
5
Bracken/grass heath with heather
5
Bracken and/or grass heathland
5
Rough grassland with scrub
5
Rough grassland including marshland
5
Permanent pasture/meadow with scrub
5
Permanent pasture and meadow
5
New and/or improved grassland
5
Cultivated arable land
10
Allotments
10
Permanent horticultural crops
10
Urban
20
Mineral workings, active pits, tips and
spoil heaps
20
Relative barriers
Open water—lakes, ponds
25
Rivers
25
Roads
25
Rail
25
a high resistance value of 10, and urban together with
derelict areas, a high resistance value of 20. These
landscape elements comprise a signiﬁcantly more in-
hospitable habitat for the redstart, thereby impeding
its dispersal. Rivers, lakes, roads and railways were re-
garded as relative barriers to dispersal, i.e. movements
between populations on either side of the barrier are
infrequent but do occur, and thus they were given the
highest resistance value of 25 (Dawson, 1994).
4.2.1. GIS approach to estimating connectivity
The land use map was reclassiﬁed by assigning a
new value to each land use according to its suitabi-
lity as habitat for redstarts and other birds of mature
deciduous woodland. In this manner, the original 25
categories were reduced to 8, and the resulting map
represented the landscape as a mosaic of various
types of landscape resistance, with greatest resistance
in areas of inhospitable habitat which also reﬂected
the occurrence of barriers (Fig. 5).
The model COST (Cost Grow) produces a graphical
display of the ecological distance between the source
populations and the local populations. It requires a
map of the core areas “sources” and a friction surface
map (Fig. 6). The operational result of COST is to
generate a distance/proximity surface (also referred to
as a cost surface) where distance is measured as the
least cost distance or the least effort in moving over
a friction surface. COST uses a growth algorithm that
can accommodate complex friction surfaces as well as
absolute barriers to movement. The output of COST
attributed a value to each cell and in effect to each
wood representing the cost of dispersal of an individ-
ual to reach that wood. The unit of measurement is
“grid cell equivalents” (gce). A grid cell equivalent of
1 indicates the cost of moving through a grid cell when
the friction equals 1. A cost of ﬁve gce’s might arise
from a movement through ﬁve cells with a friction of
1, or one cell with a friction of 5.
Fig. 7 shows the output of a radial dispersal simu-
lation from each source patch throughout the friction
surface. The colour gradation from black to dark and
light grey represents a range of cost values from 0
(black) to 1166 (light grey), where the value 0 corre-
sponds to the sources. The cost of a dispersal route
increases with the distance travelled and in landscapes
with high resistance value. The light grey areas in the
south and north-east of the study area have cost values


86
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
Fig. 5. Friction surface image. The variation in the grey colour shades indicates the different groups of landscape elements with a
corresponding landscape resistance value (for the classiﬁcation of the landscape elements see Table 1).
Sources
(distance from the sources)
Sources
(distance from the sources)
Landscape element type
(friction surface)
Landscape element type
(friction surface)
COST
Distance from the sources+Landscape  resistance
COST
Distance from the sources+Landscape  resistance
Fig. 6. The cost of each patch is estimated as the sum of the distance from the set of the source patches and of the landscape resistance
of the cells in the intervening matrix.


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
87
Fig. 7. Cost surface image. Cost values are deﬁned radially from the sources and are demonstrated as concentric rings that enclose the
sources (black areas in the centre of the rings). The gradation of the shading from black to dark and light grey indicates the range of cost
values from low to high, and the potential of patch occupancy from high to low respectively. Non-source deciduous woods are illustrated
as small, distinct, black patches with well-deﬁned boundaries, scattered throughout the cost surface.
greater than 1000. The location in the south, which is
dominated by large expanses of treeless arable land-
scape and built-up areas represents a considerable re-
sistance to species dispersal. This is also shown in
the friction surface map where this area corresponds
to types of landscape elements with resistance values
10 and 20. The chances of a successful dispersal and
subsequently of patch occupancy are expected to be
particularly low in this part of the study area.
Fig. 7 also shows the groups of woodland patches
connected by areas of similar cost. The difference be-
tween ecological and real distance was veriﬁed by the
fact that some woods, although they were located at
the same distance from the sources, were found to


88
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
have different cost values and vice versa because of
the landscape effect (e.g. patches at 40 m distance had
cost values 2 and 45, respectively, whereas on the other
hand woods with cost value 84 were situated at 720
and 220 m distance from the set of sources).
4.3. Prioritisation of sites for habitat creation
The ranking of all sites by COST determined their
degree of connectivity, guiding their prioritisation
for woodland creation. Woods with low cost values,
being characterised by high connectivity, would be
highly accessible to the source populations and there-
fore would have a high chance of being colonised.
Yet, a cost threshold value was considered necessary
to be drawn among the lower cost values, in order
to identify the least isolated woods and prioritise the
sites of the study area accordingly. Connectivity of the
potential target woods would also be accomplished by
being within the dispersal distance of the redstart from
the sources. Therefore, two values were estimated for
each site: the cost of the dispersal of an individual to
reach that wood and its distance from the sources.
The comparison of the cost and distance values
indicated that the physical distance alone could not
account for the functional isolation of the habitat
patches. Therefore, suitable sites for habitat creation
should be identiﬁed primarily by their low cost values,
and their selection could then be reﬁned by taking into
account their metric distance from the sources. It was
suggested that woods with small cost values but also
with corresponding distance values less than 700 m
could be regarded as the least isolated. It was found
that all woods with low cost up to the value of (100)
were also located within an approximate distance of
700 m from the sources, whereas sites with cost values
just above (100) were situated at long distances far
beyond the dispersal distance. As a result of employ-
ing a threshold cost value rather than a distance value
as a primary determinant for isolation, some sites with
distance less than 700 m were not selected because of
their high cost. The use of the metric distance above
was only made to help deﬁne the threshold value as
opposed to being used as a predictor of isolation on its
own right.
After having determined the threshold cost value,
two zones of low and high cost for the dispersal of
redstarts could be clearly distinguished (Fig. 8). All
the sites in the low cost zone, because of their close
proximity to the sources and relative low landscape
resistance, would be easily accessible to dispersing
individuals and thus would mostly beneﬁt from ex-
pansion. Therefore, they were targeted as ﬁrst priority
sites for habitat creation. On the other hand, the sites
in the high cost zone are characterised by a greater
degree of isolation and would thus support local pop-
ulations with a lower probability of recolonization.
These woods were regarded as second priority sites.
However, their degree of isolation would still vary de-
pending on the cost values, allowing further reﬁning
of their priority status.
4.3.1. High priority sites
Patches of the low cost zone, larger than 5 ha and
managed for good habitat quality, may support local
populations of sufﬁcient size (of at least 3–5 breed-
ing pairs) that have low extinction rate. Thus, further
enlargement of these sites was not regarded as nec-
essary for the persistence of these populations. On
the other hand, patches less than 5 ha can accom-
modate only small local populations of redstarts and
other woodland birds that have a high extinction rate
due to stochastic events (Urban and Shugart, 1986;
Verboom et al., 1991). The survival of these pop-
ulations is highly dependent on dispersal from the
surrounding habitat and therefore the need to enhance
these vulnerable populations is much greater. There-
fore, among patches with low cost only those smaller
than 5 ha were selected for expansion at an initial
stage.
Because the colonisation probability and the oc-
currence of woodland birds and redstarts is positively
related to the spatial conﬁguration of habitat patches,
the amount of deciduous woodland within a 3 km
radius of the selected woods shaped the next rule in
the selection process. The application of this crite-
rion would further reinforce the assumption that the
identiﬁed woods which fulﬁlled all the above criteria,
being also located in a high-value neighbourhood,
would support local populations that have a greater
chance of recolonization. Immigration of individuals
to these target populations could take place not only
from the identiﬁed permanent sources but also from
neighbouring populations. Thus, once the species has
settled in these woods, enhanced species recruitment
through frequent recolonization into the sites, would


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
89
Fig. 8. Prioritization of sites for new planting. Sources are shown in black; the grey area around the sources indicates the low cost zone
and the white area the high cost zone. The darker grey patches within the low cost zone are the ﬁrst priority sites for habitat creation;
those in circles represent the high priority sites. The patches within the high cost zone are the second priority sites.
buffer possible local extinctions (“rescue effect”). The
greater the area of suitable woodland within the 3 km
buffer, the lower the probability of local redstart pop-
ulations becoming extinct. Those patches, which were
found to be surrounded by a large amount of deciduous
woodland (larger than 4000 cells) were ﬁnally selected
and were identiﬁed as high priority sites for habitat
creation. It is expected that by enlarging these sites to
the minimum size required maximum beneﬁts might
be gained for the persistence of the local populations.
5. Discussion
This paper presents the development of a metho-
dology for identifying and prioritising potential sites
for habitat creation, using GIS technology (Fig. 9).
It describes a system that can support local land-use
decision making by structuring the best available
knowledge about habitat processes and species re-
sponse in a fragmented landscape into the quantiﬁ-
cation of spatial parameters. The method identiﬁes


90
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
Select “focal” species 
and define its spatial 
requirements
Select “focal” species 
and define its spatial 
requirements
Define landscape resistance 
values for each landscape 
element on the basis of their 
suitability as habitat for the 
species
Estimate the dispersal “cost” of 
each grid cell/site
Estimate the distance of each grid cell/site
from the sources
Identify “source” populations 
based on: size, spatial context 
and habitat quality
Identify “source” populations 
based on: size, spatial context 
and habitat quality
First Priority sites
Sites with relative low cost (or high 
connectivity) and within the dispersal distance 
of the species from the sources
First Priority sites
Sites with relative low cost (or high 
connectivity) and within the dispersal distance 
of the species from the sources
Second Priority sites
Sites with relative high cost (or low 
connectivity) and outside the dispersal 
distance of the species from the sources
Second Priority sites
Sites with relative high cost (or low 
connectivity) and outside the dispersal 
distance of the species from the sources
Select sites smaller than the 
minimum required size
Select sites with large amount 
of surrounding suitable habitat
High Priority sites
High Priority sites
Fig. 9. Process overview.


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
91
the best potential habitats (“sources”) and also sites
for new habitat considering ecological guidelines of
minimum patch, maximum threshold distance, cer-
tain landscape conﬁguration and the suitability of
the landscape to species dispersal. It adopts a tar-
get species with well-known requirements since the
above issues can only be addressed with the available
knowledge as a single-species approach. Population
dynamics were introduced by the spatial requirements
of the redstart and were translated into speciﬁc con-
servation objectives that governed the selection of the
sites.
Estimating connectivity is an important part of
the site-selection process. In viewing landscape con-
nectivity in either empirical or theoretical studies,
the effect of the distance between populations on
dispersal as well as the amount of habitat around a
patch (or number of corridors) is usually taken into
account but rarely the effect of the landscape mo-
saic on the dispersal of individuals. The strength of
this approach in estimating connectivity lies in the
premise that the landscape is heterogeneous; namely,
it is not regarded as a binary mosaic where habitat
patches are embedded within an ecologically neu-
tral matrix but comprises a variety of habitats and
barriers of varying degrees of suitability to differ-
ent species. The concept of landscape resistance re-
ﬂects the heterogeneity of a landscape and is applied
as a friction parameter that decreases or enhances
connectivity.
New planting at the suggested sites as well as
enhancing
breeding
populations
of
redstarts
by
decreasing the rate of extinction, would also favour
other area-sensitive woodland interior birds that may
someday be at risk. Woodland generalist species,
not typically conﬁned to the edges of small woods,
would also beneﬁt. Moreover, enlargement of the
woodland sites that are located at a short distance
from the species pool should also increase the prob-
ability of initial colonisation in the establishment
phase of a range of woodland specialists which have
relatively short dispersal distances (Opdam et al.,
1985).
The method can also be applied to species other
than woodland birds. Sufﬁcient existing knowledge
of the autecological characteristics of an umbrella
species will be necessary. It should also be possible to
formulate its spatial requirements in terms of thresh-
old distances and minimum area. Generalisation of its
spatial requirements into guidelines for site-selection
depends on the spatial scale and on the species group
that can be represented by the species concerned. The
approach can be applied to each scale level depending
on the species; the grid size must be selected accord-
ing to its dispersal distance. The ﬂexibility of the
GIS system enables precisely such a change to take
place.
5.1. The role of GIS in site-selection
The process applied is systematic, ﬂexible and re-
producible. Moreover, the study has demonstrated the
utility and feasibility of using GIS for addressing the
issue of site-selection for habitat creation. The use of
GIS enhanced the capability to view woodland con-
servation within a broader landscape context, rather
than just on individual sites (Nikolakaki and Dunnett,
1998). The easy and quick implementation of overlay
and Boolean operations made it a very useful tool
in the process. Landscape and habitat requirements
were fed in as GIS layers and were overlaid accord-
ingly. GIS was also capable of calculating attributes
by means of spatial analysis, such as area of individ-
ual patches and their distance from other woodland
patches.
One of the major advantages of using GIS was the
application of the model COST for estimating land-
scape connectivity without relying explicitly on the
physical distance. Moreover, COST, by estimating
the potential cost of dispersal for each cell, produces
a wide range of values, and the outcome map rep-
resents the potential connectivity of any site in the
landscape. This gradation of COST values allows
the comparison among sites, and thus ranks the po-
tential suitability of all sites for woodland creation
within the study area prioritising them accordingly.
Moreover, the spatial context constitutes an additional
criterion for identifying the most potentially suitable
sites among those fulﬁlling the criteria. In this way,
the approach does not adopt a classiﬁcation based on
the classical Boolean logic, where an area is either ac-
cepted or rejected given a threshold value. Regarding
the second priority sites, they could constitute part
of an ecological network where creation of corridors
could reduce their isolation. The exploration of this
scenario formed part of a later work.


92
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
In relation to the threshold cost value, although
there was a clear distinction in this study, with cost
values below 100 also corresponding to very low dis-
tance values (<700 m), this might not have been the
case for a different cost outcome. In such a case, the
amount of available funding for implementing such
a project could determine the threshold value, above
which sites could be disregarded. Habitat creation
could start at the sites with the lowest cost values con-
tinuing at patches with relatively higher cost values
in ascending order, until the full expenditure of the
funding.
A point that should also be made is that extending
habitat patches alters the mosaic around the wood-
lands resulting in changing values of the variables
(such as area of woodland within 3 km). These alter-
ations should be included in the modelling and the
computation should ideally be an iterative process.
With regard to landscape resistance, because it is a
theoretical variable, which thus far has not been stud-
ied or measured as such, its estimation was based
on sensible assumptions and literature ﬁndings for
woodland birds. Given that the difﬁculty to cross a
landscape element depends on the species concerned,
it is possible to modify the landscape resistance val-
ues. A more precise deﬁnition of the resistances re-
quires collecting ﬁeld data on the dispersal rate of the
studied species between habitat patches. However, it
would be beneﬁcial if the results could be generalised
and applied to “ecological groups” of organisms with
a common ecological proﬁle.
Though the approach is based on assumptions, it
allows the selection of the core areas that can repre-
sent the backbone of a strategic ecological network
as well as the identiﬁcation of those patches that are
more likely to receive colonists from the sources. The
identiﬁcation of these areas could direct mitigation
conservation funds. The method can be used as an
initial step in the process of site-selection on a large
scale that can then guide more detailed ﬁeld-based
assessments. Adding other factors as a series of over-
lays such as soils, soil moisture or aspect constraints
could further reﬁne the prioritisation procedure. More-
over, overlay with data layers of zoning and pending
projects could be used to assess future threats for the
identiﬁed habitats. In general, the model provides a
simple approach that can be a useful tool in nature
conservation and landscape planning, integrating pop-
ulation dynamics and spatial relations in GIS facilities
for site-selection endeavours.
Acknowledgements
The study was conducted as part of my doctoral
thesis, which was ﬁnancially supported by the Hel-
lenic Foundation of Scholarships and the Department
of Landscape of the University of Shefﬁeld. I would
like to thank Nigel Dunnett for his supervision, Not-
tinghamshire County Council for the provision of the
digital land use data, Duncan Westbury for his helpful
comments, Andrew Moran and John Nisbet for their
improvements on the english.
References
Andrén, H., 1994. Effects of habitat fragmentation on birds and
mammals in landscapes with different proportions of suitable
habitat: a review. Oikos 71, 355–366.
Bellamy, P.E., Hinsley, S.A., Newton, I., 1996a. Factors inﬂuencing
bird species numbers in small woods in south-east England. J.
Appl. Ecol. 33, 249–262.
Bellamy, P.E., Hinsley, S.A., Newton, I., 1996b. Local extinctions
and recolonizations of passerine bird populations in small
woods. Oecologia 108, 64–71.
Bellamy, P.E., Brown, N.J., Enoksson, B., Firbank, L., et al.,
1997. The role of landscape structure and dispersal in
limiting nuthatch distribution. In: Cooper, A., Power, J. (Eds.),
Proceedings of the Sixth Annual Conference of the International
Association for Landscape Ecology (UK) on Species Dispersal
and Land Use Processes. University of Ulster, IALE, UK.
Bennett, A.F., 1991. What types of organism will use the corridor?
In: Saunders, D.A., Hobbs, R.J. (Eds.), Nature Conservation. 2.
The Role of Corridors. Surrey Beaty & Sons, Chipping Norton,
NSW, pp. 407–408.
Brown, J.H., Kodric-Brown, A., 1977. Turnover rates in insular
biogeography: effect of immigration on extinction. Ecology 58,
445–449.
Carter, S. (Ed.), 1995. Britain’s Birds in 1991–1992: The Conser-
vation and Monitoring Review. British Trust for Ornithology,
Thetford Joint Nature Conservation Committee, Peterborough.
Collinge, S.K., 1996. Ecological consequences of habitat frag-
mentation: implications for landscape architecture and planning.
Landscape Urban Plann. 36, 59–77.
Cramp, S. (Ed.), 1988. Handbook of the Birds of Europe, the
Middle East and North Africa. The Birds of the Western
Palearctic, Tyrant Flycatchers to Thrushes, vol. V. Oxford
University Press, Oxford.
Dawson, D.G., 1994. Narrow is the way. In: Dover, J.W. (Ed.),
Proceedings of the Third Annual Conference of the International
Association for Landscape Ecology (UK) on Fragmentation in


P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
93
Agricultural Landscapes. Myerscough College, Preston, IALE,
UK.
Fahrig, L., Merriam, G., 1985. Habitat patch connectivity and
population survival. Ecology 66 (6), 1762–1768.
Forestry Authority, 1994. Creating New Native Woodlands.
Bulletin 112. Forestry Commission, Edinburgh.
Forman, R.T.T., Godron, M., 1986. Landscape Ecology. Wiley,
New York.
Franklin, I.R., 1980. Evolutionary change in small populations.
In: Soulé, M.E., Wilcox, B.A. (Eds.), Conservation Biology:
An Evolutionary Ecological Perspective. Sinauer Associates,
Sunderland, MA, pp. 135–149.
Fuller, R.J., Warren, M.S., 1991. Conservation management in
ancient and modern woodlands: responses of fauna to edges
and rotations. In: British Ecological Society Symposium No. 31
(Ed.), The Scientiﬁc Management of Temperate Communities
for Conservation. Blackwell Scientiﬁc Publications, Oxford,
pp. 445–471.
Fuller, R.J., Gough, S.J., Marchant, J.H., 1995. Bird populations
in new lowland woods: landscape, design and management
perspectives. In: Ferris-Kaan, R. (Ed.), The Ecology of
Woodland Creation. Wiley, Chichester, pp. 163–182.
Hanski,
I.,
1994.
Patch-occupancy
dynamics
in
fragmented
landscapes. Tree 9 (4), 131–135.
Harms, W.B., Knaapen, J.P., 1988. Landscape planning and
ecological infrastructure: the Randstad study. In: Schreiber, K.F.
(Ed.), Connectivity in Landscape Ecology, Proceedings of the
Second International Seminar of the International Association
for Landscape Ecology. Munstersche Geographische Arbeiten,
Munster, 1987.
Harms, W.B., Opdam P., 1990. Woods as habitat patches for
birds: application in landscape planning in The Netherlands. In:
Zonneveld, I.S., Forman, R.T.T. (Eds.), Changing Landscapes:
An
Ecological
Perspective.
Springer-Verlag,
New
York,
pp. 73–97.
Hinsley, S.A., Bellamy, P.E., Newton, I., Sparks, T.H., 1994a.
Factors Inﬂuencing the Presence of Individual Breeding Bird
Species in Woodland Fragments. Research Report 99, English
Nature, Peterborough.
Hinsley,
S.A.,
Bellamy,
P.E.,
Newton,
I.,
1994b.
Habitat
Fragmentation and the Occurrence of Breeding Birds in Small
Woods. Annual Report 1993–1994. Institute of Terrestrial
Ecology, Monks Wood.
Hof, J., Flather, C.H., 1996. Accounting for connectivity and spatial
correlation in the optimal placement of wildlife habitat. Ecol.
Model. 88, 143–155.
Knaapen, J.P., Scheffer, M., Harms, W.B., 1992. Estimating habitat
isolation in landscape planning. Landscape Urban Plann. 23,
1–16.
Komdeur, J., Gabrielsen, L., 1995. Effects of forest fragmentation
on breeding bird populations in Denmark. In: Skov, F.,
Komdeur, J., Fry, G., Knudsen, J. (Eds.), Proceedings of the
second Connect Workshop on Landscape Ecology, Principles
and Tools for The Study of Landscape Ecology-Potentials and
Limitations, 1993. Technical Report No. 131, Fuglocentret,
Danish National Environmental Research Institute.
Lambeck, R.J., 1997. Focal species: a multi-species umbrella for
nature conservation. Conserv. Biol. 11 (4), 849–856.
Lynch, J.F., Whigham, D.F., 1984. Effects of forest fragmentation
on breeding bird communities in Maryland USA. Biol. Conserv.
28, 287–324.
McIntyre, N.E., 1995. Effects of forest patch size. Landscape Ecol.
10 (2), 85–99.
Moore, N.W., Hooper, M.D., 1975. On the number of bird species
in British woods. Biol. Conserv. 8, 239–250.
Nikolakaki, P., Dunnett, N., 1998. Strategy for woodland creation
in Sherwood Forest: the use of GIS to produce a landscape
plan. In: Katsifarakis, K., Korﬁatis, G., Mylopoulos, Y.,
Demetracopoulos, A.C. (Eds.), Proceedings of the Fourth
International Conference on Protection and Restoration of the
Environment, Protection and Restoration of the Environment.
Aristotle University of Thessaloniki, Macedonia.
Opdam, P., 1991. Metapopulation theory and habitat fragmentation:
a review of holarctic breeding bird studies. Landscape Ecol.
5 (2), 93–106.
Opdam, P., van-Dorp, D., ter-Braak, C.J.F., 1984. The effect of
isolation on the number of woodland birds in small woods in
The Netherlands. J. Biogeograph. 11, 473–478.
Opdam, P., Rijsdijk, G., Hustings, F., 1985. Bird communities in
small woods in an agricultural landscape: effects of area and
isolation. Biol. Conserv. 34, 333–352.
Simberloff, D., 1998. Flagships, umbrellas, and keystones: is
single-species management passé in the landscape era? Biol.
Conserv. 83 (3), 247–257.
Sparks, T.H., Hinsley, S.A., Mountford, J.O., Veitch, N., Bellamy,
P.E., deNooijer, D.S., 1994. Landscape design: preliminary esti-
mates of the effects of landscape permutations on wildlife. In:
Dover, J.W. (Ed.), Proceedings of the Third Annual Conference
of
the
International
Association
for
Landscape
Ecology
on Fragmentation in Agricultural Landscapes. Myerscough
College, Preston, IALE, UK.
Taylor, P.D., 1997. Empirical explorations of landscape connec-
tivity. In: Cooper, A., Power, J. (Eds.), Proceedings of the
Sixth Annual Conference of the International Association
for Landscape Ecology on Species Dispersal and Land Use
Processes. University of Ulster, IALE, UK.
Urban, D.L., Shugart, J.H.H., 1986. Avian demography in mosaic
landscapes: modeling paradigm and preliminary results. In:
Verner, J., Morrison, M.L., Ralph, C.J. (Eds.), Wildlife 2000.
Modelling Habitat Relationships of Terrestrial Vertebrates.
University of Wisconsin Press, London, pp. 273–280.
Verboom, J., Schotman, A., Opdam, P., Metz, J.A.J., 1991.
European nuthatch metapopulations in a fragmented agricultural
landscape. Oikos 61, 149–156.
Verboom, J., Metz, J.A.J., Meelis, E., 1993. Metapopulation models
for impact assessment of fragmentation. In: Vos, C.C., Opdam,
P. (Eds.), Landscape Ecology of a Stressed Environment.
Chapman & Hall, London, pp. 172–191.
Whitcomb, R.F., Robbins, C.S., Lynch, T.F., Whitcomb, B.L.,
Klimkiewicz, M.I.C., Bystrak, D., 1981. Effects of forest
fragmentation on avifauna of the eastern deciduous forest. In:
Burgess, R.L., Sharpe, D.M. (Eds.), Forest Island Dynamics in
Man-Dominated Landscapes. Springer, New York, pp. 125–205.
Wiens,
J.A.,
Schooley,
R.L.,
Weeks,
R.D.J.,
1997.
Patchy
landscapes and animals movements: do beetles percolate? Oikos
78, 257–264.


94
P. Nikolakaki / Landscape and Urban Planning 68 (2004) 77–94
Willis, E.O., 1974. Populations and local extinctions of birds on
Barro Colorado Island. Panama Ecol. Monogr. 44, 153–169.
Willson, M.F., de Santo, T.L., Sabag, C., Armesto, J.J., 1994.
Avian communities of fragmented south-temperature rainforests
in Chile. Conserv. Biol. 8 (2), 508–520.
Winspear R.J., 1991. A Study of the Distribution of Bird Species
in Fragmented Woodland. Ph.D. Thesis, University of Leeds,
Leeds.
Pantoula Nikolakaki serves at present as the landscape and bio-
diversity ofﬁcer at Oxfordshire County Council. Her work focuses
on developing a methodology to assess biodiversity on a large
scale and on exploring the relationship between landscape charac-
ter and biodiversity using GIS, in order to assist decision making
in landscape planning. She received her PhD in landscape ecol-
ogy from the University of Shefﬁeld, in 2000. In addition, she
received her master of landscape architecture from the University
of Edinburgh, in 1995 and her diploma in agriculture from the
Aristotle University of Thessaloniki, in 1988. Her areas of interest
include conservation landscape ecology with emphasis on habitat
fragmentation issues and metapopulation dynamics, and develop-
ment of spatial decision support systems for landscape conserva-
tion planning utilising the capabilities of GIS.
