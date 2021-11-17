import json
import re


def extract_sentences_from_json(pump_name):
    with open("input.json", "rb") as file:
        content = json.load(file)

    concatenated_paragraphs = ""
    clean_concatenated_paragraphs = ""
    for article in content["content"]["articles"]:
        for paragraph in article["paragraphs"]:
            concatenated_paragraphs += paragraph["value"]
            concatenated_paragraphs = concatenated_paragraphs.replace("\n", " ")
            concatenated_paragraphs = concatenated_paragraphs.replace("- ", "")
            concatenated_paragraphs = concatenated_paragraphs.replace(". ", ".\n")
            concatenated_paragraphs = concatenated_paragraphs.replace(" .", ".")
            concatenated_paragraphs = re.sub(r' +', ' ', concatenated_paragraphs)
            concatenated_paragraphs = re.sub(r'\d( \d)+', '', concatenated_paragraphs)
            concatenated_paragraphs = concatenated_paragraphs.replace("\n ", "\n")
            concatenated_paragraphs = concatenated_paragraphs.replace("The pump ", pump_name + " ")
            concatenated_paragraphs = concatenated_paragraphs.replace(" the pump ", " " + pump_name + " ")
            concatenated_paragraphs = concatenated_paragraphs.replace(" the pump.", " " + pump_name + ".")
            concatenated_paragraphs = concatenated_paragraphs.replace("This pump ", pump_name + " ")
            concatenated_paragraphs = concatenated_paragraphs.replace(" this pump ", " " + pump_name + " ")
            concatenated_paragraphs = concatenated_paragraphs.replace(" this pump.", " " + pump_name + ".")
            concatenated_paragraphs += "\n"

        # Remove short (5 chars or less), and presumably, redundant lines
        for line in concatenated_paragraphs.split("\n"):
            if len(line) >= 5:
                clean_concatenated_paragraphs += line + "\n"
            else:
                clean_concatenated_paragraphs += "\n"

    f = open("training_data.txt", "w")
    f.write(clean_concatenated_paragraphs)
    f.close()


# def process_training_data():
#     result = ""
#     with open("sample.txt", "r") as file:
#         for line in file:
#             buffer = line
#             result += line.replace("- ", "").replace("\n", ".\n")


if __name__ == "__main__":
    extract_sentences_from_json("SQ/SQE")
