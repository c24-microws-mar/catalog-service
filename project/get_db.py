url = "http://musicbrainz.org/ws/2/release?query={}&limit=50&fmt=json"
cover_url_temp = 'http://coverartarchive.org/release/{}'
import requests
import json
import string
import random
albums = []

for word in ['offspring', 'britney', 'baby', 'metal', 'house', 'dance','hot']:#string.ascii_lowercase[0:3]:
	print word
	out = requests.get(url.format(word))
	data  = json.loads(out.text)
	if 'releases' in data:
		print('nmatches {}'.format(len(data['releases'])))
		for album in data['releases']:
			alb = { 'album': album['title'],
				'albumId': album['id'],
				'artist': album['artist-credit'][0]['artist']['name'],
				'artistId': album['artist-credit'][0]['artist']['id'],
				'price': random.randint(10,15),
}	    
			cover = requests.get(cover_url_temp.format(alb['albumId']))
			cover_url = 'NOT FOUND'
			has_cover = False
			print('.')
			if cover.ok:
				cdata = json.loads(cover.text)
				try:
					cover_url = cdata['images'][0]['thumbnails']['large'] 
					has_cover = True
				except:
					cover_url = 'FAILED'
					pass

			alb['coverUrl'] = cover_url 
			alb['hasCover'] = has_cover

			albums.append(alb)

print('generated {} elems'.format(len(albums)))
with open('database.json', 'w') as f:
	json.dump(albums, f, indent=4)
