import pypdf
from gtts import gTTS

path = open('Baudrillard1981.pdf', 'rb')
pdf_reader = pypdf.PdfReader(path)

full_text = ""
for page in pdf_reader.pages:
    text = page.extract_text()
    if text:
        full_text += text + " "
path.close()

print("Converting...")
tts = gTTS(text=full_text, lang='en', slow=False)
tts.save('Baudrillard1981.mp3')
print("Saved.")
