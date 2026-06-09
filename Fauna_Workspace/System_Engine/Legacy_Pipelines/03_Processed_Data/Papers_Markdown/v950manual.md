--- 
source: v950manual.pdf
--- 

 
Manual Written by: 
Philip S. Miller, Conservation Breeding Specialist Group (SSC/IUCN)  
Robert C. Lacy, Chicago Zoological Society 
 
 
Software Written by: 
Robert C. Lacy, Max Borbat, and JP Pollak 
 
A Stochastic Simulation 
of the Extinction Process
 
 
User’s Manual
VORTEX
Version 9.50


 
 
 
 
 
 
 
 
A contribution of the IUCN/SSC Conservation Breeding Specialist Group in collaboration with the Chicago 
Zoological Society. 
 
VORTEX is provided at no cost, in order to further conservation and science. It is distributed without warranty of its 
suitability for any particular use, and neither the program or this manual is guaranteed to be free of errors, bugs, or 
potentially misleading information. It is the responsibility of the user to ensure that the software is appropriate for 
the uses to which it is put. 
 
VORTEX is owned and copyrighted by the Chicago Zoological Society. The software is not copy-protected. In 
addition to making back-up copies, individuals, not-for-profit organizations, and governmental agencies are hereby 
given licenses for making unlimited copies of VORTEX for the purpose of furthering conservation, teaching, and 
research. 
 
Distribution of VORTEX is restricted to:  
• 
distribution by the Chicago Zoological Society;  
• 
distribution by the IUCN/SSC Conservation Breeding Specialist Group;  
• 
downloading of the program from the Internet (http://www.vortex9.org/vortex.html) by individuals, not-
for-profit organizations, and governmental agencies for their own research and conservation applications;  
• 
redistribution without charge of the unmodified executable program for the purposes described above.  
 
Unauthorized redistribution of VORTEX, in whole or in part by any for-profit organization or for any profit-making 
purposes is expressly forbidden.  
 
 
 
Cover Artwork: Linda Escher, Escher Illustrations. 
 
 
Citation of this manual: 
Miller, P.S., and R.C. Lacy. 2005. VORTEX: A Stochastic Simulation of the Extinction Process. Version 9.50 User’s 
Manual. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
 
Citation of the software program: 
Lacy, R.C., M. Borbat, and J.P. Pollak. 2005. VORTEX: A Stochastic Simulation of the Extinction Process.Version 
9.50.  Brookfield, IL: Chicago Zoological Society. 
 
 
Additional printed copies of VORTEX User’s Manual and installation CDs can be ordered through the IUCN/SSC 
Conservation Breeding Specialist Group, 12101 Johnny Cake Ridge Road, Apple Valley, MN, 55124, USA. Send 
checks for US $75.00 (for printing and shipping costs) payable to CBSG; checks must be drawn on a US bank. 
Funds may be wired to First Bank NA ABA No. 091000022, for credit to CBSG Account No. 1100 1210 1736. 
Lower costs for bulk orders may be arranged.  


 
The CBSG Conservation Council 
These generous contributors make the work of CBSG possible 
 
Benefactors ($20,000 and above) 
Chicago Zoological Society 
Elizabeth Wakeman Henderson  
  Charitable Foundation 
Minnesota Zoological Garden 
Omaha’s Henry Doorly Zoo 
SeaWorld, Inc. 
Toronto Zoo  
 
Conservators ($15,000 -$19,999) 
Columbus Zoological Gardens –  
    The WILDS 
Saint Louis Zoo 
Walt Disney’s Animal Kingdom 
Wildlife Conservation Society - NYZS 
World Association of Zoos &      
Aquariums -WAZA 
Zoological Society of London 
 
Guardians ($7,000-$14,999) 
Cleveland Zoological Society  
Nan Schaffer 
Toledo Zoological Society 
White Oak Conservation Center 
San Diego Zoo 
 
Protectors ($1,000-$6,999) 
African Safari Wildlife Park 
Albuquerque Biological Park 
Alice D. Andrews 
Allwetter Zoo Munster 
Apenheul Zoo 
ARAZPA 
AZA 
Audubon Zoological Gardens 
Bristol Zoo 
Caldwell Zoo 
Calgary Zoo 
Chester Zoo  
Cincinnati Zoo 
Colchester Zoo 
Copenhagen Zoo 
Detroit Zoological Park 
Dickerson Park Zoo 
Durrell Wildlife Conservation Trust 
Dublin Zoo 
El Paso Zoo  
Everland Zoo 
Federation of Zoological Gardens of  
  Great Britain & Ireland 
Fort Wayne Zoological Society 
Fort Worth Zoo 
Gladys Porter Zoo 
Great Plains Zoo 
Greater Los Angeles Zoo Association 
Japanese Association of Zoological 
  Parks & Aquariums –JAZGA 
Leisure & Cultural Services Department 
of Hong Kong 
Lincoln Park Zoo 
Living Desert 
 
 
 
Loro Parque 
Marwell Zoological Park 
Memphis Zoo 
Milwaukee County Zoo 
North Carolina Zoological Park 
Oklahoma City Zoo 
Ocean Park Conservation Foundation 
Paignton Zool. & Botanical Gardens 
Parco Natura Viva—Italy 
Philadelphia Zoological Garden 
Phoenix Zoo 
Pittsburgh Zoo 
Prudence P. Perry 
Randers Regnskov Tropical Zoo 
Robert Lacy 
Rotterdam Zoo 
Royal Zoological Society of Antwerp 
Royal Zoological Society of Scotland 
Royal Zoological Society of South    
Australia 
Saitama Children’s Zoo 
San Antonio Zoo 
San Francisco Zoo 
Sedgwick County Zoo 
Taipei Zoo 
Thrigby Hall Wildlife Gardens 
Tiergarten Schonbrunner 
Twycross Zoo 
Union of German Zoo Directors  
Wassenaar Wildlife Breeding Centre 
Wilhelma Zoological Garden 
Woodland Park Zoo 
Zoo Frankfurt 
Zoologischer Garten Koln 
Zoologischer Garten Zurich 
 
Stewards ($500-$999) 
Aalborg Zoo 
Academy for Protection of Primates 
Alameda Park Zoo  
Arizona-Sonora Desert Museum 
Banham Zoo & Sanctuary 
BioSolutions Division of SAIC 
Cotswold Wildlife Park 
Dutch Federation of Zoological Gardens 
Fairchild Tropical Garden 
FOTA Wildlife Park 
Givskud Zoo 
Granby Zoo 
Heidelberg Zoo 
Knoxville Zoo 
Knuthenborg Park 
Little Rock Zoo 
Lowry Park  
National Aviary in Pittsburgh 
NaturZoo Rheine 
Odense Zoo 
Oregon Zoo 
Ouwehands Dierenpark 
Palm Beach Zoo at Dreher Park 
Perth Zoo 
 
 
 
Potter Park Zoo  
Riverbanks Zoological Park 
Staten Island Zoo 
Wellington Zoo 
Welsh Mountain Zoo 
Wildlife World Zoo, Inc. 
John S. Williams 
Zoologischer Garten Rostock 
 
Curators ($250-$499) 
Bramble Park Zoo 
Emporia Zoo 
Lee Richardson Zoo 
Montgomery Zoo 
Racine Zoological Society 
Roger Williams Park Zoo 
Rosamond Gifford Zoo 
Suzanne Gendron 
The Animal Park-Gulf Breeze 
Tokyo Zoological Park Society  
Topeka Zoo, Friends of 
Zoo Madrid 
 
Sponsors ($50-$249) 
African Safari-France 
Alex Rübel 
Alice Springs Desert Park  
American Loriinae Conservancy 
Bighorn Institute 
Brandywine Zoo 
Chahinkapa Zoo 
Darmstadt Zoo 
Folsom Children's Zoo  
Jardin aux Oiseaux  
Mabel Lam 
Lisbon Zoo 
Miller Park Zoo 
National Birds of Prey Centre 
Steven J. Olson 
Parc Zoologique de Thoiry  
Plzen Zoo 
Rolling Hills Zoo 
Safari Parc de Peaugres  
Steinhart Aquarium 
Stiftung Natur-und Artenschutz in den   
Tropen 
Teruko Shimizu 
Tautphaus Park Zoo  
Touro Parc-France 
  
Supporters ($15-$49) 
Judy Steenberg 
Oglebay's Good Children's Zoo 
Osnabruck Zoo 
Plzen Zoo 
Wuppertal Zoo 
 
 
 
Thank You!
January 2005 


 
VORTEX Version 9.50 User’s Manual 
 
 
i 
Contents 
 
Contents 
Chapter 1. Introduction ..................................................................1 
 
What’s New in VORTEX Version 9? ...........................................1 
 
What’s New in Version 9.50?..................................................2 
 
How to Use This Manual .........................................................3 
 
A Note about Regional Windows Settings..............................4 
 
VORTEX Technical Support .......................................................4 
 
A Note about Cost...................................................................5 
 
Chapter 2. Getting Started with VORTEX..........................................6 
 
Installation .............................................................................6 
 
Running VORTEX.......................................................................7 
 
Size Limitations on VORTEX Analyses.......................................7 
 
Getting Around in VORTEX........................................................9 
 
A Quick Tour of VORTEX..........................................................10 
 
Chapter 3. Creating a Project: ......................................................22 
 
Data Input ............................................................................22 
 
Creating a Project.................................................................22 
 
Getting Help when Entering Input Data...............................24 


VORTEX Version 9.50 User’s Manual 
ii 
Contents 
 
Documenting Your Input with Notes....................................26 
 
Creating a Scenario ..............................................................27 
 
 
Scenario Settings........................................................................ 27 
 
 
Species Description .................................................................... 29 
 
 
Labels and State Variables ......................................................... 38 
 
 
Dispersal Among Populations..................................................... 41 
 
 
Reproductive System.................................................................. 44 
 
 
Reproductive Rates .................................................................... 49 
 
 
Mortality   .................................................................................. 53 
 
 
Catastrophes .............................................................................. 54 
 
 
Mate Monopolization .................................................................. 57 
 
 
Initial Population Size ................................................................ 58 
 
 
Carrying Capacity ....................................................................... 59 
 
 
Harvest     .................................................................................. 62 
 
 
Supplementation ........................................................................ 63 
 
 
Genetic Management.................................................................. 64 
 
Saving your Input and Running the Simulation ...................67 
 
Adding and Deleting Scenarios.............................................69 
 
 
Adding Scenarios to Your Project............................................... 70 
 
 
Deleting Scenarios from Your Project ........................................ 71 
 
 
Reordering scenarios.................................................................. 72 


 
VORTEX Version 9.50 User’s Manual 
 
 
iii 
Contents 
Chapter 4. Viewing Model Results: Text, Tabular, and Graphical 
Output ..................................................................73 
 
Text Output...........................................................................73 
 
 
Input Summary .......................................................................... 73 
 
 
Deterministic Calculations.......................................................... 74 
 
 
Output Summary ........................................................................ 77 
 
 
Other Output .............................................................................. 79 
 
Graphs and Tables ................................................................80 
 
 
Data Graphs................................................................................ 83 
 
Project Report ......................................................................85 
 
Access to Other Stored Output .............................................86 
Chapter 5. Sensitivity Testing.......................................................87 
Chapter 6. Using Functions in VORTEX ...........................................95 
 
Introduction..........................................................................95 
 
Specification of Demographic Rates as Functions................96 
 
Using Random Numbers in Functions.................................100 
 
Notes Regarding Function Syntax and Use ........................100 
 
Using Functions to Examine Genetic Evolution ..................102 
 
Examples of Rate Functions ...............................................102 
Appendix I. An Overview of Population Viability Analysis Using 
VORTEX.................................................................111 
Appendix II. Literature Cited......................................................133 


VORTEX Version 9.50 User’s Manual 
iv 
Contents 
Appendix III. VORTEX Bibliography..............................................139 
Appendix IV. Reprints.................................................................149 
 
Lacy, R.C. 2000. Structure of the VORTEX simulation model 
for population viability analysis. Ecological 
Bulletins 48:191-203.  
 
Lacy, R.C. 2000. Considering threats to the viability of small 
populations using individual-based models. 
Ecological Bulletins 48:39-51. 
 


 
VORTEX Version 9.50 User’s Manual 
 
1 
Chapter 1 
Introduction 
Chapter 
 
Introduction 
 
 
VORTEX is an individual-based simulation model for population 
viability analysis (PVA). This program will help you understand 
the effects of deterministic forces as well as demographic, 
environmental, and genetic stochastic (or random) events on the 
dynamics of wildlife populations. VORTEX models population 
dynamics as discrete, sequential events (e.g., births, deaths, catastrophes, etc.) that occur according to 
defined probabilities. The probabilities of events are modeled as constants or as random variables that 
follow specified distributions. Since the growth or decline of a simulated population is strongly 
influenced by these random events, separate model iterations or “runs” using the exact same input 
parameters will produce different results. Consequently, the model is repeated many times to reveal the 
distribution of fates that the population might experience under a given set of input conditions. 
 
VORTEX simulates a population by stepping through a series of events that describe the typical life cycle 
of sexually reproducing, diploid organisms. The program was written originally to model mammalian and 
avian populations, but its capabilities have improved so that it can now be used for modeling some 
reptiles and amphibians and perhaps could be used for fish, invertebrates, or even plants—if they have 
relatively low fecundity or could be modeled as if they do.  
 
The purpose of this manual is to provide you with complete instructions on how to install and use 
VORTEX. It is not intended as a primer on population biology; you must be conversant with this discipline 
to use the program appropriately and effectively. In addition, you must know something about the biology 
of the species that you intend to model. You should gather as much information as possible in order for 
VORTEX simulations to be meaningful. The old computer adage of “garbage in, garbage out” is aptly 
applied to population viability analysis, and PVA using VORTEX is certainly no exception. Having said 
this, it is important to recognize that many of the questions VORTEX asks as you construct your population 
model cannot be answered simply because the data do not exist. The only recourse that you will have is to 
enter your best guess. Oftentimes, your best guess is not yours alone; most (if not all) population viability 
analyses have succeeded through the efforts of many. Two or more heads are usually better than one 
when you find yourself faced with a VORTEX question with no known answer. Further information about 
VORTEX and the structure of the model is provided in publications reprinted as appendices to this manual. 
 
What’s New in VORTEX Version 9? 
 
The biggest change from prior versions of VORTEX is that the program is now a Windows application. 
Although the user interface is now totally new, experienced VORTEX users will quickly recognize that the 
content of the program (the input variables, the information output, etc.) is still very much like that of the 
old MS-DOS versions of VORTEX. In fact, unless you invoke one of the few new features of the overall 
model, results generated by the Windows version should match (except for stochastic uncertainty) the 
results produced by the earlier DOS versions.  
1 


VORTEX Version 9.50 User’s Manual 
2 
Chapter 1 
Introduction 
You cannot directly import input files from prior (DOS) versions of VORTEX into version 9. However, for 
an experienced VORTEX user, it usually takes only a few minutes to re-enter the input values from a prior 
analysis. Attempts will be made to make future updated versions of VORTEX capable of importing projects 
from all previous Windows versions of the program (version 9.0 and higher). You should not assume that 
projects from a more recent version can be read by an older version of VORTEX, and any time that you 
open a project into a newer version of the program, you should double check all input screens to confirm 
that data were transferred correctly.  
 
The user interface for entering input values, running simulations, seeing tabular and graphical 
representations of output, and obtaining help are clearly very different in the Windows VORTEX than in the 
earlier DOS versions. The easiest way to get a feel for these differences is to open the program and 
explore it. A “Quick Tour” of the new program is provided in Chapter 2, and new users are encouraged to 
use it to become more familiar with VORTEX version 9. 
 
In addition to the switch to a Windows interface, there have been a few upgrades to the underlying 
population biology model available in VORTEX. The most significant one (and the one that would be most 
noticeable to users) is the availability now of “Individual State” variables. These optional variables allow 
you to create descriptors of states or characteristics of individuals in the populations. These states can be 
anything you want them to be – for example, dominance status, body condition, location on the landscape, 
or territory quality. If you specify Individual State variables, then you must define how they are initially 
determined for each individual at the outset of the simulation and when individuals are born, and how an 
individual’s state can change across years. Once defined, these variables can be used as modifiers of any 
of the demographic rates – such as probability of breeding, litter size, mortality, susceptibility to 
catastrophes, and dispersal. Using this feature of the VORTEX model, you can create very complex and 
detailed models of population dynamics. (For example, breeding could be function of the dominance 
status of individuals, which could in turn be determined by maternal dominance status and a random 
component.) However, we will not hide the fact that appropriate and wise use of Individual State 
variables can be very difficult, and we strongly caution new VORTEX users to stay away from creating 
such complex models.  
 
What’s New in Version 9.50? 
 
Several new features have been added during the incremental upgrades leading from version 9.0 to 
version 9.50. In addition, the layout and text on some user screen have been modified slightly. The 
primary changes in version 9.50 (partly implemented in some prior versions) are: 
¾ The program now has the option of switching all text on input screens to Spanish (or back to 
English). The output files and the Help text are still all in English, but the input screens and hint 
texts can be changed to Spanish in the Vortex>Set Language menu. Translations to other languages 
may be possible in the future, if anyone volunteers to provide the translations. (If you are willing to 
do so, please send an email message to help@vortex9.org.)  
¾ Within the input section for Labels and State Variables, there is now an option to link VORTEX to 
SPATIAL, a program created by JP Pollak of Visualbiosystems(www.visualbiosystems.com) for 
modeling the movements of animals on complex landscapes. When VORTEX and SPATIAL are so 
linked as a “meta-model”, SPATIAL can simulate the movements of animals and pass data to VORTEX 
dynamically to specify the locations and, optionally, spatial characteristics such as habitat quality 
indices for the current location of each animal. SPATIAL is still undergoing development and testing. 
Contact JP for further information about the program. To use VORTEX with SPATIAL or with the 
epidemiological modeling program OUTBREAK (also developed by JP Pollak, in collaboration with 
the CBSG), you need to have installed on your computer the XML libraries provided (for free) by 


 
VORTEX Version 9.50 User’s Manual 
 
3 
Chapter 1 
Introduction 
Microsoft. The XML installation files are included with the VORTEX installation (see installation 
instructions below).  
¾ A new (“Genetic Management”) section of input provides users with the option of specifying that 
the populations are managed genetically. These options would normally be used to test the viability 
of captive or otherwise intensively managed populations, but the options may also be used to model 
a system in which the individuals select their mates in specific ways. In this new input section are 
also some options for outputting more detailed genetic results. A few of the options included now 
under Genetic Management had previously been offered as Special Options of Project Settings.  
¾ An automated Sensitivity Testing module has been added. This “ST” feature can simplify the 
process of creating multiple new scenarios in which one or more input parameters are varied from a 
baseline scenario. In addition, this module provides several ways to tabulate and graph comparative 
results from such sensitivity tests. The ST module is fairly complex, and will likely be changed and 
enhanced in the next several versions of VORTEX.  
¾ When running a simulation, the user now has the option of resuming a prior simulation, adding 
more iterations to those previously run. This feature makes it easier to break a very long analysis 
(perhaps involving 1000 or more iterations of a big analysis) into several separate sessions of 
computer time. 
 
How to Use This Manual 
 
By following the detailed instructions provided in the VORTEX User’s Manual, you should be able to 
construct surprisingly complex models of stochastic growth dynamics of wildlife populations. In addition 
to this instruction, the User’s Manual provides you with supplementary information designed to help you 
get the most out of VORTEX and to see how it and related software packages are used in practical 
applications of conservation biology.  
 
¾ Chapter 2, GETTING STARTED WITH VORTEX, gives you information on the program’s modest 
system requirements and shows you how to install, run, and close the program. 
¾ Chapter 3, CREATING A PROJECT: DATA INPUT, provides a wealth of information on the types of 
biological data necessary for developing a VORTEX population model and the mechanics of entering 
data into the program. 
¾ Chapter 4, VIEWING MODEL RESULTS, describes how to view your model results, in text, tabular 
and graphical form and how to work with output data files to assist in effective data analysis. 
¾ Chapter 5, SENSITIVITY TESTING, describes the use of the new automated sensitivity testing module 
for rapidly creating and analyzing scenarios that test alternate values for input parameters. 
¾ Chapter 6, USING FUNCTIONS IN VORTEX, presents a detailed description of how to use this major, 
but complex, feature. 
¾ Appendix I, AN OVERVIEW OF POPULATION VIABILITY ANALYSIS USING VORTEX, gives a brief 
introduction to the principles of small population biology and describes in more general terms the 
use of population viability analysis to assist with wildlife management and endangered species 
recovery. 
¾ Appendix II, LITERATURE CITED, provides a complete listing of the scientific literature referenced 
throughout this User’s Manual. 
¾ Appendix III, VORTEX BIBLIOGRAPHY, includes what we hope is a reasonably complete list of 
references to papers that discuss VORTEX as a tool for population viability analysis, and to those 
specific examples of the use of VORTEX in PVAs across a diverse taxonomic range. Authors 


VORTEX Version 9.50 User’s Manual 
4 
Chapter 1 
Introduction 
wishing to have their publications listed in future editions of this manual should email the citations 
to help@vortex9.org. 
¾ Appendix IV, REPRINTS, provides copies of two papers that describe in detail the structure of the 
VORTEX model and some of the concepts behind the model.  
 
 
Throughout the text you will find various aids that will enhance your overall use of VORTEX: 
 
Brief explanatory notes that will help you remember important points, clarify some commonly-used 
terms, etc. 
 
Text boxes that will provide additional information on general concepts in 
population biology and genetics, statistics, and simulation modeling. 
 
 
Case Studies that show you real examples of how data have been used to develop 
VORTEX simulation models. These case studies are gleaned from the many Population 
and Habitat Viability Assessment (PHVA) workshops conducted by CBSG over the past 
decade. 
 
 
A Note about Regional Windows Settings 
 
Although we cannot guarantee that VORTEX will work correctly with all possible configurations of MS 
Windows, we believe that it will adapt appropriately to most Regional Settings of date, time, and numeric 
formats. Throughout this manual, screen displays are shown from a system configured with the American 
English regional settings. For example, the ‘.’ is used as the decimal delimiter (so that the number three 
would be shown as 3.0). If your operating system is configured to use the ‘,’ as the decimal delimiter, 
then you would use that format throughout VORTEX for input and output (so that the number three would 
be shown as 3,0). Do not use any delimiter between thousands (e.g., thirty thousand would be 30000, 
not 30,000, nor 30 000, nor 30.000). VORTEX will try to automatically convert input and output files 
to the data format specified by your Windows Regional Settings. 
 
VORTEX Technical Support 
 
If you are having trouble using VORTEX and want additional information, there are a number of resources 
available to you. Be advised, however, that CBSG is unable to provide the kind of technical support you 
have come to expect (but rarely receive!) from large software companies. In this context, the phrase “you 
get what you pay for” is particularly appropriate. VORTEX is provided on the Internet free of charge 
because of our commitment to promoting the use of science in the service of biodiversity conservation. 
Significant resources have been provided over the years by the Chicago Zoological Society and the CBSG 
to support the development and continual improvement of VORTEX. Neither organization recovers these 
costs of development, nor receives any funding to provide ongoing support to VORTEX users.  
 
Nevertheless, we are committed to doing everything we can to help you get the most out of your VORTEX 
modeling experience. Towards this end, we suggest the following support options: 
 
¾ This User’s Manual. We hope that we have provided you with all of the information necessary to 
navigate your way through the program.  


 
VORTEX Version 9.50 User’s Manual 
 
5 
Chapter 1 
Introduction 
¾ Tooltips and Input Prompts. Most icons, commands, menus, and input boxes have tooltips that pop 
up with explanatory messages when the cursor is paused over them. In addition, during input, 
prompts will appear at the bottom of the window when the user clicks on a data entry box.  
¾ On-screen Help. Chapters 1-6 of this manual are provided in the Help menu of the program. 
¾ The VORTEX Listserve. To help VORTEX users in their use of the program for PVA, a VORTEX Users 
email discussion group (Listserve) has been established. The VORTEX Listserve facilitates the 
exchange of ideas, questions, answers, and suggestions among the many users of VORTEX. The 
listserve also provides a medium for announcing updates, bug fixes, and suggestions provided by 
CBSG or by the program’s developer. To get information about the listserve, or to subscribe, go to 
https://listhost.uchicago.edu/mailman/listinfo/vortex. Because there is no registration of VORTEX 
users, the listserve is only way we can assure that users will hear about updates, bug fixes, and 
other announcements. 
¾ VORTEX on the Web. Explore the VORTEX  home page at http://www.vortex9.org/vortex.html  
to download updated programs or documentation files, to report program bugs, or to obtain other 
information pertinent to the effective use of VORTEX. 
¾ Contact the CBSG Office. As a last resort, if you are unable to solve your problem by the means 
suggested above, you can reach the CBSG Office directly to get help. Our contact information is: 
Telephone: 1-952-997-9800; Fax: 1-952-997-9803; E-mail: office@cbsg.org. 
  
We urge you to read the entire User's Manual not only to better your understanding of VORTEX, but also 
to enhance your appreciation of the perils facing small populations of threatened wildlife. For a more in-
depth treatment of population viability analysis and models for use in risk assessment, we recommend 
Starfield and Bleloch (1986) and Burgman et al. (1993) as excellent introductions to these topics. 
 
A Note about Cost 
 
Vortex is provided free of charge because of the commitment of the Chicago Zoological Society to 
making it widely available to further biodiversity conservation. Similarly, the manual, developed by the 
CBSG, is provided for downloading because the CBSG cares about saving species and their habitats. 
However, the initial development and continuing improvement of the software and manual do represent a 
significant commitment by these conservation organizations. The rate at which improvements can be 
made is determined by the resources available to support that work.  
 
If your budget allows it, please consider making a donation to support the further development of Vortex.  
If you find the software to be especially valuable to you, consider donating perhaps US$100 (a wild guess 
about the investment of resources per user that have gone into Vortex), or more or less as you feel is 
appropriate, to the Chicago Zoological Society. If you find the manual to be especially helpful, consider 
donating to the CBSG. As a side benefit to US tax-payers, donations to either the Chicago Zoological 
Society or the CBSG are tax-deductible. Donations to the Chicago Zoological Society should be as a 
check written to the Chicago Zoological Society, sent to “Vortex donation, Department of Conservation 
Biology, Brookfield Zoo, Brookfield, IL 60513 USA". Donations to the CBSG should be sent to "Vortex 
donation, CBSG, 12101 Johnny Cake Ridge Road, Apple Valley, MN 55124, USA". 


VORTEX Version 9.50 User’s Manual 
6 
Chapter 2 
Getting Started with VORTEX 
Chapter 
 
Getting Started 
with VORTEX 
 
 
System Requirements 
 
VORTEX  version 9 was developed as a C++ program (for the simulation code) presented within an 
interface developed in MS Visual Basic. To our knowledge, it will install and run properly on computers 
with Pentium (or newer) processors running Win95, Win98, WinXP, Win2000, or WinNT operating 
systems. We believe that VORTEX will work properly with a diversity of Windows Regional settings – for 
example, it can use various common European data formats. However, we cannot guarantee that it will 
work with all system configurations. The default user interface of VORTEX is presented in American 
English, but a menu option allows the user to toggle the text in screen displays to Spanish. At a future 
time, versions in German, French, or other languages may be made available. 
 
For many analyses, VORTEX will use much of your computer’s system resources. Faster results and better 
performance will be obtained if you do not try to run other large applications (such as MS Word, Excel, 
or Outlook) at the same time that VORTEX is running. The program may not run properly with less than 
128 MB of system memory (RAM), and even more RAM will be required if you want to run other 
applications concurrently. In addition, the size of the populations that can be analyzed will be determined 
by the available RAM. For example, simulation of a population of 5000 living animals can require up to 
about 200 MB of RAM for storage of inbreeding calculations. The program requires much more memory 
if you include inbreeding depression in your analyses, so omitting inbreeding depression (see Chapter 3) 
will allow analysis of larger populations and will run much faster.  
 
Installation 
 
To install VORTEX from the CD: 
Place the VORTEX installation CD into the appropriate disk drive, and then run the SETUP 
program. (Either double-click on SETUP from Windows Explorer, or go to START>RUN, and then 
enter D:\SETUP.EXE, in which D: is your CD drive.)  
 
To install VORTEX from the Internet: 
Go to http://www.vortex9.org/vortex.html and download the current version of the installation 
program. Save this downloaded file to any temporary directory of your hard disk or to your 
desktop. Double-click on the downloaded file to unzip the installation package files. Unzip them 
to the directory where you saved the downloaded file, or to any directory of your choosing, other 
than the directory to where you wish to install VORTEX. Run the SETUP program. (Either double-
2 


 
VORTEX Version 9.50 User’s Manual 
 
7 
Chapter 2 
Getting Started with VORTEX 
click on SETUP from Windows Explorer, or go to START>RUN, and then enter 
C:\TEMP\SETUP.EXE, in which C:\temp is the drive and directory where you placed the installation 
files.) 
 
You may want to put a short-cut to VORTEX on your Desktop.  
 
VORTEX is copyrighted but not copy-protected. You can make as many copies as you wish, and you may 
give copies of the program to others free of charge. You may not sell the program or any components of 
it, or otherwise represent it as your personal property.  
 
If you plan on running VORTEX as a linked meta-model with either SPATIAL (a simulation of animal 
movements on the landscape) or OUTBREAK (an epidemiological simulation of infectious disease), you 
will need also to have installed the Microsoft XML library. If you have not previously installed XML 
capabilities on your computer (or you are not sure if you have), run the program MSXML.MSI that is 
available (as freeware) from the Microsoft web site or from www.vortex9.org/msxml.msi.  
Running VORTEX 
 
Start VORTEX by double-clicking on a short-cut icon, or by double-clicking on the VORTEX program itself. 
To exit the VORTEX program, just click on the Close button (marked by an ×) in the top right corner of the 
program window. Before closing, the program will always prompt you to determine if you wish to save 
any open projects.  
 
Size Limitations on VORTEX Analyses 
 
VORTEX allocates computer memory as it needs it, depending on the characteristics of the population or 
metapopulation you are modeling. VORTEX will make optimal use of all available memory to carry out the 
simulations, but the available RAM on your computer may limit the size of analysis you can complete. 
However, there are also some absolute limits to how large or complex a simulation can be. These limits 
are listed below. 
¾ Number of iterations 
 
10000 
¾ Duration of simulation  
10000 years 
¾ Number of populations  
50 
¾ Types of catastrophes 
 
25 
¾ Maximum age  
 
250 years 
¾ Maximum litter size 
 
50* 
¾ Initial population size 
 
30000 individuals 
¾ Carrying capacity 
 
60000 individuals 
*Only if specifying an exact distribution; maximum litter size is not constrained if you use a normal distribution. 
Some combinations of parameters can require large amounts of memory. For example, if you are 
including inbreeding depression in your simulation, and have chosen to model it as only partially due to 
the presence of lethal alleles, more than 50 megabytes of memory may be required to analyze a 
population that reaches 5000 living animals. In these cases, it is possible that VORTEX will abort an 
analysis if there is insufficient memory available. Even if the program does not abort, it may run 
exceedingly slowly as each individual and its pedigree is tracked throughout its lifetime. If you have 
frequent problems with aborted or slow analyses, consider taking one or more of the following steps: 
¾ Change the mechanism by which inbreeding depression is modeled. The program will run much 
faster if the population’s genetic load is due entirely to lethal as opposed to detrimental alleles. 


VORTEX Version 9.50 User’s Manual 
8 
Chapter 2 
Getting Started with VORTEX 
¾ Construct a simpler general model. Often a large population (or metapopulation) may exist, but 
the real concern may be whether smaller fragments are at risk of local extirpation. VORTEX will 
simulate small populations much more rapidly than large populations or constellations of patches 
within a metapopulation. If local patches do not exchange migrants, analyze them separately 
rather than as parts of a larger, more complex metapopulation. 
¾ Think about using a different PVA software package. If VORTEX is running so slowly as to cause 
you much grief, the types of populations you are analyzing are probably so large that the kinds of 
random forces modeled explicitly by VORTEX —demographic and environmental stochasticity, 
inbreeding, and genetic drift—are likely to be irrelevant to the population growth dynamics. In 
these cases, it may be more appropriate to use a population-based model such as one of the 
packages in the RAMAS family of software (these are produced and distributed by Applied 
Biomathematics, Setauket, NY), or to use analytical methods (e.g., life-table analysis) that 
exclude most or all stochastic factors entirely. 
 
Box A: Is VORTEX the Best PVA Model for Your Analysis? 
 
Different PVA models have different strengths and weaknesses with respect to what kinds of life 
histories they can model, what range of processes can be examined, what aspects of population 
dynamics are modeled well, and how easy they are to use for different analyses. Below is a list of 
some considerations for evaluating whether VORTEX is more or less appropriate for your analysis. 
While they are certainly not hard and fast rules, they should help you make informed decisions about 
how to best conduct your analysis. 
 
 
 
 
 
 
High fecundity 
Low fecundity 
Short lifespan 
Long lifespan 
Polyploid 
Diploid 
Genetic effects of little interest 
Changes in genetic variation of interest 
Local population (N) > 500 
Local population (N) < 500 
> 20 populations modeled 
< 20 populations modeled 
Demographic rates not estimable 
Age-specific fecundity and survival rates estimable 
(only population growth trajectories known) 
Stage- or size-dependent demography 
Age-dependent fecundity and survival rates 
Demographic rate fluctuations not estimable 
Fluctuations in rates can be estimated 
No catastrophic events of interest 
Catastrophic events modeled 
Only polygamous breeding 
Polygamous or monogamous breeding 
Random breeding 
Some adults excluded from breeding 
 
Non-random distribution of fecundity 
Population starts at stable age distribution 
Starting population not at stable age distribution 
Constant sex ratio 
Unequal sex ratio 
No trends in habitat expected 
Trends projected in habitat quality or area 
No manipulation of animal numbers 
Managed removal, supplementation, or translocation 
Fish, amphibian, invertebrate, or plant 
Bird, mammal, or reptile 
You have lots of money 
You have lots of time 
(for buying software) 
(for running analyses and summarizing results) 
 
VORTEX may be less appropriate or 
may not be needed 
VORTEX is more appropriate 
and may be necessary


 
VORTEX Version 9.50 User’s Manual 
 
9 
Chapter 2 
Getting Started with VORTEX 
Getting Around in VORTEX 
 
Your work in VORTEX will be structured as Projects and Scenarios. A Project will contain all your input, 
output, and notes about a case that you are exploring. Often, a Project will contain all the analyses about a 
given species or population. You could split your analyses of a species among multiple Projects, but that 
would preclude you from easily copying input, results, or settings among the separate Projects containing 
your work. On the other hand, there is no advantage to combining work on different species or cases into 
one Project, and it may be more useful and less confusing to keep distinct PVAs in separate VORTEX 
Projects. It is probably a good idea to specify a new directory for storing each Project (and this is the 
default in VORTEX), although you can store all your work in one directory if you wish. 
 
Each Scenario within a Project contains a discrete set of input values and (if it has been run) output. Thus, 
for a given species (Project) you may decide to test several or even many different Scenarios, each of 
which would have an alternative set of input values, representing an alternative view of the population. 
For example, different Scenarios may represent various plausible input values to be explored during 
sensitivity testing, or may represent alternative management options that might be applied to a population. 
 
The VORTEX interface has separate screens (windows) or tabs for Project Settings, Simulation Input, Text 
Output, Graphs and Tables, and a Project Report. Each of these are specific to an open Project, and you 
can toggle among the Scenarios of a Project within the input and output screens. You can open 
concurrently multiple VORTEX Projects within a VORTEX session, although there may only rarely be cases 
in which it is useful to have more than one Project open at the same time.  
 
 
An important caution: It is almost inevitable that VORTEX contains some bugs, and it may be that 
you will make some mistakes while working with VORTEX. Thus, it is possible that after you spend 
hours working on a VORTEX Project, the program will suddenly crash. It is also possible that you 
will accidentally change a very useful analysis into something that is worthless. It is strongly recommended that you 
periodically save your work, and even save it under a new name in a new directory (see below). Hard disk space is 
cheap – use it! 
 


VORTEX Version 9.50 User’s Manual 
10 Chapter 2 
Getting Started with VORTEX 
A Quick Tour of VORTEX 
 
The first screen you will see when you begin a new VORTEX session is shown in Figure 1.  
 
 
Figure 1. The Vortex opening screen 
 
After admiring this artistic representation of the extinction vortex, and appreciating the fact that the 
Chicago Zoological Society devoted a lot of resources to develop VORTEX for your use, click on the 
“Close graphic …” message to enter the program. 
 
The next screen, shown in Figure 2, asks what Project you wish to open. (Note: in Figure 2, and many 
subsequent figures, the image shown is just the sub-window that is relevant to the point being made.) 
Select the Open Project tab, so that we can use an existing sample Project. A number of sample projects 
are copied into the Projects subdirectory when you install VORTEX. More sample projects will be made 
available at http://www.vortex9.org/vortex.html, and we encourage users to contribute their project files 
to this site so that others may explore those data sets.  
 


 
VORTEX Version 9.50 User’s Manual 
 
11 
Chapter 2 
Getting Started with VORTEX 
 
Figure 2. The dialog box for starting a Project. 
Figure 3 shows the dialog box for opening an existing Project. This screen may look a little different on 
your computer, depending on where you installed the VORTEX program. Navigate to the \ZPG directory 
and then select the ZPG Project by double-clicking on the ZPG.vpj file, or single-clicking on it and then 
selecting OK. Note that windows in VORTEX can usually be resized or moved with the cursor. 
 
 
Figure 3. The dialog box for opening an existing Project. 
The ZPG Project does not represent any particular species. It has a set of input values that define a 
population that would have an expected long-term zero population growth (r = 0.0), based on the mean 
birth and death rates as modified by occasional catastrophes. This projection of zero population growth is 
dependent upon an assumption that stochastic processes – such as demographic stochasticity, temporary 


VORTEX Version 9.50 User’s Manual 
12 Chapter 2 
Getting Started with VORTEX 
mate limitation, inbreeding, and annual fluctuations (“environmental variation”) – do not reduce mean 
population performance. The population size in this case, however, is low enough that these stochastic 
processes are important impacts on the population, causing it to be unstable, often decline, and be highly 
vulnerable to extinction (as we will see). The ZPG Project has the same input values as the default values 
in the earlier DOS versions of VORTEX. 
 
When you open a Project, VORTEX opens a screen that shows the Project Settings interface and the tabs 
for the other screens – Simulation Input, Text Output, Graphs and Tables, and Project Report (Figure 4). 
On the Project Settings screen, you can specify a different Project name, enter the names of any 
collaborators, and add any Project Notes text that you wish to describe your Project. It is wise to take the 
time to document your work by typing Project Notes and, on a screen you will see later, on Input Notes. 
At the time you are working, it may be seem obvious what decisions you were making when you created 
your Project. However, months later it may be very difficult for you (or others) to recall what led you to 
design the Project as you did. If you want ever to go back to a Project, take the time now to document 
your work within the VORTEX Project (see Chapter 3 for more information on entering Input Notes). 
 
 
Figure 4. The Project window. 


 
VORTEX Version 9.50 User’s Manual 
 
13 
Chapter 2 
Getting Started with VORTEX 
Get into the habit of adding Notes to your Projects to document what you are doing. You will be 
glad that you did when you later need to tell others what you did in your analyses. 
 
Also on the Project Settings screen is a button that will send the Project Settings information to your 
Project Report. Your Report is a note pad utility (much like MS Notepad) that lets you build 
documentation of your Project. We will take a look at the Project Report soon; for now, click on the 
“Send all to Report” button to capture the settings information in your Report.  
 
Send information to your Report whenever you think that you may want it documented. It is 
easy to delete parts of the Report, but it is hard later to see something that you never sent ! 
The last item on the Project Settings screen is a Special Options button. These options are ones that most 
users will never need to use, so we won’t look at them now. Click now on the Simulation Input tab, to 
take you to the screen shown in Figure 5. 
 
 
Figure 5. The Simulation Input window. 


VORTEX Version 9.50 User’s Manual 
14 Chapter 2 
Getting Started with VORTEX 
Simulation Input is arranged as 14 screens that each request values for a section of input parameters 
(“Scenario Settings”, “Species Description”, etc.). Clicking on one of the section labels in the list on the 
left side of the screen takes you to that section of input. Within a section, it does not matter what order 
you enter values, and the input sections can be accessed in any order you wish. However, it makes sense 
to enter values in the order they appear in the program, so that you don’t forget to specify some critical 
value. In addition, some input sections will use values already entered from prior sections to compute 
useful values (such as the stable age distribution) during input. Notice that one section label, “Dispersal 
Rates”, is greyed out and disabled. That is because the current Scenario has only one population, so there 
can be no dispersal among populations. Similarly, some other sections and individual input boxes will 
become disabled if values you have specified would make that section meaningless.  
 
Take a quick look at the data input boxes on the Scenario Settings screen. As you click on any box, a 
message will be displayed at the bottom of your screen with hints about what you need to enter into that 
box. Now click on the “Species Description” label on the left to take you to that input section (Figure 6). 
Note again that some input boxes are disabled, because they pertain only to metapopulation models.  
 
Figure 6. Species Description input section. 


 
VORTEX Version 9.50 User’s Manual 
 
15 
Chapter 2 
Getting Started with VORTEX 
Step through each of the input sections, looking at the input values that are requested by VORTEX  and the 
values that were entered for this ZPG Scenario. In some sections, you may need to use vertical or 
horizontal scroll bars to see all of the data entered. You can also make the input screens larger by clicking 
and dragging the corner of the window. Go now to the Catastrophes section (Figure 7).  
 
 
Figure 7. Catastrophes input section. 
 
Because it was specified in the Species Description that the model should contain two types of 
catastrophes, the Catastrophes section has buttons to toggle between these two types. Hit the button to go 
to input for the second catastrophe (“Forest Fire”). In this particular Scenario, the two types of 
catastrophes have the same input values, so it is not obvious that you are moving between the two types 
(but you are).  
 
When you are done looking through all the input sections, click on the Run icon (the green triangle on the 
icon bar) to open up the Run Simulation dialog box shown in Figure 8. Check the box to select Scenario 
ZPG1, and then click Run!  


VORTEX Version 9.50 User’s Manual 
16 Chapter 2 
Getting Started with VORTEX 
 
Figure 8. Run Simulation window. 
Now, sit back and watch the simulation work. The lines on the screen (Figure 9) show the changing 
population size over 100 years for 100 different iterations for the ZPG1 Scenario. When the simulation is 
complete (which should take only a few seconds with this small population), the VORTEX Simulation 
display window will show a few summary statistics along the top. When you are done viewing this 
graphical display of the simulations, click on its close icon (×)  in the upper right corner. 
 
 
Figure 9. VORTEX Simulation display window. 


 
VORTEX Version 9.50 User’s Manual 
 
17 
Chapter 2 
Getting Started with VORTEX 
The VORTEX Simulation window cannot be resized, and toggling to another window during the 
VORTEX simulations may leave you with a blank VORTEX Simulation window when you return to it. 
It is best not to move off of this window while the simulations are running. When the simulations 
are complete, close the window before doing anything else.  
 
The results of the simulation you just completed are now stored with your Project on the computer. There 
are two modes in which you can view the results – “Text Output” and “Graphs and Tables”.  Go to Text 
Output by clicking on its tab. Within the Text Output section are four tabbed subsections – Input 
Summary, Deterministic Calculations, Output Summary, and Other Output (Figure 10). 
 
 
Figure 10. The Output Summary section of Text Output 
The Input Summary section shows a text listing of all the input values used in this Scenario. Deterministic 
Calculations show a text summary of the deterministic population growth that would be projected from 
the specified mean demographic rates, if stochastic processes were not acting on the population. This 
section also shows a simple graph of the deterministic population trajectory. The Output Summary section 
gives a text description of the status of the population at each year of the simulations as well as summary 


VORTEX Version 9.50 User’s Manual 
18 Chapter 2 
Getting Started with VORTEX 
statistics for the Scenario. Other Output provides some tables with basic summary statistics for the 
Scenario and for each iteration. Note that the sections of Text Output provide dropdown lists to allow you 
to move among Scenarios and Populations. Buttons are also provided to allow you to save these texts to 
simple text files, to print the text summaries, or to send the summaries to the Project Report. Send the 
Output Summary to the Report now, so that we can view and edit it later as part of our Project Report.  
 
All of the information shown on Text Output  screens is stored automatically in text files that are 
placed into your project directory. While you can access and edit these files (using, for example, 
MS Notepad or Word), it is better to first save the text to your own files, so that they are safely 
stored under names that you specify and will not be overwritten if you run the simulation again.  
 
Click now on the Graphs and Tables tab (Figure 11). If one or more Scenarios that have not yet been run, 
the list in the lower left of the screen will list those Scenario names preceded with “N.A.:” (for “not 
available”). The Graphs and Tables section has two subsections – Data Specification and Data Graphs. 
Data Specification is where you will identify which results you wish to put into your table and graph.  
 
 
Figure 11. The Graphs and Tables window. 


 
VORTEX Version 9.50 User’s Manual 
 
19 
Chapter 2 
Getting Started with VORTEX 
In the lower left list of Scenarios, make sure that ZPG1 is checked, and then double-click on the box 
under Columns. This will bring up a window that lets you specify which years you want to show as the 
columns of your table and the x-axis of your graph (Figure 12). 
 
 
Figure 12. Specification of years as the columns for tabular output. 
 
To specify years, you can Select All, select individual years by clicking on their boxes, or select rows (all 
years in a decade) or columns (years in decadal intervals) from the table. For example, to select years 0, 
10, 20, …, click on the number 0 at the top of the first column. (Do this now.) The method by which years 
are selected may be a little confusing at first, but once you learn how it works it does allow very rapid and 
flexible specification of sets of years. If you add years to your selection in a non-sequential order, you 
will want then to sort them by clicking on one of the sort buttons on the right. After you have selected the 
years you want, click on OK.  
 
When changing your selection of reporting years, you may obtain better results if you Unselect All 
before making your new selection rather than unchecking multiple boxes.  
 
Next click on the box below Rows, in order to specify which populations you want to list as rows of your 
data table and as separate lines on the graph that will be created. The way you select populations is the 
same as selecting years, except that in this Scenario there is only one population so selecting it is fairly 
trivial. Select Population 1 and hit OK. You will see now that a table has been created, displaying one of 
the result statistics for the years and population(s) that you specified. With the dropdown lists in the left 
side of the screen, you can change the table to display other output statistics.  
 
Change the Variable to N(all), and then hit the Data Graphs tab to show a graph of the values in the table 
(Figure 13). The labels, legend, and line thickness can all be changed. By right-clicking on the graph 
itself, you can also access a broader set of graph properties. By clicking on labels at the lower left, the 
graph can be sent to the Project Report (do this now), or printed, or saved as a bitmap (.bmp) file on your 
disk.  
 
 
 


VORTEX Version 9.50 User’s Manual 
20 Chapter 2 
Getting Started with VORTEX 
 
Figure 13. A Data Graph. 
  
You should note that you have the option of adding bars to your graph to show standard errors (SE) of the 
means, or standard deviations (SD) across the iterations. Click on the “Add SD bars” command to see 
these bars. 
 
Finally, to wrap up our Quick Tour of VORTEX, click on the Project Report tab. This will take you to a 
note pad that contains information we have sent to the Report from other screens (Figure 14). You will 
need to use the scroll bar or your cursor to move up and down through your Project Report. Any 
information in the Project Report can be edited, using standard Windows editing tools (delete, cut, paste, 
font settings, etc.). The Project Report is saved in Rich Text Format (and .rtf) file, and it can be edited in 
Word or other programs.


 
VORTEX Version 9.50 User’s Manual 
 
21 
Chapter 2 
Getting Started with VORTEX 
 
Figure 14. The Project Report. 
  
You have now completed your Quick Tour of VORTEX, and we have looked at most of the main features 
of the program. Spend some time exploring other aspects of the program – change some of the input 
values, run additional scenarios, create some more tables and graphs. Whenever you exit VORTEX, the 
program will ask if you want to save your Project. If you do, all input, output, and report information will 
be saved so that it can be loaded again later.  
 


VORTEX Version 9.50 User’s Manual 
22 Chapter 3 
The Data Input Process 
Chapter 
 
Creating a Project: 
Data Input  
 
 
Creating a Project 
When you open VORTEX, you must first choose whether to create a new Project or open an existing 
Project (Figure 15). To create a new Project, double-click on the Blank Project (or click on the “Blank 
Project” and then hit OK). The Open Project tab will allow you to browse to find an existing  project. The 
Recent Projects tab will allow you to select from a list of the 10 most recent Projects that you have 
worked on. You can get to these same options to create a new Project or open an existing Project from 
either the menu or the tool bar at the top of the VORTEX screen. 
  
 
Figure 15. The welcome window for starting a VORTEX  Project. 
If you choose to start with a Blank Project, the only input values that will be pre-filled are a few that are 
necessary to define the basic Project and Scenario properties. It is often easier to start a new Project by 
opening an existing Project, and then changing those input parameters that are different. However, be sure 
to go through every input screen to confirm that you have set the input parameters to the new values, and 
be sure to save the Project under a new name. When you chose to create a new Project, you next need to 
specify a Project name, and you have the option of recording your name as the Project creator (Figure 16). 
3 


 
VORTEX Version 9.50 User’s Manual 
 
23 
Chapter 3 
The Data Input Process 
You can also specify the directory in which the Project files will be stored, but it usually is reasonable to 
accept the default, which is a subdirectory with the same name as the Project. Click OK to continue. 
 
Figure 16. Dialog box for entering a new project name. 
 
Figure 17. The Project Settings window. 


VORTEX Version 9.50 User’s Manual 
24 Chapter 3 
The Data Input Process 
In the Project Settings windows (Figure 17), you have the option of listing the names of the user team that 
is developing the project (this documentation may be especially helpful in workshop or classroom 
settings), and add any notes that you wish.  
We strongly encourage you to take the time to add notes to your Project at this screen, during 
specification of input parameters, and in your Project Report. The extra few minutes you spend 
documenting your work may save you and others many hours of work later, when you try to 
remember what information and logic was used to create the project. Unfortunately, many PVAs 
are irreproducible because the authors did not fully document their work.  
The Project Settings screen also has a button to send all of the settings to your Project Report (this is 
always a good idea, so that your settings are documented in any printed reports that you create), and 
another button that takes you to a screen for specifying Special Options. The Special Options will not be 
needed by most users. They include options to: 
• 
change the way population sizes are graphed during the simulations, 
• 
use the last population as a holding site for individuals that are harvested from one population and 
then supplemented into others (if this option is chosen, then you specify also what percent of the 
individuals die during this translocation among populations), 
• 
omit the last population from metapopulation tallies (this is useful if the last population is 
considered an outside source for immigration into a metapopulation), 
• 
prevent individuals from dispersing into populations that are at their carrying capacity (where the 
immigrant or some individual would therefore die because of the population exceeding capacity), 
• 
define extinction as any reduction in population size (this is useful when the management goal is 
to prevent further population declines), 
• 
produce files with more detailed results, 
• 
invoke other options that may from time to time be made available, usually on a test basis or for 
special circumstances. (To use this option, you would need to know the undocumented codes for 
using these additional options.) 
At the bottom of the Project Settings screen is a check box to “Make input screens active for viewing ST 
scenarios.” The meaning of this option will be described in Chapter 5.  
To begin entering the values for the parameters that will specify the Scenarios of your Project, click on 
the Simulation Input tab.  
 
Getting Help when Entering Input Data 
 
VORTEX will accept most of the input that you provide, as long as the values are biologically possible and 
within the rather wide limits set by the program (see above). When entering input data, brief hints about 
the values to be entered will be displayed in a line at the bottom of the Project screen. These messages 
appear when you click on a data entry box, and sometimes they will appear as pop-up tooltip messages 
when your cursor passes over a data entry box for more than a few seconds (Figure 18). 
 
If you try to enter a value for input that is of an incorrect type (e.g., a letter when a number is required) or 
outside the acceptable bounds (e.g., a negative number for a mortality rate), then VORTEX will usually 
display a message that the value is invalid, and it will force you to enter a valid value before you proceed 
with data entry. 


 
VORTEX Version 9.50 User’s Manual 
 
25 
Chapter 3 
The Data Input Process 
 
Figure 18. Scenario Settings within Input, showing a tooltip for the Extinction Definition. 
 
It is important to remember that VORTEX will accept input values that are mathematically possible but 
biologically implausible. While VORTEX provides help on many data input questions you may have, such 
as when to enter the data as a proportion or as a percent, the ultimate responsibility for entering valid data 
that will result in a meaningful model rests with you, the user.  
 
Most of the material in Chapters 1-6 of the manual is available through the Help menu of the program. 
Selecting “Contents” on the Help menu will take you to a Table of Contents, which provides links to each 
section of the Help manual. (Click on a section heading in the Table of Contents to jump to that topic in 
the manual.) Selecting “Context-sensitive” help from the menu or clicking on the ‘?’ icon on the toolbar 
or hitting the F1 key during data entry will open the Help file and jump right to the place in the file that 
describes the current program screen.  


VORTEX Version 9.50 User’s Manual 
26 Chapter 3 
The Data Input Process 
Documenting Your Input with Notes 
 
Whether you are using VORTEX as a researcher, a wildlife manager, or a student, it is highly likely that 
you will need to document for others (and even for yourself when you return to a Project that had been set 
aside for a period of time) why you used the input values you did to create your Scenarios. When you are 
eager to get a Project running, it is very tempting to skip over the task of documenting the sources and 
reasons for your input values. However, you may save yourself later hassles if you take the time at the 
outset to record why program options and parameter values were chosen.  
 
VORTEX provides a utility to attach a note with each piece of data requested as input. You can access the 
Input Notes by either of two methods: clicking on the Notes icon on the program toolbar; or just typing 
directly into the long text box below the input window. It may be faster to type a note into the text box at 
the bottom of the screen, but there is a risk that you could enter your note for the wrong input question.  
After you type a note into the text box showing on the Simulation Input screen, and hit Enter, your Note 
will then be associated with the input parameter or question that last had cursor control.  
 
When you open Input Notes by clicking on its icon, you then select the Input section input parameter for 
which you wish to enter a note (Figure 19). You then enter the text of your note in the box at the right.  
 
 
Figure 19. Input Notes pop-up utility. 
 
As you move among input screens and boxes, any Note for the input box that is selected is displayed in 
the text box below the input window.  
 
The Input Notes screen provides commands for pasting the displayed Note or All Notes into your Project 
Report, and for printing the displayed Note or All Notes. Thus it is easy to quickly insert your Input Notes 
into a report of your work. Input Notes are always saved when you save a Project. 
 
You can view Notes for a Sensitivity Test Scenario (see Chapter 5), but the Notes that you see will be the 
Notes made for the underlying Baseline Scenario. Any changes that you make to the Notes for an ST 
Scenario will be discarded (and replaced again with the Notes from the Baseline) when you Save your 
Project.  


 
VORTEX Version 9.50 User’s Manual 
 
27 
Chapter 3 
The Data Input Process 
Creating a Scenario 
 
Input of model parameters into VORTEX is accomplished in 14 sections, each containing questions 
pertaining to a category of model parameters. You move among the input sections by clicking on their 
labels in the list on the left hand side of the Simulation Input screen. You can move among the sections to 
enter data in any order, although the list provides a logical sequence for data input. After you have visited 
an input section within a VORTEX session, the label for that section will be in italics. This may help you to 
quickly check whether you have completed data entry for every section. 
 
If you jump around among input sections, you risk forgetting to visit a section, and then running 
models that are missing some parameters or that have values from scenarios used as templates. 
In addition, VORTEX uses answers on some early screens to complete intermediate calculations 
(such as the stable age distribution) that are useful when you reach later input sections. 
 
Scenario Settings 
 
The first data input screen you encounter when creating a Scenario asks for some basic Scenario Settings 
(Figure 18 above). Subsequently, you will need to step through 13 more input screens to complete the 
process of specifying the values for all of the input parameters needed by VORTEX. Below are described 
all the input parameters requested on these screens.  
 
Scenario Name: Within each project you create scenarios that are defined by their sets of parameter 
values. As you will see, after you have defined one scenario (often a “Baseline” or “Best Guess” 
scenario), it is easy to create additional scenarios that change one or a few of the input values. The default 
scenario name for a new project is just “Scenario 1”. On the Scenarios Settings screen, you should change 
this to a more descriptive name.  
 
Number of Iterations: The answer to this question instructs VORTEX on how many times you wish to 
repeat the simulation, given the data that you provide in the subsequent steps. Each repetition is generally 
defined as a “run” or “iteration”. Because VORTEX uses a random number generator to simulate random 
events in the life cycle, no two iterations will be identical. Thus, to obtain a more complete “picture” of 
your simulated population, you will want to generate multiple iterations of your model. 
 
As a first step in the development of a sound population model, you may want to make sure that the 
simulated population is behaving in a manner that is similar to your expectations. To check this, you can 
limit the number of iterations to just 10 or 20. If you wish to obtain a relatively crude picture or your 
results, use 100 iterations. Once you are comfortable with the model and wish to obtain a more rigorous 
description of the simulated population’s behavior, it is not excessive to enter 500 or even 1000 iterations 
in this field. Note that commas are not used when specifying larger numbers during the input process, 
even if your computer is set to use American data formats . 
 
Number of years:  How far into the future do you wish to project your population? The usual answer to 
this question is 100 to 200 years, although a shorter duration can be entered so that you can assess the 
validity of your input parameters, or to examine the short-term viability of a population. If you simulate 
your population for just a few decades, however, you should be aware that processes controlling 
population dynamics might be leading the population toward extinction but, especially for long-lived 
species, the final extinction may not occur until a later time. By the time that the factors influencing 
extinction are apparent, the process may be so far along as to be almost irreversible. One of the major 
advantages of PVA modeling is that it can reveal the instability of a population long before it would be 
apparent through field observations. 


VORTEX Version 9.50 User’s Manual 
28 Chapter 3 
The Data Input Process 
 
An important point to keep in mind is that VORTEX does not necessarily require “years” to be defined as 
calendar years. Rather, the program operates more broadly in terms of “time cycles”. If the species you 
are modeling has a short generation time and life span, on the order of weeks or months—such as mice or 
shrews, for example—true calendar years would be an inappropriate time scale to use for modeling 
population dynamics. In this case, a “year” for this type of species may actually represent only one or a 
few months. When calculating your demographic inputs, it is vitally important that you make this 
adjustment consistent throughout your calculations (see Case Study I for more information). 
 
Extinction Definition: VORTEX gives you three methods to define “extinction” of your population. For 
most sexually reproducing species, ultimate biological extinction is assured whenever the population has 
declined to the point that it no longer has individuals of both sexes. In the first (and most common) 
choice, extinction is simply defined as the absence of at least one sex.  
 
You also have the option to assess the probability of a population dropping below a user-defined 
threshold size – termed quasi-extinction. The use of quasi-extinction risk offers a useful alternative to the 
standard extinction risk. If you chose to have the simulation tally quasi-extinctions, you need to specify 
the threshold “critical size” below which a population is considered extinct. The simulation will, however, 
continue to run, as the population may grow again to a size above this threshold. Such recovery from 
quasi-extinction would be tallied as a recolonization event. A third option is available under Special 
Options on the Project Settings screen, which defines extinction as any decline in population size. 
 
Number of Populations: VORTEX can model a single, isolated population or a complex metapopulation 
composed of up to 50 populations. A metapopulation is a group of populations which, because they often 
occupy fragmented, discontinuous habitat, exchange individuals with varying frequency. Note that, 
because of the added complexities associated with metapopulations, these models will often run 
considerably slower than the corresponding single-population models.  
 
If there is no exchange of individuals among populations (i.e., dispersal) in your model, it 
maybe faster to run several individual simulations (with each one modeling an isolated 
population) instead of a more complex metapopulation model. 
Case Study I:  
Calculating input parameters when the “time cycle” is less than one year 
 
Consider a hypothetical rodent population where the average generation time is 180 days.  In order 
to model this population most effectively in VORTEX, the user must adjust the “time cycle” to account 
for this shortened generation time. In this case, we will define a VORTEX “year” as 90 days. 
Consequently, events whose occurrences are typically described on an annual or per-generation 
basis must be redefined in terms of the new definition of “year”. 
 
For example, consider a major catastrophic flood that is thought to occur on average once every 100 
years. The annual probability of occurrence, then, is 0.01. Because of the altered definition of 
“year”, the rodent model must define the probability that this flood will occur in any given 90-day 
interval. The number of 90-day time cycles in a calendar year is T = 365 / 90 = 4.06. Therefore, 
 
.
.
.
.
0025
0
06
4
010
0
Pr(flood)
Pr(flood)
365
90
=
=
=
T
 
 
The same considerations must be applied to all other demographic rates, such as mortality, age of 
first and last breeding, etc. In addition, appropriate migration, harvesting and supplementation rates 
must be established relative to the revised time cycle. 


 
VORTEX Version 9.50 User’s Manual 
 
29 
Chapter 3 
The Data Input Process 
Enter the number of populations that comprise your metapopulation model or enter 1 for a simulation 
composed of a single population. If you intend to build a metapopulation model, you will later need to 
specify dispersal rates and some other parameters. 
 
Species Description 
 
The next section of input includes a set of basic questions about the species being modeled (Figure 20). 
 
 
Figure 20. Species Description section of Input. 
 
Inbreeding depression: Check this box if you want to include inbreeding depression in your model, as a 
reduction in first-year survival among inbred individuals. (See Box B for more information). Although 
most diploid species that have been studied show depressed fitness when inbred, you may sometimes 
want to leave inbreeding depression out of your model so that you can compare results with and without 
inbreeding depression – thereby allowing you to document what impacts inbreeding depression could 
have on population viability. 


VORTEX Version 9.50 User’s Manual 
30 Chapter 3 
The Data Input Process 
 
Box B: Quantification of Inbreeding Depression 
 
Inbreeding depression is the reduction in fitness commonly observed when individuals are produced 
by matings between genetic relatives. Inbreeding depression seems to affect most (perhaps even all) 
species of sexually reproducing organisms, and can cause reduction in survival (of infants, juveniles, 
and adults), mate acquisition, fertility, fecundity, number of progeny per litter or brood, and a 
variety of physiological measures related to fitness such as growth rate, disease resistance, stress 
resistance, metabolic efficiency, sensory acuity, and behavioral dominance (see Lacy 1997 and 
references therein).  
 
Although inbreeding depression can affect many components of fitness, often the overall effect can 
be reasonably well summarized by or combined into an effect on infant survival. For example, if 
inbreeding causes a 10% reduction in litter size, and then a 10% reduction in survival of those 
individuals born, the cumulative effect would be the same as a 19% reduction in infant survival 
(resulting in 81% of the yearlings which would have been produced if no inbreeding had occurred). 
Also, most of the published literature on inbreeding depression in wild species of animals deals only 
with effects on juvenile survival (Ralls et al. 1988; Lacy et al. 1993). Therefore, the primary way in 
which inbreeding depression is incorporated into VORTEX is through a reduction in first-year survival 
of inbred individuals. (If desired, inbreeding effects on later survival, reproduction, carrying capacity, 
and even dispersal can be modeled using functions of inbreeding to specify demographic rates: see 
Chapter 5 for more information.) 
 
While inbreeding depression is widely known (and has been for centuries), understanding the various 
possible underlying mechanisms, the ways of quantifying it, and the consequences for population 
survival and viability is not at all simple. Inbreeding depression may result from recessive deleterious 
alleles (which are exposed more frequently in homozygous inbred individuals), or from a general 
disadvantage of homozygotes relative to heterozygotes, or from other genetic mechanisms (see 
Charlesworth and Charlesworth 1987; Lacy 1993b). In studies of Drosophila flies, it has been 
observed that about half of the effect of inbreeding depression on survival is due to recessive lethal 
alleles (Simmons and Crow 1977). The relationship between survival and inbreeding caused by the 
presence of recessive lethal alleles is described by an exponential decline: 
 
bF
S
S
−
=
e
0
 
 
in which S0 is the survival of non-inbred individuals, F is the inbreeding coefficient, b is the average 
number of lethal alleles per haploid genome (half the number per diploid individual), and S is the 
resultant survival rate (Morton et al. 1956). Figure B-1 gives the expected relationship between the 
extent of inbreeding and juvenile survival for a series of hypothetical scenarios differing in the total 
number of lethal equivalents.  
 
Even if the overall inbreeding depression is due only partly to recessive lethal alleles, the relationship 
between inbreeding and survival might be expected to be roughly an exponential decline of this 
form. By observing the relationship between survival and inbreeding, the coefficient b in the above 
equation can be measured. The value b is a measure of the severity of the effects of inbreeding (not 
in terms of how inbred the population is—as that is measured by F—but rather in terms of how much 
fitness is depressed for any given level of inbreeding), and it is the number of recessive lethal alleles 
per haploid genome that would cause the observed rate of inbreeding depression. This concept is 
called the number of “lethal equivalents” in the population. A population with 4.0 lethal equivalents 
per diploid individual (b = 2.0) might have 4 lethal alleles per individual, or it might have 8 alleles 
per individual which each cause 50% reduction in survival when homozygous, or it might have 2 
lethal alleles and four 50% lethals, or any other combination of deleterious alleles which have the 
same total effect. 
 
VORTEX uses this concept of lethal equivalents to quantify the severity of depression of first-year 
survival due to inbreeding. Thus, the user must specify how many lethal equivalents characterize the 
population under study. For only a few species, however, has the number of lethal equivalents been 
measured in careful breeding studies. Among those species that have been studied, the number of 
lethal equivalents per diploid (2b) ranges from 0 to more than 30, but it is usually in the range of 1 
to 5. (Isn’t it depressing to know that you probably carry from 1 to 5 alleles which would be fatal  


 
VORTEX Version 9.50 User’s Manual 
 
31 
Chapter 3 
The Data Input Process 
Box B (Continued)… 
 
Inbreeding Coefficient (F)
0.0
0.1
0.2
0.3
0.4
0.5
Juvenile Survival
0.0
0.2
0.4
0.6
0.8
1.0
2.0 LE
4.0 LE
6.0 LE
 
genetic defects if you had two copies of any one of those alleles? Aren’t you glad that you are 
diploid?) To date, no clear patterns have emerged to suggest that certain taxonomic, ecological, or 
other categories of species typically have high or low number of lethal equivalents – it seems to be 
largely a matter of chance whether a population is severely affected by inbreeding or not. 
 
How does VORTEX use “lethal equivalents”?   
VORTEX simulates inbreeding depression in two ways, because different genetic mechanisms of 
inbreeding depression can have different consequences for population viability. Recessive lethal 
alleles are rather efficiently removed from a population by natural selection when inbreeding occurs. 
As a result, many individuals may die in the early generations of inbreeding, but when they die they 
take their lethal alleles with them to the grave, and subsequent generations of individuals have 
fewer lethal alleles to cause inbreeding depression. (This process is often referred to as “purging the 
genetic load” of lethal alleles. See Hedrick 1994; Ballou 1997; and Lacy and Ballou 1998.) On the 
other hand, selection is ineffective at purging inbreeding depression when the inbreeding depression 
results from a general advantage of heterozygotes over all homozygotes (or, to a lesser extent, 
when it is caused by recessive sub-lethal alleles).  
 
To model the effects of lethal alleles, which can be removed by selection during generations of 
inbreeding, VORTEX assigns to each individual at the start of a simulation some unique lethal alleles. 
If inbred descendants happen to receive two copies of the same lethal allele, they are killed. To 
model the component of inbreeding depression that is not effectively reduced by selection, VORTEX 
calculates the inbreeding coefficient of each individual and then applies an exponential equation like 
the one above (but using just a part of the total lethal equivalents) to determine how much that 
individual’s survival is reduced. To incorporate these two mechanisms of inbreeding depression, 
VORTEX needs to know (i.e., you need to tell it) how much of the overall inbreeding depression (lethal 
equivalents) to assign to lethal alleles vs. other genetic mechanisms. As mentioned above, for 
Drosophila flies, it has been reported that about half of the lethal equivalents are due to actual lethal 
alleles. Almost no other species have been studied in sufficient detail to quantify the contributions of 
different types of alleles to inbreeding depression, but the scant data available are not inconsistent 
with about half of the inbreeding effects being due to lethals in other species as well. 
 
In summary: if you don’t know what to enter for inbreeding depression in VORTEX, use the default 
values of 3.14 lethal equivalents (the median of 40 mammalian populations surveyed by Ralls et al. 
1988) with 50% of that due to lethal alleles. 
 
 
Figure B-1.  Expected juvenile survival as a function of 
inbreeding coefficient under alternative levels of 
inbreeding depression severity, defined as the number of 
lethal equivalents (LE) per haploid genome (see text for 
details). 


VORTEX Version 9.50 User’s Manual 
32 Chapter 3 
The Data Input Process 
VORTEX runs much more slowly when inbreeding depression is included and is modeled with less 
than 100% of the impact due to lethal recessives (see below). This is because the program will 
need to calculate and store all pairwise kinships among individuals in the population (N2 kinships, 
where N is the maximum population size attained). Therefore, if your population is expected to 
remain moderately large (perhaps > 500), so that inbreeding will be a rare event, you may want to 
obtain much greater speed by assuming in your model that inbreeding has no impact on fitness.  
 
VORTEX includes a detailed simulation of genetic change in the populations. At the beginning of a 
simulation, each founder individual is assigned two unique alleles at each of a number of loci. Each 
offspring is then randomly assigned one of the two alleles from each parent at each locus. VORTEX 
normally models allele transmission at 10 loci that may contain lethal alleles (allowing up to 10 unique 
and independent lethal recessive alleles per founder) and also at one neutral locus (with no impact on 
inbred progeny). In the Genetic Management section of input, you have the option of asking VORTEX to 
model alleles at a greater number of neutral loci. Doing so will produce more precise results for genetic 
trends, and the details of the emergent genetic patterns at the modeled loci can optionally be output to a 
file for further examination.  
 
In its simplest form, inbreeding depression is modeled in VORTEX as a reduction in the survival of 
offspring during the first year of life. As a result, the program generally underestimates the impact of 
inbreeding as it can also depress other components of fitness such as adult survival, fecundity, and/or 
success in competition for mates. (More complex relationships between inbreeding and demographic rates 
can also be modeled; see Chapter 6 for more on this subject.) 
 
Lethal Equivalents: This box and the next ask you to specify the severity and nature of inbreeding 
depression in your simulated population. Enter the average impact of inbreeding on first-year survival, 
quantified as a number of “lethal equivalents” per diploid individual. As described more fully in Box B, 
the default value of 3.14 is a summary statistic based on a survey of 40 captive mammalian populations 
(Ralls et al. 1988). If you have specific data indicating a different genetic load, you can enter it here.  
 
Percent Due to Recessive Lethals: Enter here the percent of the total genetic load (quantified by the lethal 
equivalents you entered into the previous box) that is due to recessive lethal alleles. The number of lethal 
alleles per founder is limited to 10; therefore, the product of the number of lethal equivalents and the 
percent of the total genetic load attributable to lethals cannot exceed this number. The lethal alleles are 
distributed randomly among 10 autosomal loci; thus, the number of lethals per founder will be distributed 
approximately as a Poisson distribution. A plausible value – one that is consistent with data on 
Drosophila and a few other species that have been studied well – would be 50%. However, cases have 
been reported in which nearly all of the genetic load is due to lethals, while – in other populations – 
virtually none of the effects of inbreeding appears consistent with the action of recessive lethal alleles 
(Lacy et al. 1996). You may wish to test low and high values to see if it affects your simulations of 
population dynamics. (It probably won’t, because it is difficult to maintain a population for long at the 
very small population sizes at which effective purging of recessive lethal alleles would occur.) 
 
EV Concordance of Reproduction & Survival:  Environmental variation (EV) is the annual variation in 
the probabilities of reproduction and survival that arise from random variation in environmental 
conditions. (For a more detailed introduction to this topic, refer to Boxes C and D.) EV impacts all 
individuals in the population simultaneously. The sources of this environmental variation are outside the 
population; examples include weather, predator and prey population densities, and parasite loads. These 
factors can affect reproduction and survival independently or simultaneously. Check this box if you think 
that good years for reproduction are also good years for survival. 


 
VORTEX Version 9.50 User’s Manual 
 
33 
Chapter 3 
The Data Input Process 
 
Box C: A Brief Statistics Primer  
 
Many demographic characteristics among wildlife species (e.g., birth and death rates, litter size, etc.) 
fluctuate randomly in magnitude from one year to the next. In order to be able to describe this 
variability, and to use VORTEX most effectively, you must have at least some basic knowledge of a 
few concepts in statistics.  
 
Population Statistics vs. Sample Statistics 
It is important to keep in mind the distinction between the value of a variable or statistic in a 
population and the value of the variable across a smaller set of observations sampled from that 
population. Usually, we do not know the true value for the entire population, and that is something 
we wish to estimate by examining a sample from that population. For some statistics, such as the 
mean, the best (and unbiased) estimate of the true population value is simply that statistic 
calculated for the observed sample. For some other statistics, such as the variance and standard 
deviation, the statistic calculated on the sample is a biased measure of the value for the whole 
population, so that correction factors must be applied to get a better estimate of the population 
statistic. Below we somewhat loosely follow a common convention of using Greek letters to 
symbolize the true (but often unknown) population statistic, Roman letters for sample statistics, and 
letters with “hats” (for example, hˆ ) to symbolize estimated values. 
 
Measures of Central Tendency and Variability 
When a biologist studies a particular demographic characteristic in a wildlife population over some 
period of time, one generally notes an abundance of values clustered near the middle of a range of 
annual observations. In the language of statistics, the description of this concentration near the 
midpoint is a measure of central tendency. The most common measure of central tendency is the 
arithmetic mean or, more simply, the mean. The mean of a sample of observations is calculated as 
 
 
,
n
X
X
n
i
i
∑
=
=
1
 
 
which says that the sample mean equals the sum of all measurements in the sample divided by the 
number of measurements in that sample. Another common measure of central tendency is the 
median, which is the value at which 50% of the observations fall below and the remainder fall above 
that value. For a symmetrical distribution, the median will approximate the mean. 
 
To complete our initial description of these data, we must define a measure of variability in the data. 
The most commonly used measure of variability is the variance, usually denoted by s2:  
 
.
)
(
1
2
2
−
−
= ∑
n
X
X
s
i
 
 
The “n-1” in the denominator is a necessary correction factor to ensure that the estimate from the 
sample is an unbiased estimate of the variance in the population. (If we measured the variance on 
the entire population, we would not need this correction and could simply use n in the denominator.) 
 
From this equation, it is evident that s2 gets larger as the amount of variability about the mean 
increases. The standard deviation (s), often abbreviated as SD, is the positive square root of the 
variance and is another very common descriptor of variation in a sample of observations. As you 
enter data into VORTEX for your species, you will be defining the variation in demographic rates in 
terms of standard deviations. We can also describe variability through the use of the coefficient of 
variation (here labeled CV), in which sample variability is expressed as a percentage of the mean: 
 
 
.
%
100
⋅
=
X
s
CV
 
Finally, the simplest measure of variability is the range of values observed in the sample. 
Unfortunately, the observed range is highly sensitive to the number of observations that are made. 


VORTEX Version 9.50 User’s Manual 
34 Chapter 3 
The Data Input Process 
 
Box C (Continued)… 
 
The Binomial Distribution  
When summarizing a dataset consisting of a number of individual observations, it is useful to present 
that summary graphically in the form of a frequency distribution, usually in the form of a bar graph. 
Often we are dealing with data on a dichotomous variable—such as alive or dead, breeding or not  
breeding, male or female—and we are interested in tallying  
the frequency of each possibility in a sample of n  
observations (also known as cases or trials). The probability  
of any given case belonging to one or the other category is  
denoted p and q, with p + q = 1. The frequency of samples  
consisting of 0, 1, 2, …, or n observations of a specific  
category in a sample of n cases is described by a binomial  
distribution. Figure C-1 shows a pair of binomial distributions 
 for n = 5. 
 
 
 
 
 
 
 
 
 
 
If n observations are sampled from a population with X belonging to one category and n – X in the 
other, then the population parameter p, the proportion of the observations that is in the first 
category, can be estimated by the observed proportion within that sample: 
 
.
ˆ
n
X
p =
 
 
If this sampling procedure were to be repeated a number of times, each estimate of pˆ  would likely 
be different. The variance of all possible values of pˆ  would be 
 
,
ˆ
n
pq
p =
2
σ
 
 
in which p is the true probability in the population, and q = 1 – p. If p is estimated from the sample, 
however, then this variance is biased (underestimated); replacing n by n – 1 results in a better 
estimate of the variance of p across samples. The standard deviation of pˆ  is therefore estimated by 
 
.
ˆ
ˆ
ˆ
1
−
=
n
q
p
sp
 
The Normal Distribution 
In a manner similar to the categorical data  
described by a binomial distribution, continuous  
variables are generally observed to have an  
abundance of values nested around the mean with  
progressively fewer observations near the  
maximum or minimum values. When these  
observations are viewed graphically, the resulting  
frequency distribution takes on the look of the  
familiar “bell-shaped” curve, particularly when the  
number of observations (n) becomes large. This  
curve is more formally described as a normal  
distribution. Figure C-2 shows a normal distribution. 
Figure C-1. The binomial distribution for sample size  
n = 5 and (a) p = q = 0.5; and (b) p = 0.4, q = 0.6. The 
bars give the probabilities p(X) of obtaining a particular 
number of observations of the first category. For example, 
with p = 0.4 and q = 1 – p = 0.6, the probability of obtaining 
a sample consisting of one observation (out of a possible 5) 
in the first category is 0.259. 
p(X)
0.0
0.1
0.2
0.3
0.4
X
0
1
2
3
4
5
p(X)
0.0
0.1
0.2
0.3
0.4
(a)
(b)
p = 0.5
q = 0.5
p = 0.4
q = 0.6
 
X
f(X)
µ - 3σ
µ
µ - 2σ
µ − σ
µ + σ
µ + 2σ
µ + 3σ
Figure C-2. A normal distribution.


 
VORTEX Version 9.50 User’s Manual 
 
35 
Chapter 3 
The Data Input Process 
 
 
EV Correlation Among Populations: You specify here the correlation of EV among populations 
(applicable, of course, only when more than one population is modeled). If this value is set to 0.0, then 
EV will be completely independent among populations. If this value is set to 1.0, then EV in reproduction 
and in survival will be completely synchronized among populations. As a result, good years for 
reproduction and / or survival in one population will lead to similarly good years in all other populations. 
If this degree of correlation is set to an intermediate value, then EV will be partly correlated among 
populations. 
 
Environmental variation in the metapopulation context can be considered to exist at two levels: local 
(population-specific) and global (acting across all populations). The total EV, when expressed as a 
variance rather than a standard deviation as entered by the user, is simply the sum of the EV existing at 
these two levels. The correlation of EV among populations that you enter, then, is simply the proportion 
of the total EV (when expressed as a variance) that is global in scope (i.e., common to all populations). 
 
Case Study II:  
Correlating environmental variation for reproduction and survival 
 
North America’s whooping crane (Grus americana) shows a classic migratory pattern typical of many 
bird species. The last remaining substantial population breeds in Alberta’s Wood Buffalo National 
Park and spends the winter at Aransas National Wildlife Refuge along the Gulf Coast of Texas. 
Because of this movement pattern, the environmental conditions affecting chick production are quite 
different from those impacting mortality during the majority of the year (Mirande et al. 1991). 
Consequently, we would expect EV affecting these processes to be uncorrelated when constructing a 
VORTEX model 
Box C (Continued)…  
 
Note in Figure C-2 the relationship between the population mean (µ) and standard deviation (σ) in a 
normal distribution. Using a fairly simple method known as normalizing a distribution, we can calculate 
that 68.3% of all observations in a normally-distributed population fall within the range of µ ± σ, 
95.5% fall within µ ± 2σ, and 99.7% fall within µ ± 3σ. This kind of information is helpful when 
estimating standard deviations in demographic rates caused by environmental variation when only a 
range of observations are available (see Box E for additional details).  
 
It is also noteworthy that the binomial distribution becomes quite close to a normal distribution when 
the number of observation per sample (n) is large—say, when n > 20. Observe that even when n is as 
small as 5, the distributions shown in Figure C-1 look like approximate bell curves. However, one 
important distinction between the binomial and normal distributions is the binomial distributions are 
always bounded at 0 and n, while normal distributions have “tails” that are infinitely long, but rapidly 
diminishing. 
 
For more information on the theory and applications of these and many other concepts relevant to an 
understanding of population dynamics and risk projections, see Caughley (1977), Sokal and Rohlf 
(1994), and Zar (1996). 


VORTEX Version 9.50 User’s Manual 
36 Chapter 3 
The Data Input Process 
  
Box D: The Statistics of Demographic Stochasticity  
and Environmental Variability 
 
Now that you have reviewed some of the general definitions of central tendency and variability (see 
Box C), as well as some characteristics of the binomial and normal distributions, we can discuss the 
statistical nature of demographic and environmental stochasticity. 
 
Demographic stochasticity is the random fluctuation in observed birth rate, death rate, and sex ratio 
of a population resulting from stochastic sampling processes, even if the probabilities of birth and 
death remain constant over time. In such cases, the annual variation in numbers of individuals that 
are born, that die, and that are of a given sex can be specified from statistical theory and would be 
expected to follow binomial distributions. Environmental variability is the annual fluctuation in 
probabilities of birth and death arising from random fluctuations in the environment (e.g., weather, 
abundance of prey or predators, prevalence of nest sites, etc.). Annual fluctuations in the 
probabilities of reproduction and mortality are modeled in VORTEX as binomial distributions, while 
environmental variation in carrying capacity (see Box F for more on this topic) is modeled as a 
normal distribution. 
 
Note that the distinction between demographic stochasticity and environmental variability is a subtle 
one (even some professional population biologists have been confused by this!). Demographic 
stochasticity is the variation in an observed vital rate due to the sampling variation that is inherent 
because each individual (an observation) is an independent and random sample from a population 
with a given mean or probability. Hence, it is the variation in sample means  ( X ) around a fixed 
population mean (µ). Environmental variation, on the other hand, is variation (due to extrinsic 
factors that vary over time) in the population mean itself (i.e., µ is different each year). 
 
Putting this information together, we conclude that the variation across years in the frequencies of 
births and deaths—both in real populations and our simulated VORTEX populations—will have two 
components: the demographic variation resulting from binomial sampling around the mean for each 
year, and additional fluctuations due to environmental variability. In actuality, catastrophic events 
(to be discussed in more detail later in the User’s Manual) also contribute to the overall observed 
variation across many years of data, but they are treated separately from standard annual 
environmental variability. 
 
 
 
 
 
 
 
 
 
Annual Demographic Rate (%)
0
10
20
30
40
50
60
70
80
90
100
Year
1
2
3
4
5
6
7
8
9
10
"Outlier"
Annual Demographic Rate (%)
0
10
20
30
40
50
60
70
80
90
100
Frequency (%)
0
20
40
60
80
Excluding outlier
Including outlier
EV only
 
Figure D-1. Left panel: Expected values for a given annual demographic rate, showing binomial sampling 
variance arising from demographic stochasticity with a sample size (n) of 100 individuals. Right panel: 
Frequency distribution of that same demographic rate based on observed mean and variance of annual 
values. Solid and dashed curves show the normal distributions that most closely fit the observed data with 
and without the catastrophic “outlier”, while the dotted line shows the normal approximation to the 
binomial distribution expected solely from environmental variability (and excluding the outlier). The 
difference between the solid and dotted lines gives the variation attributable to demographic stochasticity. 


 
VORTEX Version 9.50 User’s Manual 
 
37 
Chapter 3 
The Data Input Process 
 
Box D (Continued)… 
 
The left panel of Figure D-1 shows ten years of expected values of a given demographic rate—say, 
juvenile mortality—in a simulated wildlife population. Each “bell-shaped” curve depicts the 
probability distribution we would expect from demographic stochasticity acting on that rate in that 
year (Actually, these little curves of demographic stochasticity would be binomial, but the normal 
distributions are close enough for illustration purposes). For example, the expected rate (µ) in year 1 
is 15.2%. However, when the fate of each juvenile in the population is considered, it is possible that 
the actual rate may deviate from 15.2% solely from this sampling process. In addition, the expected 
mortality changes from year to year due to environmental variation, with each annual curve again 
reflecting the sampling variance (demographic stochasticity) expected for that year’s value. Note 
that these curves become tighter (the standard deviation resulting from demographic stochasticity 
decreases) as the means deviate from near 50%. In addition, notice that the mortality rate in year 7 
is particularly high; perhaps a catastrophic event occurred in that year to produce such high 
mortality. 
 
With annual rate data in hand, we can actually calculate the relative contributions that demographic 
stochasticity (DS) and environmental variability (EV) make to the total observed variance. Consider 
the example presented in Figure D-1. The mean mortality rate calculated from these annual data is 
0.387 with a standard deviation (combining effects of DS and EV) of 0.148. Note, however, that the 
catastrophe shown as the outlier in the dataset was not included in this calculation; if it were, the 
mean and standard deviation would change to 0.435 and 0.204, respectively. If we consider the data 
with the outlier absent, we can calculate the standard deviation due to EV: 
 
2
DS
2
TOT
2
EV
EV
σ
σ
σ
σ
−
=
=
 
 
where 
2
TOT
σ
 is the total variance across the data and 
2
DS
σ
 is the mean sampling (binomial) variance 
across the individual rates (see Box B for how to calculate a binomial variance). In the example 
above, the mean binomial variance turns out to 0.0022. Therefore, 
 
140
0
0022
0
0219
0
2
EV
EV
.
.
.
=
−
=
=
σ
σ
 
 
which is the variation across years of the mean (peak) values for each curve in the left panel of the 
figure. This calculation tells us that the contribution of demographic stochasticity to the total 
variance observed in our nine years of mortality data (remember, we removed the outlier from the 
analysis) is quite small—the variance attributable to environmental variability is almost 90% of the 
total variance in mortality. This is shown graphically in the right panel of Figure D-1. In order for 
demographic stochasticity to make a significant contribution to the total observed variance, the 
number of individuals sampled for a given rate (n) would have to be quite small—on the order of a 
few tens. 
 
The right panel of Figure D-1 also shows the frequency distribution obtained by including the 
catastrophe outlier in the calculation of overall mean and variance. The inclusion of this single 
observation results in a significantly poorer fit to the data, as the overall distribution of values (the 
mean of all values in the left panel) does not look much like a normal distribution. This helps in part 
to illustrate why catastrophes—events that are infrequent in occurrence yet severe in population 
impact—are treated separately from more typical annual or seasonal fluctuations.  
 
Finally, it is instructive to note that each of the distributions in the right panel of Figure D-1 extend 
beyond 0.0 and/or 1.0. As this is biologically implausible, we need to truncate these distributions in 
order to allow their proper use in defining probabilities. Partly for this reason, VORTEX usually uses a 
binomial distribution (which does not extend beyond 0% and 100%, but which otherwise looks much 
like a normal distribution) to represent EV. For ease of calculation, VORTEX sometimes does use a 
normal distribution when it is a very close approximation to the binomial, but it then truncates the 
normal curve symmetrically about the mean to avoid creating any bias. 


VORTEX Version 9.50 User’s Manual 
38 Chapter 3 
The Data Input Process 
 
Number of Types of Catastrophes: Catastrophes can be thought of as extremes of environmental variation 
that strongly impact reproduction and/or survival. Types of catastrophes might include sudden habitat 
destruction, floods, forest fire, epidemic disease outbreaks, etc. Catastrophes can be significant threats to 
small, isolated populations. For example, disease decimated the last population of black-footed ferrets, 
and a hurricane killed half of remaining wild Puerto Rican parrots. It is up to you to determine what types 
of catastrophe, if any, may impact your population. Later in the data input process, you will be given the 
opportunity to define how each type of catastrophe will impact reproduction and survival.  
 
You may be able to identify historical catastrophes by examining birth and/or death rate data over 
several past years for your species of interest. If you find a demographic rate that is significantly 
different than that described by normal levels of variation—for example, at least 2 standard 
deviations from the mean value—you may use that as evidence of a catastrophic event. 
 
When you are finished with entering Species Description parameters, click on the heading for Labels and 
State Variables on the left-hand list. 
 
Labels and State Variables 
 
In this Input section, you can enter optional labels for your populations, as well as define parameters that 
describe characteristics or “states” of your populations and individuals.  
 
The powerful options in this section can be rather confusing to use. Most users can skip over this 
entire Input section, with the possible exception of entering Population Labels. Only experienced 
users should attempt to define and use Population State Variables, Individual State Variables, or 
meta-model linkages to other programs. 
 
Population Labels and State Variables:  VORTEX allows the user to enter a label for each population being 
modeled (Figure 21). The labels can be any text, up to 20 characters long. These population labels will be 
used as headers for entry of population-specific demographic rates (on subsequent data entry screens) and 
as labels in the output files. One population label is entered per line. 
 
When entering a population label, the user may also specify up to 10 numbers for use as “state variables” 
describing some characteristic of the population. These state variables must be numeric values that are 
entered on below the population labels in the table. State variables may describe characteristics such as 
measures of habitat quality or habitat suitability for the population, elevation or some other descriptor of 
the habitat, or perhaps an identifying code for the subspecies or local population. This option of entering 
population state variables is provided so that demographic rates (such as fecundity, mortality, and 
Box D (Continued)… 
 
The above methods are a bit complex. Because DS is usually quite small when the sample sizes (n) 
are at all large, a quick, somewhat generous, estimate of EV is simply the total variation in rates 
observed across years (treating DS as an insignificant contributor to the observed variation). 
 
Finally, keep in mind that the VORTEX simulation program generates DS automatically as it 
determines whether each individual lives, whether it breeds, and what sex it is. Unlike some other 
PVA programs, you do not specify that DS should be added into the model, and you cannot exclude 
it (from the model or from real life). You do need to specify the magnitude of EV, however, as EV 
results from external processes rather than being an intrinsic and inevitable part of all population 
dynamics. The size of DS is a consequence of the population size; the size of EV depends on the 
constancy of the environment. 


 
VORTEX Version 9.50 User’s Manual 
 
39 
Chapter 3 
The Data Input Process 
carrying capacity) can be specified to be functions of these state variables. (See Chapter 6 for a 
description of the use of functions for demographic rates.) In such functions, the state variables are 
symbolized as PS1, PS2, etc. Functions characterizing the demographic rates for each population could 
always be entered in earlier versions of VORTEX even without using state variables, but the use of state 
variables can allow for a more consistent representation of demographic rates across populations and 
easier testing of the effects of varying habitat or population characteristics. These capabilities will be 
explained in much greater detail in Chapter 6. 
 
 
Figure 21. Labels and State Variables Input section. 
 
Individual State (IS) Parameters: VORTEX provides the user with the option of creating up to ten 
“Individual State” parameters that define characteristics of individuals. These state parameters may 
represent any feature of the organism that can be specified or coded by a numeric value. For example, 
dominance status might be encoded as Dominant = 1.0; Subdominant = 2.0; and Subordinate = 3.0. Or a 


VORTEX Version 9.50 User’s Manual 
40 Chapter 3 
The Data Input Process 
state variable might be used to represent some measure of body condition. Or two state variables might be 
used to track the x and y coordinates of each individual’s location on a landscape.  
 
To create one or more individual state variables, check the box, then indicate how many variables you 
will be creating. For each variable, you then enter into the table a label, which can be any text that will 
help you to remember what parameter you were representing. The VORTEX program, however, will track 
the Individual State variables with the labels IS1, IS2, etc., as indicated in the first column of the table.  
 
For each IS variable, you need to enter three functions (or constants) to define: (a) an initialization 
function (Init fn) – the starting value for each individual at the beginning of the simulation; (b) a birth 
function (Birth fn) – the value for each newborn individual; and (c) a transition function (Transition fn) – 
the change in state (if any) each year of the simulation. These functions are entered in the same way as 
other functions that can be used to specify demographic rates (see Chapter 6).  
 
 
Meta-model linkages to other programs: VORTEX provides the capacity to run the population simulation 
simultaneously (functionally in parallel) with one or more other models that might describe the dynamics 
of parts of an overall system. (See Miller and Lacy 2003b for a discussion of the concept of meta-
models.) For example, an epidemiological modeling program, OUTBREAK, can model the dynamics of an 
infectious disease in the population. VORTEX and OUTBREAK can be run at the same time on the same 
simulated population, with VORTEX simulating demographic and genetic changes and constantly 
informing OUTBREAK of the current census of the population, while OUTBREAK models the changes of 
disease state (susceptible, latent infected, infectious, recovered) and constantly informs VORTEX which 
individuals are in each state. The disease states can then be used to modify reproduction, survival, 
dispersal or other demographic rates for individuals in the meta-model. OUTBREAK was developed by JP 
Pollak (of visualbiosystems) in collaboration with the CBSG. The program is available at 
http://www.vortex9.org/outbreak.html. 
 
Case III:  
Using an Individual State Variable to model transmission of mitochondrial DNA 
haplotypes 
 
Mitochondrial DNA haplotypes are inherited from the maternal parent. This matrilineal transmission 
can be modeled by creating an Individual State Variable (IS1, labeled “mtDNA”). To assign randomly 
one of 10 haplotypes (encoded 1 through 10) to the founder individuals, specify a Initialization 
Function of “=CEIL(RAND*10)”. The maternal inheritance is defined simply with the birth function of 
“=IS1”, because the individual state parameters for use in the birth function are set at birth to be 
the values from the maternal parent (pending redefinition in the birth function). In the absence of 
mutation, the transition function also would be “=IS1”, to preserve the value for each individual 
across years. To model mutation to one of the original haplotypes, with mutation rate 0.0001, the 
transition function could be set to “=(RAND< 0.00011)*(CEIL(RAND*10))”. The mutation rate used 
in the function has to be elevated by 10% to account for the cases in which mutation would be to 
the existing haplotype, leaving the value unchanged.  
 
Once the mtDNA haplotype is defined as an individual state variable, demographic rates can be 
specified to be functions of an individual’s haplotype. The final frequencies of haplotype will not be 
tallied by VORTEX (because VORTEX doesn’t even know that the Individual State Variable you created 
is a categorical variable). However, you can obtain a complete listing of all individuals at the end of 
the simulation, including their state variables, by selecting the Special Option (from the Project 
Settings screen) to “Produce a file of all living individuals at the end of each iteration.” You can then 
analyze those data in whatever spreadsheet or other utility software you prefer.  


 
VORTEX Version 9.50 User’s Manual 
 
41 
Chapter 3 
The Data Input Process 
Another program that has been developed by JP Pollak is SPATIAL. SPATIAL simulates the movement of 
animals on the landscape, and it too can be linked to VORTEX as a meta-model. SPATIAL can be used as a 
tool to link VORTEX to GIS models of habitat suitability and landscape change. SPATIAL is still under 
development (www.visualbiosystems.com/spatial.html ).  
 
VORTEX also provides the capability for a user to create (or otherwise obtain) his or her own model and 
link it to VORTEX as a dynamic, multi-component meta-model. Full explanation of the proper use of meta-
models is beyond the scope of this manual, and users are strongly cautioned to not expect to be able to 
build and use meta-models without the assistance of an expert. Lacy and Miller (2002) and Miller and 
Lacy (2003a, 2003b) discuss the conceptual need to link PVA models with other kinds of knowledge, and 
the methods that might be used to develop such meta-models.  
 
In order to use VORTEX as a component of a meta-model, linked to OUTBREAK, SPATIAL, or any other 
program, you need to have XML capabilities installed on your computer. The installation package for the 
XML system files is available for free from the Microsoft website, and is also provided at 
www.vortex9.org/msxml.msi.  
 
Dispersal Among Populations 
 
This next section of input (Figure 22) is accessible only if you specified (in the Scenario Settings) that 
your Scenario is to have more than one population. If you are modeling a metapopulation, you now need 
to specify a few parameters that help to define the system of dispersal of individuals among populations, 
and the rates of dispersal of individuals between populations. 
 
Dispersing classes  
 
Age Range – Youngest and Oldest:  In these boxes, enter the youngest and oldest ages of those individuals 
that move between populations. If both sexes are capable of moving between populations, and the ages at 
which males and females disperse are different, you must decide which age(s) you use for these fields. 
This decision will be based largely upon how conservative you want to be about your estimation of 
potential risk. For example, if males begin moving among populations at 3 years of age and females at 5 
years of age, entering 3 as the youngest age to disperse may underestimate the risk of population decline 
and/or extinction since females are allowed to move at an earlier age in the model. (It is possible to 
specify different rates of dispersal for the two sexes, or for different age classes, by using the Dispersal 
Modifier Function, described below.) 
 
Dispersing Sex(es):  Check the appropriate box(es) to specify whether males, females, or both can 
disperse from the natal population. 
 
Percent Survival of Dispersers:  Often, dispersal among populations occupying discrete areas of suitable 
habitat is dangerous. Traversing the matrix of unsuitable habitat between populations may expose an 
individual to additional risks of predation or lack of food, and entry into a new population may require 
competition with the established residents. Enter here the survival rate (as a percent) of individuals that 
are dispersing between populations. The dispersal mortality is imposed separately from other mortality 
detailed elsewhere in the program. (More specifically, this dispersal mortality is imposed after annual 
mortality. See Appendix IV for a detailed description of VORTEX program flow.) A dispersal survival rate 
of 80% means that there is a 20% chance that an individual will die during the process of moving from 
population A to population B. 
 


VORTEX Version 9.50 User’s Manual 
42 Chapter 3 
The Data Input Process 
 
Figure 22. Dispersal input section. 
It is important to remember that while most input data should be in the form of 
percentages, a few others are input as proportions. Check the labels and 
prompts for clarification of the required data format. 
 
Dispersal Modifier Function: Dispersal patterns can be very complex and determined by many factors. 
VORTEX does not provide a full model of dispersal across complex landscapes, but instead models 
movements among discrete populations, with the user specifying the rate of movement between each pair 
of populations (as you will do in a later Input section). However, this box provides you with the 
opportunity to customize dispersal, in perhaps very complex ways. Any function entered here will be used 
as a modifier of the rates to be entered later. For example, you could cause dispersal of males to be twice 
as high as the specified rate (and twice as high as for females), by entering “=D*(1+(S=’M’))”. The 
parameter ‘D’ in the equation stands for the specified dispersal rate between any two populations. Such 
dispersal modifier functions can be used to cause dispersal to be dependent on sex, age, inbreeding, 
population density, and many other characteristics of the individuals and populations.  
 


 
VORTEX Version 9.50 User’s Manual 
 
43 
Chapter 3 
The Data Input Process 
With respect to dispersal or other aspects of population dynamics, the standard VORTEX model 
may not match precisely the behavior of your species. Often, the differences between the model 
and reality will not cause substantial differences in long-term population dynamics and risk. 
(Although definitive confirmation of this assumption may require testing a more complex and 
complete model to see if the refinements do matter.) In many cases, VORTEX does provide the 
capability to create models that are more complex – sometimes much more complex! – than the 
standard VORTEX model. These more complex population models are built by using functions 
rather than constants for input values. Using such functions provides considerable flexibility, but 
you should use them cautiously if you are not yet fully familiar with the VORTEX model.  
 
Dispersal Rates 
 
In the grid at the bottom of this screen, you enter dispersal rates to specify the probability that a given 
individual of the appropriate age-sex class will disperse from population A to population B in a specific 
year. That is, a rate of 1.00 indicates a 1% probability that an individual will migrate from population A to 
population B. Equivalently, if a population consists of 100 one-year old females with a dispersal rate 
between two populations of 1%, then one of these females would, on average, be expected to disperse in 
that direction in any given simulation year. 
 
Dispersal rates need not be symmetric among populations; enter whatever probability you deem 
appropriate for each pair of populations. Enter 0 to indicate no exchange of individuals between a pair of 
populations. The values on the diagonal of the grid – the percents of individuals that do not disperse each 
year – is automatically calculated by the program so that the rows will sum to 100%. 
 
In the Dispersal Rates section of the screen are four commands that can make it easier to enter dispersal 
rates. “Import Rate Matrix” allows you import the grid values from a semi-colon delimited text file. This 
file can be created in Excel or whatever software you choose. It must contain values for all cells of the 
grid, including the labels (although the labels in the file will be ignored and will not over-write what 
shows on the screen). The easiest way to see the format of the rate matrix file is to select “Export Rate 
Matrix”, and then look at the file that was created. With these commands, you can create a large matrix in 
a spreadsheet program, and then import it into VORTEX, and you can export rate matrices for modification 
or for re-use in other VORTEX projects. When you have only a few populations, these commands are 
usually not worth using. However, if you have, for example, 40 populations, you very well may want to 
use Excel to generate your dispersal rate matrix rather than typing in all 1560 pairwise dispersal rates! 
 
Another command allows you to apply a multiplier to each non-diagonal cell in the grid. By entering a 
value and hitting “Apply Multiplier of ” you can shift all of the dispersal rates upwards or downwards. 
This makes it much easier to test a range of dispersal rates across Scenarios of your Project. For example, 
you might enter an initial set of rates, and then apply multipliers of 0, 2, and 4 in order to test no 
dispersal, and 2x, and 4x increases in dispersal. The fourth command (“Fill Matrix with”) in this section 
lets you quickly fill the non-diagonal elements of the matrix with some constant dispersal rate. This 
makes it easy to set up a meta-population with a uniform rate of dispersal among all pairs of populations.  
 
VORTEX provides you with significant flexibility in defining dispersal rates for individuals within a 
metapopulation. That is, rates may be inversely proportional to distance, directly proportional to habitat 
area, or they may be defined through a more complex determining function. However, you have the task 
of calculating these rates for each pair of populations—VORTEX does not calculate them for you based on 
a set of internal rules. A considerable body of literature exists on the methods for estimating dispersal 
rates between populations. Capture-recapture studies can provide some of the best data for this process of 
estimation, although experimental difficulties do exist (see Ims and Yoccoz (1997) for more information). 
An example of estimating dispersal rates from molecular data is described in Case Study IV. 


VORTEX Version 9.50 User’s Manual 
44 Chapter 3 
The Data Input Process 
 
Reproductive System 
 
Monogamous, Polygamous, Long-term Monogamy, or Long-term Polygamy:  VORTEX models breeding 
systems as monogamous vs. polygamous, and short-term vs. long-term. With monogamous breeding, 
there must be a male for every breeding female; males may therefore become a limiting factor restricting 
breeding. In polygamous models, there only needs to be at least one male for all females to have an 
opportunity to breed. However, in a later section (Mate Monopolization) you can specify that only a 
subset of males have opportunities to breed. For example, you can create a polygynous system in which 
some males control harems of typically 5 females, while the remaining males are excluded from breeding.  
 
If you do not choose a “Long-term” option, then VORTEX will assume that mates are randomly reshuffled 
each year and that all available individuals have an equal probability of breeding. If you do specify one of 
the “Long-term” models, then once pairs are formed, those pairs will remain together across years of the 
simulation until either the male or the female dies or disperses to a different population. Demographically, 
it will not matter whether you choose long-term pairings or re-arrangement of pairs each year. 
Genetically, there may be a small effect on the rate of loss of genetic diversity from the population.  
 
VORTEX does not fully customize the details of mating systems because of the complexities of considering 
a wide variety of species and their particular characteristics. More complex breeding systems can 
substantially impact genetic variation, but are less likely to seriously alter the demographic performance 
of a population. In the future, VORTEX will also allow you to model a species with hermaphroditic 
breeding—that is, a species in which each individual is both male and female and can therefore 
potentially mate with any other individual, including itself. Presently, this option is not yet enabled. 
 
Age of First Reproduction for Females (and Males):  VORTEX defines breeding as the time when the first 
offspring are born, not the age of onset of sexual maturity or the age of first conception. The program also 
assumes that breeding (and, for that matter, all other events) occurs at discrete intervals—usually years, 
but this can be described in terms of whatever you have defined as a suitable time cycle. Thus, breeding 
age must be entered as an integer value; you cannot enter 2.5 years as the first age of breeding but must 
enter either 2 or 3 years. In addition, you should enter the median age of first breeding, not the earliest 
age ever observed since the earliest observed age may not be typical of the normal population behavior. 
Case Study IV:  
Estimating migration rates from DNA sequence data 
 
The Anacapa Island deer mouse (Peromyscus maniculatus anacapae) is endemic to the Anacapa 
islands off the coast of California near Los Angeles. Pergams et al. (2000) conducted a population 
viability analysis to develop a comprehensive management plan involving the potential for captive 
breeding, reintroduction, or translocation of individuals following eradication of introduced rats. 
 
Nucleotide sequences were obtained from the mitochondrial DNA (mtDNA) cytochrome oxidase 
subunit II gene of mice sampled across each of the three Anacapa Islands. Based on the average 
amount of nucleotide sequence divergence among mice from the different islands, the authors were 
able to directly calculate an estimate of gene flow, Nm, where N is the average size of a pair of islands 
and m is the average rate of migration between those islands per generation (see Nei 1982 for 
details). For example, Nm between Middle and West Anacapa was calculated to be 7.27 individuals per 
generation. Since a generation in Anacapa Island deer mice is only 84 days, and assuming a time 
cycle of 21 days for the analysis, the number of individuals migrating between the two islands is 
(7.27)(0.25) = 1.8175 per time cycle. The average population size across Middle and West Anacapa 
Islands was estimated to be 19,044 mice, so the migration rate is then calculated to be 
1.8175/19,044 = 0.0000954. Finally, the authors assumed a symmetrical pattern of migration, so that 
the estimate of the rate of migratin from Middle to West Anacapa (equivalent to that from West to 
Middle Anacapa) is (0.5)(0.0000954) = 0.0000477. 


 
VORTEX Version 9.50 User’s Manual 
 
45 
Chapter 3 
The Data Input Process 
 
Figure 23. Reproductive System input section. 
 
 
Case Study V:  
Estimating age of first breeding in males and females 
 
The babirusa (Babyrousa babyrussa) is one of the more interesting endemic mammals on the 
Indonesian island of Sulawesi. Individuals in captivity can reach sexual maturity as early as 5 
months of age. However, most captive animals approach the age of one year before reaching sexual 
maturity. Even at this age, the animals are quite small and it is considered unlikely that they will 
reproduce until they are older than one year of age. Taking into account the gestation length of 
about 5 months (usually 155 – 158 days), it is likely that female babirusa in the wild will have their 
first litter at the age of 2 years. On the other hand, males of this age will have to deal with strong 
competetion for mates among older and stronger males. Consequently, Manansang et al. (1996) 
developed VORTEX models for this species in which the age of first breeding among males was 
estimated to be delayed until 4 years.  


VORTEX Version 9.50 User’s Manual 
46 Chapter 3 
The Data Input Process 
Maximum Age of Reproduction: VORTEX assumes that individuals can breed at a rate typical for that 
species throughout their adult lifespan. If your species does not reproduce throughout its entire adult life, 
do not enter the species’ maximum life expectancy. For example, humans typically reach reproductive 
senescence before they die. In this case, if the typical life expectancy is 70 years but they cease 
reproduction at 50 years, then enter 50 as the maximum breeding age.  
 
Maximum Number of Progeny per Year: Enter the most individuals born to a given female during a year 
(time cycle). If your species produces more than one set of offspring (in the form of litters, clutches, pods, 
etc.) per year, but you are using a year as your time cycle, add each set together and then enter the total 
number born during the year. You can enter the maximum number that has ever been recorded—even 
though such an event may be quite rare—and later on during the data input process you can then assign a 
low probability of occurrence to this maximum value. 
 
You have the option of entering a mean and standard deviation for the distribution of offspring numbers, 
rather than specifying the percentage of females producing each possible number of young (see below). 
This removes the limitation on the size of offspring numbers that can be modeled, and therefore makes it 
much easier to model species with high fecundities. To choose this option, enter 0 for the maximum 
number. Subsequent screens will allow you to specify the nature of this normal distribution. 
 
When annual offspring numbers per female are not large—for example, five or 
fewer—it is recommended to specify the exact distribution, rather than using the 
optional normal distribution. 
 
 
Sex Ratio at Birth: Enter here a number between 0.0 and 100.0 to represent the average percentage of 
newborn offspring that are male. This number is typically very near 50%, signifying a roughly equal 
Case Study VI:  
Modeling species with high fecundity 
 
The distribution of the winged mapleleaf mussel (Quadrula fragosa) has been reduced to only a few 
sites in the St. Croix River between Minnesota and Wisconsion in the United States. As is typical of 
nearly all freshwater bivalves, this species reproduces by broadcasting a large number of larval 
offspring known as glochidia into the water column. Kjos et al. (1998) estimated that an adult 
female mussel produced a mean number of 171,000 glochidia in a typical breeding cycle. Only those 
glochidia that locate and encyst within the gills of its host fish, excyst following metamorphosis, and 
then settle onto suitable substrate on the river bottom will survive to the subadult age class.  
 
Because of the impossibility (at least with today’s computer systems) of tracking such a large 
number of individual offspring, VORTEX cannot normally deal with such high levels of fecundity. 
However, this situation can be made much more tractable by simply redefining what is meant by 
“reproduction”; instead of defining it in terms of the production of glochidia, we can define it as the 
number of individuals that successfully settle onto suitable river-bottom substrate. Kjos et al. (1998) 
estimated that only about 0.2% of the glochidia find and successfully encyst onto a host, that about 
15% of those successfully metamorphose and excyst, and about 20% of those excysted juveniles 
settle onto suitable substrate. In other words, 
 
Final brood size = [171,000 glochidia]×[0.002 encyst]×[0.15 excyst]×[0.2 settle] = 10 
 
By condensing a series of mortality events from the very early stages of the mussel’s life cycle, the 
authors were able to define a system of reproduction that was amenable to the VORTEX modeling 
system. Other types of organisms that would benefit from this type of simplification include 
amphibians, fish, and even insects. 


 
VORTEX Version 9.50 User’s Manual 
 
47 
Chapter 3 
The Data Input Process 
male:female sex ratio at birth. If relatively more or fewer males are born to a given female per year, enter 
the appropriate percentage (e.g., 55 for 55% males). 
 
Density Dependent Reproduction: Does the reproductive rate of your species change with changing 
population size? That is, is reproduction low when the population is small due to a difficulty in finding 
mates or, conversely, does reproduction drop off when the population is large (more specifically, at high 
density) due to limited resources or territories, intraspecific competition, crowding, stress, etc.? If so, 
check the box and then enter the subsequent parameters defining the nature of the density dependence.  
 
If your population’s reproduction is density dependent, you will need to model this relationship. VORTEX 
models density dependence with an equation that specifies the proportion of adult females that reproduce 
as a function of the total population size. Normally, the proportion of females breeding would decrease as 
the population size becomes large. In addition, it is possible to model an Allee effect—a decrease in the 
proportion of females breeding at low densities due, for example, to difficulty in finding mates. The 
equation that VORTEX uses to model density dependence is: 
 
in which P(N) is the percent of females the breed when the population size is N, P(K) is the percent that 
breed when the population is at carrying capacity (K, to be entered later), and P(0) is the percent of 
females breeding when the population is close to zero (in the absence of any Allee effect). The exponent 
B can be any positive number and determines the shape of the curve relating the percent breeding to 
population size, as the population becomes large. If B = 1, the percent breeding changes linearly with 
population size. If B = 2, P(N) is a quadratic function of N. Figure 24A shows representative density-
dependence curves for different values of B in the absence of an Allee effect. 
 
The term A in the density dependence equation defines the magnitude of the Allee effect. One can think 
of A as the population size at which the percent of females breeding falls to 50% of its value in the 
absence of the effect (Akçakaya 1997). Figure 24B shows several density-dependence curves for different 
values of A with a steep decrease in breeding at high densities (B = 8). Figure 24C gives the same curves 
as in Figure 24A, but with the addition of an Allee effect (A = 1). 
 
By inspecting the density-dependence equation, one can see that when the population is at carrying 
capacity, P(N) = P(K). When the population is very small (N is near 0), then P(N) = P(0) if there is no 
Allee effect. It is also apparent that the Allee effect term [N / (N + A)] will have a strong impact on the 
value of P(N) when N is small. When N is much larger than A, the Allee term will have very little effect 
on the value of P(N). Fowler (1981) provides a review of density-dependence functions and presents 
some density curves for large mammals. We have chosen to model density dependence using the equation 
given above because it provides the user with considerable flexibility—despite its relatively simple 
formulation. Fowler (1981) suggests that density dependence in reproductive success can often be 
modeled quite well with a quadratic function, that is, with B = 2. 
% Adult Females Breeding per Year [P(N)]
10
20
30
40
50
60
70
80
90
100
B = 16
B = 0.25
0.5
1
2
4
8
P(0) = 80%; P(K) = 40%; K = 100; A = 0
Population Size (N)
10
20
30
40
50
60
70
80
90
100
P(0) = 80%; P(K) = 40%; K = 100; B = 8
A = 0
0.5
1
2
A = 4
Population Size (N)
0
10
20
30
40
50
60
70
80
90
100
% Adult Females Breeding per Year [P(N)]
0
10
20
30
40
50
60
70
80
90
100
B = 16
B = 0.25
0.5
1
2
4
8
P(0) = 80%; P(K) = 40%; K = 100; A = 1
A
C
B
Figure 24. Plots of the default density 
dependence relationship as used by 
VORTEX in the absence of an Allee 
effect (A = 0; panel A), in the 
presence of a steep decrease in 
breeding success at high population 
densities (B = 8; panel B), and both a 
steep decrease in breeding success 
at high population densities and an 
Allee effect (A = 1 and B = 8; panel C). 
( )
A
N
N
K
P
P
P
N
P
B
K
N
+
−
−
=
])
))
(
)
0
(
[(
)
0
(
(
)
(


VORTEX Version 9.50 User’s Manual 
48 Chapter 3 
The Data Input Process 
 
It is best to derive the values of P(0), P(K), A, and B from a regression analysis of data on the breeding 
rate of your population. If these data are unavailable, but you can estimate P(0) and P(K), then you may 
want to explore several different combinations of A and B to come up with a curve that seems appropriate 
for your population. You could use graphics or statistical software—or even graph paper and a 
calculator—to construct a range of hypothetical curves, using different combinations of parameters, as 
was done to produce Figure 24. In any event, once you have decided on a particular set of parameters to 
use you should always graph the resulting curve to verify that it represents the mode of density-dependent 
behavior you are looking for. After you have entered the appropriate parameters as shown on Figure 25 
below, VORTEX can display a graph of the specified density dependence function for you so that you can 
verify the intended nature of the relationship. Select the population from the drop-down list and then hit 
the “View” command to see your graph. (Note: you will want to specify at the bottom of the graphing box 
that you want to plot the function against the ‘N’ parameter.) 
 
Depending on the shape of the density dependence curve you have specified, and the mortality 
rates you will enter later, your population may never be able to reach the carrying capacity K (also to 
be specified later). The combination of density-dependence in both reproduction and survival will 
determine over what range of sizes the population is expected to experience average net growth 
and over what range it would be expected to decline due to deaths outnumbering births. 
 
 
 
Figure 25. Specifying and graphing density dependence. 
 


 
VORTEX Version 9.50 User’s Manual 
 
49 
Chapter 3 
The Data Input Process 
 
 
Reproductive Rates 
 
The next section of input (Figure 27) asks for parameter values that specify reproductive rates. Note that 
you decide when in the development of the next generation the “birth” is defined to occur. For mammals, 
you would probably use parturition as the point at which offspring are tallied. For oviparous species, 
however, you can start to tally offspring at egg-laying, or at hatching, or at fledging, or at any other 
developmental stage that makes sense to you and for which you can specify the demographic rate 
parameters. For amphibians, you may choose to start each animal’s life in the VORTEX model at 
metamorphosis. Whenever you define an individual’s life to begin, you must make sure that the first year 
mortality rates you specify in the next input section are appropriate for the choice you made about when 
to start recording offspring. For example, if you tally offspring starting at hatching, then the clutch sizes 
you specify on this screen will be in terms of the number of hatches, and your first year mortality will be 
from hatching through the subsequent 12 months. If you choose to start offspring at fledging, then the 
clutch size will be specified in terms of the number of fledglings, and survival will be from fledging 
onwards.  
Case Study VII:  
Modeling density dependence in reproductive success 
 
Peary caribou (Rangifer tarandus) are distributed in fragmented populations across the Canadian 
Arctic. These animals are continually stressed by food resource limitation in the harsh winter 
climate, with this stress becoming magnified as population density increases. Consequently, a risk 
analysis conducted on this taxon (Gunn et al. 1998) included density-dependent reproductive 
success at high population densities (Allee effects were not considered to be a factor). Field data 
show 80% of adult females are able to breed under optimal density conditions, while only 10% are 
expected to be successful when the population reaches carrying capacity. In other words, P(0) = 
80% and P(K) = 10%. To approximate the expected shape of the density dependence curve 
modeled in VORTEX, the exponential steepness parameter B was set to 4. The functional form of this 
relationship is shown in the top panel of Figure 26. 
 
In contrast, the winged mapleleaf mussel (Quadrula fragosa)  
inhabits isolated stretches of the St. Croix River in Minnesota  
and Wisconsin (United States), with individuals separated  
from one another by as much as 20-25 meters. While no  
evidence points to a suppression of reproductive success at  
higher densities, the mode of reproduction in these mussels  
suggests that Allee effects may play a major role in 
influencing reproduction as population size (and density)  
declines (Kjos et al. 1998). In fact, reproductive success is  
thought to drop off rapidly as populations are reduced to  
below about 30% of the estimated carrying capacity. To  
model this phenomenon , P(0) =, P(K) = 19.4%, and A = 4  
(the exponential steepness B is set to zero when  
reproductive success is unaffected at high densities). This  
relationship is shown in the bottom panel of Figure 26. 
Population Density, (N/K)*100
0
10
20
30
40
50
60
70
80
90
100
% Females Producing Brood
0
4
8
12
16
% Females Producing Calves
0
10
20
30
40
50
60
70
80
90
Peary Caribou (Rangifer tarandus)
Winged Mapleleaf Mussel (Quadrula fragosa)
Figure 26. Density dependence functions as 
modeled in VORTEX for Peary caribou (top panel: 
Gunn et al. 1998) and the winged mapleleaf 
mussel (bottom panel: Kjos et al. 1998).  


VORTEX Version 9.50 User’s Manual 
50 Chapter 3 
The Data Input Process 
 
Figure 27. Reproductive Rates input section. 
 
% Adult Females Breeding:  Here you specify the mean percentage of adult females that breed in a given 
year (or, stated another way, the probability that a given adult female will successfully produce offspring 
in a given year). Data on the interbirth interval, or the timespan between successive birth events for a 
given female, can be useful for estimating the percentage of adult females breeding annually. A simple 
example: if the average length of time between successive births for adult females is 2 years, then 50% of 
all adult females are expected to breed in a given year (this assumes, of course, that animals can breed 
throughout their normal lifespan). A more detailed example is presented below in Case Study VIII.  
 
EV in % Breeding:  Environmental variation (EV) in reproduction is modeled by the user entering a 
standard deviation (SD) for the percent females producing litters of offspring (see Box C for a refresher 
on some basic concepts in statistics and their calculation). VORTEX then determines the percent breeding 
for a given year by sampling from a binomial distribution with the specified mean and standard deviation.  
 
 


 
VORTEX Version 9.50 User’s Manual 
 
51 
Chapter 3 
The Data Input Process 
 
 
Although environmental variation in birth and death rates can have a substantial impact on the viability of 
a population, it is often difficult to obtain the data needed to estimate EV. Long-term field studies are 
needed in order to determine the amount of fluctuation that occurs in the demographic rates of your 
Case Study VIII:  
Using interbirth intervals to estimate annual % adult females breeding 
 
In a risk assessment for the Ugandan population of the eastern subspecies of chimpanzee Pan 
troglodytes schweinfurthii, Edroma et al. (1997) used interbirth interval (IBI) data from a number of 
well-studied populations in Uganda and neighboring countries. The mean IBI for these populations 
was set at 5 years. However, the early death of an infant will cause the IBI for a given female to 
shorten dramatically. Data suggest that if an infant dies at 6 months of age, the IBI will be reduced 
to about 2 years. This rapid response means that the effect of infant mortality on population growth 
may be quite small, so long as the mother is not killed or harmed by the same forces responsible for 
the death of her infant. In addition, infant mortality was set at 16%, and the frequency of non-
sterile females in the population was estimated at 91%. Given these data, a corrected interbirth 
interval can be calculated as: 
(
)( )
(
)( )
97
.
4
91
.
0
2
16
.
0
5
84
.
0
=
+
=
corr
IBI
 
Based on this estimate of the interbirth interval, the percentage of adult females producing an 
offspring in a given year is (4.97)-1 = 20.1%. 
Box E: A Quick and Easy Way to Estimate a Standard Deviation 
from Scant Data 
 
Ideally, to estimate the standard deviation of a demographic rate across years, we would want to 
have many years (perhaps 10 or more) of field data. However, we often have information on just a 
few years, and often only the best and worst years in recent times. Fortunately, the expected range 
observed in a sample of n values from a normal distribution can be specified (see below, and Rohlf 
and Sokal 1981). To estimate the standard deviation of a distribution, the observed range (best – 
worst years) can be divided by the expected range. For example, across 15 years of observations on 
Sonoran pronghorn antelope (Hosack 1998), the mortality rate of fawns was 85% in the worst year 
and 55% in the best year. Dividing the observed range (30%) by the expected range for a normal 
distribution (3.47 SD units), provides us with an estimate of the SD of 30% / 3.47 = 8.64%. 
Number of observations 
Range 
2 
1.13 
3 
1.69 
4 
2.06 
5 
2.33 
6 
2.53 
7 
2.70 
8 
2.85 
9 
2.97 
10 
3.08 
15 
3.47 
20 
3.74 
25 
3.93 
30 
4.09 
40 
4.32 
50 
4.50 
Table E-1. Mean ranges (in SD units) for 
samples of a normal distribution (from Table 26 
in Rohlf and Sokal 1981)


VORTEX Version 9.50 User’s Manual 
52 Chapter 3 
The Data Input Process 
population. If these data are available, the standard deviation in mean birth rate can be simply calculated 
using the methods in Box C. If your dataset is small but you are comfortable with making a rough 
quantitative estimate of the variability, you can use the technique presented in Box E. 
 
A common problem in estimating annual fluctuations in demographic rates is that the data might be so 
sparse that it is difficult or impossible to estimate the parameters on an annual basis. If this is the case, 
you might be forced to admit that the data are not sufficient to allow estimation of the variability around 
the mean values. The only alternatives are to guess at the fluctuations in reproductive and mortality rates, 
based on a general understanding of the natural history of the species, or to omit environmental variability 
from the model altogether (by entering 0 when each standard deviation is requested). In this case, you 
must recognize that a potentially important component of population variability and instability is being 
ignored in your analysis. 
 
Another difficulty with these approaches, which may add a significant bias if sample sizes are small, is 
that some of the year-to-year variation observed in reproductive and mortality rates is actually due to the 
expected demographic stochasticity resulting from random sampling of individuals, even if environmental 
factors do not cause fluctuations in the annual probabilities of birth and death. Refer to Box D for 
methods of removing this source of variation as a means of estimating EV alone. 
 
In order of ease of use (easiest to most difficult) and precision (least precise to most precise), 
your options for estimating environmental variation (EV) in population demographic rates are: 
guess at the “typical” fluctuations in your species’ reproduction and mortality rates; calculate the 
variation across years in these rates from long-term field data; adjust the observed variation by 
subtracting the variance due to demographic stochasticity (random sampling), even if the 
probabilities of birth and death remain constant through time. 
 
Use Normal distribution approximation/Specify exact distribution: Previously, you defined the maximum 
number of offspring produced annually per female; you are must now specify the percentage of 
litters/clutches/broods produced by the breeding adult females that are of a given size. You have two 
options for specifying the distribution of numbers of progeny. You can use a Normal distribution 
approximation or you can fully specify the probabilities of each number of progeny. When you use the 
Normal approximation, VORTEX will randomly select a number of progeny for each breeding female by 
sampling from a normal distribution with the specified mean and standard deviation, and then choosing 
the closest whole number of offspring to the value sampled. The distribution will be symmetrically 
truncated, if necessary, in order to prevent the specification of negative litter sizes and to prevent bias in 
the sampling of the distribution. 
 
If you have data on the percents of females producing each possible number of progeny, and if the 
maximum number produced is not very large, then it is more accurate to enter that exact distribution. You 
accomplish this by entering the percentage (i.e., a number between 0.0 and 100.0) for each specified size 
up to the maximum. For example, if the maximum litter size is 5 but the average litter is comprised of just 
2 individuals, you would enter a much higher percentage of females producing smaller litters (say, 60% 
produce a litter of 2 but only 5% produce a litter of 5). The total must add to 100%, and the final value 
will be entered automatically by the program in order to sum to 100%. 
 
Copy input values from:  When modeling a metapopulation, you often will want to use the same 
values for most input parameters across all of the populations. On the left side of the Simulation 
Input screens is a tool that allows you to copy input values from any one population to all 
subsequent populations. You can copy only those values in the current Section of input, or copy 
values in all the input Sections.  


 
VORTEX Version 9.50 User’s Manual 
 
53 
Chapter 3 
The Data Input Process 
 
Mortality 
 
In this next section of input (Figure 28), you enter the age-sex specific mortalities. In the language of 
matrix life-table analysis (e.g., Caughley 1977; Caswell 2001), VORTEX defines mortality as the mortality 
rate qx, or the percentage of animals alive at age x that die before reaching age x + 1. Enter mortality rates 
as a percent (between 0 and 100) for each age-sex class. Once reproductive age is reached, the annual 
probability of mortality remains constant over the life of the individual and is entered only once (but see 
Chapter 6 for further information on how to relax this assumption). 
 
Mortality of Females (Males) as %:  In these tables, enter the mean mortality rates for each age class, and 
enter also a standard deviation (SD) for each mean to describe the environmental variation (EV) in each 
rate. For information on the calculation and statistical treatment of variance in demographic parameters 
used in VORTEX, see Boxes C and D. 
 
 
Figure 28 Mortality Rates input section. 


VORTEX Version 9.50 User’s Manual 
54 Chapter 3 
The Data Input Process 
 
Be aware that if you enter a standard deviation for each mean mortality rate that is at least half of 
the survival rate (100% - mortality rate) – in other words, the coefficient of variation in survival is at 
least 50% – in occasional years the mortality rate will be set at 100% and the population will 
immediately go extinct. For example, if all age-specific mortality rates are 50% and the standard 
deviations are set at 25%, then in about 1 in 40 years the mortality rate after adjustment for EV will 
be 100% (since the rate will exceed the mean by 2 standard deviations about 2.5% of the time). 
 
 
A substantial literature exists on the many methods by which one can estimate age-sex specific mortality 
rates in wild populations; Caughley (1977) is a good text from which to start an exploration of this body 
of information. 
 
Catastrophes 
 
In the next section of input (Figure 29), you enter data to characterize catastrophes that might strike your 
populations. Note that you must do this for each type of catastrophe you identified (back in the Species 
Description section) across each population comprising your metapopulation (if you are modeling more 
than one population). You toggle among the types of catastrophes by clicking on the buttons arrayed 
across the top of the Catastrophes window.  
 
Don’t forget to enter data for Catastrophe 2 (if any) and all further catastrophes 
after you have completed entering data for Catastrophe 1. 
Case Study IX:  
Estimating mortality rates from sightings of banded Whooping Cranes 
 
As of 1991, the last remaining population of the whooping crane (Grus americana) could be tracked 
and censused from its breeding grounds in Wood Buffalo National Park (Alberta, Canada) to its 
wintering grounds along the Texas Gulf Coast at Aransas National Wildlife Refuge. During a 
Conservation Viability Assessment for this population, Mirande et al. (1991) estimated mortality 
rates for the population based on recorded sightings of banded birds. From 1976 through 1989, 
about 234.5 cranes were observed to hatch at Wood Buffalo NP (taking the midpoint of the possible 
range in those few years in which counts were imprecise), of which 172 arrived in Aransas the 
following winter. This yields an estimated juvenile survival rate of 73.3%. During the 14 years of 
close monitoring of the Wood Buffalo population, the observed variance around the mean 
survivorship of 0.733 was 0.047. The variance that would be expected from random binomial 
sampling based on this mean is 0.013. The difference (V = 0.034, or SD = 0.184) can be attributed 
to environmental variation. 
 
Mortality after the first year can similarly be determined from either data on banded birds of known 
age, or from winter census reports from Aransas filed since 1938 (young of the year are 
distinguishable from older birds upon arrival at Aransas). Since 1938, a total of 2359 birds older 
than 1 year of age returned to Aransas, out of a total of 2594 birds that departed Aransas the 
previous spring. This yields an estimated annual mortality after the first year of 9.06%. Among the 
banded birds, 89.9% annual survival was observed in 386 bird-years, but band loss after several 
years could have accounted for some of the “mortality” recorded among banded individuals. No 
variation was detectable statistically among mortality rates calculated separately for each age class 
beyond the first year. 
 
The observed annual variation in survival rates from 1938 to 1990 was V = 0.00255; the variation 
expected due to binomial sampling from a constant probability is V = 0.00220. The difference can be 
attributed to environmental variation in the probability of surviving, with V = 0.00035, or SD = 
0.019. This value turned out to be very close to the intuitive estimate provided by workshop 
participants – that annual fluctuations in mortality rates would be about ± 2%. 


 
VORTEX Version 9.50 User’s Manual 
 
55 
Chapter 3 
The Data Input Process 
 
Figure 29. Catastrophes input section. 
 
In the top grid on this screen, you can enter labels for each catastrophe, as a way to remind yourself and 
others what events you were modeling. 
 
Global/Local: Each catastrophe is to be specified as global or local in scope (this is applicable only when 
more than one population is modeled). You are given considerable flexibility in how the scope of each 
catastrophe is specified, so it is important to read the following information carefully in order to correctly 
model your metapopulation. 
 
A global catastrophe will occur in the same years in all populations, but the severity of effects can be 
entered as different or equal across populations. Local catastrophes occur independently among the 
populations. To cause a catastrophe to be regional in scope, affecting only a subset of the populations, 
you can specify that it is global, but then set the severity factors to 1.0 (see below) for those populations 
which are not affected by that regional catastrophe. 
 


VORTEX Version 9.50 User’s Manual 
56 Chapter 3 
The Data Input Process 
You may also specify that a catastrophe is global for some populations, but local for others. In that case, 
the catastrophe happens concurrently across the populations for which it is global, but occurs 
independently in those populations for which it is local. 
 
Normally, the frequency of a global catastrophe would be set to be the same in each population affected 
by that global catastrophe. However, you can specify different frequencies for a global catastrophe among 
the populations. When the catastrophe hits a population, it will also hit all other populations in which that 
catastrophe has at least as high a frequency of occurrence. The catastrophe will sometimes occur in the 
populations that have higher frequencies while not occurring in populations with lower frequencies. 
 
Case Study X:  
A “catastrophe sampler” 
 
1. Attwater’s Prairie Chicken 
The impact of hurricanes was assessed by Seal (1994) in a Population and Habitat Viability 
Assessment for Attwater’s prairie chicken (Tympanuchus cupido attwateri), an endangered bird 
that was reduced to just 3 disjunct subpopulations in coastal southeastern Texas. Based on data 
from the National Oceanic and Atmospheric Administration, it was assumed that hurricanes strike 
this area on average once every 70 years. Species biologists indicated that populations in Refugio 
County dropped from 1,200 – 1,500 in the spring prior to Hurricane Beulah to approximately 250 
in October following that storm. Therefore, it was assumed that catastrophic hurricanes would 
result in 80% mortality of the adult (post-fledging) population. This would translate into a 
severity factor with respect to survival of 0.20. Because hurricanes typically occur during late 
summer and autumn, it was assumed that such an event would not affect reproductive success 
as breeding occurs in the spring. 
 
2. Winged Mapleleaf Mussel 
Kjos et al. (1998) identified major upriver chemical spills as the primary catastrophe impacting 
the last surviving populations of the winged mapleleaf mussel, Quadrula fragosa. A chemical spill 
of this type could occur as a result of, for example, an accident involving a vehicle carrying 
hazardous materials. A detailed analysis by the Minnesota Department of Transportation suggests 
that the probability of such an event could be quite small (see Kjos et al. (1998) for a detailed 
description of the calculation). A very conservative estimate of the probability was set at 0.20%; 
i.e., it is thought to occur perhaps, on average, once every 500 years. However, if it were to 
occur, it would have major effects on the mussel populations: in the year that such an event 
occurs, both reproductive success (proportion of adult females breeding) and survival (spread out 
across all age classes) would be reduced by 30%, equivalent to a pair of severity factors equal to 
0.70.  
 
3. Mountain Gorilla 
The primary catastrophic event modeled by Werikhe et al. (1998) in their evaluation of mountain 
gorilla (Gorilla gorilla beringei) viability was the spread of disease from humans to gorillas. As the 
extent of human-gorilla interaction increases with rising human population pressures, the 
likelihood of passing human diseases to gorillas is thought to be markedly higher. Data from 
discussions with primate veterinarians at the PHVA Workshop led to the construction of the 
following major disease events: 
• Influenza-like disease – 10% annual probability of occurrence; 5% reduction in survivorship; 
no effect on reproduction 
• Severe, but not pandemic, viral disease – 10% annual probability of occurrence; 25% 
reduction in survivorship; 20% reduction in the proportion of adult females breeding 
• Hypothetical viral disease with chronic cyclicity, targeting the organ reproductive system – 4% 
annual probability of occurrence; 25% reduction in survivorship; 100% reduction in the 
proportion of adult females breeding (i.e., no reproduction during a catastrophe year). 


 
VORTEX Version 9.50 User’s Manual 
 
57 
Chapter 3 
The Data Input Process 
Frequency %:  Once the scope of the catastrophe is identified, you need to define the probability that a 
given catastrophe will occur in a particular year. Enter this as a percent from 0.0 to 100.0. For example, a 
value of 1.0 means that there is a 1% chance that this particular event will occur in any one year. Stated 
another way, a catastrophe given a frequency of occurrence of 1.0% means that, in a simulation lasting 
100 years, this event is expected to occur one time on average.  
 
Severity (proportion of normal values): For each catastrophe, you need to define the severity with respect 
to reproduction (percentage of adult females breeding) and survival. The fecundity and survival rates for 
years in which a catastrophe occurs are obtained by multiplying those rates in a “normal”, non-
catastrophe year by the specified factor. These severity factors range from 0.0 to 1.0. Entering 0.0 
indicates a total loss of reproduction or survival for the population and 1.0 means that the catastrophe, 
when it occurs, will have no effect. For example, entering 0.75 for the severity factor with respect to 
reproduction means that, if 50% of adult females breed in a normal year, then only (50%)(0.75) = 37.5% 
breed in a year with a catastrophe.  
 
Catastrophe severity factors greater than 1.0 can be used in your model. This would result in 
“catastrophes” having beneficial effects on reproduction and/or survival. 
 
 
Mate Monopolization 
 
You are now asked to specify the male breeding characteristics of your population. This information is 
important for those species that may have an established social structure and, consequently, exclude some 
adult males from the pool of available breeders. The look of this screen (Figure 30) will depend on 
whether you specified Monogamous or Polygamous breeding back in the Reproductive System section. 
If you previously specified that the breeding system in your population was polygynous, you must specify 
how many of the males are breeders. To describe the degree of polygyny, you will need to provide an 
value in one of the following three lines of the grid: 
 
a) % Males in Breeding Pool 
b) % Males Successfully Siring Offspring (producing at least one offspring in the average breeding 
cycle or year) 
c) Mean # of Mates/Successful Sire (the mean number of litters sired by successful males in each year) 
 
Whichever one of the three parameters you specify, VORTEX will calculate the other two values based on 
the assumption that some males are excluded from the breeding pool and breeding success among males 
in the pool of available breeders is described by a Poisson distribution. Only the top number is actually 
used in the simulation model; the other two are provided as alternative ways to enter the degree of 
polygyny.  
 
If you earlier specified that the species has a monogamous breeding system, you are asked specify only 
the percentage of the total adult male population that makes up the pool of available breeders (and each 
male can breed with only one female each year). Remember that not all males within this pool may breed 
in a given year, depending on the number of adult females that are successful breeders. 
 
 


VORTEX Version 9.50 User’s Manual 
58 Chapter 3 
The Data Input Process 
 
Figure 30. Mate Monopolization input section. 
 
Initial Population Size 
 
In this section of input (Figure 31), you specify the number of individuals at the start of your simulation.  
 
Stable Age Distribution/Specified Age Distribution: You have two options for entering initial population 
sizes. If you do not know the precise age-class distribution in your population (as is usually the case), you 
can initialize your population according to the stable age distribution (see Box G in Chapter 4 for a 
definition of and methods for calculating this distribution). If you select the stable age distribution, you 
then enter the total Initial Population Size for each population. VORTEX will assign individuals to each 
age-sex class proportionate to the stable age distribution, and will show that distribution in the grids. 
 
If instead you choose to enter a Specified Age Distribution, you will then enter the actual size of each age 
class for both males and females. You may need to use scroll bars to view the older age classes in the 
grids. As you enter these values, you will notice that the total initial population size changes accordingly. 


 
VORTEX Version 9.50 User’s Manual 
 
59 
Chapter 3 
The Data Input Process 
 
Figure 31. Initial Population Size input section. 
 
Carrying Capacity 
(see Figure 32) 
Carrying Capacity (K): The carrying capacity describes the upper limit for the size of your simulated 
population within a given habitat and must be specified by the user in this next section of input (see Box 
F for a more in-depth discussion of this parameter). If the population size N exceeds K at the end of a 
particular time cycle, additional mortality is imposed across all age and sex classes in order to reduce the 
population back to this upper limit. The probability of any animal dying during this truncation process is 
set to (N – K / N), so that the expected population size after the additional mortality is K.  
 
SD in K Due to EV: If you think that the habitat carrying capacity varies over time due to environmental 
variation (EV), you can enter a standard deviation (SD) here to account for this variability. For example, 
the habitat might support different population sizes in different years due to changing conditions such as 
rainfall or food resources. The standard deviation should be entered as a number of animals, not as a 
percentage of K; for example, if K = 2000 with a standard deviation of 10%, then enter 200. 


VORTEX Version 9.50 User’s Manual 
60 Chapter 3 
The Data Input Process 
 
Figure 32. Carrying Capacity input section. 
 
Be careful! If you enter a standard deviation for the carrying capacity that is greater than K/3, 
then the value for K could drop to zero during your simulation – resulting in an unwanted 
extinction event. If you’re not convinced, see Box C for an explanation of why this is so. 
 
Trend in K?  VORTEX allows you to simulate changes in the carrying capacity. Such changes may be 
positive or negative and result from human activities such as resource utilization or corrective 
management strategies, or from intrinsic ecological processes such as forest succession. To include a 
trend in carrying capacity, check the box. Then specify the time period during which the trend will occur, 
and the annual rate of change in K. The trend will begin in year 1 and continue for the specified duration. 
The program will model a liner trend over this time period. Note: more complex patterns of changing K 
can be specified by entering a function in the box for Carrying Capacity (see Chapter 6). 


 
VORTEX Version 9.50 User’s Manual 
 
61 
Chapter 3 
The Data Input Process 
 
 
Box F: What Exactly Is Carrying Capacity, Anyway? 
 
“Carrying capacity—rarely in the field of resource management 
has a term been so frequently used to the confusion of so many.” 
(MacNab 1985) 
 
The definition and use of the concept of carrying capacity is one of the more tricky issues in 
population viability analysis (and, for that matter, in much of population ecology). Pick up any 
number of textbooks on ecology or wildlife management and you are likely to find that each one 
presents a slightly different formal definition of carrying capacity. In fact, some authors (e.g., 
Caughley 1977) choose not to use the term altogether in their presentation of the mathematics of 
population growth. In the context of wildlife management, the habitat carrying capacity for a 
particular population can be defined as the maximum number of individuals that environment can 
sustain over time in the absence of unnatural disturbances, and without inducing harmful trends in 
the abundance of the resources required by that population.  
 
We can gain more insight into this concept by considering the familiar (and admittedly simplistic) 
logistic equation for population growth: 
 




−
=
K
N
K
rN
dt
dN
 
 
where r is the intrinsic rate of population increase, N is population size, and K is carrying capacity. 
Mathematically, K can be thought of as the population size limit at which the rate of growth dN/dt is 
equal to zero. Some ecologists define K as a ratio of the total rate of food production in the habitat 
(P) to the per capita rate of food consumption necessary for survival (M). Since a population of size 
N must consume food resources at a rate of NM just to stay alive, there are P – NM resources 
available for the production of new individuals. If NM exceeds P, then resources available for 
reproduction become negative and the population must decrease in size.  
 
When N is very small—for example, when a population is re-established in its native habitat—the 
potential growth rate is very close to exponential. If the population exceeds its carrying capacity, the 
number of individuals will be reduced until N ≤ K. The carrying capacity, then, can be thought of as 
representing a stable equilibrium population size. Many population ecologists describe the gradual 
approach towards this equilibrium in terms of damped oscillations in population growth. 
 
Empirically, one could estimate the habitat carrying capacity for a given animal species by 
calculating the total food supply appropriate for that species that is available in the habitat, and 
dividing that value by the rate of that species’ consumption of its available food supply (for a 
detailed discussion of this technique, see Hobbs and Swift (1985)). For example, Petit and Pors 
(1996) estimated population sizes, flower availability and nectar output for each of three species of 
columnar cacti on Curaçao. Carrying capacities for the two species of nectar-feeding bats dependent 
on these cacti could then be estimated based on the daily availability of mature flowers and the field 
energy requirements of the bats, with additional energy requirements associated with pregnancy and 
lactation taken into account.  
 
If detailed data such as these are unavailable, a rough estimate of habitat carrying capacity can be 
generated using long-term data on population size. If the size of the population of interest appears 
to be relatively constant over the period of observation (and in the absence of significant human 
impact),  one can fairly safely assume that the population is at or near its carrying capacity. If this 
equilibrium is observed in the presence of major human influences, such as a strong hunting 
pressure, then historical data could be consulted to determine if this stable size is indeed natural or 
purely artificial. One could also calculate K for a given habitat using population density data from 
undisturbed habitats elsewhere in the species’ range. 
 


VORTEX Version 9.50 User’s Manual 
62 Chapter 3 
The Data Input Process 
Harvest 
 
In this section, VORTEX gives you the option of removing individuals during a simulation (Figure 33). 
 
 
Figure 33. Harvest input section. 
Harvest can mimic hunting, culling, research-related removals, removal of young individuals for 
translocation programs, etc. Check the Population Harvested? box to request a regular harvest of 
individuals. 
The harvest can begin and end at any time during the stipulated length of the simulation. Enter the First 
Year of Harvest and the Last Year of Harvest. For example, if you wish to begin harvesting in year 10 and 
end in year 25, enter 10 and 25 for these two questions, respectively. No harvest will be allowed before 
or after the time frame that you have specified. 
If you wish to harvest every year within the specified time frame, enter 1 for the Interval Between 
Harvests. If you wish to harvest animals every other year, enter 2. As another example, if the first year of 


 
VORTEX Version 9.50 User’s Manual 
 
63 
Chapter 3 
The Data Input Process 
harvest is 10, the final year is 50 and the interval is 10 years, then harvesting will take place in years 10, 
20, 30, 40 and 50. 
Optional Criterion for Harvest: You can specify here some criterion that will restrict harvesting to occur 
only if the population status meets certain conditions. You enter this as a function (see Chapter 6). For 
example, if you enter “=(N/K)>0.8” then harvests will only occur if the ratio of the population size to 
the varying capacity is at least 0.8 (and if it is a harvest year as defined above). Leave the grid cell entry 
as  1 if you do not want to provide any harvest threshold criteria. 
Female (Male) Ages being Harvested: Enter the number of females and/or males that you will harvest at 
each time interval defined for each age class through adults. Enter 0 for no individuals to be harvested in 
a given age class. VORTEX will conduct the harvest immediately prior to calculating the year’s breeding 
pairs, so the youngest individual that can be harvested is one year old. If the program attempts to harvest 
individuals from an age class and finds an insufficient number of individuals, the simulation will continue 
without the harvest of those individuals determined not to exist. VORTEX will then report at the end of the 
simulation that some of the attempted harvests could not be carried out. 
 
Supplementation 
 
You also have the option of adding any number of juvenile or adult, male or female individuals to each 
population (Figure 34). This option can simulate supplementation through, for example, a translocation or 
releases from a captive breeding program. As with the harvest option, supplemental individuals can be 
added at any time and interval within the specified time frame for the simulation. Furthermore, you are 
allowed to both harvest and supplement individuals in a fashion independent of one another. 
 
VORTEX assumes that the individuals that are being added to the recipient population are 
unrelated to both each other and to any other individual in the recipient population. Consequently, 
supplementation is a means of increasing genetic diversity as well as total numbers of individuals 
within a population. 
 
If you want to supplement your population(s), check the Population Supplemented? box. You must then 
provide the values on the subsequent lines to define the nature of the supplementation. 
First (Last) Year of Supplementation: The supplementation can begin and end at any time during the 
stipulated length of the simulation. Enter the years in which you wish to begin and end supplementation. 
For example, if you wish to begin supplementing in year 20 and end in year 50, enter 20 and 50 for these 
two questions, respectively. No supplementation will be allowed before or after the time frame that you 
have specified. 
Interval Between Supplementations: If you wish to supplement every year within the specified time 
frame, enter 1. If you wish to supplement every other year, enter 2. 
Optional Criterion for Supplementing: You can specify here some criteria that will restrict 
supplementation to occur only if the population status meets certain conditions. You enter this as a 
function (see Chapter 5). For example, if you enter “=(N/K)<0.25” then supplements will be added only 
if the ratio of the population size to the varying capacity is at less then 0.25 (and if it is a supplementation 
year as defined above). Leave the grid cell entry as  1 if you do not want to provide any criterion for 
supplementing. 
Female (Male) Ages being Supplemented: Enter the number of females and/or males that you will add at 
each time interval defined for each age class through adults. Enter 0 for no individuals to be 
supplemented in a given age class. These parameters differ slightly from the parameters defining 
harvesting in that the last age class listed on the screen corresponds to the first year of adulthood instead 
of the aggregate adult stage. This difference results from the fact that while harvesting selects any adult 


VORTEX Version 9.50 User’s Manual 
64 Chapter 3 
The Data Input Process 
individual regardless of age, VORTEX must assign a specific age class to each adult that is being added to 
the recipient population. The age of adults added to the population is always equal to the age at which 
breeding commences.   
 
 
Figure 34. Supplementation input section. 
 
 
Genetic Management 
 
In this last section of Input (Figure 35) provides a series of options that are new in version 9.50 (although 
some were provided as Special Options in earlier versions). Most of the options in this section would be 
applicable primarily to populations that are captive or otherwise under intensive management, such that 
the animals breeding each year are controlled. A few of the options provide more detailed genetic results 
from the simulations. Most or all of the options in this section would not be needed by most users of 
VORTEX. (If you do not need these options, you can proceed to the next section and run your simulation!) 
 


 
VORTEX Version 9.50 User’s Manual 
 
65 
Chapter 3 
The Data Input Process 
 
Figure 35. Genetic Management input section. 
Import starting population from file: VORTEX can start the simulation with a known or assumed population 
that has a defined pedigree structure. This option allows the user to provide to VORTEX a population 
pedigree (a “studbook”) that might describe a captive population or a wild population that has been 
monitored closely for a number of generations. The file specifying the pedigree of the starting population 
should be a text (ASCII) file, with a line for each individual in the population, in the following format: 
 
# Any lines preceded by a ‘#’’ are ignored as comments, but there must be at least 3 lines of non-data headers at the top. 
# Note that females are coded as 1, males as 0. 
# Required field are ID,Dam,Sire,Sex,Selected,Living,Age – but you can add other data to the end of the lines if you wish 
    58,  WILD,  WILD,0,0,0, -1 
    69,  WILD,  WILD,1,0,0, -1 
   139,  WILD,  WILD,1,0,0, -1 
   155,    58,    69,0,1,1,5 
   160,    58,   139,1,1,1,4 
   170,   155,   160,1,1,1,2 


VORTEX Version 9.50 User’s Manual 
66 Chapter 3 
The Data Input Process 
The variables listed for each animals should be separated by commas, no spaces (except when an optional 
space is used to complete a 6-character name for the ID, Dam, or Sire). ID, Dam, and Sire should each be 
a 6 (or fewer) character name, with “WILD” as dam and sire to indicate a founder. Sex is coded as 0, m, 
or M for male; and 1, f, or F for female. The next data field indicates whether of not an individual should 
be included in the starting population, with 1 or T for included; and 0 or F for excluded. The next data 
field indicates if the animal in the pedigree is currently alive (T or 1) or dead (F or 0). the last field is the 
age of each individual. Age can be set to -1 (or anything) for dead animals. The format of the file is the 
same as the .txt file used by the Lineage pedigree drawing software (see www.ansci.cornell.edu/lineage/) 
and produced by the PM2000 pedigree analysis program (see www.vortex9.org/pm2000.html). 
Number of neutral loci to be modeled:  VORTEX normally simulates Mendelian transmission of alleles at 
one neutral locus. Up to 10 loci can be simulated by specifying the number here. This will produce more 
precise estimates of genetic variation within and genetic distances among populations, and can be useful 
for simulating patterns of molecular genetic data that might arise from the population dynamics. 
Read starting allele frequencies from file:  VORTEX normally starts the simulation with each founder 
individual carrying unique alleles at the modeled locus or loci. For testing changes in known or assumed 
starting frequencies of alleles at loci, you can specify that the simulation should sample from a known 
distribution of allele frequencies when it assign alleles to founders. This option might be used to test 
expected patterns of microsatellite DNA alleles, or to test the evolution of alleles with specific selected 
effects on demography. (Although the alleles at “neutral” loci in VORTEX usually have no impact on 
fitness, it is possible to specify that demographic rates are functions of genotypes.) The starting allele 
frequencies are specified in a text file with the following format: 
 
3 
3 4 2 
.33 .33 .34 
.25 .25 .25 .25 
.5 .5 
The first line specifies the number of loci modeled. The next line gives the number of alleles for each of 
these loci. The subsequent lines give the allele frequency distributions for the loci.  
Breed to maintain the population at K:  With this option checked, the program will calculate each year the 
expected number of matings required to bring the population to (but not beyond) the carrying capacity. 
Note that carrying capacity may still not be reached if there are not enough adult females to fulfill the 
required number of matings.  
Prevent matings with kinships (inbreeding) greater than F = x.xxx:  With this option, females will not be 
paired with a male that is more closely related than the specified maximal allowable inbreeding. If a male 
initially chosen is too closely related, a different male will be picked instead. (See the option four down to 
see what happens if repeated males are unsuitable.) 
Pair according to mean kinships:  Managed breeding programs can retain maximal genetic diversity by 
selecting as breeders those individuals with the lowest mean kinship (MK) to the living population 
(Ballou and Lacy 1995). If this option is selected, then the user must also specify if the MK list for 
prioritizing breeders is to be updated as each pairing is selected (“dynamic MK list”) or left unchanged 
within each year as pairs are selected (“static MK list”). A dynamic list will preserve genetic diversity 
better if most males and females that are paired do produce offspring (i.e., the % females breeding is 
high). A static list will provide better genetic management if many pairings fail (because the dynamic list 
would incorrectly assume that many pairs do produce the expected offspring).  
(Optional) maximum number of mates:  The option allows you to put a constraint on the number of 
females to which a male can be paired each year. This option can be useful to constrain harem size, or to 
prevent a single male from dominating breeding when pairs are selected by using a static MK list.  


 
VORTEX Version 9.50 User’s Manual 
 
67 
Chapter 3 
The Data Input Process 
(Optional) limitation of pairings to sires with:  This option allows the user to specify a constraint on 
which males are suitable as sires. The constraint is specified using a function, as described in Chapter 6. 
For these functions specifying mate suitability, the variables describing individual characteristics (e.g., 
‘A’ for age, ‘I’ for inbreeding, ‘P’ for population) refer to the value for the potential sire; the variable ‘O’ 
is the ID of the dam (such that the variable ‘IIS1(O)’ would refer to the first individual state variable of 
the dam); Examples of the use of this option include: 
“=I<10”  [for avoiding mating with a sire than has an inbreeding level greater than 10%] 
“=A>(IIS1(O))” [to force the sire to be older than the dam, if IS1 is set to age] 
This option can provide a great deal of flexibility in creating complex breeding systems, but it can be very 
difficult to specify the constraint function correctly. Detailed discussion of how to use this option is 
beyond the scope of this manual. 
Number of times to try to find a mate:  If constraints on suitable males to select as mates are specified in 
the above options related to inbreeding or limitations of pairings, then this option will specify how many 
times the program should select a male and test it’s suitability before giving up and leaving the female 
without a mate for that year. A default value of 10 is used if this input box is left empty or is set to 0.  
Produce a file in GenePop format at the end of each iteration:  Checking this box will generate at the end 
of each iteration of the simulation a file (with extension .gp) listing all living individuals and their 
genotypes. The file is in the format required for analysis with the GenePop software 
(http://wbiomed.curtin.edu.au/genepop/). 
Produce a file of allele frequencies and probabilities of persistence:  If this option is checked, then 
VORTEX will create an output file (with extension .gen) that lists for each founder allele the mean 
frequency at the end of the simulations and the probability of persistence (proportion of iterations in 
which the allele persisted).  
 
It is always good to watch the VORTEX website for upgrades!  The Genetic Management section 
of VORTEX is still undergoing considerable improvements, as are many other sections!  
 
Saving your Input and Running the Simulation 
 
After you have completed entering values for all of the input parameters, it is probably wise to save your 
project. (You would probably be disappointed if you spent a long time entering input values, did not save 
them, and then the program crashed during the simulation because one number was wrong.) To save your 
Project, click on the save icon (the disk) on the toolbar, or select Save or SaveAs from the File menu. If 
you save as a file name other than what you originally specified for the Project, VORTEX will prompt you 
to find out if you wish to change the Project name to match the file name. (It makes sense to keep the file 
name and the project name the same, although you do not have to do so.) 
 
To run your simulation, click on the Run icon (the green triangle) on the toolbar or select Run Simulation 
from the VORTEX menu. The Run Simulation box (Figure 36) will then appear. Check the boxes to 
indicate which scenario(s) you wish to run and then hit the Run! command.  
 
During the simulation, a graph of the changing population size will be displayed (Figure 37). If the 
simulation runs slowly (as it will if you have a very large population size) you can hit buttons to Stop, 
Pause, or Clear Lines. Stopping will terminate the simulation without completing all of the iterations. 
Pausing will temporarily stop the simulation (as you might want to do while describing the model to 
others), and then will Resume when you hit that button (which appears after you hit Pause). Clear Lines 
just gives you a way to erase all prior lines if the screen is getting cluttered and unreadable. 


VORTEX Version 9.50 User’s Manual 
68 Chapter 3 
The Data Input Process 
 
Figure 36. Run Simulation selection window. 
 
Figure 37. VORTEX Simulation population size graph. 


 
VORTEX Version 9.50 User’s Manual 
 
69 
Chapter 3 
The Data Input Process 
 
 
VORTEX uses a very fast method to write all of the lines to the screen. (If they are slow, that is 
because the simulation itself, rather than the graphing, is taking a long time.)  Consequently, the 
program may not refresh the display if you drag the graph window or toggle out to another Windows 
application and back. Therefore, it is best to not try to do anything else on your computer while the 
simulation is running. (This also helps by leaving all memory and system resources available to 
VORTEX.) If you feel that you must do other work (e.g., using Word or Excel or check email) while the 
VORTEX simulation is working, you should specify the Special Option (under Project Settings) of “Do 
not show graphs during iterations.” 
 
When the requested simulations are complete, VORTEX displays a few summary statistics at the top of the 
graph. When you are done viewing the graph, close it by clicking on the ‘x’ icon in the upper right corner. 
If you want to print or save this graph of the simulation, use the Windows PrntScrn button to copy the 
image to your Windows clipboard. You can then paste it into Word, or PowerPoint, or any other program 
that can display images. (However, data for tabulating and graphing summary results have already been 
saved on your disk – as we will see in the next Chapter, so there is usually no need to save these rather 
cluttered displays of all iterations.)  
 
Additional iterations can be added to the results for a simulation that has already been run by selecting the 
“Resume” command from the Run Simulation window (Figure 36). In this case, VORTEX will resume that 
simulation, adding to the results (and averaging into prior results of means across iterations) up to the 
number of iterations currently specified in the Scenario Settings. I.e., if the simulation is first run for 100 
iterations, and then the number of iterations is changed to 500, resuming the simulation will add 400 more 
iterations to the tallied results.  
 
Adding and Deleting Scenarios 
 
Congratulations! You have created and run your first scenario. However, it is highly unlikely that you are 
now done with your analysis of the particular species, population, and issue at hand. Almost certainly, 
you were uncertain about some of the input parameters you entered. Possibly the estimate was based on 
few (or no!) data. It may be that the data came from field studies conducted in a different part of the 
species range. And it may be that the data are accurate descriptions of the past or even present status of 
the population, but are not likely to be good descriptors of the future performance of the population, in 
light of expected or planned changes to the habitat or populations. In any case, a major part of almost all 
population viability analyses is “sensitivity testing” – the examination of the impacts of varied input 
parameters on the projected population performance. You should refer to the background material in 
Appendix I and in the references for a more thorough discussion of the topic of sensitivity testing. 
 
To conduct sensitivity testing, or any investigation of alternative scenarios that may be used to describe 
the population, you need to create, run, and analyze scenarios that vary from your initial case for one or a 
few input parameters. One way to do this would be to start from the beginning and create a new analysis 
in VORTEX. However, the program makes it very easy for you to copy all input from a prior Scenario into 
one or more new Scenarios in your Project. In these newly copied Scenarios, you can then change the few 
input parameters that you want to vary, and re-run the simulations for each case. In addition, VORTEX now 
provides a module for automated sensitivity testing, with which you can rapidly create and analyze a 
series of Scenarios that vary specific input parameters. The automated Sensitivity Testing is described in 
Chapter 5. The last part of this chapter, below, describes how you can manually add and delete Scenarios 
from your Project, for the purpose of sensitivity testing, to test possible management strategies, or for any 
other purpose. 


VORTEX Version 9.50 User’s Manual 
70 Chapter 3 
The Data Input Process 
 
Adding Scenarios to Your Project 
 
To add a scenario, from any Simulation Input window, click on the “Add Scenario” command in the 
upper left. The pop-up window shown in Figure 38 will appear. 
 
 
Figure 38. New Scenario window for adding Scenarios based on a prior Scenario. 
 
Click on the existing Scenario that you want to use as a template for new Scenarios, then select below the 
number of copies you wish to create of this Scenario, and then click on “OK”.  
 
The new Scenarios you create will initially be named as “Scenario1 – Copy 1”, Scenario1 – Copy 2”, etc., 
in which “Scenario1” is the name of whatever Scenario you chose to use as the template, and they will be 
placed into your Project immediately after the template Scenario. After you create new Scenarios, you can 
toggle among the Scenarios in any of three ways: (1) you can use the drop-down list to select the Scenario 
you wish to work on, (2) you can click on the small ‘<’ and ‘>’ buttons alongside the dropdown list to 
move backwards and forwards through the list of Scenarios, and (3) you can click on the buttons to the 
right with the Scenario names. (See Figure 39.)  
 
The first task you should complete after creating new Scenarios is to change their names to something 
more descriptive. You do this in the top input box (Scenario Name) of the Scenario Settings screen. After 
changing the Scenario name to something more descriptive, go to the Input sections where you want to 
vary the parameters in the new Scenarios, and make the desired changes.  
 
Once you have many Scenarios in your Project, it is easy to accidentally change the labels and 
input values for the wrong Scenario, because the screens for the various Scenarios look so similar. 
Before you start editing input values, make sure that you are working on the intended Scenario.  
 


 
VORTEX Version 9.50 User’s Manual 
 
71 
Chapter 3 
The Data Input Process 
 
Figure 39. Multiple means for moving among alternative Scenarios. 
 
After you create new Scenarios, it is always wise to save the Project so that you won’t lose your Scenarios 
if something later goes wrong. (However, VORTEX always prompts you to save each open Project when 
you exit the program, so you do have a chance later to save everything – if nothing does go wrong.) 
 
Deleting Scenarios from Your Project 
 
If you have created Scenarios that you no longer want, you can delete them by hitting the “Delete 
Scenario” command at the top of the Input window. This will delete the current Scenario. A prompt will 
first warn you that you cannot recover from this action (other than by re-creating the Scenario again).  
 


VORTEX Version 9.50 User’s Manual 
72 Chapter 3 
The Data Input Process 
Reordering scenarios 
 
After you add and delete Scenarios from your Project, you may find that the Scenarios are not listed in the 
order you would like them to have. VORTEX provides a Scenario Manager (Figure 40), which you access 
by clicking on the “re-order” command next to the dropdown list of Scenario names. The Scenario 
Manager lets you change the order of the Scenarios in your Project (moving them up or down in the list).  
 
 
Figure 40. Scenario Manager window. 
 
 
 
 


 
VORTEX Version 9.50 User’s Manual 
 
73 
Chapter 4 
Viewing Model Results 
Chapter 
 
Viewing Model Results:  
Text, Tabular, and 
Graphical Output 
 
 
 
Once you have entered all of the necessary input parameters and given the 
command to run your first VORTEX model, you are ready to look at your simulation results.  A display of 
changing population sizes was displayed (perhaps very quickly) on your screen as the simulation was 
running (Figure 37). While you may want to capture that image onto your Windows clipboard with a 
PrntScrn system command, the more useful presentations of model results are generally those that provide 
mean results across iterations, perhaps with standard deviations to indicate the variation among iterations 
or standard errors to indicate the precision with which the means were estimated from the finite number 
of iterations run. In addition, there are many measures of population performance and viability other than 
just the projected population size. This chapter describes how to use VORTEX to view text, tabular, and 
graphical summaries of your results.  
 
Text Output 
 
Click on the Text Output tab to access simple text descriptions of your Project input or results (Figure 
41). There are four subsections of Text Output.  
 
Input Summary 
 
The first section provides a summary of the input values you entered for each Scenario. It is wise to scroll 
through this Input Summary in order to be sure that you entered the values as you intended. In addition, 
you can cut and paste from this text summary into any reports that you need to create of your work. At the 
top of the Input Summary, and similarly at the top of the other three sections of Text Output, are three 
command buttons. These allow you to send the text to the Project Report, print the text, or save the text as 
a file that you would specify. The Project Report will be described in detail later – it is a simple word 
processor that allows you to start building a report of your analyses while you are working within the 
VORTEX program. (You can then access that report from MS Word or other software to further edit and 
refine it.) If you chose to print the text, VORTEX will open the standard Windows Print utility. If you save 
the text, VORTEX saves it as a simple text file, which could later be viewed, edited, or printed from 
NotePad, MS Word, or other word processing software.  
4 


VORTEX Version 9.50 User’s Manual 
74 Chapter 4 
Viewing Model Results 
 
Figure 41. Input Summary section of Text Output. 
 
At the top of the text display window are dropdown lists that let you move among the reports for the 
various Scenarios and Populations (within Scenarios). In the Input Summary, all Populations in each 
Scenario are contained within the same text file, so you could find them by scrolling down. However, the 
file can be very large, so it is often faster to use the dropdown list to jump to the place where text on a 
Population starts.  
 
Deterministic Calculations 
 
The second section of Text Output provides both text and a simple graph to display the deterministic 
projections of population size (Figure 42). The text window shows the exponential rate of increase, r, the 
annual rate of change, λ, and the per generation rate of change or “net replacement rate”, R0, as 
determined from life table analysis of the mean rates of reproduction and survival in your model. The 
mean generation time and a stable age distribution (calculated from age-specific birth and death rates) are 
also given. See Box G for a brief description of these deterministic calculations.  


 
VORTEX Version 9.50 User’s Manual 
 
75 
Chapter 4 
Viewing Model Results 
 
Figure 42. Deterministic Calculations shown in Text Output. 
 
The graph given with the Deterministic Calculations is fairly simple and crude, but it shows the 
exponential growth (or decline) projected from the life table calculations (up to the limit set by the 
carrying capacity). The graph can be sent to your Project Report, printed, or exported to a bitmap (.bmp) 
file for import into other programs.  
 
The deterministic calculations are performed by VORTEX as soon as you enter the input values for your 
model. Therefore, you can view these results (and also the Input Summary text) even before you run your 
simulations. It is often helpful (and always recommended) to look at the deterministic projections before 
proceeding with stochastic simulations, so that you will know whether the rates of reproduction and 
survival are at least minimally adequate to allow for population growth in the absence of random 
fluctuations and other destabilizing processes (such as inbreeding and harvest). 
 


VORTEX Version 9.50 User’s Manual 
76 Chapter 4 
Viewing Model Results 
 
It is important to look at the deterministic projections of population growth for any analysis. If 
r is negative, the population is in deterministic decline (the number of deaths outpace the 
number of births), and will become extinct even in the absence of any stochastic 
fluctuations. The difference between the deterministic population growth rate and the growth 
rate resulting from the simulation can give an indication of the importance of stochastic 
factors as threats to population persistence. 
 
 
Box G: Deterministic Calculations in VORTEX 
 
Before the actual stochastic simulation begins, VORTEX performs a standard life table analysis to 
calculate the deterministic mean population growth rate (r, the exponential growth rate; or λ 
(“lambda”), the annual multiplicative growth rate), the mean generation time for males and females, 
and the stable age distribution used (optionally) to initialize the starting population. These 
calculations will provide accurate long-term averages, if stochastic variation (due to demographic 
stochasticity, environmental variation, catastrophes, and inbreeding effects) is minimal. Life table 
analyses implicitly assume that age-specific birth and death rates are constant through time; they 
yield over-estimates of long-term population growth if there is any variation in demographic rates. 
 
The deterministic population growth rate r is calculated by solving the Euler equation: 
 
(
)
∑
=
−
,
1
rx
x
x
e
m
l
 
 
in which lx and mx are the age-specific mortality and fecundity rates, respectively for age class x to 
x+1, and the summation is over all age classes. Lambda is related to r by: 
 
.
r
e
=
λ
 
 
The stable age distribution, or the proportion of the population at each age class cx, is given by: 
 
(
)
.
∑
−
−
=
rx
x
rx
x
x
e
l
e
l
c
 
 
The determination of a stable age distribution for males in a given population becomes a bit more 
complicated if the mortality schedules are different for the two sexes. In this case, r is calculated 
based on female life history tables (since females control population growth), but the lx’s used in the 
age distribution equation are those for males. Moreover, the exact form of the equation is dependent 
on when the age classes were censused. In the above equation, c0 is the proportion of the 
population aged 0 plus a small increment, just after the breeding season but before mortality is 
imposed. In order to build the initial population, VORTEX omits age class 0 (because the simulations 
begin just before the breeding season), and re-scales the age distribution in order to sum to 1.0.  
 
The life table calculations assume that there is no limitation of mates (i.e., there are always enough 
breeding males to mate with all breeding females). Other complications arise if there are 
catastrophes in the simulation model. In those cases, VORTEX adjusts the fecundity and mortality 
rates to account for the effect of catastrophes, averaged across years. 
 
For more information on the details of life table analysis, refer to any number of general ecology or 
population biology texts such as Pielou (1977), Krebs (1994), or Caughley (1977). 


 
VORTEX Version 9.50 User’s Manual 
 
77 
Chapter 4 
Viewing Model Results 
Output Summary 
 
The third section of Text Output lists the basic status of each population at each year of the simulations.  
 
 
Figure 43. Output Summary section of Text Output. 
 
The statistics reported in this file are: 
¾ The cumulative number of iterations (populations) that have become extinct or remain extant; 
¾ The probability of population extinction (PE) or survival (equivalent to the proportion of 
iterations (populations) that have become extinct or remain extant); 
¾ The mean population size, reported separately for all populations (N-all) and only for those 
remaining extant (N-extant), with standard error (SE) and standard deviation (SD) across 
iterations; 
¾ The mean “expected heterozygosity” (or “gene diversity”) remaining in the extant populations, 
with standard error and standard deviation across iterations; 


VORTEX Version 9.50 User’s Manual 
78 Chapter 4 
Viewing Model Results 
¾ The mean “observed heterozygosity” (equal to 1 – [mean inbreeding coefficient]) remaining in 
the extant populations, with standard error and standard deviation across iterations; 
¾ The mean number of alleles remaining within extant populations (from an original number equal 
to twice the number of founder individuals), with standard error and standard deviation;  
and, if the inbreeding depression option is included in the simulation, 
¾ The number of lethal alleles remaining per diploid individual, with standard error and standard 
deviation, determined by the nature and extent of the genetic load identified in the input process, 
and the intensity of inbreeding the population undergoes. 
 
Following these yearly reports, the output file presents a series of final summary information that 
includes: 
¾ The final probability of population extinction and, the converse, the probability of population 
persistence; 
¾ If at least 50% of the iterations went extinct, the median time to extinction; 
¾ Of those iterations that suffer extinctions, the mean time to first population extinction, with SE 
and SD across iterations; 
¾ The mean times to re-colonization and re-extinction of those simulations that went extinct; 
¾ The mean final population size, with SE and SD across iterations, for all populations, including 
those that went extinct (e.g., had a final size of 0); 
¾ The mean final population size for those iterations that do not become extinct, with SE and SD 
across iterations; 
¾ The final age-sex composition of the extant populations; and 
¾ The mean population growth rate, r, with SE and SD across iterations. When harvesting or 
supplementation are included in your model, VORTEX will report the mean population growth rate 
for years without harvest or supplementation, for years with harvest or supplementation, and 
averaged across all years. VORTEX reports the growth rate as the exponential growth (r) rather 
than the arithmetic growth rate (lambda), because the mean r over time is equal to the long-term r. 
(Whereas the geometric mean lambda is the long term lambda.) This mean growth rate is 
calculated from the mean (across years and across iterations) of N in one year over N in the prior 
year, except that this ratio is calculated before any truncation of N due to exceeding carrying 
capacity. Thus, if K = 100, N(year 0) = 80, N(year 1 before truncation at K) = 120, the growth 
rate used in the mean would be r = ln(120/80) = 0.405, even though the growth rate experienced 
after considering the truncation for K would be ln(100/80). VORTEX reports the growth calculated 
before truncation for K, because that better reflects the demographic potential for population 
growth. [If you need it, the mean r after K truncation is simply ln(finalN/initialN)/ (# years).] 
 
Additional summary information will be provided when you have built a metapopulation model. For 
example, the output file will also include the same set of summary data for the global metapopulation, and 
will also present a set of within-population means. These means are unweighted averages across 
populations, while the standard deviations are means of the individual standard deviations of the 
populations. Population sizes and genetic metrics are averaged across only those populations that survived 
some simulations. Similarly, times to extinction, recolonization, and re-extinction are averaged across 
only those populations that had some extinctions. Finally, if any recolonization events occurred during the 
simulation, VORTEX will report the frequency of recolonization, the mean time to recolonization, and the 
frequency and mean time to population re-extinction if appropriate. Also given for metapopulations will 
be some tables of genetic distances (and identities), with standard errors, to show the amount of genetic 
differentiation that existed between populations at the end of the simulations. 
 
The standard errors reported for each summary statistic will indicate whether the number of iterations was 
large enough to give results that are sufficiently stable (precise) for your purposes. 


 
VORTEX Version 9.50 User’s Manual 
 
79 
Chapter 4 
Viewing Model Results 
Other Output 
 
The fourth section of Text Output provides two summary tables, in grid formats (Figure 44). One table 
provides a line of basic summary statistics for each Population of each Scenario that has been run. The 
summary statistics tabulated are the number of iterations (#Runs), the deterministic growth rate (det-r), 
the mean stochastic growth rate (stoc-r) experienced in the simulations, the SD of the stochastic 
population growth [SD(r)], and final values (at the end of the simulation) for many of the descriptive 
statistics listed above in the Output Summary.  
 
 
Figure 44. Scenario Summaries table in Other Output. 
The other table in Other Output provides Iteration Summaries – a tabulation for each iteration of the year 
of extinction (if extinction occurs), final population size, and, if extinction does not occur, the final gene 
diversity, mean inbreeding coefficient, and number of founder alleles remaining. The data in this Iteration 
Summary table can be used to analyze the full distribution (not just the mean and SD) of the times to 
extinction, final population sizes, and genetic statistics. The “Export” button for the Other Output tables 


VORTEX Version 9.50 User’s Manual 
80 Chapter 4 
Viewing Model Results 
will export these tables as text files delimited with semi-colons. These files can be imported directly into 
Excel or other spreadsheet software for further analysis (the column headers should transfer over). 
Graphs and Tables 
Click on the Graphs and Tables tab to access a section that lets you build tables and graphs displaying 
results for a variety of summary statistics (Figure 45). In the Data Specification tab of Graphs and Tables, 
you specify what Scenarios, Populations, Years, and Variables you want to put into the table that will be 
displayed at the right. VORTEX then also creates a graph of the data in your table, and gives you access to 
tools to customize your graph.  
 
The Data Specification area can be confusing, but it gives you considerable flexibility in what you put 
into your tables and graphs. To understand how the Data Specification works, you should first realize that 
the results from your analyses can be considered to be a series of data points in a three-dimensional space.  
 
 
Figure 45. Data Specification and Table screen of the Graphs and Tables for output. 


 
VORTEX Version 9.50 User’s Manual 
 
81 
Chapter 4 
Viewing Model Results 
The three dimensions of the data are: Years (the year of the simulation at which the data point was taken), 
Populations/Scenarios (which Population from which Scenario is being observed), and Variables (which 
summary variable is being tabulated). These three dimensions need to be assigned to the columns, rows, 
and cell values of the table you create. For example, a common table would be to display some Variable 
(such as the mean population size) as the cell contents, in a grid with a series of Years  (such as 0, 10, 20, 
…) as the column headings and Populations (such as Population1, Population2, and Metapopulation) as 
the row headings. (See Figure 45 for an example of a table specification similar to this.) 
 
However, you could instead want the Years to be arrayed down the side of the table as the rows, with the 
Populations across the top as the columns. To do this, you would select Populations from the dropdown 
list for Columns, and Years from the dropdown list for Rows. You could instead tabulate multiple 
Variables (such as PE, N, SD(N), and MedianTE) as columns with Populations as rows, or Variables as 
rows with Populations as columns. In the specification of the remaining dimension (Years) you then give 
from which Year of the simulation you want the value of these Variables displayed. (Usually, but not 
always, you would select the final year.) Figure 46 shows an example of a table of this type.  
 
 
Figure 46. An example of a Table with Variables as Columns. 


VORTEX Version 9.50 User’s Manual 
82 Chapter 4 
Viewing Model Results 
VORTEX can display a multi-part table, with results from a different Scenario shown in each part. You 
select which Scenario(s) you want to examine by checking the boxes in the grid on the lower left of the 
screen. To then specify which Years, Populations, and Variable(s) you want in your table, you need to 
specify the Columns and Rows in the grid in the lower left, and pick from the dropdown list which 
Variable/Year/Population is to be tabulated. The specification of Columns and Rows can be done by 
typing the numbers of the desired Years or Populations into the grid under Columns or Rows, as 
appropriate.  
 
Alternatively, you can click on the “…” button for Rows or Columns. That will open up a window for 
specification of the Years, Populations, or Variables, as appropriate (Figure 47).  
 
 
Figure 47. Year Specification window for creating tables and graphs. 
 
Specification of the Years in this window can be confusing, but it is also very fast once you learn how to 
use it. You can quickly “Select All” years by clicking on the command, if you want every year shown in 
your table and graph. (You can also “Deselect All” if you want to remove a prior selection.) To specify 
that only some years should be selected, you can check on those years in the grid. The boxes in the grid 
are arrayed across rows for each decade. That is, the check boxes in the first row of the grid are years 0, 1, 
2, …, 9; the check boxes in the second row of the grid are years 10, 11, 12, …, 19; etc.  If you want to 
select all of the years in one column (such as years 0, 10, 20, …), you can click on the column heading. 
Similarly, to select all of the years in one decade (e.g., 20, 21, 22, …, 29), you can click on the row label. 
The order in which you select the years is shown in the list that accumulates on the right, and this would 
be the order that the years show up in your data table. Presumably, you would want the years to be in 
ascending order in your table. To re-order the years, click on the “Sort Ascending” command. After you 
have selected (and possibly sorted) the years you want in your table, click “OK” to send that selection to 
the Data Specification screen.  
 
Selection of Populations or Variables is done in a similar way, except that they are more straightforward 
to select because they are displayed in a single vertical list of check boxes.  
 
After you have completed specification of your data table, you can click on commands to print the table, 
send it to your Project Report, or export it to a text file delimited with semi-colons. 
 


 
VORTEX Version 9.50 User’s Manual 
 
83 
Chapter 4 
Viewing Model Results 
Data Graphs 
 
If you click on the Data Graphs tab, VORTEX will display a graph of the data that are in your table (Figure 
48). The dimension used for table columns is plotted as the x-axis; the dimension used for the rows of the 
table will create separate lines on the graph; the values displayed in the table will be the y-axis of the 
graph. To remember how the graph axes relate to the table lay-out, think of each row of the table as being 
plotted as a line on the graph, with the columns (place in the row) being the dependent (x-axis) variable 
and the value given in the table being the dependent (y-axis) variable.  
 
 
Figure 48. Data Graphs window. 
 
The initial size of the Data Graphs window that opens up will often force your graph to be squeezed into a 
fairly small window, and often the legend will not be displayed (because it doesn’t fit in the small 
window). To see a better image of the graph, click on the corner of the Project window and drag it out to a 
larger size.  
 
On the Data Graphs window, you are provided with several Graph Options for changing the look of your 
graphs. You can change the text or position of the legend, the text or font of the main title or the axis 
titles, and the line thickness. You can also toggle between a line graph and a bar graph, although for many 


VORTEX Version 9.50 User’s Manual 
84 Chapter 4 
Viewing Model Results 
kinds of data that would be plotted only one of these two graphs would be reasonable. Command buttons 
are provided to allow you to Print the graph, send it to the Project Report, or Export the graph to a bitmap 
(.bmp) file. You can also add error bars to show standard errors (SE) around the plotted means, or 
standard deviations (SD) across iterations. The SE and SD options are available only for those plotted 
variables for which they would be applicable. (E.g., there is no error around deterministic growth rates.) 
 
While these basic Graph Options will be adequate for many purposes, VORTEX also provides you with 
access to a much more extensive graphing utility. To fine-tune your graphs, right-click on the graph and 
select Properties. That will bring up an Advanced Graph Properties window that gives you considerable 
control over almost all aspects of the graph (Figure 49). 
 
 
Figure 49. Advanced Graph Properties. 


 
VORTEX Version 9.50 User’s Manual 
 
85 
Chapter 4 
Viewing Model Results 
Project Report 
 
The Project Report tab takes you to a simple word processor utility that you can (and should) use to 
document your work and begin to develop a report for sharing with others (Figure 50). 
 
 
Figure 50. The Project Report. 
 
In the earlier sections for Project Settings, Text Output, and Graphs and Tables, you had the option to 
send text, tables, and graphs to your Project Report. This is where you were sending them! It is always a 
good idea to liberally send information to your Project Report whenever you think that it may be 
information that you will want to capture for inclusion in project reports of any sort. It is always easy later 
to edit or delete sections of your Project Report, but it may be difficult to later resurrect information that 
you neglected to send to the report.  
 


VORTEX Version 9.50 User’s Manual 
86 Chapter 4 
Viewing Model Results 
The Project Report gives you tools for standard format changes, including fonts, colors, italics, bold, 
alignment, and bullets. You also have the option to Save, Open, or Print reports. VORTEX automatically 
saves your Report with the Project, and re-loads it when you open the Project again. You only need to 
explicitly Save a Report if you wish to save it under a new filename. When you save a report, it is saved 
in Rich Text Format (an .rtf file). Such files can be imported directly into MS Word and most other word 
processors, where you can use their more powerful editing capabilities to further refine your report.  
 
Access to Other Stored Output 
 
The results made available to you in the Text Output and Tables and Graphs sections of VORTEX are all 
stored in text files (with extensions .inp, .det. .out, .dat, .sum, .run, and .rtf) placed into your Project 
directory. You can access these files directly if you wish to view the data within other word processing, 
spreadsheet, database, or graphical software. However, if you wish to edit these files in any way, you 
should first make a copy of the files and then edit only the copy. If you change the files that were created 
by VORTEX, you may make the data inaccessible when you re-open your Project. Another file that you 
should not edit is the file with extension .vpj. This “vortex project” file is the master file that stores the 
data for your Project. Any changes made to this file outside of the VORTEX program can cause your 
Project to be corrupted and possibly un-openable.  
 
In addition to the results made available to you within VORTEX, the program stores other results in 
additional files that are placed into your Project directory. Some of these additional files contain more 
detailed results (often, far more detailed than most users would care to examine). These files typically are 
text files with semi-colon delimiters, formatted so that they can be opened directly into Excel and many 
other spreadsheet and database programs. Which additional files are created depends on the settings you 
select in the Special Options of the Project Settings. Available files include (in which “project” is 
replaced by the name of your Project, and “scenario” is replaced by the name of the Scenario): 
 
project_scenario.run  
A listing for each iteration of the year the population went extinct (if it 
did go extinct), and (if it did not go extinct) the final population size, 
gene diversity, mean inbreeding, and number of founder alleles. 
 
project_scenario.ani  
A listing for each iteration of the animals living at the end of the 
iteration, including their sex, age, inbreeding coefficient, and genotypes 
at the modeled loci.  
 
project_scenario.gen  
A listing of final allele frequencies and probabilities of allele persistence, 
averaged across the iterations, for the first locus modeled.  
 
project_scenario_Iter#.gp  
A listing in GenePop format of the individuals alive at the end of the 
iteration, including their sex, age, inbreeding coefficient, and genotypes 
at the modeled loci.  
 


 
VORTEX Version 9.50 User’s Manual 
 
87 
Chapter 5 
Sensitivity Testing 
Chapter 
 
 
Sensitivity Testing 
 
 
 
An important part of any Population Viability Analysis is the testing of 
alternative values for some model parameters. There are a variety of 
reasons that we need to test the sensitivity of model projections to changes 
in parameter values. First, we never know all the values as precisely and 
accurately as we would want (especially when the analysis is focused on an endangered species, for 
which – almost by definition – it will be hard to obtain large sample sizes for estimating population 
parameters). Sensitivity testing is essential to document the uncertainty in the model projections that 
result from uncertainty in input parameter values. Second, sensitivity testing can reveal which model 
parameters are key factors that strongly determine population dynamics. Fortunately, often some of the 
parameters that we can estimate only crudely (if at all) are ones that when tested with alternative plausible 
values are found to have very little impact on model results. For example, in a population of several 
thousand individuals, it is unlikely that inbreeding will occur frequently enough for it to matter what 
number we use as a guess for the number of lethal equivalents in the population. Knowing which model 
parameters are strong determinants of population dynamics can help us understand what parameters need 
to be estimated more accurately (perhaps through further field studies), and what factors might be 
effective targets for management. Finally, although the testing of various proposed management strategies 
is not usually considered “sensitivity testing”, the process of testing options is much the same as testing 
uncertain parameters. See Appendix I for further discussion of the use of sensitivity testing in PVA.  
 
It should be noted that tests of “sensitivity” and the related concept of “elasticity” are often defined in 
formal mathematical ways by modelers (see Starfield and Bleloch 1986; Burgman et al. 1993; Caswell 
2001). In this manual, “sensitivity testing” is used in a more generic way to refer to any evaluation of the 
impact on model results of changes in input parameter values. Partly, this more generic use of the concept 
reflects our view that it is more meaningful to test the effects of the likely or plausible (or planned) range 
of each parameter than to vary every tested parameter rigidly by constant proportions. (It is not clear to us 
that there is even any useful meaning to a comparison of the effects of 10% variation in, say, breeding age 
to the effects of 10% variation in the number of lethal equivalents driving inbreeding depression.) 
However, with the flexibility provided by VORTEX, you are free to conduct sensitivity tests in whatever 
formal or loosely structured ways you may deem useful.  
 
In Chapter 3, you learned how to create new Scenarios from an existing Scenario, in order to test 
alternative sets of input values. The new Sensitivity Testing module of VORTEX allows you to more 
rapidly create sets of Scenarios that vary input parameters of concern. To open this module, select the 
“ST” button on the top toolbar. This will open the window shown in Figure 51. This window has two 
subsections – one to “Setup Scenarios” and one to examine “Comparative Results” in tables and graphs.  
 
5


VORTEX Version 9.50 User’s Manual 
88 Chapter 5 
Sensitivity Testing 
The Sensitivity Testing module is still undergoing testing and refinement. Although it should 
give correct results, and can be a very convenient and powerful way to quickly analyze and 
present sensitivity tests, it is also likely that some bugs remain that will cause the program to 
crash with certain combinations of ST analyses, or will cause you to endure features that are 
not yet very user friendly. Save a copy of your project before entering the ST module! 
 
 
Figure 51. The Sensitivity Testing window. 
 
To set up a Sensitivity Test analysis, you must first have created one or more Scenarios that you will use 
as “Baseline” templates, from which you will alter one or more input parameters. Click on “Add 
Analysis”, select the pre-existing Scenario that will serve as your Template; type a name for this 
Sensitivity Analysis (this can be any name that is descriptive to you); and specify the Level code (any 
number) of the first variant Scenario that you will create from the Baseline (Figure 52). Then, for each 
variable that you will modify in synchrony (as opposed to parameters that you might alter in independent 
Sensitivity Tests), select from the dropdown list which input parameter is to be changed, and specify the 
value to which you want it changed. In specifying the new value of an input variable, you can enter either 
a number, or you can enter a function of the value used in the Baseline model. To specify the new value 
as a function of the Baseline value, enter a function in which ‘B’ represents the value in the Baseline 
Scenario. For example, “=B+10” would increase the value in the Baseline by 10, while “=B*1.10” would 
increase it by 10%.  
 


 
VORTEX Version 9.50 User’s Manual 
 
89 
Chapter 5 
Sensitivity Testing 
While most Sensitivity Tests would vary just a single input parameter, at times you will want to vary 
several at once. For example, within a single Sensitivity Test, you may want to shift mortality rates of 
both males and females, or both juveniles and adults. Or you may want to change the EV in mortality in 
synchrony with mortality, so that the ratio of EV to the mean remains constant through your tests. You 
can change as many as 10 input parameters in synchrony in the ST module.  
 
 
Figure 52. Adding a Sensitivity Testing Analysis. 
 
To add new levels (alternative values of the parameter to be tested), click on the “Add Level” button, 
specify a new code for Level, and specify the Variable(s) and Value(s). Most commonly, the Level codes 
for an ST Analysis would be 1, 2, 3, etc. However, the codes that you specify will determine the order of 
placement of data on tables and graphs, so there are often reasons to choose values that have meaning 
with respect to the ST Analysis (e.g., you might use Levels 5, 10, 15, and 20 to code ST Scenarios that 
vary mortality from 5%, 10%, 15%, and 20%) or that have correspondence among multiple ST Analyses 
(see below). The Baseline Scenario is always treated by VORTEX as Level = 0.  
 
It might not make much sense to change different input parameters in the different Levels of a given 
Sensitivity Test, when the Sensitivity Test is used to examine uncertain parameters, but VORTEX will let 
you do this if you are so inclined. However, if the different Levels of your Analysis represent alternative 
proposed management strategies to conserve a species, you may well need to change different input 
values to represent the various desired Scenarios.  


VORTEX Version 9.50 User’s Manual 
90 Chapter 5 
Sensitivity Testing 
 
To add a new, independent ST analysis, click on “Add Analysis” and repeat the above steps to specify the 
Baseline, Analysis name, Level, Variable(s), and Value(s). Figure 53 shows the setup for three ST 
Analyses, in which Sex Ratio, the number of Lethal Equivalents, and the % of Adult Females Breeding 
are each varied by from -20% to +20%. Note that the Level codes reflect the percent change in each 
variable. Note also that there was no need to explicitly create a Level = 0 for each ST Analysis, because 
the Baseline Scenario is, by default, the Level = 0 case. For the test of Lethal Equivalents, the values were 
entered directly, rather than as a function of the Baseline. This was necessary because the Lethal 
Equivalents input parameter is one of the few that cannot be specified as a function in VORTEX. 
 
 
Figure 53. Setup for three ST Analyses. 
 
After ST Analyses are set up, and you hit “OK” to exit the ST module, it is wise to save your project (in 
case something goes badly wrong while you experiment with the new ST module!). Each Level of each 
ST Analysis that you specified is then created by VORTEX as a new Scenario, and it can be viewed in the 
Simulation Input section of the program. These ST Scenarios will be labeled with codes that reflect the 
baseline, ST Analysis, and Level. You can toggle through the ST Scenarios in Simulation Input, just as 
you would any other Scenarios that your created. However, you cannot use the scrollbars to move around 
within each input screens of the ST Scenarios unless you check the box at the bottom of the Project 
Settings window to “Make input screens active for viewing ST Scenarios”. Even when you make input 
screens active for ST Scenarios, you should not change any of the input values in the ST Scenarios. Any 


 
VORTEX Version 9.50 User’s Manual 
 
91 
Chapter 5 
Sensitivity Testing 
changes that you make to ST Scenarios within the Simulation Input will be ignored and discarded when 
you save your Project. This is because the ST Scenarios are never actually fully created in your VORTEX 
Project. Instead, VORTEX creates the ST Scenarios from the specified Baseline at the time that you choose 
to run the ST Scenarios. Similarly (and for the same reason), any changes that you make to Notes for ST 
Scenarios will be discarded when you save your Project. If you change some input values in a Baseline, 
the corresponding values will change in each ST Scenario based on it. This can be very useful, if you 
decide after creating some ST Analyses to make a change in some value in the Baseline and all ST 
Scenarios created from it, but it can also be dangerous if you are not aware of what VORTEX is doing in the 
ST module. 
 
After setting up ST Analyses, and saving your Project, you can then run these ST Scenarios by going to 
the Run window, which will now show the ST Scenarios as being available for running (Figure 54).  
 
 
Figure 54. The Run Simulation window, showing Scenarios created in ST Analyses. 
 
After running any ST Analysis Scenarios of interest, you can return to the ST module to view the results 
in tables and graphs. To assess your ST results, click on the Comparative Results tab (Figure 55). The 
first choice you make on this screen is to display results from one ST Analysis, for one or more measures 
of population performance or viability (select “Single ST Scheme” in the top dropdown list) vs. display 
results for Multiple ST Analyses, for a single measure of population viability (select “Multiple ST 
Schemes”). I.e., your results will be compared across one or more Variables for a single ST Analysis, or 
across one or more ST Analyses for a single Variable. (To compare multiple Variables for Multiple ST 
Analyses would require one more dimension than can be easily displayed or interpreted!) 
 
If you choose a Single ST Scheme, you select that ST Scheme from the next dropdown list, and then 
select the one or more variables that you want displayed. The window for selecting the Variable(s) is the 


VORTEX Version 9.50 User’s Manual 
92 Chapter 5 
Sensitivity Testing 
same as the one used in the Graphs and Tables section of the program. If you choose Multiple ST 
Schemes, you select the output Variable that you want displayed, and then choose which ST Analyses 
you want to compare. You next Population and Year for which you want to view Comparative Results. 
Then specify if you want to “Group by ST Level” – which means that the ST Level will be the columns of 
the table and x-axis of the graph – or “Group by Variable/ST Scheme” – which means that ST Level will 
be the rows of the table and the lines on the graph. (Try it both ways to see the difference in how the data 
are displayed.) 
 
Figure 55 shows a Data Specification for examining three output Variables from a Sensitivity Test of the 
effect of varying the Sex Ratio. As in the Tables and Graphs section of the program, a table of results is 
produced that can be printed, sent to your report, or exported.  
 
 
Figure 55. Comparative Results section of the ST module. 
 
Figure 56 shows the graph of these results, obtained by clicking on the Data Graphs tab. You can improve 
the axes, labeling, and other aspects of the graph by using the provided Graph Options, or by right-
clicking on the graph to open the Graphics Properties window. The graph shows which Variable has the 
greatest response to the input value for the parameter that was examined in this Sensitivity Test. (In this 
case, probability of population survival was strongly influenced by sex ratio, with more males causing 
lower population viability.)  
 


 
VORTEX Version 9.50 User’s Manual 
 
93 
Chapter 5 
Sensitivity Testing 
 
 
Figure 56. A Data Graph from the Comparative Results section of the ST module. 
 
A more interesting comparison from the Sensitivity Tests is the comparison across multiple ST Schemes, 
to see which input parameter has the greatest impact on population viability. Figure 57 shows the graph 
for a comparison of the sensitivity to Sex Ratio, Lethal Equivalents, and %Breeding. In this case, varying 
Lethal Equivalents is seen to have little or no impact on population survival (with the modest differences 
due perhaps simply to sampling error because relatively few iterations were run). Increasing Sex Ratio 
(more males) damages population survival, while increasing % Breeding improves the probability of 
population survival by about the same amount. By coding the Levels differently, you can get the lines to 
all be increasing, or all decreasing, if you so wish.  Plots of this type, for comparing sensitivity of model 
results to several input parameters are called “spider plots” (for an obvious reason) and can be a 
convenient way to illustrate Sensitivity Test results. You can also use bar charts or other graph types to 
show your results. Experiment with graphing options to see what kinds of graphs can be produced by 
VORTEX. 
 
 


VORTEX Version 9.50 User’s Manual 
94 Chapter 5 
Sensitivity Testing 
 
Figure 57. A “spider plot” comparing sensitivity to three input parameters. 
 
 
There are several easy ways to copy any graph from VORTEX into a Word document, a 
PowerPoint slide, or another external document. You can hit the Export Graph button to 
create a bitmap (.bmp) file, or you can send the graph to your report and then from there 
copy (Ctrl-C) and paste (Ctrl-V) it into another document. Either of these methods transfers 
the graph in a format that requires a lot of disk space. Alternatively, you can open the Graph 
Properties by right-clicking on the graph, then go to the System tab to Export the image in 
WMF format to the Windows clipboard or to a file. WMF format images require very little disk 
space.  
 


 
VORTEX Version 9.50 User’s Manual 
 
95 
Chapter 6 
Using Functions in VORTEX 
Chapter 
 
 
 
Using Functions  
in VORTEX 
 
Introduction 
 
VORTEX provides the option of modeling demographic rates as functions of population or individual 
parameters. The population descriptors that can be used as variables in the functions include time (year in 
the simulation), iteration, population, population size, carrying capacity, numbers of juveniles (animals in 
the first age class), subadults (greater than 1 year, but not yet breeding age), adult females, adult males, all 
females, or all males, and gene diversity (expected heterozygosity). Individual characteristics that can be 
entered as variables in these functions include ID#, sex, age, number of mates (0 or 1 for females and 
monogamous males; possibly more for polygamous males), inbreeding coefficient, and genotypes at 
modeled loci. Almost all demographic rate parameters – such as the percent of females breeding each 
year, environmental variation in breeding, litter/clutch size, sex ratio, mortality rates, environmental 
variation in mortality, catastrophe frequency and severities, carrying capacity, dispersal, dispersal 
mortality, occurrence of harvest and supplementation, and definition of extinction – can be specified to be 
functions of the above population and individual variables.  
 
The flexibility to specify population rates as functions rather than as fixed constants has been added to 
VORTEX so that users can model specific population dynamics that might be known to be appropriate for 
some species, or that are of interest in a theoretical analysis. With some creativity and perhaps 
considerable effort, VORTEX can now model many of the kinds of population dynamics that can be 
envisioned. As just a few examples: 
 
¾ it might be known that carrying capacity will change at some determined date in the future; 
¾ it might be believed that reproductive rates will change over time, perhaps due to some 
management action; 
¾ the density dependence observed in reproduction might not fit the shapes of the curves allowed in 
previous versions of VORTEX; 
¾ mortality rates might change over time, or respond in a complex way to population density; 
¾ inbreeding might impact fecundity, adult survival, or might affect the two sexes differently; 
¾ dispersal might be age and sex dependent; 
¾ fecundity, mortality, or the effects of catastrophes might be age-dependent; 
¾ environmental variation might occur with a periodicity that is longer than a year, or catastrophes 
might have multi-year effects. 
 
Note that VORTEX includes within the basic data entry screens the option to model reproduction as a 
density dependent function, and an option to model carrying capacity as having a linear change over a 
6


VORTEX Version 9.50 User’s Manual 
96 
Chapter 6 
Using Functions in VORTEX 
specified number of years. Easy access to these two particular functions are provided because they are 
needed more frequently than are detailed functional dependencies of most other rates. Even for these two 
rates, however, you can specify these functions to have almost any shape if you use the function editor to 
specify the rates.  
 
For most users and for most purposes there will be no need or desire to model demographic rates as 
functions; it is usually fully adequate to specify fixed demographic rates rather than functions. 
Specification of rates as functions can be difficult: the appropriate form of the function is rarely known, 
the function parameters are usually very difficult to estimate, and it is not trivial to enter a function 
correctly. If alternative functions need to be examined in sensitivity testing, the number of combinations 
of input parameters to be explored can quickly become overwhelming. Consequently, we would not 
recommend that novice users or students use the function option within VORTEX.  
 
Specification of Demographic Rates as Functions 
 
Dependencies of demographic rates on population and individual parameters are entered into VORTEX by 
specifying the functional relationships. There are two ways that you can enter a function rather than a 
constant for an input variable: you can type the function directly into the input box for specifying the rate, 
or you can open a Function Editor to help you develop the function to describe the relationship. VORTEX 
provides an option (and this option is the default for new Projects) to have the Function Editor open 
automatically whenever you enter a “=” as the first character in an input box for a demographic rate. The 
other way to open the Function Editor is to click on the Function Editor icon on the toolbar. If you type a 
function directly into an input box, you must precede the function with an “=” sign (to distinguish the 
specification of a rate as a function rather than as a constant). If you open the Function Editor by typing 
an “=” in an input box, and then develop a function within the Function Editor, then the Function Editor 
will insert the function back into the active input box when you accept the function. It is usually easier 
(and safer) to build a function first within the Function Editor and then send it over to the input screen.  
 
 
Figure 58. The Function Editor utility. 
 


 
VORTEX Version 9.50 User’s Manual 
 
97 
Chapter 6 
Using Functions in VORTEX 
When you open the Function Editor (Figure 58), you can enter the desired function by typing it into the 
box at the top of the window, or you can use the screen keypads to select numbers, operators, and 
functions, which will then be pasted into the function box. It is probably fastest to just type the function 
you want, but the keypads can help remind you what operators, trigonometric functions, Boolean 
operators, and other functions are available for use. The population and individual variables available for 
use in functions are listed in a box in the lower part of the Function Editor window (see Table 1). The 
Function Editor also keeps a list of recently used functions, and they can be recalled (and further edited, if 
desired) by clicking of the drop-down list in the Function box.  
 
In specifying a function, you should make no assumptions about the order of precedence of operators (see 
Table 2 for list of valid operators). For example, the function A+B*C is interpreted as (A+B)*C. 
(Precedence is left to right, so VORTEX interprets A*B+C in the standard way, but it is risky to assume that 
VORTEX will read a function the way you would read it.) Always use parentheses to specify the order in 
which operations are to be performed. (Parentheses), [brackets], and {braces} may be used 
interchangeably to indicate the order of operations. 
 
The case of function names and variables is ignored. All letters that are entered in a function within the 
Function Editor are converted to upper case by VORTEX.  The separator used between variables in a binary 
operator must be a semi-colon (;), not a comma (,), to avoid problems arising from the comma being used 
as a decimal separator with some regional data settings. (See the examples in Table 2, below.) 
 
It can be difficult to correctly specify the function that describes the relationship you want for a 
demographic rate. To help you confirm that you have specified the correct function, VORTEX can display a 
simple x-y Function Preview plot of any function entered into the Function Editor. From the drop-down 
list above the graph, you must select which dependent variable from your function should be plotted 
along the x-axis. The plot will show the relationship to the selected x-variable, with each other dependent 
variable fixed at some simple value (e.g., sex = female, K = 100, N = 100, numbers of males, females, 
juveniles, and subadults = 50, iteration = 1, year = 1, population = 1, gene diversity = 100%, inbreeding = 
0). You can change the range and increment of the x-axis if you wish. The Function Preview graph will 
not display until you click the “Update Graph” command.  
 
If you know how to read reverse Polish notation for functions, you can click the command to “Show 
Polish Notation” in order to confirm that VORTEX is interpreting the parentheses to produce the order of 
operations that you desired.  
 
After you have confirmed that you have the function that you want, you can cut and paste it into an input 
box, or (if you triggered the Function Editor by typing an ‘=’ into an input box) just hit ‘OK’ to transfer 
your function over to the input box you had left.  


VORTEX Version 9.50 User’s Manual 
98 
Chapter 6 
Using Functions in VORTEX 
 
 
 
Table 1. Valid Function Variables 
 
Population descriptors 
N = Population size   
K = Carrying capacity   
Y = Year   
P = Population identifier 
R = Run (simulation iteration) 
M = Number of adult males in the population   
F = Number adult females 
J = Number of juveniles (age 0-1)   
U = Number of subadults (age > 1, < breeding age) 
X = Number of females (all ages) 
W = Number of males (all ages) 
G = Percentage of initial gene diversity (expected heterozygosity) remaining in the population 
D = Dispersal rate (from the matrix entered), used only in functions modifying dispersal. 
 
NN(p), KK(p), MM(p), FF(p), JJ(p), XX(p), WW(p), GG(p) = the 
parameter above (N, K, etc.) for population p.  
PP = Recipient population of a dispersing individual, for use in Dispersal Modifier functions. 
 
PS1, PS2, PS3, … , PS9 = Population State Variables previously defined. 
PPS1(p), PPS2(p), etc. = Population State Variables for population p. 
 
Individual descriptors 
A = Age 
O = Individual ID (an arbitrary integer assigned to each individual); O = ID of dam when 
testing acceptability of mates against optional criteria. 
S = Sex (0 or ‘F’ for female, 1 or ‘M’ for male) 
I = Inbreeding coefficient (must be expressed as a percentage) 
Q  = Number of mates (0 or 1 for females, possibly more for polygamous males) 
V = Paternal allele identifier 
Z = Maternal allele identifier 
VV(i) and ZZ(i) = the paternal and maternal alleles at the ith modeled locus.  
 
IS1, IS2, IS3, … , IS10 = Individual State Variables previously defined. 
IIS1(i), IIS2(i), …  = Individual State Variables for the ith individual (ID). 
 
Tallies 
CAT(c) = Number of years since last occurrence of Catastrophe type c. (c > maximum 
years, if catastrophe has not yet occurred.) 
ITOT(i) = Total, across living individuals in the population, of ith state individual variable. 
IMEAN(i) = Mean, across individuals in the population, of ith state individual variable. 
IITOT(p;i) = Total, across individuals in population p, of ith state individual variable.   
IIMEAN(p;i) = Mean, across individuals in population p, of ith state individual variable. 


 
VORTEX Version 9.50 User’s Manual 
 
99 
Chapter 6 
Using Functions in VORTEX 
 
Table 2. Valid Operators   (Note that there are alternative names for several operators.) 
 
Function 
Description 
Example 
Unary Operators 
 
ABS 
Absolute value 
ABS(-10) = 10 
NEG 
Negative 
NEG(-10) = 10 
CEIL 
Ceiling 
CEIL(3.12) = 4 
FLOOR 
Truncate 
FLOOR(3.12) = 3 
ROUND 
Round 
ROUND(3.12) = 3 ; ROUND(5.5) = 6 
SQRT, SQR 
Square root 
SQR(1.44) = 1.2 
LN, LOG 
Natural logarithm  
LN(1.60) = 0.47 
LOG10 
Base 10 logarithm  
LOG10(1.60) = 0.20412 
EXP 
e raised to specified power 
EXP(0.47) = 1.60 
Binary Operators 
 
+ 
Addition 
1.0+2.0 = 3.0 
- 
Subtraction 
2.0–1.0 = 1.0 
* 
Multiplication 
2.0*3.0 = 6.0 
/ 
Division 
6.0/2.0 = 3.0 
POW, ^ 
Exponentiation 
POW(10;0.20412) = 10^0.20412 = 1.60 
MAX 
Maximum 
MAX(3.12;4.21) = 4.21 
MIN 
Minimum 
MIN(3.12;4.21) = 3.12 
MOD, % 
Modulus (Division remainder) 
MOD(33;10) = 33%10 = 3; MOD(33.5;5) = 3.5 
Logical (Boolean) Operators 
 
==, = 
Is equal to 
(3=2) = 0 = FALSE 
NOT, ! 
Negation 
!(3=4) = 1 = TRUE 
!=, # 
Not equal to 
(3#4) = 1 
AND, && 
And 
((3=4)AND(3#4)) = 0 
OR, || 
Or 
((3=4)OR(3#4)) = 1 
> 
Greater than 
(3>4) = 0 
< 
Less than 
(3<4) = 1 
>= 
Greater than or equal to 
(3>=3) = 1 
<= 
Less than or equal to 
(3<=3) = 1 
Trigonometric Operators 
 
SIN 
Sine 
SIN(PI/2) = 1.0 
COS 
Cosine 
COS(PI/2) = 0.0 
TAN 
Tangent 
TAN(PI/4) = 1.0 
ASIN 
Arcsine 
ASIN(1.0) = 1.5707963 
ACOS 
Arccosine 
ACOS(0.0) = 1.5707963 
ATAN 
Arctangent 
ATAN(1.0) = 0.7853981 
Defined Constants 
 
PI 
3.1415927 
SIN(PI/4) = 0.7071067 
E 
2.7182818 
LN(E) = 1.0 
TRUE 
1 
(10>5) = TRUE 
FALSE 
0 
!TRUE = FALSE 
Random Number Generators 
 
RAND 
Uniform random (0 – 1) 
RAND = 0.2341 or 0.8714 or 0.9151 or … 
NRAND 
Normal random deviate 
NRAND = 0.512 or –0.716 or –2.376 or … 
SRAND 
A “seeded” random number generator; hence, SRAND(x) provides a random number between 
0 and 1 with a given seed value x 
SNRAND 
 
A “seeded” random normal deviate; hence, SNRAND(x) returns a number from a (0,1) normal 
distribution with the seed value x


VORTEX Version 9.50 User’s Manual 
100 Chapter 6 
Using Functions in VORTEX 
Using Random Numbers in Functions 
 
Random number generators can be used to create a wide variety of stochastic events (for example, a 5-
-year drought that occurs on average once every 30 years), but the proper use of these functions requires 
careful consideration of how the “seed” values (implicit, as in RAND and NRAND, or explicit, as in SRAND 
and SNRAND) determine when new random numbers are selected. Repeated calls to the random number 
return the same value if the same seed is specified. Random numbers produced with different, even 
sequential, seeds will not be correlated. The “unseeded” forms (RAND and NRAND) set their own unique 
(or nearly so) seed each time they are called. The very first use of a random number generator in VORTEX 
uses a seed based on the number of seconds elapsed since the turn of the century. Each call to an 
unseeded random number generator also sets a new seed for the next call for an unseeded random 
number. Thus, identically configured computers starting the same simulation at exactly the same second 
on their clocks would produce identical results for an analysis. This synchrony may require, however, that 
all memory storage locations (including hard disk caches) and even the hard disk contents are identical on 
the systems (because they will affect the time required for each read or write to the disk). 
 
The specification of random number seeds allows synchronization of sequences of random numbers. This 
can be used to create synchrony of events, such as catastrophes or environmental variation across 
populations, or autocorrelations among years (time lags or cycles). If several different demographic rates 
are specified by functions containing random number generators (perhaps to trigger separate catastrophes 
impacting survival and fecundity), care must be taken to create the desired synchrony or lack of 
synchrony. If two functions contain the same seed values, they will return the same random number. Seed 
values must be distinct to create independence of random numbers. (See examples below.) 
 
Proper use of random number seeds can be difficult. Think carefully about the effect of any seed that you 
use in a function, to be certain that it will produce the same random numbers when you want them, and 
independent random numbers otherwise. Any variable (e.g., A for age, Y for year, R for run, P for 
population) included within the seed will cause the same “random” number to be chosen for each case 
with the same value for those variables (A, Y, R, P). For example, if you specify SRAND(P) within a 
function, then each population will get an independent random number, and that set of random numbers 
will be the same over all calls to evaluate that function (such as for every year, every run, and every 
individual within each population). If you specify SRAND((P*100)+Y), then each population will get a 
new independent random number each year of the simulation, but the set of random numbers will be the 
same across all runs of the simulation. You would normally want to include the variable R in the random 
number seeds (e.g., SRAND((R*10000)+(P*100)+Y)), in order to cause the random numbers to be 
independent among runs. See the examples below for further information about random number seeds. 
 
The seeds used by VORTEX will be converted to integers between 0 and 65536. Non-integer seeds will be 
truncated [hence, SRAND (35.23) = SRAND(35.89)] and values above 64K will be “wrapped” [the 
modulus taken, so that SRAND(65636) = SRAND(100)].  
 
Notes Regarding Function Syntax and Use 
 
• 
Variables of trigonometric functions are assumed to be in radians. 
• 
The operator NEG is the same as using a minus (-) sign before a number. By the context, VORTEX 
will interpret whether a minus sign signifies subtraction (a binary operation) or the negative (a 
unary operation). 
• 
CEIL, FLOOR, and ROUND convert real numbers to integer values, but all expressions are 
evaluated as real numbers. For example,  


 
VORTEX Version 9.50 User’s Manual 
 
101 
Chapter 6 
Using Functions in VORTEX 
 
FLOOR(3.7)/FLOOR(4.1) = CEIL(2.1)/CEIL(3.7) = ROUND(3.1)/ROUND(3.6) = 0.75. 
• 
Numbers may be written with or without leading and trailing zeroes. Decimal points for integral 
values are optional. For example, all of the following are valid expressions: 3, 3.00, 0.03, 
.03, -0.30, -5. 
• 
Functions containing invalid mathematical expressions are prohibited, such as: 
SQR(-10) 
Square root of a negative number 
LN(-10) 
Natural log of a negative number or zero 
5/0  
Division by zero 
TAN(1.5707963) Tangent of PI / 2 
ASIN(1.1) 
Arcsine or arccosine of a value greater than 1 or less than –1 
• 
Some mathematically valid functions would be ambiguous or meaningless. For example, functions 
of carrying capacity (K) should not contain K as an independent predictor (of itself). Functions of K 
should also not include A (age) or S (sex) as parameters, because the condition of exceeding the 
carrying capacity is a population-level phenomenon, and K is assessed once for each population 
each year. If K is a function of inbreeding (I), the value of I applied in the function will be the 
mean for the population. 
• 
The total length of a function cannot exceed 1024 characters. Functions cannot contain more than 
64 numerical constants, or more than a total of 256 constants plus variables plus operators. (Often 
you can find an alternative form that is shorter. At least we hope that you never need to use a 
function longer than this!)   
• 
Many of the variables that can be used in rate functions will themselves change during each year of 
the simulation. In order to avoid irresolvable interdependencies of parameters and rates, the 
population size (N) and sizes of subsets (J, F, M, U, X, W) and gene diversity (G) used in function 
evaluations are the numbers that were tallied at the last (pre-breeding season) census. 
• 
Even without specifying rates as functions, many of the rates used in VORTEX can be specified to be 
different for different years, sexes, ages, or inbreeding levels. (e.g., age-specific mortality, 
inbreeding depression in juvenile mortality, linear trends in K, etc.) Be aware that the effects of any 
functions entered are imposed on top of such dependencies that might be given in the standard input 
format. For example, EV in carrying capacity could be specified via standard input, or via a 
function of the type  
K = 100+(10*NRAND), 
thereby giving an annual level of EV in K equal to a standard deviation of 10. The advantage of 
creating EV by specification within functions (rather than more simply as a parameter given to 
VORTEX) is that you have greater control over how EV is implemented in the model. For example, it 
is possible to specify that EV is concordant between two populations (but not with others):  
RATE = 50+[10*SNRAND(Y+(R*100)+[(P>2)*100*SRAND(P)])]. 
In this function, the overall mean demographic rate is 50 with annual fluctuations due to EV (SD) 
equal to 10. Populations 3 and greater will experience independent annual fluctuations, while 
populations 1 and 2 will fluctuate synchronously. The use of year (Y) in the seed for the random 
number causes a new random number to be used each year. The use of R (iteration or run) in the 
seed causes the sequence of seed values to be different in each simulation. The inclusion of 
(P>2)*100*SRAND(P) within the seed causes a different sequence of random numbers to be 
chosen for each population after the first two have been evaluated. The seeds must include 
Y+(R*100) to ensure that every year-iteration is independent. (If you use Y+R as the seed, then 
year 3 of iteration 1 will have the same value as year 2 of iteration 2, etc.) In the simpler example of 
EV in K given above, no seed was needed or specified, so an independent random number will be 
selected each iteration, each year, and each population. These examples show how elaborate and 
non-intuitive the functions can become when you want to create even moderately complex models 
of population dynamics. 


VORTEX Version 9.50 User’s Manual 
102 Chapter 6 
Using Functions in VORTEX 
 
Using Functions to Examine Genetic Evolution 
 
The parameters available for use in functions defining demographic rates include an individual’s 
paternally inherited allele (V) and the maternally inherited allele (Z) of the (normally) non-selected locus, 
which is monitored for tracking genetic diversity. (The symbols for these variables V and Z have no 
intuitive meaning, but are rather the result of few letters remaining available for denoting additional 
parameters for functions.) By specifying that demographic rates are functions of the alleles carried by an 
individual, it is possible to model a wide variety of genetic processes impacting population dynamics, 
including: the effect and fate of alleles that confer alternative life history strategies (e.g., lower fecundity 
but higher survival); balancing, disruptive, or directional selection for alleles impacting demography; 
hybrid vigor or outbreeding depression caused by introgression of alleles from a distinct taxon or 
geographic population; and genetically based individual variation in demographic rates. 
 
When the initial population is created, and when the population is supplemented with any new 
individuals, the founders are assigned unique alleles sequentially. Hence the first individual of the 
Population 1 is assigned alleles 1 and 2, the second individual is assigned alleles 3 and 4, and so on. Final 
frequencies of all founder alleles in each population, averaged across all iterations, can be outputted to a 
file if that option is selected within Special Options of Project Settings. The allele frequencies are placed 
into a file with extension .gen. 
 
Examples of Rate Functions 
 
The easiest way to demonstrate the formats in which functions can be entered into VORTEX is with a series 
of examples. The examples shown below include a plot of the function where appropriate as well as the 
actual expression. 
 
1. Continuous linear decline over time 
 
RATE = 50–(0.2*Y) 
 
This function specifies a starting rate 
(perhaps for adult female breeding success or 
for carrying capacity) equal to 50 in year 0, 
with a decline of 0.2 per year resulting in a 
rate equal to 30 after 100 years. 
 
 
 
 
 
 
 
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


 
VORTEX Version 9.50 User’s Manual 
 
103 
Chapter 6 
Using Functions in VORTEX 
2. Linear decline limited to a period of years 
 
RATE = 50–(0.2*MIN((Y-1);50)) 
 
In this case, the decline occurs only through 
the first 50 years of the simulation. Note that 
the decline is specified to start in year 2, so 
that year 1 still has a rate of 50. This is the 
form of the function used by VORTEX if the 
user specifies a linear trend in carrying 
capacity. 
 
 
 
 
 
 
 
3. Linear decrease during intervals of years 
 
RATE = 50–(5*(MIN(5;Y)+((Y-25)*(Y>25)))) 
 
The rate starts at 45 in year 1, declines to 25 
by year 5, and again resumes the decline at a 
rate of 5 per year after year 25. 
 
 
 
 
 
 
 
 
 
 
 
4. Exponential decline 
 
RATE = 50*(0.98^Y) 
 
The rate declines by 2% each year.  
 
 
 
 
 
 
 
 
 
 
 
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


VORTEX Version 9.50 User’s Manual 
104 Chapter 6 
Using Functions in VORTEX 
5. Exponential decline with inbreeding 
 
RATE = 50*EXP(-2.0*(I/100)) 
The rate declines from 50 in non-inbred 
animals down to 6.7 in fully inbred animals (I 
= 100%). Note that the inbreeding coefficient 
(I) is expressed as a percent. An equation like 
this might be used to specify a decline in 
fecundity due to inbreeding. 
 
 
 
 
 
 
 
 
 
6. Age-dependent fecundity, with linear decline after the onset of breeding 
 
RATE = (A>=5)*(50-((A-5)*2)) 
 
Breeding begins with a rate of 50 at age 5, but 
then declines by 2 each year thereafter. 
 
 
 
 
 
 
 
 
 
 
 
 
 
7. Age-dependent fecundity, with a symmetrical peak at age 15 
 
RATE = (A>=5)*(50-(ABS(A-15)*2)) 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
Inbreeding Coefficient (%)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Age (Years)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Age (Years)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


 
VORTEX Version 9.50 User’s Manual 
 
105 
Chapter 6 
Using Functions in VORTEX 
8.  Age-dependent fecundity, with an asymmetrical peak at age 10 
 
RATE = (A>=5)*[{[A<10]*([A-5]*10)}+([A>9]*[60-A])] 
Different trends are specified for age intervals 
0-4, 5-9, and 10+. Note the use of 
parentheses, brackets, and braces to improve 
readability. 
 
 
 
 
 
 
 
 
 
 
 
9. Increase in mortality with inbreeding 
 
RATE = 100-(50*EXP(-1.57*(I/100))) 
The survival rate declines exponentially 
(described by the portion within the 
outermost parentheses), while the percent 
mortality is set at 100-survival. This is the 
equation used by VORTEX to model increased 
juvenile mortality if there are 3.14 lethal 
equivalents and no recessive lethal alleles 
contributing to inbreeding depression. 
 
 
 
 
 
 
 
10. Stepwise increase 
 
RATE = 10+((Y>10)*10)+((Y>20)*10)+((Y>30)*10) 
The rate increases from 50 to 80 at 10-year 
intervals. An alternative way to express the 
same function would be 
RATE = 50+(10*(MIN(3;FLOOR( 
(Y-1)/10)))) 
 
 
 
 
 
 
 
 
 
 
Age (Years)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Inbreeding Coefficient (%)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0
80.0
90.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0
80.0
90.0


VORTEX Version 9.50 User’s Manual 
106 Chapter 6 
Using Functions in VORTEX 
 
11. Different rates at different intervals 
RATE = (10*(A<3))+(25*(A=3))+(30*((A=4)OR(A=5)))+(35*((A>5)AND(A<10)))+ 
(20*((A>=10)AND(A<15))) 
The rate increases stepwise with age, then 
drops to a lower level for years 10 through 
14, and then drops to zero for animals 15 
years and older. Note that although it can be 
tedious, any rate function can be modeled by 
specifying the rate for each interval of the 
dependent variable.  
 
 
 
 
 
 
 
 
12. Cyclical response 
RATE = 50+(10*SIN((PI*Y)/5)) 
Here the rate fluctuates between 40 and 60 
according to a sine wave with a 10-year 
periodicity. 
 
 
 
 
 
 
 
 
 
 
 
 
13. Regular pulses of a higher rate 
RATE = Y%8=0*20+30 
Background rate of 30 jumps to 50 every 8th 
year. Note that the order of operators was left 
to the VORTEX default (left to right). This is 
not a safe practice, but it does work in this 
case. 
 
 
 
 
 
 
 
 
Age (Years)
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


 
VORTEX Version 9.50 User’s Manual 
 
107 
Chapter 6 
Using Functions in VORTEX 
 
14. Pulses of longer duration 
RATE = (((Y%8)<3)*20)+30 
The rate jumps to 50 for a 3-year time span 
every 8th year. In this case, parentheses were 
used (wisely) to be sure that the intended 
order of operators was followed. 
 
 
 
 
 
 
 
 
 
 
15. Random pulses: catastrophes 
RATE = 50-(20*(SRAND(Y+(R*100))<0.05)) 
The background rate of 50 drops to 30 on 
average once every 20 years. A seeded 
random number is needed; otherwise the 
years in which the rate drops would be 
independent among individuals (effectively, 
the rate would continuously be 49). The seed 
of Y+(R*100) causes a different seed to be 
used for each year of each iteration (if there 
are 100 or fewer years). The above function is 
equivalent to specifying a catastrophe with 
frequency = 5% and severity = 0.60. 
 
 
 
16. Random pulses independent among populations 
RATE = 50-(20*[(SRAND[Y+(R*100)+(100*SRAND(P))])<0.05]) 
The “catastrophes” are independent among populations, because each population (P) sets a new (and 
random) seed for the random number generator which tests whether the catastrophe occurs. Careful 
use of parentheses (or brackets) is critical in this function, in order to ensure that the random number 
seeds work as intended. 
 
 
17. Catastrophes affecting only selected age class(es) 
RATE = 50-((A<3)*20*(SRAND(Y+(R*100))<0.05)) 
The catastrophe affects only individuals of ages 1 and 2. The 2-D graphs of this function do not  
illustrate the age-dependent relationship: The graphs against Y and R set A = 1 (and show the 
catastrophes affecting young individuals); while the graph against A happens to display a year and 
iteration (Y = R =1) in which no catastrophe for any age occurs. 
 
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


VORTEX Version 9.50 User’s Manual 
108 Chapter 6 
Using Functions in VORTEX 
18. Multi-year catastrophes 
RATE = 50-(20*(SRAND((Y/2)+(R*100))<0.10)) 
The catastrophes have a 2-year impact, 
because the seed value is converted to an 
integer, giving pairs of subsequent years the 
same random number. The frequency per year 
is 10%, so that the frequency of an onset of a 
2-year catastrophe is 5%. 
 
 
 
 
 
 
 
 
19. Multi-year catastrophes with a decreased impact in year 2 
RATE = 50-([10*(SRAND(Y+(R*100))<0.05)]+[8*(SRAND((Y-1)+(R*100))<0.05)]) 
The second seed is the same as the first seed 
from the previous year. Thus the catastrophe 
has a lesser impact (severity = 0.84 rather 
than 0.80) in the second year. This approach 
can also be used to model catastrophes which 
impact survival in one year (using a function 
with an expression like that in the first 
brackets above) and fecundity in the second 
year (using a function containing the 
expression in the second set of brackets). 
Note that in example #18, catastrophes 
always start in even-numbered years, while in 
this example catastrophes can begin in any 
year. 
 
 
20. Random variation across years 
RATE = 50+[10*(SNRAND(Y+(R*100)))] 
This is the same as imposing a mean rate of 
50 with environmental variation of SD = 10. 
 
 
 
 
 
 
 
 
 
 
 
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0
80.0
90.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Year of Simulation
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0
80.0


 
VORTEX Version 9.50 User’s Manual 
 
109 
Chapter 6 
Using Functions in VORTEX 
21. Linear density dependence 
RATE = 50*((K-N)/K) 
The rate declines from 50, at N = 0, to 0 when 
N = K. 
 
 
 
 
 
 
 
 
 
 
 
 
22. Density dependence used as the default for breeding in VORTEX 
RATE = [50-(20*[(N/K)^4])]*[N/(1+N)] 
The rate peaks near 50 when N is small, 
declines at higher densities, and is 30 when N 
= K. At very small N, the rate is also 
depressed. For example, it is reduced by 50% 
when N = 1, and reduced by 25% when N = 3. 
In terms of the coefficients that can be 
entered into the optional density-dependence 
for breeding in VORTEX, P(0) = 50, P(K) = 
30, B = 4, and A = 1. 
 
 
 
 
 
23. Density dependence, relative to the average density across populations 1 and 2 
RATE = 50*([KK(1)+KK(2)]-[NN(1)+NN(2)])/[KK(1)+KK(2)]) 
Note the use of KK(p) and NN(p) to indicate K and N for population p. 
 
24. Sex-specific dispersal rates 
RATE = D*[(S='M')OR(RAND>0.35)] 
If the above function is used for the Dispersal Modifier Function, then 35% of the females are 
prevented from dispersing. Thus, dispersal rates for females are effectively reduced by 35% relative 
to male dispersal. An unseeded random number is used so that dispersal will be determined 
independently each female. Note that the dispersal rates entered subsequently (D) will be those 
applied to males, with females having lower rates. A similar approach can be used to create age-
-specific dispersal rates (or dispersal mortality).  
 
 
Population Size
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Population Size
0
10
20
30
40
50
60
70
80
90
100
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0


VORTEX Version 9.50 User’s Manual 
110 Chapter 6 
Using Functions in VORTEX 
25. Alleles confer differential reproductive rates 
RATE = 40+(10*(V%2))+(10*(Z%2)) 
In this case, half of the alleles (specifically, 
those with even numbers) cause an increment 
of 10 in the breeding rate of their carriers. An 
individual that is homozygous for an even-
numbered allele will have a breeding rate 
equal to 60%, while those homozygous for an 
odd-numbered allele will have a rate equal to 
40%. 
 
 
 
26. Overdominance for survival, all unique founder alleles 
RATE = 20+(10*(V=Z)) 
An infinite alleles model in which homozygotes have a mortality of 30%, while the rate for 
heterozygotes is 20%.  
27. Overdominance for survival, two functionally distinct founder alleles 
RATE = 20+(10*((V%2)=(Z%2))) 
A two allele model in which homozygotes with two odd or two even alleles have a mortality of 30%, 
while the rate for heterozygotes is 20%. 
28. Outbreeding depression for breeding rate upon introgression from supplemented individuals 
RATE = 50-(10*((V<20)=(Z>19))) 
With ten initial founders, and with some number 
of individuals from another source used as 
supplements at a later stage, the breeding rate is 
50% for an individual which carries both of its 
alleles from the initial founders, or both from the 
source population of the supplements, vs. 40 for 
individuals which are heterozygous, carrying an 
allele from each source. 
 
 
 
 
29. Genetically-based individual variation in 
breeding success 
RATE = 
50+(5*(SNRAND((R*100)+V)+SNRAND((
R*100)+Z))) 
In this case, breeding rates vary around a 
mean of 50 with a standard deviation equal to 
5*SQRT(2). 
 
Allele Identifier
0
10
20
30
40
50
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Allele Identifier
0
10
20
30
40
50
Demographic Rate
0.0
5.0
10.0
15.0
20.0
25.0
30.0
35.0
40.0
45.0
50.0
Allele Identifier
0
10
20
30
40
50
Demographic Rate
0.0
10.0
20.0
30.0
40.0
50.0
60.0
70.0


 
VORTEX Version 9.50 User’s Manual 
 
111 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Appendix 
 
An Overview of 
Population Viability 
Analysis Using VORTEX 
 
 
Introduction 
 
This Appendix presents an overview of processes threatening the health and persistence of wildlife 
populations, the methods of population viability analysis, the VORTEX simulation program for PVA, and 
the application of such techniques to wildlife conservation. Much of the following material is adapted 
from Lacy (1993a) and Lacy (1993/4). 
 
The Dynamics of Small Populations 
 
Many wildlife populations that were once widespread, numerous, and occupying contiguous habitat have 
been reduced to one or more small, isolated populations. The primary causes of the decline of many 
species are obvious and deterministic: Populations are over-harvested; natural habitat is converted and 
lost to the species, often involving the replacement of diverse ecological communities with monocultures; 
environments are polluted, with the dumping of toxins into the air, water, and soil; local and now even 
global climates are modified by the actions of humans; and numerous exotic competitors, predators, 
parasites and diseases are introduced into communities that have never evolved defenses to the new 
invaders. The primary causes of species decline are usually easy to understand, and often easy to study 
and model, but usually, though not always, difficult to reverse. Even if the original causes of decline are 
removed, a small isolated population is vulnerable to additional forces, intrinsic to the dynamics of small 
populations, which may drive the population to extinction (Shaffer 1981; Soulé 1987; Clark and Seebeck 
1990).  
 
Of particular impact on small populations are stochastic, or random or probabilistic, processes. Indeed, 
the final extinction of most populations often occurs not so much because of a continuation of the 
pressures that led to the initial decline, but because of bad luck. Chance, or stochastic, processes usually 
have little impact on long-term population dynamics, as long as the population is abundant and spread 
over a wide geographic range and a number of habitats. Deterministic processes, such as those listed 
above, predominate in widespread, still common species, while local chance events impacting subsets of 
the population will average out across the broader, diverse range. When a population becomes small, 
isolated, and localized, however, chance events can become important, even dominating the long-term 
dynamics and fate of a population.  
 
I 


VORTEX Version 9.50 User’s Manual 
112 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Many stages in the life history of an organism, and the processes that define the history of a biological 
population, are essentially stochastic sampling phenomena. Births, deaths, dispersal, disease, sex 
determination, and transmission of genes between generations all are largely probabilistic phenomena. 
Small samples intrinsically have greater variance around the probabilistic mean or expectation than do 
large samples, and therefore small populations will experience greater fluctuations in births, deaths, sex 
ratio, and genetic variation than will larger populations. The fundamental problem facing small 
populations is that the fluctuations they experience due to the multiple stages of sampling each generation 
make it increasingly likely that the populations will, unpredictably, decline to zero. Once populations are 
small, the probability that they will become extinct can become more strongly determined by the amount 
of fluctuations in population size than in the mean, deterministic population growth rate. Thus, extinction 
can be viewed as a process in which once common and widespread populations become reduced to small, 
isolated fragments due to extrinsic factors, the small remnant populations then become subjected to large 
fluctuations due to intrinsic processes, the local populations occasionally and unpredictably go extinct, 
and the cumulative result of local extinctions is the eventual extinction of the taxon over much or all of its 
original range (Gilpin and Soulé 1986; Clark et al. 1990). 
 
The stochastic processes impacting on populations have been usefully categorized into demographic 
stochasticity, environmental variation, catastrophic events, and genetic drift (Shaffer 1981). Demographic 
stochasticity is the random fluctuation in the observed birth rate, death rate, and sex ratio of a population 
even if the probabilities of birth and death remain constant. Assuming that births and deaths and sex 
determination are stochastic sampling processes, the annual variations in numbers that are born, die, and 
are of each sex can be specified from statistical theory and would follow binomial distributions. Such 
demographic stochasticity will be most important to population viability perhaps only in populations that 
are smaller than a few tens of animals (Goodman 1987), in which cases the annual frequencies of birth 
and death events and the sex ratios can deviate far from the means.  
 
Environmental variation is the fluctuation in the probabilities of birth and death that results from 
fluctuations in the environment. Weather, the prevalence of enzootic disease, the abundances of prey and 
predators, and the availability of nest sites or other required microhabitats can all vary, randomly or 
cyclically, over time. The fluctuations in demographic rates caused by environmental variation is additive 
to the random fluctuations due to demographic stochasticity. Thus, the difference between the observed 
variation in a demographic rate over time and the distribution describing demographic variation must be 
accounted for by environmental variation. 
 
Catastrophic variation is the extreme of environmental variation, but for both methodological and 
conceptual reasons rare catastrophic events are analyzed separately from the more typical annual or 
seasonal fluctuations. Catastrophes such as epidemic disease, hurricanes, large-scale fires, and floods are 
outliers in the distributions of environmental variation. As a result, they have quantitatively and 
sometimes qualitatively different impacts on wildlife populations. (A forest fire is not just a very hot day.) 
Such events often precipitate the final decline to extinction (Simberloff 1986, 1988). For example, one of 
two populations of whooping crane was decimated by a hurricane in 1940 and soon after went extinct 
(Doughty 1989). The only remaining population of the black-footed ferret (Mustela nigripes) was being 
eliminated by an outbreak of distemper when the last 18 ferrets were captured (Clark 1989). 
 
Genetic drift is the cumulative and non-adaptive fluctuation in allele frequencies resulting from the 
random sampling of genes in each generation. This can impede the recovery or accelerate the decline of 
wildlife populations for several reasons (Lacy 1993b). Inbreeding, not strictly a component of genetic 
drift but correlated with it in small populations, has been documented to cause loss of fitness in a wide 
variety of species, including virtually all sexually reproducing animals in which the effects of inbreeding 
have been carefully studied (Wright 1977; Falconer 1981; O'Brien and Evermann 1988; Ralls et al. 1988; 
Lacy et al. 1993; Lacy 1997). Even if the immediate loss of fitness of inbred individuals is not large, the 


 
VORTEX Version 9.50 User’s Manual 
 
113 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
loss of genetic variation that results from genetic drift may reduce the ability of a population to adapt to 
future changes in the environment (Fisher 1958; Robertson 1960; Selander 1983). 
 
Thus, the effects of genetic drift and consequent loss of genetic variation in individuals and populations 
negatively impact on demographic rates and increase susceptibility to environmental perturbations and 
catastrophes. Reduced population growth and greater fluctuations in numbers in turn accelerates genetic 
drift (Crow and Kimura 1970). These synergistic destabilizing effects of stochastic process on small 
populations of wildlife have been described as “extinction vortices” (Gilpin and Soulé 1986).  
 
What is Population (and Habitat) Viability Analysis? 
 
Analyses which have used the VORTEX simulation for guiding conservation decisions refer variously to 
“Population Viability Analysis (PVA)”, “Population and Habitat Viability Analysis (PHVA),” 
“Population Vulnerability Analysis”, “Population Viability (or Vulnerability) Assessment”, and other 
variants on the name. This diversity of terminology has caused some confusion among practitioners of the 
PVA (or PHVA) approach, and probably even more confusion among wildlife managers who have tried 
to understand what analysis was being described, and whether it could be a useful tool in their efforts to 
conserve biodiversity. The diversity of perceptions about the PVA approach is not limited to its name. 
Different people mean different things by PVA, and the definitions and practice of PVA are constantly 
evolving. We don’t think it is not the case, as has sometimes been suggested, that some people are doing 
PVA correctly, and others incorrectly, but rather that people are using different (if related) kinds of 
analyses and labeling them with the same (or similar) terms. What analysis is correct depends on the need 
and the application. Below, we attempt to clarify what PVA is, by suggesting a more consistent 
terminology and by describing the features that characterize the application of the PVA approach to 
conservation. The perspective offered here is necessarily biased by personal experiences in conservation; 
we will not attempt an exhaustive historical account of this field. 
 
Population viability analysis originally described methods of quantitative analysis to determine the 
probability of extinction of a population. Shaffer (1981) first defined a minimum viable population 
(MVP) as the size at which a population has a 99% probability of persistence for 1000 years, but it might 
be more meaningful biologically to consider it to be the size below which a population's fate becomes 
determined largely by the stochastic factors that characterize extinction vortices. One concept of 
population viability analysis is any methodology used to determine an MVP (Shaffer 1990). More 
broadly, PVA is the estimation of extinction probabilities and other measures of population performance 
by analyses that incorporate identifiable threats to population survival into models of the extinction 
process (Brussard 1985; Gilpin and Soulé 1986; Burgman et al. 1993; Lacy 1993/1994).  
 
Shaffer's (1981) original term “minimum viable population” (MVP) has fallen into disfavor (Soulé 1987), 
even as the PVA approach has risen in popularity. Shaffer stressed that an MVP was an estimate of the 
population size below which the probability of extinction was unacceptably high, that different 
populations would have different MVPs, and that the MVP determined for a population would depend on 
the threatening factors that were considered. However, the term implied to some people that there was a 
well-defined number below which extinction was certain and above which persistence was assured. Re-
emphasizing the probabilistic nature of the extinction process, a number of conservation biologists have 
focused on methods for estimating the probability of extinction over defined time periods for a designated 
population exposed to a specific scenario of environmental conditions, threats to persistence, and future 
management actions and other foreseeable events (Brussard 1985; Starfield and Bleloch 1986; Soulé 
1987; Simberloff 1988; Gilpin 1989; Shaffer 1990; Boyce 1992; Burgman et al. 1993). Thus, “Population 
Viability Analysis” (or the synonymous “Population Viability Assessment” and “Population Vulnerability 
Analysis”) came to describe any of the array of methods for quantifying the probability of extinction of a 


VORTEX Version 9.50 User’s Manual 
114 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
population. Although PVA has been extended by some to encompass a broader approach to conservation 
(see below), the term “Population Viability Analysis”, or PVA, should perhaps be reserved for its 
original, yet still rather broad, meaning. 
 
Beginning in about 1989 (Lacy et al. 1989; Seal and Lacy 1989; Seal et al. 1990), it became increasingly 
recognized that PVA can often be most usefully incorporated into a strategy for the conservation of a 
taxon if it is part of, and often central to, a conservation workshop that mobilizes collaboration among the 
array of people with strong interest in or responsibility for a conservation effort (e.g., governmental 
wildlife agencies, conservation NGOs, and the local people who interact with the species or its habitat) or 
with particular expert knowledge about the species, its habitats, or the threats it faces (e.g., academic 
biologists, conservation professionals, other wildlife biologists, experts on human demographics and 
resource use). Conservation problems are almost always multi-faceted, involving not only complex 
dynamics of biological populations, but also interactions with human populations, the past, present, and 
future impacts of humans on habitats, and human political, social, and economic systems (Alvarez 1993; 
Bormann and Kellert 1991; Clark 1989, 1993). Many people need to contribute knowledge, expertise, and 
ideas in order to achieve the recovery of threatened species. Population viability analyses can provide a 
framework for incorporating the many needed kinds of knowledge into species conservation efforts, 
because PVAs do allow the assessment of many kinds of factors that threaten the persistence of 
populations (Lacy 1993a; Lindenmayer et al. 1993). 
 
The Conservation Breeding Specialist Group (CBSG) of the IUCN’s Species Survival Commission 
especially has advocated and used workshops centered on PVAs to provide guidance to conservation 
assessment and planning (see references to CBSG workshops in Appendix III). Over the past few years, 
the PVA workshop as an approach to species conservation has expanded considerably beyond the 
quantitative analysis of extinction probabilities as advanced by Shaffer (1981, 1990), Soulé (1987), Gilpin 
(1989), Clark et al. (1991), Boyce (1992), and others. PVA workshops have incorporated consideration of 
resource use and needs by local human populations (Seal et al. 1991; Bonaccorso et al. 1999), education 
programs for the local human populations (Odum et al. 1993), trade issues (Foose et al. 1993), and trends 
in human demographics and land use patterns (Walker and Molur 1994; Herrero and Seal 2000). 
Recognizing that the conservation assessment workshops increasingly incorporated more than just the 
population biology modeling (which still formed a core organizing and analysis framework for the 
workshop), the CBSG has termed their workshops Population and Habitat Viability Analyses (PHVA). 
We would recommend that the term Population and Habitat Viability Analysis (PHVA) be used to 
describe the collaborative workshop approach to species conservation that centers on, but encompasses 
more than, a Population Viability Analysis (in the narrow sense). The concept of a PHVA continues to 
expand and evolve, as it should considering the need for more holistic and flexible approaches to 
conservation (e.g., Ruggiero et al. 1994). Thus, in the usage I recommend, PVA is a quantitative analysis 
of the probability of population persistence under defined sets of assumptions and circumstances. PHVA 
is a workshop process that brings to bear the knowledge of many people on species conservation, eliciting 
and assessing multiple options for conservation action, principally by using the tool of PVA as a way 
evaluate present threats to population persistence and likely fates under various possible scenarios.  
 
Population Viability Analysis (PVA) 
 
Two defining characteristics of a PVA are an explicit model of the extinction process and the 
quantification of threats to extinction. These features set PVA apart from many other analyses of the 
threats facing species, including, for example, the IUCN Red Books of Threatened Species. As a 
methodology to estimate the probability of extinction of a taxon, PVA necessarily must start with an 
understanding, or model, of the extinction process (Clark et al. 1990).  
 


 
VORTEX Version 9.50 User’s Manual 
 
115 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Generally, the model of extinction underlying a PVA considers two categories of factors: deterministic 
and stochastic. Deterministic factors, those that can shift species from long-term average population 
growth to population decline include the well-known threats of over-harvest, habitat destruction, pollution 
or other degradation of environmental quality, and the introduction of exotic predators, competitors, and 
diseases. Singly or combined, these forces have driven many wildlife populations to low numbers and, for 
some, to extinction. Once a population becomes small, and isolated from conspecific populations that 
might serve as sources for immigrants that could stabilize demographics and genetics, its dynamics and 
fate can become dominated by a number of random or stochastic processes (as outlined above and by 
Shaffer 1981). Thus, even if the original deterministic causes of decline are stopped or reversed, the 
instability caused by the action of stochastic processes acting on small populations can cause the 
extinction of a population.  
 
In nature, most threatening processes have both deterministic and stochastic features. For example, a high 
level of poaching might be seen as a deterministic factor driving a wildlife population toward extinction, 
but whether an individual animal is killed might be largely a matter of chance. In a PVA, poaching might 
be modeled as a deterministic process by killing a determined proportion of the animals, or it might be 
modeled as a stochastic process by giving each animal that probability of being killed but allowing the 
exact numbers killed to vary over time. If the population is large and the percent of animals killed is high, 
then these two ways of modeling the effects of poaching will yield the same results: the deterministic 
component of poaching dominates the population dynamics. If the population is small or the percent of 
animals killed is very low, then the numbers killed in a stochastic model (and in nature) might vary 
substantially from year to year: the stochastic nature of poaching further destabilizes the population. 
 
Which of the various deterministic and stochastic factors are important to consider in a PVA will depend 
on the species biology, the present population size and distribution, and the threats it faces. For example, 
orang utans may be threatened by forest destruction and other largely deterministic processes, but 
inbreeding and randomly skewed sex ratios resulting from highly stochastic processes are unlikely to be 
problems, at least not on a species-wide basis. On the other hand, even if the remnant Atlantic coastal 
rainforest of Brazil is secured for the future, the populations of golden lion tamarins (Leontopithecus 
rosalia) which can persist in that remnant forest are not sufficiently large to be stable in the face of 
stochastic threats (Seal et al. 1990; Rylands 1993/4; Ballou et al. 1997). The identification of the primary 
threats facing a taxon via a comprehensive PVA is important for conservation planning. For example, 
tamarin populations might be stabilized by the translocations and reintroductions that are underway and 
planned, but an orang utan PHVA recognized that releases of confiscated “pet” orang utans are unlikely 
to have a conservation benefit for those populations which are facing habitat destruction, not stochastic 
fluctuations and inbreeding. For many species, such as the whooping crane (Grus americana), the 
temporarily extinct-in-the-wild black-footed ferret (Mustela nigripes), and the Puerto Rican parrot 
(Amazona vitatta), only a single population persisted in the wild. Although those populations may have 
been maintained or even increased for a number of years, the principal threat was that a local catastrophe 
(e.g., disease epidemic, severe storm) could decimate the population (Clark 1989; Lacy et al. 1989; 
Mirande et al. 1991). The primary recovery actions therefore needed to include the establishment of 
additional populations. Tragically, some taxa, such the eastern barred bandicoot (Perameles gunnii) in 
Australia, may be critically threatened simultaneously by deterministic factors and stochastic processes 
(Lacy and Clark 1990). 
 
PVA is formally an assessment of the probability of extinction, but PVA methods often focus on other 
indicators of population health. Mean and variance in population growth (Lindenmayer and Lacy 1995a, 
1995b, 1995c), changes in range, distribution, and habitat occupancy (Hanski and Gilpin 1991, 1997), and 
losses of genetic variability (Soulé et al. 1986; Lande and Barrowclough 1987; Seal 1992; Lacy and 
Lindenmayer 1995) can be analyzed and monitored. Although not yet common, monitoring of population 
health could also utilize measures of developmental stability (Clarke 1995), physiological parameters 


VORTEX Version 9.50 User’s Manual 
116 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
such as body condition (Altmann et al. 1993) or levels of the hormones related to stress and reproduction 
(Sapolsky 1982, 1986), or the stability of behavior and the social structure of the population (Samuels and 
Altmann 1991). 
 
The interactions and synergism among threatening processes will often cause numerical, distributional, 
physiologic, behavioral, and genetic responses to concordantly reflect species decline and vulnerability. It 
remains important, however, to understand and target the primary causal factors in species vulnerability. 
The recent proposal to base IUCN categories of threat on quantified criteria of probability of extinction, 
or changes in such indicators as species range, numbers, and trends (Mace and Lande 1991; Mace et al. 
1992; Mace and Stuart 1994; IUCN Species Survival Commission 1994) reflects the increased 
understanding of the extinction process that has accompanied the development of PVA, and 
simultaneously demands that much more progress be made in developing predictive models, gathering 
relevant data on status and threats, and applying the PVA techniques. 
 
Population and Habitat Viability Analysis (PHVA) 
 
Population and Habitat Viability Analysis is a multi-faceted process or framework for assisting 
conservation planning, rather than a singular technique or tool. It is often interwoven with other 
techniques for managing complex systems, such as decision analysis (Maguire 1986; Maguire et al. 
1990). Even when viewed as the PHVA workshop, all such conservation workshops involved and 
required substantial pre-workshop and post-workshop activities. Some PHVA workshops have been 
extended into multiple workshops and less formal, smaller collaborative meetings, often focused on 
subsets of the larger problems of species conservation. 
 
Although PHVAs are diverse and not well defined, the PHVA process contains a number of critical 
components. First, it is essential to gather an array of experts who have knowledge of the species or 
problem. A PHVA is not required to bring together experts, but it often facilitates such sharing of 
expertise because the collective knowledge of many is essential for a useful PVA (in the narrow sense) to 
be completed. In addition to a diversity of people, a PHVA workshop also requires and therefore 
facilitates the involvement of a number of agencies and other concerned organizations. For example, the 
PVA on the two endemic primates of the Tana River Primate Reserve in Kenya (Seal et al. 1991) was 
convened by the Kenya Wildlife Service, facilitated by the IUCN SSC Captive Breeding Specialist 
Group, benefited from the expertise contributed by members of the IUCN SSC Primate Specialist Group, 
and was sponsored by the World Bank. The involvement of many agencies and interested parties is 
critical to endangered species recovery.  
 
An early requirement, or prerequisite, of a PHVA workshop is to determine the conservation problem to 
be addressed, and to state the goals of the management plan. Many endangered species programs have not 
clearly identified their goals. For example, at a PHVA and Conservation Assessment and Management 
Plan workshop on the forest birds of the Hawaiian islands (Ellis et al. 1992a, 1992b), it became apparent 
that the agencies responsible for the conservation of Hawaii's bird fauna had not determined whether their 
goal was to prevent species extinctions, prevent taxa (species or subspecies) from becoming extirpated on 
any of the islands they presently inhabit, preserve species in sufficient numbers and distribution to allow 
them to continue to fill ecological roles in the biological communities, or the restoration of taxa to most or 
all parts of the original ranges. The management actions required to achieve these various levels of 
conservation are quite different. In contrast, a  PHVA on the Grizzly Bear in the Central Rockies of 
Canada (Herrero and Seal 2000) clearly identified that provincial policy called for maintenance of stable 
or growing populations of the species. Thus, the criterion against which alternative management scenarios 
were judged was whether the PVA projections indicated that the populations would not decline. 
 


 
VORTEX Version 9.50 User’s Manual 
 
117 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
PHVA workshops facilitate the assembly of all available data. Often, important information is found in 
the field notes of researchers or managers, in the heads of those who have worked with and thought about 
the problems of the species, and in unpublished agency reports, as well as in the published scientific 
literature. A pending PHVA can be the impetus that encourages the collection of data in anticipation of 
presentation, review, and analysis at the workshop. For example, a Sumatran Tiger PHVA helped 
stimulate the systematic collection of data on sightings and signs of tigers in protected areas throughout 
the island of Sumatra, and collation and integration with a Geographic Information System (GIS) map of 
habitats and human pressures on those habitats. The PHVA on the Grizzly Bear in the Central Canadian 
Rockies Ecosystem provided the opportunity for detailed habitat mapping data to be integrated with 
population biology data on the bears, resulting in the development of models which would allow 
projection of the impacts of habitat changes on the bear populations. 
 
It is important to specify the assumptions that underlay a PHVA, and any consequent management 
recommendation. For example, the Hawaiian bird conservation efforts are constrained by a belief that no 
birds bred outside of the islands should ever be brought back to the islands for release. While this position 
derives from a reasonable concern for disease transmission (much of the decline of Hawaii's native birds 
is thought to be due to introduced avian diseases) as much as from any political or philosophical stand, 
any justification for the restriction must be questioned in light of the fact that wildlife agencies import and 
release, without quarantine, 1000s of exotic game birds onto the islands annually. 
 
Once experts are assembled, problems stated and goals set, data gathered, and assumptions specified, then 
the PHVA process can proceed with what I describe as PVA in the narrow sense: estimation of the 
probability of population persistence. The available data are used to estimate the parameters that are 
needed for the model of population dynamics to be applied. Often, data are not available from which to 
estimate certain key parameters. In those cases, subjective and objective, but non-quantified, information 
might be solicited from the assembled experts, values might be obtained from data on related species, or a 
factor might simply be omitted from the model. While such a non-precise process might consist simply of 
intuitive judgments made by experts, it is important to specify how values for the parameters in the model 
were obtained. The resulting limitations of the analyses should be acknowledged, and a decision made if, 
how, by whom, and when the missing data would be collected so that more refined analyses could be 
conducted. With the PVA model, projections of the most likely fate, and distribution of possible fates, of 
the population under the specified assumptions are made.  
 
Because so much of a PVA – the data, the model, and even the interpretation of output – is uncertain, a 
PVA that provides an estimate of the probability of extinction under a single scenario is of very limited 
usefulness. An essential component of the PHVA process, therefore, is sensitivity testing. Ranges of 
plausible values for uncertain parameters should be tested, to determine what effects those uncertainties 
might have on the results. In addition, several different PVA models might be examined at a PHVA 
workshop, or the same general model tested under different structural assumptions. Different participants 
in the process should assess and interpret the results. Such sensitivity testing reveals which components of 
the data, model, and interpretation have the largest impact on the population projections. This will 
indicate which aspects of the biology of the population and its situation contribute most to its 
vulnerability and, therefore, which aspects might be most effectively targeted for management. In 
addition, uncertain parameters that have a strong impact on results are those which might be the focus of 
future research efforts, to better specify the dynamics of the population. Close monitoring of such 
parameters might also be important for testing the assumptions behind the selected management options 
and for assessing the success of conservation efforts.  
 
Closely parallel to the testing of uncertainties in the present situation is the testing of options for 
management. PVA modeling allows one to test the expected results of any given management action, 
under the assumptions of the model and within the limitations of present knowledge, on the computer 


VORTEX Version 9.50 User’s Manual 
118 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
before implementation in the field. This process can guide selection of the management options most 
likely, given current knowledge, to be effective, and will define target recovery goals that should be 
obtained if our knowledge is adequate and the recommended actions are followed. A PHVA workshop on 
the Black Rhinoceros in Kenya's 11 rhino sanctuaries (Foose et al. 1993) suggested that periodic 
movement of rhinos between fenced sanctuaries to reduce inbreeding and demographic fluctuations 
would be necessary to stabilize the populations in the smaller parks. Moreover, the modeling provided 
estimates of the rate at which the larger populations would be able to provide surplus animals for 
translocation.  
 
It would be an error to assume that any PVA model incorporates everything of interest. A PVA 
simulation program can only include those processes that are known to the programmer. This will likely 
be a subset of what might be known to the field biologists, which in turn will definitely be a subset of 
those processes that impact natural populations. A number of variables affecting population dynamics and 
viability are not yet commonly examined in PVA models. These include: social and ecological 
determinants of dispersal; complex social processes, such as the role of non-breeders in group stability 
and the impacts of other aspects of the social environment on reproductive success and survival; 
competitive, exploitative, or mutualistic interactions with other species experiencing their own population 
dynamics; and the effects of changes in the global environment. To date, most PVA models treat 
organisms as independent actors in spatially homogeneous physical, biotic, and social environments. 
There is tremendous opportunity and need for elaboration of PVA models, and it is likely that 
increasingly sophisticated models will also become more specific to the individual taxa and environments 
under study. 
 
PHVA workshops must incorporate consideration of the assumptions of the PVA model used and the 
biases or limitations in interpretation that could result. PHVAs consider only those threatening processes 
of which we have knowledge, for which we can develop algorithms for modeling or other methods for 
analysis, and for which we have some data. As a result, it is likely that PVAs will underestimate the 
vulnerability of most populations to extinction, and that PHVA workshops will be less comprehensive 
than is desirable. We need always to be cognizant of the limits of our understanding of wildlife 
populations, and to include appropriate margins for error in our conservation strategies. 
 
PVA is, by definition, an assessment of the probability of persistence of a population over a defined time 
frame. Yet, persistence of a population, while a necessary condition for effective conservation of natural 
systems, is often not sufficient. Prevention of extinction is the last stand of conservationists, but the goals 
should be higher: conservation of functional biological communities and ecosystems. PVA usually 
ignores the functional role of a species in a community, but a PHVA workshop should consider much 
more than the prevention of the final biological extinction of the taxon. A species, such as the American 
Bison (Bison bison), can be functionally extinct in terms of no longer filling its original role in nature, 
even as it is praised as a conservation success story and would be considered safe from extinction and 
viable. 
 
The use of the PHVA process to help guide conservation decisions is not a singular event, in which an 
analysis can be completed, management actions recommended and implemented, and conservation 
thereby assured. The many uncertainties in the process mandate that PVA be used as a tool in an adaptive 
management framework, and a PHVA workshop is just one stage of an effective conservation strategy. In 
adaptive management, the lack of knowledge adequate to predict with certainty the best course of action 
is recognized, management actions are designed in such a way that monitoring will allow testing of the 
adequacy of our model and understanding, and corrective adjustments to management plans are made 
whenever the accumulating data suggest that the present course is inadequate to achieve the goals and that 
a better strategy exists (Holling 1978). The urgency of the biodiversity crisis will not permit us ethically 
to refrain from aggressive conservation action until we have scientifically sound understanding of all the 


 
VORTEX Version 9.50 User’s Manual 
 
119 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
factors that drive population, community, and ecosystem dynamics. PHVA provides a forum for making 
use of the information we do have, in a well-documented process that is open to challenge and 
improvement. PHVA workshops can, therefore, assist wildlife managers in the very difficult and 
important job of using science to safeguard the future of wildlife populations. 
 
In summary, Population Viability Analysis (PVA) and Population and Habitat Viability Analysis (PHVA) 
refer to an array of interrelated and evolving techniques for assessing the survival probability of a 
population and possible conservation actions. It might be useful to restrict the term PVA to its original 
meaning -- the use of quantitative techniques to estimate the probability of population persistence under a 
chosen model of population dynamics, a specified set of biological and environmental parameters, and 
enumerated assumptions about human activities and impacts on the system. PHVA refers to a workshop 
approach to conservation planning, which elicits and encourages contributions from an array of experts 
and stakeholders, uses PVA and other quantitative and non-quantitative techniques to assess possible 
conservation actions, and strives to achieve consensus on the best course of action from competing 
interests and perspectives, incomplete knowledge, and an uncertain future. 
 
Many of the components of PVAs and PHVAs, even when used in isolation, can be effective educational 
and research tools. To be a useful framework for advancing the conservation of biodiversity, however, 
PHVA must incorporate all of: (1) collection of data on the biology of the taxon, status of its habitat, and 
threats to its persistence, (2) quantitative analysis of available data, (3) input of population status and 
identifiable threats to persistence into analytical or simulation models of the extinction process, (4) 
assessment of the probability of survival over specified periods of time, given the assumptions and 
limitations of the data and model used, (5) sensitivity testing of estimates of extinction probability across 
the range of plausible values of uncertain parameters, (6) specification of conservation goals for the 
population, (7) identification of options for management, (8) projection of the probability of population 
survival under alternative scenarios for future conservation action, (9) implementation of optimal actions 
for assuring accomplishment of conservation goals, (10) continued monitoring of the population, (11) 
reassessment of assumptions, data, models, and options, and (12) adjustment of conservation strategies to 
respond to the best information available at all times. There are many uncertain aspects of population 
dynamics, especially of endangered taxa, including few data on species biology and habitats, uncertain 
political and social climate for implementing conservation actions, and the unpredictability inherent in 
small populations due to the many stochastic forces that drive population dynamics. 
 
The rapid development of PVA as a research and management tool, and the concurrent but not always 
parallel expansion of the scope of what conservation threats, options, and actions are considered in PHVA 
workshops, has led to confusion. Different people can describe rather distinct kinds of analyses with the 
same terminology, while others use different terms to describe nearly identical approaches. The ever-
changing concepts of PVA and PHVA are confusing, but the flexibility of the processes is also their 
strength. Current tools are inadequate to address fully the challenges of stemming the losses of 
biodiversity. The PVA/PHVA framework allows and encourages rapid application of new tools, data, and 
interpretations into increasingly effective conservation programs. 
 
Methods for Analyzing Population Viability 
 
An understanding of the multiple, interacting forces that contribute to extinction vortices is a prerequisite 
for the study of extinction-recolonization dynamics in natural populations inhabiting patchy environments 
(Gilpin 1987), the management of small populations (Clark and Seebeck 1990), and the conservation of 
threatened wildlife (Shaffer 1981, 1990; Soulé 1987; Mace and Lande 1991).  
 


VORTEX Version 9.50 User’s Manual 
120 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Shaffer (1981) suggested several ways to conduct PVAs. Perhaps the most rigorous method, and the one 
that would produce the most defensible estimates, would be an empirical observation of the stability and 
long term fates of a number of populations of various sizes. Berger (1990) presented a good example of 
this approach, in which he observed that populations of bighorn sheep in the mountains of the western 
USA persisted only when the populations consisted of more than 100 animals. A few other studies of 
wildlife populations have provided empirical data on the relationship between population size and 
probability of extinction (e.g., Belovsky 1987; Thomas 1990), but presently only order of magnitude 
estimates can be provided for MVPs of vertebrates (Shaffer 1987). More empirical studies are needed, but 
the time and numbers of populations required for such studies are precluded in the cases of most species 
threatened with extinction -- exactly those for which estimates of population vulnerability are most 
urgently needed.  
 
A more elegant and general approach to PVA is to develop analytical models of the extinction process 
that will allow calculation of the probability of extinction from a small number of measurable parameters. 
Goodman's (1987) model of demographic fluctuations, and applications to conservation of the classic 
population genetic models of loss of genetic diversity by genetic drift (Franklin 1980; Soulé et al. 1986; 
Lande and Barrowclough 1987) are valuable efforts in this direction. Unfortunately, our understanding of 
population biology is not yet sufficient to provide fully adequate analytical models of the extinction 
process. For example, none of the existing analytical models incorporate all three of demographic, 
environmental, and genetic fluctuations, and thus they do not begin to model the array of extinction 
vortices described by Gilpin and Soulé (1986). Moreover, the analytical models make extremely 
simplifying assumptions about a number of the intricacies of population structure. For example, social 
groupings or preferences are often assumed to be invariant or lacking, resulting in random mating; and 
dispersal is usually assumed to be random between all sites (the "island model") or only to occur between 
adjacent sites (the "stepping stone model"). Much more work is needed either to develop more complex 
and flexible models or to demonstrate that the simple models are sufficient to provide guidance for 
conservation. 
 
A third method of conducting a PVA is the use of computer simulation modeling to project the 
probability distribution of possible fates of a population. Simulation models can incorporate a very large 
number of threatening processes and their interactions, if the processes can be described in terms of 
quantitative algorithms and parameterized. Although many processes affecting small populations are 
intrinsically indeterminate, the average long-term fate of a population and the variance around the 
expectation can be studied with computer simulation models. The focus is on detailed and explicit 
modeling of the forces impinging on a given population, place, and time of interest, rather than on 
delineation of rules (which may not exist) that apply generally to most wildlife populations.  
 
Modeling and Population Viability Analysis 
 
A model is any simplified representation of a real system. We use models in all aspects of our lives, in 
order to: (1) extract the important trends from complex processes, (2) permit comparison among systems, 
(3) facilitate analysis of causes of processes acting on the system, and (4) make predictions about the 
future. A complete description of a natural system, if it were possible, would often decrease our 
understanding relative to that provided by a good model, because there is "noise" in the system that is 
extraneous to the processes we wish to understand. For example, the typical representation of the growth 
of a wildlife population by an annual percent growth rate is a simplified mathematical model of the much 
more complex changes in population size. Representing population growth as an annual percent change 
assumes constant exponential growth, ignoring the irregular fluctuations as individuals are born or 
immigrate, and die or emigrate. For many purposes, such a simplified model of population growth is very 
useful, because it captures the essential information we might need regarding the average change in 


 
VORTEX Version 9.50 User’s Manual 
 
121 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
population size, and it allows us to make predictions about the future size of the population. A detailed 
description of the exact changes in numbers of individuals, while a true description of the population, 
would often be of much less value because the essential pattern would be obscured, and it would be 
difficult or impossible to make predictions about the future population size. 
 
In considerations of the vulnerability of a population to extinction, as is so often required for conservation 
planning and management, the simple model of population growth as a constant annual rate of change is 
inadequate for our needs. The fluctuations in population size that are omitted from the standard ecological 
models of population change can cause population extinction, and therefore are often the primary focus of 
concern. In order to understand and predict the vulnerability of a wildlife population to extinction, we 
need to use a model which incorporates the processes which cause fluctuations in the population, as well 
as those which control the long-term trends in population size. Many processes can cause fluctuations in 
population size: variation in the environment (such as weather, food supplies, and predation), genetic 
changes in the population (such as genetic drift, inbreeding, and response to natural selection), 
catastrophic effects (such as disease epidemics, floods, and droughts), decimation of the population or its 
habitats by humans, the chance results of the probabilistic events in the lives of individuals (sex 
determination, location of mates, breeding success, survival), and interactions among these factors (Gilpin 
and Soulé 1986). 
 
Models of population dynamics which incorporate causes of fluctuations in population size in order to 
predict probabilities of extinction, and to help identify the processes which contribute to a population's 
vulnerability, are used in Population Viability Analysis (PVA). For the purpose of predicting vulnerability 
to extinction, any and all population processes that impact population dynamics can be important. Much 
analysis of conservation issues is conducted by largely intuitive assessments by biologists with experience 
with the system. Assessments by experts can be quite valuable, and are often contrasted with "models" 
used to evaluate population vulnerability to extinction. Such a contrast is not valid, however, as any 
synthesis of facts and understanding of processes constitutes a model, even if it is a mental model within 
the mind of the expert and perhaps only vaguely specified to others (or even to the expert himself or 
herself).  
 
A number of properties of the problem of assessing vulnerability of a population to extinction make it 
difficult to rely on mental or intuitive models. Numerous processes impact population dynamics, and 
many of the factors interact in complex ways. For example, increased fragmentation of habitat can make 
it more difficult to locate mates, can lead to greater mortality as individuals disperse greater distances 
across unsuitable habitat, and can lead to increased inbreeding which in turn can further reduce ability to 
attract mates and to survive. In addition, many of the processes impacting population dynamics are 
intrinsically probabilistic, with a random component. Sex determination, disease, predation, mate 
acquisition -- indeed, almost all events in the life of an individual -- are stochastic events, occurring with 
certain probabilities rather than with absolute certainty at any given time. The consequences of factors 
influencing population dynamics are often delayed for years or even generations. With a long-lived 
species, a population might persist for 20 to 40 years beyond the emergence of factors that ultimately 
cause extinction. Humans can synthesize mentally only a few factors at a time, most people have 
difficulty assessing probabilities intuitively, and it is difficult to consider delayed effects. Moreover, the 
data needed for models of population dynamics are often very uncertain. Optimal decision-making when 
data are uncertain is difficult, as it involves correct assessment of probabilities that the true values fall 
within certain ranges, adding yet another probabilistic or chance component to the evaluation of the 
situation. 
 
The difficulty of incorporating multiple, interacting, probabilistic processes into a model that can utilize 
uncertain data has prevented (to date) development of analytical models (mathematical equations 
developed from theory) which encompass more than a small subset of the processes known to affect 


VORTEX Version 9.50 User’s Manual 
122 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
wildlife population dynamics. It is possible that the mental models of some biologists are sufficiently 
complex to predict accurately population vulnerabilities to extinction under a range of conditions, but it is 
not possible to assess objectively the precision of such intuitive assessments, and it is difficult to transfer 
that knowledge to others who need also to evaluate the situation. Computer simulation models have 
increasingly been used to assist in PVA. Although rarely as elegant as models framed in analytical 
equations, computer simulation models can be well suited for the complex task of evaluating risks of 
extinction. Simulation models can include as many factors that influence population dynamics as the 
modeler and the user of the model want to assess. Interactions between processes can be modeled, if the 
nature of those interactions can be specified. Probabilistic events can be easily simulated by computer 
programs, providing output that gives both the mean expected result and the range or distribution of 
possible outcomes. In theory, simulation programs can be used to build models of population dynamics 
that include all the knowledge of the system which is available to experts. In practice, the models will be 
simpler, because some factors are judged unlikely to be important, and because the persons who 
developed the model did not have access to the full array of expert knowledge. 
 
Although computer simulation models can be complex and confusing, they are precisely defined and all 
the assumptions and algorithms can be examined. Therefore, the models are objective, testable, and open 
to challenge and improvement. PVA models allow use of all available data on the biology of the taxon, 
facilitate testing of the effects of unknown or uncertain data, and expedite the comparison of the likely 
results of various possible management options. 
 
PVA models also have weaknesses and limitations. A model of the population dynamics does not define 
the goals for conservation planning. Goals, in terms of population growth, probability of persistence, 
number of extant populations, genetic diversity, or other measures of population performance must be 
defined by the management authorities before the results of population modeling can be used. Because the 
models incorporate many factors, the number of possibilities to test can seem endless, and it can be 
difficult to determine which of the factors that were analyzed are most important to the population 
dynamics. PVA models are necessarily incomplete. We can model only those factors which we 
understand and for which we can specify the parameters. Therefore, it is important to realize that the 
models probably underestimate the threats facing the population. Finally, the models are used to predict 
the long-term effects of the processes presently acting on the population. Many aspects of the situation 
could change radically within the time span that is modeled. Therefore, it is important to reassess the data 
and model results periodically, with changes made to the conservation programs as needed. 
 
Dealing with uncertainty 
 
It is important to recognize that uncertainty regarding the biological parameters of a population and its 
consequent fate occurs at several levels and for independent reasons. Uncertainty can occur because the 
parameters have never been measured on the population. Uncertainty can occur because limited field data 
have yielded estimates with potentially large sampling error. Uncertainty can occur because independent 
studies have generated discordant estimates. Uncertainty can occur because environmental conditions or 
population status have been changing over time, and field surveys were conducted during periods which 
may not be representative of long-term averages. Uncertainty can occur because the environment will 
change in the future, so that measurements made in the past may not accurately predict future conditions.  
 
Sensitivity testing is necessary to determine the extent to which uncertainty in input parameters results in 
uncertainty regarding the future fate of the population. If alternative plausible parameter values result in 
divergent predictions for the population, then it is important to try to resolve the uncertainty with better 
data. Sensitivity of population dynamics to certain parameters also indicates that those parameters 
describe factors that could be critical determinants of population viability. Such factors are therefore good 
candidates for efficient management actions designed to ensure the persistence of the population. 


 
VORTEX Version 9.50 User’s Manual 
 
123 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
The above kinds of uncertainty should be distinguished from several more sources of uncertainty about 
the future of the population. Even if long-term average demographic rates are known with precision, 
variation over time caused by fluctuating environmental conditions will cause uncertainty in the fate of 
the population at any given time in the future. Such environmental variation should be incorporated into 
the model used to assess population dynamics, and will generate a range of possible outcomes (perhaps 
represented as a mean and standard deviation) from the model. In addition, most biological processes are 
inherently stochastic, having a random component. The stochastic or probabilistic nature of survival, sex 
determination, transmission of genes, acquisition of mates, reproduction, and other processes preclude 
exact determination of the future state of a population. Such demographic stochasticity should also be 
incorporated into a population model, because such variability both increases our uncertainty about the 
future and can also change the expected or mean outcome relative to that which would result if there were 
no such variation. Finally, there is “uncertainty” which represents the alternative actions or interventions 
that might be pursued as a management strategy. The likely effectiveness of such management options 
can be explored by testing alternative scenarios in the model of population dynamics, in much the same 
way that sensitivity testing is used to explore the effects of uncertain biological parameters. 
 
Often, the uncertainty regarding a number of aspects of the population biology, current status, and threats 
to persistence is too large to allow scientifically accurate and reliable projections of population dynamics. 
Therefore, the predictions made from PVA models should be considered to be projections about what 
would most likely happen to the population if various hypotheses about the status of the populations and 
the threats are true. Conservation and management decisions must be made based on the most plausible 
hypotheses about the population status, before sufficient data could be collected to test those hypotheses 
scientifically. An important advantage of PVA models is that they forced systematic consideration and 
specification of the assumptions and hypotheses that must be made in the absence of adequate data. This 
facilitates careful reassessment and improvement in the analyses, as better data become available.  
 
Questions that can be explored with PVA models 
 
Below are some of the conservation and management questions that can be explored by Population 
Viability Analysis modeling. References describing uses of VORTEX give many examples of these and 
other applications of PVA techniques to guide conservation. 
 
Using the best current information on the biology of the taxon and its habitat, are the populations 
projected to persist if conditions remain as they are now? Beyond just the persistence of the population, 
what is the most likely average population size, range of population sizes across years, and rate of loss of 
genetic variation? If the population is at risk of extinction, is the extinction expected to result primarily 
from negative average population growth (mean deaths exceeding mean births), from large fluctuations in 
numbers, from effects of accumulated inbreeding, or from a combination of these factors? 
 
Given that there is considerable uncertainty about several aspects of the species biology and its habitat, is 
the population likely to persist across the plausible ranges of parameters that might characterize the 
population? In particular, how sensitive are the population dynamics to varying estimates of reproductive 
success, juvenile survival, adult survival, effects of natural catastrophes, initial population size, carrying 
capacity of the habitat, and dispersal among populations? Are there critical values for any of these 
parameters which demarcate a transition from a population that would be considered viable to one that is 
not?  
 
Which factors have the greatest influence on the projected population performance? If important factors 
are identified, management actions might be designed to improve these factors or ameliorate the negative 
effects. How much change would be required in aspects of the population in order to ensure population 
survival?  


VORTEX Version 9.50 User’s Manual 
124 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
What would be the effect of removing some individuals from the population? Would there be a significant 
benefit from supplementing the population with individuals translocated from other populations or 
released from captive breeding stocks? Can the population sustain controlled harvest? Can it sustain 
poaching? 
 
Would a corridor connecting fragmented habitats improve long-term viability? Could the same effect be 
achieved by translocating a few individuals? What will happen to population viability if mortality 
increases for individuals dispersing between habitat patches? 
 
What will happen to the wildlife population if trends in human populations and human impacts on the 
environment continue unabated? 
 
The VORTEX Population Viability Analysis Model 
 
The VORTEX computer program is a simulation of the effects of deterministic forces as well as 
demographic, environmental and genetic stochastic events on wildlife populations. It is an attempt to 
model many of the extinction vortices that can threaten persistence of small populations (hence, its name). 
VORTEX models population dynamics as discrete, sequential events that occur according to probabilities 
that are random variables following user-specified distributions. VORTEX simulates a population by 
stepping through a series of events that describe an annual cycle of a typical sexually reproducing, diploid 
organism: mate selection, reproduction, mortality, increment of age by one year, migration among 
populations, removals, supplementation, and then truncation (if necessary) to the carrying capacity. 
Although VORTEX simulates life events on an annual cycle, a user could model "years" that are other than 
12 months duration. The simulation of the population is iterated many times to generate the distribution of 
fates that the population might experience.  
 
VORTEX is an individual-based model. That is, it creates a representation of each animal in its memory and 
follows the fate of the animal through each year of its lifetime. VORTEX keeps track of the sex, age, and 
parentage of each animal. Demographic events (birth, sex determination, mating, dispersal, and death) are 
modeled by determining for each animal in each year of the simulation whether any of the events occur. 
(See figure below.)  
 
 
VORTEX requires a lot of population-specific data. For example, the user must specify the amount of 
annual variation in each demographic rate caused by fluctuations in the environment. In addition, the 
frequency of each type of catastrophe (drought, flood, epidemic disease) and the effects of the 
Breed 
Age 1 Year
Death 
Census 
Immigrate
Supplement
N 
Emigrate
Harvest
Carrying 
Capacity 
Truncation 
VORTEX Simulation Model Timeline
Events listed above the timeline increase N, while 
events listed below the timeline decrease N.


 
VORTEX Version 9.50 User’s Manual 
 
125 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
catastrophes on survival and reproduction must be specified. Rates of migration (dispersal) between each 
pair of local populations must be specified. Because VORTEX requires specification of many biological 
parameters, it is not necessarily a good model for the examination of population dynamics that would 
result from some generalized life history. It is most usefully applied to the analysis of a specific 
population in a specific environment. 
 
In the program explanation that follows, demographic rates are described as constants specified by the 
user. Although this is the way the program is most commonly and easily used, VORTEX does provide the 
capability to specify most demographic rates as functions of time, density, and other parameters (see 
Chapter 5). 
 
Demographic stochasticity 
 
VORTEX models demographic stochasticity by determining the occurrence of probabilistic events such as 
reproduction, litter size, sex determination, and death with a pseudo-random number generator. For each 
life event, if the random value sampled from a specified distribution falls above the user-specified 
probability, the event is deemed to have occurred, thereby simulating a binomial process. Demographic 
stochasticity is therefore a consequence of the uncertainty regarding whether each demographic event 
occurs for any given animal. 
 
The source code used to generate random numbers uniformly distributed between 0 and 1 was obtained 
from Maier (1991), based on the algorithm of Kirkpatrick and Stoll (1981). Random deviates from 
binomial distributions, with mean p and standard deviation s, are obtained by first determining the 
integral number of binomial trials, N, that would produce the value of s closest to the specified value, 
according to: 
N binomial trials are then simulated by sampling from the uniform 0-1 distribution to obtain the desired 
result, the frequency or proportion of successes. If the value of N determined for a desired binomial 
distribution is larger than 25, a normal approximation is used in place of the binomial distribution. This 
normal approximation must be truncated at 0 and at 1 to allow use in defining probabilities, although, 
with such large values of N, s is small relative to p and the truncation would be invoked only rarely. To 
avoid introducing bias with this truncation, the normal approximation to the binomial (when used) is 
truncated symmetrically around the mean. The algorithm for generating random numbers from a unit 
normal distribution follows Latour (1986). 
 
Environmental variation 
 
VORTEX can model annual fluctuations in birth and death rates and in carrying capacity as might result 
from environmental variation. To model environmental variation, each demographic parameter is 
assigned a distribution with a mean and standard deviation that is specified by the user. Annual 
fluctuations in probabilities of reproduction and mortality are modeled as binomial distributions. 
Environmental variation in carrying capacity is modeled as a normal distribution. Environmental variation 
in demographic rates can be correlated among populations.   
 
Catastrophes 
 
Catastrophes are modeled in VORTEX as random events that occur with specified probabilities. A 
catastrophe will occur if a randomly generated number between zero and one is less than the probability 
2
)
1
(
s
p
p
N
−
=


VORTEX Version 9.50 User’s Manual 
126 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
of occurrence. Following a catastrophic event, the chances of survival and successful breeding for that 
simulated year are multiplied by severity factors. For example, forest fires might occur once in 50 years, 
on average, killing 25% of animals, and reducing breeding by survivors 50% for the year. Such a 
catastrophe would be modeled as a random event with 0.02 probability of occurrence each year, and 
severity factors of 0.75 for survival and 0.50 for reproduction. Catastrophes can be local (impacting 
populations independently), or regional (affecting sets of populations simultaneously).  
 
Genetic processes 
 
VORTEX models loss of genetic variation in populations, by simulating the transmission of alleles from 
parents to offspring at a hypothetical neutral (non-selected) genetic locus. Each animal at the start of the 
simulation is assigned two unique alleles at the locus. Each offspring created during the simulation is 
randomly assigned one of the alleles from each parent. VORTEX monitors how many of the original alleles 
remain within the population, and the average heterozygosity and gene diversity (or “expected 
heterozygosity”) relative to the starting levels. VORTEX also monitors the inbreeding coefficients of each 
animal, and can reduce the juvenile survival of inbred animals to model the effects of inbreeding 
depression. 
 
Inbreeding depression is modeled as a loss of viability of inbred animals during their first year. The 
severity of inbreeding depression is commonly measured by the number of “lethal equivalents” in a 
population (Morton et al. 1956). The number of lethal equivalents per diploid genome estimates the 
average number of lethal alleles per individual in the population if all deleterious effects of inbreeding 
were due entirely to recessive lethal alleles. A population in which inbreeding depression is one lethal 
equivalent per diploid genome may have one recessive lethal allele per individual, it may have two 
recessive alleles per individual, each of which confer a 50% decrease in survival, or it may have some 
other combination of recessive deleterious alleles which equate in effect with one lethal allele per 
individual.  
 
VORTEX partitions the total effect of inbreeding (the total lethal equivalents) into an effect due to recessive 
lethal alleles and an effect due to loci at which there is heterozygote advantage (superior fitness of 
heterozygotes relative to all homozygote genotypes). To model the effects of lethal alleles, each founder 
starts with a unique recessive lethal allele (and a dominant non-lethal allele) at up to five modeled loci. 
By virtue of the deaths of individuals that are homozygous for lethal alleles, such alleles can be removed 
slowly by natural selection during the generations of a simulation. This diminishes the probability that 
inbred individuals in subsequent generations will be homozygous for a lethal allele.  
 
Heterozygote advantage is modeled by specifying that juvenile survival is related to inbreeding according 
to the logarithmic model: 
in which S is survival, F is the inbreeding coefficient, A is the logarithm of survival in the absence of 
inbreeding, and B is the portion of the lethal equivalents per haploid genome that is due to heterozygote 
advantage rather than to recessive lethal alleles. Unlike the situation with fully recessive deleterious 
alleles, natural selection does not remove deleterious alleles at loci in which the heterozygote has higher 
fitness than both homozygotes, because all alleles are deleterious when homozygous and beneficial when 
present in heterozygous combination with other alleles. Thus, under heterozygote advantage, the impact 
of inbreeding on survival does not diminish during repeated generations of inbreeding. 
Unfortunately, for relatively few species are data available to allow estimation of the effects of 
inbreeding, and the magnitude of these effects apparently varies considerably among species (Falconer 
1981; Ralls et al. 1988; Lacy et al. 1993) and even among populations of the same species (Lacy et al. 
1996). Even without detailed pedigree data from which to estimate the number of lethal equivalents in a 
BF
A
S
−
=
)
ln(


 
VORTEX Version 9.50 User’s Manual 
 
127 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
population and the underlying nature of the genetic load (recessive alleles or heterozygote advantage), 
PVAs must make assumptions about the effects of inbreeding on the population being studied. If genetic 
effects are ignored, the PVA will overestimate the viability of small populations. In some cases, it might 
be considered appropriate to assume that an inadequately studied species would respond to inbreeding in 
accord with the median (3.14 lethal equivalents per diploid) reported in the survey by Ralls et al. (1988). 
In other cases, there might be reason to make more optimistic assumptions (perhaps the lower quartile, 
0.90 lethal equivalents), or more pessimistic assumptions (perhaps the upper quartile, 5.62 lethal 
equivalents). In the few species in which inbreeding depression has been studied carefully, about half of 
the effects of inbreeding are due recessive lethal alleles and about half of the effects are due to 
heterozygote advantage or other genetic mechanisms that are not diminished by natural selection during 
generations of inbreeding, although the proportion of the total inbreeding effect can vary substantially 
among populations (Lacy and Ballou 1998). 
 
A full explanation of the genetic mechanisms of inbreeding depression is beyond the scope of this 
manual, and interested readers are encouraged to refer to the references cited above. 
 
VORTEX can model monogamous or polygamous mating systems. In a monogamous system, a relative 
scarcity of breeding males may limit reproduction by females. In polygamous or monogamous models, 
the user can specify the proportion of the adult males in the breeding pool. Males are randomly reassigned 
to the breeding pool each year of the simulation, and all males in the breeding pool have an equal chance 
of siring offspring. 
 
Deterministic processes 
 
VORTEX can incorporate several deterministic processes, in addition to mean age-specific birth and death 
rates. Density dependence in mortality is modeled by specifying a carrying capacity of the habitat. When 
the population size exceeds the carrying capacity, additional morality is imposed across all age classes to 
bring the population back down to the carrying capacity. Each animal in the population has an equal 
probability of being removed by this truncation. The carrying capacity can be specified to change over 
time, to model losses or gains in the amount or quality of habitat.  
 
Density dependence in reproduction is modeled by specifying the proportion of adult females breeding 
each year as a function of the population size. The default functional relationship between breeding and 
density allows entry of Allee effects (reduction in breeding at low density) and/or reduced breeding at 
high densities.  
 
Populations can be supplemented or harvested for any number of years in each simulation. Harvest may 
be culling or removal of animals for translocation to another (unmodeled) population. The numbers of 
additions and removals are specified according to the age and sex of animals.  
 
Migration among populations 
 
VORTEX can model up to 50 populations, with possibly distinct population parameters. Each pairwise 
migration rate is specified as the probability of an individual moving from one population to another. 
Migration among populations can be restricted to one sex and/or a limited age cohort. Emigration from a 
population can be restricted to occur only when the number of animals in the population exceeds a 
specified proportion of the carrying capacity. Dispersal mortality can be specified as a probability of 
death for any migrating animal, which is in addition to age-sex specific mortality. Because of between-
population migration and managed supplementation, populations can be recolonized. VORTEX tracks the 
dynamics of local extinctions and recolonizations through the simulation. 
 


VORTEX Version 9.50 User’s Manual 
128 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Output 
 
VORTEX outputs: (1) probability of extinction at specified intervals (e.g., every 10 years during a 100 year 
simulation), (2) median time to extinction, if the population went extinct in at least 50% of the 
simulations, (3) mean time to extinction of those simulated populations that became extinct, and (4) mean 
size of, and genetic variation within, extant populations.  
 
Standard deviations across simulations and standard errors of the mean are reported for population size 
and the measures of genetic variation. Under the assumption that extinction of independently replicated 
populations is a binomial process, the standard error of the probability of extinction is reported by 
VORTEX as: 
in which the frequency of extinction was p over n simulated populations. Demographic and genetic 
statistics are calculated and reported for each subpopulation and for the metapopulation.  
 
Sequence of program flow 
 
(1) The seed for the random number generator is initialized with the number of seconds elapsed since 
the beginning of the 20th century.  
 
(2)  The user is prompted for an output file name, duration of the simulation, number of iterations, the 
size below which a population is considered extinct, and a large number of population parameters. 
 
(3)  The maximum allowable population size (necessary for preventing memory overflow) is calculated 
as: 
in which K is the maximum carrying capacity (carrying capacity can be specified to change during a 
simulation, so the maximum carrying capacity can be greater than the initial carrying capacity), s is 
the annual environmental variation in the carrying capacity expressed as a standard deviation, and L 
is the specified maximum litter size. 
 
(4)  Memory is allocated for data arrays. If insufficient memory is available for data arrays then Nmax is 
adjusted downward to the size that can be accommodated within the available memory and a 
warning message is given. In this case it is possible that the analysis may have to be terminated 
because the simulated population exceeds Nmax. Because Nmax is often several-fold greater than the 
likely maximum population size in a simulation, a warning that it has been adjusted downward 
because of limiting memory often will not hamper the analyses. 
 
(5)  The deterministic growth rate of the population is calculated from mean birth and death rates that 
have been entered. Algorithms follow cohort life-table analyses (Ricklefs 1979). Generation time 
and the expected stable age distribution are also calculated. Life-table calculations assume constant 
birth and death rates, no limitation by carrying capacity, no limitation of mates, no loss of fitness due 
to inbreeding depression, and that the population is at the stable age distribution. The effects of 
catastrophes are incorporated into the life table analysis by using birth and death rates that are 
weighted averages of the values in years with and without catastrophes, weighted by the probability 
of a catastrophe occurring or not occurring.  
 
(6)  Iterative simulation of the population proceeds via steps 7 through 26 below. 
n
p
p
p
)
1
(
)
(
SE
−
=
(
)(
)
L
s
K
K
+
+
=
1
3
max


 
VORTEX Version 9.50 User’s Manual 
 
129 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
 
(7)  The starting population is assigned an age and sex structure. The user can specify the exact age-sex 
structure of the starting population, or can specify an initial population size and request that the 
population be distributed according to the stable age distribution calculated from the life table. 
Individuals in the starting population are assumed to be unrelated. Thus, inbreeding can occur only 
in second and later generations. 
 
(8)  Two unique alleles at a hypothetical neutral genetic locus are assigned to each individual in the 
starting population and to each individual supplemented to the population during the simulation. 
VORTEX therefore uses an infinite alleles model of genetic variation. The subsequent fate of genetic 
variation is tracked by reporting the number of extant neutral alleles each year, the expected 
heterozygosity or gene diversity, and the observed heterozygosity. The expected heterozygosity, 
derived from the Hardy-Weinberg equilibrium, is given by 
in which pi is the frequency of allele i in the population. The observed heterozygosity is simply the 
proportion of the individuals in the simulated population that are heterozygous. Because of the 
starting assumption of two unique alleles per founder, the initial population has an observed 
heterozygosity of 1.0 at the hypothetical locus and only inbred animals can become homozygous. 
Proportional loss of heterozygosity through random genetic drift is independent of the initial 
heterozygosity and allele frequencies of a population (Crow and Kimura 1970), so the expected 
heterozygosity remaining in a simulated population is a useful metric of genetic decay for 
comparison across scenarios and populations. The mean observed heterozygosity reported by 
VORTEX is the mean inbreeding coefficient of the population. 
 
(9)  For each of the10 alleles at five non-neutral loci that are used to model inbreeding depression, each 
founder is assigned a unique lethal allele with probability equal to 0.1 x the mean number of lethal 
alleles per individual.  
 
(10)  Years are iterated via steps 11 through 25 below.  
 
(11)  The probabilities of females producing each possible size litter are adjusted to account for density 
dependence of reproduction (if any). 
 
(12)  Birth rate, survival rates, and carrying capacity for the year are adjusted to model environmental 
variation. Environmental variation is assumed to follow binomial distributions for birth and death 
rates and a normal distribution for carrying capacity, with mean rates and standard deviations 
specified by the user. At the outset of each year a random number is drawn from the specified 
binomial distribution to determine the percent of females producing litters. The distribution of litter 
sizes among those females that do breed is maintained constant. Another random number is drawn 
from a specified binomial distribution to model the environmental variation in mortality rates. If 
environmental variations in reproduction and mortality are chosen to be correlated, the random 
number used to specify mortality rates for the year is chosen to be the same percentile of its binomial 
distribution as was the number used to specify reproductive rate. Otherwise, a new random number 
is drawn to specify the deviation of age- and sex-specific mortality rates from their means. 
Environmental variation across years in mortality rates is always forced to be correlated among age 
and sex classes. 
 
The carrying capacity (K) for the year is determined by first increasing or decreasing the carrying 
capacity at year 1 by an amount specified by the user to account for changes over time. 
(
)
∑
−
=
2
1
i
e
p
H


VORTEX Version 9.50 User’s Manual 
130 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
Environmental variation in K is then imposed by drawing a random number from a normal 
distribution with the specified values for mean and standard deviation. 
 
(13)  Birth rates and survival rates for the year are adjusted to model any catastrophes determined to have 
occurred in that year. 
 
(14)  Breeding males are selected for the year. A male of breeding age is placed into the pool of potential 
breeders for that year if a random number drawn for that male is less than the proportion of adult 
males specified to be breeding. Breeding males are selected independently each year; there is no 
long-term tenure of breeding males and no long-term pair bonds. 
 
(15)  For each female of breeding age, a mate is drawn at random from the pool of breeding males for that 
year. If the user specifies that the breeding system is monogamous, then each male can only be 
paired with a single female each year. Males are paired only with those females which have already 
been selected for breeding that year. Thus, males will not be the limiting sex unless there are 
insufficient males to pair with the successfully breeding females.  
 
If the breeding system is polygynous, then a male may be selected as the mate for several females. 
The degree of polygyny is determined by the proportion of males in the pool of potential breeders 
each year.  
 
The size of the litter produced by that pair is determined by comparing the probabilities of each 
potential litter size (including litter size of 0, no breeding) to a randomly drawn number. The 
offspring are produced and assigned a sex by comparison of a random number to the specified birth 
sex ratio. Offspring are assigned, at random, one allele at the hypothetical genetic locus from each 
parent.  
 
(16)  The genetic kinship of each new offspring to each other living animal in the population is 
determined. The kinship between new animal A, and another existing animal, B, is 
in which fij is the kinship between animals i and j, M is the mother of A, and P is the father of A. The 
inbreeding coefficient of each animal is equal to the kinship between its parents, F = fMP, and the 
kinship of an animal to itself is 
(
)
F
fA
+
=
1
5
.
0
. (See Ballou 1983 for a detailed description of this 
method for calculating inbreeding coefficients.) 
 
(17)  The survival of each animal is determined by comparing a random number to the survival 
probability for that animal. In the absence of inbreeding depression, the survival probability is given 
by the age and sex-specific survival rate for that year. If a newborn individual is homozygous for a 
lethal allele, it is killed. Otherwise, the survival probability for individuals in their first year is 
multiplied by  
in which b is the number of lethal equivalents per haploid genome, and Pr[Lethals] is the proportion 
of this inbreeding effect due to lethal alleles.  
 
(18)  The age of each animal is incremented by 1. 
 
(19)  If more than one population is being modeled, migration among populations occurs stochastically 
with specified probabilities. 
(
)
PB
MB
AB
f
f
f
+
=
5
.
0
[
]
(
)F
Lethals
b
e
Pr
1−
−


 
VORTEX Version 9.50 User’s Manual 
 
131 
Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
 
(20)  If population harvest is to occur that year, the number of harvested individuals of each age and sex 
class are chosen at random from those available and removed. If the number to be removed do not 
exist for an age-sex class, VORTEX continues but reports that harvest was incomplete. 
 
(21)  Dead animals are removed from the computer memory to make space for future generations.  
 
(22)  If population supplementation is to occur in a particular year, new individuals of the specified 
age-class are created. Each immigrant is assumed to be genetically unrelated to all other individuals 
in the population, and it carries the number of lethal alleles that was specified for the starting 
population.  
 
(23)  The population growth rate is calculated as the ratio of the population size in the current year to the 
previous year.  
 
(24)  If the population size (N) exceeds the carrying capacity (K) for that year, additional mortality is 
imposed across all age and sex classes. The probability of each animal dying during this carrying 
capacity truncation is set to (N - K)/N, so that the expected population size after the additional 
mortality is K. 
 
(25)  Summary statistics on population size and genetic variation are tallied and reported. 
 
(26)  Final population size and genetic variation are determined for the simulation.  
 
(27)  Summary statistics on population size, genetic variation, probability of extinction, and mean 
population growth rate are calculated across iterations and output. 


VORTEX Version 9.50 User’s Manual 
132 Appendix I 
An Overview of Population Viability Analysis Using VORTEX 
 


 
VORTEX Version 9.50 User’s Manual 
 
133 
Appendix II 
Literature Cited 
 
Appendix 
 
 
Literature Cited 
 
 
 
 
 
 
 
Akçakaya, H.R. 1997. RAMAS Metapop: Viability Analysis for Stage-Structured Metapopulations (Version 2.0). 
Setauket, NY: Applied Biomathematics. 
Altmann, J., D. Schoeller, S.A. Altmann, P. Muruthi and R.M. Sapolsky. 1993. Body size and fatness of free-living 
baboons reflect food availability and activity levels. American Journal of Primatology 30:149-161. 
Alvarez, K. 1993. Twilight of the Panther. Biology, Bureaucracy, and Failure in an Endangered Species Program. 
Myakka River Publ., Sarasota, Florida. 
Ballou, J.D. 1983. Calculating inbreeding coefficients from pedigrees. Pages 509-520 in: Schonewald-Cox, C.M, 
S.M. Chambers, B. MacBryde, and W.L. Thomas (eds.). Genetics and Conservation: A Reference for Managing 
Wild Animal and Plant Populations. Menlo Park, California: Benjamin/Cummings. 
Ballou, J.D. 1997. Ancestral inbreeding only minimally affects inbreeding depression in mammalian populations. 
Journal of Heredity 88:169-178. 
Ballou, J.D. and R.C. Lacy. 1995. Identifying genetically important individuals for management of genetic diversity  
in pedigreed populations. Pages 76-111 in J.D. Ballou, M. Gilpin, and T.J. Foose (eds.), Population 
Management for Survival & Recovery. Analytical Methods and Strategies in Small Population Conservation. 
New York: Columbia University Press. 
Ballou, J.D., R.C. Lacy, D. Kleiman, A. Rylands, and S. Ellis (eds.). 1997. Leontopithecus II. The Second 
Population and Habitat Viability Assessment for Lion Tamarins (Leontopithecus). Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Belovsky, G.E. 1987. Extinction models and mammalian persistence. Pages 35-57 in: Soulé, M.E. (ed.).  Viable 
Populations for Conservation. Cambridge: Cambridge University Press. 
Berger, J. 1990. Persistence of different-sized populations: an empirical assessment of rapid extinctions in bighorn 
sheep. Conservation Biology 4:91-98. 
Bonaccorso, F., P. Clark, P.S. Miller, and O. Byers (eds.). 1999. Conservation Assessment and Management Plan 
for the Tree Kangaroos of Papua New Guinea and Population and Habitat Viability Assessment for Matschie’s 
Tree Kangaroo: Final Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Bormann, F.H. and S.R. Kellert. 1991. Ecology, Economics, and Ethics. The Broken Circle. New Haven: Yale 
University Press. 
Boyce, M.S. 1992. Population viability analysis. Annual Review of Ecology and Systematics 23:481-506. 
II 


VORTEX Version 9.50 User’s Manual 
134 Appendix II 
Literature Cited 
Brussard, P. 1985. Minimum viable populations: how many are too few? Restoration and Management Notes 
3:21-25. 
Burgman, M., S. Ferson and H.R. Akçakaya. 1993. Risk Assessment in Conservation Biology. New York: Chapman 
and Hall.  
Caswell, H. 2001. Matrix Population Models. 2nd ed. Sunderland, MA: Sinauer. 
Caughley, G. 1977. Analysis of Vertebrate Populations. London: John Wiley and Sons. 
Charlesworth, D., and B. Charlesworth. 1987. Inbreeding depression and its evolutionary consequences. Annual 
Reviews of Ecology and Systematics 18:237-268. 
Clark, T.W. 1989. Conservation Biology of the Black-Footed Ferret. Philadelphia: Wildlife Preservation Trust 
International. 
Clark, T.W. 1993. Creating and using knowledge for species and ecosystem conservation: Science, organizations, 
and policy. Perspectives in Biology and Medicine 36:497-525. 
Clark, T.W., R.M. Warneke and G.G. George. 1990. Management and conservation of small populations. Pages 1-
18 in: Clark, T.W. and J.H. Seebeck (eds.). Management and Conservation of Small Populations. Brookfield, 
Illinois: Chicago Zoological Society.  
Clark, T.W., G.N. Backhouse and R.C. Lacy. 1991. The population viability assessment workshop: A tool for 
threatened species management. Endangered Species Update 8:1-5. 
Clark, T.W., and Seebeck, J.H. (eds.) 1990. Management and Conservation of Small Populations. Brookfield, 
Illinois: Chicago Zoological Society.  
Clarke, G.M. 1995. Relationships between developmental stability and fitness: Application for conservation biology. 
Conservation Biology 9:18-24. 
Crow, J.F. and Kimura, M. 1970. Introduction to Population Genetics Theory. New York: Harper and Row. 
Doughty, R.W. 1989. Return of the Whooping Crane. Austin : University of Texas Press. 
Edroma, E.L., N. Rosen, and P.S. Miller (eds.). 1997. Conserving the Chimpanzees of Uganda: Population and 
Habitat Viability Assessment for Pan troglodytes schweinfurthii. Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Ellis, S., K. Hughes, C. Kuehler, R.C. Lacy and U.S. Seal (eds.). 1992a. Alala, Akohekohe, and Palila Population 
and Habitat Viability Assessment Reports. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Ellis, S., C. Kuehler, R.C. Lacy, K. Hughes and U.S. Seal (eds.). 1992b. Hawai`ian Forest Birds Conservation 
Assessment and Management Plan. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Falconer, D.S. 1981. Introduction to Quantitative Genetics. 2nd ed. New York: Longman. 
Fisher, R.A. 1958. The Genetical Theory of Natural Selection. 2nd ed. New York; Dover. 
Fowler, C.W. 1981. Density dependence as related to life history strategy. Ecology 62:602-610. 
Franklin, I.R. 1980. Evolutionary change in small populations. Pages 135-149 in: Soulé, M.E. and B.A. Wilcox 
(eds.). Conservation Biology: An Ecological/Evolutionary Perspective. Sunderland, MA: Sinauer Associates.  
Foose, T.J., R.C. Lacy, R. Brett and U.S. Seal (eds.). 1993. Kenyan Black Rhino Metapopulation Workshop Report. 
Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Gilpin, M.E. 1987. Spatial structure and population vulnerability. Pages 125-139 in: Soulé, M.E. (ed.).  Viable 
Populations for Conservation. Cambridge: Cambridge University Press. 
Gilpin, M.E. 1989. Population viability analysis. Endangered Species Update 6:15-18.  
Gilpin, M.E., and M.E. Soulé. 1986. Minimum viable populations: processes of extinction. Pages 19-34 in: Soulé, 
M.E. (ed.). Conservation Biology: The Science of Scarcity and Diversity. Sunderland, MA: Sinauer Associates.  


 
VORTEX Version 9.50 User’s Manual 
 
135 
Appendix II 
Literature Cited 
Goodman, D. 1987. The demography of chance extinction. Pages 11 – 34 in: Soulé, M.E. (ed.). Viable Populations 
for Conservation. Cambridge: Cambridge University Press.  
Gunn, A., U.S. Seal, and P.S. Miller (eds.). 1998. Population and Habitat Viability Assessment Workshop for Peary 
Caribou and Arctic-Island Caribou (Rangifer tarandus). Apple Valley, MN: Conservation Breeding Specialist 
Group (SSC/IUCN). 
Hanski, I.A and M.E Gilpin. 1991. Metapopulation dynamics: A brief history and conceptual domain. Biological 
Journal of the Linnean Society 42:3-16.  
Hanski, I.A and M.E Gilpin (eds.). 1997. Metapopulation Biology: Ecology, Genetics, and Evolution. London: 
Academic Press. 
Hedrick, P.W. 1994. Purging inbreeding depression and the probability of extinction: full-sib mating. Heredity 
73:363-372. 
Herrero, S., P.S. Miller and U. S. Seal  (eds.). 2000. Population and Habitat Viability Assessment Workshop for the 
Grizzly Bear of the Central Rockies Ecosystem (Ursus arctos horribilis). Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Hobbs, N.T., and D.M. Swift. 1985. Estimates of habitat carrying capacity incorporating explicit nutritional 
constraints. Journal of Wildlife Management 49:814-822. 
Holling, C.S. (ed.). 1978. Adaptive Environmental Assessment and Management. International Series on Applied 
Systems Analysis 3, International Institute for applied systems analysis. Toronto: John Wiley and Sons. 
Hosack, D.A. 1998. Population Viability Analysis Workshop for the Endangered Sonoran Pronghorn (Antilocapra 
americana sonoriensis) in the United States. Washington, DC: Defenders of Wildlife. 
Ims, R.A., and N.G. Yoccoz. 1997. Studying transfer processes in metapopulations: Emigration, migration, and 
colonization. Pages 247 – 265 in: Hanski, I.A. and M.E. Gilpin (eds.). Metapopulation Biology: Ecology, 
Genetics, and Evolution. London: Academic Press.  
IUCN Species Survival Commission. 1994. IUCN Red List Categories. IUCN, Gland, Switzerland. 
Kirkpatrick, S, and Stoll, E. 1981. A very fast shift-register sequence random number generator. Journal of 
Computational Physics 40:517. 
Kjos, C., O. Byers, P.S. Miller, J. Borovansky, and U.S. Seal (eds.). 1998. Population and Habitat Viability 
Assessment Workshop for the Winged Mapleleaf Mussel (Quadrula fragosa): Final Report. Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Krebs, C.J. 1994. Ecology: The Experimental Analysis of Distribution and Abundance. 4th ed. New York: Harper 
Collins. 
Lacy, R.C. 1993a. VORTEX: A computer simulation model for Population Viability Analysis. Wildlife Research 
20:45-65. 
Lacy, R.C. 1993b. Impacts of inbreeding in natural and captive populations of vertebrates: Implications for 
conservation. Perspectives in Biology and Medicine. 36:480-496. 
Lacy, R.C. 1993/1994. What is Population (and Habitat) Viability Analysis? Primate Conservation 14/15:27-33. 
Lacy, R.C. 1997. Importance of genetic variation to the viability of mammalian populations. Journal of Mammalogy 
78:320-335. 
Lacy, R.C., G. Alaks, and A. Walsh. 1996. Hierarchical analysis of inbreeding depression in Peromyscus polionotus.  
Evolution 50:2187-2200. 
Lacy, R.C. and J.D. Ballou. 1998. Effectiveness of selection in reducing the genetic load in populations of 
Peromyscus polionotus during generations of inbreeding. Evolution 52:900-909. 
Lacy, R.C. and T.W. Clark. 1990. Population viability assessment of the eastern barred bandicoot in Victoria. Pages 
131-146 in: Clark, T.W. and J.H. Seebeck (eds.). Management and Conservation of Small Populations. 
Brookfield, IL: Chicago Zoological Society.  


VORTEX Version 9.50 User’s Manual 
136 Appendix II 
Literature Cited 
Lacy, R.C, N.R. Flesness and U.S. Seal (eds.). 1989. Puerto Rican Parrot Population Viability Analysis. Report to 
the U.S. Fish and Wildlife Service. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Lacy, R.C. and D.B. Lindenmayer. 1995. A simulation study of the impacts of population sub-division on the 
mountain brushtail possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupialia), in south-eastern 
Australia. II. Loss of genetic variation within and between sub-populations. Biological Conservation 73:131-
142. 
Lacy, R.C., and P.S. Miller. 2002. Incorporating human populations and activities into population viability analysis.  
 
Pages 490-510 in S.R. Beissinger  and D.R. McCullough (eds.), Population Viability Analysis. Chicago: 
University of Chicago Press. 
Lacy, R.C., Petric, A.M., and Warneke, M. 1993. Inbreeding and outbreeding depression in captive populations of 
wild species. Pages 352-374 in Thornhill, N.W. (ed.). The Natural History of Inbreeding and Outbreeding. 
Chicago: University of Chicago Press. 
Lande, R. and G.F. Barrowclough. 1987. Effective population size, genetic variation, and their use in population 
management. Pages 87-123 in Soulé, M.E. (ed.). Viable Populations for Conservation. Cambridge: Cambridge 
University Press. 
Latour, A. (1986). Polar normal distribution. Byte (August 1986):131-2. 
Lindenmayer, D.B. and R.C. Lacy. 1995a. Metapopulation viability of Leadbeater's Possum, Gymnobelideus 
leadbeateri, in fragmented old-growth forests. Ecological Applications 5:164-182. 
Lindenmayer, D.B. and R.C. Lacy. 1995b. Metapopulation viability of arboreal marsupials in fragmented old-
growth forests: Comparison among species. Ecological Applications 5:183-199. 
Lindenmayer, D.B. and R.C. Lacy. 1995c. A simulation study of the impacts of population sub-division on the 
mountain brushtail possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupialia), in south-eastern 
Australia. I. Demographic stability and population persistence. Biological Conservation 73:119-129. 
Lindenmayer, D.B., T.W. Clark, R.C. Lacy and V.C. Thomas. 1993. Population viability analysis as a tool in 
wildlife conservation policy: A review with reference to Australia. Environmental Management 17:745-758. 
Mace, G.M. and R. Lande. 1991. Assessing extinction threats: Toward a re-evaluation of IUCN threatened species 
categories. Conservation Biology 5:148-157. 
Mace, G. et al. 1992. The development of new criteria for listing species on the IUCN Red List. Species 19:16-22. 
Mace, G. and S. Stuart. 1994. Draft IUCN Red List Categories, Version 2.2. Species 21-22:13-24. 
MacNab, J. 1985. Carrying capacity and related slippery shibboleths. Wildlife Society Bulletin 13:403-410. 
Maguire, L.A. 1986. Using decision analysis to manage endangered species populations. Journal of Environmental 
Management 22:345-360. 
Maguire, L.A., R.C. Lacy, R.J. Begg and T.W. Clark. 1990. An analysis of alternative strategies for recovering the 
eastern barred bandicoot in Victoria. Pages 147-164 in: Clark, T.W. and J.H. Seebeck (eds.). Management and 
Conservation of Small Populations. Brookfield, IL: Chicago Zoological Society.  
Maier, W.L. (1991). A fast pseudo random number generator. Dr. Dobb's Journal (May 1991):152-7. 
Manansang, J., A. MacDonald, D. Siswomartono, P.S. Miller, and U.S. Seal (eds.). 1996. Population and Habitat 
Viability Assessment for the Babirusa (Babyrousa babyrussa). Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Miller, P.S., and R.C. Lacy.  2003a. Integrating the human dimension into endangered species risk assessment. 
Pages 41-63 in: F.R. Westley and P.S. Miller, eds. Experiments in Consilience: Integrating Social and Scientific 
Responses to Save Endangered Species. Island Press, Washington, DC. 
Miller, P.S., and R.C. Lacy.  2003b. Metamodels as a tool for risk assessment. Pages 333-351 in: F.R. Westley and  
P.S. Miller, eds. Experiments in Consilience: Integrating Social and Scientific Responses to Save Endangered 
Species. Island Press, Washington, DC. 


 
VORTEX Version 9.50 User’s Manual 
 
137 
Appendix II 
Literature Cited 
Mirande, C., R. Lacy, and U. Seal (eds.). 1991. Whooping Crane (Grus americana) Conservation Viability 
Assessment Workshop Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Morton, N.E., Crow, J.F., and Muller, H.J. 1956. An estimate of the mutational damage in man from data on 
consanguineous marriages. Proceedings of the National Academy of Sciences, USA 42:855-863. 
O'Brien, S.J. and Evermann, J.F. 1988. Interactive influence of infectious diseases and genetic diversity in natural 
populations. Trends in Ecology and Evolution 3:254-9.  
Odum, A., et al (eds.). 1993. Aruba Island Rattlesnake Population and Habitat Viability Assessment (PHVA) 
Workshop. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Pergams, O.R.W., R.C. Lacy, and M.V. Ashley. 2000. Conservation and management of Anacapa Island deer mice. 
Conservation Biology 14:819-832. 
Petit, S., and L. Pors. 1996. Survey of columnar cacti and carrying capacity for nectar-feeding bats on Curaçao. 
Conservation Biology 10:769-775. 
Pielou, E.C. 1977. Mathematical Ecology. New York: John Wiley and Sons. 
Ralls, K., Ballou, J.D., and Templeton. A.R. 1988. Estimates of lethal equivalents and the cost of inbreeding in 
mammals. Conservation Biology 2:185-93.  
Ricklefs, R.E. 1979. Ecology. 2nd ed. New York: Chiron. 
Robertson, A. (1960). A theory of limits in artificial selection. Proceedings Royal Society of London 153B:234-49. 
Rohlf, F.J., and R.R. Sokal. 1981. Statistical Tables. 2nd ed. New York: W.H. Freeman and Company. 
Ruggiero, L.F., G.D. Hayward and J.R. Squires. 1994. Viability analysis in biological evaluations: Concepts of 
population viability analysis, biological population, and ecological scale. Conservation Biology 8:364-372. 
Rylands, A.B. 1993/1994. Population viability analyses and the conservation of the lion tamarins, Leontopithecus, of 
south-east Brazil. Primate Conservation 14/15: 34-42. 
Samuels, A. and J. Altmann. 1991. Baboons of the Amboseli basin: Demographic stability and change. International 
Journal of Primatology 12:1-19. 
Sapolsky, R.M. 1982. The endocrine stress-response and social status in the wild baboon. Hormones and Behavior 
15:279-292. 
Sapolsky, R.M. 1986. Endocrine and behavioral correlates of drought in the wild baboon. American Journal of 
Primatology 11:217-227. 
Seal, U.S. (ed.). 1992. Genetic Management Strategies and Population Viability  of the Florida Panther (Felis 
concolor coryi). Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1994. Attwater’s Prairie Chicken Population and Habitat Viability Assessment. Apple Valley, MN: 
Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. and R.C. Lacy (eds.). 1989. Florida Panther Population Viability Analysis. Report to the U.S. Fish and 
Wildlife Service. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., J.D. Ballou and C.V. Padua (eds.). 1990. Leontopithecus Population Viability Analysis Workshop Report. 
Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., R.C. Lacy, K. Medley, R. Seal and T.J. Foose (eds.). 1991. Tana River Primate Reserve Conservation 
Assessment Workshop Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Selander, R.K. 1983. Evolutionary consequences of inbreeding. Pages 201-215 in: Schonewald-Cox, C.M, S.M. 
Chambers, B. MacBryde, and W.L. Thomas (eds.). Genetics and Conservation: A Reference for Managing Wild 
Animal and Plant Populations. Menlo Park, CA: Benjamin/Cummings. 
Shaffer, M.L. 1981. Minimum population sizes for species conservation. Bioscience 1:131-134. 
Shaffer, M.L. 1987. Minimum viable populations: Coping with uncertainty. Pages 69-86 in: Soulé, M.E. (ed.). 
Viable Populations for Conservation. Cambridge: Cambridge University Press. 


VORTEX Version 9.50 User’s Manual 
138 Appendix II 
Literature Cited 
Shaffer, M.L. 1990. Population viability analysis. Conservation Biology 4:39-40.  
Simberloff, D.A. 1986. The proximate causes of extinction. Pages 259-276 in: Raup, D.M., and D. Jablonski (eds.). 
Patterns and Processes in the History of Life. Berlin: Springer-Verlag. 
Simberloff, D.A. 1988. The contribution of population and community biology to conservation science. Annual 
Review of Ecology and Systematics 19:473-511. 
Simmons, M.J., and J.F. Crow. 1977. Mutations affecting fitness in Drosophila populations. Annual Review of 
Genetics 11:49-78. 
Sokal, R.R., and F.J. Rohlf. 1994. Biometry. 3rd ed. New York: W.H. Freeman and Company. 
Soulé, M.E. (ed). 1987. Viable Populations for Conservation. Cambridge: Cambridge University Press. 
Soulé, M., M. Gilpin, W. Conway and T. Foose. 1986. The millenium ark: How long a voyage, how many 
staterooms, how many passengers? Zoo Biology 5:101-113. 
Starfield, A.M. and A.L. Bleloch. 1986. Building Models for Conservation and Wildlife Management., New York: 
Macmillan. 
Thomas, C.D. 1990. What do real population dynamics tell us about minimum population sizes? Conservation 
Biology 4:324-327.  
Walker, S. and S. Molur (eds.). 1994. Population and Habitat Viability Analysis (PHVA) Workshop for 
Indian/Nepali Rhinoceros. Zoo Outreach Organisation/CBSG India, Coimbatore. 
Werikhe, S., L. Macfie, N. Rosen, and P.S. Miller (eds.). 1998. Can the Mountain Gorilla Survive? Population and 
Habitat Viability Assessment Workshop for Gorilla gorilla beringei. Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Wright, S. 1977. Evolution and the Genetics of Populations. Vol. 3. Experimental Results and Evolutionary 
Deductions. Chicago: University of Chicago Press. 
Zar, J.H. 1996. Biostatistical Analysis. 3rd ed. Englewood Cliffs: Prentice Hall. 
 


 
VORTEX Version 9.50 User’s Manual 
 
139 
Appendix III 
VORTEX Bibliography 
Appendix 
 
 
 
VORTEX Bibliography 
 
We have attempted to compile an exhaustive list of articles and reports 
that use VORTEX as a tool in population viability analysis. If we have 
missed any other examples, or if you have published a contribution that 
you would like to add to the growing list, please contact the Conservation 
Breeding Specialist Group (see page 3 for details) and we will update this 
Bibliography. 
 
 
Ahlmann, V., K. Collins, and U.S. Seal (eds.). 2000. Riverine Rabbit (Bunolagus monticularis): A Population and 
Habitat Viability Assessment Workshop. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Allendorf, F. and N. Ryman. 2002. The role of genetics in population viability analysis. Pages 50-85 in: Beissinger, 
S.R. and D.R. McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Araya, B., D. Garland, G. Espinoza, A. Sanhuesa, A. Simeone, A. Teare, C. Zavalaga, R. Lacy, and S. Ellis (eds.). 
2000. Population and Habitat Viability Assessment for the Humboldt Penguin (Spheniscus humboldti). Final 
Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Armbruster, P., P. Fernando, and R. Lande. 1999. Time frames for population viability analysis of species with long 
generations: An example with Asian elephants. Animal Conservation 2(1):69-73. 
Armstrong, D.P. and J.G. Ewen. 2002. Dynamics and viability of a New Zealand robin population reintroduced to 
regenerating fragmented habitat. Conservation Biology 16(4):1074-1085. 
Armstrong, D.P., Perrott, J.K. and Castro, I. 1997. The effect of food supply on the viability of hihi populations: An 
experimental study on Mokoia. Report to WWF-NZ, Wellington, New Zealand, 130pp. 
Arteaga, A., I. Canizales, G. Hernandez, M. Cruz Lamas, A. De Luca, M. Muñoz, A. Ochoa, A. Seijas, J. 
Thorbjarnarson, A. Velasco, S. Ellis, and U. Seal (eds.). 1997. Taller de Análisis de la Viabilidad Poblacional y 
del Hábitat del Caiman del Orinoco (Crocodylus intermedius). Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Ashraf, N.V.K., R. Chellam, S. Molur, U.S. Seal, D. Sharma, and S. Walker (eds.). 1995. Asiatic Lion Population 
and Habitat Viability Assessment Report. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Asquith, N. M. 2001. Misdirections in conservation biology. Conservation Biology 15(2):345-352. 
Aurioles Gamboa, D., C. Godínez Reyes, M.E. Durán Lizarraga, F.J. García Rodrígurz, C.J. Hernández Camacho, S. 
Luque, P.S. Miller and S. Ellis (eds.). 1999. Conservación, Análisis y Manejo Planificado sobre los Pinnípedos 
de México y Análisis de la Viabilidad de la Población y del Hábitat para el Lobo Marino de California 
(Zalophus californianus californianus). Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
III


VORTEX Version 9.50 User’s Manual 
140 Appendix III 
VORTEX Bibliography 
Ballou, J.D., R.C. Lacy, D. Kleiman, A. Rylands, and S. Ellis (eds.). 1997. Leontopithecus II. The Second 
Population and Habitat Viability Assessment for Lion Tamarins (Leontopithecus). Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Barongi, R., J. Ventocilla, P.S. Miller, and U.S. Seal (eds.). 1996. Population and Habitat Viability Assessment for 
Baird’s Tapir (Tapirus bairdi). Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Beissinger, S.R. 2002. Population viability analysis: Past, present, future. Pages 5-17 in: Beissinger, S.R. and D.R. 
McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Beissinger, S.R., J.R. Walters, D.G. Catanzano, K.G. Smith, J.B. Dunning, S.M. Haig, B.R. Noon, and B.M. Smith. 
2002. The use of models in avian conservation. Current Ornithology 17 (in press). 
Belovsky, G.E., C. Mellison, C. Larson, and P.A. Van Zandt. 2002. How good are PVA models? Testing their 
predictions with experimental data on the brine shrimp. Pages 257-283 in: Beissinger, S.R. and D.R. 
McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Berry, H., M. Bush, B. Davidson, O. Forge, B. Fox, J. Grisham, M. Howe, S. Hurlbut, L. Marker-Kraus, J. 
Martenson, L. Munson, K. Nowell, M. Schumann, T. Shille, K. Venzke, T. Wagener, D. Wildt, S. Ellis, and U. 
Seal (eds.). 1997. Population and Habitat Viability Assessment for the Namibian Cheetah (Acinonyx jubatus) 
and Lion (Panthera leo). Workshop Report. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Bonaccorso, F., P. Clark, P.S. Miller, and O. Byers (eds.). 1999. Conservation Assessment and Management Plan 
for the Tree Kangaroos of Papua New Guinea and Population and Habitat Viability Assessment for Matschie’s 
Tree Kangaroo: Final Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Bowland, A.E., K.S. Bishop, P.J. Taylor, J.Lamb, F.H. van der Bank, E. van Wyk, and D. York. 2001. Estimation 
and management of genetic diversity in small populations of plains zebra (Equus quagga) in KwaZulu-Natal, 
South Africa. Biochemical Systematics & Ecology 29(6): 563-583. 
Boyce, M.S. 2002. Reconciling the small-population and declining-population paradigms. Pages 41-49 in: 
Beissinger, S.R. and D.R. McCullough (eds.). Population Viability Analysis. Chicago, IL: University of 
Chicago Press. 
Brito, D., and F.A.S. Fernandez. 2000. Metapopulation viability of the marsupial Micoureus demerarae in small 
Atlantic forest fragments in south-eastern Brazil. Animal Conservation 3(3):201-209. 
Brito, D. and M. d. S. L. Figueiredo. 2003. Minimum viable population and conservation status of the Atlantic  
Forest spiny rat Trinomys eliasi. Biological Conservation 113(1):153-158. 
Brook, B.W., M.A. Burgman, and R. Frankham. 2000. Differences and congruencies between PVA packages: The 
importance of sex ratio for predictions of extinction risk. Conservation Ecology 4(1): 6. [online] URL: 
http://www.consecol.org/vol4/iss1/art6. 
Brook, B.W., Cannon, J.R., Lacy, R.C., Mirande, C. and Frankham, R. 1999. A comparison of the population 
viability analysis packages GAPPS, INMAT, RAMAS and VORTEX for the Whooping Crane (Grus americana). 
Animal Conservation 2:23-31.  
Brook, B.W. & Kikkawa, J. 1998. Examining threats faced by island birds: A PVA on the Capricorn silvereye using 
long-term data. Journal of Applied Ecology 35: 491-503.  
Brook, B.W., Lim, L., Harden, R. and Frankham, R. 1997a. Does population viability analysis software predict the 
behaviour of real populations? A retrospective study on the Lord Howe Island woodhen Tricholimnas sylvestris 
(Sclater). Biological Conservation 82: 119-128. 
Brook, B.W., Lim, L., Harden, R. and Frankham, R. 1997b. How secure is the Lord Howe Island Woodhen? A 
population viability analysis using VORTEX. Pacific Conservation Biology 3:125-133.  
Bustamante, J. 1996. Population viability analysis of captive and released bearded vulture populations. Conservation 
Biology 10:822-831. 


 
VORTEX Version 9.50 User’s Manual 
 
141 
Appendix III 
VORTEX Bibliography 
Cancino, J., P.S. Miller, J. Bernal Stoopen, and J. Lewis (eds.). 1995. Population and Habitat Viability Assessment 
for the Peninsular Pronghorn (Antilocapra americana peninsularis). Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Chapman, A., Brook, B.W., Clutton-Brock, T.H., Grenfell, B.T. and Frankham, R. 2001. Population viability 
analysis on a cycling population: a cautionary tale. Biological Conservation 97(1):61-69.  
Clark, T.W., G.N. Backhouse, and R.C. Lacy. 1991a. The population viability assessment workshop: A tool for 
threatened species management. Endangered Species Update 8:1-5. 
Clark, T.W., G.N. Backhouse, and R.C. Lacy. 1991b. Report of a workshop on population viability assessment as a 
tool for threatened species management and conservation. Australian Zoologist 27:28-35. 
Clark, T.W., G.N. Backhouse, and R.C. Lacy. 2002. The population viability assessment workshop: A tool for 
threatened species management. Endangered Species Update 19(4):136-141. 
Combreau, O., F. Launay, and M. Lawrence. 2001. An assessment of annual mortality rates in adult-sized migrant 
houbara bustards (Chlamydotis (undulata) macqueenii). Animal Conservation 4(2):133-141. 
Conant, S. and M. Morin. 2001. Why isn't the Nihoa Millerbird extinct? Studies in Avian Biology 22:338-346. 
Conservation Breeding Specialist Group (SSC/IUCN). 1996. Population and Habitat Viability Assessment for the 
Striped Legless Lizard (Delma impar). Mosman, NSW: Australasian Regional Association of Zoological Parks 
and Aquaria.  
Conservation Breeding Specialist Group (SSC/IUCN). 2000. Conservation Assessment and Management Plan for 
Arabian Carnivores and Population and Habitat Viability Assessment for the Arabian Leopard and Tahr. Apple 
Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Conservation Breeding Specialist Group (SSC/IUCN). 2002. Evaluation et Plans de Gestion pour la Conservation 
(CAMP) de la Faune de Madagascar: Lemuriens, Autres Mammiferes, Reptiles et Amphibiens, Poissons d’eau 
douce et Evaluation de la Viabilite des Populations et des Habitats de Hypogeomys antimena (Vositse). Apple 
Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Edroma, E.L., N. Rosen, and P.S. Miller (eds.). 1997. Conserving the Chimpanzees of Uganda: Population and 
Habitat Viability Assessment for Pan troglodytes schweinfurthii. Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Ellis, S., and U.S. Seal. 1995. Tools of the trade to aid decision making for species survival. Biodiversity and 
Conservation 4:553-572. 
Ellis, S., K. Hughes, C. Kuehler, R.C. Lacy and U.S. Seal (eds.). 1992. Alala, Akohekohe, and Palila Population and 
Habitat Viability Assessment Reports. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Ewins, P., M. de Almeida, P. Miller and O. Byers (eds.). 2000. Population and Habitat Viability Assessment 
Workshop for the Wolves of Algonquin Park: Final Report. Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Fisher, A., E. Rominger, P. Miller and O. Byers. 1999. Population and Habitat Viability Assessment Workshop for 
the Desert Bighorn Sheep of New Mexico (Ovis canadensis): Final Report. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Foose, T.J., R.C. Lacy, R. Brett and U.S. Seal (eds.). 1993. Kenyan Black Rhino Metapopulation Workshop Report. 
Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Forys, E.A. and S.R. Humphrey. 1999. Use of population viability analysis to evaluate management options for the 
endangered Lower Keys marsh rabbit. Journal of Wildlife Management 63(1):251-260. 
Galimberti, F., S. Sanvito, L. Boitani, and A. Fabiani, A. 2001. Viability of the southern elephant seal population of 
the Falkland Islands. Animal Conservation 4(1): 81-88. 
Gonzalez, L.M., B. Heredia, A. Araujo, I. Robinson, J. Worms, P.S. Miller, and U.S. Seal (eds.). 2002. Population 
and Habitat Viability Assessment for the Mediterranean Monk Seal (Monachus monachus) in the Eastern 
Atlantic. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 


VORTEX Version 9.50 User’s Manual 
142 Appendix III 
VORTEX Bibliography 
González, S., M. Merino, M. Gimenez-Dixon, S. Ellis, and U.S. Seal (eds.). 1993. Population and Habitat Viability 
Assessment for the Pampas Deer (Ozotoceros bezoarticus). Apple Valley, MN: Captive Breeding Specialist 
Group (SSC/IUCN). 
Guichard, C., S. Ellis, Y. Matamoros, and U.S. Seal (eds.). 2001. Análisis de la Viabilidad de Poblaciónal y del 
Hábitat del Manatí en México. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Gunn, A., U.S. Seal, and P.S. Miller (eds.). 1998. Population and Habitat Viability Assessment Workshop for Peary 
Caribou and Arctic-Island Caribou (Rangifer tarandus). Apple Valley, MN: Conservation Breeding Specialist 
Group (SSC/IUCN). 
Guo, J., Y. Chen and J. Hu. 2002. Population viability analysis of giant pandas in the Yele Nature Reserve. Journal  
for Nature Conservation 10(1):35-40. 
Haig, S.M. and J.D. Ballou. 2002. Pedigree analyses in wild populations. Pages 388-405 in: Beissinger, S.R. and 
D.R. McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Haig, S.M., J.R. Belthoff, and D.H. Allen. 1993. Population viability analysis for a small population of red-cockaded 
woodpeckers and an evaluation of enhancement strategies. Conservation Biology 7:289-301. 
Hamilton, S. and H. Moller. 1995. Can PVA models using computer packages offer useful conservation advice? 
Sooty shearwaters Puffinus griseus in New Zealand: As a case study. Biological Conservation 73(2):107-117. 
Heredia, B., P. Gaona, A. Vargas, S. Ellis, and U.S. Seal (eds.). 1999. Taller Análisis de la Viabilidad de Población 
y del Habitat para el Lince Ibérico (Lynx pardinus). Apple Valley, MN: Conservation Breeding Specialist 
Group (SSC/IUCN). 
Herrero, S., P.S. Miller and U. S. Seal  (eds.). 2000. Population and Habitat Viability Assessment Workshop for the 
Grizzly Bear of the Central Rockies Ecosystem (Ursus arctos horribilis). Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Hosack, D.A., P.S. Miller, J.J. Hervert, and R.C. Lacy. 2002. A population viability analysis for the endangered 
Sonoran pronghorn, Antilocapra americana sonoriensis. Mammalia 66(2):207-229. 
Hou, W.-R., Z.-J. Zhang and J.-C. Hu. 2001. A preliminary analysis on population viability for black bear in  
Wolong. Zoological Research 22:357-361. 
Howells, O., and G.E. Jones. 1997. A feasibility study of reintroducing wild boar (Sus scrofa) to Scotland: Are 
existing woodlands large enough to support minimum viable populations? Biological Conservation 81:77-89. 
Jackson, S.M. 1999. Preliminary predictions of the impacts of habitat area and catastrophes on the viability of 
Mahogany Glider Petaurus gracilis populations. Pacific Conservation Biology 5(1):56-62.  
Jennings, M., R. Beiswinger, S. Corn, M. Parker, A. Pessier, B. Spencer, and P.S. Miller (eds.). 2001. Population 
and Habitat Viability Assessment for the Wyoming Toad (Bufo baxteri). Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
de Jong, Y. A., P. R. van Olst, and R. C. C. M. de Jong. 1997. Feasibility of reintroduction of the Eurasian lynx 
(Lynx lynx) on 'De Veluwe', the Netherlands, by using the stochastic simulation programme VORTEX. 
Zeitschrift fuerSaugetierkunde 62:44-51. 
Kaiya, Z., S. Ellis, S. Leatherwood, M. Bruford, and U.S. Seal (eds.). 1994. Baiji Population and Habitat Viability 
Assessment Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Kelly, B.T., P.S. Miller, and U.S. Seal (eds.). 1999. Population and Habitat Viability Assessment Workshop for the 
Red Wolf (Canis rufus). Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Kjos, C., O. Byers, P.S. Miller, J. Borovansky, and U.S. Seal (eds.). 1998. Population and Habitat Viability 
Assessment Workshop for the Winged Mapleleaf Mussel (Quadrula fragosa): Final Report. Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Kovács, T., Z. Korsós, I. Rehák, K. Corbett, and P.S. Miller (eds.). 2002. Population and Habitat Viability 
Assessment for the Hungarian Meadow Viper (Vipera ursinii rakosiensis). Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 


 
VORTEX Version 9.50 User’s Manual 
 
143 
Appendix III 
VORTEX Bibliography 
Kumar, A., S. Molur, and S. Walker (eds.). 1995. Lion Tailed Macaque Population and Habitat Viability 
Assessment Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Lacy, R.C. 1993. VORTEX: A computer simulation model for Population Viability Analysis. Wildlife Research 20:45-
65. 
Lacy, R.C. 1993/1994. What is Population (and Habitat) Viability Analysis? Primate Conservation 14/15:27-33. 
Lacy, R.C. 1996.  Further population modelling of northern white rhinoceros under various management scenarios.  
Appendix 3 in: Foose, T.J. (ed.). Summary – Northern White Rhinoceros Conservation Strategy Workshop. 
Cumberland, OH: International Rhino Foundation. 
Lacy, R.C. 2000. Structure of the VORTEX simulation model for population viability analysis. Ecological Bulletins 
48:191-203. 
Lacy, R.C. and T.W. Clark. 1990. Population viability assessment of the eastern barred bandicoot in Victoria. Pages 
131-146 in:Clark, T.W. and J.H. Seebeck (eds.). The Management and Conservation of Small Populations. 
Brookfield, IL: Chicago Zoological Society. 
Lacy, R.C. and T.W. Clark. 1993. Simulation modeling of American marten (Martes americana) populations: 
Vulnerability to extinction. Great Basin Naturalist 53:282-292. 
Lacy, R.C, N.R. Flesness and U.S. Seal (eds.). 1989. Puerto Rican Parrot Population Viability Analysis. Report to 
the U.S. Fish and Wildlife Service. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Lacy, R.C. and D.B. Lindenmayer. 1995. A simulation study of the impacts of population subdivision on the 
mountain brushtail possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupialia), in south-eastern 
Australia. II. Loss of genetic variation within and between subpopulations. Biological Conservation 73:131-
142. 
Lane, S.J. and  J.C. Alonso. 2001. Status and extinction probabilities of great bustard (Otis tarda) leks in Andalucia, 
southern Spain. Biodiversity & Conservation 10(6):893-910.  
Lee, H., D. Garshelis, U.S. Seal, and J. Shillcox (eds.). 2001. Asiatic Black Bears PHVA: Final Report. Apple 
Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Leighton, M; U.S. Seal, K. Soemarna, Adjisasmito, M. Wijaya, T.Mitra Setia, G. Shapiro, L. Perkins, K. Traylor-
Holzer, and R. Tilson. 1995. Orangutan life history and vortex analysis. Pages 97-107 in: Nadler, R.D., B.F.M. 
Galdikas, L.K. Sheeran, and N. Rosen (eds.). The Neglected Ape. New York: Plenum Press.  
de Leon, J., N. Lawas, R. Escalada, P. Ong, R. Callo, S. Hedges, J. Ballou, D. Armstrong, and U.S. Seal (eds.). 
1996. Tamaraw (Bubalus mindorensis) Population and Habitat Viability Assessment Report. Apple Valley, 
MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Li, X.H., D.M.Li, Y.G. Yong, and J. Zhang. 1997. A preliminary analysis on population viability analysis for giant 
panda in Foping. Acta Zoologica Sinica 43(3):285-293. 
Li, X. and D. Li. 1998. Current state and the future of the crested ibis (Nipponia nippon): A case study by population 
viability analysis.    Ecological Research 13(3):323-333. 
Lindenmayer, D.B., M.A. Burgman, H.R. Akçakaya, R.C. Lacy, and H.P. Possingham. 1995. A review of the 
generic computer programs ALEX, RAMAS/Space and VORTEX for modelling the viability of wildlife populations. 
Ecological Modelling 82:161-174.  
Lindenmayer, D.B., T.W. Clark, R.C. Lacy, and V.C. Thomas. 1993. Population viability analysis as a tool in 
wildlife conservation policy: With reference to Australia. Environmental Management 17:745-758. 
Lindenmayer, D.B. and R.C. Lacy. 1995a. Metapopulation viability of Leadbeater's possum, Gymnobelideus 
leadbeateri, in fragmented old-growth forests. Ecological Applications 5:164-182. 
Lindenmayer, D.B. and R.C. Lacy. 1995b. Metapopulation viability of arboreal marsupials in fragmented old-
growth forests: comparison among species. Ecological Applications 5:183-199.  


VORTEX Version 9.50 User’s Manual 
144 Appendix III 
VORTEX Bibliography 
Lindenmayer, D.B. and R.C. Lacy. 1995c. A simulation study of the impacts of population subdivision on the 
mountain brushtail possum, Trichosurus caninus Ogilby (Phalangeridae: Marsupialia), in south-eastern 
Australia. I. Demographic stability and population persistence. Biological Conservation 73:119-129. 
Lindenmayer, D.B. and R.C. Lacy. 2002. Small mammals, habitat patches and PVA models: A field test of model 
predictive ability. Biological Conservation 103(3):247-265. 
Lindenmayer, D.B., R.C. Lacy, and M.L. Pope. 2000. Testing a simulation model for population viability analysis. 
Ecological Applications 10:580-597. 
Lindenmayer, D.B., R.C. Lacy, V.C. Thomas, and T.W. Clark. 1993. Predictions of the impacts of changes in 
population size and environmental variability on Leadbeater's Possum, Gymnobelideus leadbeateri McCoy 
(Marsupialia: Petauridae) using Population Viability Analysis: An application of the computer program 
VORTEX. Wildlife Research 20:67-86. 
Lindenmayer, D.B., V.C. Thomas, R.C. Lacy, and T.W. Clark. 1991. Population Viability Analysis (PVA):  The 
concept and its applications, with a case study of Leadbeater's Possum, Gymnobelideus leadbeateri McCoy. 
Report to the Forest and Timber Inquiry (Resource Assessment Commission), Consultancy Series No. 
FTC91/18, Canberra, Australia. 170 pp. 
Lombard, K.B. 1996. A population viability analysis of the Hawaiian Monk Seal (Monachus schauinslandi). M. Sc. 
dissertation. University of Michigan, Ann Arbor, MI. 
Lorek, H. and M. Sonnenschein. 1999. Modelling and simulation software to support individual-based ecological 
modelling. Ecological Modelling 115(2-3):199-216. 
Maehr, D.S., R.C. Lacy, E.D. Land, O.L. Bass Jr., and T.S. Hoctor. 2002. Evolution of population viability 
assessments for the Florida panther: A multiperspective approach. Pages 284-311 in: Beissinger, S.R. and D.R. 
McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Maguire, L.A., R.C. Lacy, R.J. Begg, and T.W. Clark. 1990. An analysis of alternative strategies for recovering the 
eastern barred bandicoot in Victoria. Pages 147-164 in: Clark, T.W. and J.H. Seebeck (eds.). The Management 
and Conservation of Small Populations. Brookfield, IL: Chicago Zoological Society. 
Majluf, P., E.A. Babcock, J.C. Riveros, M.A. Schreiber, and W. Alderete. 2002. Catch and bycatch of sea birds and 
marine mammals in the small-scale fishery of Punta San Juan, Peru. Conservation Biology 16(5):1333-1343.  
Manansang, J., S. Hedges, D. Siswomartono, P.S. Miller, and U.S. Seal (eds.). 1996. Population and Habitat 
Viability Assessment Workshop for the Anoa (Bubalus depressicornis and Bubalus quarlesi). Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Manansang, J., A. MacDonald, D. Siswomartono, P.S. Miller, and U.S. Seal (eds.). 1996. Population and Habitat 
Viability Assessment for the Babirusa (Babyrousa babyrussa). Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Manansang, J., P.S. Miller, J.W. Grier, and U.S. Seal (eds.). 1997. Population and Habitat Viability Assessment for 
the Javan Hawk-Eagle (Spizaetus bartelsi). Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Manansang, J. D. Siswomartono, T. Soejarto, U.S. Seal, P.S. Miller, and S. Ellis (eds.). 1997. Marine Turtles of 
Indonesia: Population Viability and Conservation Assessment and Management Workshop. Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Marmontel, M., S. R. Humphrey and T. J. O'Shea. 1997. Population viability analysis of the Florida manatee 
(Trichechus manatus latirostris), 1976-1991. Conservation Biology 11(2):467-481. 
Marshall, K. and G. Edwards-Jones. 1998. Reintroducing capercaillie (Tetrao urogallus) into southern Scotland: 
Identification of minimum viable populations at potential release sites. Biodiversity & Conservation 7(3):275-
296. 
Matamoros, Y., G. Wong, and U.S. Seal (eds.). 1996. Population and Habitat Viability Assessment Workshop for 
Saimiri oerstedi citrinellus. Final Report. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 


 
VORTEX Version 9.50 User’s Manual 
 
145 
Appendix III 
VORTEX Bibliography 
Mathews, F. and D.W. Macdonald. 2001. The sustainability of the common crane (Grus grus) flock breeding in 
Norfolk: Insights from simulation modeling. Biological Conservation 100(3):323-333. 
McCann, K., A. Burke, L. Rodwell, M.Steinacker and U. S. Seal  (eds.). 2000. Population and Habitat Viability 
Assessment for the Wattled Crane (Bugeranus carunculatus) in South Africa. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
McCann, K., K. Morrison, A. Byers, P. Miller and Y. Friedmann  (eds.). 2001. Blue Crane (Anthropoides 
paradiseus): A Population and Habitat Viability Assessment Workshop. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Miller, P.S. 1996. Impacts of the Hawaiian longline fishery on the Pacific Ocean population of loggerhead turtles 
(Caretta caretta): An analysis using the VORTEX simulation modelling package. Pages 105-132 in: Bolten, A.B., 
J.A. Wetherall, G.H. Balazs, and S.G. Pooley (eds.). Status of Marine Turtles in the Pacific Ocean Relevant to 
Incidental Take in the Hawaii-Based Pelagic Longline Fishery. U.S. Department of Commerce, NOAA 
Technical Memorandum, NOAA-TM-NMFS-SWFCS-230, 167 p.  
Miller, P. S. and R. C. Lacy. 1999. VORTEX Version 8 users manual. A stochastic simulation of the simulation 
process. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Miller, P.S., and R.C. Lacy.  2003a. Integrating the human dimension into endangered species risk assessment. 
Pages 41-63 in: F.R. Westley and P.S. Miller, eds. Experiments in Consilience: Integrating Social and Scientific 
Responses to Save Endangered Species. Island Press, Washington, DC. 
Miller, P.S., and R.C. Lacy.  2003b. Metamodels as a tool for risk assessment. Pages 333-351 in: F.R. Westley and  
P.S. Miller, eds. Experiments in Consilience: Integrating Social and Scientific Responses to Save Endangered 
Species. Island Press, Washington, DC. 
Mills, L.S., S.G. Hayes, C. Baldwin, M.J. Wisdom, J. Citta, D.J. Mattson, and K. Murphy. 1996. Factors leading to 
different viability predictions for a grizzly bear data set. Conservation Biology 10:863-873. 
Mills, M.G.L, S. Ellis, R. Woodroffe, A. Maddock, P. Stander, A. Pole, G. Rasmussen, P. Fletcher, M. Bruford, D. 
Wildt, D. Macdonald, and U.S. Seal (eds.). 1998. Population and Habitat Viability Assessment for the African 
Wild Dog (Lycaon pictus) in Southern Africa. Final Workshop Report. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Mirande, C., R. Lacy, and U. Seal (eds.). 1991. Whooping Crane (Grus americana) Conservation Viability 
Assessment Workshop Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Molur, S., R. Sukumar, and S. Walker (eds.). 1995. Great Indian One-Horned Rhinoceros Population and Habitat 
Viability Assessment Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Novellie, P.A., P.S. Miller, and P.H. Lloyd. 1996. The use of VORTEX simulation models in a long-term programme 
of re-introduction of an endangered large mammal, the Cape mountain zebra (Equus zebra zebra). Acta 
Œcologica 17:657-671. 
Odum, A., et al (eds.). 1993. Aruba Island Rattlesnake Population and Habitat Viability Assessment (PHVA) 
Workshop. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Ounsted, M., K. Soemarna, W. Ramono, U.S. Seal, A. Green, Rudyanto, and R. Ounsted (eds.). 1994. The White-
Winged Wood Duck in Sumatra: Population and Habitat Viability Analysis Report. Apple Valley, MN: Captive 
Breeding Specialist Group (SSC/IUCN). 
Paolo, C., and L. Boitani. 1991. Viability assessment of the Italian wolf and guidelines for the management of the 
wild and a captive population. (In Italian). Ricerche de Biologia della Selvaggina 89:1-58. 
Parysow, P. and D.J. Tazik. 2002. Assessing the effect of estimation error on population viability analysis: an 
example using the black-capped vireo. Ecological Modelling 155(2-3):217-229. 
Pergams, O.R.W. 1998. Genetic, morphological, and population viability analysis of California Channel Island deer 
mice. M.Sc. thesis, University of Illinois at Chicago. 


VORTEX Version 9.50 User’s Manual 
146 Appendix III 
VORTEX Bibliography 
Phillips, M., N. Fascione, P.Miller and O. Byers (eds.). 2000. Wolves in the Southern Rockies: A Population and 
Habitat Viability Assessment: Final Report. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Pinder, L., and U.S. Seal (eds.). 1994. Population and Habitat Viability Assessment Report for Cervo-do-Pantanal 
(Blastocerus dichotomus). Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Plissner, J.H. and S.M. Haig. 2000. Viability of piping plover Charadrius melodus metapopulations. Biological 
Conservation 92(2):163-173. 
Portales, G.L., P. Reyes, H. Rangel, A. Velazquez, P.S. Miller, S. Ellis, and A.T. Smith (eds.). 1997. Taller 
Internacional para la Conservación de los Lagomorfos Mexicanos en Peligro de Extinción. Reporte del Taller. 
Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Pucek, Z., I. Udina, U.S. Seal, and P.S. Miller (eds.). 1996. Population and Habitat Viability Assessment for the 
European Bison (Bison bonasus). Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Rao, R.J., D. Basu, S.M. Hasan, S. Molur, and S. Walker (eds.). 1995. Indian Gharial Population and Habitat 
Viability Assessment Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Reed, D.H., J.J. O’Grady, B.W. Brook, J.D. Ballou, and R. Frankham. 2003. Estimates of minimum viable 
population sizes for vertebrates and factors influencing those estimates. Biological Conservation 113:23-34. 
Rodríguez, J.P., and F. Rojas-Suárez. 1994. Population viability analysis of three populations of insular psitacids of 
Venezuela. Pages 97-113 in: Morales, G., I. Novo, D. Bigio, A. Luy, and F. Rojas-Suárez (eds.). Biologia y 
Conservacion de los Psitacidos de Venezuela. Caracas: SCAV, EBAFY, Econatura, SCAPNHP and Provita. 
Rodríguez-Luna, E., L. Cortés Ortiz, P.S. Miller, and S. Ellis (eds.). 1996. Population and Habitat Viability 
Assessment for the Mantled Howler Monkey (Alouatta palliata mexicana). Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Rylands, A., K. Strier, R. Mittermeier, J. Borovansky, and U.S. Seal (eds.). 1998. Population and Habitat Viability 
Assessment Workshop for the Muriqui (Brachyteles arachnoides). Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1992a. Bali Starling Population Viability Assessment Report. Apple Valley, MN: Captive Breeding 
Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1992b. Black-Footed Ferret Recovery Plan Review. Apple Valley, MN: Captive Breeding Specialist 
Group (SSC/IUCN). 
Seal, U.S. (ed.). 1992c. Genetic Management Strategies and Population Viability of the Florida Panther (Felis 
concolor coryi). Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1994a. Attwater’s Prairie Chicken Population and Habitat Viability Assessment. Apple Valley, 
MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1994b. Houston Toad Population and Habitat Viability Assessment Report. Apple Valley, MN: 
Conservation Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1994c. Population and Habitat Viability Assessment for the Greek Population of the Mediterranean 
Monk Seal (Monachus monachus). Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. (ed.). 1996. Kirtland’s Warbler (Dendroica kirtlandii) Population and Habitat Viability Assessment 
Workshop Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., J.D. Ballou and C.V. Padua (eds.). 1990. Leontopithecus Population Viability Analysis Workshop Report. 
Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., and M.W. Bruford (eds.). 1991. Pink Pigeon (Columba [Nesoenas] mayeri) Conservation Viability 
Assessment Workshop. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., and T. Foose (eds.). 1989. Javan Rhinoceros Population Viability Analysis. Apple Valley, MN: Captive 
Breeding Specialist Group (SSC/IUCN). 


 
VORTEX Version 9.50 User’s Manual 
 
147 
Appendix III 
VORTEX Bibliography 
Seal, U.S., P. Garland, D. Butler, A. Grant, and C. O’Donnell (eds.). 1993. Population Viability Analysis for the Kea 
(Nestor notabilis) and Kaka (Nestor meridionalis). Apple Valley, MN: Captive Breeding Specialist Group 
(SSC/IUCN). 
Seal, U.S., and S. Hereford (eds.). 1992. Mississippi Sandhill Crane Population and Habitat Viability Assessment 
Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. and R.C. Lacy (eds.). 1989. Florida Panther Population Viability Analysis. Report to the U.S. Fish and 
Wildlife Service. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S. and R.C. Lacy. 1990. Florida Key Deer (Odocoileus virginianus clavium) Population Viability 
Assessment. Report to the U.S. Fish and Wildlife Service. Apple Valley, MN: Captive Breeding Specialist 
Group (SSC/IUCN). 
Seal, U.S., R.C. Lacy, K. Medley, R. Seal and T.J. Foose (eds.). 1991. Tana River Primate Reserve Conservation 
Assessment Workshop Report. Apple Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., J. Manansang, D. Siswomartono, T. Suhartono, J. Sugarjito (eds.). 1996. Komodo Monitor (Varanus 
komodoensis) Population and Habitat Viability Assessment Workshop Report. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Seal, U.S., S. Walker, and S. Molur (eds.). 1995. Barasingha Population and Habitat Viability Assessment Report. 
Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Sillero-Zubiri, C., J. Malcolm, S. Williams, J. Marino, Z. Tefera, K. Laurenson, D. Gottelli, A. Hood, D. 
Macdonald, D. Wildt, and S. Ellis. 2000. Ethiopian Wolf Conservation Strategy Workshop: Final Report. Apple 
Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Soberon, R., P. Ross and U.S. Seal (eds.). 2000. Cocodrilo Cubano Análisis de la Viabilidad de la Población y del 
Hábitat: Borrador del Informe. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Soemarna, K., R. Tilson, W. Ramono, D.W. Sinaga, R. Sukumar, T.J. Foose, K. Traylor-Holzer, and U.S. Seal 
(eds.). 1994. The Sumatran Rhino in Indonesia: Population and Habitat Viability Analysis Report. Apple 
Valley, MN: Captive Breeding Specialist Group (SSC/IUCN). 
Somers, M.J. 1997. The sustainability of harvesting a warthog population: Assessment of management opinions 
using simulation modelling. South African Journal of Wildlife Research 27(2):37-43.  
Sommer, S., A.T. Volahy, and U.S. Seal. 2002. A population and habitat viability assessment for the highly 
endangered giant jumping rat (Hypogeomys antimena), the largest extant endemic rodent of Madagascar. 
Animal Conservation 5(4):263-273. 
Song, Y.L. 1996. Population viability analysis for two isolated populations of Haianan Eld’s deer. Conservation 
Biology 10:1467-1472. 
South, A.B., S.P. Rushton, and D.W. Macdonald. 2000. Simulating the proposed reintroduction of the European 
beaver Castor fiber to Scotland. Biological Conservation 93:103-116.. 
Strier, K. B. 2000. Population viabilities and conservation implications for muriquis (Brachyteles arachnoides) in 
Brazil's Atlantic Forest. Biotropica 32(4B):903-913. 
Supriatna, J., R. Tilson, K. Gurmaya, J. Manansang, W. Wardojo, A. Sriyanto, A. Teare, K. Castle, and U.S. Seal 
(eds.). 1994. Javan Gibbon and Javan Langur Population and Habitat Viability Analysis Report. Apple Valley, 
MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Taylor, B.L., P.R. Wade, U. Ramakrishnan, M. Gilpin, and H.R. Akçakaya. 2002. Incorporating uncertainty in 
population viability analyses for the purpose of classifying species by risk. Pages 239-252 in: Beissinger, S.R. 
and D.R. McCullough (eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Tilson, R., U.S. Seal, K. Soemarna, W. Ramono, E. Sumardja, S. Poniran, C. van Schaik, M. Leighton, H. Rijksen, 
and A. Eudey (eds.). 1993. Orang utan Population and Habitat Viability Analysis Report. Apple Valley, MN: 
Captive Breeding Specialist Group (SSC/IUCN). 


VORTEX Version 9.50 User’s Manual 
148 Appendix III 
VORTEX Bibliography 
Tilson, R., K. Soemarna, W. Ramono, S. Lusli, K. Traylor-Holzer, and U.S. Seal (eds.). 1992. Sumatran Tiger 
Population and Habitat Viability Analysis Report. Apple Valley, MN: Captive Breeding Specialist Group 
(SSC/IUCN). 
Tilson, R., K. Soemarna, W. Ramono, R. Sukumar, U.S. Seal, K. Traylor-Holzer, and C. Santiapillai (eds.). 1994. 
The Asian Elephant in Sumatra: Population and Habitat Viability Analysis Report. Apple Valley, MN: Captive 
Breeding Specialist Group (SSC/IUCN). 
Tunhikorn, S., W. Brockelman, R. Tilson, U. Nimmanheminda, P. Ratankorn, R. Cook, A. Teare, K. Castle, and 
U.S. Seal (eds.). 1994. Population and Habitat Viability Analysis Report for Thai Gibbons: Hylobates lar and 
H. pileatus. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Wade, P.R. 2002. Bayesian population viability analysis. Pages 213-238 in: Beissinger, S.R. and D.R. McCullough 
(eds.). Population Viability Analysis. Chicago, IL: University of Chicago Press. 
Walker, S. (ed.). 1994. Manipur Brow-Antlered Deer (Sangai) Population and Habitat Viability Assessment. Apple 
Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Walker, S. and S. Molur (eds.). 1994. Population and Habitat Viability Analysis (PHVA) Workshop for 
Indian/Nepali Rhinoceros. Zoo Outreach Organisation/CBSG India, Coimbatore. 
Wang, Y., S.-W. Chu, and U.S. Seal (eds.). 1994. Population and Habitat Viability Assessment Workshop Report for 
the Asiatic Black Bear (Ursus thibetanus formosanus). Apple Valley, MN: Conservation Breeding Specialist 
Group (SSC/IUCN). 
Wang, Y., S.-W. Chu, D. Wildt, and U.S. Seal (eds.). 1995. Clouded Leopard (Neofelis nebulosa brachyurus) 
Population and Habitat Viability Assessment. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Wei, F., Feng, Z. and Hu, J. 1997. Population viability analysis computer model of giant panda population in 
Wuyipeng, Wolong Natural Reserve, China. International Conference on Bear Research and Management 
9(2):19-23. 
Wemmer, C., A. Than, S.T. Khaing, S. Monfort, T. Allendorf, J. Ballou, and S. Ellis. 2000. Thamin Population and 
Habitat Viability Assessment: Final Report. Apple Valley, MN: Conservation Breeding Specialist Group 
(SSC/IUCN). 
Werikhe, S., L. Macfie, N. Rosen, and P.S. Miller (eds.). 1998. Can the Mountain Gorilla Survive? Population and 
Habitat Viability Assessment Workshop for Gorilla gorilla beringei. Apple Valley, MN: Conservation Breeding 
Specialist Group (SSC/IUCN). 
Whittington, P., R.J.M. Crawford, O. Huyser, D. Oschadleus, R. Randall, P. Ryan, L. Shannon, A. Woolfardt, J. 
Cooper, R. Lacy, and S. Ellis (eds.). 2000. African Penguin Population and Habitat Viability Assessment. Final 
Report. Apple Valley, MN: Conservation Breeding Specialist Group (SSC/IUCN). 
Wilson, M.H., C.B. Kepler, N.F.R. Synder, S.R. Derrickson, F.J. Dein, J.W. Wiley, J.M. Wunderle, A.E. Lugo, D.L. 
Graham, and W.D. Toone. 1994. Puerto Rican parrots and potential limitations of the metapopulation approach 
to species conservation. Conservation Biology 8:114-123. 
Xu, H., and H. Lu. 1996. A preliminary analysis of population viability for Chinese water deer (Hydropotes inermis) 
lived in Yancheng. (In Chinese). Acta Theriologica Sinica 16:81-88. 
Yuan, S.D., G. Yazhen, L. Xiaoping, Q. Yang, J. Sale, C. Kirkpatrick, J. Ballou, and U.S. Seal (eds.). 1999. CBSG 
Guizhou Snub-nosed Monkey Conservation and PHVA Workshop Report. Apple Valley, MN: Conservation 
Breeding Specialist Group (SSC/IUCN). 
Zhang, X., D. Wang, and K. Wang. 1994. The VORTEX model and its application on the management of the Chinese 
River Dolphin (Lipotes vexillifer) population. Chinese Biodiversity 2:133-139. 
 


 
VORTEX Version 9.50 User’s Manual 
 
149 
Appendix IV 
Reprints 
Appendix 
 
 
 
Reprints 
 
 
 
 
 
 
Lacy, R.C. 2000. Structure of the VORTEX simulation model for 
population viability analysis. Ecological Bulletins 48:191-203. 
(Reprinted with permission of the publisher.) 
 
Lacy, R.C. 2000. Considering threats to the viability of small 
populations using individual-based models. Ecological Bulletins 
48:39-51. 
(Reprinted with permission of the publisher.) 
 
IV
