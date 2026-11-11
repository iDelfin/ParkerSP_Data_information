# SP_Data_information
[![looking at data](https://github.com/iDelfin/ParkerSP_Data_information/actions/workflows/action_space.yml/badge.svg)](https://github.com/iDelfin/ParkerSP_Data_information/actions/workflows/action_space.yml)

## Intro
Saluton, mi estas iDelfin !!!

This project aims to achive the creation of a interactive map of the solar system and some active mission that can be found and maped.

![solar System plot](.\Result\SolarSystem\solar_sistem_plt.png)

### Current Status
The project is still in development (and I'm one person with less free time than I would like :c) and for the moment have only developed a plot of all the celectial bodies adn objects in a lis

### Future changes
You can always look at the issue page to see what are the current objectives but do feel free to create issues about what you would like to see
#### Changes to have
- Revamping the whole Class for the objects, missions and solar system
- Specific colors for planets in plot
- Diferent plots for inner and outer solar system
- Learn arcade to draw and create animation of mission and celectial objects

## Dependencies
For this proyect we use the following library to obtain the telemetry and positional information
- Coordinate Data Analysis System (CDAS) web services
  - [Web page](https://cdaweb.gsfc.nasa.gov/WebServices/REST/)
  - [pypi](https://pypi.org/project/cdasws/)

The requests are made once per day for the following celectial bodies and objects
### Celectial bodies
- Mercury
- Venuse
- Earth
- Mars
- Jupiter
- Saturn
- Uranus
- Neptun
- Pluto
### Objects
- Parker Space Probe (PSP)

After new data is reaceve from the Parker Space Probe a notification will be sent to ntfy.

## Current observations
- The Parker space probe has stoped sending new data from the `PSP_COHO1HR_MERGED_MAG_PLASMA` since april 26 2026 and don't know why
  - If you have any information about this behavior please share
