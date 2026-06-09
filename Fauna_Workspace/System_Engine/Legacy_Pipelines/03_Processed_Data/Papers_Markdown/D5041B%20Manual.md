--- 
source: D5041B%20Manual.pdf
--- 

DCC MODEL D5041B
(PRO GRAM FOR PULSE-CODED TAGS)
USER’S MAN UAL


Ta ble of Con tents
IN TRO DUC TION
1
How to use this man ual
1
What is the DCC II and how does it work?
1
Data col lec tion pro ce dures
3
SYS TEM DE SCRIP TION
4
Ae rial track ing
4
Sta tion ary data log ging
5
PRE PARING YOUR EQUIP MENT TO LOG DATA
5
Re ceiver con nec tions
6
DCC II con nec tions
7
HANDAR 540A con nec tions
8
CON TROLS
9
DCC II USER’S IN TER FACE
13
DCC II key board
13
In ter acting with the DCC II
15
GETTING THE DCC II STARTED
16
How to start the sys tem
16
Se lecting a pro gram
17
AE RIAL TRACKING
17
En tering fre quen cies
18
Set ting pro gram vari ables
19


Scanning fre quen cies
20
The scan ta ble
21
Scanning op tions
22
Changing pro gram vari ables
26
Re setting the DCC II’s time
26
STA TION ARY DATA LOGGING
27
Set ting Pro gram Vari ables
27
En tering Fre quencies
30
Logging the data
31
Data log ging op tions
32
Holding on a fre quency
35
How to Exit Logging
36
Viewing the DCC II’s data
36
Ae rial data
38
Sta tion ary data
39
GETTING YOUR DATA OUT OF THE DCC II
39
Offloading data us ing an IBM-compatible PC
40
Offloading data us ing a Macintosh PC
44
Ex pla na tion of outputted data
46
CHARGING THE BAT TERIES
48
POWER CON SID ER ATIONS
49
TIPS AND TECH NIQUES
50
Test pro ce dures
50


How to con serve data file space
52
How to con serve power
52
AP PEN DIX A - WAR RANTY
53
AP PEN DIX B - TUNING TRANS MIT TERS
54
AP PEN DIX C - AD JUSTING THE THRESH OLD CON TROL
55
AP PEN DIX D - DE SCRIP TION OF KEYS
56
Keys used in ae rial track ing
57
Keys used in sta tion ary data log ging
60
AP PEN DIX E - QUES TIONS
63
AP PEN DIX F - DCC II SPEC I FI CA TIONS
64
AP PEN DIX G - JULIAN DATE CAL EN DARS
65


IN TRO DUC TION
How to use this man ual
Wel come to log ging data with the ATS Data Col lec tion Com puter (DCC). We
wish you much suc cess with your field work.
Now a word about this man ual. Through out this man ual, the sym bol n sig ni fies
nu meric in put by the user of the DCC. One n means only one digit can be en tered. 
A se ries of n‘s in di cates the num ber of dig its al lowed for the vari able. For
ex am ple, nnn means up to three dig its can be en tered.
We urge you to read the en tire man ual be cause we feel all the in for ma tion is
im por tant.
If you have any ques tions about in for ma tion in the man ual, con tact ATS. We
value your feed back on our data col lec tion sys tem. Your ideas en able us to
con tin u ally im prove our prod ucts.
What is the DCC and how does it work?
Ad vanced Te lem e try Sys tems (ATS) has a data col lec tion sys tem spe cif i cally
de signed for use with pulse-coded trans mit ters. Or i ginally, it was de signed for
track ing the move ments of Salmon. This data col lec tion sys tem can be used for
ae rial track ing or sta tion ary data log ging. To en sure that no fish is missed, the
sys tem has the ca pa bil ity of mon i tor ing 400 fish within a time span of 10 min utes. 
Each fre quency chan nel con tains 10 trans mit ters. Each trans mit ter has a unique
pulse-coded pat tern. Soft ware iden ti fies the in di vid ual trans mit ters by their
pat tern dur ing ae rial track ing and by both their pat tern and their pe riod dur ing
sta tion ary data log ging.
page 1
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)
Figure 1 - Pattern of a pulse-coded transmitter


The trans mit ter’s sig nal has a pat tern of one wide pulse fol lowed by two nar row
pulses. The ID (iden ti fi ca tion) code is de pend ent on the spac ing of these pulses.
Fig ure 1 il lus trates the sig nal pat tern of a pulse-coded tag. In this fig ure, the id
code of the trans mit ter is 15. For a de tailed de scrip tion of id codes, re fer to the
“Ex pla na tion of outputted data” sec tion.
If trans mit ters are equipped with the mor tal ity op tion, the sig nal pat tern changes
to one wide pulse fol lowed by three nar row pulses. Fig ure 2 il lus trates the pat tern
of a pulse-coded tag in mor tal ity.
In ae rial track ing, tagged fish are lo cated as they tra verse the river by us ing the
sys tem from an air plane. The user con structs fre quency ta bles to be scanned; then
presses the ID (iden ti fi ca tion) key to iden tify the trans mit ters. The data is
au to mat i cally stored when a trans mit ter is iden ti fied. Data stored con sists of the
date and time that the fish was iden ti fied and the fre quency and id code of the
fish’s trans mit ter.
In sta tion ary data log ging, the fish are mon i tored along the river by a num ber of
stra te gi cally placed data sta tions. As the fish pass the data sta tion, they are
iden ti fied and the data is au to mat i cally stored. Data con sists of the date and time
when a fish reg is tered as pres ent, the an tenna num ber and the iden tity of the fish.
The iden tity of the fish in cludes the fre quency and id code of the fish’s trans mit ter 
and also the pe riod mea sure ment of the trans mit ter’s sig nal. Then, once each hour 
the data is trans ferred to a Data Col lec tion Plat form (DCP) for trans mis sion to the
GOES Sat el lite ev ery three hours. Ideally, the data sta tions can re main un at tended 
in the field for an ex tended pe riod of time.
The main dif fer ence be tween the ae rial and sta tion ary sys tems is the iden ti fy ing
func tion. Be cause no hu man user is pres ent dur ing sta tion ary data log ging to
make judg ment calls on the in com ing data, the sta tion ary pro gram uses stricter
cri te ria for ac cept ing a trans mit ter as iden ti fied. 
The DCC is sup plied with ROM-based soft ware writ ten in C lan guage that is
pres ent upon power-up.
page 2
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 2 - Mor tal ity sig nal of a pulse-coded trans mit ter


The DCC’s soft ware is flex i ble and easy to use. There are sev eral pa ram e ters that
you can pro gram ac cord ing to the needs of your spe cific study. Data  offloaded
from the DCC II can be im ported di rectly into most data base and spread sheet
pack ages.
Data col lec tion pro ce dures
The DCC must be pro grammed to con trol the re ceiver’s op er a tion. The DCC
sends each fre quency to be mon i tored to the re ceiver for a spec i fied amount of
time. The re ceiver’s tone de coder col lects any sig nals com ing in on the fre quency
and sends them to the DCC.
This sys tem is spe cif i cally de signed for use with pulse-coded trans mit ters. It can
be used for ae rial track ing or sta tion ary data log ging.
With ae rial track ing, you have many op tions avail able while iden ti fy ing or
hold ing on a fre quency. You can tune the fre quency up or down, move up or
down a chan nel, add and de lete fre quen cies, and merge a fre quency ta ble into the
ta ble you are scan ning.
With sta tion ary log ging, you have a choice of log ging con tin u ously or with a log
or store in ter val. And, more than one an tenna can be used if you have a
multi plexer.
The DCC’s data file is a bat tery-backed stor age area where data is held for
re trieval at a later time. The data stored de pends on whether you are do ing ae rial
track ing or sta tion ary data log ging. In ae rial track ing, the data stored in cludes the
date and time, fre quency, and id code re ceived when the DCC reg is ters an an i mal
as pres ent. In sta tion ary data log ging, the data stored in cludes the date and time,
an tenna num ber, fre quency, id code and pe riod of the in com ing trans mit ter sig nal. 
The DCC uses 10 bytes of data file mem ory to store data. These 10 bytes are
con sid ered to be one block of data. The DCC is ca pa ble of stor ing 320,240 bytes
or 32,024 blocks of data.
To elim i nate the pos si ble loss of data due to power source fail ure, the DCC has
bat tery-backed mem ory for up to 10 years.
page 3
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


SYS TEM DE SCRIP TION
Ae rial track ing
For ae rial track ing, the sys tem con sists of an ATS model D5041 Data Col lec tion
Com puter (DCC), an ATS model R4000 Chal lenger re ceiver and an an tenna.
page 4
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 3 - Sta tion ary Data Logging Sys tem


Sta tion ary data log ging
For sta tion ary data log ging, the sys tem con sists of an ATS model D5041 Data
Col lec tion Com puter (DCC), an ATS model R4000 Chal lenger re ceiver, a Data
Col lec tion Plat form (DCP), an an tenna and ex ter nal power sources for the
re ceiver and DCP.
PRE PARING YOUR EQUIP MENT TO LOG DATA
This three part sec tion de scribes the phys i cal con nec tions nec es sary to set up the
sys tem for data log ging. The DCC con nects to the re ceiver to log data.
page 5
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)
Fig ure 4 - Re ceiver with ex ter nal power source con nected


Re ceiver con nec tions
1. Con nect an ex ter nal power source to the re ceiver. Fig ure 4 dem on strates the
con nec tion of ex ter nal power to the re ceiver. Using the ex ter nal power cord, plug
the end with the round con nec tor into the re ceiver’s CHG EXT PWR jack. The
op po site end has two al li ga tor clips which at tach to the ter mi nals of the ex ter nal
power source. At tach the clip on the red wire to the pos i tive ter mi nal and the clip
on the black wire to the neg a tive ter mi nal.
NOTE: Hav ing ex ter nal power con nected to the re ceiver will not re charge the
re ceiver’s in ter nal bat ter ies. To re charge the re ceiver’s in ter nal bat ter ies, plug
the bat tery charger ATS sup plied into the re ceiver’s CHG EXT PWR jack
when the re ceiver is not op er at ing.
2. Con nect the an tenna to the re ceiver.
page 6
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 5 - Re ceiver with an tenna con nected


Fig ure 5 dem on strates this con nec tion. Using a co ax ial ca ble, con nect the
an tenna to the re ceiver’s ANT (an tenna) jack.
The re ceiver uses an an tenna to col lect the trans mit ter sig nals. With a multi plexer, 
up to four an ten nas can be used. Using a co ax ial ca ble, con nect one end to the
multi plexer’s RE CEIVER jack and the other end to the re ceiver’s ANT jack.
Then, us ing more co ax ial ca bles, con nect the an ten nas to the multi plexer’s
an tenna jacks num bered 1, 2, 3, and 4. If only two an ten nas are used, con nect the
an ten nas to the multi plexer’s an tenna jacks num bered 1 and 2. If three an ten nas
are used, con nect the an ten nas to the multi plexer’s an tenna jacks num bered 1, 2,
and 3. When us ing a sys tem with four an ten nas, the po si tion of the an tenna
be comes im por tant. The four an tenna sys tem is used for di rec tional log ging. Each
an tenna is po si tioned to point in a par tic u lar di rec tion (north, south, east, west).
Re mem ber, you have to keep track of which di rec tion cor re sponds with which
an tenna num ber for in ter pret ing your data.
DCC con nec tions
1. Con nect the DCC to the re ceiver.
Fig ure 6 dem on strates the con nec tion. ATS sup plies the ap pro pri ate rib bon
ca ble. Plug one end into the DCC’s TO REC con nec tor. Plug the other end
into the re ceiver’s TO DCC con nec tor. Most ATS model R4000 re ceiv ers
and all model R8000 re ceiv ers have the same con nec tor as the DCC.
There fore, you can place ei ther end of the rib bon ca ble on the re ceiver. 
2. Con nect the DCC to the multi plexer (op tional).
ATS sup plies a ca ble with a 15-pin con nec tor on one end and a 9-pin
con nec tor on the other end. Place the end of the ca ble with 15 pins on the
DCC’s AUX PORT con nec tor. Place the other end of the ca ble with 9 pins on
the multi plexer’s TO DCC con nec tor.
3. Con nect the DCC to a Handar 540A Data Col lec tion Plat form (op tional).
For sta tion ary data log ging, the DCC is con nected to a Handar 540A Data
Col lec tion Plat form (DCP) which trans mits to the GOES Sat el lite. The ca ble
plugs into the the DCC’s DCP con nec tor and into the DCP’s PRO GRAM I/O
con nec tor. 
page 7
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


HANDAR 540A con nec tions
With sta tion ary data log ging, this sys tem can be used with a Handar 540A Data
Col lec tion Plat form (DCP). The DCC trans fers data to the DCP ev ery hour. The
DCP then trans mits the data to the GOES Sat el lite once ev ery three hours.
1. Con nect a so lar panel to the DCP.
The so lar panel con nects to the DCP’s SOLAR PANEL/BATT CHARGER
con nec tor. 
page 8
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 6 - DCC con nected to re ceiver


Con necting a so lar panel to the DCP al lows the DCP’s in ter nal bat ter ies to be
re charged when the so lar panel re ceives ad e quate sun light. 
2. Con nect the DCC to the DCP.
Using the ca ble ATS pro vided, con nect one end to the DCC’s AUX PORT
and the other end into the DCP’s PRO GRAM I/O con nec tor.
CON TROLS
This sec tion ex plains the DCC and re ceiver con trols that per tain to data log ging.
Re ceiver con trols used dur ing man ual re ceiver op er a tion are not dis cussed here. If 
you are al ready fa mil iar with the con trols, a list is pro vided be low to tell you what 
po si tion the con trols should be in dur ing data log ging. If you are not fa mil iar with
the con trols, pro ceed to the next sec tion for a de tailed ex pla na tion. 
DCC CON TROLS:
1. Set EXT TERM/LO CAL switch to “LO CAL”.
2. Set POWER switch to “ON”.
3. Leave BACK LIGHT switch “OFF” (for un at tended field stays).
RE CEIVER CON TROLS:
1. Set ON-OFF switch to “ON”.
2. Turn AU DIO “OFF”.
3. Turn RF GAIN fully “ON”.
4. Ad just tone thresh old control for the amount of noise in the en vi ron ment
(see Appendix C).
5. Set INT/AU DIO_ON/FREQ switch to “FREQ”.
page 9
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


Re ceiver con trols
The fol low ing ex plains which re ceiver con trols to use when the re ceiver is
con nected to the DCC. Fig ure 7 points to their lo ca tion on the re ceiver’s face.
•
ON-OFF Switch
This switch turns power on and off (whether in ter nal bat ter ies or an ex ter nal
source sup plies power to the sys tem). The ON-OFF switch is a lock ing tog gle 
switch that must be pulled up be fore mov ing to the de sired po si tion. The
ON-OFF switch should be placed in the ON po si tion while op er at ing.
•
AU DIO Con trol
This con trol ad justs the au dio level of the speaker or head set.
page 10
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 7 - Re ceiver face


NOTE: DURING DATA LOGGING, THE RE CEIVER’S AU DIO
CON TROL SHOULD BE OFF.
The au dio con trol is off when it is fully turned coun ter clock wise. When the
au dio is on, the tone de coder (which de tects the pulses) does not func tion.
Your data log ging sys tem will re ceive the clean est sig nal when us ing the tone 
de coder.
•
RF GAIN Con trol
The Ra dio Fre quency (RF) Gain con trol var ies the gain of the in ter me di ate
fre quency (IF) am pli fi ers. It var ies the sen si tiv ity of the re ceiver and keeps
the re ceiver from over load ing. Dur ing data log ging, the RF Gain con trol
should be turned clock wise as far as pos si ble. This sets the gain at max i mum.
•
TONE DE CODER THRESH OLD CON TROL
This con trol ad justs the thresh old of the tone de coder. It should be ad justed
when op er at ing con di tions are ei ther very noisy or very quiet. See
AP PEN DIX C for more in for ma tion on ad just ing the thresh old con trol.
•
INT/AU DIO_ON/FREQ Con trol
This con trol should al ways be in the FREQ po si tion when us ing the re ceiver
with a DCC. 
DCC con trols
There are four tog gle switches on the DCC. Fig ure 8 points to their lo ca tion on
the DCC’s face plate.
NOTE: Some of the tog gle switches are lock ing tog gle switches. They must be
pulled up be fore they can be moved to a new po si tion.
•
EXT TERM/LO CAL Switch
Upon power-up of the DCC, this switch MUST be in the LO CAL po si tion. If
the DCC is pow ered up with this switch in the EXT TERM (ex ter nal
ter mi nal) po si tion, turn the DCC off, move the switch to the LO CAL
po si tion, and then turn the DCC on again. This switch should only be in the
EXT TERM po si tion when offloading data to a PC.
page 11
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


•
Power Switch
In the OFF po si tion, the DCC is OFF. Be fore mov ing the switch to the ON
po si tion, the EXT TERM/LO CAL switch must be in the LO CAL po si tion to
prop erly ini tial ize the dis play. When the switch is moved to the ON po si tion,
the soft ware is pres ent (loaded and run ning). The soft ware ver sion is
dis played mo men tarily. Then, the cur rent time is dis played fol lowed by
“Press key....._”. 
•
REC/COMP Switch
This is a mo men tary con tact switch. It re mains in the COMP (com puter)
po si tion un less it is man u ally held in the REC (re ceiver) po si tion. While the
switch is in the COMP po si tion, the DCC has con trol of the re ceiver’s
fre quency se lec tion. With the switch in the REC po si tion, the user can
man u ally con trol the fre quency with the re ceiver di als (along the bot tom of
page 12
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 8 - DCC face


the re ceiver’s face plate). This switch al lows the user to trans fer fre quency
con trol to the re ceiver with out dis con nect ing the DCC.
CAU TION: Be care ful when us ing the REC/COMP switch while log ging data in 
the field. If con trol has been given to the re ceiver and you tune to a fre quency
where a fish is pres ent, that pres ence is re corded on the wrong chan nel. This is
be cause the DCC sent out one fre quency but you in ter ceded and gave it an other
fre quency. If you are log ging valid data, dis con tinue log ging be fore us ing the
REC/COMP switch.
•
Back Light switch
This switch turns the light ing of the DCC’s screen on and off. Be care ful to
use back light ing only when nec es sary be cause it con sumes a lot of power.
NOTE: The re ceiver must be con nected to the DCC to use the back light ing.
DCC USER’S IN TER FACE
DCC key board
Fig ure 9 dis plays the DCC’s key board. To ac cess com mands lo cated on the top
half of the key, first press and re lease the SHIFT key. Then, press and re lease the
de sired key.
NOTE: The SHIFT key does not func tion like the shift key on a type writer or
com puter, where the shift key is held down while a sec ond key is pressed. 
Since the sys tem has two main func tions - ae rial track ing and sta tion ary data
log ging - the key board is di vided into two menus. The ae rial menu is for ae rial
track ing and the sta tion ary menu is for sta tion ary data log ging. This pre vents the
user from con fus ing func tion keys for ae rial track ing with func tion keys for
sta tion ary data log ging. How ever, some of the func tion keys un der the ae rial
menu can be used in sta tion ary data log ging as well. Pressing a key that has no
sig nif i cance in the pres ent menu re sults in “NOT AN OP TION” be ing dis played
on the DCC’s screen. 
Upon power-up, the DCC’s pro gram is in nei ther the ae rial menu nor the
sta tion ary menu. In this man ual, we re fer to this stage as the main menu. 
page 13
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


From the main menu, the fol low ing ae rial menu keys are ac ces si ble: TIME,
FREQ, SETUP, and SCAN. Then, af ter press ing the SCAN key, the rest of the
keys in the ae rial menu be come ac ces si ble. 
To en ter the sta tion ary menu from the main menu, you must first press the
SETUP key lo cated in the sta tion ary menu be fore the rest of the keys in the
sta tion ary menu be come ac ces si ble.
While in the sta tion ary menu, the DCC’s screen dis plays “STA TION ARY Press
key....._” (on two lines) when ever the func tion of a key in the sta tion ary menu is
com pleted. 
To exit from the sta tion ary menu, it is nec es sary to press the ESC key. Af ter
ex it ing the sta tion ary menu, the DCC’s screen dis plays “Press key....._”. Now, the 
pro gram is back at its main menu.
page 14
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 9 - DCC key board


From the main menu, you can also ac cess the keys that are not con tained in ei ther
the ae rial menu or the sta tion ary menu. These keys are the VIEWD key, the TEST 
key and the spe cial func tion keys - F1, F2, and F3.
Fig ure 10 shows the flowchart of the DCC’s pro gram. As you can see, press ing
the SETUP key in the sta tion ary menu al lows ac cess to the rest of the keys in the
sta tion ary menu as stated ear lier. Pressing the ID key while in the sta tion ary menu 
would re sult in “NOT AN OP TION” be ing dis played on the DCC’s screen
be cause the ID key is not in the sta tion ary menu’s do main.
In ter acting with the DCC
In many in stances, you will be en ter ing num bers into the DCC. Ex am ples in clude
en ter ing the date and time, scan time, etc. A few keys fa cil i tate this pro cess. The
fol low ing dis cusses these key func tions as they per tain to en ter ing num bers.
page 15
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)
Fig ure 10 - DCC pro gram flowchart


•
ENTER key:
Af ter typ ing num bers, press the ENTER key for the DCC to ac cept the
num bers. If no num bers are typed be fore the ENTER key is pressed, the DCC
ac cepts the cur rent value of the pa ram e ter that is dis played on the DCC’s
screen.
•
← key:
If an er ror is made while typ ing a num ber, press the ← (Back space) key to
move the cur sor back and cor rect the num ber. The ← key must be pressed
be fore the ENTER key. For ex am ple, if you wanted to set the scan time to 10
sec onds but typed 11 in stead, press the ← key once to cor rect the scan time.
Do not hold the back space key down. If you need to move the cur sor back
more than one space, press and re lease the ← key re peat edly.
•
ESC key:
Pressing the ESC key al lows you to exit from the cur rent func tion. For
ex am ple, press ing ESC while scan ning in ae rial track ing stops the scan ning.
Pressing ESC also al lows you to exit from log ging (the LOG func tion) or
view ing data (the VIEWD func tion) while in sta tion ary data log ging.
GETTING THE DCC STARTED
How to start the sys tem
1. Set the EXT TERM/LO CAL switch in the LO CAL po si tion.
The DCC must have the EXT TERM/LO CAL switch in the LO CAL po si tion
when you power up. If the EXT TERM/LO CAL switch was not in the
LO CAL po si tion when you pow ered up, turn the DCC off, put the EXT
TERM switch in the LO CAL po si tion, and turn the DCC on again. If the DCC 
still fails to power up, the bat ter ies may need charg ing.
NOTE: Some of the tog gle switches on the DCC are lock ing tog gle switches.
They must be pulled up be fore mov ing to a new po si tion.
page 16
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


2. Move the power switch on the DCC to the ON po si tion.
The soft ware is pres ent (loaded and run ning) when you power up the DCC.
The soft ware ver sion is dis played mo men tarily. Then, the cur rent time is
dis played. The cur rent time in cludes the last 2 dig its of the year, the julian
day, the hour, and the min utes. For ex am ple, the year 1996 julian day 200,
hour 10, and min utes 30 is dis played as 96/200/10:30. If the cur rent time is
in cor rect, re fer to the “Re setting the DCC’s time” sec tion. Next, “Press
key....._” is dis played. The DCC is in the main menu. From here, you de cide
on ei ther ae rial track ing or sta tion ary data log ging.
NOTE: The current DCCII program has a power recovery feature. If a power
outage occurs during logging, the DCCII is able to resume logging when power
is restored. The message “Power recovered. Press ‘ESC’ key to avoid Logging”
is displayed momentarily on the DCCII’s screen. Unless ‘ESC’ is pressed, the
DCCII resumes logging using the log table and settings it had at the time of the
power loss.
Se lecting a pro gram
Since there are two pro grams, one for ae rial track ing and the other for sta tion ary
data log ging, a main sec tion is de voted to each pro gram. Please re fer to the
ap pro pri ate sec tion be low.
NOTE: Do not change pro grams un til all data has been offloaded and erased
from the pre vi ous pro gram.
AE RIAL TRACKING
From the main menu, the fol low ing keys in the ae rial menu are ac ces si ble: TIME,
FREQ, SETUP, and SCAN. Then, af ter press ing the SCAN key, the rest of the
keys in the ae rial menu be come ac ces si ble.
Be fore you be gin ae rial track ing, you need to en ter the fre quen cies to be scanned
and set the pro gram vari ables. Pro ceed to the next sec tions.
page 17
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


En tering fre quen cies
To en ter fre quen cies into the fre quency ta ble(s), press the FREQ key.
1.   Ae rial
Fre quency Ta ble
#(1-4):n
En ter the num ber of the fre quency ta ble. 
There are four sep a rate fre quency ta bles num bered 1 through 4. You must choose
one of them to en ter the set of fre quen cies. Four sep a rate ta bles are used for
re search ers us ing a dif fer ent set of fre quen cies for dif fer ent study ar eas. Later,
dur ing scan ning, you can merge any or all of these ta bles to gether. 
2.   # of
chan nels:nn
En ter the num ber of chan nels.
A chan nel num ber is as signed to each fre quency. Each of the four fre quency
ta bles can have a max i mum of 75 chan nels. There fore, the max i mum num ber 
of chan nels you can log is 4*75=300. 
NOTE: The first fre quency that you en ter is as signed chan nel num ber 0.
3. FR1(00):nnnnnn
En ter the en tire fre quency of the trans mit ter in kHz with out dec i mal points.
For ex am ple, to en ter the fre quency 151.234 MHz you would en ter 151234.
NOTE: You can use the CHAN ⇑ and CHAN ⇓ keys to move up and down in the
fre quency ta ble if you make a mis take when en ter ing the fre quen cies.
Re peat Step 3 un til all fre quen cies are en tered and then pro ceed to the next
sec tion.
page 18
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


Set ting pro gram vari ables
To set pro gram vari ables, press the SETUP key. 
1.   SCAN TIME
(secs):nnn
En ter the scan time in sec onds.
The scan time is the amount of time the re ceiver re mains on each fre quency
(or chan nel). The max i mum pos si ble scan time is 5 min utes (300 secs). 
2.    Low est fre quency
 of re ceiver:nnn
En ter the low est fre quency of the re ceiver in MHz with out any dec i mal
points. For ex am ple, if you have a 150.000-153.999 MHz re ceiver, en ter the
num ber 150.
NOTE: The fre quency of your ATS re ceiver is etched on the bot tom edge of the
re ceiver’s face plate.
 At this point, the sta tus of the data file pointer and data file is dis played
mo men tarily as:
      DataPointer is 
at nnnnnn.
DCC is nnn% full!
If there is no data in the DCC, you will see the fol low ing mes sage:
      Data is erased!
Oth er wise, you are given the op tion to erase data next.
3.   Erase data?
En ter ‘1’ if YES
or ‘0’ if NO:n
If the data has al ready been offloaded, en ter ‘1’ for YES to over write the old
data. Re mem ber, the old data is not im me di ately erased. The data file pointer
is set to zero and new data is stored over the old data as it is logged. If the data
page 19
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


has not been offloaded, en ter ‘0’ for NO to keep old data. At this point, go
offload this data. 
Next, the pro gram dis plays the cur rent time ac cord ing to the DCC’s clock. If the
cur rent time is cor rect, press ENTER on Steps 4-7 to ac cept the cur rent value of
the year, julian day, hour and min utes. Oth er wise, you are given the op tion to
change the time in the next four steps.
4. Year:nn
En ter the last two dig its of the pres ent year.
5. Julian Day:nnn
En ter the julian day. Julian days are from 1 to 365.
6. Hour:nn
En ter the hour in 24-hour for mat. Hours are from 0 to 23. Zero is mid night
and 23 is 11pm.
7. Min utes:nn
En ter the min utes. Min utes are from 0 to 59.
Again, the cur rent time is dis played.
Then, the pro gram dis plays “Press key....._”.
If you need to change the pro gram vari ables, see “Changing pro gram vari ables”
on page 26.
Scanning fre quen cies
To start scan ning fre quen cies, press the SCAN key.
Note: When log ging data, the re ceiver’s RF Gain should be fully clock wise and
the re ceiver’s Au dio should be off (fully coun ter clock wise). The Tone De coder
Thresh old con trol should be ad justed to where it is not trig ger ing on noise but
only on valid sig nals. See “Re ceiver con trols” on page 10 and Ap pen dix B on
Tuning Trans mit ters.
1.   Be gin Scanning
Ta ble #(1-4):n
page 20
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


There are four sep a rate fre quency ta bles. To start scan ning, at least one
fre quency ta ble must be moved into the scan ta ble. 
2.   Erase data?
En ter ‘1’ if YES
or ‘0’ if NO:n
If the data has al ready been offloaded, en ter ‘1’ for YES to over write the old
data. Re mem ber, the old data is not im me di ately erased. The data file pointer
is set to zero and new data is stored over the old data as it is logged. If the data
has not been offloaded, en ter ‘0’ for NO to keep old data. At this point, go
offload this data. 
When scan ning has started, the DCC dis plays:
      *SCANNING*
FR(0)=151120
In this ex am ple, the fre quency (FR) of chan nel num ber 0 (shown in
pa ren the sis) is 151120.
The next two sec tions ex plain the scan ta ble and how it can be mod i fied (merg ing
scan ta bles, add ing and de let ing fre quen cies). Re fer to the “Scanning op tions”
sec tion for in for ma tion on how to iden tify trans mit ters on a chan nel and for
in for ma tion on op tions avail able while scan ning.
The scan ta ble
Af ter initializing the sys tem for ae rial track ing (us ing the TIME, FREQ, and
SETUP keys), the DCC scans a list of fre quen cies called the scan ta ble. The scan
ta ble was cre ated when the SCAN key was pressed and the ta ble num ber of one of 
the per ma nent fre quency ta bles was en tered. At this time, the scan ta ble con sists
of one fre quency ta ble. How ever, you can mod ify the scan ta ble by merg ing other
fre quency ta bles, add ing new fre quen cies, or de let ing fre quen cies. Re mem ber, the 
scan ta ble is a tem po rary ta ble. It is a sep a rate fre quency ta ble from the fre quency
ta bles en tered us ing the FREQ key. If you exit scan ning and re turn to the main
menu, the scan ta ble will be erased. To erase the scan ta ble and choose a new
fre quency ta ble, re turn to the main menu by ex it ing scan ning and then press the
SCAN key again. Please re fer to the next three sec tions.
page 21
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


Scanning op tions
•
The ID key:
To iden tify which trans mit ters are on a chan nel, press and re lease the ID key.
On the DCC’s screen, you see:
  FR(0):151120
*IDEN TIFY*
200/10:30
15 15 15
In this ex am ple, the fre quency (FR) of chan nel 0 (shown in pa ren the sis) is
151120. The julian day is 200. The hour is 10. The min utes are 30. The id
code is 15. 
The ID key can be pressed at any time that the re ceiver is scan ning. If a
trans mit ter is pres ent on the cur rent chan nel be ing scanned, the trans mit ter’s id
code ap pears on DCC’s screen. If the trans mit ter is in mor tal ity, an “M” ap pears
be fore the trans mit ter’s id code. The date and time along with the trans mit ter’s
fre quency and id code are au to mat i cally stored when a trans mit ter is iden ti fied.
Press the RESUM key to re sume scan ning.
•
The VIEWD key:
To view the data stored in mem ory, press and re lease the VIEWD key. 
You can press this key while scan ning data or at any point where the pro gram
dis plays “Press key....._”. The num ber of data blocks stored is dis played on the
DCC’s screen. The pro gram asks you to en ter the start ing block num ber and the
num ber of blocks to view. Re mem ber, the first block of data is block num ber
zero. Press ENTER to view the next block of data or ESC to re turn to scan ning or
“Press key....._”. Please re fer to the “Viewing the DCC’s data” sec tion for an
ex pla na tion of what is dis played while view ing data.
page 22
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


•
The HOLD key:
To put a hold on a fre quency, sim ply press and re lease the HOLD key while
the DCC is scan ning. To re move the hold on a fre quency and re sume
scan ning, press the RESUM key.
The DCC ‘s screen dis plays:
 ***HOLDING***
FR(0):151120
In this ex am ple, the fre quency (FR) of chan nel 0 (shown in pa ren the sis) is
151120.
The HOLD key also pro vides ac cess to the ID, TUNE ⇑, TUNE ⇓, CHAN ⇑,
CHAN ⇓ , ADDFR, DELFR and MERGE keys. The func tion of the ID key is
ex plained ear lier in this sec tion. The re main ing keys are ex plained be low.
•
TUNE ⇑ key:
The TUNE ⇑ key tunes the cur rent fre quency of the chan nel up 1 kHz each
time it is pressed. This tun ing is tem po rary. As soon as you re sume scan ning,
the fre quency re turns to what it orig i nally was. This key can be used while
hold ing or iden ti fy ing on a chan nel in ae rial track ing. 
NOTE: Do not hold this key down. It will re sult in a pro gram er ror.
•
TUNE ⇓ key:
The TUNE ⇓ key tunes the cur rent fre quency of the chan nel down 1 kHz each 
time it is pressed. This tun ing is tem po rary. As soon as you re sume scan ning,
the fre quency re turns to what it orig i nally was. This key can be used while
hold ing or iden ti fy ing on a chan nel in ae rial track ing.
NOTE: Do not hold this key down. It will re sult in a pro gram er ror.
•
CHAN ⇑ key:
The CHAN⇑ key moves for ward to the next fre quency or chan nel in the scan
ta ble. This key can be used while hold ing or iden ti fy ing on a chan nel in ae rial
track ing.
page 23
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


NOTE: Do not hold this key down. It will re sult in a pro gram er ror.
•
CHAN ⇓ key:
The CHAN⇓ key moves back to the pre vi ous fre quency or chan nel in the
scan ta ble. This key can be used while hold ing or iden ti fy ing on a chan nel in
ae rial track ing.
NOTE: Do not hold this key down. It will re sult in a pro gram er ror.
•
The ADDFR key:
To add a fre quency to the ta ble you are cur rently scan ning, press and re lease
the ADDFR key.
On the DCC’s dis play, you see:
***ADD FREQ***
FREQ:nnnnnn
En ter the fre quency in kHz with out dec i mal points.
You can ac cess this key at any time dur ing hold ing. The ADDFR key al lows you
to add a fre quency to the cur rent scan ta ble. It does not mat ter which fre quency is
cur rently dis played on the re ceiver when you press this key. The pro gram asks
you for the fre quency to add. En ter the en tire fre quency (in kHz) with out dec i mal
points. Af ter en ter ing the fre quency, the pro gram re sumes at the point where the
ADDFR key was pressed. The fre quency that you add is placed at the end of the
cur rent scan ta ble. If you wish to add more fre quen cies, sim ply re peat the
pro ce dure. No changes are made to the orig i nal fre quency ta bles us ing the FREQ
key. There fore, if you exit and re-enter the log ging, the fre quen cies pre vi ously
added will no lon ger be in the cur rent scan ta ble.
•
The DELFR key:
To de lete a fre quency from the cur rent scan ta ble, press and re lease the
DELFR key. 
On the DCC’s dis play, you will see:
 ***DE LETE FREQ***
FREQ:nnnnnn
page 24
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


En ter the fre quency in kHz with out dec i mal points.
You can ac cess this key at any time dur ing hold ing. It does not mat ter which
fre quency is cur rently dis played on the re ceiver when you press this key. The
DCC searches for the fre quency you en tered. If the fre quency is found, you will
see the word “DE LETING” fol lowed by the dis play of the fre quency you en tered. 
The fre quency is de leted by set ting it equal to 0. If the fre quency was not found,
you will see the phrase “FREQ NOT FOUND” dis played. Af ter this, the pro gram
re sumes at the point where DELFR was pressed. If you wish to de lete more
fre quen cies, sim ply re peat the pro ce dure. The chan nel that con tained the
fre quency is not de leted, but its fre quency is set to zero. Dur ing scan ning, any
chan nel with a fre quency set to zero is skipped. No changes are made to the
orig i nal fre quency ta bles en tered us ing the FREQ key. There fore, if you exit and
re-enter the log ging, the fre quen cies pre vi ously de leted will no lon ger be set to
zero in the cur rent scan ta ble.
•
The MERGE key:
To merge a fre quency ta ble into the cur rent scan ta ble, press and re lease the
MERGE key while hold ing on any fre quency.
On the DCC’s dis play, you will see:
 Add
Ta ble #(1-4):n
En ter the num ber of the ta ble you wish to merge. 
Press RESUM to re sume scan ning.
You can ac cess this key at any time dur ing hold ing. The MERGE key al lows you
to merge fre quency ta bles. When you start scan ning, you choose one of four
fre quency ta bles to scan. The func tion of the MERGE key is to al low you to
merge more fre quency ta bles into the cur rent scan ta ble. You can merge all four
fre quency ta bles to gether. When you merge a fre quency ta ble into the cur rent
scan ta ble, the merged fre quency ta ble is added to the end of the cur rent scan
ta ble. Fig ure 11 shows an ex am ple of merg ing ta bles.
page 25
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


The ideal sit u a tion is to en ter four dif fer ent fre quency ta bles which will be used
for ae rial track ing. Start the scan ning with one of the fre quency ta bles. As the
trans mit ters are found, de lete their fre quen cies from the scan ta ble. When there
are only a few fre quen cies re main ing, add an other fre quency ta ble to scan us ing
the MERGE key. Or, if you need to add only a few fre quen cies to the scan ta ble,
you can use the ADDFR key. 
Changing pro gram vari ables
If you need to change a pro gram vari able ac cessed by the SETUP key, first press
the SETUP key. Then, press ENTER un til you get to the pro gram vari able you
want to change. Pressing ENTER ac cepts the pre vi ous value which is cur rently
dis played. Next, en ter the new vari able. Once the new vari able is en tered, press
ESC to re turn to “Press key....._”. All vari able set tings be yond the one you
changed will re main at their pre vi ous set ting.
Re setting the DCC’s time
To view or edit the DCC’s time, press the TIME key.
1. Year:nn
page 26
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 11 - Merging fre quency ta bles


En ter the last two dig its of the pres ent year.
2. Julian Day:nnn
En ter the julian day. Julian days are from 1 to 365.
3. Hour:nn
En ter the hour in 24-hour for mat. Hours are from 0 to 23. Zero is mid night
and 23 is 11pm.
4. Min utes:nn
En ter the min utes. Min utes are from 0 to 59.
NOTE: The DCC should main tain time ac cu rately even when it is pow ered off.
If the DCC prompts you for the cur rent time upon power-up, it is an in di ca tion
that the back-up bat tery is fail ing.
Af ter the date and time are en tered, the screen redisplays the cur rent time
fol lowed by “Press key....._”. 
You can ac ti vate the TIME key at any point in the pro gram when “Press key....._” 
is dis played. 
STA TION ARY DATA LOGGING
Set ting Pro gram Vari ables
To set pro gram vari ables for sta tion ary data log ging, press the SETUP key. 
1.   SCAN TIME
(secs):nnn
En ter the scan time in sec onds.
The scan time is the amount of time the re ceiver re mains on each fre quency
(or chan nel). The max i mum pos si ble scan time is 5 min utes (300 secs). 
2.   TIME OUT
(secs):nnn
page 27
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


En ter the time out in sec onds. If you do not wish to use a time out, en ter ‘0’. A
‘0’ will de fault to the set ting of the scan time.
The time out al lows you to quit log ging on a fre quency be fore the scan time is
up if there are no in com ing sig nals on that fre quency. For ex am ple: If you are
us ing a scan time of 10 sec onds and pro gram the time out for 2 sec onds, you
will not waste 10 sec onds on a fre quency that does not have any in com ing
sig nals. In stead, the DCC will move to the next fre quency af ter only 2
sec onds. 
3.   LOG con tin u ous
‘0’ or ev ery
‘#’ mins?:n
En ter the log in ter val in min utes. If you want con tin u ous data log ging, en ter 
‘0’ for the log in ter val. If you chose a log in ter val other than ‘0’, pro ceed to
Step 5. 
The log in ter val is equal to the time to log once through the fre quency ta ble.
For ex am ple, if you have 20 chan nels with a scan time of 5 sec onds and you
en ter a log in ter val of 15 min utes, it takes 100 sec onds (or 1.67 min utes) to
log the 20 chan nels. Then, the pro gram waits 15-1.67=13.333 min utes be fore 
log ging through the fre quency ta ble again. The DCC’s screen will
au to mat i cally shut off dur ing the in ac tive part of the log in ter val. Dur ing the
in ac tive part of the log in ter val, the DCC is in a low power mode. If us ing a
re ceiver with com puter-controlled on-off ca pa bil ity, the re ceiver will be
pow ered off dur ing the in ac tive part of the log in ter val.
4.   STORE con tin u ous
‘0’ or ev ery
‘#’ of mins?:n
En ter the store in ter val in min utes. If you do not wish to use this op tion, en ter 
‘0’. 
The store in ter val is the amount of time elapsed be tween stor ing data for a
spe cific fre quency. The DCC still logs all fre quen cies in the fre quency
ta ble(s) con tin u ously. It will store data the first time the an i mal is pres ent.
Then, if the an i mal re mains pres ent, it will not store data for that an i mal un til
this store in ter val has elapsed. For ex am ple, say you are log ging 10
fre quen cies with a store in ter val of 15 min utes. All an i mals ar rive in the first
hour at dif fer ent times and re main in the area for sev eral days. The first time
the sig nal from each an i mal’s trans mit ter is de tected, data for that fre quency
is stored. There fore, ev ery an i mal’s ar rival time is fairly ac cu rate. Then, for
the next sev eral days, data is stored for each an i mal in 15 min ute in ter vals
page 28
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


from the time the an i mal ar rived un til the an i mal leaves the area. This is a way 
of con serv ing space in the data file. You should use this op tion if the an i mal’s
ar rival time is more im por tant to you than the an i mal’s de par ture time. Since
the store in ter val in this ex am ple is 15 min utes, your de par ture time could be
off by a max i mum of 15 min utes.
NOTE: The DCC moves rap idly through the fre quen cies that are not due to be
logged (store in ter val has not yet elapsed). 
5.   # of an ten nas
used:n
En ter the num ber of an ten nas you are us ing. Up to four an ten nas may be used if
us ing a multi plexer. Re fer to “Re ceiver Con nec tions” on page 6 for more about
the multi plexer.
6.  Low est fre quency
 of re ceiver:nnn
En ter the low est fre quency of the re ceiver in MHz with out any dec i mal
points. For ex am ple, if you have a 150.000-153.999 MHz re ceiver, en ter the
num ber 150.
NOTE: The fre quency of your ATS re ceiver is etched on the bot tom edge of the
re ceiver’s face plate.
 At this point, the sta tus of the data file pointer and data file is dis played
mo men tarily as:
      DataPointer is 
at nnnnnn.
DCC is nnn% full!
If there is no data in the DCC, you will see the fol low ing mes sage:
      Data is erased!
Oth er wise, you are given the op tion to erase data next.
7.   Erase data?
En ter ‘1’ if YES
or ‘0’ if NO:n
page 29
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


If the data has al ready been offloaded, en ter ‘1’ for YES to over write the old
data. Re mem ber, the old data is not im me di ately erased. The data file pointer
is set to zero and new data is stored over the old data as it is logged. If the data
has not been offloaded, en ter ‘0’ for NO to keep old data. At this point, go
offload this data. 
Next, the pro gram dis plays the cur rent time ac cord ing to the DCC’s clock. If the
cur rent time is cor rect, press ENTER on Steps 8-11 to ac cept the cur rent value of
the year, julian day, hour and min utes. Oth er wise, you are given the op tion to
change the time in the next four steps.
8. Year:nn
En ter the last two dig its of the pres ent year.
9. Julian Day:nnn
En ter the julian day. Julian days are from 1 to 365.
10. Hour:nn
En ter the hour in 24-hour for mat. Hours are from 0 to 23. Zero is mid night
and 23 is 11pm.
11. Min utes:nn
En ter the min utes. Min utes are from 0 to 59.
Again, the cur rent time is dis played.
Then, the pro gram dis plays “Press key.....”.
If you need to change the pro gram vari ables, see “Changing pro gram vari ables”
on page 26.
En tering Fre quencies
Be fore datalogging can be gin, you must en ter fre quen cies into a fre quency ta ble. 
This sec tion ex plains how to en ter fre quen cies into the fre quency ta ble used
dur ing sta tion ary data log ging.
To en ter fre quen cies into the fre quency ta ble, press the ENTF key.
page 30
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


1.   # of
chan nels:nnn
A chan nel num ber is as signed to each fre quency. The max i mum num ber of
chan nels is 100.
NOTE: The first fre quency that you as sign is chan nel num ber 0.
The only time you should start with a chan nel num ber other than 0 is if you
have al ready pro grammed the fre quen cies in and you wish to change a few
that you know are far ther down the chan nel list. Then, you can by pass some
chan nels to get to the chan nels that you have to change.
2. FR(00):nnnnnn
En ter the en tire fre quency of the trans mit ter in kHz with out dec i mal points.
For ex am ple, to en ter the fre quency 151.234 MHz you would en ter 151234.
NOTE: You can use the CHAN ⇑ and CHAN ⇓ keys to move up and down in the
fre quency ta ble if you make a mis take when en ter ing the fre quen cies. 
Re peat Step 2 un til all fre quen cies are en tered and then pro ceed to the “Logging
the data” sec tion.
Logging the data
To start the sta tion ary data log ging, press the LOG key. 
As the DCC is log ging data (with the screen on), you see the fol low ing dis played
on the DCC’s screen:
96/200/10:30 A#=1
FR(0)=151120
15-180
In this ex am ple, the year (last 2 dig its) is 96, the julian day is 200, the hour is
10, the min utes are 30, the an tenna num ber (A#) is 1, the fre quency (FR) of
chan nel num ber 0 (shown in pa ren the sis) is 151120, the id (iden ti fi ca tion)
code is 15 and the sig nal strength is 180.
page 31
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


The DCC per forms the iden tify (id) func tion on each chan nel. If a trans mit ter
reg is ters as pres ent, the id code ap pears on the third line of the DCC’s screen. For
a trans mit ter in mor tal ity, a “M” ap pears be fore the trans mit ter’s id code. 
NOTE: The sig nal strength is a mea sure ment of sig nal level. It should be used as 
a means of de ter min ing the gen eral di rec tion of the stron gest sig nal. It is not
meant as a mea sure ment of dis tance.
If a sig nal is de tected, all of the data dis played on the DCC’s screen dur ing
log ging (date and time, an tenna num ber, fre quency, id code and sig nal strength) is 
stored along with the pe riod of the in com ing sig nal. Also, once each hour, the
DCC sends its data for the hour to the DCP. In cluded in this hourly data is the
DCC’s volt age and the re ceiver’s volt age.
Note: When log ging data, the re ceiver’s RF Gain should be fully clock wise and
the re ceiver’s Au dio should be off (fully coun ter clock wise). The Tone De coder
Thresh old con trol should be ad justed to where it is not trig ger ing on noise but
only on valid sig nals. See “Re ceiver con trols” on page 10 and Ap pen dix B on
Tuning Trans mit ters.
Data log ging op tions
The fol low ing ex plains which keys can be ac cessed dur ing log ging:
•
The VIEWD key:
To view the data stored in mem ory, press and re lease the VIEWD key. 
You can press this key while log ging data or at any point where the pro gram
dis plays “Press key....._”. The num ber of data blocks stored is dis played on the
DCC’s screen. The pro gram asks you to en ter the start ing block num ber and the
num ber of blocks to view. Re mem ber, the first block of data is block num ber
zero. Press ENTER to view the next block of data or ESC to re turn to log ging or
“Press key.....”. Please re fer to the “Viewing the DCC’s data” sec tion for an
ex pla na tion of what is dis played while view ing data.
•
The SCR key:
To turn the DCC’s screen off or on de pend ing on its cur rent sta tus, press and
re lease the SCR key.
page 32
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


The SCR key can only be ac cessed when log ging data. With the screen off, the
cur rent drain is less. There fore, you should turn the screen off when you leave the
sys tem run ning in the field. Turn the screen on (by the same pro ce dure) when you 
re turn to the field. The screen is au to mat i cally turned on dur ing power-up of the
DCC and is au to mat i cally turned off dur ing the in ac tive part of the log in ter val
when us ing a log in ter val other than ‘0’.
•
The ADDFR key:
To add a fre quency to the ta ble you are cur rently log ging, press and re lease
the ADDFR key.
On the DCC’s dis play, you will see:
***ADD FREQ***
FREQ:nnnnnn
En ter the fre quency in kHz with out dec i mal points.
The ADDFR key al lows you to add a fre quency to the cur rent log ging ta ble. You
can ac cess this key at any time dur ing log ging or hold ing. It does not mat ter
which fre quency is cur rently dis played on the re ceiver when you press this key.
The pro gram asks you for the fre quency to add. En ter the en tire fre quency (in
kHz) with out dec i mal points. Af ter en ter ing the fre quency, the pro gram re sumes
at the point where the ADDFR key was pressed. The fre quency that you add is
placed at the end of the cur rent log ging ta ble. If you wish to add more
fre quen cies, sim ply re peat the pro ce dure. No changes are made to the orig i nal
fre quency ta bles us ing the FREQ key. There fore, if you exit and re-enter the
log ging, the fre quen cies pre vi ously added will no lon ger be in the cur rent log ging
ta ble.
•
The DELFR key:
To de lete a fre quency from the cur rent log ging ta ble, press and re lease the
DELFR key. 
On the DCC’s dis play, you will see:
 ***DE LETE FREQ***
FREQ:nnnnnn
En ter the fre quency in kHz with out dec i mal points.
page 33
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


You can ac cess this key at any time dur ing log ging or hold ing. It does not mat ter
which fre quency is cur rently dis played on the re ceiver when you press this key.
The DCC searches for the fre quency you en tered. If the fre quency is found, you
will see the word “DE LETING” fol lowed by the dis play of the fre quency you
en tered. The fre quency is de leted by set ting it equal to 0. If the fre quency was not
found, you will see the phrase “FREQ NOT FOUND” dis played. Af ter this, the
pro gram re sumes at the point where DELFR was pressed. If you wish to de lete
more fre quen cies, sim ply re peat the pro ce dure. The chan nel that con tained the
fre quency is not de leted, but its fre quency is set to zero. Dur ing log ging, any
chan nel with a fre quency set to zero is skipped. No changes are made to the
orig i nal fre quency ta bles en tered us ing the FREQ key. There fore, if you exit and
re-enter the log ging, the fre quen cies pre vi ously de leted will no lon ger be set to
zero in the cur rent log ging ta ble.
•
The HOLD key
To put a hold on a fre quency, sim ply press and re lease the HOLD key while
the DCC is log ging data. To re move the hold on a fre quency and re sume
log ging, press the ESC key.
The HOLD key holds the re ceiver on the pres ent fre quency and dis plays
re peat edly ei ther the pe riod (in mil li sec onds) or the sig nal strength of the
in com ing sig nal.
On the DCC’s dis play, you see:
***HOLDING***
      0:Pe riod
      1:Sgnl Strength
      En ter Choice:n
If you choose ‘0’, you see the in com ing pe ri ods dis played:
FR(0):151120
       991 991 991
In this ex am ple, the fre quency (FR) you are hold ing on is 151120. The
chan nel num ber of the fre quency (shown in pa ren the sis) is 0. And, the pe riod
of the in com ing sig nal is 991.
If you choose ‘1’, you see the in com ing sig nal strengths dis played:
page 34
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


FR(0):151120
      A#=1 
      180 180 181
In this ex am ple, the fre quency (FR) is 151120. The chan nel num ber (shown
in pa ren the sis) is 0. The an tenna num ber (A#) is 1. And, the in com ing sig nal
strengths are 180, 180 and 181.
The other func tion of the HOLD key is to ac cess the TUNE and CHAN keys.
In ad di tion, you can change the cur rent log ging ta ble while hold ing by us ing
the ADDFR and DELFR keys. Pro ceed to the sec tion “Holding on a
fre quency”.
Holding on a fre quency
While the DCC is log ging data, you can sus pend log ging and hold on a fre quency
as ex plained in the pre vi ous sec tion. Six keys can be ac cessed while hold ing on a
fre quency. These are the CHAN⇑, CHAN⇓, TUNE⇑, TUNE⇓, ADDFR and
DELFR keys. The ADDFR and DELFR keys are dis cussed in the pre vi ous
sec tion. The re main ing keys are ex plained be low:
•
CHAN ⇑ and CHAN ⇓
If you hold on a fre quency and it is not the fre quency you wanted, use the
CHAN keys to find the cor rect fre quency in the cur rent log ging ta ble. 
•
TUNE ⇑ and TUNE ⇓
Once you have the cor rect fre quency, the TUNE keys may be used to tune the
fre quency up or down by 1 kHz each time the key is pressed and re leased. The 
tun ing is tem po rary. The tuned fre quency is not stored in the fre quency ta ble.
The TUNE keys en able you to de ter mine which fre quency is the best
fre quency for log ging data. 
If you want to hold on a fre quency that is not in the cur rent log ging ta ble and could
not be eas ily tuned from one of the cur rent log ging ta ble fre quen cies, put the DCC in
the hold mode and hold the REC/COMP switch in the REC po si tion. Then, se lect the
fre quency with the di als on the re ceiver’s face.
Also, while hold ing on a fre quency you can lis ten to the sig nal by turn ing the au dio
on. How ever, re mem ber to turn the au dio off when the DCC re sumes log ging. 
page 35
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


Press the ESC key to re sume datalogging.
How to Exit Logging
To stop data log ging, press the ESC key.
If the DCC is ac tively log ging, the DCC waits for the scan time to ex pire
be fore it quits log ging data.
NOTE: If you power off the DCC while it is in the in ac tive part of the log in ter val 
(when us ing a log in ter val other than ‘0’) be fore press ing the ESC key, the next
time you power on the DCC it is pos si ble that the DCC’s screen will dis play
mes sages in cor rectly (on top of each other on the same line). If this oc curs, turn
the DCC off again, wait one min ute, and turn the DCC back on.
When the DCC runs out of space to store data, it prints the mes sage “data file
Full” con tin u ously. At this point, data is no lon ger logged. Press ESC to exit.
Af ter ex it ing sta tion ary data log ging, “STA TION ARY Press key....._” is
dis played.
To exit from the sta tion ary menu, press ESC again.
Viewing the DCC’s data
To view the data in the DCC’s mem ory, press the VIEWD key. You can also
erase data or re store data us ing the VIEWD key.
1.  *MEM ORY OP TIONS*
 0:View Data
 1:Erase Data
 2:Re store Data
En ter Choice:n
To view data, en ter ‘0’. The DCC re sponds by dis play ing the num ber of data
blocks avail able to view. Com plete Steps 2-5.
To erase data, en ter ‘1’. Com plete Step 6 only.
page 36
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


To re store data, en ter ‘2’. If you chose to re store data, the fol low ing mes sage is
dis played:
**Written over
data can not be
re stored!! **
Pro ceed to Step 7.
2.    Start at:nnnnn
En ter the start block num ber. The cur rent start block de faults to zero. If you
do not want to start at the first block, sim ply en ter the start block num ber you
de sire.
3. # blocks:nnnnn
The num ber of blocks of data to view de faults to the re main ing num ber of
blocks cur rently stored in the data file. If you do not want to view the en tire
num ber of blocks re main ing in the data file, sim ply en ter the num ber of
blocks you wish to view.
4. Press the ENTER key to ad vance to the next block of data. 
The DCC’s screen dis plays one block of data at a time.
5. Re peat Step 4 un til all data is viewed or press the ESC key to exit view ing data.
Since each pro gram has a dif fer ent for mat for view ing data, please re fer to the
ap pro pri ate sec tion be low for in for ma tion on view ing data.
6.   Erase data?
En ter ‘1’ if YES
or ‘0’ if NO:n
If the data has al ready been offloaded, en ter ‘1’ for YES to over write the old
data. Re mem ber, the old data is not im me di ately erased. The data file pointer
is set to zero and new data is stored over the old data as it is logged. If the data
has not been offloaded, en ter ‘0’ for NO to keep old data. At this point, go
offload this data. 
7.   Type of Re store
0:Use last dptr
1:En ter dptr
En ter Choice:n
page 37
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


En ter ‘0’ and com plete Step 8 to re store the value of the pre vi ous data file
pointer. Oth er wise, en ter ‘1’ and com plete Step 9 to en ter a new data file
pointer .
If you chose to re store the last data file pointer, the fol low ing mes sage is
dis played:
This re stores
the dptr to its
pre-ERASE value.
8.   Are You Sure?
En ter ‘1’ if YES
or ‘0’ if NO:n
En ter ‘1’ to re store the value of the pre vi ous data file pointer. Oth er wise,
en ter ‘0’ to can cel the re store.
If you en tered ‘1’, “Data re stored!” is dis played.
9.   En ter the num ber
of data blocks
to be re stored
—>:n
En ter the de sired num ber of data blocks to re store (as sumes start ing from
block #0). 
If a num ber other than ‘0’ is en tered, “Data re stored!” is dis played.
 To offload the re stored data, re fer to the sec tion “Getting your data out of the
DCC”. 
Ae rial data
When view ing data stored dur ing ae rial track ing, you see the fol low ing dis played
on the DCC’s screen:
200/10:30
FR=1120
ID=150
In this ex am ple, the julian day is 200, the hour is 10, the min utes are 30, the
last 4 dig its of the fre quency (FR) are 1120 and the id code is 150.
page 38
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


The id code con sists of the first 2 dig its of the pe riod from the start of one
pulse to the start of an other pulse in its pat tern. For ex am ple, the id code of a
pulse-coded tag with a pat tern of 155 ms is 15. Offloaded data will show
ei ther a ‘0’ or a ‘6’ af ter the id code. A ‘0’ in di cates the DCC did not de tect a
mor tal ity sig nal. A ‘6’ in di cates the DCC de tected a mor tal ity sig nal. 
Sta tion ary data
When view ing data stored dur ing sta tion ary data log ging, you see the fol low ing
dis played on the DCC’s screen:
200/10:30 A#=1
FR=1120
ID=150   SS=180
PE RIOD=992
In this ex am ple, the julian day is 200, the hour is 10, the min utes are 30, the
an tenna num ber (A#) is 1, the last 4 dig its of the fre quency (FR) are 1120, the
id code is 150, the sig nal strength is 180 and the pe riod is 992. 
The id code con sists of the first 2 dig its of the pe riod from the start of one
pulse to the start of an other pulse in its pat tern. For ex am ple, the id code of a
pulse-coded tag with a pat tern of 155 ms is 15. Offloaded data will show
ei ther a ‘0’, a ‘3’ or a ‘6’ af ter the id code. A ‘0’ in di cates the DCC did not
de tect a mor tal ity sig nal. A ‘3’ in di cates the DCC de tected a mor tal ity sig nal
once. And, a ‘6’ in di cates the DCC de tected a mor tal ity sig nal twice.
The pe riod is the mea sure ment from the start of the first pulse to the start of
the sec ond pulse in a pat tern. For more in for ma tion on id codes and pe ri ods,
re fer to the “Ex pla na tion of outputted data” sec tion.
GETTING YOUR DATA OUT OF THE DCC
The DCC can be used for ei ther ae rial track ing or sta tion ary data log ging. Data
stored in ae rial track ing is dif fer ent from data stored in sta tion ary data log ging.
How ever, both ae rial track ing and sta tion ary data log ging use the same ar eas in
mem ory to store data. 
page 39
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


NOTE: Never start sta tion ary data log ging when ae rial track ing data has not
been offloaded and never start ae rial track ing when sta tion ary data has not
been offloaded.
Offloading data us ing an IBM-compatible PC
The soft ware PROCOMM PLUS is used to es tab lish com mu ni ca tion be tween
your PC and your DCC.
If you are us ing the DOS ver sion of PROCOMM PLUS, please pro ceed to the
next sec tion “Using the DOS ver sion of PROCOMM PLUS”. If you are us ing
PROCOMM PLUS for Win dows, please pro ceed to the sec tion “Using
PROCOMM PLUS for Win dows”.
Using the DOS ver sion of PROCOMM PLUS
1. Move to the DOS prompt.
2. In sert the GETDATA disk ATS pro vided into the floppy disk drive of your PC.
NOTE: If your PC has a hard drive, copy the con tents of the GETDATA disk to
a sub di rec tory on your PC’s hard drive. Working off the hard drive will
sub stan tially speed up the offloading pro cess.
3. Using the EIA-232 ca ble sup plied by ATS, con nect the DCC to a per sonal
com puter (PC) with a floppy disk drive. Fig ure 12 dem on strates this con nec tion.
Plug one end of the ca ble into the EXT TER MI NAL con nec tor of the DCC
and the other end of the ca ble into the se rial port of the PC.
4. Make sure the DCC is pow ered on with “Press key.....” dis played on its screen.
5. Move the DCC’s EXT TERM/LO CAL switch to the EXT TERM po si tion.
6. Change to the drive or sub di rec tory where the GETDATA disk files are
lo cated.
page 40
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


7. Type GETDATA and press ENTER.
Af ter a few sec onds de lay, you will see in struc tions on pre par ing the DCC for 
offloading. Once all con di tions are met, press any key to con tinue.
Next, you will see a mes sage tell ing you how many blocks of data you can
offload. You do not want to at tempt to offload more blocks of data than the
GETDATA disk or hard drive can hold.
Then, PROCOMM PLUS is au to mat i cally loaded. This com mu ni ca tion
pro gram trans fers data from the DCC to the PC.
8. En ter which se rial port you are us ing - COM1 or COM2.
The num ber of blocks in the DCC avail able for offloading is dis played next.
9. En ter the start ing block num ber for the data offload.
page 41
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)
Fig ure 12 - DCC con nected to PC for offloading data


Re mem ber, the first block of data stored is block num ber zero.
10. En ter the num ber of blocks you want to offload.
NOTE: When offloading data, you must con sider file size. If you have many
blocks of avail able data, it is not nec es sary to offload all the blocks into one file.
For ex am ple: If you have 10,000 blocks of avail able data stored, offload blocks
0-4,999 to one file and blocks 5,000-5,999 to an other file. If you are im port ing
data into a spread sheet or da ta base pro gram, check to see how many lines of
data it will ac cept.
As the data is trans ferred, a win dow on the PC’s screen dis plays in for ma tion
about its prog ress. The “COR REC TIONS” line should equal 0. If the num ber 
of cor rec tions is not equal to 0, try offloading again. When the data trans fer is
com plete, “COM PLETED” flashes in side the block.
11. Type ‘Y’ to have data shown on the screen as well as writ ten to a file.
NOTE: The offloading pro cess is con sid er ably faster if you an swer NO to
hav ing data shown on the screen.
Af ter a few sec onds, you are asked to choose the type of data for mat you
pre fer. The choices are reg u lar-Ascii or ready-for-import into other com puter 
pro grams.
12. Press the let ter of the de sired data for mat.
13. En ter the file name for the re sult ing file.
It is a good idea to store the out put file in a dif fer ent lo ca tion than the
GETDATA disk. Oth er wise, you may run out of room on the GETDATA
disk.
If you an swered ‘Y’ to Step 11, data is printed on the screen and sent to the
out put file si mul ta neously as it is pro cessed.
Using PROCOMM PLUS for Win dows
1. In stall PROCOMM PLUS for Win dows.
page 42
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


2. Install GETCODE script by running “Setup” on the GETCODE installation
disk provided by ATS.
3. En ter PROCOMM PLUS 4.8 (by choos ing the PROCOMM PLUS icon under
Programs, Procomm Plus in the Windows Start Menu) and verify that the Script
path to C:\Program Files\Symantec\Procomm Plus\Aspect and the Down load path 
is C:\Program Files\Symantec\Procomm Plus\Download (in the Options
pull-down menu, choose Data Op tions, Paths, if invalid en ter the spec i fied paths,
choose Save as, then OK to save as nor mal op tions).
NOTE: Steps 1-3 need not be re peated af ter the first offloading un less us ing a
dif fer ent PC.
4. Using the EIA-232 ca ble sup plied by ATS, con nect the DCC to a per sonal
com puter (PC) with a floppy disk drive. Fig ure 12 dem on strates this con nec tion.
Plug one end of the ca ble into the EXT TER MI NAL con nec tor of the DCC
and the other end of the ca ble into the se rial port of the PC. 
5. Make sure the DCC is pow ered on with “Press key.....” dis played on its screen.
6. Move the DCC’s EXT TERM/LO CAL switch to the EXT TERM po si tion.
7. En ter PROCOMM PLUS for Win dows by choos ing the PROCOMM PLUS
icon.
8. From the Scripts pull-down menu, choose “Run”.
9. Choose the file “GETCODE.WAX”.
10. Click on “OK”.
11. En ter which se rial port you are us ing - COM1 or COM2.
The num ber of blocks in the DCC avail able for offloading is dis played next.
12. En ter the start ing block num ber for the data offload.
Re mem ber, the first block of data stored is block num ber zero.
13. En ter the num ber of blocks you want to offload.
NOTE: When offloading data, you must con sider the file size. If you have many
blocks of avail able data, it is not nec es sary to offload all the blocks into one file. 
For ex am ple: If you have 10,000 blocks of avail able data stored, offload blocks
page 43
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


0-4,999 to one file and blocks 5,000-9,999 to an other file. If you are im port ing
data into a spread sheet or da ta base pro gram, check to see how many lines of
data it will ac cept. 
As the data is trans ferred, a win dow on the PC’s screen will dis play
in for ma tion about its prog ress. When the data trans fer is com plete,
“COM PLETED” flashes in side the block.
14. Type ‘Y’ to have data shown on the screen as well as writ ten to a file.
NOTE: The offloading pro cess is con sid er ably faster if you an swer NO to
hav ing data shown on the screen.
Af ter a few sec onds, you are asked to choose the type of data for mat you
pre fer. The choices are reg u lar-ASCII and ready-for-import into other
com puter pro grams.
15. Press the let ter of the de sired for mat.
16. En ter the file name for the re sult ing file.
The out put file path de faults to your C:\Program Files\Symantec\Procomm
Plus\Download di rec tory on your PC. In other words, this is where your
out put file will be lo cated.
If you an swered ‘Y’ to Step 14, data is printed on the screen and sent to the
out put file si mul ta neously as it is pro cessed.
Many soft ware file-handling pro grams need spe cific file ex ten sions.
Con sider this re quire ment when nam ing the data files dur ing the offloading
pro cess. Lo tus soft ware, for ex am ple, re quires the file ex ten sion “.prn”.
Since each pro gram has a dif fer ent for mat for out put ting data, please re fer to the
“Ex pla na tion of outputted data” sec tion.
Offloading data us ing a Macintosh PC
1. In stall the Mi cro phone II soft ware.
2. In sert the GETDATA disk into the disk drive.
3. Copy the disk to the hard drive.
page 44
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


4. An swer “OK” to cre at ing a new folder.
A new folder will be cre ated named GETDATA DISK and it is iden ti cal to
the GETDATA disk in the floppy disk drive.
5. Using the EIA-232 ca ble sup plied by ATS, con nect the DCC to the per sonal
com puter (PC).
Plug one end of the ca ble into the EXT TER MI NAL con nec tor of the DCC
and the other end of the ca ble into the phone port of the PC. 
NOTE: If you are us ing a Macintosh Powerbook, plug the EIA-232 into the
printer port in stead of the phone port. The phone port is oc cu pied by an in ter nal 
mo dem.
6. Make sure the DCC is pow ered on with “Press key.....” dis played on its screen.
7. Move the DCC’s EXT TERM/LO CAL switch to the EXT TERM po si tion.
8. En ter the GETDATA folder.
9. Choose Mi cro phone set tings.
10. Choose the Getdata icon.
Check that all the con di tions listed are met. Then, click on the Done icon to
con tinue.
Next, you will see the num ber of blocks avail able dis played on the
Macintosh’s screen. Again, click the Done icon to con tinue.
11. En ter the start ing block num ber for the data offload.
Re mem ber, the first block of data stored is block num ber zero.
12. En ter the num ber of blocks to offload.
NOTE: When offloading data, you must con sider the file size. If you have many
blocks of avail able data, it is not nec es sary to offload all the blocks into one file. 
For ex am ple: If you have 10,000 blocks of avail able data stored, offload blocks
0-4,999 to one file and blocks 5,000-9,999 to an other file. If you are im port ing
data into a spread sheet or da ta base pro gram, check to see how many lines of
data it will ac cept.
page 45
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


 Af ter the X-modem trans fer is com pleted, you will see in struc tions on
trans lat ing data to a user-recognizable for mat.
13. En ter the CODED3A ap pli ca tion.
14. En ter “getdata.dat” as the name of the in put file.
15. En ter the name of the out put file.
Do not use a pe riod in the file name. Also, do not give this file the same name
as the in put file. This is the file you will im port into Ex cel.
16. Choose the data for mat for the out put file.
To use Microsoft Ex cel, al ways choose op tion “b”.
17. Press RE TURN when the data trans la tion stops.
From here, you can im port the out put file into Microsoft Ex cel by en ter ing Ex cel
and open ing the file you cre ated just cre ated.
Since each pro gram has a dif fer ent for mat for out put ting data, please re fer to the
“Ex pla na tion of outputted data” sec tion.
Ex pla na tion of outputted data
There are two out put for mats avail able. The ASCII for mat in cludes descriptors
which tell you what each num ber rep re sents. How ever, the Im port-Ready for mat
uses only num bers sep a rated by com mas. There fore, be low is an ex pla na tion of
what each num ber rep re sents when us ing the Im port-Ready for mat.
Ae rial track ing
For ae rial track ing, im port-ready data is outputted in the fol low ing for mat:
96,200,10,30,,1120,150
In this ex am ple, the year (last 2 dig its) is 96, the julian day is 200, the hour is
10, the min utes are 30, the an tenna num ber is 1, the fre quency (last 4 dig its) is
1120  and the id code is 15. 
page 46
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


The id code con sists of the first 2 dig its of the pat tern. For ex am ple, the id
code of a pulse-coded tag with a pat tern of 155 ms is 15. Offloaded data will
show ei ther a ‘0’ or a ‘3’ af ter the id code. A ‘0’ in di cates the DCC did not
de tect a mor tal ity sig nal. A ‘3’ in di cates the DCC de tected a mor tal ity sig nal.
Sta tion ary data log ging
For sta tion ary data log ging, im port-ready data is outputted in the fol low ing
for mat:
96,200,10,30,1,1120,150,992,180
In this ex am ple, the year (last 2 dig its) is 96, the julian day is 200, the hour is
10, the min utes are 30, the an tenna num ber is 1, the fre quency (last 4 dig its) is
1120, the id code is 150, the pe riod (in mil li sec onds) is 992 and the sig nal
strength mea sure ment is 180.
The id code con sists of the first 2 dig its of the pat tern which is based on the
spac ing from the start of the first pulse to the start of the sec ond pulse in the
pat tern. For ex am ple, the id code of a coded tag with a pat tern (spac ing) of
155 ms is 15. Offloaded data will show ei ther a ‘0’, a ‘3’ or a ‘6’ af ter the id
code. A ‘0’ in di cates the DCC did not de tect a mor tal ity sig nal. A ‘3’
in di cates the DCC de tected a mor tal ity sig nal once. And, a ‘6’ in di cates the
DCC de tected a mor tal ity sig nal twice. 
The pe riod stored is the pe riod of the start of one pat tern to the start of the next 
pat tern. It may also be a mul ti ple of the pe riod as shown in the ta ble be low.
ID CODE
PAT TERN
PE RIOD
2 X PE RIOD
3 X PE RIOD
10
105
840
1680
2520
11
115
920
1840
2760
12
125
1000
2000
3000
13
135
1080
2160
3240
14
145
1160
2320
3480
15
155
992
1984
2976
16
165
1056
2112
3168
17
175
1120
2240
3360
18
185
1184
2368
3552
19
195
1248
2496
3744
page 47
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


When the pe riod is stored as a mul ti ple of one pe riod, it in di cates that the
DCC failed on an at tempt to de code the pat tern dur ing the scan time. In our
ex am ple above, the pe riod stored was 992. Looking in the ta ble above, this
in di cates a pat tern of 155 was cor rectly de coded twice. If the pe riod stored
was 1984, it in di cates the sec ond pat tern was not de coded cor rectly but the
third pat tern was. And, if the pe riod stored was 2976, it would in di cate the
sec ond and third pat terns were not de coded cor rectly but the fourth pat tern
was. 
CHARGING THE BAT TERIES
To re charge the DCC’s in ter nal bat ter ies, plug the bat tery charger into the EXT
TERM con nec tor on the DCC’s face plate us ing the adapter ATS sup plied.
The DCC and the re ceiver con tain re charge able NiCad bat ter ies. Both are charged 
by us ing the same bat tery charger, but the DCC re quires an ad di tional adapter.
Be cause the DCC’s con nec tor is dif fer ent from the re ceiver’s con nec tor, it is
nec es sary to place the adapter on the end of the bat tery charger’s ca ble be fore
page 48
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems
Fig ure 13 -  DCC be ing re charged


plug ging the charger into the DCC’s EXT TER MI NAL con nec tor. Fig ure 13
dem on strates the con nec tions nec es sary to charge the DCC bat ter ies.
To re charge the re ceiver’s in ter nal bat ter ies, plug the bat tery charger into the
CHG EXT PWR con nec tor on the re ceiver’s face plate.
NOTE: Only use the bat tery charger to re charge the re ceiver’s or DCC’s
in ter nal bat ter ies. Do not use the bat tery charger to power the re ceiver and
DCC from an AC out let. No harm will be done if you try this. How ever, us ing the 
bat tery charger in this way may not pro vide suf fi cient power over time and may
also con trib ute noise. If you need to power the re ceiver from an AC out let, you
can pur chase an AC adapter from ATS.
POWER CON SID ER ATIONS
If an ex ter nal power source is used, power can be pro vided to the re ceiver and
DCC for pro longed pe ri ods of time. The DCC uses the re ceiver’s power when it is 
at tached to the re ceiver. If the re ceiver is us ing an ex ter nal power source, the
DCC also uses the ex ter nal power source for power. When the ex ter nal power
source loses power, both the re ceiver and the DCC use the re ceiver’s bat tery. If
both the ex ter nal power source and the re ceiver lose their power, the DCC runs
off its own bat ter ies un til they lose power. The DCC con tains a back-up bat tery
for its data file and its vari ables. There fore, in the case of to tal power fail ure, the
data is not lost. The ex pected life of the DCC’s back-up bat tery is 10 years. 
The re ceiver trickle charges the DCC bat ter ies any time a charged re ceiver is
con nected. How ever, the re ceiver’s bat ter ies are not trickle charged when an
ex ter nal power source is con nected to the re ceiver.
The DCC’s NiCad bat ter ies have a ca pac ity of 1200 mA-hours. Thus, if we
as sume an av er age cur rent of 15 mA, we can ex pect a life of 80 hours. This fig ure 
as sumes the DCC is log ging data with out the re ceiver at tached. In prac tice, the
DCC would drain cur rent from the re ceiver or ex ter nal power source. The
sys tem’s to tal cur rent drain dur ing dif fer ent stages of the data log ging pro cess are
shown in the Cur rent Drain ta ble be low.
Both the DCC and the re ceiver should be fully charged be fore they are left in the
field for sta tion ary data log ging. See the “Test pro ce dures” sec tion for
in for ma tion on read ing bat tery volt ages. Oth er wise, charge the re ceiver and DCC
over night. Even if they are fully charged, charg ing them over night should not
cause any prob lems.
page 49
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


DCCs and re ceiv ers used in ae rial track ing will need to be charged more
fre quently un less the re ceiver is pow ered by a gell cell. Again, the DCCs and
re ceiv ers should be fully charged be fore be gin ning ae rial track ing.
CUR RENT DRAIN
DCC
RE CEIVER
TO TAL
Ae rial track ing
15 mA
135 mA
150 mA
Iden tifying
Sta tion ary data log ging
8 mA
135 mA
143 mA
Screen on
Sta tion ary data log ging
7 mA
135 mA
142 mA
Screen off
Dur ing sleep mode
3 mA
*O mA
3 mA
(Log in ter val in ac tive)
When data file is full
8 mA
*O mA
8 mA
TIPS AND TECH NIQUES
This sec tion de scribes some check points you can use to test that your data log ging 
sys tem is work ing cor rectly.
Test pro ce dures
•
Press the TEST key to mea sure the bat tery volt ages of the DCC and the
re ceiver.
To get the ac tual volt age read ing of the re ceiver’s in ter nal bat ter ies, the
re ceiver must be at tached to the DCC with out ex ter nal power. If the DCC  is
not op er a tional, you have no way of check ing the bat tery volt ages.
•
The red LED on the DCC should blink once for each pulse re ceived.
page 50
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


•
The “+” sign on the re ceiver’s dis play should blink once for each pulse re -
ceived.
If the “+” sign stays on con tin u ously, ei ther the AU DIO is on or the re ceiver
is be ing over loaded with sig nals or noise.
•
The words “lo-bat” flash on the re ceiver’s screen when the re ceiver is ex -
pe ri enc ing low power.
•
The fre quency dis played on the re ceiver’s dis play should be the same as
the fre quency on the re ceiver’s dis play.
If the fre quen cies are not dis play ing cor rectly on the re ceiver, check if you
have en tered the low est fre quency cor rectly. 
The DCC has a few keys which are use ful for test ing over all sys tem op er a tion.
These keys are the F1, F2, and VIEWD keys. The TEST and F1 keys are to be
used be fore log ging data.
•
F1 key
The F1 key tests the DCP and its con nec tions. Af ter press ing the F1 key, the
DCC’s screen will dis play “TESTS FINE” if the DCP is in the cor rect mode
of op er a tion and is com mu ni cat ing with the DCC ac cu rately. Pressing the F1
key erases the con tents of the DCP’s text buffer. There fore, this key should
only be used be fore you com mence sta tion ary data log ging.
The F2 and VIEWD keys test that the sys tem is stor ing data in the DCC’s data file 
and send ing the same data to the DCP. Both keys are used to test the sta tion ary
data log ging op er a tion.
•
F2 key
The F2 key reads the con tents of the DCP’s text buffer to en sure that the DCC
is send ing data cor rectly to the DCP. As you re call, the DCC sends data to the
DCP ev ery hour. The DCP then trans mits data to the GOES Sat el lite ev ery
three hours. The trick is to use the F2 key just be fore the DCP trans mits its
data to the sat el lite be cause once the data is trans mit ted to the sat el lite, the
data in the DCP’s text buffer is erased. Pressing the F2 key reads the DCP’s
text buffer one line at a time. Press the ENTER key to see the next line of data. 
It will take a num ber of sec onds for the DCC to read the first line of the DCP’s 
data, es pe cially if there is a large amount of data in the DCP’s text buffer.
page 51
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


•
VIEWD key
The VIEWD key dis plays the data stored in the DCC’s data file dur ing
sta tion ary data log ging. The data is also dis played one line at a time. Pressing
the ENTER key al lows you to view the next line of data. When in the field,
use this key to view small quan ti ties of data to en sure that the sys tem is
op er at ing cor rectly. For view ing large quan ti ties of data, see the
OFFLOADING sec tion.
For more in for ma tion about the func tion of the keys, please see the REF ER ENCE 
sec tion. 
How to con serve data file space
In some stud ies, you may need to find ways to con serve the data file space.
Usually, this is when the data log ging sys tem is placed in a re mote area so data
re trieval is in fre quent. If this is the case, you can use the store in ter val data
log ging op tion. This op tion asks you to en ter a time in ter val in min utes. Once the
DCC stores data on a par tic u lar fre quency, it will skip that fre quency un til the
amount of time you pro grammed for the store in ter val has elapsed. Then, af ter the 
store in ter val has elapsed, it will re sume search ing for that fre quency again un til
data is stored. This op tion is only avail able when us ing sta tion ary data log ging.
How to con serve power
To make your data log ging sys tem con serve power, you can use a log in ter val
other than ‘0’. This op tion makes the DCC sleep for a user-programmed pe riod of 
time to con serve power (sav ing about 8 mA). If you wish to use this op tion, you
need to have your re ceiver mod i fied so that the DCC can con trol the re ceiver’s
power. That way, dur ing the in ac tive part of the log in ter val, the DCC will turn
the re ceiver’s power off thus con serv ing about 135 mA. So while ac tively log ging 
the sys tem con sumes about 145 mA, and dur ing the in ac tive part of the log
in ter val the sys tem con sumes about 3 mA. This op tion is only avail able when
us ing sta tion ary data log ging.
page 52
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


AP PEN DIX A - WAR RANTY
Ad vanced Te lem e try Sys tems (ATS) war ran ties its Data Col lec tion Com puters
for a pe riod of one year from the date of ship ment. Dur ing the war ranty pe riod,
ATS will re pair or re place, at our op tion, any de fec tive data col lec tion com put ers.
De fec tive prod ucts must be re turned to ATS in Isanti, Min ne sota or to a
des ig nated ser vice cen ter for war ranty ser vice. The buyer shall pre pay ship ping
charges to ATS; ATS will pay re turn ship ping costs.
Lim i ta tions: War ranty does not ap ply to de fects re sult ing from im proper
main te nance or use, al ter ations, phys i cal dam age, or op er a tion out side
en vi ron men tal spec i fi ca tions.
No other war ran ties are ex pressed or im plied. ATS spe cif i cally dis claims any
im plied war ran ties of mer chant abil ity and fit ness for a par tic u lar use.
The rem e dies listed un der this war ranty are the buy ers’ sole and ex clu sive
rem edy. ATS shall not be li a ble for any di rect, in di rect, spe cial, in ci den tal or
con se quen tial dam ages.
page 53
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


AP PEN DIX B - TUNING TRANS MIT TERS
Dur ing the tun ing pro cess, the trans mit ter’s tem per a ture should be equiv a lent to
the ex pected field tem per a ture. Ideally, the fi nal tun ing should be done at the field 
site.
The DCC does not need to be pres ent.
1. Place the trans mit ters 100 to 200 me ters away from the re ceiv ing an tenna.
2. Con nect the re ceiv ing an tenna to the re ceiver.
3. Make sure the au dio con trol is off.
The trans mit ters should be tuned in us ing the tone de coder of the re ceiver.
4. Set the RF gain at max i mum (turn clock wise as far as it will go).
5. Ad just the thresh old con trol (see the Re ceiver Con trols sec tion of your
Re ceiver Man ual).
6. The “+” sign should flash over a range of 3-5 kHz in di cat ing de tec tion of the
sig nal. Use the cen ter of that range as the fre quency to pro gram into the DCC.
7. The thresh old may have to be re ad justed if noise causes er rors in the data.
page 54
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


AP PEN DIX C - AD JUSTING THE THRESH OLD CON TROL
You need to ad just the tone de coder thresh old con trol (see Fig ure 7 on page 10) if
con di tions are ex tremely noisy or ex tremely quiet.
1. Con nect an an tenna to the re ceiver.
2. Se lect a fre quency where no valid sig nals are pres ent.
Ver ify this by turn ing on the au dio and if no pulses are heard, there are no
valid sig nals pres ent.
3. Turn the au dio off.
4. If the “+” sign on the re ceiver’s dis play is flash ing or on, use a small flat
screw driver to turn the tone de coder thresh old con trol coun ter-clockwise un til the
“+” sign is off.
5. Then, slowly turn the tone de coder thresh old con trol clock wise un til the “+”
sign on the re ceiver’s dis play flashes.
The tone de coder is now trig ger ing on noise.
6. Turn the tone de coder thresh old con trol slightly back (coun ter-clockwise) un til
the “+” sign dis ap pears.
At this point, the re ceiver has  the max i mum sen si tiv ity it can have with out
trig ger ing on noise.
7. De pending on noise con di tions, you may have to fur ther re duce the thresh old to 
get more noise im mu nity.
page 55
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


AP PEN DIX D - DE SCRIP TION OF KEYS
The DCC’s keys are listed in al pha bet i cal or der with the func tion of each key
ex plained.
•
← key
If an er ror while typ ing a num ber, press the ← key to back space and cor rect
the num ber. The ← key must be pressed be fore the ENTER key is pressed.
•
ENTER key
When en ter ing num bers into the DCC, the ENTER key must be pressed to tell 
the DCC you have fin ished. If no num bers are typed be fore the ENTER key is 
pressed, the DCC as sumes you do not wish to change the cur rent value of the
pa ram e ter dis played on the DCC’s screen.
•
ESC key
The ESC key is pressed to exit the sta tion ary menu. Also, press ing the ESC
key al lows you to exit from the cur rent func tion. For ex am ple, press ing ESC
while scan ning in ae rial track ing stops the scan ning. Pressing ESC also
al lows you to exit from log ging (the LOG func tion) or view ing data (the
VIEWD func tion) while in sta tion ary data log ging.
•
SHIFT key
The SHIFT key pro vides ac cess to the func tions lo cated on the up per half of
the keys. Press and re lease the SHIFT key be fore press ing the func tion key
you need.
•
TEST key
The TEST key reads the re ceiver’s volt age. The volt age is dis played on the
DCC’s screen in tenths of volts. For ex am ple, RECvolt=115 is ac tu ally 11.5
volts. The re ceiver’s bat tery volt age should re main above 11.5 volts for
proper op er a tion. The DCC uses the re ceiver’s bat ter ies for op er a tion and its
own bat ter ies are for back-up only. The TEST key also tests the
com mu ni ca tion be tween the DCC’s key board and screen.
page 56
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


•
TIME key
The TIME key al lows you to en ter the cor rect julian day and time for ae rial
track ing. Julian days are from 1 to 365. Hours are from 0 to 23. Zero is
mid night and 23 is 11 pm. Min utes are from 0 to 59.
•
VIEWD key
The VIEWD key dis plays the data stored in the DCC’s data file dur ing
sta tion ary datalogging. The data is also dis played one line at a time. Pressing
the ENTER key al lows you to view the next line of data. When in the field,
use this key to view small quan ti ties of data to en sure that the sys tem is
op er at ing cor rectly. For view ing large quan ti ties of data, see the
OFFLOADING sec tion.
Keys used in ae rial track ing
•
ADDFR key
The ADDFR key al lows you to add a fre quency to the pres ent scan ta ble
dur ing ae rial track ing. You can ac cess this key dur ing hold ing. It does not
mat ter which fre quency is cur rently dis played on the re ceiver when you press 
this key be cause the new fre quency will au to mat i cally be added to the end of
the pres ent scan ta ble. En ter the en tire fre quency (in kHz with out dec i mal
points) to add and then press the RESUM key.
•
CHAN⇑ key
The CHAN⇑ key moves to the next fre quency or chan nel in the scan ta ble.
This key can be used while hold ing or iden ti fy ing on a chan nel in ae rial
track ing. The CHAN⇑  key can also be used to move to the next fre quency or
chan nel when en ter ing fre quen cies un der the FREQ key.
•
CHAN⇓ key
The CHAN⇓ key moves back to the pre vi ous fre quency or chan nel in the
scan ta ble. This key can be used while hold ing or iden ti fy ing on a chan nel in
ae rial track ing. The CHAN⇓  key can also be used to move to the next
fre quency or chan nel when en ter ing fre quen cies un der the FREQ key.
page 57
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


•
DELFR key
The DELFR key al lows you to de lete a fre quency from the pres ent scan ta ble
dur ing ae rial track ing. You can ac cess this key dur ing hold ing.  It does not
mat ter which fre quency is cur rently dis played when you press this key. The
pro gram asks you for the fre quency to de lete. En ter the en tire fre quency (in
kHz) with out dec i mal points. If the fre quency is found in the cur rent log ging
ta ble, you see the word “DE LETING” fol lowed by the fre quency you
en tered. Oth er wise, you see “FREQ NOT FOUND”. Af ter this, the pro gram
re sumes at the point where DELFR was pressed. No changes are made to the
orig i nal fre quency ta ble en tered us ing the ENTF key. If you wish to de lete
more fre quen cies, sim ply re peat the pro ce dure.
•
FREQ key
The FREQ key al lows you to en ter fre quency ta bles for ae rial track ing. You
can en ter up to 4 dif fer ent fre quency ta bles into the DCC. Each fre quency
ta ble can have up to 75 chan nels max i mum. En ter the en tire fre quency in kHz 
with out dec i mal points.
•
HOLD key
The HOLD key holds the re ceiver on the pres ent fre quency and pro vides
ac cess to the MERGE, ADDFR, DELFR, TUNE⇓, TUNE⇑, BACK and
CHAN⇑ keys used in ae rial track ing. Re fer to those keys for fur ther
de scrip tions.
•
ID key
The ID key key can be pressed at any time that the re ceiver is scan ning dur ing
ae rial track ing. If a trans mit ter is pres ent on the cur rent chan nel be ing
scanned, the first two dig its of the trans mit ter’s id code will ap pear on DCC’s
screen. If the trans mit ter is in mor tal ity, an “M” will ap pear be fore the first
two dig its of the trans mit ter’s id code. The date and time along with the
trans mit ter’s fre quency and id code are au to mat i cally stored when a
trans mit ter is iden ti fied.
page 58
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


•
MERGE key
The MERGE key al lows you to merge fre quency ta bles dur ing ae rial
track ing. You can ac cess this key dur ing hold ing. If you merge a fre quency
ta ble into the pres ent scan ta ble, the new fre quency ta ble is au to mat i cally
added to the end of the scan ta ble.
•
RESUM key
The RESUM key re moves the hold on a fre quency or ex its the iden ti fi ca tion
pro cess dur ing ae rial track ing. In both cases, it re sumes scan ning the pres ent
scan ta ble.
•
SCAN key
The SCAN key is used to be gin scan ning one of the fre quency ta bles you
en tered us ing the FREQ key dur ing ae rial track ing. You must en ter a num ber
of a fre quency ta ble to start scan ning. 
•
SETUP key
This key pro vides ac cess to the pro gram vari ables. Be fore scan ning for the
first time, it in nec es sary to ini tial ize pro gram vari ables. You will be al lowed
to set all the pro gram vari ables nec es sary for scan ning (ex cept the
fre quen cies) af ter press ing this key. See the “Set ting pro gram vari ables”
sec tion for more in for ma tion.
•
TUNE⇑ key
The TUNE⇑ key tunes the cur rent fre quency of the chan nel up 1 kHz each
time it is pressed. This tun ing is tem po rary. As soon as you re sume scan ning,
the fre quency re turns to what it orig i nally was. This key can be used while
hold ing or iden ti fy ing on a chan nel in ae rial track ing. 
•
TUNE⇓ key
The TUNE⇓ key tunes the cur rent fre quency of the chan nel down 1 kHz each
time it is pressed. This tun ing is tem po rary. As soon as you re sume scan ning,
the fre quency re turns to what it orig i nally was. This key can be used while
hold ing or iden ti fy ing on a chan nel in ae rial track ing. 
page 59
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


Keys used in sta tion ary data log ging
•
ADDFR key
This key is lo cated in the ae rial menu. How ever, it can be used in sta tion ary
data log ging as well. The ADDFR key al lows you to add a fre quency to the
cur rent log ging ta ble. You can ac cess this key at any time dur ing log ging or
hold ing. It does not mat ter which fre quency is cur rently dis played on the
re ceiver when you press this key. The pro gram asks you for the fre quency to
add. En ter the en tire fre quency (in kHz) with out dec i mal points. Af ter
en ter ing the fre quency, the pro gram re sumes at the point where the ADDFR
key was pressed. The fre quency you added is placed at the end of the cur rent
log ging ta ble. No changes are made to the orig i nal fre quency ta ble en tered
us ing the ENTF key. To add more than one fre quency, sim ply re peat the
pro ce dure as needed.
•
DELFR key
This key is lo cated in the ae rial menu. How ever, it can be used in sta tion ary
data log ging as well. The DELFR key al lows you to de lete a fre quency from
the cur rent log ging ta ble. You can ac cess this key at any time dur ing log ging
or hold ing.  It does not mat ter which fre quency is cur rently dis played when
you press this key. The pro gram asks you for the fre quency to de lete. En ter
the en tire fre quency (in kHz) with out dec i mal points. If the fre quency is
found in the cur rent log ging ta ble, you see the word “DE LETING” fol lowed
by the fre quency you en tered. Oth er wise, you see “FREQ NOT FOUND”.
Af ter this, the pro gram re sumes at the point where DELFR was pressed. No
changes are made to the orig i nal fre quency ta ble en tered us ing the ENTF key. 
If you wish to de lete more fre quen cies, sim ply re peat the pro ce dure.
•
ENTF key
This key lets you en ter fre quen cies into the fre quency ta ble used in sta tion ary
data log ging. En ter the fre quency in kHz with out dec i mal points.
page 60
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


•
F1 key
The F1 key tests the DCP and its con nec tions. Af ter press ing the F1 key, the
DCC’s screen will dis play “TESTS FINE” if the DCP is in the cor rect mode
of op er a tion and is com mu ni cat ing with the DCC ac cu rately. Pressing the F1
key erases the con tents of the DCP’s text buffer. There fore, this key should
only be used be fore you com mence sta tion ary data log ging.
•
F2 key
The F2 key reads the con tents of the DCP’s text buffer to en sure that the DCC
is send ing data cor rectly to the DCP. As you re call, the DCC sends data to the
DCP ev ery hour. The DCP then trans mits data to the GOES Sat el lite ev ery
three hours. The trick is to use the F2 key just be fore the DCP trans mits its
data to the sat el lite be cause once the data is trans mit ted to the sat el lite, the
data in the DCP’s text buffer is erased. Pressing the F2 key reads the DCP’s
text buffer one line at a time. Press the ENTER key to see the next line of data. 
It will take a num ber of sec onds for the DCC to read the first line of the DCP’s 
data, es pe cially if there is a large amount of data in the DCP’s text buffer.
•
HOLD key
The HOLD key holds the re ceiver on the pres ent fre quency and dis plays
ei ther the pe riod (in millisceonds) or the sig nal strength of the in com ing
sig nals. The HOLD key also pro vides ac cess to the TUNE⇓, TUNE⇑,
CHAN⇓ and CΗΑΝ⇑ keys. Re fer to those keys for fur ther de scrip tions.
•
LOG key
This be gins the sta tion ary data log ging. You should have al ready in i tial ized
the pro gram vari ables and en tered your fre quen cies us ing the SETUP and
ENTF keys.
•
SCR key
This turns the DCC’s screen off. The only time this key can be ac cessed is
while you are log ging data in sta tion ary data log ging. Turn ing the DCC’s
screen off low ers the DCC’s cur rent drain. The DCC’s screen should be
turned off when left in the field.
page 61
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


•
SETUP key
The SETUP key al lows ac cess to the ENTF, LOG, and SCR keys of the
sta tion ary data log ging pro gram. First, you are given the op tions of eras ing
data, en ter ing the num ber of chan nels and an ten nas, and cor rect ing the day,
hour, or min utes. 
page 62
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


AP PEN DIX E - QUES TIONS
If you have any ques tions con cern ing your data log ging sys tem, call Ad vanced
Te lem e try Sys tems (ATS) at (763) 444-9267. Di rect ques tions re gard ing soft ware 
to Nancy Christensen or email to nchristensen@atstrack.com. Di rect ques tions
re gard ing or ders or gen eral in for ma tion to sales or email to sales@atstrack.com.
You may also visit our website at www.atstrack.com.
page 63
Ad vanced Te lem e try Sys tems
R07-04-A
DCC man ual (Coded pro gram)


AP PEN DIX F - DCC SPEC I FI CA TIONS
SPEC I FI CA TIONS DCC Data Col lec tion Com puter
PRO CES SOR
Philips 80C51
MEM ORY
384k static RAM (320k avail able for data stor age)
32 - 4 byte words EPROM (for cal i bra tion pa ram e ters)
64k pro gram stor age and op er at ing sys tem EPROM
DIS PLAY
4 line x 16 char ac ter LCD
LED backlight
KEY BOARD
20 key, dual func tion
Func tions:
En ter date and time
Set pro gram vari ables
Set pro gram vari ables
En ter fre quen cies
En ter fre quen cies
Start log ging
Start Scanning
Screen on/off
Iden tify
View data
Hold on a fre quency
Shift
Add a fre quency
En ter
De lete a fre quency
Back space key
Merge fre quency ta bles
Re sume
Tune up/down
Es cape
Chan nels up/down
Spe cial func tion keys(3)
Test bat tery volt age
CON TROLS
Power on/off
Backlight on/off
Re ceiver con trol/Com puter con trol
Ex ter nal/lo cal ter mi nal
Key board
CON NEC TIONS
Ex ter nal ter mi nal
Aux il iary in put/out put
Re ceiver in ter face
Bat tery charger
POWER
Bat tery type:
1.2 amp/hour nickel-cadmium with ex ter nal
recharger or re charged when con nected to re ceiver
Op er ating volt age:
6-20 volts DC
Cur rent drain:
7 mA w/ screen off; 10 mA w/ screen on; 15-50 mA
w/ screen and backlight on
PHYS I CAL
Size:
4.3" wide x 8.3" long x 7" high(11 cm wide x 21 cm
long x 18 cm  high)
Weight:
3 lbs. (1.36 kg.)
EN VI RON MEN TAL
Op er ating tem per a ture:
-20°C to + 50°C (or lower with clock com pen sa -
tion)
Hu mid ity:
95% non-condensing
WAR RANTY
One year parts and la bor on ma te ri als and work man ship.
page 64
DCC man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


AP PEN DIX G - JULIAN DATE CAL EN DARS
JULIAN DATE CAL EN DAR
(PER PET UAL)
Day
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
Day
1
001
032
060
091
121
152
182
213
244
274
305
335
1
2
002
033
061
092
122
153
183
214
245
275
306
336
2
3
003
034
062
093
123
154
184
215
246
276
307
337
3
4
004
035
063
094
124
155
185
216
247
277
308
338
4
5
005
036
064
095
125
156
186
217
248
278
309
339
5
6
006
037
065
096
126
157
187
218
249
279
310
340
6
7
007
038
066
097
127
158
188
219
250
280
311
341
7
8
008
039
067
098
128
159
189
220
251
281
312
342
8
9
009
040
068
099
129
160
190
221
252
282
313
343
9
10
010
041
069
100
130
161
191
222
253
283
314
344
10
11
011
042
070
101
131
162
192
223
254
284
315
345
11
12
012
043
071
102
132
163
193
224
255
285
316
346
12
13
013
044
072
103
133
164
194
225
256
286
317
347
13
14
014
045
073
104
134
165
195
226
257
287
318
348
14
15
015
046
074
105
135
166
196
227
258
288
319
349
15
16
016
047
075
106
136
167
197
228
259
289
320
350
16
17
017
048
076
107
137
168
198
229
260
290
321
351
17
18
018
049
077
108
138
169
199
230
261
291
322
352
18
19
019
050
078
109
139
170
200
231
262
292
323
353
19
20
020
051
079
110
140
171
201
232
263
293
324
354
20
21
021
052
080
111
141
172
202
233
264
294
325
355
21
22
022
053
081
112
142
173
203
234
265
295
326
356
22
23
023
054
082
113
143
174
204
235
266
296
327
357
23
24
024
055
083
114
144
175
205
236
267
297
328
358
24
25
025
056
084
115
145
176
206
237
268
298
329
359
25
26
026
057
085
116
146
177
207
238
269
299
330
360
26
27
027
058
086
117
147
178
208
239
270
300
331
361
27
28
028
059
087
118
148
179
209
240
271
301
332
362
28
29
029
088
119
149
180
210
241
272
302
333
363
29
30
030
089
120
150
181
211
242
273
303
334
364
30
31
031
090
151
212
243
304
365
31
FOR LEAP YEAR USE OTHER CHART
page 65
DCC Man ual (Coded pro gram)
R07-04-A
Ad vanced Te lem e try Sys tems


JULIAN DATE CAL EN DAR
(FOR LEAP YEARS ONLY)
Day
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
Sep
Oct
Nov
Dec
Day
1
001
032
061
092
122
153
183
214
245
275
306
336
1
2
002
033
062
093
123
154
184
215
246
276
307
337
2
3
003
034
063
094
124
155
185
216
247
277
308
338
3
4
004
035
064
095
125
156
186
217
248
278
309
339
4
5
005
036
065
096
126
157
187
218
249
279
310
340
5
6
006
037
066
097
127
158
188
219
250
280
311
341
6
7
007
038
067
098
128
159
189
220
251
281
312
342
7
8
008
039
068
099
129
160
190
221
252
282
313
343
8
9
009
040
069
100
130
161
191
222
253
283
314
344
9
10
010
041
070
101
131
162
192
223
254
284
315
345
10
11
011
042
071
102
132
163
193
224
255
285
316
346
11
12
012
043
072
103
133
164
194
225
256
286
317
347
12
13
013
044
073
104
134
165
195
226
257
287
318
348
13
14
014
045
074
105
135
166
196
227
258
288
319
349
14
15
015
046
075
106
136
167
197
228
259
289
320
350
15
16
016
047
076
107
137
168
198
229
260
290
321
351
16
17
017
048
077
108
138
169
199
230
261
291
322
352
17
18
018
049
078
109
139
170
200
231
262
292
323
353
18
19
019
050
079
110
140
171
201
232
263
293
324
354
19
20
020
051
080
111
141
172
202
233
264
294
325
355
20
21
021
052
081
112
142
173
203
234
265
295
326
356
21
22
022
053
082
113
143
174
204
235
266
296
327
357
22
23
023
054
083
114
144
175
205
236
267
297
328
358
23
24
024
055
084
115
145
176
206
237
268
298
329
359
24
25
025
056
085
116
146
177
207
238
269
299
330
360
25
26
026
057
086
117
147
178
208
239
270
300
331
361
26
27
027
058
087
118
148
179
209
240
271
301
332
362
27
28
028
059
088
119
149
180
210
241
272
302
333
363
28
29
029
060
089
120
150
181
211
242
273
303
334
364
29
30
030
090
121
151
182
212
243
274
304
335
365
30
31
031
091
152
213
244
305
366
31
(USE IN 2004, 2008, 2012, 2016, ETC.)
page 66
Ad vanced Te lem e try Sys tems
R07-04-A
DCC Man ual (Coded pro gram)
