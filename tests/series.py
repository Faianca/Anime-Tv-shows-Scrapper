__author__ = 'jmeireles'

from scrapper.scrapper import Scrapper

testS = Scrapper()
#serie = testS.get_series("http://www.animehere.com/anime/terra-formars.html")
episode = testS.get_episode("http://www.animehere.com/terra-formars-episode-10.html")
print episode

