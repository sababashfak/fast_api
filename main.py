from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI(title="File Upload and Save System")

@app.get("/")
async def root():
  return{"message" : "Hello World"}


#@app.post("/uploaded file")

