from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import json

tokenizer = AutoTokenizer.from_pretrained("bigscience/T0pp")
model = AutoModelForSeq2SeqLM.from_pretrained("bigscience/T0pp")
model.eval()

d = {"question": "How has the once-niche world of digital currencies invaded the mainstream?" ,"passage": "It was the kind of conversation happening in group texts, Twitter threads, Zoom rooms and Clubhouse panels across the country as the once-niche world of digital currencies has invaded the mainstream via art, sports, entertainment and media. In the process, Bitcoin and other cryptocurrencies have gone from curiosity to punchline to viable investment. They have made a lot of people very rich — making the entire category harder than ever to ignore."}

question = d["question"]
passage = d['passage']
instruction = 'Given the following passage "'+passage+'", is the question '+'"'+question+'" answerable. Please answer in "Yes or No"'
answer = tokenizer.decode(model.generate(tokenizer.encode(instruction, return_tensors="pt"))[0],skip_special_tokens=True)
print(answer)
