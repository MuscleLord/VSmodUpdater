"""
 _____                                       _____ 
( ___ )-------------------------------------( ___ )
 |   |                                       |   | 
 |   | __     ______                      _  |   | 
 |   | \ \   / / ___| _ __ ___   ___   __| | |   | 
 |   |  \ \ / /\___ \| '_ ` _ \ / _ \ / _` | |   | 
 |   |   \ V /  ___) | | | | | | (_) | (_| | |   | 
 |   |    \_/  |____/|_| |_| |_|\___/ \__,_| |   | 
 |___|                                       |___| 
(_____)-------------------------------------(_____)
"""

import requests
import asyncio
import json
import os
import wget
import zipfile
import sys, io
import ctypes
import time
from bs4 import BeautifulSoup as bs
from logger import Error, Events

from logo_ascii import LogoAscii

# import re
# from urllib.parse import urlparse, urlencode, parse_qsl


class bcolors:

    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"
    ITALIC = "\x1b[3m"
    UNDERLINE = "\x1b[4m"
    INVERSE = "\x1b[7m"
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"
    GRAY = "\x1b[90m"
    BRIGHT_RED = "\x1b[91m"
    BRIGHT_GREEN = "\x1b[92m"
    BRIGHT_YELLOW = "\x1b[93m"
    BRIGHT_BLUE = "\x1b[94m"
    BRIGHT_MAGENTA = "\x1b[95m"
    BRIGHT_CYAN = "\x1b[96m"
    BRIGHT_WHITE = "\x1b[97m"
    BG_BLACK = "\x1b[40m"
    BG_RED = "\x1b[41m"
    BG_GREEN = "\x1b[42m"
    BG_YELLOW = "\x1b[43m"
    BG_BLUE = "\x1b[44m"
    BG_MAGENTA = "\x1b[45m"
    BG_CYAN = "\x1b[46m"
    BG_WHITE = "\x1b[47m"
    BG_GRAY = "\x1b[100m"
    BG_BRIGHT_RED = "\x1b[101m"
    BG_BRIGHT_GREEN = "\x1b[102m"
    BG_BRIGHT_YELLOW = "\x1b[103m"
    BG_BRIGHT_BLUE = "\x1b[104m"
    BG_BRIGHT_MAGENTA = "\x1b[105m"
    BG_BRIGHT_CYAN = "\x1b[106m"
    BG_BRIGHT_WHITE = "\x1b[107m"
    colors = {
        "reset": "\x1b[0m",
        "bold": "\x1b[1m",
        "italic": "\x1b[3m",
        "underline": "\x1b[4m",
        "inverse": "\x1b[7m",
        "black": "\x1b[30m",
        "red": "\x1b[31m",
        "green": "\x1b[32m",
        "yellow": "\x1b[33m",
        "blue": "\x1b[34m",
        "magenta": "\x1b[35m",
        "cyan": "\x1b[36m",
        "white": "\x1b[37m",
        "gray": "\x1b[90m",
        "bright_red": "\x1b[91m",
        "bright_green": "\x1b[92m",
        "bright_yellow": "\x1b[93m",
        "bright_blue": "\x1b[94m",
        "bright_magenta": "\x1b[95m",
        "bright_cyan": "\x1b[96m",
        "bright_white": "\x1b[97m",
        "bg_black": "\x1b[40m",
        "bg_red": "\x1b[41m",
        "bg_green": "\x1b[42m",
        "bg_yellow": "\x1b[43m",
        "bg_blue": "\x1b[44m",
        "bg_magenta": "\x1b[45m",
        "bg_cyan": "\x1b[46m",
        "bg_white": "\x1b[47m",
        "bg_gray": "\x1b[100m",
        "bg_bright_red": "\x1b[101m",
        "bg_bright_green": "\x1b[102m",
        "bg_bright_yellow": "\x1b[103m",
        "bg_bright_blue": "\x1b[104m",
        "bg_bright_magenta": "\x1b[105m",
        "bg_bright_cyan": "\x1b[106m",
        "bg_bright_white": "\x1b[107m",
    }


class TerminalColorTheme:
    def __init__(self, bg: str, fg: str):
        super().__init__()
        """
            0 = Black       8 = Gray
            1 = Blue        9 = Light Blue
            2 = Green       A = Light Green
            3 = Aqua        B = Light Aqua
            4 = Red         C = Light Red
            5 = Purple      D = Light Purple
            6 = Yellow      E = Light Yellow
            7 = White       F = Bright White
        """
        combined = f"{bg}{fg}"
        os.system(f"color {combined}")


class TextColor:
    RESET = "\x1b[0m"
    BOLD = "\x1b[1m"
    ITALIC = "\x1b[3m"
    UNDERLINE = "\x1b[4m"
    INVERSE = "\x1b[7m"
    BLACK = "\x1b[30m"
    RED = "\x1b[31m"
    GREEN = "\x1b[32m"
    YELLOW = "\x1b[33m"
    BLUE = "\x1b[34m"
    MAGENTA = "\x1b[35m"
    CYAN = "\x1b[36m"
    WHITE = "\x1b[37m"
    GRAY = "\x1b[90m"
    BRIGHT_RED = "\x1b[91m"
    BRIGHT_GREEN = "\x1b[92m"
    BRIGHT_YELLOW = "\x1b[93m"
    BRIGHT_BLUE = "\x1b[94m"
    BRIGHT_MAGENTA = "\x1b[95m"
    BRIGHT_CYAN = "\x1b[96m"
    BRIGHT_WHITE = "\x1b[97m"
    BG_BLACK = "\x1b[40m"
    BG_RED = "\x1b[41m"
    BG_GREEN = "\x1b[42m"
    BG_YELLOW = "\x1b[43m"
    BG_BLUE = "\x1b[44m"
    BG_MAGENTA = "\x1b[45m"
    BG_CYAN = "\x1b[46m"
    BG_WHITE = "\x1b[47m"
    BG_GRAY = "\x1b[100m"
    BG_BRIGHT_RED = "\x1b[101m"
    BG_BRIGHT_GREEN = "\x1b[102m"
    BG_BRIGHT_YELLOW = "\x1b[103m"
    BG_BRIGHT_BLUE = "\x1b[104m"
    BG_BRIGHT_MAGENTA = "\x1b[105m"
    BG_BRIGHT_CYAN = "\x1b[106m"
    BG_BRIGHT_WHITE = "\x1b[107m"

    # use inside another string
    @classmethod
    def FromRGB(clr, _R: int, _G: int, _B: int):
        return f"\033[38;2;{_R};{_G};{_B}m"

    @classmethod
    def BackGround_FromRGB(clr, _R: int, _G: int, _B: int):
        return f"\033[48;2;{_R};{_G};{_B}m"

    # For use separate from string
    @classmethod
    def PrintRGB(clr, _R: int, _G: int, _B: int):
        print(f"\033[38;2;{_R};{_G};{_B}m")

    @classmethod
    def CReset(clr):
        return f"\033[0m"

    @classmethod
    def ResetP(clr):
        print(f"\033[0m")


class VSmodUpdater:
    #######################
    def __init__(self):

        TerminalColorTheme("0", "7")
        self.ENCODING_STR = "utf-8"
        ctypes.windll.kernel32.SetConsoleTitleW("VSmodUpdater")
        # sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding=self.ENCODING_STR)
        self.HOME_URL = "https://mods.vintagestory.at/"
        ###### API's ######
        self.MAIN_API = "http://mods.vintagestory.at/api"
        self.MOD_API = f"{self.MAIN_API}/mod/"
        self.PATH_OUT = ".\\output"

        self.modlist = None
        self.mod_info_list = []
        self.new_changes = []
        self.modpath = None
        self.terminalSize(125, 70)
        os.system("cls")
        Events("Starting up...")

    def Run(self):
        TerminalColorTheme("0", "7")
        print(LogoAscii.text)
        Events("Writing logo to console.")
        # with open("ascii.txt", "r", encoding="unicode-escape") as logostr:
        #  print(logostr.read())
        self.Handle_dirs()

        self.CheckDirForMods()

        asyncio.run(self.CheckForUpdates())

    def terminalSize(self, col: int, row: int):
        cmd = f"mode {col},{row}"
        os.system(cmd)
        Events("Making changes to termianl size.")

    def separator(self, _chr: str, _count: int, _flush=True):
        print(f"{_chr * _count}", flush=_flush)

    """
    CHANGELOG_API = f"{MAIN_API}/changelogs/"  # eg: http://mods.vintagestory.at/api/changelogs/4405  <--  [assetid]=4405
    TAGS_API = f"{MAIN_API}/tags"
    SEARCH_MOD_API = f"{MAIN_API}/mods?"

    SEARCH_PARAMS_QUERY = {
        "tagids[]": "",
        "gameversion": "",
        "gameversions[]": "",
        "author": "",
        "text": "",
        "orderby": "",
        "orderdirection": "",
    }

    SEARCH_PARAMS_QUERY["tagids[]"] = "7"
    SEARCH_PARAMS_QUERY["gameversion"] = "239"
    SEARCH_PARAMS_QUERY["gameversions[]"] = ""
    SEARCH_PARAMS_QUERY["author"] = ""
    SEARCH_PARAMS_QUERY["text"] = ""
    SEARCH_PARAMS_QUERY["orderby"] = "lastreleased"
        # Order by, one of: 'asset.created', 'lastreleased', 'downloads', 'follows', 'comments', 'trendingpoints' (default: asset.created)
    SEARCH_PARAMS_QUERY["orderdirection"] = ""
        # Order direction, one of: 'desc', 'asc' (default: desc)


    sorted_params_dict = {}

    for item in SEARCH_PARAMS_QUERY.items():
        if item[1] == "":
            print("empty")
        else:
            sorted_params_dict.update(dict({item[0]: item[1]}))
            print(sorted_params_dict)

    urls_parsed = urlparse(SEARCH_MOD_API)
    query = dict(parse_qsl(urls_parsed.query))
    query.update(sorted_params_dict)
    new_url = urls_parsed._replace(query=urlencode(query, safe="[]")).geturl()
    print(new_url)
    mods_sres = requests.get(new_url, timeout=60)
    print(json.dumps(mods_sres.json(), indent=2))
    """

    #########################
    def Handle_dirs(self):

        curr_path = os.path.dirname(os.path.abspath(__file__))
        # print(curr_path)
        if not os.path.isfile(".\\modsdir.txt"):
            f = open(".\\modsdir.txt", "w+", encoding=self.ENCODING_STR)
            mods_dir = input("What is your mod directory? ")
            f.write(mods_dir)
            f.close
            Events("Made new file 'modsdir.txt'")

        f = open(".\\modsdir.txt", "r", encoding=self.ENCODING_STR)

        if f.read() == "":
            f.close()
            f = open(".\\modsdir.txt", "w", encoding=self.ENCODING_STR)
            mods_dir = input("What is your mod directory? ")
            f.write(mods_dir)
            f.close()
            Events("No directory path specified in 'modsdir.txt'")

        f.close()

        f = open(".\\modsdir.txt", "r", encoding=self.ENCODING_STR)
        self.modpath = f.read()
        f.close()

        if not os.path.isdir(self.PATH_OUT):
            os.mkdir(self.PATH_OUT)
            print("Creating output directory", flush=True)
            Events("Created output directory")

        self.modlist = os.listdir(self.modpath)
        check_zipcount = 0
        for mz in self.modlist:
            if mz.endswith(".zip"):
                check_zipcount += 1
        # print(check_zipcount)
        if check_zipcount <= 0:
            print(
                f"{TextColor.YELLOW}No mods found in your folder...\n{TextColor.RESET}"
            )
            Events("No mods where found in your folder.")
            input("Press Enter to exit")
            exit()

    def CheckDirForMods(self):
        # TextColor.PrintRGB(128, 200, 134)

        print("\nMods in your folder: \n", flush=True)
        Events("Checking folder for mods...")
        print(TextColor.BRIGHT_BLUE, flush=True)
        for mod in self.modlist:
            # Get modinfo.json data inside local mod-zipfile
            if mod.endswith(".zip"):
                get_zip = zipfile.ZipFile(os.path.join(self.modpath, mod), mode="r")
                with get_zip.open("modinfo.json", mode="r") as mod_info:
                    mod_info_content = mod_info.read().decode(self.ENCODING_STR)
                    # print(mod_info_content)
                    try:

                        mod_info_json = json.loads(mod_info_content.lower())

                        if "name" in mod_info_json:
                            self.mod_info_list.append(mod_info_json)
                            print(mod_info_json["name"], flush=True)
                            Events(f'Found mod: {mod_info_json["name"]}')
                        else:
                            Error("Key 'name' was not found in mod_info_json")
                            print(
                                "Key 'name' was not found in mod_info_json", flush=True
                            )
                    except json.decoder.JSONDecodeError as e:
                        print(f"Error parsing JSON for {mod}: {e}", flush=True)
                        Error(f"Error parsing JSON for {mod}: {e}")
                    except Exception as e:
                        print(e)
                        Error(e)
        print(TextColor.RESET, flush=True)

        self.separator("_", 50)

    async def CheckForUpdates(self):
        doFlush = False
        Events("Checking for updates...")
        print("\nChecking for updates...\n", flush=True)
        await asyncio.sleep(2)
        for mod in self.mod_info_list:

            # Get new mod info data from database to check version
            # print(mod.keys())
            if "modid" in mod:
                try:
                    API_REQ = f"{self.MOD_API}{str(mod['modid'])}"
                    mod_res = requests.get(
                        API_REQ, headers={"Accept": "application/json"}, timeout=60
                    )

                    res_modinfo = mod_res.json()["mod"]
                    asset_id = res_modinfo["assetid"]
                    releases = res_modinfo["releases"][0]
                    if releases["modversion"] != mod["version"]:
                        self.separator("_", 50, doFlush)
                        self.separator("#", 50, doFlush)

                        print(
                            f"\n{TextColor.GREEN}{mod['name']}{TextColor.RESET} has a newer version!",
                            flush=doFlush,
                        )
                        Events(f"{mod['name']} has a newer version!")
                        self.new_changes.append("x")
                        try:
                            # Pull data from HTML at the mod website for changelog. API don't serve specifics in it for that as it seems for now.
                            MOD_URL = f"{self.HOME_URL}{str(mod['modid'])}"
                            mod_changelog_res = requests.get(MOD_URL, timeout=60)

                            CHLOG_NAME = "changelogtext"
                            # regex = r""
                            # for m in CHLOG_NAME:
                            #    regex = regex + r"[\_\-\.'\!\s]*" + m
                            # regex = regex + r"[\_\-\.'\!\s]*"

                            # html_chname = mod_changelog_res.text.strip(" _-.'!")  # useless!?
                            url_chname = bs(
                                mod_changelog_res.text, features="html.parser"
                            )
                            # print(url_chname)
                            # search in html for '<div class="changelogtext">' tags.
                            res_chname = url_chname.find_all(
                                "div",
                                class_=CHLOG_NAME,
                            )

                            chlog_text = ""
                            if len(res_chname) < 1:
                                print("no changelog found", flush=doFlush)
                                Events("No changlog where found")
                            else:
                                chlog_text = res_chname[0].get_text()
                                """
                                Get first '<div class="changelogtext">' where latest changlog text is ans extract it.
                                ex:
                                <div class="changelogtext" style="display:none;">
                                    <strong>v1.7.4</strong><br>
                                    <h3>Changelog</h3>
                                    <ul>
                                        <li>Fix Japanese translation - thanks @RikeiR.</li>
                                        <li>Fix issue when unable to place carried block</li>
                                    </ul>
                                </div>

                                """

                            ####################
                            print(
                                f"Current version= {TextColor.RED}{mod['version']}{TextColor.RESET} >>> new version= {bcolors.BRIGHT_CYAN}{releases['modversion']}{TextColor.RESET}",
                                flush=doFlush,
                            )
                            Events(
                                f"Current version= {mod['version']} >>> new version= {releases['modversion']}"
                            )
                            chlogvStr = f"{CHLOG_NAME} v{releases['modversion']}:"
                            self.separator("-", len(chlogvStr), doFlush)
                            print(TextColor.CYAN, flush=doFlush)
                            print(
                                f"ChangeLog v{releases['modversion']}:", flush=doFlush
                            )
                            Events(f"ChangeLog v{releases['modversion']}:")

                            for lines in chlog_text.splitlines():
                                if f"v{releases['modversion']}" not in lines:
                                    new_str = ""
                                    # wordwrap long lines
                                    if len(lines) > 70:
                                        sl = lines.split(" ")
                                        count = 0
                                        for words in sl:
                                            new_str += words + " "
                                            count += 1
                                            max_words_ln = 14
                                            if count == max_words_ln:
                                                new_str += "\n\t"

                                    print(f"\t{new_str}", flush=doFlush)
                                    Events(f"\t{new_str}")
                            print(TextColor.RESET, flush=doFlush)
                            self.separator("-", len(chlogvStr), doFlush)

                        except IndexError as e:
                            print("IndexError:", e, flush=doFlush)
                            Error(f"IndexError: {e}")
                        except requests.exceptions.Timeout as e:
                            print(
                                "WEB_HTML: requests.exceptions.Timeout:",
                                e,
                                flush=doFlush,
                            )
                            Error(f"WEB_HTML: requests.exceptions.Timeout: {e}")
                        except Exception as e:
                            print(e)
                            Error(e)
                        #################################
                        print(
                            f"\n{TextColor.BRIGHT_YELLOW}Downloading from:{TextColor.RESET}",
                            flush=True,
                        )
                        Events(f"Downloading from:")

                        def bar_custom(current, total, width=80):
                            progress = current / total
                            bar_width = int(width * progress)
                            bar = f"[{'=' * bar_width}{' ' * (width - bar_width)}] {progress * 100:.1f}%"
                            sys.stdout.write(f"\r{bar}")
                            sys.stdout.flush()

                        print(TextColor.BRIGHT_MAGENTA, flush=doFlush)
                        file_id = releases["fileid"]
                        downlink = f"{self.HOME_URL}download?fileid={str(file_id)}"
                        Events("url: " + downlink)
                        print(downlink, flush=True)
                        repl_str = f"{self.PATH_OUT}/"
                        """
                        wget_test = (
                            "http://speedtest.wdc01.softlayer.com/downloads/test500.zip"
                        )
                        wres = wget.download(
                            wget_test, out=None, bar=bar_custom
                        ).replace(repl_str, "")
                        """
                        response = wget.download(
                            downlink, out=self.PATH_OUT, bar=bar_custom
                        ).replace(repl_str, "")
                        Events("Downloading file: " + response)

                        print(TextColor.RESET, flush=doFlush)
                        print(
                            f"\nDone! Check output folder for file: {response}\n",
                            flush=doFlush,
                        )
                        Events(f"Done! Check output folder for file: {response}")
                        #################################
                        self.separator("#", 50, doFlush)

                        self.separator("_", 50, doFlush)
                    else:
                        print(
                            f"{TextColor.GREEN}{mod['name']}{TextColor.RESET} is the latest!",
                            flush=doFlush,
                        )
                        Events(f"{mod['name']} is the latest!")
                except KeyError as e:
                    print(e)
                    Error(e)
                except TypeError as e:
                    print(e)
                    Error(e)
                except IndexError as e:
                    print("IndexError:", e)
                    Error(f"IndexError: {e}")
                except requests.exceptions.Timeout as e:
                    print("MOD: requests.exceptions.Timeout:", e)
                    Error(f"MOD: requests.exceptions.Timeout: {e}")
                except Exception as e:
                    print(e)
                    Error(e)
            else:
                print(f"modid key does not exist for mod: {mod['name']}")
                Error(f"modid key does not exist for mod: {mod['name']}")
        self.separator("_", 50, doFlush)

        if len(self.new_changes) == 0:
            print("Everything is up to date!", flush=doFlush)
            Events("Everything is up to date!")


if __name__ == "__main__":
    app = VSmodUpdater()
    
    app.Run()

    input("\n\nDownload complete, press Enter to exit!")
    Events("Exit...")
