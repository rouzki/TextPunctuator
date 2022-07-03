# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"

import logging
from re import M
from langdetect import detect

from torch import cuda

from .utils import T5Model

# model name
MODEL_NAME = "ZakaryaRouzki/t5-punctuation"


class TextPunctuator:
    """main class used to pucntuate texts"""
    def __init__(self, use_gpu=False):
        ## using gpu
        if use_gpu:
            if cuda.is_available(): # check if gpu is available
                self.device = 'cuda' 
            else: # gpu not available
                raise Exception("GPU is not available! please set use_gpu=False to use CPU instead.")
        else: 
            self.device = 'cpu'
        
        # load model
        self.model = T5Model(MODEL_NAME, self.device)



    def punctuate(self, text: str, lang:str=None):
        """
        Perform punctuation on the given text,
        Make sure that the language is French then call model to generate predctions
        Args:
            - text (str): Text to punctuate (unpunctuated).
            - lang (str):  language / only if user is sure it's french.
        """

        # detect language
        self.detect_lang(self, text, lang)

        # return model predictions
        return self.model.generate_predictions(text)
        

    @staticmethod
    def detect_lang(self, text, lang):
        """ 
        detect language of input text
        Args:
            same as punctuate() function
        """
        # if lang is not forced 
        if not lang:
            # detect language
            lang = detect(text)
        
        # if lang is not french raise exception
        if lang != 'fr':
            raise Exception(F"""Non French text detected. Text Punctuation currently only supports French text, more languages will be availlable Soon.
            If you are certain the input is French, pass argument lang='fr' to this function.""")



