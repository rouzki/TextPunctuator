# -*- coding: utf-8 -*-

__author__ = "Zakarya ROUZKI"
__email__ = "zakaryarouzki@gmail.com"

from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

class T5Model:
    """
    Function to load T5 model / tokenizer and generate predictions

    ARGS:
    MODEL_NAME: name of the model to load from HF
    device: gpu or cpu
    """

    def __init__(self, MODEL_NAME, device):
        self.model_name = MODEL_NAME
        self.device = device
        self.load_model(MODEL_NAME)

    def load_model(self, MODEL_NAME):
        """load t5 model"""
        self.model = T5ForConditionalGeneration.from_pretrained(MODEL_NAME)
        self.tokenizer = T5Tokenizer.from_pretrained(MODEL_NAME)

        ## sending model to device
        self.model = self.model.to(self.device)


    def generate_predictions(self, text):
        """ 
        generate model prediction from text

        steps:
            * tokenize text and encode it
            * get input_ids and attention_mask 
            * pass it to the model
            * get generated_ids
            * convert it back using tokenizer
        """
        ## encode text
        inputs = self.tokenizer.encode_plus(text, max_length=128, pad_to_max_length=True, truncation=True, padding="max_length", return_tensors='pt')

        ## get inputs and attention_masks
        ids = inputs['input_ids'].to(self.device, dtype = torch.long)
        mask = inputs['attention_mask'].to(self.device, dtype = torch.long)

        # generate outputs / ids
        generated_ids = self.model.generate(
            input_ids = ids,
            attention_mask = mask, 
            max_length=150, 
            num_beams=2,
            repetition_penalty=2.5, 
            length_penalty=1.0, 
            early_stopping=True
            )
        
        # decode moodel outputs
        text_punctuated = self.tokenizer.decode(generated_ids[0], skip_special_tokens=True, clean_up_tokenization_spaces=True) 

        return text_punctuated