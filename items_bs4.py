#!/usr/bin/python3

from bs4 import BeautifulSoup

file = open('items.faix', 'r') 

soup = BeautifulSoup(file, 'xml')

print(soup.prettify())
