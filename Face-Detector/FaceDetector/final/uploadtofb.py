from os import listdir
from os.path import isfile, join
import facebook
import os

album_id = "491908687843533"

def main(pic_name):
  # Fill in the values noted in previous steps here
  cfg = {
    "page_id"      : "408098652891204",  # Step 1
    "access_token" : "EAAEAekZCYNhsBAJsLdO73r7dDwwo5QIMWykkhX9TkbJPyiN7ZBxE5sVtWPFSGqaYl0bZBvyZAKsVgVsGAF2vu6meNEQZBZBUNvFqeNw3yMr12KAYAvfhBFRZCZAXWmYOKhkZCmkkImBcA5rro4RLT9VUGPrEFZBLWGKmQBmXTN78ELCgZDZD"
 # Step 3
    }
  api = get_api(cfg)
  msg = open(pic_name, "rb").read()
  api.put_photo(image=msg,album_path=album_id  + "/photos" )
  

def get_api(cfg):
  graph = facebook.GraphAPI(cfg['access_token'])
  # Get page token to post as the page. You can skip 
  # the following if you want to post as yourself. 
  resp = graph.get_object('me/accounts')
  page_access_token = None
  for page in resp['data']:
    if page['id'] == cfg['page_id']:
      page_access_token = page['access_token']
  graph = facebook.GraphAPI(page_access_token)
  return graph
  # You can also skip the above if you get a page token:
  # http://stackoverflow.com/questions/8231877/facebook-access-token-for-pages
  # and make that long-lived token as in Step 3

if __name__ == "__main__":
	allfiles = [f for f in listdir("./") if isfile(join("./", f))]
	code = '#uploaded#'
	for i in allfiles:
    		if (code not in i) and (('.jpg' or '.png') in i.lower()):
        		main(i)
			os.rename(i,code+i)