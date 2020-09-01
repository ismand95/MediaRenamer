# MediaRenamer

**DISCLAIMER: I developed this tool as one of my first Python projects, as it may be very buggy and incomplete. 
It is also very probably outside the bounds of the IMDb EULA and I can't really recommend it...**

This is a small tool to scrape meta-data of individual TV-Show seasons on IMDb and rename files in the working directory 
accordingly.

This tool is designed to rename files named after weird naming conventions usually scattered around the internet. 
Fx. "ShowMan.Derp.S01E02.Derp.mkv". This script uses regex to convert all files in the folder (within same show) to
more appropriate names - following the this naming convention: "Show Man S01E02 - Episode Name.mkv".

The script is _only_ is intended for non-pirated and legally obtained content. 

## How to use

- Before running initially set the log_enabled and if applicable log_location variables accordingly. User executing the
script needs r/w access to the log_location folder.

- Navigate to the folder containing files named like _above_ and run the script using compatible python interpreter.

- Script will ask for a url. This url is the link to the season page at IMDb - fx: https://www.imdb.com/title/tt0475784/episodes?season=3&ref_=tt_eps_sn_3

- Script will ask for an extension - this is to avoid file conflicts if there's additional files in the folder. This is 
fx. .mkv or the likes when dealing with media content.

- Script will now rename files and output logs (if enabled) to the log-file defined in 