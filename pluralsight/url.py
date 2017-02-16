#!/usr/bin/env python3
from urllib.request import urlopen

def fetch_story():
	with urlopen('http://sixty-north.com/c/t.txt') as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words


def print_words(story_words):
	for word in story_words:
		print(word)


def main():
	words = fetch_story()
	print_words(words)


if __name__ == '__main__':
	main()