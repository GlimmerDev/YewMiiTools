@ECHO OFF
CHOICE /C YN /M "Is this for the Wii U Version? [y = Wii U|n = Switch]: "
IF ERRORLEVEL 2 goto switch
IF ERRORLEVEL 1 GOTO wiiu
:switch
for /D %%d in ("%cd%\Npc_*") do (
    echo.
    echo Proccessing %%~nd ...
    %cd%\tools\BotwUnpacker.exe /b %%d temp.out.pack
    %cd%\tools\BotwUnpacker.exe /bs %%d temp.out.pack
    %cd%\tools\BotwUnpacker.exe /e temp.out.pack %%~nd.out.sbactorpack
    echo.
    echo Built pack to %%~nd.out.sbactorpack
    del temp.out.pack
    goto finish
)

:wiiu
for /D %%d in ("%cd%\Npc_*") do (
    echo.
    echo Proccessing %%~nd ...
    %cd%\tools\BotwUnpacker.exe /b %%d temp.out.pack
    %cd%\tools\BotwUnpacker.exe /e temp.out.pack %%~nd.out.sbactorpack
    echo.
    echo Built pack to %%~nd.out.sbactorpack
    del temp.out.pack
)

:finish
