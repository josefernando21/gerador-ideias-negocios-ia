from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel
from models import Base, Idea, GenerateRequest, GenerateResponse, IdeaResponse
from typing import List
import json
import random
import uvicorn

# DB Setup
SQLALCHEMY_DATABASE_URL = "sqlite:///./ideas.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gerador de Ideias de Negócios com IA", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Templates para geração
REVENU_MODELS = ["Freemium", "Assinatura", "Venda única", "Marketplace", "Afiliados"]
TECH_STACKS = ["Next.js + Supabase", "React + Firebase", "Flutter + AWS", "Django + Vercel"]
IDEAS_TEMPLATES = [
    "Plataforma {niche} com {tech} para {market}",
    "App de IA para otimizar {niche} em {market}",
    "Marketplace de serviços {niche} B2B para {market}",
]

def generate_ideas(niche: str, market: str, budget: str) -> dict:
    ideas = []
    for i in range(5):
        idea = {
            "title": f"Ideia {i+1}: {random.choice(IDEAS_TEMPLATES).format(niche=niche, market=market, tech=random.choice(TECH_STACKS))}",
            "description": f"Solução inovadora usando IA para {niche} no mercado de {market}. Modelo {random.choice(REVENU_MODELS)}. Orçamento adequado: {budget}.",
            "revenue": random.choice(REVENU_MODELS),
            "tech": random.choice(TECH_STACKS)
        }
        ideas.append(idea)
    
    swot = {
        "Strengths": "IA escalável, baixo custo inicial.",
        "Weaknesses": f"Dependente de dados {niche}.",
        "Opportunities": f"Crescimento {market}.",
        "Threats": "Concorrência tech."
    }
    
    return {"ideas": ideas, "swot": swot}

@app.post("/generate/", response_model=GenerateResponse)
def generate_idea(request: GenerateRequest, db: Session = Depends(get_db)):
    result = generate_ideas(request.niche, request.market, request.budget)
    
    # Salvar no DB
    db_idea = Idea(niche=request.niche, market=request.market, budget=request.budget, generated_ideas=json.dumps(result))
    db.add(db_idea)
    db.commit()
    db.refresh(db_idea)
    
    return GenerateResponse(**result)

@app.get("/ideas/", response_model=List[IdeaResponse])
def get_ideas(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return db.query(Idea).offset(skip).limit(limit).all()

@app.get("/")
def read_root():
    return {"message": "Gerador de Ideias de Negócios - Acesse /static/index.html ou /docs"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
