--- 
source: Untitled-526.pdf
--- 

Habitat evaluation using GIS
A case study applied to the San Joaquin Kit Fox
Ross Gerrarda,*, Peter Stineb, Richard Churchc, Michael Gilpind
aNational Center for Ecological Analysis and Synthesis, University of California at Santa Barbara,
735 State Street, Suite 300, Santa Barbara, CA 93101-5504, USA
bUSGS Biological Resources Division, Western Ecological Research Center, California State University,
Sacramento, CA 95819-6129, USA
cDepartment of Geography/National Center for Geographic Information and Analysis,
University of California, Santa Barbara, CA 93106-4060, USA
dDepartment of Biology 0116, University of California at San Diego, La Jolla, CA 92093-0116, USA
Received 28 June 1999; received in revised form 1 June 2000; accepted 15 September 2000
Abstract
Concern over the fate of plant and animal species throughout the world has accelerated over recent decades. Habitat loss is
considered the main culprit in reducing many species' abundance and range, leading to numerous efforts to plan and manage
habitat preservation. Our work uses Geographic Information Systems (GIS) data and modeling to de®ne a spatially explicit
analysis of habitat value, using the San Joaquin Kit Fox (Vulpes macrotis mutica) of California (USA) as an example. Over the
last 30 years, many ®eld studies and surveys have enhanced our knowledge of the life history, behavior, and needs of the kit
fox, which has been proposed as an umbrella or indicator species for grassland habitat in the San Joaquin Valley of California.
There has yet been no attempt to convert much of this ®eld knowledge into a model of spatial habitat value useful for planning
purposes. This is a signi®cant omission given the importance and visibility of the imperiled kit fox and increasing trends
toward spatially explicit modeling and planning. In this paper we apply data from northern California to derive a small-cell
GIS raster of habitat value for the kit fox that incorporates both intrinsic habitat quality and neighborhood context, as well the
effects of barriers such as roads. Such a product is a useful basis for assessing the presence and amounts of good (and poor)
quality habitat and for eventually constructing GIS representations of viable animal territories that could be included in future
reserves. # 2001 Elsevier Science B.V. All rights reserved.
Keywords: Kit fox; GIS; Habitat conservation plan
1. Introduction
The San Joaquin Kit Fox (Vulpes macrotis mutica)
has been a federally listed endangered species in the
United States since 1967. It once ranged widely over
the San Joaquin Valley of California (Fig. 1). Immense
agricultural and urban development have greatly
reduced and fractured its habitat during the 20th
century. Over the past 30 years, a body of information
Landscape and Urban Planning 52 (2001) 239±255
* Corresponding author. Present address: ISERA Group, 5370
Hollister Avenue No. 2, Santa Barbara, CA 93111, USA.
Tel.: 1-805-967-3820; fax: 1-805-681-7328.
E-mail addresses: gerrard@isera.com (R. Gerrard),
pstine@fs.fed.us (P. Stine), church@geog.ucsb.edu (R. Church),
mgilpin@ucsd.edu (M. Gilpin).
0169-2046/01/$20.00 # 2001 Elsevier Science B.V. All rights reserved.
PII: S 0 1 6 9 - 2 0 4 6 ( 0 0 ) 0 0 1 1 9 - 5


on kit fox habitat requirements has been generated
through along-road spotlight surveys and numerous
®eld studies. In this paper we propose a method for
translating some of the knowledge garnered from ®eld
studies into a small-cell raster of kit fox habitat value
that can be created and stored in a Geographic Infor-
mation System (GIS). Since the kit fox has not made
substantial progress toward recovery and removal
from US. Endangered species list, there is a continuing
need to evaluate potential habitat as part of regional
planning in the areas where it still occurs. Enhancing
this need is the trend toward Habitat Conservation
Fig. 1. Locator map.
240
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


Plans as a tool for mediating land use con¯icts invol-
ving disturbance of endangered species' habitats.
Meanwhile, growth pressures continue throughout
the fox's extant range. These factors taken together
suggest an increasing requirement to augment ®eld
study with a GIS-based method for evaluating kit fox
habitat quality.
2. Background
The San Joaquin Kit Fox (Vulpes macrotis mutica)
is a small canid that historically occupied most of the
San Joaquin Valley of California. It has an average
length of 20 in. and a tail length of 12 in., stands
between 9 and 12 in. at the shoulder, weighs an
average of about 5 pounds, and has conspicuously
large ears (O'Farrell, 1983). Its primary habitat is
relatively open grassland or scrubland, where it inha-
bits dens and feeds on prey such as ®eld mice,
kangaroo rats, ground squirrels, and insects. The kit
fox is active primarily at night (Morrell, 1971; Bell,
1998).
Its numbers are not well known even after 25 years
of along-road nighttime spotlight surveys and numer-
ous ®eld studies. Population estimates have ranged
from 1000 to 3000 (Laughrin, 1970) to 14,000 (Mor-
rell, 1975). Adjustments to Morrell (1975) ®gures
gave an estimate of about 7000 animals (O'Farrell,
1983). Limited resources for surveying will always
make accurate estimates of abundance and distribution
of a widely distributed nocturnal species such as the
kit fox very dif®cult. Another dif®culty in measuring
abundance is the cyclical nature of kit fox populations.
Drought, common in California, can bring about a
substantial decline in plant seed production with a
corresponding crash in the populations of the noctur-
nal rodents that the kit fox preys upon (Dennis and
Otten, 2000). In the Carrizo Plain of central Califor-
nia, scarcity of small-mammal prey during the drought
of 1989±1991 led to decreased kit fox reproductive
success (White and Ralls, 1993; White et al., 1996).
After 1991, increasing rainfall led to an increased kit
fox population (Ralls and White, 1995).
Despite the disparities in population counts, the kit
fox has long been recognized as being endangered and
was given relatively early protection under various
laws. It received status as a ``protected furbearer'' in
California in 1965, a US federal government listing as
``endangered'' in 1967, and a state listing as ``rare''
(later ``threatened'') in 1971 (Morrell, 1975).
The decline of the kit fox is a result of several
factors. Paramount is loss of habitat. In the 1960s and
1970s, this was primarily conversion from native
scrub to agricultural in Kern County and elsewhere
in the San Joaquin Valley (Knapp, 1978). More
recently, growing human population and accompany-
ing urbanization has become an equal if not greater
threat, especially in parts of the northern range such as
Contra Costa and Alameda Counties near the San
Francisco Bay Area metropolis and around the city
of Bakers®eld in Kern County (Begley, 1997). Direct
mortality as a result of rodent poisoning (Bell, 1994)
and agricultural land conversion operations (Knapp,
1978) has also been signi®cant. Other factors include
road kills and illegal shooting.
Ultimately, habitat preservation is essential to the
recovery of the species. Nighttime spotlight surveys
have been conducted by the California Department of
Fish and Game (CDFG) since 1970 (quarterly, along
seven or eight 48 km rural routes). While the spotlight
survey data are somewhat sparse, the results indicate
that in those areas where habitat has been preserved,
the fox populations are fairly stable over time. There
are cyclical ¯uctuations (likely owing to droughts) but
no long-term decline (Ralls and Eberhardt, 1997; Ralls
and White, 1995). This indicates the central impor-
tance of habitat preservation to the species' recovery,
assuming of course an absence of deleterious activities
such as rodent poisoning, illegal shooting, or exces-
sive traf®c. The unlikelihood of ever accurately sur-
veying the complete distribution and abundance of the
kit fox indicates that assessing potential habitat will
have to be key in conservation and recovery planning.
Motivations put forward for conserving species and
habitats have included moral and economic reasons,
among others. In the US, there are strong legal reasons
which are encompassed within the national Endan-
gered Species Act. Under this law, ``listed'' species
(those designated either as ``threatened'' or given the
more critical designation ``endangered'') have con-
siderable protection from being killed or harassed, or
having their habitat destroyed. The process of decid-
ing which species are listed and which are not is very
controversial and time consuming, and certainly not
all imperiled species have actually been listed. The
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
241


San Joaquin Kit Fox, however, has been on the list
longer than almost any other, entering the ``endan-
gered'' category in 1967, even before the major revi-
sion of the Endangered Species Act in 1973, which is
the basis of the current law. In the 1990s, the law's
implementation took a strong turn away from absolute
prohibition of harassing/killing listed species to a
policy of allowing ``incidental'' damage to species
and their habitats (such as from developing houses or
shopping malls) as long as that damage is balanced by
off-site mitigation. Thus for example, a developer
could proceed in known habitat while paying to pre-
serve other habitat elsewhere. This type of approach is
known under the law as a Habitat Conservation Plan
(HCP) and is now seen as the preferred tool used
by the US Government for addressing endangered
species issues. Under US Interior Secretary Bruce
Babbitt, the number of HCPs has swelled from about
10 in 1993 to about 500 either completed or in
progress by 2000.
What is the importance of the San Joaquin Kit Fox
in enforcement of the Endangered Species Act and
HCP development, and why is habitat evaluation for
the kit fox needed now? The kit fox takes a place of
prominence because it is regarded as an ``umbrella''
species, meaning that it has wider spatial requirements
than other species. Thus, if an area of habitat is set
aside that is suf®cient for the fox, other species with
lesser spatial requirements will be protected also. The
``umbrella'' designation has been conferred as of®cial
policy by the US Fish and Wildlife Service (USFWS)
in the San Joaquin Valley Upland Species Recovery
Plan (USFWS, 1998). Another factor driving the
importance of the kit fox is current and anticipated
economic and population growth in the San Joaquin
Valley (Fig. 1). Even conservative estimates forecast
several million additional residents in the next 25
years. These growth pressures are potentially threa-
tening to kit fox habitat and also are forcing extensive
work on HCPs in order to meet legal requirements for
conservation. Without approved HCPs, there could be
disruptions to local economies as development pro-
jects will be curtailed sharply or stopped altogether, in
the manner that commercial logging in both the south-
western and northwestern US was virtually halted in
the 1990s due to concerns about the spotted owl. These
studies, as their name implies, will focus on conser-
ving adequate habitat, not on counting and protecting
a certain number of animals, which is logistically
dif®cult or impossible to do in most cases. The
combination of the recent Recovery Plan and its
conferral of policy-level umbrella status on the kit
fox, along with the explosion of HCP work in central
California, indicates a signi®cant need to provide
general habitat evaluation tools for the species.
3. Methods
The San Joaquin Kit Fox is associated with two
major habitat types. One is scrubland such as the
Alkali sink plant communities in Kern County at
the southern part of the fox's range (Knapp, 1978).
The other is annual grassland, which is more prevalent
at the northern end of the fox's range (Bell, 1998). Our
method in this paper uses data from the northern range
(eastern Contra Costa and Alameda Counties), where
grassland is the main available habitat type. While the
northern range is not a population stronghold as are
western Kern County and the Carrizo Plain, documen-
ted kit fox occurrences there have persisted into the
1990s (Natural Diversity DataBase Program, CDFG).
The primary environmental datalayer available to
us was a detailed vegetation/land cover map of a
228,000 acre region in eastern Contra Costa and
Alameda Counties (Jones and Stokes Associates
Inc., 1996). Other mappable biological and physical
data, if available, could be used to characterize sui-
table habitat for the San Joaquin Kit Fox. Our vegeta-
tion datalayer distinguished 23 different landcover
types, which are shown in Table 1. These habitat
and land cover types may be generalized as:
Annual grassland:
68%
Oak woodland:
18%
Cropland/orchard:
7%
Urban and developed:
3%
Surface water:
2%
Shrubland:
1%
Wetland or riparian:
1%
Given this high-resolution vegetation data, our goal
was to estimate the value of any landscape unit (such
as a 4 ha grid cell) as potential habitat for the kit fox.
To understand the needs of the fox and how those
habitat needs vary over space, we consulted with
several experts. Our other major source of biological
242
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


input was ®eld studies and summaries such as Morrell
(1971), White and Ralls (1993), Bell (1994), Bell
(1998), and others. The overall goal of the effort
was a habitat value map for the region consisting of
23,418 cells, each 4 ha in size, where each cell is
assigned a habitat score. After consulting with experi-
enced biologists, we made the following assumptions
regarding habitat requirements for the San Joaquin Kit
Fox:
1. The value of a grid cell for kit fox habitat has both
an intrinsic component and a situational or
``neighborhood'' component.
2. The following vegetation types can be assigned
relative intrinsic values for kit fox habitat as
follows:
 grassland (value  4),
 oak
or
riparian
woodland,
or
shrubland
(value  0),
 cropland/orchards, or wetlands (value  ÿ2),
 open water (value  ÿ4),
 urban/developed (value  ÿ20).
3. Daily movement of animals can extend up to 2
miles in any direction (this determines the spatial
extent of the ``neighborhood'' in¯uence alluded to
in (1) above).
4. All freeways, permanent water bodies, and urban/
developed areas are impenetrable barriers.
The experts with whom we consulted are pre-emi-
nent kit fox biologists, including Bell and Spiegel (see
Acknowledgements), who are the authors of several
detailed studies (Bell, 1994, 1998; Bell et al., 1994;
Orloff et al., 1986; Spiegel, 1996). Admittedly, none
of the four authors of this paper can be regarded as a
kit fox expert. We are more specialists in GIS, reserve
design,
and
decision
support
applications.
Our
approach in this paper is to integrate the extensive
®eld work done by the biologists with computer
mapping techniques for evaluating habitat. One of
the striking things about the literature on the kit fox
is that virtually all of it is reporting on ®eld work
(surveys, radio telemetry studies, etc.). Thus far, there
has been no attempt to use this knowledge to make
generic measures of habitat value; yet this step is
crucial if biologically and legally defensible HCPs
are to be developed. It is very likely that a regional
HCP for eastern Alameda and Contra Costa counties
will get under way in the next 5 years, and there are
now or will be many HCPs within the kit fox's extant
range.
As important as experts can be for this type of study,
we did not feel that their opinions alone were suf®-
cient. Accordingly, we marshaled a considerable
amount of literature, both published and unpublished,
and found that it supported the assumptions made
above and provided an additional level of veri®cation,
especially in regard to home range sizes and preferred
land cover type. Multiple studies by Ralls and others
on the Carrizo Plain (Fig. 1) are particularly relevant,
since that area is grassland habitat very similar to our
study area (White and Ralls, 1993; Ralls and White,
1995; White et al., 1996).
While assumptions (1)±(4) above match the condi-
tions found in eastern-Alameda±Contra Costa, differ-
ent assumptions might be more appropriate in other
areas. For example, Morrell (1971) mapped home
ranges showing daily movements that extended out-
ward little more than 1 mile in the area of the Buena
Vista lakebed in Kern County. While we assume 2
miles for this study, our method could easily accom-
modate other parameters. A major determinant of
Table 1
Landcover types in the study area
Grassland without features
5.24%
Grassland Ð dryland farmed
44.37%
Grassland with wind turbines
17.15%
Grassland with vernal pool aggregations
1.52%
Shrubland
0.31%
Shrubland Ð scrub
0.21%
Shrubland Ð chaparral
0.56%
Oak woodland
18.13%
Mixed conifer woodland
0.07%
Riparian habitat
0.01%
Riparian forest and woodland
0.45%
Emergent wetland
0.04%
Permanent marsh
0.02%
Seasonal wetland
0.35%
Aquatic habitat (open water)
2.16%
Agricultural Ð cropland
5.70%
Agricultural Ð orchard
1.20%
Developed
0.44%
Residential
0.81%
Industrial/commercial
0.76%
Disturbed ground
0.26%
Landfill
0.15%
Landscaped parks/golf courses
0.07%
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
243


daily animal movement will be prey biomass density.
If it is relatively high, home range size and daily
movement will likely be less as there is less need
for an animal to travel far to meet food requirements.
Differing habitat type and quality lead to signi®cantly
different range sizes and movement behavior, accord-
ing to published evidence (Morrell, 1971; Koopman
et al., 1998; White and Ralls, 1993; Zoellick and
Smith, 1992; Zoellick et al., 1989). For example,
Morrell (1971) reported home range sizes of 2.6±
5.2 km2 in western Kern County. Koopman et al.
(1998) reported about 4.5 km2 in the same region,
on the Naval Petroleum Reserves. On the Carrizo
Plain in San Luis Obispo County, much larger home
range sizes, 11±12 km2, were reported by White and
Ralls (1993). Such larger range sizes also characterize
the desert kit fox in Arizona (Zoellick and Smith,
1992). Zoellick et al. (1989) postulated that relatively
lengthy nocturnal movement by desert kit foxes is
partly due to low prey abundance in their creosote
bush habitat. All of these results suggest that habitat
use and daily or seasonal movement will vary depend-
ing on the physical environment. To meet planning
needs under different circumstances, our assumptions
can easily be altered within the general framework
described here for deriving habitat value.
Our ®rst step was to convert our high-resolution
vegetation data of eastern-Alameda±Contra Costa,
which was in the form of an Arc/Info polygon cover-
age (ESRI, 1996), to grid cell format. We decided on
4 ha cells (200 m on each side, about 10 acres). This is
a size that was the minimum mapping unit in the
regional data for wetland/riparian (40 ha was used for
the major habitats such as grassland and oak wood-
land). Cells smaller than 4 ha were ruled out as con-
tributing little bene®t to the analysis relative to the
signi®cant increase in cell numbers. Of course, the
identical methods that we describe with respect to 4 ha
cells could also be applied to smaller or larger cells if
desired. The conversion from vector (polygon) cover-
age to a grid was accomplished via the Arc/Info
command Polygrid. Essentially, this function drapes
a ``mesh'' of 4 ha cells over the vegetation map and
assigns each cell a category based on the underlying
vegetation type. What happens if more than one
vegetation type occupies a cell? This occurrence
demands that a choice be made as to which vegetation
category will be assigned to the cell. By default,
Polygrid will assign that category occupying the great-
est area of the cell, the ``majority-rules'' criterion.
Alternatively, Polygrid accepts a user-de®ned weight-
ing scheme that overrides ``majority-rules.'' We
applied a set of weights that favored riparian, wet-
lands, shrubland, and grassland with vernal pools.
This has the effect of preserving riparian and wetland
environments, which would otherwise be lost in the
conversion because they tend to be small and narrow.
After converting our GIS data to raster format, we
had a grid representing the distribution of the 23
different vegetative/land cover classi®cations. We
applied the biological assumptions to reclassify the
raster to a grid of intrinsic habitat value. The reclas-
si®cation was as follows: cells that were any type of
grassland, the prime San Joaquin Kit Fox habitat, were
valued at 4, oak woodland (and the small amounts of
other woodland and shrubland) at 0, agricultural lands
and wetlands at ÿ2, surface water at ÿ4, and devel-
oped categories at ÿ20. In this manner the original 23
categories were reduced to 5 (Fig. 2). These relative
values are termed intrinsic habitat values because they
measure only the characteristics of a particular grid
cell and not the cell's surroundings. (The assigned
ranking of 4 to all grassland, including grassland under
a dryland farming regime, was speci®cally pursued
with the consulting biologists. They concluded that
even though this category is under cultivation as
pasture and grain crops and is subject to a low to
moderate level of plowing, it still warrants a top
ranking for kit fox suitability.)
An intrinsic evaluation of a cell is by itself not an
accurate rating of the quality of that cell. While
grassland is the preferred habitat of the kit fox, there
is a difference between a grassland cell surrounded by
dense woodland or near urbanization and a grassland
cell surrounded by other grassland cells. Thus, at the
request of the kit fox biologists, we needed to address
the spatial context in which each cell is found. The
assumption that animal movement may range up to 2
miles in any direction provided a bound on the relevant
``neighborhood'' of any cell. If within a 2-mile radius
of a cell there are other ``good'' cells (i.e., grassland),
we have a high-value neighborhood. If the locality is
composed of marginal or poor cells, the spatial context
is downgraded. Ultimately, the quality of any cell will
be the additive combination of its intrinsic qualities
and its situational qualities. That is, we will take the
244
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


sum of the intrinsic habitat quality layer and the
``spatial context'' layer to create a total value grid layer.
To derive a ``spatial context'' or ``neighborhood
effect'' grid that grades each 4 ha cell based on its
neighborhood, we applied Arc/Grid's Focalsum func-
tion. We used Focalsum to add the total intrinsic value
of cells in the de®ned locality (2-mile radius) around
each individual cell. The product is a new grid, again
composed of 23,418 individual 4 ha cells that span the
region, each cell given a value equal to the total
intrinsic value lying within its neighborhood.
There are different options to the Focalsum
command that allow different ways of adding up
neighborhood values. We decided to apply a dis-
tance-sensitive property such that the farther out a
cell is from the processing cell (neighborhood center),
the less it counts toward the neighborhood sum.
Our relative weighting was such that a cell at a
distance of 2 miles is worth about 10% as much to
the neighborhood score for the central cell as the
central cell itself (Fig. 3). Any of a number of other
distance decay properties could have been used,
including having none at all and allowing the most
distant cells to count the same as the central part of
the neighborhood.
The output of the Focalsum operation with the
distance weighting as shown in Fig. 3 was a grid layer
of raw weighted sums that ranged from ÿ78,218 to
104,116. It was necessary to partition this range of
values into a small number of categories. In accord
with biological opinion, we created eight categories by
dividing the range ÿ78,218 to 104,116 into eight even
parts. Associated with each of the eight categories is a
value that re¯ects how the intrinsic cell value will be
Fig. 2. Intrinsic habitat values for the San Joaquin Kit Fox.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
245


modi®ed based on neighborhood value:
ÿ78,218 to ÿ55,427:
subtract 8
ÿ55,426 to ÿ32,635:
subtract 6
ÿ32,634 to ÿ9843:
subtract 4
ÿ9842 to 12,949:
subtract 2
12,950 to 35,741:
subtract 1
35,742 to 58,533:
remain same
58,534 to 81,325:
add 1
81,326 to 104,116:
add 2
A grid of values ÿ8, ÿ6, ÿ4, ÿ2, ÿ1, 0, 1, and 2
was created by reclassifying the raw sums grid in
accordance with the above mapping. This is the
``spatial context'' grid that we need to indicate general
areas of positive habitat versus poor habitat (Fig. 4). A
fairly smooth pattern emerges in which the middle part
of the region, with its extensive grassland, is the most
favorable general area. Near urban and developed
areas such as the west±central, neighborhood value
Fig. 3. The decay in the impact of a neighborhood cell with distance from the central cell.
246
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


declines sharply. This is an intended result and re¯ects
the incompatibility of urban and developed uses with
kit fox habitat. Grassland cells near such urban areas
(and another developed area at the north end) may
have good intrinsic ratings but will have poor ®nal
rankings after their spatial context has been accounted
for. Other poorly ranked areas include surface water
(for obvious reasons) and the extensive tracts of oak
woodland.
It makes sense now to revisit the weighting scheme
of grassland  4, woodland  0, cropland=wetland 
ÿ2, water  ÿ4, and urban  ÿ20 (under assumption
(2) above). The goal is to create appropriate relative
weights. Inevitably, there is a subjective element to
such a scoring scheme. However, there is a visible
advantage in using negative numbers for non-habitat
because it becomes easy to see what areas are down-
graded based on situational (neighborhood) concerns.
The sharply negative category, urban, is scored intrin-
sically at ÿ20 so that not only is urban itself con-
sidered inhospitable, but for a certain distance away, at
the urban±wildland interface, there will be a lingering
downgrade of habitat value due to the neighborhood
effect.
The neighborhood categories as valued in Fig. 4
re¯ect a desire to make it more likely for a cell to
decline in habitat value based on spatial context than
to increase in value. Certainly, there is no requirement
to use eight categories as we have done as opposed to
seven or 10 categories; nor do the categories have to be
based on an even partition of the range of raw sums.
Several alternatives were tried, but the results were
Fig. 4. `Neighborhood effect' grid.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
247


either clearly unrealistic or varied little from those
shown here (i.e., the results were quite robust on this
data set). So while the neighborhood effect ®lter
derived here is not the only such datalayer that could
be derived, it is certainly a realistic one based on the
data at hand.
To create a ®nal habitat value grid that incorporates
biological assumption (1), we summed the intrinsic
habitat value grid (Fig. 2) and the spatial context grid
(Fig. 4). This created a grid with 24 different values
ranging from ÿ28 to 6. It is super¯uous to retain
many rankings that are all highly negative in nature.
To create a more manageable number of categories,
we consolidated the values from ÿ28 to ÿ4 and
assigned to them the value ÿ4, and remaining values
stayed the same, except that those cells that were
developed or urban were rolled back to their original
intrinsic value of ÿ20. This left us with 12 rankings of
®nal habitat value which may be regarded as preli-
minary values, pending any necessary ®nal modi®ca-
tions such as incorporating roads.
Up to this point, our derivation of habitat value has
relied on the vegetative cover in the region. Given the
presence of major roads in the area, we felt that it was
necessary to modify our results by introducing road
corridors within the landscape as barriers to animal
movement. After consulting with biologists and plan-
ners familiar with the area, the list of relevant roads
was narrowed to one freeway (which slices the region
into northern and southern parts) and two secondary
(two-lane) roads. The latter two were incorporated
simply by converting their line representations to grid
cells and inserting them onto the preliminary ®nal
habitat value layer. The freeway, however, is a much
Fig. 5. De®ning the freeway road barrier.
248
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


more signi®cant barrier to kit fox movement. In
addition, land immediately along the road is inhos-
pitable habitat due to noise and traf®c danger. To
model the freeway's presence accurately, we decided
to buffer the freeway corridor. This procedure
involved making a grid representation of the freeway,
widening that by one cell thickness on each side to
create a 200 m buffer around the traf®c lanes (Fig. 5).
This buffered corridor was then overlaid onto the
preliminary ®nal habitat value map that was calculated
from the vegetation data (Fig. 6). This type of buffer-
ing rests on the idea that out to a certain radius there
are negative impacts due to highways (noise, etc.), but
beyond that radius, such impacts sharply drop off.
The buffer approach has an advantage in that the
radius can be expanded or contracted depending on
Fig. 6. Total habitat values for the San Joaquin Kit Fox.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
249


local conditions. The user can be as conservative as
desired in applying the proper radius and once again
de®nes the value of the relevant parameter. (The 12
®nal habitat value categories, ranging from ÿ20 to 6,
are consolidated to eight categories in Fig. 6 in order
to create a more manageable black and white ®gure
for publication.)
4. Discussion
The path taken to arrive at the ®nal habitat value
grid in Fig. 6 is not unique. There are many decision
points along the way. For example, roads could have
been included earlier, in the intrinsic habitat value
map, and then been processed as part of the neighbor-
hood effect analysis. The result would have been a
gradual decline in ®nal habitat value as one nears a
road; it is conceivable that this approach would be
superior to our use of a buffer around roadways,
depending on the species or circumstances of the
application. Numerous other aspects of the basic
approach are variable. For example, the choice of
raster cell size is variable, as is the priority determina-
tion of which habitat types are assigned to which cells
(in the conversion from vector to raster). Assumptions
regarding intrinsic valuation of habitat types, relevant
neighborhood size for each cell (based on estimated
daily animal movement), the form of distance-decay
(if any) to apply to calculate the neighborhood sums,
how sums should be categorized, how wide of a road
buffer to use, etc. are all variable. Different choices
could result in outcomes different from those illu-
strated here. We in fact investigated multiple alter-
natives before deciding on the strategy that produced
the results presented here. In all cases, the overall
results were quite similar, i.e., sensitivity analysis was
performed, and the results on our data were quite
stable.
We feel that presenting a general method that may
be tailored to particular circumstances will be of most
use to practitioners. An approach that leaves little open
for local modi®cation, and simply imposes a single
answer, will not be effective. Different environmental
conditions will affect kit fox habitat value within its
range, and there is likely always to be some level of
uncertainty among biologists regarding habitat pre-
ferences of most species. Particularly in the US, any
regional plan (HCP, Environmental Impact Statement,
others) is subject to lengthy public comment and
often to legal challenge. In the face of this, planning
methods need to be ¯exible and process-oriented
rather than static and ®xed. Otherwise, they are likely
to fail.
Although we have used an area in the kit fox's
northern range to illustrate our procedure, the same or
similar methods could be used in other locations (e.g.,
Kern County, Carrizo Plain, Salinas Valley). This
would likely involve different assumptions regarding
habitat preferences, daily movement patterns, and
range sizes. The most appropriate parameters for
the species and area of interest easily ®t into the
general type of process that we describe here for
developing a GIS habitat value surface (Fig. 7). There
is no one method or answer that can be applied in a
process such as this, but a series of choices that must
be resolved based on the most reasonable biological
input and local knowledge available. However, our
general process of combining intrinsic value and
situational value based on mapped environmental
variables and imposing the presence of signi®cant
barriers where they exist should be applicable to many
different mobile species, not just the kit fox.
There seems to have been only a single previous
attempt to estimate potential kit fox habitat in the
eastern-Alameda±Contra Costa region, by Bell et al.
(1994). Using a combination of ground and aerial
reconnaissance, they estimated 108,000 acres of
potential habitat in the two counties. In our effort that
resulted in Fig. 6, we have about 112,000 acres of
habitat with a ®nal value of 4 or higher. The value 4
was the original intrinsic value of a preferred habitat
(grassland) cell and so is the most reasonable bench-
mark for comparison. Our result of 112,000 acres is
quite close to the 108,000 acres of Bell et al. (1994). In
terms of habitat with value 3 or higher, our method
estimates 124,000 acres.
How might the habitat values map (Fig. 6) be used?
One way is general analysis of where the best potential
kit fox habitat is located. This information could be
pro®tably used to direct mitigation funds or other
habitat protection funds to areas of highest value.
To assess future threats, one could intersect Fig. 6
with other datalayers, such as zoning and pending
projects, to try to predict how much good habitat is
threatened or likely to be lost soon. Another use,
250
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


having much potential, is to combine cells into viable
territories that could support kit fox pairs or social
groups. For example, a reasonable assumption in this
part of the northern range is that a pair of kit foxes
needs 4 square miles of best quality (grassland) habi-
tat. This translates directly to a minimum habitat value
total or score of 1536 in Fig. 6 (i.e., 256 cells all of
value 6). In areas where habitat is less than ideal,
attaining the requisite score for a viable patch will
necessitate more total area. Such a larger territory
Fig. 7. Process overview.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
251


likely would offer less prey density and might be more
dif®cult to defend but perhaps would be minimally
acceptable as habitat. By investing as we have in up-
front biological and behavioral input, subsequent
analysis such as territory generation is made easier.
Gilpin et al. (1998) describes methods for generating
viable kit fox territories using the spatial model of
habitat value in Fig. 6.
Vegetative cover is likely the single most important
environmental variable with respect to evaluating San
Joaquin Kit Fox habitat. However, our reliance on
vegetation cover and roads as the primary factors
in¯uencing habitat value was a function of data avail-
ability and does not mean that other factors are without
importance and utility. Perhaps the most signi®cant
omission herein is the lack of soils data. Detailed soils
data were unavailable for this study. Soils can be an
important environmental variable because the use of
numerous dens (more easily created and expanded in
certain soil types) seems to be of great importance to
fox survival strategy. Foxes will change dens several
times a month, at least outside of the breeding season,
probably as a strategy to avoid their primary predator,
coyotes (Bell, 1998; Koopman et al., 1998). The kit
fox is thought to prefer friable soils for ease of digging
and maintaining dens (O'Farrell, 1983). Presence of
hardpan layers or near-surface water or bedrock are
signi®cant deterrents to denning. However, the role of
soil type in in¯uencing kit fox habitat value is not
well understood. Bell (1998) indicates that the
species is found on virtually every soil type, including
high-clay soils in eastern-Alameda±Contra Costa.
Bell (1994) found a positive association between kit
fox presence and clay soils in Alameda±Contra Costa
but further noted that the result may only re¯ect the
fact that clay soil is very common in the region. If true,
this suggests that including soils data would have
created little change in our results reported here. As
it was, the ®nal habitat values map (Fig. 6) was
presented to personnel of CDFG and USFWS as well
as the local jurisdictions, and their feedback was
positive.
However, if a habitat evaluation analysis were
undertaken in other parts of the kit fox range such
as the Carrizo Plain or Ciervo-Panoche area (central
California), soils could be an important consideration
and could complicate the spatial distribution of habitat
value. The important point for our purposes is that our
fundamental approach would not change if other
environmental variables such as soils were included.
A cell's intrinsic value can always be adjusted to
re¯ect additional information, and the use of a spatial
®lter to de®ne the local context of each cell would
proceed in the same manner.
Our approach in this paper is to evaluate potential
habitat, as opposed to relying on sighting or occur-
rence data. It will always be extremely dif®cult to map
species distributions directly based on empirical evi-
dence. The CDFG spotlight survey program attempts
to do this but is limited to a small number of areas and
has never been carried out in the Alameda±Contra
Costa region.
This is not to say that direct observations are not
valuable. Numerous methods have been used, includ-
ing aerial surveys, scent station counts, radio collaring
and tracking, and spotlight surveys. In the Alameda±
Contra Costa area, Bell et al. (1994) conducted trans-
ect surveys using baited traps in an attempt to ®nd kit
foxes (none were found). Although the CDFG spot-
light survey program has never been active in the
northern kit fox range, we do have a 25-year record of
sighting data through the California Natural Diversity
DataBase Program. There are 109 data points grouped
in Alameda, Contra Costa, and adjacent San Joaquin
Counties. These data are valuable in that they verify
the persistence of the kit fox in the Alameda±Contra
Costa study area, including sightings in the far
north (Black Diamond Mines Regional Preserve) in
the early 1990s. However, these data are of limited
use for planning purposes because the inventory has
been spatially and temporally highly uneven. This
means that the absence of kit fox occurrences on
the map does not necessarily mean an absence of
the species but possibly only an absence of inventory
effort.
Realistically, conservation planning for the kit fox
in many parts of its range will depend on evaluating
potential habitat through physical environmental vari-
ables that can be mapped and stored, manipulated, and
displayed using GIS. The dif®culty of aerial and
transect surveys and the other means of counting
highlight that we probably will never be able to assess
directly these populations, and thus a potential habitat
approach must be a signi®cant element of the planning
toolbox. Furthermore, this applies to numerous other
species as well.
252
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


5. Conclusion
Habitat conversion continues to threaten endan-
gered species such as the San Joaquin Kit Fox,
while conservation efforts by governmental and
non-governmental agencies continue. While a signi®-
cant amount of ®eldwork has revealed substantial
biological information on the kit fox, there has been
little or no attempt to convert this into a spatially
explicit form for planning purposes. Yet this step is
vitally necessary for future conservation assessment
centered around the fox, which has been on the
endangered list for 30 years. The kit fox's importance
is further magni®ed because it is used as an umbrella
species for grassland habitat, meaning that habitat set-
asides granted to the wide-ranging fox could collat-
erally protect many other species as well (Bell, 1998;
Kelly et al., 1997). In fact, policy-level umbrella status
for the San Joaquin Kit Fox was conferred by the
recent Recovery Plan for Upland Species in the San
Joaquin Valley. The reason: its ``broad distribution and
requirement for relatively large areas of habitat means
that conservation of the kit fox will provide an
umbrella of protection for many other species that
require less habitat'' (USFWS, 1998).
Current interest in conservation of grassland, oak
woodland, and seasonal wetlands in northern Califor-
nia is underscored by the purchase in mid-1998 of
61,000 acres near Mt. Hamilton, just south of our
study area, by the non-pro®t, The Nature Conservancy
of California. This purchase, the largest protected area
ever acquired in northern California, contains habitats
much like those of eastern-Alameda±Contra Costa. It
was justi®ed partly on the basis of securing the future
of the kit fox, as well as of the California red-legged
frog (recently listed as ``threatened'') and the south-
western pond turtle, which are also inhabitants of our
Alameda±Contra Costa study area.
Our strategy in this paper was to incorporate as
much biological information as possible to create a
model of spatial habitat value in a GIS format. The
vegetation map was the paramount environmental
layer because of known feeding behavior and habitat
use by the kit fox. Other signi®cant layers, principally
soils, could be added later without altering the basic
technique. We assigned intrinsic cell values and then
used the GIS to pass a spatial ®lter over the intrinsic
habitat values, leading to a ``neighborhood effect'' that
measured the spatial context of each cell. The ®nal
result was a map of potential habitat value for the kit
fox that combined intrinsic and neighborhood value
and also incorporated road barriers.
The analysis of potential habitat herein is ultimately
an input to other questions such as: What size, type,
and number of blocks of habitat would be necessary to
conserve this relatively wide-ranging species? How
much of the best quality kit fox habitat is in the most
imminent danger of loss? Assuming planned devel-
opment projects go forward, how much kit fox habitat
would remain 10 years hence and in what spatial
con®guration? What areas should be considered for
acquisition if mitigation funds become available? The
GIS habitat value model derived in this paper can
provide a needed basis for regional assessment of this
important mammal. Furthermore, many other species
could have their potential habitat evaluated using the
same basic approach.
Acknowledgements
This research was conducted as part of a Working
Group supported by the National Center for Ecologi-
cal Analysis and Synthesis, funded by the National
Science Foundation (Grant No. DEB-94-21535), the
State of California, and the University of California at
Santa Barbara.
For biological opinion and data on the kit fox, we
thank Heather Bell and Sheila Larsen of the US Fish
and Wildlife Service, Joanne Karlton and Kevin Hunt-
ing of the California Department of Fish and Game,
Linda Spiegel of the California Energy Commission,
Katherine Ralls of the Smithsonian Institute, and
Patrick Kelly and Scott Phillips of the San Joaquin
Valley
Endangered
Species
Recovery
Planning
Program.
For access to various data sets of the region and for
continuing input on the local area, we thank Beth
Stone and Brad Olson of the East Bay Regional Park
District.
References
Begley, S., 1997. Survival by handout? Natl. Wildl. (December±
January), 52±57.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
253


Bell, H.M., 1994. Analysis of habitat characteristics of San
Joaquin Kit Fox in its northern range. Master's Thesis in
Biological Sciences. California State University, Hayward,
CA.
Bell, H.M., 1998. San Joaquin Kit Fox (Vulpes macrotis mutica),
pp. 122±136. In: Recovery Plan for Upland Species of the San
Joaquin Valley, California. US Fish Wildlife Service, Region 1,
Portland, OR, 319 pp.
Bell, H.M., Alvarez, J.A., Eberhardt, L.L., Ralls, K., 1994.
Distribution and abundance of San Joaquin Kit Fox. Research
Report. Department of Fish and Game, The Resources Agency,
State of California. Unpublished.
Dennis, B., Otten, M., 2000. Joint effects of density dependence
and rainfall on abundance of San Joaquin Kit Fox. J. Wildl.
Mgmt. 64, 388±400.
ESRI (Environmental Systems Research Institute, Inc.), 1996. Arc/
Info Version 7.04. Redlands, CA.
Gilpin, et al., M., 1998. The patch: a spatial unit for conservation
reserve design optimization. Working Paper. National Center
for Ecological Analysis and Synthesis.
Jones and Stokes Associates, Inc., 1996. Data Contract with US
National Biological Service, Sacramento, CA.
Kelly, P.A., Williams, D.F., Cypher, B.L., 1997. The San Joaquin
Kit Fox as an umbrella species for conservation efforts in
central
California.
Annual
Meeting
of
the
Society
for
Conservation Biology, Victoria, BC, June 9 (Abstract available
at: http://arnica.csustan.edu/esrpp/scbfox2.htm).
Knapp, D.K., 1978. Effects of agricultural development in Kern
County, California, on the San Joaquin Kit Fox in 1977.
Research
Report.
Department
of
Fish
and
Game,
The
Resources Agency, State of California.
Koopman, M.E., Scrivner, J.H., Kato, T.T., 1998. Patterns of
den use by San Joaquin Kit Foxes. J. Wildl. Mgmt. 62,
373±379.
Laughrin, L., 1970. San Joaquin Kit Fox: its distribution and
abundance. Research Report. Department of Fish and Game,
The Resources Agency, State of California.
Morrell, S.H., 1971. The life history of the San Joaquin Kit Fox.
Master's Thesis in Zoology. University of California, Santa
Barbara, CA.
Morrell, S.H., 1975. San Joaquin Kit Fox distribution and
abundance in 1975. Research Report. Department of Fish and
Game, The Resources Agency, State of California.
Natural Diversity DataBase Program. Department of Fish and
Game, The Resources Agency, State of California. http://
www.dfg.ca.gov.
O'Farrell, T., 1983. San Joaquin Kit Fox recovery plan. US Fish
and Wildlife Service (Contract No. DE-ACOB-76NV01183),
January 31.
Orloff, S., Hall, F., Spiegel, L., 1986. Distribution and habitat
requirements of the San Joaquin Kit Fox in the northern
extreme of their range. Trans.: West. Section Wildl. Soc. 22,
60±70.
Ralls, K., Eberhardt, L.L., 1997. Assessment of abundance of San
Joaquin Kit Foxes by spotlight surveys. J. Mammal. 78, 65±73.
Ralls, K., White, P.J., 1995. Predation on San Joaquin Kit Foxes by
larger canids. J. Mammal. 76, 723±729.
Spiegel, L.K., 1996. Studies of the San Joaquin kit fox in
undeveloped and oil-developed areas. Research Report No.
P700-96-003. California Energy Commission, 131 pp.
White, P.J., Ralls, K., 1993. Reproduction and spacing patterns of
kit foxes relative to changing prey availability. J. Wildl. Mgmt.
57, 861±867.
White, P.J., White, C.A.V., Ralls, K., 1996. Functional and
numerical responses of kit foxes to a short-term decline in
mammalian prey. J. Mammal. 77, 370±376.
US Fish and Wildlife Service, 1998. Recovery plan for upland
species of the San Joaquin Valley, California. US Fish and
Wildlife Service, Region 1, Portland, OR, 319 pp. (Executive
summary).
Zoellick, B.W., Smith, N.S., 1992. Size and spatial organization of
home ranges of kit foxes in Arizona. J. Mammal. 73, 83±88.
Zoellick, B.W., Smith, N.S., Henry, R.S., 1989. Habitat use and
movements of desert kit foxes in western Arizona. J. Wildl.
Mgmt. 53, 955±961.
Ross Gerrard, Ph.D. serves as Principal Investigator at ISERA
Group, Inc. on a Phase II Small Business Innovative Research
award (from the US National Science Foundation) to develop
decision support software for public school districting and
enrollment forecasting. Recently he completed a Post-doctoral
Research appointment with the National Center for Ecological
Analysis and Synthesis (NCEAS) at the University of California at
Santa Barbara (UCSB). His research at NCEAS involved using
optimization modeling to pursue the selection of natural reserves
and protected areas for multi-species conservation. This included
extensive GIS, database, and user interface development. Dr.
Gerrard received his Ph.D. in Geography from UCSB in 1995. His
dissertation focused on optimal location/districting models for
public sector facilities and developed two new integer program-
ming formulations geared to that topic. He has presented research
at several national conferences and has co-authored several articles
for refereed academic journals.
Peter Stine, Ph.D. is an Ecologist at the Western Ecological
Research Center of the US Geological Survey Biological
Resources Division in Sacramento, CA. He has extensive
experience in HCP development throughout California and was
formerly with the US FWS working in that regard. He has recently
worked extensively in environmental assessment and regional
ecological monitoring programs in such regions as the Mojave
Desert, the San Francisco Bay Delta, and the southern California
coastal ecoregion, and was significantly involved in California Gap
Analysis. Dr. Stine received his Ph.D. in Geography from UCSB in
1995.
Richard Church is a Professor of Geography at UCSB. He has
extensive experience in the modeling of complex logistics and
spatial optimization problems. He received a Ph.D. from the Johns
Hopkins University in Environmental Systems Engineering in
1974. He specializes in applied Operations Research as well as
Location and Transportation research and Decision Support
Systems. He has published over 100 papers and monographs in
related journals and research publication series. Dr. Church has
254
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255


served as a consultant to numerous federal agencies and private
companies. He has recently published in the area of conservation
reserve design and is supervising a decision support system for the
US Forest Service and Bureau of Land Management.
Michael Gilpin is a Professor of Biology at the University of
California, San Diego. He has pursued a wide range of problems in
theoretical population biology, including island biogeography,
community structure, and population genetics. In recent years,
his laboratory has established strong ties with the US FWS and the
National Marine Fisheries Service to understand recovery issues
facing endangered species, such as grizzly bears, Columbia River
salmon stocks, desert tortoises and kangaroo rats. Professor Gilpin
received his Ph.D. from UC Irvine. He is an editor for the Journal
of Theoretical Biology and received a Guggenheim Fellowship to
investigate optimal management of captive species.
R. Gerrard et al. / Landscape and Urban Planning 52 (2001) 239±255
255
