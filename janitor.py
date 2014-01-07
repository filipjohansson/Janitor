import os, ConfigParser, codecs, shutil
from datetime import datetime
from libs.apscheduler.scheduler import Scheduler
from libs.pyplex.server import Server

# Import settings from settings file
config = ConfigParser.ConfigParser()
config.readfp(codecs.open("settings.ini", "r", "utf8"))

# Set some basic settings variables
deleteFiles = config.getboolean('Settings', 'Delete')
plexServerIP = config.get('Settings', 'PlexServerIP')
plexServerPort = config.get('Settings', 'PlexServerPort')
scanInterval = config.getint('Settings', 'ScanInterval')

# Get the lists of movies and shows to save
moviesToSave = config.get('Save', 'Movies')
moviesToSave = moviesToSave.splitlines()
showsToSave = config.get('Save', 'Shows')
showsToSave = showsToSave.splitlines()

# Connect to Plex server
server = Server(plexServerIP, plexServerPort)

def clean():
	# Get the movies section
	sections = server.library.movies
	for section in sections:
		movies = section.getContent()

		# Loop through the movies in the section
		for movie in movies:
			if movie.viewed:
				if not (movie.title in moviesToSave):
					if (deleteFiles):
						print 'Deleted the movie', movie.title
						# Delete with this function
						shutil.rmtree(os.path.abspath(os.path.join(movie.file, os.pardir)))
					else:
						print 'Wants to delete the movie', movie.title

	# Get the shows section
	sections = server.library.shows
	for section in sections:
		shows = section.getContent()
		for show in shows:
			if not (show.title in showsToSave):
				for episode in show.getAllEpisodes():
					if episode.viewed:
						if (deleteFiles):
							print 'Deleted the episode', episode.title, 'from the show', show.title
							# Delete with this function
							os.remove(episode.file)
						else:
							print 'Wants to delete the episode', episode.title, 'from the show', show.title

scheduler = Scheduler(standalone=True)
scheduler.add_interval_job(clean, minutes=scanInterval)
print 'Hi! I\'m your new Janitor.\nMy job is to keep you place tidy and to get rid of all the old stuf you don\'t need anymore.'
if not (deleteFiles):
	print 'It seems like you don\'t want me to throw your stuff away. That is fine by me, but after giving me a test run you probably want to give me permission to throw your stuff away as well.'
print 'I will clean your place every', str(scanInterval), 'minutes. If you ever feel the need to fire me just hit Ctrl+C (please don\'t!)\nLets get down to business!\n\n'
clean()
try:
	scheduler.start()
except (KeyboardInterrupt, SystemExit):
	pass
