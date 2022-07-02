# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"


from Punctuator import TextPonctuator
import logging

punctuator = TextPonctuator(use_gpu=False)


text = "Sur la base de ces échanges Blake Lemoine a donc jugé que le système avait atteint un niveau de conscience lui permettant d’être sensible Ce dernier a ensuite envoyé par email un rapport sur la sensibilité supposée de LaMDA à deux cents employés de Google Très vite les dirigeants de l’entreprise ont rejeté les allégations"

text_punctuated = punctuator.punctuate(text, lang='fr')

print(text_punctuated)
logging.info(f"text ponctuated: [ {text_punctuated} ].")