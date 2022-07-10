#!/usr/bin/python3
# -*- coding: utf-8 -*-

#learn to train machine learning model for use it in spacy and train custom models in spacy

#https://youtu.be/wpyCzodvO3A

import spacy
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
import json

def load_data(file):
	with open(file, 'r', encodung='utf-8') as f:
		data = json.load(f)
	return(data)
	

	