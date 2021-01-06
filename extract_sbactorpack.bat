@ECHO OFF
if EXIST Npc_*.sbactorpack (
    for %%f in (Npc_*.sbactorpack) do (
        echo %%~nf
        %cd%\tools\BotwUnpacker.exe /d %%f temp.bactorpack
        %cd%\tools\BotwUnpacker.exe /u temp.bactorpack %%~nf
    )
    del temp.bactorpack
) ELSE (
    echo.
    echo No NPC packs found! Place .sbactorpack files in this folder first.
)