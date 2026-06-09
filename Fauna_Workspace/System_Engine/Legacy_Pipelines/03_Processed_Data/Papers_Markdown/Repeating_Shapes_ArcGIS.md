--- 
source: Repeating_Shapes_ArcGIS.pdf
--- 

 
1 
NAME:  Repeating Shapes for ArcGIS 
Installation File:  repeat_shapes.exe 
Last modified:  November 4, 2012 
TOPICS:  hexagon, square, triangle, repeat, 
sample, tessellation, array, matrix, lattice, point, 
systematic, grid, extent 
AUTHOR:  Jeff Jenness 
Wildlife Biologist, GIS Analyst 
Jenness Enterprises 
3020 N. Schevene Blvd. 
Phone:  1-928-607-4638 
Flagstaff, AZ 86004       USA 
Email:  jeffj@jennessent.com 
Web Site:  http://www.jennessent.com 
 
DESCRIPTION:  Researchers and land managers often require a way to systematically divide the 
landscape into equal-sized portions.  Breaking up the landscape this way simplifies monitoring 
plans, and is an essential step in developing systematic sampling designs. 
This tool generates an array of repeating shapes over a user-specified area.  These shapes can 
be hexagons, squares, rectangles, triangles, circles or points, and they can be generated with 
any directional orientation. 
Shapes can be generated over all selected records of a feature theme, over the entire rectangular 
extent of a theme, over the rectangular extent of all themes in the view, or over the visual extent 
of the display. 
For those who have access to ArcView 3.x, this extension can be used in conjunction with the 
“Random Point Generator” extension (http://www.jennessent.com/arcview/random_points.htm) to 
generate random points within a systematically divided sampling area.  This extension can be 
used to generate systematic polygons over the landscape, and the “Random Point Generator” 
extension can then be used to generate random sample points within those polygons. 
Output:  This extension produces either a point or a polygon feature class and adds it as a layer 
to the map.  The new feature class will be created in the projection and datum of the map display. 
REQUIRES:   ArcView 9.x or 10.x.  
UPDATES:  See p. 24.    
Recommended Citation Format:  For those who wish to cite this extension, the author 
recommends something similar to: 
Jenness, J. 2012.  Repeating shapes for ArcGIS.  Jenness Enterprises.  Available at: 
http://www.jennessent.com/arcgis/repeat_shapes.htm. 
Please let me know if you cite this extension in a publication (jeffj@jennessent.com). I will update 
the citation list to include any publications that I am told about. 
Acknowledgments:  Jenness Enterprises gratefully acknowledges the Ontario Ministry of 
Agriculture, Food and Rural Affairs for supporting portions of this extension.


 
2 
Table of Contents 
INSTALLING REPEATING SHAPES:............................................................................................................ 2 
For ArcGIS 9.x ...................................................................................................................................... 2 
For ArcGIS 10.0 .................................................................................................................................... 3 
Viewing the Tool: .................................................................................................................................. 4 
UNINSTALLING REPEATING SHAPES TOOL .............................................................................................. 6 
For ArcGIS 9.x. ..................................................................................................................................... 6 
For ArcGIS 10.0 .................................................................................................................................... 6 
TROUBLESHOOTING ................................................................................................................................. 9 
If Any of the Tools Crash ....................................................................................................................... 9 
“Object variable or With block variable not set” Error: ............................................................................. 9 
RICHTX32.OCX Error (also comct332.ocx, comdlg32.ocx, mscomct2.ocx, mscomctl.ocx, msstdfmt.dll 
errors): .................................................................................................................................................. 9 
GENERAL INSTRUCTIONS ....................................................................................................................... 12 
Choose the Region of Interest: ............................................................................................................ 12 
With Respect to Selected Features in a Feature Layer: ................................................................................................ 12 
Within the Extent of a Particular Layer: .......................................................................................................................... 14 
Within the Extent of All Layers in the Map: ..................................................................................................................... 14 
Within the Extent of the Display: ..................................................................................................................................... 14 
Choose the Shape Type to Create ....................................................................................................... 14 
Set Shape Parameters: ....................................................................................................................... 15 
Generating Points in a Square Pattern: .......................................................................................................................... 15 
Generating Points in a Triangular Pattern: ..................................................................................................................... 16 
Generating Circles in a Square Pattern: ......................................................................................................................... 17 
Generating Circles in a Triangular Pattern: .................................................................................................................... 17 
Generating Squares: ....................................................................................................................................................... 18 
Generating Rectangles: ................................................................................................................................................... 19 
Generating Triangles: ...................................................................................................................................................... 20 
Generating Hexagons: ..................................................................................................................................................... 21 
GENERAL NOTES: .................................................................................................................................. 23 
Stopping the Process: ......................................................................................................................... 23 
UPDATES ................................................................................................................................................ 24 
 
 
Installing Repeating Shapes: 
For ArcGIS 9.x 
First close ArcGIS if it is open.  The tools do not install properly if ArcGIS is running during the 
installation. 
Install the Repeating Shapes extension by double-clicking on the file repeat_shapes.exe 
(available at  http://www.jennessent.com/downloads/repeat_shapes.zip, or from a link on the 
page http://www.jennessent.com/arcgis/repeat_shapes.htm) and following the instructions.  The 
installation routine will register the Repeating Shapes DLL with all the required ArcMap 
components. 
The default install folder for the extension is named “repeating_shapes” and is located inside the 
folder “Program Files\Jennessent”.  This folder will also include some additional files and this 
manual. 


 
3 
For ArcGIS 10.0 
Note:  This function will only work if you have ArcGIS 10 installed.   
1. First close ArcGIS if it is open.  The tools do not install properly if ArcGIS is running during 
the installation. 
2. Install the Repeating Shapes extension onto your hard drive by double-clicking on the file 
repeat_shapes_10.exe (available at 
http://www.jennessent.com/downloads/repeat_shapes_10.zip, or from a link on the page 
http://www.jennessent.com/arcgis/repeat_shapes.htm) and following the instructions.  This 
installation routine will install the Repeating Shapes DLL and several ancillary files on your 
hard drive, but will not register the tools with ArcGIS. 
3. Use Windows Explorer to open your installation folder (if you used the default values, then 
this folder will be located at “Program Files\Jennessent\repeating_shapes\”.  This folder will 
also include some additional files and this manual. 
 
4. For Windows XP:  Double-click the file “Repeat_Shapes_ArcGIS_10_Installer.bat” to 
register all the tools with ArcGIS 10.0.  
For Windows 7/Vista:  Double-click the file “Repeat_Shapes_ArcGIS_10_Installer.bat” to 
register all the tools with ArcGIS 10.0.  
If the registration is successful, then you should see a “Registration Succeeded” notice. 
 
Note:  For the concerned or curious, the batch file Repeat_Shapes_ArcGIS_10_Installer.bat 
contains the following single line of text: 
"%CommonProgramFiles%\ArcGIS\bin\ESRIRegAsm.exe" /p:Desktop "repeat_shapes.dll" 
/f:"repeat_shapes.reg" 
It directs the ESRI installer ESRIRegAsm to register the extension DLL repeat_shapes.dll 
within ArcGIS, using GUID and Class ID values from the registry file repeat_shapes.reg (also 


 
4 
located in your installation directory).  Both Repeat_Shapes_ArcGIS_10_Installer.bat and 
repeat_shapes.reg may be opened and viewed using standard text editors such as Notepad 
or WordPad. 
5. Alternative Method if you do not get the “Registration Succeeded” message:  If the 
method above does not work, the reason is probably due to the “%CommonProgramFiles” 
environmental variable pointing to the wrong location, and/or Windows Vista or Windows 7 
Security settings.  The fix is to use a batch file that includes the full pathnames to 
“ESRIRegAsm.exe” and to the extension DLL and REG files.  You may edit the BAT file 
yourself, or you may use the tool Make_Batch_Files.exe (located in your installation folder) 
to create new registration and unregistration batch files that are properly formatted to your 
system.   
If using Windows XP:  Simply double-click on the file Make_Batch_Files.exe to create the 
new batch files. 
If using Windows Vista or Windows 7:  Right-click on the file Make_Batch_Files.exe and 
click “Run as Administrator” to create the new batch files. 
 
Repeat Step 4 above to register the tool in ArcGIS 10, but this time use the new BAT file 
Register_Repeating_Shapes.bat. 
Viewing the Tool: 
1) After installing Repeating Shapes, open ArcMap and then open the “Customize” window 
(either by clicking the “Customize” menu item in the “Tools” menu, or by simply double-
clicking on a blank portion of the button bar): 


 
5 
 
2) Click on the “Commands” tab and scroll down until you see the “Jenness Enterprises”  
category: 
 
3) In the “Jenness Enterprises” category, find the command named “Repeating Shapes”.  
Simply drag this command up to your button bar.  IMPORTANT:  If you want the Repeating 
Shapes button to always be available whenever you open ArcMap, make sure you have 
“Normal.mxt” selected in the bottom right corner of the dialog.  If you only want Repeating 
Shapes to be available within this particular map document, change the selection to your map 
document (which should be right under “Normal.mxt” in the drop-down box). 
4) Close the “Customize” dialog box and you will be ready to go. 


 
6 
Uninstalling Repeating Shapes Tool 
For ArcGIS 9.x. 
1) Close ArcGIS if it is open. 
2)   Click the Start button. 
3) Open your Control Panel. 
4) Double-click “Add or Remove Programs”. 
5) Scroll down to find and select “Repeating Shapes”. 
6) Click the “Remove” button and follow the directions. 
 
 
For ArcGIS 10.0 
1) Close ArcGIS if it is open. 
2) Use Windows Explorer to open your installation folder (if you used the default values, 
then this folder will be located at “Program Files\Jennessent\repeating_shapes\”.  This 
folder will also include some additional files and this manual. 


 
7 
 
3) For Windows XP:  Double-click the file Uninstall_Repeat_Shapes.bat to unregister all 
the tools with ArcGIS 10.0.   
For Windows 7/Vista:  Double-click the file Uninstall_Repeat_Shapes.bat to unregister 
all the tools with ArcGIS 10.0.   
If the unregistration is successful, then you should see an “Unregistration Succeeded” 
notice. 
 
4) Alternative Method if you do not get the "Unregistration Succeeded" message:  If 
the method above does not work, the reason is probably due to the 
"%CommonProgramFiles" environmental variable pointing to the wrong location, and/or 
Windows Vista or Windows 7 Security settings.  The fix is to use a batch file that includes 
the full pathnames to "ESRIRegAsm.exe" and to the extension DLL and REG files.  You 
may edit the BAT file yourself, or you may use the tool Make_Batch_Files.exe (located in 
your installation folder) to create new registration and unregistration batch files that are 
properly formatted to your system.   
If using Windows XP:  Simply double-click on the file Make_Batch_Files.exe to create 
the new batch files. 
If using Windows Vista or Windows 7:  Right-click on the file Make_Batch_Files.exe 
and click "Run as Administrator" to create the new batch files. 


 
8 
 
Repeat Step 3 above to unregister the tools in ArcGIS 10, but this time use the new BAT 
file Unregister_Repeating_Shapes.bat. 
5) Click the Start button. 
6) Open your Control Panel. 
7) Double-click “Add or Remove Programs”. 
8) Scroll down to find and select “Repeating Shapes 10”. 
9) Click the “Remove” button and follow the directions. 
 
 
Note:  For the concerned or curious, the batch file Uninstall_Repeat_Shapes.bat contains the 
following single line of text: 
"%CommonProgramFiles%\ArcGIS\bin\ESRIRegAsm.exe" /p:Desktop /u "repeat_shapes.dll" 


 
9 
It directs the ESRI installer ESRIRegAsm to unregister the DLL repeat_shapes.dll within ArcGIS.  
Uninstall_Repeat_Shapes.bat may be opened and viewed using standard text editors such as 
Notepad or WordPad. 
 
Troubleshooting 
If Any of the Tools Crash 
If a tool crashes, you should see a dialog that tells us what script crashed and where it crashed.  I 
would appreciate it if you could copy the text in that dialog, or simply take screenshots of the 
dialog and email them to me at jeffj@jennessent.com.  Note:  Please make sure that the line 
numbers are visible in the screenshots!  The line numbers are located on the far right side of the 
text.  Use the scrollbar at the bottom of the dialog to make the line numbers visible. 
“Object variable or With block variable not set” Error: 
If you open ArcMap and immediately see the error dialog appear with one or more error 
messages stating that “Object variable or With block variable not set”, then 90% of the time it is 
because ArcGIS was running when you installed the extension.  The “Object” variable being 
referred to is the “Extension” object, and ArcGIS only sets that variable when it is initially turned 
on. 
The solution is usually to simply close ArcGIS and restart it.  If that does not work, then: 
1) Close ArcGIS 
2) Reinstall the extension 
3) Turn ArcGIS back on. 
RICHTX32.OCX Error (also comct332.ocx, comdlg32.ocx, mscomct2.ocx, mscomctl.ocx, 
msstdfmt.dll errors): 
If you see a line in the error dialog stating: 
Component 'RICHTX32.OCX' or one of its dependencies not correctly registered: a file is 
missing or invalid 
Or if you see a similar error stating that one or more of the files comct332.ocx, comdlg32.ocx, 
mscomct2.ocx, mscomctl.ocx  or msstdfmt.dll are missing or invalid, then simply follow the 
instructions for RICHTX32.OCX below, but substitute the appropriate file for RICHTX32.OCX. 
This error is almost always due to the fact that new installations of Windows 7 and Windows Vista 
do not include a file that the extension expects to find.  For example, the file “richtx32.ocx” is 
actually the “Rich Text Box” control that appears on some of the extension dialogs.  The other 
files refer to other common controls that might appear on the various extension dialogs. 
The solution is to manually install the missing file (richtx32.ocx) yourself.  Here is how to do it: 
1) Open Windows Explorer and locate the file richtx32.ocx in your extension installation file. 
2) If you are running a 32-bit version of Windows, then copy richtx32.ocx to the directory 
C:\Windows\System32\ 
If you are running a 64-bit version of Windows, then copy richtx32.ocx to the directory 
C:\Windows\SysWOW64\ 
3) Open an “Elevated Command Prompt” window.  This is the standard Windows Command 
Prompt window, but with administrative privileges enabled.  You need these privileges 
enabled in order to register the OCX with Windows.  Note:  The Elevated Command 
Prompt opens up in the “..\windows\system32” directory, not the “..\Users\[User Name]” 
directory.  The window title will also begin with the word “Administrator:” 


 
10
 
a. Method 1:  Click the “Start” button, then “All Programs”, then “Accessories” and then 
right-click on “Command Prompt” and select Run as Administrator. 
b. Method 2:  Click the “Start” button, and then click on the “Search Programs and 
Files” box.  Type “cmd” and then click CONTROL+SHIFT+ENTER to open the 
Command window with Administrator privileges. 
 
For more help on opening an Elevated Command Prompt, please refer to: 
http://www.sevenforums.com/tutorials/783-elevated-command-prompt.html 
http://www.winhelponline.com/articles/158/1/How-to-open-an-elevated-Command-
Prompt-in-Windows-Vista.html 
Or simply do a search for “Elevated Command Prompt”. 
4) Register the file richtx32.ocx using the Windows RegSvr function: 


 
11
a. If using a 32-bit version of Windows, type the line 
regsvr32.exe c:\windows\system32\richtx32.ocx 
 
b. If using a 64-bit version of Windows, type the line 
regsvr32.exe %windir%\syswow64\richtx32.ocx 
 
c. Click [ENTER] and you should see a message that the registration succeeded.  
 


 
12
General Instructions 
Choose the Region of Interest:   
Click the 
 button and choose your region of interest: 
 
The first option, “With Respect to Selected Features in a Theme”, will generate shapes that will 
completely cover all the selected features in some point, line or polygon theme.  The other three 
options will generate shapes that completely cover some rectangular area encompassing either a 
single theme, all the themes in the view, or the visible extent in the view. 
With Respect to Selected Features in a Feature Layer: 
This option will generate shapes that completely cover all the selected features in a feature layer.  
You will be asked which feature theme to use: 


 
13
 
If you choose a theme with no records selected, then you will have the option to either generate 
shapes over all features or go back and choose another theme: 
 


 
14
Within the Extent of a Particular Layer: 
This option will generate shapes that completely cover the entire rectangular area that 
encompasses your layer.  You will be asked with layer to use, and you are not restricted to 
feature layers for this function: 
 
Within the Extent of All Layers in the Map: 
This option will cover all the themes in your view; essentially equal to the rectangular region that 
you see when you click the “Zoom to Full Extent” button 
. 
Within the Extent of the Display: 
This option will use cover the entire visible region within your map display. 
Choose the Shape Type to Create 
You have seven options for shape type and arrangement.  Points and circles may be generated 
in either a square or triangular pattern.  Squares, triangles and hexagons will completely cover 
the region of interest.  All options can be oriented in any direction. 
 


 
15
 
Set Shape Parameters: 
All options have several parameters relating to size, spacing and orientation of shapes.  The 
directions and size values are based on your map spatial reference (i.e. projection and datum).  If 
your map has no projection set, then the direction and size values will be based on the first layer 
in the map.   
Polygon feature classes will include an Area field, and point feature classes will include X- and Y-
coordinate fields. 
Generating Points in a Square Pattern: 
This option generates an array of points lined up in rows and columns, and oriented in any 
direction you choose.  If you found the 4 closest points to some random location within the array, 
those 4 closest points would form a square. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with perfectly vertical and 
horizontal rows and columns.  An offset value of either 0º or 90º will produce vertical and 
horizontal rows and columns, and you can enter any value within this range. 


 
16
 
TIP:  If you wish to use values of 0º, 22.5º, 45º or 67.5º, you can automatically enter those values 
by clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 90º, simply click the “Randomize” button. 
Generating Points in a Triangular Pattern: 
This option generates an array of points lined up in 3 general directions and oriented in any 
direction you choose.  If you found the 3 closest points to some random location within the array, 
those 3 closest points would form an equilateral triangle. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array with one perfectly 
horizontal orientation.  An offset value of either 0º or 60º will produce an array with one horizontal 
row of points, and you can enter any value within this range. 
 


 
17
TIP:  If you wish to enter values of 0º, 15º, 30º or 45º, you can automatically enter those values by 
clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 60º, simply click the “Randomize” button. 
Generating Circles in a Square Pattern: 
This option generates an array of circular polygons lined up in rows and columns, and oriented in 
any direction you choose.  If you found the 4 circle centerpoints that are closest to some random 
location within the array, those 4 points would form a square.  These circles may overlap and/or 
may fail to cover the entire region, depending on the size parameters you enter. 
You must specify the size of the circles.  Circle size may be defined in terms of area, radius, 
diameter or circumference.  If you enter a value for any one of these, the other 3 will fill in 
automatically. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array with perfectly 
vertical and horizontal rows and columns.  An offset value of either 0º or 90º will produce an array 
with vertical and horizontal circles, and you can enter any value within this range. 
 
TIP:  If you wish to enter values of 0º, 22.5º, 45º or 67.5º, you can automatically enter those 
values by clicking on the illustrations below the text box.  If you wish to generate a random 
orientation between 0º and 90º, simply click the “Randomize” button.  
Generating Circles in a Triangular Pattern: 
This option generates an array of circular polygons lined up in 3 general directions, and oriented 
in any direction you choose.  If you found the 3 circle centerpoints closest to some random 


 
18
location within the array, those 3 points would form an equilateral triangle.  These circles may 
overlap and/or may fail to cover the entire region, depending on the size parameters you enter.  
You must specify the size of the circles.  Circle size may be defined in terms of area, radius, 
diameter or circumference.  If you enter a value for any one of these, the other 3 will fill 
automatically. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array with one perfectly 
horizontal orientation.  An offset value of either 0º or 60º will produce an array with one horizontal 
row of circles, and you can enter any value within this range. 
 
TIP:  If you wish to enter values of 0º, 15º, 30º or 45º, you can automatically enter those values by 
clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 60º, simply click the “Randomize” button.  
Generating Squares: 
This option generates an array of adjacent square polygons, arranged so that they line up in rows 
and columns and cover the entire region of interest, and are oriented in any direction you choose. 
You must specify the size of the squares.  Square size may be defined in terms of area or edge 
length.  If you enter a value for either of these, the other value will fill automatically. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array with perfectly 
vertical and horizontal rows and columns.  An offset value of either 0º or 90º will produce an array 
with vertical and horizontal squares, and you can enter any value within this range. 


 
19
 
TIP:  If you wish to enter values of 0º, 22.5º, 45º or 67.5º, you can automatically enter those 
values by clicking on the illustrations below the text box.  If you wish to generate a random 
orientation between 0º and 90º, simply click the “Randomize” button.  
Generating Rectangles: 
This option generates an array of adjacent rectangular polygons, with an option to offset adjacent 
rows by a specified percentage of the rectangle edge length.  An offset percentage of either 0% 
or 100% will produce an array of rectangles arranged in both rows and columns.  Any other value 
will cause each consecutive row of rectangles to be shifted by the specified percentage of the 
specified Edge 1 Length value.  The final array of rectangles will cover the entire region of interest 
and will be oriented in any direction you choose. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array with perfectly 
horizontal rows.  An offset value of either 0º or 180º will produce an array with horizontal rows of 
rectangles, and you can enter any value within this range. 


 
20
 
TIP:  If you wish to enter values of 0º, 45º, 90º or 135º, you can automatically enter those values 
by clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 180º, simply click the “Randomize” button.  
Generating Triangles: 
This option generates an array of equilateral triangular polygons arranged so that they cover the 
entire region of interest, and are oriented in any direction you choose.  
You must specify the size of the triangles.  Triangle size may be defined in terms of area, edge 
length or height.  If you enter a value for any one of these, the other 2 will fill automatically. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array in which one edge 
of the triangles is perfectly horizontal.  An offset value of either 0º or 60º will produce an array 
with one horizontal edge on the triangles, and you can enter any value within this range. 


 
21
 
TIP:  If you wish to enter values of 0º, 15º, 30º or 45º, you can automatically enter those values by 
clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 60º, simply click the “Randomize” button.  
Generating Hexagons: 
This option generates an array of hexagonal polygons arranged so that they cover the entire 
region of interest, and are oriented in any direction you choose.  
You must specify the size of the hexagons.  Hexagon size may be defined in terms of area, edge 
length, width or diameter.  If you enter a value for any one of these, the other 3 will fill 
automatically. 
You must specify the general orientation of the array.  The “Degrees Offset” value in the dialog 
below refers to the general orientation of the array in comparison with an array in which one edge 
of the hexagons is perfectly horizontal.  An offset value of either 0º or 60º will produce an array 
with one horizontal edge on the triangles, and you can enter any value within this range. 


 
22
 
TIP:  If you wish to enter values of 0º, 15º, 30º or 45º, you can automatically enter those values by 
clicking on the illustrations below the text box.  If you wish to generate a random orientation 
between 0º and 60º, simply click the “Randomize” button.  
As soon as the process finishes, the extension will generate a short report describing what it has 
done: 


 
23
 
General Notes: 
Stopping the Process:  At any point during the computations you may cancel the process by 
clicking on the “Stop” button at the bottom right corner of the progress meter dialog.  This should 
stop the process within approximately 1 second.  This may be useful to you if you, like the author, 
accidentally enter a size value in “degrees” while forgetting that the view is currently projected, 
and therefore causing the extension to attempt to generate a new feature class with trillions of 
shapes. 
 


 
24
Updates 
 
Version 1.5.107:  July 26, 2009:   
o 
Added functions to save to file and personal geodatabases 
o 
Added functions to show progress at various points in the analysis 
o 
Multiple minor bug fixes, speed enhancements and modifications 
o 
Added buttons to dialogs to open manual 
 
Version 1.5.123:  October 24, 2010 
o 
Multiple minor bug fixes, speed enhancements and modifications 
o 
Added ArcGIS 10 installation functions  
 
Version 1.5.131:  November 6, 2010 
o 
Added function to generate rectangles. 
o 
Fixed a bug in which it was clearing the selection of the layer used to determine the 
extent for the new repeating shapes layer. 
 
Version 1.5.131:  March 14, 2011 
o 
Added additional ArcGIS 10 registration instructions to manual to handle Windows 
7/Vista and Windows 32-bit/64-bit issues.  
 
Version 1.5.138:  August 4, 2011 
o 
Corrected an error in the Hexagon Generator code in which it the hexagons were too 
small if the user had specified the size according to the hexagon diameter.  
Specifically the code would generate hexagons with an edge size equal to half the 
hexagon width, rather than half the hexagon diameter. 
o 
Added a Tool Version label to the first dialog.  
 
Version 1.5.141: January 16, 2012 
o 
Corrected a bug in which the “With respect to Selected Features” option would result 
in a new feature class which covered the entire rectangular extent of the selected 
features.  
 
Version 1.5.147: February 20, 2012 
o 
Corrected a bug in which it was reporting some intermediate variables in message 
boxes.  These were debugging messages intended for the author, and not intended 
for the online version. 
o 
This version also replaces an outdated version of the DLL which somehow got on the 
website.  
 
Version 1.5.151: August 13, 2012 
o 
Fixed an error in which the progress meter report textbox would get too much text, 
triggering an “Invalid Property Value” error.  This revision uses a RichTextBox control 
instead of a TextBox control. 
 
Version 1.5.152: November 4, 2012 
o 
Fixed an error that caused a crash when the tool encountered a feature layer without 
a feature class. 
 
Enjoy! Please contact the author if you have problems or find bugs.  
 
Jeff Jenness 
 
 
 
jeffj@jennessent.com 
 
Jenness Enterprises  
 
 
http://www.jennessent.com  
 
3020 N. Schevene Blvd.  
 
(928) 607-4638  


 
25
 
Flagstaff, AZ  86004  
 
USA  
Updates to this extension and an on-line version of this manual are available at  
http://www.jennessent.com/arcgis/repeat_shapes.htm  
 
Please visit Jenness Enterprises ArcGIS Tools site for more ArcGIS tools and other software by 
the author.  We also offer GIS consultation services for both ArcGIS and ArcView 3.x to help you 
meet your specific data analysis and application development needs. 
 
