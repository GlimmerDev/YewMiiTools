@echo OFF
set /p npc="Enter NPC directory (or drag and drop): "
set /p mii="Enter Mii file name: "

copy "%mii%" "tools\temp.mii"
copy "%npc%\Actor\UMii\" tools\
cd tools
rename *.bumii temp.bumii
aampTool.exe temp.bumii
yewmiiconv.py temp.mii temp.bumii.xml FinalResult.bumii.xml
aampTool.exe FinalResult.bumii.xml
move FinalResult.bumii.aamp "..\FinalResult.bumii"
del temp.*
del FinalResult.*
cd ..