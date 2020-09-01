# MediaRenamer

**DISCLAIMER: I developed this tool as one of my first Python projects, as it may be very buggy and incomplete.**

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

- Script will now rename files and output logs (if enabled) to the log-file defined in 