import json
import os
import re


def extract_sentences_from_json():
    for root, dirs, files in os.walk("./input"):
        for name in files:
            print("Now processing: " + name)
            with open("./input/" + name, "r", encoding='utf-16') as file:
                content = json.load(file)

            pump_name = name.split(".")[0].split("_")[0]
            concatenated_paragraphs = ""
            clean_concatenated_paragraphs = ""
            for article in content["content"]["articles"]:
                for paragraph in article["paragraphs"]:
                    concatenated_paragraphs += paragraph["value"]
                    concatenated_paragraphs = concatenated_paragraphs.replace("\n", " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace("- ", "")
                    concatenated_paragraphs = concatenated_paragraphs.replace(". ", ".\n")
                    concatenated_paragraphs = re.sub(r'([mM]in\.|[Ee]\.g\.|[mM]ax\.|[fF]ig(s)?\.) *\n', r'\1 ', concatenated_paragraphs)
                    concatenated_paragraphs = concatenated_paragraphs.replace(" .", ".")
                    concatenated_paragraphs = re.sub(r' +', ' ', concatenated_paragraphs)
                    concatenated_paragraphs = re.sub(r'\d (\d |\d)+', '', concatenated_paragraphs)
                    concatenated_paragraphs = concatenated_paragraphs.replace("\n ", "\n")
                    concatenated_paragraphs = concatenated_paragraphs.replace("The pump ", pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" the pump ", " " + pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" the pump.", " " + pump_name + ".")
                    concatenated_paragraphs = concatenated_paragraphs.replace("This pump ", pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" this pump ", " " + pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" this pump.", " " + pump_name + ".")
                    concatenated_paragraphs = concatenated_paragraphs.replace("The pumps ", pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" the pumps ", " " + pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" the pumps.", " " + pump_name + ".")
                    concatenated_paragraphs = concatenated_paragraphs.replace("These pumps ", pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" these pumps ", " " + pump_name + " ")
                    concatenated_paragraphs = concatenated_paragraphs.replace(" these pumps.", " " + pump_name + ".")
                    concatenated_paragraphs += "\n"

                # Remove short (5 chars or less), and presumably, redundant lines
                for line in concatenated_paragraphs.split("\n"):
                    if len(line) >= 5:
                        clean_concatenated_paragraphs += line + "\n"
                    else:
                        clean_concatenated_paragraphs += "\n"

            f = open("./output/" + name.split(".")[0] + ".txt", "w", encoding='utf-8')
            f.write(clean_concatenated_paragraphs)
            f.close()

if __name__ == "__main__":
    extract_sentences_from_json()
