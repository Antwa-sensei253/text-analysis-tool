# Text Analysis Tool

## Overview

This repository contains a comprehensive text analysis tool that performs various natural language processing (NLP) tasks such as Named Entity Recognition (NER), sentiment analysis, translation, and text summarization. The tool features a graphical user interface (GUI) built with Tkinter to make these functionalities accessible.

## Features

- **Named Entity Recognition (NER)**: Identifies entities like persons, geopolitical entities (GPE), and organizations within a text using spaCy.
- **Sentiment Analysis**: Analyzes the sentiment of a text (positive, negative, or neutral) using a lexicon-based approach.
- **Translation**: Translates the text to Arabic using Google Translate.
- **Text Summarization**: Summarizes the text based on a specified compression ratio.

## Installation

### Clone the repository:


`git clone https://github.com/Antwa-sensei253/text-analysis-tool.git`
`cd text-analysis-tool`

### Install the required packages:


`pip install spacy googletrans==4.0.0-rc1 pip install tk python -m spacy download en_core_web_sm`

### Run the program:


`python gui.py`
