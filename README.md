# AI Sentiment Analyzer

A Python-based Command Line Interface (CLI) application that analyzes user-entered sentences to predict their emotional sentiment (Positive, Negative, or Neutral)

## 📌 Project Objective
The main goal of this project is to develop a clean, modular Python application that processes textual input, normalizes it, tokenizes the words, and evaluates sentiment by matching keywords against pre-defined positive and negative lexicons

## 📂 Project Structure
]To keep the codebase clean, organized, and scalable, the project is divided into three distinct modules:
**`lexicon.py`**: Contains the datasets for sentiment evaluation (`positive_words` and `negative_words`)
*`logic.py`**: Handles user input validation (gracefully catching empty inputs and exit signals) and contains the word-counting logic
* `main.py`**: Acts as the central controller that orchestrates the execution flow and displays the final AI prediction

## 🚀 Features & Requirements Fulfilled
- Continuous Execution**: The program runs continuously in a loop until the user explicitly types `exit`
- Robust Input Handling**: Gracefully handles and flags invalid or empty inputs using custom validation loops
- Case Normalization**: Automatically normalizes user inputs to lowercase for consistent dictionary matching
- Tokenized Word Matching**: Splits text into distinct tokens to calculate precise match counts instead of simple substring matching

