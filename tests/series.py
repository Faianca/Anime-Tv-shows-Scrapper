__author__ = 'jmeireles'

from scrapper.scrapper import Scrapper

testS = Scrapper()
serie = testS.get_series("http://www.animehere.com/anime/terra-formars.html")

for episod in serie['episodes']:
    print episod.title
    print testS.get_episode(episod.href)

    print "--------------------"

