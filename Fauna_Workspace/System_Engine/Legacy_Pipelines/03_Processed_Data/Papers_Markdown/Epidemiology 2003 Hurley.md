--- 
source: Epidemiology 2003 Hurley.pdf
--- 

ORIGINAL ARTICLE
Post Office Box Addresses: A Challenge
for Geographic Information System-Based Studies
Susan E. Hurley,* Theresa M. Saunders,† Rachna Nivas,* Andrew Hertz,† and Peggy Reynolds‡
Background: Geographic information system (GIS)-based health
studies require information on the physical location of data points,
such as subject addresses. In a study of California women diagnosed
with breast cancer between 1988 and 1997, we needed to locate the
residential addresses of 4,537 women with post ofﬁce boxes (POBs).
Methods: We investigated the feasibility of tracing street addresses
for the POBs and examined potential selection biases and case
attribute misclassiﬁcations introduced by different methods of han-
dling POBs in GIS-based health studies.
Results: Our tracing method yielded street addresses for only 34%
of POBs in our study. Examination of subjects’ case characteristics
revealed that boxholders were not representative of the full popula-
tion. Geocoding using a POB’s delivery-weighted ﬁve-digit zip code
centroid, as a proxy for street address, resulted in case attribute
misclassiﬁcation for 81% of boxholders.
Conclusions: Disease registries should modernize their infrastruc-
ture to complement GIS technologies. Epidemiologists should un-
derstand GIS data limitations and consider potential biases intro-
duced by incomplete or inaccurate geocoding.
(Epidemiology 2003;14: 386–391)
G
eographic information systems (GIS) technology is be-
coming increasingly important in public health re-
search.1–5 Recognizing the utility of GIS in health research,
the US Department of Health and Human Services recently
set a goal of increasing the proportion of government health
data systems using address geocoding to promote nationwide
use of GIS at all levels.6 The ﬁrst step in GIS projects is to
geocode the data points of interest (ie, assign a location such
as latitude/longitude, census tract, and so on). One common
starting point for epidemiologic studies is the geocoding of
subjects’ residential addresses. Once geocoded, locational
attributes can be assigned to subjects (eg, socioeconomic
status and proximity to environmental toxicants). While gov-
ernment agencies are responding to the call for geocoded
data, issues related to geocoding quality and completeness
remain only partially explored.5,7
We are currently using GIS to evaluate environmental
factors related to regional variations in breast cancer inci-
dence in California. Because of our study’s focus, we are
concerned about potential biases introduced by regional dif-
ferences in successful geocoding. Of particular concern are
addresses that cannot readily be geocoded, such as post ofﬁce
boxes (POBs). It is a common practice to assign latitude/
longitude coordinates to POBs based on their delivery-
weighted ﬁve-digit zip code centroid (the geographic center
point of a polygon formed by the zip code boundaries). The
effects of potential biases and misclassiﬁcation introduced by
such geocoding methods have not been fully scrutinized.
A preliminary geographic assessment of our subjects
with POBs, compared with those with street addresses, sug-
gested that they were distributed unevenly throughout the
state and were more likely to be in rural locations. Hence, we
conducted a small substudy to geocode the POB addresses in
our breast cancer study and to assess the quality of this
coding.
METHODS
Our study protocols were approved by the Committee
for the Protection of Human Subjects of the California Health
and Human Services Agency. The California Cancer Registry
(CCR) provided us with the records of all women in Califor-
nia diagnosed with invasive breast cancer between 1988 and
1997 (N  181,110). The CCR extracts information from
patients’ hospital records; patients’ addresses at diagnosis are
geocoded for the CCR by Geographic Data Technology
(GDT).8 This work focuses on 4,537 (2.5%) women from our
breast cancer study who had POB addresses. Of these, 4,299
had traditional post ofﬁce boxes, 192 had rural/star route
Editor’s note: An invited commentary on this article appears on page 384.
Submitted 25 June 2002; ﬁnal version accepted 2 March 2003.
From the *Public Health Institute, †Impact Assessment, Inc, and ‡California
Department of Health Services–Environmental Health Investigations
Branch, Oakland, CA.
This work was supported by the National Institutes of Health/National
Institute of Environmental Health Sciences Grant # U01 CA/ES81789.
Correspondence: Peggy Reynolds, California Department of Health Services,
Environmental Health Investigations Branch, 1515 Clay Street, Suite
1700, Oakland, CA 94612. E-mail: preynold@dhs.ca.gov.
Copyright © 2003 by Lippincott Williams & Wilkins
1044-3983/03/1404-0386
DOI: 10.1097/01.EDE.0000073161.66729.89
Epidemiology • Volume 14, Number 4, July 2003
386


boxes, 39 had highway contract boxes, 6 had general delivery
boxes, and 1 had a military box.
We explored several tracing methods to obtain residen-
tial street addresses for these women and pilot tested each to
determine their cost and effectiveness. Many had limitations
precluding their use for our purposes (Table 1). The most
promising strategy was to obtain street address information
from POB rental records of the US Postal Service. Federal
Regulations9 allow the US Postal Service to release boxhold-
ers’ street address information to other government agen-
cies.10 During October and November of 2002, we mailed
4,537 inquiries to postmasters throughout California, request-
ing the name and street address of the person who held each
POB on the date indicated in the CCR records as the subject/
boxholder’s diagnosis date. To protect our subjects’ conﬁ-
dentiality, we revealed neither their names nor the signiﬁ-
cance of the date.
We calculated the postmasters’ response rate (Fig. 1)
and evaluated whether each postmaster-provided street ad-
dress was a match to our subject (ie, likely to represent the
subject’s street address at diagnosis). We considered each
postmaster-provided address a match if the boxholder’s last
name was the same as our subject’s last or maiden names or
if the postmaster-provided address was a residential facility;
addresses were considered not to be a match if the boxhold-
er’s last name differed from the subject’s last name or if the
boxholder was a business or nonresidential institution. We
attempted to geocode and map the matched street addresses
by standardizing them using ZP4 software11 and then assign-
ing geographic coordinates to each address using ArcView
GIS12 with GDT street data. Of the 1,547 matched addresses,
we geocoded 1,063 (69%) using ArcView batch-matching
and 415 (27%) using manual geocoding. We evaluated the
potential effect of excluding nonmatched addresses from our
geographic analyses by comparing the case characteristics of
subject/boxholders whom we could and could not match to a
street address.
Major US geocoding vendors such as GDT routinely
use the delivery-weighted ﬁve-digit zip code centroid (zip-
centroid; Fig. 2) of a POB to assign a proxy residential
location. Because residential addresses are often distributed
unevenly throughout zip code polygons, zip-centroids have
been developed to account for the actual distribution of
residences throughout a zip code.8 We geocoded all boxhold-
ers’ addresses and determined their US Census block-group
assignment by two methods: ﬁrst using the zip-centroid of the
POB and second using the postmaster-provided street ad-
dress. To assess potential case-attribute misclassiﬁcation, we
TABLE 1.
Summary of Limitations for Address Tracing Techniques Pilot Tested as Possible Means of Obtaining Street
Addresses for Boxholders
Information Source
Chief Limitations
US Postmaster post ofﬁce box rental records
▪For some boxholders, only current information available.
▪Manual, labor-intensive process required to request information.
Department of Motor Vehicles records
▪Addresses linked to drivers’ license renewal date, which may not reﬂect the true
date the subject lived at address.
▪Address provided may be post ofﬁce box.
▪Difﬁcult, lengthy process to establish records access.
▪Provides only current address and one previous address.
911 Emergency Services records
▪Requires knowledge of subject’s phone number.
▪Provides only street addresses (not residents’ names).
Social Security Administration records
▪Difﬁcult, lengthy process to establish records access.
Free Internet White Pages and reverse directories
▪Provides only current information for individuals listed in local telephone
directories.
▪Often provides only a phone number (no address).
▪Requires labor-intensive, individual record searching.
Fee-based reverse directory service
▪Provides only current information for individuals listed in local telephone
directories.
▪Directories not available for all areas in California.
▪Requires knowledge of subject’s home phone number
Fee-based identiﬁcation and credential veriﬁcation
▪Information limited to public records and publicly available information.
services
▪Dates associated with residences may not be accurate.
▪Address provided may be a post ofﬁce box.
▪Costly service.
Epidemiology • Volume 14, Number 4, July 2003
POB Addresses: A Challenge for GIS Studies
© 2003 Lippincott Williams & Wilkins
387


compared the degree of urbanization,13 socioeconomic status
(SES), and agricultural pesticide exposure measure14 as-
signed to subjects based on their geographic locations derived
from these two geocoding methods. Since GIS-based envi-
ronmental health studies often assign exposure attributes
based on a subject’s proximity to a certain location of interest
(eg, incinerator, air monitoring site), we evaluated the poten-
tial for exposure misclassiﬁcation by calculating the distance
between the geocoded point of the zip-centroid of the POB
and the boxholder’s street address.
RESULTS
Postmaster Response Rates
Although their overall response rate was good (90%),
postmasters provided us with boxholder street addresses in
only 1,963 (47%) of their 4,193 responses (Fig. 1). The more
recent the address information we asked for, the more likely
it was that postmasters could provide it (Fig. 3). Our inquiries
regarding rural/star route and highway contract boxes were
less likely to yield a street address (31% and 13%, respec-
tively) than inquiries regarding traditional post ofﬁce boxes
(44%). Street addresses do not exist for general delivery and
military boxes.
Assessment of Potential Biases
In approximately 2.5% of the CCR records in our breast
cancer study, subject addresses were limited to a POB.
(During the period of our study, patients with other types of
cancer had similar percentages of POB addresses in their
records.) Boxholders were more likely to be age 50 or older
and non-Hispanic white (Table 2). Comparing boxholders
whom we could and could not match, we found that race/
ethnicity distributions were similar between the 2 groups;
not-matched subjects were slightly more likely than matched
FIGURE 1. Postmaster responses to inquiries requesting street
addresses for post office boxholders.
FIGURE 2. Sample delivery-weighted zip code centroid with overlay of zip code region, census block groups and census tracts for
a rural area in California.
Hurley et al
Epidemiology • Volume 14, Number 4, July 2003
© 2003 Lippincott Williams & Wilkins
388


to have later stage disease at diagnosis and to be in the
youngest (50 years) and oldest (70 years) age groups.
We found substantial discordances between area-
attribute assignments based on geocoded POB zip-centroids
and street addresses provided by postmasters (Table 3). When
street address, rather than POB zip-centroid, was used to
pinpoint subjects’ geographic location, 81% were assigned to
a different census block-group. We saw less dramatic but still
substantial discordance in area-attribute assignments (urbaniza-
tion, SES and agricultural pesticide exposure); most notably,
43% of subjects were assigned to a different SES quartile.
The distance between each subject’s street address and
her POB’s zip-centroid was within 1 mile for 25% of the
street addresses; most were within 5 miles of the zip-centroid
(Fig. 4). However, 25% of our boxholders had a geocoded
street address that fell more than 4.3 miles away from the
zip-centroid.
DISCUSSION
Our results demonstrate that it is possible to obtain
street addresses for POB holders from the US Postal Service,
but this approach is unlikely to yield substantial improvement
in overall geocoding success, particularly for older addresses.
Furthermore, the use of zip-centroids as a proxy for residen-
tial street address may result in substantial misclassiﬁcation
of geographically-based attributes.
Reliance on POB tracing through postal service records
alone is not ideal. Using only the postmaster responses, our
means of matching boxholders and study subjects was limited
TABLE 2.
Characteristics of Boxholders and Non-boxholders Among Women Diagnosed
with Invasive Breast Cancer in California between 1988 and 1997 as Identified in the
California Cancer Registry
Case Characteristic
Boxholders
Non-Boxholders
(N  176,574)
Matched to a
Street Address
(N  1,582)
Not Matched to a
Street Address
(N  2,955)
No.
%
No.
%
No.
%
Age at diagnosis
50 years
338
(21)
653*
(22)
41,380
(23)
50–69 years
785
(50)
1,349*
(46)
74,882
(43)
70  years
459
(29)
952*
(32)
60,312
(34)
Race/ethnicity
Non-Hispanic White
1,373
(87)
2,608
(88)
136,311
(77)
Non-Hispanic Black
29
(2)
71
(2)
10,033
(6)
Hispanic
114
(7)
185
(6)
18,063
(10)
Non-Hispanic Asian
or Paciﬁc Islander
33
(2)
45
(2)
10,107
(6)
Other
33
(2)
46
(2)
2,060
(1)
Stage at diagnosis
Early
989
(63)
1,718
(58)
110,377
(63)
Late
523
(33)
1,082
(37)
56,783
(32)
Unknown
70
(4)
155
(5)
9,414
(5)
* Total N for boxholders not matched to a street address  2,954; one subject has an unknown age at
diagnosis.
FIGURE 3. Postmaster response by year POB was held by
subject.
Epidemiology • Volume 14, Number 4, July 2003
POB Addresses: A Challenge for GIS Studies
© 2003 Lippincott Williams & Wilkins
389


to a comparison of their names. Of the nonmatching street
addresses, 16% were for boxholders with a different last
name than our subject’s. We cannot discount the possibility
that excluding these women from our analyses might intro-
duce additional bias. Although our match rate may have
improved had we revealed the subject/boxholders’ names, we
did not do so to protect our subjects’ conﬁdentiality. Addi-
tionally, it puts a burden on the postal service to make tracing
requests that could be satisﬁed through other resources.
Using all the tracing methods at our disposal (see Table
1), would have been costly and labor intensive without
increasing our POB/street address match rate dramatically.
The overarching limitation we faced was our need for histor-
ical information. We asked postmasters for address informa-
tion that was 3–12 years old. However, because of postal
service policies on record keeping, we could not expect POB
holder information from 2 years or more earlier to be avail-
able unless the boxholder had maintained her box continu-
ously to the present. Any of the other tracing methods we
explored would have yielded considerably better results, if
performed within 2 years of initial case ascertainment.
These results suggest a need for a reevaluation of data
collection practices and a modernization of registry infra-
structure that will allow GIS to be used to its full potential.
Concerted efforts by cancer reporting abstractors and central
registry staff to ascertain case street addresses (rather than
POBs) would help improve the quality of address information
in registry records. Although the California Cancer Registry’s
geocoding is over 95% complete for residential addresses, it
is important to recognize and evaluate the potential effect of
missing data on GIS-based health research. In our breast
cancer study, POB addresses accounted for the majority
(75.5%) of ungeocodable addresses. Our analysis of box-
holder case characteristics suggests that they are not neces-
sarily representative of the whole case population and that
excluding them could introduce selection bias. Assigning
POBs to zip-centroids may also introduce substantial geo-
graphically-based exposure misclassiﬁcation.
Although these differences may not be critical to all
health studies that use disease registry data, it is important to
consider such data limitations in the context of individual
research questions. For example, some of our breast cancer
study’s environmental exposure assignments are based on
residential proximities of a half mile or less, whereas our
analyses revealed that the median distance between POB
zip-centroids and boxholder street addresses was 2.2 miles,
with some discrepant by more than 100 miles. We remain
uncertain about why these larger discrepancies might exist;
possible explanations include subjects with high mobility or
multiple residences and reporting errors on the part of post-
masters, disease registry abstractors or boxholders them-
selves. Clearly, reliance on POB zip-centroids for geocoding,
in our breast cancer study, would result in substantial expo-
sure misclassiﬁcation. GIS-based health studies also face the
challenge of address-matching errors, arising from incom-
plete or erroneous source data and geocoding base maps.
Base-map errors, such as positional inaccuracy and bad or
theoretical address ranges that introduce interpolation error,
can cause locational errors in address geocoding.
It is unknown to what extent our results can be gener-
alized outside California. The data quality concerns we faced
may be magniﬁed for researchers studying rural populations,
TABLE 3.
Concordance of Breast Cancer Case
Characteristics When Using Data Based on Geocoded
Delivery-Weighted Zip Code Centroids of Post Office Box
Addresses and Corresponding Geocoded Boxholder Street
Addresses
Case Characteristic
Percent
Discordant*
US Census Block-group
81
Urban/rural status of block-group†
6
Socioeconomic status of block-group (quartiles)‡
43
Exposure to agricultural pesticides (quintiles)§
25
* Percent of subjects assigned to different categories by the two methods.
† Based on US Census deﬁnition of an urban area (ie, a centralized area
with a population  50,000 and a population density 1,000 people/mi2).13
‡ Based on SES quartiles from the sum of rankings for all California
block-groups by education, family income and occupation.
§ Based on quintiles of pesticide use density, by pounds per square mile
applied, derived from 1990 California Pesticide Use Report (PUR) data using
methods of Gunier et al.14 (0  1 lb/mi2; ﬁrst quintile  1–9 lbs/mi2;
second quintile  10–36 lbs/mi2; third quintile  37–119 lbs/mi2; fourth
quintile  120–444 lbs/mi2; and ﬁfth quintile  444 lbs/mi2.)
FIGURE 4. Distance between geocoded boxholder street ad-
dress points and delivery-weighted five-digit zip code cen-
troids of corresponding POBs. Minimum  0; 1st quartile 
0.98 miles; median  2.20 miles; 3rd quartile  4.29 miles;
maximum  437 miles. (The largest discrepancies may repre-
sent people with high mobility or multiple residences, or they
may be caused by reporting errors.)
Hurley et al
Epidemiology • Volume 14, Number 4, July 2003
© 2003 Lippincott Williams & Wilkins
390


for whom disease registry records are likely to contain a
higher proportion of POB addresses.
Disease registry data are a valuable epidemiologic re-
source. The emergence of GIS technology as an epidemio-
logic tool promises new scientiﬁc insights but depends on the
availability of useable geographic data. While disease regis-
tries work toward improving the quality and completeness of
their geocoded data, epidemiologists should understand the
limitations of such data and consider, within the context of
their research questions, the potential biases introduced by
incomplete or inaccurate geocoding.
ACKNOWLEDGMENTS
We thank the California Cancer Registry for providing
the data used in this study. We also thank the legal staff of the
US Postmaster General’s ofﬁce for their assistance with the
composition and formatting of the inquiry letters used in our
substudy. Our gratitude is extended to local postmasters
throughout California for their timely and helpful responses
to our inquiries.
REFERENCES
1. Richards T, Croner C, Rushton G, et al. Geographic information systems
and public health: mapping the future. Public Health Rep. 1999;114:
359–373.
2. MacDorman M, Gay G. State initiatives in geocoding vital statistics
data. J Public Health Manage Pract. 1999;5:91–93.
3. Thrall G. The future of GIS in public health management and practice.
J Public Health Manage Pract. 1999;5:75–82.
4. Bouton PB, Fraser M. Local health departments and GIS: the perspective
of the National Association of County and City Health Ofﬁcers. J Public
Health Manag Pract. 1999;5:33–41.
5. Williams RC, Howie MM, Lee CV, et al. Geographic information systems
in public health: proceedings of the third national conference [Agency for
Toxic Substances and Disease Registry, GIS in Public Health web site].
1998. Available at: http://www.atsdr.cdc.gov/gis/conference98/index.html.
Accessed January 15, 2002.
6. US Department of Health and Human Services. Healthy People 2010
(Volumes I and II). 2nd Edition. Washington, DC: U.S. Government
Printing Ofﬁce; 2000. (Publication No. S/N 017-001-00547-9).
7. Krieger N, Waterman P, Lemieux K, et al. On the wrong side of the
tracts? Evaluating the accuracy of geocoding in public health research.
Am J Public Health. 2001;91:1114–1116.
8. Dynamap/ZIP4 centroids and correspondence ﬁles [data ﬁle]. Leba-
non, NH: Geographic Data Technologies (GDT); 2002.
9. Ofﬁce of the Federal Register, National Archives and Records Adminis-
tration. United States Code of Federal Regulations, Title 39, Postal Service;
Chapter I, United States Postal Service; Part 265, Release of Information,
Section 265. 6(d)(4)(i). Available from U. S. Government Printing Ofﬁce
(http://www.access.gpo.gov/nara/cfr/waisidx_01/39cfr265_01. html). Last
updated July 1, 2001.
10. US Postal Service. Domestic Mail Manual, Part D910 - Post Ofﬁce Box
Service [USPS Postal Explorer web site]. May 2, 2002. Available at:
http://pe.usps.gov/text/dmm/d910. htm. Accessed June 15, 2002.
11. Semaphore Corporation. ZIP4 database and CASS-certiﬁed address
cleaning software [Semaphore Corp., Free Internet Resources web site].
February 1, 2001. Available at: http://www.semaphorecorp.com/cgi/zp4.
html. Accessed March 1, 2001.
12. ArcView. Version 3.2a. Redlands, CA: Environmental Systems Research
Institute; 2000.
13. US Bureau of the Census. Census of Population and Housing, 1990:
Summary Tape File 3 on CD-ROM Technical Documentation. Wash-
ington, DC: Bureau of the Census; 1992.
14. Gunier RB, Harnly ME, Reynolds P, et alJ. Agricultural pesticide use in
California: pesticide prioritization, use densities, and population distri-
butions for a childhood cancer study. Environ Health Perspect. 2001;
109:1071–1078.
Epidemiology • Volume 14, Number 4, July 2003
POB Addresses: A Challenge for GIS Studies
© 2003 Lippincott Williams & Wilkins
391
