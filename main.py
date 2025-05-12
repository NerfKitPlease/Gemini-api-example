from google import genai
import os

client = genai.Client(api_key="YOUR_API_KEY")
textsave = ""

def genAPIRequst(req):
    print("⏱️  Waiting For Response..")
    print("")
    response = client.models.generate_content(
        model = "gemini-2.0-flash", contents = req
    )
    global textsave 
    textsave = response.text
    return response.text

def deltxt():
    with open("rep.txt", "w") as file:
        pass

def writetxt(value):
    split = 100 # split-saves the response according to this value
    with open("rep.txt", "w") as file:
        for i in range(0, len(value), split):
            file.write(value[i:i+split] + "\n")

deltxt()

while True:
    print(genAPIRequst(input("📡 Send Req To AI >> ")))
    deltxt()
    writetxt(textsave)
    print("")
