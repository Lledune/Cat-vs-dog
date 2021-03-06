import os 
import pathlib
from pathlib import Path
from fastbook import search_images_bing, download_url, Image
path = "/home/lucien/Desktop/Repos/cat_vs_dog"
#Change API key here by BING SEARCH api key 
key = os.environ.get('AZURE_SEARCH_KEY', 'f41e130be326403780e49014b672175d')

#Getting images from bing for cats and dogs 
cats = search_images_bing(key, 'cat')
ims = cats.attrgot('contentUrl')

#Test to look at one image 
dest = path + '/images/cats/cat.jpg'
download_url(ims[0], dest)
im = Image.open(dest)
im.to_thumb(128,128)

#Downloading images of cats, dogs, rabbits 

names = "cat", "dog", "rabbit"
path = Path(path + '/images/')
if not path.exists():
    path.mkdir()
    for o in names: 
        dest = (path/o)
        dest.mkdir(exist_ok = True)
        results = search_images_bing(key, o)
        download_images(dest, urls = results.attrgot('contentUrl'))