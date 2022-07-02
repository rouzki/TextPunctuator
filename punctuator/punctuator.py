# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"

import logging
from re import M
from langdetect import detect

from torch import cuda

from utils import T5Model

MODEL_NAME = "ZakaryaRouzki/t5-punctuation"


class TextPonctuator:

    def __init__(self, use_gpu=False):
                
        ## using gpu
        if use_gpu:
            if cuda.is_available():
                self.device = 'cuda' 
            else:
                raise("GPU is not available! please set use_gpu=False to use CPU instead.")
        else:
            self.device = 'cpu'

        self.model = T5Model(MODEL_NAME, self.device)



    def punctuate(self, text, lang=None):

        self.detect_lang(self, text, lang)

        return self.model.generate_predictions(text)
        

    @staticmethod
    def detect_lang(self, text, lang):
        if not lang:
            lang = detect(text)
        if lang != 'fr':
            raise Exception(F"""Non French text detected. Text Punctuation currently only supports French text, more languages will be availlable Soon.
            If you are certain the input is French, pass argument lang='fr' to this function.""")



