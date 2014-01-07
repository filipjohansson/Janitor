Janitor
=====
Watch your media in Plex and let Janitor delete them from your hard drive when you are done.

### The problem
Plex is great at managing and ordering my media, but lets face it; most of the movies and shows I watch I never ever want to see again. Wouldn't it be nice if Plex could delete the files from my hard drive after I'm done watching them?

### The solution
Janitor!

## Requirements
* Python
* [Plex Media Server](https://plex.tv/downloads)

## Usage
Run:
    python janitor.py

## Settings
Name | Values | Description
--- | --- | ---
Delete | True or False | If set to false, no files will be deleted. Great for testing what the script actually does
PlexServerIP | Address | The address to the Plex Media Server
PlexServerPort | Port | The port the Plex Media Server is running on
ScanInterval | Time in minutes | Sets the scan interval, standard is every 6 hours
Movies | List | A list of movies that you don't want Janitor to remove
Shows | List | A list of shows that you don't want Janitor to remove

## Contribute
This is my first Python application and I'm still learning so please feel free to send pull requests.
