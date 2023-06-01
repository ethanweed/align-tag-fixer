import os
import glob
from itertools import chain
import pandas as pd


def chat2penn(cut_file_folder):

   os.chdir(cut_file_folder, output_directory = cut_file_folder)
 
  
  chat_words = []
  chat_POS = []
  
  for file in glob.glob('*.cut'):
    with open(file,'r') as f:
        text = f.read()

    # remove final newline, if there is one
    if text.endswith('\n'):
        text = text[0:-2]

    # make a list
    text = text.split('\n')[2:]

    temp_words = []
    temp_chat_POS = []

    for item in text:
        #print(item)
         temp_words.append(item.split(' {[')[0])
         temp_chat_POS.append(item.split(' {[')[1])

    chat_words.append([x.replace('_', '') for x in temp_words])

    temp_chat_POS = [x.replace('scat ', '') for x in temp_chat_POS]
    temp_chat_POS = [x.replace(']}', '') for x in temp_chat_POS]
    temp_chat_POS = [x.replace(']', '') for x in temp_chat_POS]

  chat_POS.append(temp_chat_POS)
  chat_words = list(chain.from_iterable(chat_words))
  chat_POS = list(chain.from_iterable(chat_POS))

    #chat_POS = [x.replace(']', '') for x in chat_POS]

  chat_info = pd.DataFrame(zip(chat_words, chat_POS), columns=['chat_words', 'chat_POS'])

  chat_info.to_csv(output_file_directory + 'custom_chat_tags.csv', index=False)