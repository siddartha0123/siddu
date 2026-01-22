import os
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

# configuare .env
load_dotenv()
generative_configure = {
     "temperature":0.7,
     "max_output_tokens" : 100
}
app = FastAPI()
app.add_middleware(CORSMiddleware,
                   allow_origins=["*"],allow_methods=["*"])
# adding frontend
app.mount("/static",StaticFiles(directory="static"),name="static")

# configure genai
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# model
model = genai.GenerativeModel("gemini-flash-latest",generation_config=generative_configure)

@app.post("/")
async def quote_generater():
     try:
          prompt = ("Who is  joyboy from onepiece?")
          response = model.generate_content(prompt)
          if not response:
               raise ValueError("Your getting empty result")
          return {"quote":response.text}
     except Exception as e:
          raise HTTPException(status_code=500,detail=str(e))