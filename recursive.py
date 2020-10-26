# functions
def download_file(file_url, file_name):
	file_data = urllib.request.urlopen(file_url).read()
		
	# saves data to file
	file_stream = open(file_name, 'wb')
	file_stream.write(file_data)
	file_stream.close()
	return None

def download_dir(dir_url):
	## TODO: finish this function
	print(dir_url)
	return None

# github API format
# https://api.github.com/repos/:owner/:repo/contents/:path

import urllib.request
import json

url = 'https://api.github.com/repos/trenton3983/programming_computer_vision_with_python/contents/PCV'

data = urllib.request.urlopen(url).read()

# total number of elements
total = len(json.loads(data))

for res in range(total):
	# gets resource parameters
	res_name = json.loads(data)[res]['name']
	res_type = json.loads(data)[res]['type']

	# checks for resource type
	if res_type == 'dir':
		download_dir(url + '/' + res_name)
	else:
		file_url = json.loads(data)[res]['download_url']
		download_file(file_url, res_name)