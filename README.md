# AI Sentiment Analyzer

A Python-based Command Line Interface (CLI) application that analyzes user-entered sentences to predict their emotional sentiment (Positive, Negative, or Neutral)[cite: 5].

## 📌 Project Objective
The main goal of this project is to develop a clean, modular Python application that processes textual input, normalizes it, tokenizes the words, and evaluates sentiment by matching keywords against pre-defined positive and negative lexicons[cite: 5, 12, 13, 24].

## 📂 Project Structure
]To keep the codebase clean, organized, and scalable, the project is divided into three distinct modules[cite: 18]:
**`lexicon.py`**: Contains the datasets for sentiment evaluation (`positive_words` and `negative_words`)[cite: 24].
*`logic.py`**: Handles user input validation (gracefully catching empty inputs and exit signals) and contains the word-counting logic[cite: 16, 17].
* `main.py`**: Acts as the central controller that orchestrates the execution flow and displays the final AI prediction[cite: 15].

## 🚀 Features & Requirements Fulfilled
- Continuous Execution**: The program runs continuously in a loop until the user explicitly types `exit`[cite: 16].
- Robust Input Handling**: Gracefully handles and flags invalid or empty inputs using custom validation loops[cite: 17].
- Case Normalization**: Automatically normalizes user inputs to lowercase for consistent dictionary matching[cite: 12].
- Tokenized Word Matching**: Splits text into distinct tokens to calculate precise match counts instead of simple substring matching[cite: 14].

