# Text Punctuator Based on Transformers model T5.
T5 model fine-tuned for punctuation restoration.
Model currently supports only French Language. More language supports will be added later using mT5.

Train Datasets : 
Model trained using 2 french datasets (around 500k records): 
- [orange_sum](https://huggingface.co/datasets/orange_sum) 
- [mlsum](https://huggingface.co/datasets/mlsum) (only french text)


more info will be added later.

---------------------------
## 🚀 Usage
**Below is a quick way to get up and running with the model.**
1. First, install the package.
```bash
pip install TextPunctuator
```
2. Sample python code.
```python

from Punctuator import TextPunctuator

punctuator = TextPunctuator(use_gpu=False)

text = "Sur la base de ces échanges Blake Lemoine a donc jugé que le système avait atteint un niveau de conscience lui permettant d’être sensible Ce dernier a ensuite envoyé par email un rapport sur la sensibilité supposée de LaMDA à deux cents employés de Google Très vite les dirigeants de l’entreprise ont rejeté les allégations"

text_punctuated = punctuator.punctuate(text, lang='fr')

text_punctuated
# Outputs the following:
# Sur la base de ces échanges, Blake Lemoine a donc jugé que le système avait atteint un niveau de conscience lui permettant d’être sensible. Ce dernier a ensuite envoyé par email un rapport sur la sensibilité supposée de LaMDA à deux cents employés de Google. Très vite, les dirigeants de l’entreprise ont rejeté les allégations.
```

-----------------------------------------------
## ☕ Contact 
Contact [Zakarya ROUZKI ](https://zakaryarouzki@gmail.com) or at [Linkedin](https://linkedin.com/in/rouzki).

-----------------------------------------------
