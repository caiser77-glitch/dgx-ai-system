--- 
source: Ecological Modelling 2006 Calenge.pdf
--- 

ecological modelling 1 9 7 ( 2 0 0 6 ) 516–519
available at www.sciencedirect.com
journal homepage: www.elsevier.com/locate/ecolmodel
Short communication
The package “adehabitat” for the R software: A tool for the
analysis of space and habitat use by animals
Cl´ement Calenge ∗
UMR CNRS 5558, Laboratoire de Biom´etrie et de Biologie Evolutive, Universit´e Claude Bernard Lyon 1, 69622 Villeurbanne Cedex, France
a r t i c l e
i n f o
Article history:
Received 15 September 2005
Received in revised form 1 February
2006
Accepted 14 March 2006
Published on line 18 April 2006
Keywords:
R software
Adehabitat
Habitat selection
Space use
Wildlife
Home range
Package
a b s t r a c t
The practical analysis of space use and habitat selection by animals is often a problem due
to the lack of well-designed programs. I present here the “adehabitat” package for the R
software, which offers basic GIS (Geographic Information System) functions, methods to
analyze radio-tracking data and habitat selection by wildlife, and interfaces with other R
packages. These tools can be downloaded freely on the internet. Because the functions of
this package can be combined with other functions of R, “adehabitat” provides a powerful
environment for the analysis of the space and habitat use.
© 2006 Elsevier B.V. All rights reserved.
The study of the relationships between animals and their
environment is one of the main issues in ecology. It implies
the analysis of the use of space by animals, of the inter-
actions between animals, and of the relationships between
animals and their habitat. The recent development of Geo-
graphic Information Systems (GIS) has made easier this
type of study, and especially the study of habitat selection,
by taking into account more explicitly the spatial dimen-
sion of the data in the analyses (Manly et al., 2002). This
expanded the range of possible analysis, and as a result
numerous methods have been developed during the last
decade in this ﬁeld of Ecology (e.g. Guisan and Zimmermann,
2000).
∗Tel.: +33 4 72 43 27 56; fax: +33 4 72 43 13 88.
E-mail address: calenge@biomserv.univ-lyon1.fr.
However, the practical data analysis remains a problem.
First, the analyst has to perform spatial analyses within a GIS
(computation of buffers (areas containing all points located
within some speciﬁed distance of a mapped feature), estima-
tion of home ranges, etc.), and second, he needs a statistical
software to analyze the data more deeply. After the analy-
ses, he may also need to move the data back to GIS for more
speciﬁcally GIS analyses. The interface between GIS and statis-
tical software is often missing and can make the analysis long
and difﬁcult. In addition, the quality of commercial statistical
program has been criticized by several authors in Ecology sci-
ence (Chessel, 1992; Tufto and Cavallini, 2005). Indeed, such
“canned” programs are not open enough. They provide only
0304-3800/$ – see front matter © 2006 Elsevier B.V. All rights reserved.
doi:10.1016/j.ecolmodel.2006.03.017


ecological modelling 1 9 7 ( 2 0 0 6 ) 516–519
517
standard statistical procedures, and limit the development of
new approaches.
In this framework, open-source software may be viewed as
an alternative (Tufto and Cavallini, 2005). Such programs are
distributed freely under a licence known as the GNU General
Public Licence (GPL; Free Software Foundation and Inc., 1991),
which also relies on standard copyright laws. All the source
code is available, so that a user can make changes inside the
program. The modiﬁed version is also free and available. This
usually results in very efﬁcient programs, because they are
built and modiﬁed by their users.
Tufto and Cavallini still noted that the awareness of this
phenomenon was weaker among biologists than researchers
belonging to other ﬁelds of science, despite its undeniable
desirable qualities. They recommended the use of free soft-
ware, and listed the programs that may be of great interest,
giving a special mention to the R software (R Development
Core Team, 2005).
My purpose is to present, after a brief description of the R
software, the package I developed to analyze the use of space
and habitat selection by animals: “adehabitat”. It gathers a set
of methods, through R functions, intended to provide tools for
biologists.
1.
The R software
Ross Ihaka and Robert Gentleman, from the Auckland Uni-
versity, developed the R software to provide a statistical envi-
ronment to their laboratory in 1992, and based this software
on the S language. This one was invented at the AT&T Bell
Laboratories by John Chambers and his colleagues during the
mid-1970s. They wanted to encourage the user to “slide into
programming, perhaps without noticing” (Chambers, 1998),
and to ensure that a user can easily implement his own tech-
niques.
With the help of Martin M¨achler (working at the ETH
Z ¨urich), Ihaka and Gentleman released this software as free
open-source software in 1995 (Ihaka and Gentleman, 1996).
Presently, the “Comprehensive R Archive Network” (CRAN) is
the core of an increasingly growing R community (Hornik and
Leisch, 2001); it is the central repository for material related
to R, including packages of functions (518 at the time of
writing), tutorials and discussion forums (URL: http://cran.r-
project.org/). The use of R implies the learning of a command
language. At ﬁrst sight, this aspect may seem to be a draw-
back, but it has actually numerous desirable qualities. First,
this language is very intuitive (e.g. a t-test is carried out with
the function t.test(), a generalized linear model is ﬁtted using
the function glm(), etc.). In addition, this language renders eas-
ier the run of repeated and batch analyses. For example, it is
not necessary to repeat manually all the steps of an analysis
if only one detail is to be changed in it. Numerous tutorials
are available on the internet to help users quickly learn the
language.
Several packages are available for the analysis of ecolog-
ical data. Among them, the “ade4” package allows the anal-
ysis of ecological and environmental data in the framework
Fig. 1 – Capture screen of one session with R and the package “adehabitat”.


518
ecological modelling 1 9 7 ( 2 0 0 6 ) 516–519
of Euclidean Exploratory methods (Chessel et al., 2004), the
“vegan” package is intended for the vegetation and com-
munity analysis, and the “GRASP” package aims at building
predictive models of the distribution range of species in bio-
geography, using generalized regression and spatial prediction
(Lehmann et al., 2002).
2.
The “adehabitat” package
I have developed the “adehabitat” package to study the space
use and habitat selection by wildlife. It contains about 100
functions giving tools frequently used in this ﬁeld of research.
The graphical possibilities of this package (Fig. 1), and the
combination of the “adehabitat” functions with the pow-
erful analysis environment provided by R allow the users
to design a large diversity of analyses of the relationships
between animals and their environment. A quick learning
can be carried out with the tutorial included in the pack-
age.
The “adehabitat” package includes functions that create
an interface with GIS commonly used in Ecology, such as
Arcview GIS (ESRI, 1996), the free program GRASS (available
at: http://grass.itc.it/) or the free software Landserf (avail-
able at: www.soi.city.ac.uk/∼jwo/landserf/). Single maps can
be imported within R, and then combined into multilayer
maps; these maps are grids of pixels on which several vari-
ables are measured, allowing multivariate analysis of habitat
use by animals. Several basic GIS functions are also avail-
able in “adehabitat”. It is for example possible to compute
buffers around lines or points, to determine the habitat com-
position at given points, to select sub-areas on a map, to
deﬁne masks, to reduce the resolution of a map, and so
on. In addition, several functions provide an interface with
the spatial classes of the “sp” package which is itself an
interface toward other R packages dealing with spatial data
(Pebesma and Bivand, 2005), another efﬁcient way to analyze
data.
Common analyses of habitat selection may also be carried
out using “adehabitat”. Thus, several functions allow the com-
putation of selection ratios (Manly et al., 2002), compositional
analysis (Aebischer et al., 1993), K-select analysis (Calenge
et al., 2005) or Ecological Niche Factor Analysis (ENFA, Hirzel
et al., 2002). Moreover, habitat suitability maps can be com-
puted using Mahalanobis distances (Clark et al., 1993), the
DOMAIN algorithm (Skov, 2000), or the ENFA (Hirzel et al.,
2002). Resource selection functions may also be ﬁtted, using
the spatial classes of “adehabitat” and the powerful mod-
elling capabilities of R. To take into account the multivariate
aspect of habitat (Hall et al., 1997), this package also pro-
vides an interface with the package “ade4” (Chessel et al.,
2004).
“Adehabitat” also includes several tools suitable for the
analysis of radio-tracking data. Home range estimators
include the minimum convex polygon (Mohr, 1947) the ker-
nel estimator (Worton, 1989), the nearest neighbor convex hull
(Getz and Wilmers, 2004), or the grid method (Siniff and Tester,
1965). And so, the estimates can be used in the analyses of
spatial interactions between animals, habitat selection, etc.
Schoener’s ratio can be computed to detect temporal autocor-
relation in the relocations (Swihart and Slade, 1985), and basic
statistics to analyze animal movements such as speed or turn-
ing angles (Turchin, 1998).
3.
Discussion
The main objective of the “adehabitat” package is to pro-
vide tools for analyzing the relationships between animals
and their environment. Because the R community is very
active, the package is improved frequently, making new func-
tions available to other users. Thus, since its ﬁrst release
in September 2004, two additional versions of the package
have been submitted on CRAN as a result of the sugges-
tions made by the users concerning the methods that would
ﬁnd their place in “adehabitat”. For instance, the recent
development of GPS (Global Positioning System) to moni-
tor space use by animals has raised a number of ques-
tions among ecologists (autocorrelation, how to analyze such
trajectories, etc.). In view of this situation, Paolo Cavallini
(working at Faunalia, Italy) created a discussion forum to
make the communication easier between scientists of various
ﬁelds interested by the analysis of animal movement (URL:
www.faunalia.com/animov/). Several functions of the pack-
age have been added or modiﬁed following discussions that
arose on this forum, e.g. the kernel Brownian bridge estima-
tor of the home range (Bullard, 1991) or the nearest neighbor
convex hull estimator of the home range (Getz and Wilmers,
2004).
The functions of “adehabitat”, and more generally, the R
functions are well documented on the help pages. These pages
describe the arguments and options needed by the functions,
give examples of use, and sometimes the context in which
they were developed and the context in which they are to
be used. Examples of syntax for some standard analyses are
available at the URL: www.faunalia.com/animov/howto.php.
Thus, R is more than a simple technical tool, and becomes
integral part of the development of methods. This illustrates
well the philosophy behind the S language, which is, owing
to the nice expression of Chambers (1998), “to turn ideas into
software”. R is therefore the biometrical tool par excellence. As
the interdisciplinarity emerges today as an important aspect
of science (e.g. Morillo et al., 2003), the R software and the “ade-
habitat” package will be of major use to wildlife biometricians
who are concerned by the use of space and habitat selection
by animals.
Acknowledgments
I would like to thank the “Ofﬁce national de la chasse et
de la faune sauvage” for their ﬁnancial support. I warmly
thank Anne-B´eatrice Dufour (University of Lyon, France) for
her unvaluable comments on earlier drafts on this manuscript.
I am also grateful to Mathieu Basille who programmed the
ENFA and related functions for “adehabitat”, and suggested
many improvements to bring to the package; to Daniel Ches-
sel for his helpful advices about “good programming practice”
and all the users who send us their comments and contributed
to the improvement to the package.


ecological modelling
1 9 7
( 2 0 0 6 ) 516–519
519
r e f e r e n c e s
Aebischer, N.J., Robertson, P.A., Kenward, R.E., 1993.
Compositional analysis of habitat use from animal
radio-tracking data. Ecology 74, 1313–1325.
Bullard, F., 1991. Estimating the home range of an animal: a
Brownian bridge approach, M.Sc. Thesis, Johns Hopkins
University, Chapel Hill, North Carolina.
Calenge, C., Dufour, A.B., Maillard, D., 2005. K-select analysis: a
new method to analyse habitat selection in radio-tracking
studies. Ecol. Model. 186, 143–153.
Chambers, J.M., 1998. Programming with Data. Springer, New
York.
Chessel, D., 1992. Echanges interdisciplinaires en analyse de
donn´ees ´ecologiques. Professoral thesis. Universit´e Lyon 1,
Villeurbanne, France.
Chessel, D., Dufour, A.B., Thioulouse, J., 2004. The ade4
package-I: one-table methods. R News 4, 5–10.
Clark, J.D., Dunn, J.E., Smith, K.G., 1993. A multivariate model
of female black bear habitat use for a geographic
information system. J. Wildl. Manage. 57, 519–526.
ESRI, 1996. Using Arcview GIS, The geographic information
system for everyone, Environmental Systems Research
Institute Inc., USA.
Free Software Foundation, Inc., 1991. GNU General Public
License, version 2. Available at: www.gnu.org/copy
left/gpl.html.
Getz, W.M., Wilmers, C.C., 2004. A local nearest-neighbor
convex-hull construction of home ranges and utilization
distributions. Ecography 27, 489–505.
Guisan, A., Zimmermann, N.E., 2000. Predictive habitat
distribution models in ecology. Ecol. Model. 135, 147–186.
Hall, L.S., Krausman, P.R., Morrison, M.L., 1997. The habitat
concept and a plea for standard terminology. Wildl. Soc.
Bull. 25, 173–182.
Hirzel, A.H., Hausser, J., Chessel, D., Perrin, N., 2002.
Ecological-niche factor analysis: How to compute habitat
suitability maps without absence data? Ecology 83,
2027–2036.
Hornik, K., Leisch, F., 2001. Vienna and R: Love, Marriage and
the Future. In: R., Dutter (Ed.), Festschrift. 50 Jahre
¨Osterreichische Statistische Gesellschaft. ¨Osterreichische
Statistische Gesellschaft, Vienna, Autriche, pp. 61–70.
Ihaka, R., Gentleman, R., 1996. R: a language for data analysis
and graphics. J. Comput. Graph. Stat. 5, 299–314.
Lehmann, A., Leathwick, J.R., Overton, J.M., 2002. GRASP v.2.2
User’s Manual. Landcare Research, Hamilton.
Manly, B.F.J., McDonald, L.L., Thomas, D.L., MacDonald, T.L.,
Erickson, W.P., 2002. Resource selection by animals. In:
Statistical Design and Analysis for Field Studies. Kluwer
Academic Publisher, London.
Mohr, C.O., 1947. Table of equivalent populations of North
American small mammals. Am. Midl. Nat. 37, 223–
249.
Morillo, F., Bordons, M., Gomez, I., 2003. Interdisciplinarity in
science: a tentative typology of disciplines and research
areas. J. Am. Soc. Inf. Sci. Technol. 54, 1237–1249.
Pebesma, E.J., Bivand, R.S. 2005. S classes and methods for
spatial data: the sp package, unpublished report.
R Development Core Team, 2005. R: a language and
environment for statistical computing. R Foundation for
Statistical Computing, Vienna, Austria, www.R-project.org.
Siniff, D.B., Tester, T.W., 1965. Computer analysis of
animal-movement data obtained by telemetry. Bioscience
15, 104–108.
Skov, F., 2000. Potential plant distribution mapping based on
climatic similarity. Taxon 49, 503–515.
Swihart, R.K., Slade, N.A., 1985. Testing for independence of
observations in animal movements. Ecology 66, 1176–1184.
Tufto, J., Cavallini, P., 2005. Should wildlife biologists use free
software? Wildl. Biol. 11, 67–76.
Turchin, P., 1998. Quantitative analysis of movement,
Sunderland, MA.
Worton, B.J., 1989. Kernel methods for estimating the utilization
distribution in home-range studies. Ecology 70, 164–168.
