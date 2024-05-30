import tkinter as tk
import NER
import sentiment
import translate
import summary

def analyze_text():
    text = input_text.get("1.0", "end-1c")
    ner_results = NER.perform_ner(text)
    sentiment_result = sentiment.analyze_sentiment(text)
    translated_text = translate.translate_to_arabic(text)
    summary_result = summary.solve(text, 0.2)  # Adjust the percentage as needed
    ner_output.config(text=f"NER Results:\n{ner_results}")
    sentiment_output.config(text=f"Sentiment Analysis:\n{sentiment_result}")
    translation_output.config(text=f"Translated Text (Arabic):\n{translated_text}")
    summary_output.config(text=f"Text Summary:\n{summary_result}")

window = tk.Tk()
window.title("Text Analysis Tool")

input_text = tk.Text(window, height=10, width=50)
input_text.pack()

submit_button = tk.Button(window, text="Submit", command=analyze_text)
submit_button.pack()

ner_output = tk.Label(window, text="")
ner_output.pack()
sentiment_output = tk.Label(window, text="")
sentiment_output.pack()
translation_output = tk.Label(window, text="")
translation_output.pack()
summary_output = tk.Label(window, text="")
summary_output.pack()

window.mainloop()
