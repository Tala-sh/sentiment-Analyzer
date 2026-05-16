from lexicon import POSITIVE_WORDS,NEGATIVE_WORDS
from logic import Input_user_handler,Count_tokens_Analyzer

def main():
   while True:
       text = Input_user_handler()

       if text is None:
           print("program stopped")
           break

       pos_found, neg_found = Count_tokens_Analyzer(text,POSITIVE_WORDS,NEGATIVE_WORDS)

       print(f"Positive Words Found:{pos_found}")
       print(f"Negative Words Found:{neg_found}")

       if pos_found > neg_found:
           print("AI Result :Positive ")
       elif pos_found < neg_found:
           print("AI Result :Negative ")
       else:
           print("AI Result :Neutral")


if __name__ == '__main__':
   main()



