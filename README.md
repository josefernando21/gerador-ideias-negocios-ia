# 🧠 Gerador de Ideias de Negócios com IA

![Demo](demo.gif) <!-- Adicione screenshot/GIF aqui -->

## 🚀 Sobre
Fullstack app Python/FastAPI + Vanilla JS. Gere ideias de negócios personalizadas com IA (templates avançados). Ideal para startups/empresas. Responsivo, com gráficos SWOT e histórico.

**Features**:
- Formulário intuitivo (nicho, mercado, orçamento).
- Geração de 5 ideias + revenue/tech stack/SWOT.
- API REST + Swagger (/docs).
- Persistência SQLite.
- Dark/light mode.
- Chart.js visuals.

## 🛠 Setup Local (Windows)
1. `cd gerador-ideias-negocios`
2. `python -m venv venv`
3. `venv\\Scripts\\activate`
4. `pip install -r requirements.txt`
5. `uvicorn main:app --reload`
6. Abra http://localhost:8000

## 🌐 Deploy
- **Frontend**: Vercel/Netlify (static/).
- **Backend**: Railway/Render (fullstack).
- GitHub: Clone > Deploy.

## 📱 API Endpoints
- `POST /generate/` - Gere ideia (JSON body).
- `GET /ideas/` - Histórico.
- `/docs` - Swagger UI.

Feito para portfólio GitHub! ✨
