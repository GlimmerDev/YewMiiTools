# YewMiiTools
Tool to simplify conversion between Mii and TLoZ:BoTW's UMii. At the moment, it's still a few steps, but I plan to combine some of these steps to make it even easier.

## Usage
1. Place desired NPC .sbactorpack file(s) from extracted game files into YewMiiTools folder. These can be found in /romfs/Actor/Pack/, see here for NPC names: https://gbatemp.net/threads/botw-item-names-for-pandaonsmacks-trainer.463959/
2. Place your 3DS/WiiU format .mii file(s) into YewMiiTools folder.
3. Run "extract_sbactorpack.bat" to extract all sbactorpack files.
4. Run "mii_to_umii.bat" and follow on-screen instructions. First, drop the extracted NPC directory (or type/paste it in). Then, drop (or type/paste) the Mii file you wish to inject. 
5. The script should run and generate "FinalResult.bumii". This is the finished injected UMii.
6. Copy the FinalResult.bumii into the extracted NPC folder you wish to replace, and rename it to match the NPC's UMii file. (Example, /Npc_HatenoVillage001/Actor/UMii/Npc_HatenoVillage001.bumii)
7. Run "build_sbactorpack.bat" to rebuild the NPC folders. It will prompt you to specify whether you use the Wii U or Switch version.
8. The script will generate "OriginalNPCName.out.sbactorpack". This is your final file that can be put back into the gamefiles or loaded with LayeredFS.

