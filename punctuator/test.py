# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"


from utils import TextPonctuator

punctuator = TextPonctuator(use_gpu=False)


text = 'this is a test text with some formatting rules that should not be displayed inputs and outputs'

text_punctuated = punctuator.punctuate(text, lang='fr')