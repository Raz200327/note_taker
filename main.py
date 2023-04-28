import openai
import textract
import time

openai.api_key = "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"

pdf_name = input("Input PDF Name: ")

# specify the path of the PDF file you want to extract text from
pdf_path = f"./{pdf_name}"

# extract text from the PDF using textract
text = textract.process(pdf_path).decode('utf-8')

counter = 0
chunks = []
sentence = ""
for i in text.split("."):
    if counter <= 25:
        sentence += i + "."
        counter += 1

    else:
        counter = 0
        chunks.append(sentence)
        sentence = ""

chunk_count = 0
for a in chunks:
    chunk_count += 1
    print(f"Chunk {chunk_count}/{len(chunks)}")
    try:
        summary = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You write notes for given paragraphs. Make the notes in dot point format."},
                {"role": "user", "content": f"Here is the paragraph:\n{a}"}
            ]
        )
        with open(f"./{pdf_name.replace('.pdf', '')} notes.txt", "a") as file:
            file.write(summary["choices"][0]["message"]["content"])
    except:
        time.sleep(1)
        summary = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system",
                 "content": "You write notes for given paragraphs. Make the notes in dot point format."},
                {"role": "user", "content": f"Here is the paragraph:\n{a}"}
            ]
        )
        with open(f"./{pdf_name.replace('.pdf', '')} notes.txt", "a") as file:
            file.write(summary["choices"][0]["message"]["content"])











