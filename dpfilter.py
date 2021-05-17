#!/usr/bin/python3

# Developer By Abdulrahman Kamel
# Github: github.com/Abdulrahman-Kamel

import re
import argparse
from sys import argv,stdin,modules

class checkEntiries():
	def __init__(self):
		from sys import modules
		if 'argv' not in modules:		
			from sys import argv
		if 'stdin' not in modules:
			from sys import stdin

	def readStdin(self):
		data = []
		if not stdin.isatty():
			for line in stdin:
				data.append(line.strip())
		return data

	def readArgv(self, Position):
		data = []
		if len(argv) > 1:
			for line in open(argv[int(Position)], 'r'):
				data.append(line.strip())
		open(argv[int(Position)], 'r').close()
		return data


class dataFilter():
	def __init__(self):
		self.regex_url = "^(http|https):\/\/.*.*\/(.*)"
		self.regex_url_param = "^(http|https).*\=.*"
	
	def url(self, line):
		Match = re.match(self.regex_url, line)
		return bool(Match)
	
	def url_param(self, line):
		Match = re.match(self.regex_url_param, line)
		return bool(Match)


class main():
	def __init__(self):
		self.paramValueRegex = '=[a-z9A-Z0-9!@#$%^*()-`,\\//+:=._-]*'
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
		for key, value in self.urls_with_id_2.items():
			self.urls_with_id_2[key] = re.sub(self.paramValueRegex,str('='+'FUZZ00'),self.urls_with_id_2[key])

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
checkEntiries = checkEntiries.readStdin() + argv
argv 		  = checkEntiries.readArgv(1) if len(argv) > 1 else []


if __name__ == '__main__':
	main()
