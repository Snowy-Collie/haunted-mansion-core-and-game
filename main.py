#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ==============================================================================
# MIT License
#
# Copyright (c) 2026 Snowy Collie
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ==============================================================================

import glob
import json
import os
import sys
import urllib.request
def step(choice):
    global text
    print("\033[36m"+text[choice][0])
    l=len(text[choice][1])
    if l==0:
        return 0
    output="\033[33m"
    for i in range(l):
        output+="{}: {}\n".format(i,text[choice][1][i][0])
    line=output.count("\n")+1
    try:
        user=int(input(output+"\033[31mPlease enter your choice(0-{}): \033[34m".format(l-1)))
        sys.stdout.write(f"\033[{line}A\r\033[J") 
        sys.stdout.flush()
        if user<0 or user>=l:
            print("\033[31mInvalid choice, please try again.")
            return step(choice)
        else:
            if text[choice][1][user][0] != "None":
                print("\033[32m"+text[choice][1][user][0])
                return step(text[choice][1][user][1])
            else:
                return step(text[choice][1][user][1])
    except:
        sys.stdout.write(f"\033[{line}A\r\033[J") 
        sys.stdout.flush()
        print("\033[31mInvalid input, please try again.")
        return step(choice)

def load():
    global text
    if not os.path.exists("./games"):
        os.makedirs("./games")
    if not os.path.exists("./games/pilot_game_en.json"):
        try:
            req = urllib.request.Request("https://cshmg.acsstudio.site/games/pilot_game_en.json", headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'})
            with urllib.request.urlopen(req) as response:
                with open("./games/pilot_game_en.json", 'wb') as f:
                    f.write(response.read())
        except Exception:
            pass
    
    filelst=glob.glob("./games/*.json")
    if filelst==[]:
        print("\033[31mNo game found, please put your game in the games folder.\033[0m")
        return 0
    line=len(filelst)+1
    for i in range(len(filelst)):
        print("\033[36m{}:\033[33m {}\033[0m".format(i, os.path.basename(filelst[i])))
    game=int(input("\033[36mPlease choose a game to play(0-{}):\033[0m".format(len(filelst)-1)))
    sys.stdout.write(f"\033[{line}A\r\033[J") 
    sys.stdout.flush()
    if game<0 or game>=len(filelst):
        print("\033[31mInvalid choice, please try again.\033[0m")
        return load()
    else:
        with open(filelst[game],"r") as f:
            text=json.load(f)
        return 1

def main():
    global text
    step(0)
if __name__ == "__main__":
    print("\033[31mPlease use \033[36mPowerShell (Windows 10)\033[31m or \033[36mTERMINAL (Windows 11, Unix, Linux)\033[31m to run this program for better experience.\n\033[34m",end="")
    input("Press Enter to continue, or Ctrl+C to exit.")
    sys.stdout.write(f"\033[{2}A\r\033[J") 
    sys.stdout.flush()
    if load():
        main()