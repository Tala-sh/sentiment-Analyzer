from lexicon import POSITIVE_WORDS ,NEGATIVE_WORDS

# from pydoc import text
from lexicon import POSITIVE_WORDS ,NEGATIVE_WORDS


def Input_user_handler():
    while True:
        Enter_sentons=input("please enter sentence or write exite to stop ")

        if Enter_sentons.strip()=="":
            print("empty input not allowed ")
            continue

        if Enter_sentons=="exit":
            print("program stop")
            break

        return Enter_sentons.lower()

"""this function response on count number of negative and positive word to detect
later 
"""

def Count_tokens_Analyzer(text,POSITIVE_WORDS,NEGATIVE_WORDS):
    tokens=text.split()
    pos_count = sum(1 for token in tokens if token in POSITIVE_WORDS)
    neg_count = sum(1 for token in tokens if token in NEGATIVE_WORDS)
    return pos_count,neg_count


#create new variable to count word number of positive and negative

# pos_coun = 0
# neg_coun = 0
#
# tokens = text.split()
#
# for token in tokens:
#     if token in POSITIVE_WORDS:
#         pos_coun+=1
#     elif token in NEGATIVE_WORDS:
#         neg_coun+=1
