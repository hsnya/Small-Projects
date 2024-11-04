"""This program reads files and detect how positive or negative they are."""

import csv
import os.path


def strip_punctuation(s: str) -> str:
    """A function to remove punctuation marks."""
    
    punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
    
    for punc_char in punctuation_chars:
        s = s.replace(punc_char, '')
    
    return s


def get_positives(s: str) -> int:
    """A function that counts the number of positive words in the string."""
    
    s = strip_punctuation(s.lower()).split()
    
    positive_words = []
    with open(os.path.abspath(__file__) + '/../assets/positive_words.txt') as positives_file:
        for lin in positives_file:
            if lin[0] != ';' and lin[0] != '\n':
                positive_words.append(lin.strip())
    
    positive_score = 0
    for word in positive_words:
        positive_score += s.count(word)
    return positive_score
        

def get_negatives(s: str) -> int:
    """A function that counts the number of negative words in the string."""
    
    s = strip_punctuation(s.lower()).split()
    
    negative_words = []
    with open(os.path.abspath(__file__) + '/../assets/negative_words.txt') as negatives_file:
        for lin in negatives_file:
            if lin[0] != ';' and lin[0] != '\n':
                negative_words.append(lin.strip())
    
    negative_score = 0
    for word in negative_words:
        negative_score += s.count(word)
        
    return negative_score
 
        
def input_file(prompt: str = '', extension: str = 'txt/csv') -> tuple[str]:
    """A function that prompt the user for a file path."""
    
    while True:
        file_name = input(prompt)
        file_path = os.path.abspath(__file__) + '/../inputs/' + file_name
        file_name = os.path.splitext(os.path.basename(file_path))
        if os.path.isfile(file_path) and file_name[1] in extension:
            break
        print("There is no file of that name, write another one.")
    return (file_path) + file_name


def tweets_csv_detector(file_data: tuple[str] = None):
    """A function that takes a csv of tweets and analyze it and write its sentiment score in another file."""
    if file_data == None:
        file_data = input_file('Enter txt/csv file name including the extension (from the inputs file): ', 'csv')
    
    output_path = os.path.abspath(__file__) + '/../outputs/' + file_data[1] + '_{}' + file_data[2]
    
    order = 0
    while (os.path.exists(output_path.format(order))):
        order += 1
    
    with open(file_data[0]) as inputs_file:
        with open(output_path.format(order), 'w') as outputs_file:
            reader = csv.DictReader(inputs_file)
            writer = csv.DictWriter(outputs_file, ('Number of Retweets', 'Number of Replies', 'Positive Score', 'Negative Score', 'Net Score'))
            writer.writeheader()
            
            for row in reader:
                text = row['tweet_text']
                pos_score, neg_score = get_positives(text), get_negatives(text)
                net_score = pos_score + neg_score
                writer.writerow({x:y for x,y in zip(writer.fieldnames,(row['retweet_count'], row['reply_count'], pos_score, neg_score, net_score))})
    

tweets_csv_detector((os.path.abspath(__file__) + '/../inputs/project_twitter_data.csv','project_twitter_data','.csv'))
# tweets_csv_detector()