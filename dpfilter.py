#!/usr/bin/python3

# Developer By Abdulrahman Kamel
# Github: github.com/Abdulrahman-Kamel

import re
from sys import argv,stdin

class checkEntiries():
	def __init__(self):
		pass

	def readStdin(self):
		data = []
		if not stdin.isatty():
			for line in stdin:
				data.append(line.strip())
		return data
# 
	def readArgv(self, Position):
		data = []
		for line in open(argv[int(Position)], 'r'):
			data.append(line.strip())
		open(argv[int(Position)], 'r').close()
		return data


class dataFilter():
	def __init__(self):
		pass

	def url(self, line):
		regex_url = "^(http|https):\/\/.*.*\/(.*)"
		Match = re.match(regex_url, line)
		return bool(Match)
	
	def url_param(self, line):
		regex_url_param = "^(http|https).*\=.*"
		Match = re.match(regex_url_param, line)
		return bool(Match)


class main():
	def __init__(self):
		self.data = checkEntiries
		urls = self.GetUrls()
		self.save_with_id(self.urls)
		self.urls_with_id_2 = self.urls_with_id.copy()
		self.change_param_value()
		self.remove_duplicate()
		self.store_unique_id()
		self.urls_unique_list = []		
		self.return_original_value()
		self.results()

	def GetUrls(self):
		self.urls = []
		for line in checkEntiries:
			if dataFilter.url_param(line) == True:
				self.urls.append(line)
		return self.urls

	def save_with_id(self, data):
		self.urls_with_id = {}
		ID = 0 
		for url in data:
			self.urls_with_id.update({ID:url.strip()}) 
			ID +=1

	def change_param_value(self):
		paramValueRegex = '=[a-z9A-Z0-9!@#$%^*()-`,\\//+:=._-]*'
		for key, value in self.urls_with_id_2.items():
			self.urls_with_id_2[key] = re.sub(paramValueRegex,str('='+'FUZZ00'),self.urls_with_id_2[key])

	def remove_duplicate(self):
		tmp = [] 
		self.urls_dict_unique = dict() 
		for key, value in self.urls_with_id_2.items(): 
		    if value not in tmp: 
		        tmp.append(value) 
		        self.urls_dict_unique[key] = value

	def store_unique_id(self):
		self.unique_keys = []
		for key,value in self.urls_dict_unique.items():
			self.unique_keys.append(key)

	def return_original_value(self):
		self.urls_unique_list = []
		for ID in self.unique_keys:
			self.urls_unique_list.append(self.urls_with_id[ID])

	def results(self):
		for url in self.urls_unique_list:
			print(url)


# static variables
checkEntiries = checkEntiries()
dataFilter 	  = dataFilter()
argv 		  = checkEntiries.readArgv(1) if len(argv) > 1 else []
checkEntiries = checkEntiries.readStdin() + argv


if __name__ == '__main__':
	main()
