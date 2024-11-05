"""This program reads files and detect how positive or negative they are."""

import csv
import os.path

positive_words = []
with open(os.path.abspath(__file__) + '/../assets/txt/positive_words.txt') as positives_file:
    for lin in positives_file:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

negative_words = []
with open(os.path.abspath(__file__) + '/../assets/txt/negative_words.txt') as negatives_file:
    for lin in negatives_file:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())


def strip_punctuation(s: str) -> str:
    """A function to remove punctuation marks."""
    
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    
    for punc_char in punctuation_chars:
        s = s.replace(punc_char, '')
    
    return s


def get_positives(s: str) -> int:
    """A function that counts the number of positive words in the string."""
    
    s = strip_punctuation(s.lower()).split()
    
    positive_score = 0
    for word in positive_words:
        if word in s:
            pass
        positive_score += s.count(word)
    return positive_score
        

def get_negatives(s: str) -> int:
    """A function that counts the number of negative words in the string."""
    
    s = strip_punctuation(s.lower()).split()

    
    negative_score = 0
    for word in negative_words:
        negative_score += s.count(word)
        
    return negative_score
 
        
def input_file(prompt: str = '') -> tuple[str]:
    """A function that prompt the user for a file path."""
    
    while True:
        file_name = os.path.splitext(input(prompt))
        file_path = f'{os.path.abspath(__file__)}/../inputs/{file_name[1].replace('.','')}/{file_name[0]}{file_name[1]}'
        if os.path.isfile(file_path):
            break
        print("There is no file of that name, write another one.")
    return (file_path) + file_name


def file_order(file_data):
    output_path = f'{os.path.abspath(__file__)}/../outputs/{file_data[2].replace('.','')}/{file_data[1]}_{'{}'}{file_data[2]}'
    
    order = 0
    while (os.path.exists(output_path.format(order))):
        order += 1
    
    return output_path.format(order)
    
    
def tweets_detector_txt(file_data: tuple[str] = None):
    """A function that takes a csv of tweets and analyze it with csv module and write its sentiment score in another file."""
    if file_data == None:
        file_data = input_file('Enter txt/csv file name including the extension (from the inputs file): ')
    
    output_path = file_order(file_data)
    
    with open(file_data[0]) as inputs_file:
        with open(output_path, 'w') as outputs_file:
            header = inputs_file.readline()
            outputs_file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
            outputs_file.write('\n')
            
            for line in inputs_file:
                values = line.strip().split(',')
                positive_score = get_positives(values[0])
                negative_score = get_negatives(values[0])
                net_score = positive_score - negative_score
                
                outputs_file.write(','.join(map(str, (values[1], values[2], positive_score, negative_score, net_score))))
                outputs_file.write('\n')
            

def tweets_detector_csv(file_data: tuple[str] = None):
    """A function that takes a csv of tweets and analyze it with dictionaries and write its sentiment score in another file."""
    if file_data == None:
        file_data = input_file('Enter txt/csv file name including the extension (from the inputs file): ')
    
    output_path = file_order(file_data)
    
    with open(file_data[0]) as inputs_file:
        with open(output_path, 'w') as outputs_file:
            reader = csv.reader(inputs_file)
            writer = csv.writer(outputs_file)
            header = next(reader)
            writer.writerow(('Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score'))
            
            for line in reader:
                positive_score = get_positives(line[0])
                negative_score = get_negatives(line[0])
                net_score = positive_score - negative_score
                
                writer.writerow(map(str, (line[1], line[2], positive_score, negative_score, net_score)))


def tweets_detector_dicts(file_data: tuple[str] = None):
    """A function that takes a csv of tweets and analyze it and write its sentiment score in another file."""
    if file_data == None:
        file_data = input_file('Enter txt/csv file name including the extension (from the inputs file): ')
    
    output_path = file_order(file_data)
    
    with open(file_data[0]) as inputs_file:
        with open(output_path, 'w') as outputs_file:
            reader = csv.DictReader(inputs_file)
            writer = csv.DictWriter(outputs_file, ('Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score'))
            writer.writeheader()
            
            for line in reader:
                positive_score = get_positives(line['tweet_text'])
                negative_score = get_negatives(line['tweet_text'])
                net_score = positive_score - negative_score
                
                writer.writerow({x:y for x,y in zip(writer.fieldnames,map(str, (line['retweet_count'], line['reply_count'], positive_score, negative_score, net_score)))}) 


tweets_detector_txt((f'{os.path.abspath(__file__)}/../inputs/csv/project_twitter_data.csv','project_twitter_data','.csv'))
# tweets_detector_csv((f'{os.path.abspath(__file__)}/../inputs/csv/project_twitter_data.csv','project_twitter_data','.csv'))
# tweets_detector_dicts((f'{os.path.abspath(__file__)}/../inputs/csv/project_twitter_data.csv','project_twitter_data','.csv'))
# tweets_detector_txt()