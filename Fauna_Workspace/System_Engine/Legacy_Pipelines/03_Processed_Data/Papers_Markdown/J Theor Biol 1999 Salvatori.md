--- 
source: J Theor Biol 1999 Salvatori.pdf
--- 

J. theor. Biol. (1999) 198, 567}574
Article No. jtbi.1999.0936, available online at http://www.idealibrary.com on
Estimating Temporal Independence of Radio-telemetry Data on
Animal Activity
V. SALVATORI*?, A. K. SKIDMORE*, F. CORSI- AND F. VAN DER MEER*
*International Institute for Aerospace Survey and Earth Science (I¹C), P.O. Box 6, 7500 AA Enschede,
¹he Netherlands and -Institute of Applied Ecology (IEA), <ia ¸. Spallanzani 32, 00161 Roma, Italy
(Received on 5 January 1999, Accepted in revised form on 15 March 1999)
Radio-telemetry is an excellent tool for gathering data on the biology of animals and their
interactions with the environment they inhabit. Many methods have been developed for
analyses of spatial information, on home range size and utilization density. Activity patterns
are often described using radio-tracking data, but no generally accepted method is currently
available speci"cally for determining the temporal independence of this type of data for
statistical inference. Activity rhythms have generally been analysed by ecologists with the
assumption that data are temporally independent, or by subjectively "xing an independence
interval, based on attributes of their ranging behaviour. Although some good approximations
of activity patterns can be obtained in these ways, we underline the need for a functionally
correct method of estimating independence interval. Here we use semi-variograms to estimate
the minimum interval required for the readings to be sequentially independent. This geostatis-
tical tool is applied to the analysis of data on activity of Chilean foxes (Pseudalopex culpaeus)
and Chacoan peccaries (Catagonus wagneri). Data were collected in the "eld by radio-tracking
over 24-hr periods, with readings on activity state taken every 15 min. The spatial dimension in
which the theory of geostatistics lies has been transferred into the time dimension, so that the
correlation interval is expressed in time units (min). Time of independence as estimated by the
variogram was 110 min for foxes, while data on peccaries indicated that they have long periods
of activity, more suitable for time-series analysis.
( 1999 Academic Press
Introduction
Animal activity has been the focus of a consider-
able number of studies, particularly with respect
to mammals (Dann & Asho!, 1975; Dallaire
& Ruckebusce, 1974). Data on small-sized ani-
mals can be collected in the laboratory, yielding
information on internally regulated rhythms of
? Author to whom correspondence should be addressed.
Present address: Department of Geography, University of
Southampton, High"eld, Southampton SO17 1BJ, U.K.
E-mail: vs497 @soton.ac.uk.
activity (zeitgeber, Nielsen, 1984). Data collected
in the "eld are preferred by ecologists, as the
patterns of alternating sleep and activity are
strongly in#uenced by environmental (extrinsic)
rather than individual (intrinsic) factors for all
animals, producing much inter-individual varia-
bility, which can sometimes swamp underlying
patterns (McNamara & Houston, 1986). Making
data discontinuous and increasing the interval
between activity records can smooth the detailed
individual variability. In this way, the assump-
tion of independence may be satis"ed and statis-
tical tests can then be used for inference.
0022}5193/99/013567#08 $30.00/0
( 1999 Academic Press


The monitoring of animal movements by
radio-tracking provides useful data on the behav-
iour of individuals, particularly those living in
closed environments or having nocturnal habits,
as the radio signal obviates the need to observe
them directly (Amlaner & Macdonald, 1980). Ac-
tivity data from radio-telemetry are frequently
analysed with inferential statistics, testing di!er-
ences in percentages of activity at di!erent times
of the day (Garshelis & Pelton, 1980) to draw
conclusions and generalizations. The probability
theory underlying parametric and non-paramet-
ric statistics assumes that sampling is random,
and successive observations are independent.
Only under these assumptions it is appropriate to
apply inferential statistical tests (Sokal & Rohlf,
1995; Steel & Torrie, 1960). In the presence
of autocorrelation, the statistical estimates for
a sample will be biased with respect to the popu-
lation (Diggle, 1990). Tests for dependent data
and methods for resampling data should be ap-
plied to avoid this problem.
Independence of activity data is particularly
hard to assess, as it is not set by any "xed param-
eter. An animal's state of activity will be in-
#uenced by its previous or future state of activity,
so &&inactivity'' and &&activity'' are dependent. In
other words, the states are temporally autocor-
related, which means that samples collected in
rapid succession will be more similar compared
to those collected at longer intervals (Rossi et al.,
1992). Although autocorrelation of ecological
variables has been considered in the spatial di-
mension (Legendre & Fortin, 1989)*and spatial
correlograms have been used to make structural
inference about ecological response surfaces
(Sokal, 1979)*very few studies in the last two
decades have focused on autocorrelation of activ-
ity over time from radio-tracking data. Where it
has been done, correlograms have been used to
estimate cyclicity within the 24-hr period (Don-
caster & Macdonald, 1997). If the data on activity
are collected continuously and at regular inter-
vals, they are suitable for time-series analysis of
the periodicity of activity patterns (Diggle, 1990).
In most cases involving radio-tracking, however,
data are not evenly spaced in time, or if they are,
they rarely cover continuous periods longer than
the 24-hr cycle, making it impossible to detect
over-circadian patterns or cycles.
We have reviewed a sample of 36 papers pub-
lished in the last two decades on animal activity
where data were collected by telemetry tech-
niques. We looked at the methods used for ana-
lyses, and how independence of data was treated.
In two instances, time-series analysis was con-
ducted (Taber et al., 1993; Doncaster & Mac-
donald, 1997), and data were highly correlated
over periods of at least 8 hr. In the remaining 34
publications, analyses involved inferential statis-
tics, with the implicit assumption that data were
independent. Of these studies, 21 ignored the
possibility of autocorrelation, and treated data as
if they were independent. In six cases, the prob-
lem of data independence was tackled in a subjec-
tive way, and an independence interval was set
according to the author's perception. In seven
studies the time for independence was estimated
by objective methods, including the runs test
(Branch, 1993), the Markov chains (Arthur
& Krohn, 1991), or by applying the same inde-
pendence interval calculated for spatial analysis
of ranging behaviour (Salvatori et al., 1999).
In this paper, we use the semi-variogram func-
tion to analyse patterns in the time dimension
from data collected by radio-telemetry. The semi-
variogram is the basic tool in geostatistics. It is
a curve showing the dissimilarity in the outcome
of sampling as the distance between observation
sites increases (Olea, 1991). We test the e$cacy of
this treatment for the estimation of an &&interval of
independence'' for radio-telemetry data, which
can be used either a priori, while optimizing data
collection in the "eld, or a posteriori, while re-
sampling data for statistical analyses. We exam-
ine the outputs from the semi-variogram for the
information they provide on the characteristics of
the species as well as the nature of data.
The Semi-variogram Function
Geostatistics is used for the detection and es-
timation of spatial patterns (Matheron, 1963), in
other words it is the study of phenomena that
#uctuate in space (Olea, 1991). The "eld origin-
ally started with the objective of improving fore-
casts of ore grade and reserves in mining, but the
mathematical generality of the approach led to
the application in other earth science and related
"elds
of
application
such
as
soil
patterns
568
V. SALVATORI E¹ A¸.


(Varekamp et al., 1997) and optimal sampling
problems (Curran & Atkinson, 1998), to name
a few. The most promising results in geostatistics
have been achieved in estimation and forecasting,
extending the probabilistic-stochastic methods
to the spatial domain; the regionalization of
statistics.
Geostatistics assumes that, on average, sam-
ples closed together in time and/or space are
more similar than those that are farther apart.
Spatial continuity tools such as the variogram
are used to infer the spatial autocorrelation based
on random function theory (Journel & Huij-
bregts, 1978). Let z(x) represent the value of
a variable at location x, where x is a vector (x, y),
and let z(x#h) represent the value of the same
variable at some h distance (or lag) and direction
away. Assuming stationarity, the expectation of
the variable z(x) is constant, equal to the mean
value (of the observations) and independent of
location x. Thus,
E[z(x)]"k.
Similarly, the second-order stationarity assump-
tion implies that the covariance of a variable z(x)
measured at two locations x and x#h depends
only on the distance between the two points and
not on the values z(x) and z(x#h) as
CO<[z(x), z(x#h)]"E[z(x)z(x#h)]
!E[z(x)]E[z(x#h)]
"E[z(x)z(x#h)]!kk.
The covariance function C(h) can be de"ned as
C(h)"E[z(x)z(x#h)]!k2.
If the covariance C(h) is stationary, the variance
and semi-variogram are also stationary
C(0)"E[z(x)!k2]"<AR[z(x)],
c*(h)"EM[z(x#h)!z(x)]2N/2/
"C(0)!C(h),
where the * in c*(h) indicates that these are ex-
perimental semi-variance values derived only for
a number of discrete distance classes. The semi-
variogram now summarizes the spatial con-
tinuity for all possible pairings of data for all
signi"cant lag distances h as
c*(h)" 1
2n(h)
n(h)
+
i/1
[z(xi)!z(xi#h)]2,
where n(h) is the number of pairs of points separ-
ated by a distance h. Mathematical model curves
are
"tted
through
experimentally
obtained
semi-variances either by expert judgement or
through least-squares "tting approaches. These
models are de"ned by a range, a, and sill vari-
ance, C. The range is the distance at which
the statistical dependency in the data is lost
and variability is purely random. The sill vari-
ance is the corresponding variance found for
pairs separated over distances greater than the
range (Fig. 1).
Variograms often exhibit a non-zero y-inter-
cept, the nugget variance, C0. This variance can
be attributed to measurement errors and to
variability at spacing smaller than the average
sampling interval. Nugget variance can be in-
corporated in variogram models as a second
component stacked on top of the structurally
controlled component of the variance as
c(h)"C0#c1(h).
Commonly used models are the spherical model
de"ned as
c(h)"G
CC
3
2A
h
aB!1
2A
h
aB
3D
04h(a,
C,
h5a;
the exponential model de"ned as
c(h)"C(1!e~h@a);
the linear model de"ned as
c(h)"Ch;
INDEPENDENCE OF ANIMAL ACTIVITY DATA
569


FIG. 1. Variogram parameters.
the Gaussian model de"ned as
c(h)"C [1!e~(h@a)2];
and the power model de"ned as
c(h)"Cha.
As the semi-variance value at di!erent inter-
vals is directly dependent on the statistics of the
pairs corresponding to each interval, a small
number of pairs will result in less reliable results
(Isaaks & Srivastava, 1989). As a rule of thumb,
geostatisticians suggest that each interval class
must be represented by at least 30}50 pairs of
points (Journel & Huijbregts, 1978), but this de-
pends on the underlying data and method used to
estimate the variogram.
The variogram permits estimation of the min-
imum interval required for the data to be inde-
pendent. Since it assumes that the variance in the
data is represented by a model, it could be argued
that the estimate is acceptable only under the
particular assumptions of the model (de Gruijter
& ter Braak, 1990). Despite this constraint,
model-based sampling has been shown to be
more e!ective than design-based approach for
answering questions such as &&how much?'' (i.e.
the global average value of a variable over a
period of time) and &&when?'' (i.e. the structural
di!erences within a period of time) (Hauvelink,
1997; Webster, 1999).
Methods
Animal activity was detected for Chilean foxes
(Pseudalopex culpaeus) and Chacoan peccaries
(Catagonus wagneri). Data were collected on indi-
vidual animals over a 24-hr schedule, with binary
readings
0}1
(0"non-active,
1"active)
at
15-min intervals, yielding up to 96 observations
in each session (Salvatori et al., 1999; Taber et al.,
1993). Percentages of activity in the 24 hr were
computed hourly as the proportion of active
readings.
A moving average was used to smooth di!er-
ences between 1-hr blocks (Bailey & Gatrell,
1995), and to increase the number of data that
made up single-block statistics (Isaaks & Srivas-
tava, 1989). Percentages of activity then assumed
a continuous distribution over the 24-hr period,
and were considered to be highly dependent on
each other within the minimum time lag of
15 min between "xes.
Variogram models were "tted to the experi-
mental data using a weighted least-squares ap-
proach as advocated by Journel & Huijbregts
(1978, Section III.C. 6) and David (1977, Sections
6.1 and 6.2). This implies that a constant lag spac-
ing has to be selected to derive the experimental
570
V. SALVATORI E¹ A¸.


semi-variances for discrete distances of h. The
model to be "tted to experimental variograms
was chosen by looking at the squares sum of
deviations (SSD) and the weighted total sum of
squares (SST). The model corresponding to the
minimum value of the ratio between SSD and
SST was selected. This also gives a measure of the
variance explained by the selected model. Given a
model type, a weighted least-squares approxima-
tion will yield the optimum values of the vari-
ogram model parameters by measuring the close-
ness of "t by the sum of squares of the di!erences
between a generic variogram estimator (i.e. ex-
perimental values) 2c* (h) and a model 2c* (h; h),
where h are the model parameters (i.e. range, sill
and nugget). The method we used for the least-
squares "tting is outlined in Cressie (1991) and
estimates h by minimizing
K+
i/1
M2c*(hi)e!2c(hie; h)N2
for some direction of e.
In order to have a comparable number of pairs
at each considered h, semi-variances were com-
puted setting the maximum lag at 12 hr.
Results
Forty-"ve sessions of 24-hr activity data were
available for analysis. Thirty-three were taken on
seven foxes and 12 on four peccaries over the four
seasons. All the data sets produced variograms
exhibiting small variance values for short time
intervals, with increasing variance values as the
time interval became longer.
The models "tted to experimental variograms
were able to explain a high portion of the vari-
ance of the data. The average explained variance
was 87% (min"34.4, max"98.9), with two
outliers lowering the overall goodness of "t,
explaining less than 50% of the data variance.
The average was 89.3% when they were not
considered.
Data on fox activity showed variance values
increasing toward an asymptote, re#ecting the
degree of temporal variability or, conversely,
continuity of data. Although not all the vario-
grams reached a stable sill, all of them showed the
same pattern of initially increasing variance with
FIG. 2. Plot of semi-variogram function from data on
activity
of
a
Chilean
fox.
Experimental
model:
c(h)"1!e~h@a, where a"range"1.15, this model ex-
plained 87.6% of the data variance.
greater intervals of time between sampling points
(Fig. 2). In some cases the variance increased
almost linearly until it reached a stage after which
the behaviour changed abruptly.
Beyond the range, the behaviour of the semi-
variogram di!ered between individuals, most
probably due to the small number of pairs avail-
able for larger time intervals. Except for one
outlier, the values of the range lay between less
than 1 and 3 hr, showing that the individual
variation was not large. The ranges of semi-
variograms obtained from data collected in peri-
ods with di!erent environmental characteristics
(i.e. seasonality, availability of food) were consis-
tent, highlighting an overall constant pattern of
variability in activity. The mean range value was
110 min (n"33; 95% con"dence limits after log-
normal transformation: 89}134). Comparison
with the independence interval estimated by
methods based on spatial movement of the ani-
mals (336 min, Salvatori et al., 1999), showed that
the variogram estimate di!ered signi"cantly from
the spatial estimate (paired t-test, t"!2.8;
d.f."6; p(0.05).
For the peccary data, the values for all the
semi-variograms increased with the time interval
considered, but in no case was a sill reached.
Plotted over a period of 12 hr the variance in-
creased linearly (Fig. 3).
No range values were estimated for the peccary
data as experimental semi-variograms were best
"tted by linear or power models, which had no
INDEPENDENCE OF ANIMAL ACTIVITY DATA
571


FIG. 3. Plot of semi-variogram function from data on
activity of a Chacoan peccary. Power model: c(h)"hx,
where x"0.55, this model explained 94.7% of the data
variance.
sill within the time period considered. Despite the
absence of a sill, it is possible to interpret activ-
ities which are characteristic of the species. In this
case, the semi-variograms suggest the presence of
a linear gradient. The autocorrelation exhibited
by the data set remains dependent within the
sampling interval, and never reaches an uncor-
related distribution within 12 hr.
Discussion
A continuously distributed variable may as-
sume similar values at closely spaced intervals. In
classical geostatistics the interval is space, where-
as in this paper the interval is time. In either case,
closely spaced observations cannot be regarded
as independent for the purpose of statistical test-
ing. From our review of published papers on
animal activity based on radio-tracking data, it
appears that an objective and universally suitable
method is needed for the estimation of temporal
independence. Where dependent data are used
for analyses with methods assuming indepen-
dence, pseudo-replication renders the signi"-
cance tests of questionable value (Sokal & Rohlf,
1995).
Methods used for testing independence in
radio-telemetry data include:
1. the runs test (Branch, 1993).
2. Markov chains (Arthur & Krohn, 1991).
3. Collection of data using design-based samp-
ling (e.g. strati"ed random design Green
& Bear, 1990; Somers, 1997).
4. The time required for the animals to cross an
average home range (Salvatori et al., 1999,
Doncaster & Macdonald, 1997).
The runs test does not give a direct estimate of
the independence interval, but rather an indica-
tion of whether the data are randomly distributed
(Sokal & Rohlf, 1995). Although it can be very
e$cient for this purpose, it does not measure the
interval needed to resample the data in order to
reach independence. The Markov chain is a
probabilistic model that can provide estimates of
the independence interval. Its application can be
di$cult, however, for irregularly spaced data
(Ball, 1985). The strati"ed random design ensures
random sampling at the data collection stage
(Altmann, 1974; Brus & de Gruijter, 1997). How-
ever, it can result in an ine$cient sampling e!ort,
because to collect enough data to represent the
whole 24-hr period may require much "eld e!ort
and time (Webster, 1999). Furthermore, it must
be considered that radio-telemetry data are most
frequently collected for various analytical pur-
poses over and above activity (e.g. habitat use),
so that a sampling design that respects temporal
and spatial data independence providing the
maximum available information is not always
possible. For this reason it is often useful to
resample the data for independence. Finally, the
method used by Salvatori et al. (1999) considered
independence in the spatial dimension, and was
thus not a priori a correct estimate for the time
dimension. The resulting temporal independence
interval was actually greater than necessary for
the activity data. Thus, although the assumption
of temporal independence was respected, it led to
an underuse of the available data set.
The sampling strategy in the study of peccaries
and foxes was such that only at a time interval
greater than 10 hr was the number of pairs
smaller than 50. This gives some con"dence to
the
estimate
of
the
independence
interval
for the fox data, particularly because it falls
within an interval of 4 hr in 97% of the com-
puted semi-variograms, allowing statistics to be
carried out on samples of at least 80 pairs. The
variance value in the peccary data decreased if
572
V. SALVATORI E¹ A¸.


plotted over long periods, showing a unimodal
pattern in all cases. The small number of pairs
(n(30) obtained for the time intervals longer
than 14 hr meant that no inferences may be
drawn from the semi-variogram pattern at this
scale.
The variograms for the two species used here
re#ect the di!erences in activity rhythms shown
by diverse species. According to their ecology,
animals might exhibit very well de"ned periods of
activity, such as the Chacoan peccary, a noctur-
nal herbivore; or they might show a more ran-
dom distribution of activity in the 24-hr period,
as shown by the Chilean foxes, an opportunistic
carnivore. Taber et al. (1993) conducted a time-
series analysis on the Chacoan peccary data set,
and described a unimodal pattern of activity,
with a periodicity of 24 hr. The same pattern was
suggested by the semi-variograms, which showed
an activity variance that did not reach an asym-
ptote within any one 12-hr block.
One
advantage
of
the
geostatistical
tool
described here over other methods such as time-
series analysis is that data do not need to be
recorded at regular intervals in order to success-
fully calculate a semi-variogram (Diggle, 1990),
and missing data do not need to be estimated to
"ll the gaps, as is often the case in multivariate
analysis (Webster & Oliver, 1990). Using geo-
statistics, the interval for which data exhibit
temporal independence, as estimated from each
semi-variogram, may be calculated in a robust
and objective manner. The calculations are based
on a large number of samples, as the di!erences
(lag) between all time intervals are utilized. The
periodicity at which the time series data exhibit
independence may be used as a basis for resamp-
ling the available data set. The resampled data
may be assumed to be independent, and therefore
used in classical inferential statistics.
The time for independence estimated by the
semi-variogram is also of interest for the purpose
of optimizing "eld data collection. Data may be
recorded more intensively at the beginning of
a study in order to estimate an optimal time
interval for sampling from geostatistics. With ac-
tivity data such as those shown in Fig. 3 for the
peccaries,
the
semi-variogram
proves
useful
in identifying the most appropriate method of
analysis.
In summary, testing the assumption of tem-
poral independence is problematic for some
ecological data sets, particularly those based on
radio-telemetry, where the continuous variable of
activity can only be collected at discrete and
irregular intervals. We present a geostatistical
technique for objectively estimating temporal in-
dependence, which can help to optimize sampling
techniques and to avoid biases in the inferences
drawn from radio-telemetry data.
A.B. Taber kindly supplied data on Chacoan pecca-
ries. We wish to express our gratitude to A. Cam-
panella and G. Vaglio-Laurin for collaborating in the
data collection on Chilean foxes. Prof. A. Stein
(Wageningen Agricultural University) kindly pro-
vided us with software COKRIG. Special thanks to
C.P. Doncaster for insightful comments during prep-
aration of the manuscript. F.F. Palomares, C. Ron-
dinini, I. Sinibaldi and two anonymous reviewers who
revised previous drafts of the manuscript provided
useful comments.
REFERENCES
ALTMANN, J. (1974). Observational study of behavior: samp-
ling methods. Behaviour 49, 227}267.
AMLANER, C. J. & MACDONALD, D. W. (eds). (1980).
A Handbook of Biotelemetry and Radio ¹racking. Oxford:
Pergamon press.
ARTHUR, S. M. & KROHN, W. B. (1991). Activity patterns,
movements and reproductive ecology of "shers in South-
central Maine. J. Mammal 72, 379}385.
BAILEY, T. C. & GATRELL, A. C. (1995). Interactive Spatial
Data Analysis. Burnt Mill, England: Longman Group Ltd.
BALL, M. A. (1985). In: Mathematics in the Social and ¸ife
Sciences: ¹heories, Models and Methods (Bell, G. M. ed.).
Chichester, England: Ellis Horwood Ltd.
BRANCH, L. C. (1993). Seasonal patterns of activity and
body-mass in the plains vizcacha, ¸agostomus maximus
(family Chinchillidae). Can. J. Zool. 71, 1041}1045.
BRUS, D. J. & DE GRUIJTER J. J. (1977). Random sampling
or geostatistical modelling? Choosing between design-
based and model-based sampling strategies for soil (with
Discussion). Geoderma 80, 1}59.
CRESSIE, N. A. C. (1991). Statistics for Spatial Data, 900pp.
New York: Wiley.
CURRAN, P. J. & ATKINSON, P. M. (1998). Geostatistics and
remote sensing. Prog. Phys. Geog. 22, 61}78.
DAAN, S. & ASHOFF, J. (1975). Circadian rhythms of loco-
motor activity in captive birds and mammals: their vari-
ation with season and latitude. Oecologia 18, 269}316.
DALLAIRE, A. & RUCKEBUSCE, Y. (1974). Rest-activity cycle
and sleep patterns in captive foxes (<ulpes vulpes). Experi-
entia 30, 59}60.
DAVID, M. (1997). Geostatistical Ore Reserve Estimation,
364pp. Amsterdam: Elsevier.
DE GRUIJTER, J. J. & TER BRAAK, C. J. F. (1990). Model-free
estimation from spatial samples: a reappraisal of classical
sampling theory. Math. Geol. 22, 407}415.
INDEPENDENCE OF ANIMAL ACTIVITY DATA
573


DIGGLE, P. J. (1990). ¹ime Series. A Biostatistical Introduc-
tion. Oxford: Clarendon Press.
DONCASTER, C. P. & MACDONALD, D. W. (1997). Activity
patterns and interactions of red foxes (<ulpes vulpes) in
Oxford city. J. Zool. ¸ond. 241, 73}87.
GARSHELIS, D. L. & PELTON, M. R. (1980). Acitity of black
bears in the Great Smoky Mountains National Park.
J. Mammal 6, 8}19.
GREEN, R. A. & BEAR, G. D. (1990). Seasonal cycles and
daily activity patterns of rocky mountain elk. J. =ildl.
Manage, 54, 272}279.
HEUVELINK, G. B. M. (1997). In Discussion of: D. J. Brus
& J. J. de Gruijter, Random sampling or geostatistical
modelling. Geoderma 80, 45}59.
ISAAKS, E. H. & SRIVASTAVA, R. M. (1989). An Introduction
to Applied Geostatistics, Oxford: Oxford University Press.
JOURNEL, A. G. & HUIJBREGTS, C. J. (1978). Mining Geo-
statistics. London, England: Academic Press.
LEGENDRE, P. & FORTIN, M-J. (1989). Spatial patterns and
ecological analysis. <egetatio 80, 107}138.
MATHERON, G. (1963). Principles of geostatistics, Econ.
Geol. 58, 1246}1266.
MCNAMARA, J. M. & HOUSTON, A. I. (1986). The common
currency for behavioral decision. Am. Nat. 127, 358}378.
NIELSEN, E. T. (1984). Relation of behavioural activity
rhythms to the changes of day and night. A revision of
views. Behaviour 89, 147}173.
OLEA, R. A. 1991. Geostatistical Glossary and Multilingual
Dictionary 177pp. Oxford: Oxford University Press.
ROSSI, R. E., MULLA, D. J., JOURNEL, A. G. & FRANZ, E. H.
(1992). Geostatistical tools for modeling and interpreting
ecological spatial dependence. Ecol. Monogr. 62, 277}314.
SALVATORI, V., VAGLIO-LAURIN, G., MESERVE, P. L.,
BOITANI, L. & CAMPANELLA, A. (1999). Spatial organiza-
tion, activity, and social interactions of culpeo foxes
(Pseudalopex culpaeus) in North-central Chile. J. Mammal
80, in press.
SOKAL, R. R. (1979). Ecological parameters inferred from
spatial correlograms. In: Contemporary Quantitative Ecol-
ogy and Related Ecometrics, pp. 167}196. Fairland, Md:
International Co-operative Publishing House.
SOKAL, R. R. & ROHLF, F. J. (1995). Biometry, 3rd Edn.
New York: W. H. Freeman and Co.
SOMERS, M. J. (1997). Activity patterns and activity budgets
of warthogs (Phacochoerus aethiopicus) in the Eastern
Cape Province, South Africa. Afr. J. Ecol. 35, 73}79.
STEEL, R. G. D. & TORRIE, J. H. (1960). Principles and
Procedures of Statistics. New York: McGraw-Hill.
TABER, A. B., DONCASTER, C. P., NERIS, N. N. & COLMAN,
F. H. (1993). Ranging behavior and population dynamics
of the Chacoan peccary, Catagonus wagneri. J. Mammal
74, 443}454.
VAREKAMP, C., SKIDMORE, A. K. & BURROUGH, P. A. B.
(1977). Using public domain geostatistical and GIS soft-
ware for spatial interpolation. Photogr. Eng. Rem. Sens. 62,
845}854.
WEBSTER, R. (1999). Sampling, estimating and understand-
ing soil pollution. In: GeoEN< II: Geostatistics for Envir-
onmental Applications (Gomez-Hernandez, J., Soares, A.
& Froidervaux, R., eds). Dordrecht: Kluwer Academic Pub-
lishers, in press.
WEBSTER, R. & OLIVER, M. A. (1990). Statistical Methods in
Soil and ¸and Resource Survey. Oxford: Oxford University
Press.
574
V. SALVATORI E¹ A¸.
