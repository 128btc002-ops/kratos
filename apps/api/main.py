from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import uuid

app = FastAPI(title="KRATOS API")

# Autorise toutes les origines en dev
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "KRATOS API is running"}

@app.get("/projects/quick")   # on passe en GET
def quick_project(description: str):
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <title>KRATOS is coming</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <style>
        body{{
          background:#0A0A0B;
          color:#FFFFFF;
          font-family:Inter,sans-serif;
          display:flex;
          align-items:center;
          justify-content:center;
          height:100vh;
          flex-direction:column;
        }}
        .logo{{
          font-size:8rem;
          color:#00F5D4;
          margin-bottom:1rem;
        }}
        .btn{{
          background:#00F5D4;
          color:#0A0A0B;
          padding:.75rem 1.5rem;
          border:none;
          border-radius:4px;
          font-weight:bold;
          cursor:pointer;
        }}
      </style>
    </head>
    <body>
      <div class="logo">Κ</div>
      <h1>KRATOS is coming</h1>
      <p>{description}</p>
      <button class="btn">Join early access</button>
    </body>
    </html>
    """
    return {"project_id": str(uuid.uuid4()), "url": f"https://demo.kratos.app/p/{uuid.uuid4()}", "html": html}