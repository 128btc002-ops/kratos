from fastapi import FastAPI 
app = FastAPI(title="KRATOS API") 
 
@app.get("/") 
def read_root(): 
    return {"message": "KRATOS API is running"} 
