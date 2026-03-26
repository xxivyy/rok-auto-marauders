
<div align="center">

### [![Python](https://img.shields.io/badge/Python-3.12-blue)]() [![License](https://img.shields.io/badge/License-AGPLv3-orange)]()

### [Introduction](#introduction) • [Usage](#usage) • [Description](#description) • [Notes](#notes) • [License](#license)

</div>

---

# Introduction

This project further automated ROK's Auto Marauder feature to fully work afk for 48 hours.

It can be used by anyone who wants to burn AP during the Marauder Stage in pre KVK.

[!!!] Use at your own risk. Botting is against the games TOS.

---

# Usage

### Ingame prerequisites:
1. Setup auto marauder marches + settings (5 march, use ap, max amount, etc).
2. Make sure auto marauder is the selected mode in barbarian search mode (barbs, forts, (marauders)), possibly start it once to lock it in. 
3. Enter your city and hit "space" or map button to get the view right over your city. This is the most optional view for the bot to work.

### Option 1: Download Release

Not available at the moment.

### Option 2: Manual Setup

Make sure CMD window is ran with **Administrator** so the inputs can be made to the game window.

1. `git clone https://github.com/xxbread/rok-auto-marauders/` & `cd rok-auto-marauders`

2. `pip install -r requirements.txt` or make sure your packages are not too outdated.

3. `python -m automarauder`

At the moment, the project is designed to be ran as a module.

### Test Case 1

Timespan: March 19, ~1:00 UTC - March 20th, ~22:00 UTC (2026)

Condition: Pre-KVK 4 , Marauder Stage , 5x Peacekeeper Marches (LVL40-LVL60) , INF & Archer Troops

Result: ~400K+ within ~45H

---

# Description

This project is about automating marauder farming for the game Rise Of Kingdoms on its PC Client. Since the developers already added an auto marauder function, it was already much easier to farm marauders. However, it still requires constant manual attention every hour or so. After around 60x barbarian kills per march, the "run" cancels and all marches return back to your city. This loses out on a lot of progress as specially during the night / when you sleep, in cases where you want to burn big amounts of AP within the 48h time window, or just want to be done with it as soon as possible. This project aims at closing that "gap" and to max out the afk factor while keeping the most amount of efficiency as possible.

---

# Notes

### [Disclaimer]

The reason for this project was personal use. The reason for publishing it was to show parts of my current code quality, and ask for criticism in regards to that. AI was only used to help autocomplete and for `move_to()` smoothing logic in `automation.py` (i am not really much of a mathematician :D) to have as much of my "own" work as possible. Thanks for your understanding, feel free to fork, suggest/criticise or use by yourself.

### [Opinion]

In my opinion, marauders are still the single best use for AP spending when considering:
1. Chaining 100k++ AP during KVK is absolute madness, unless you are either very unemployed or pay pilots to do it for you.
2. You are already spending on popups, and therefore speedups become more relevant than crystals. Up to your preference.

Based on those factors, one please make up their own conclusion on whether to prefer Marauders or KVK Barbarians. 

Optional (future) Consideration: marauders are supposed to be slightly "nerfed" and be dropping crystals in SOC, once pre-kvk moves into the kvk map. Because i do not have experience with this yet, i will not comment nor take this into consideration for now. Still its worth to be mentioned for your own conclusion.

---

# License

This project is licensed under the [GNU Affero General Public License v3.0 (AGPLv3)](https://github.com/xxbread/rok-auto-marauders/blob/main/LICENSE).
