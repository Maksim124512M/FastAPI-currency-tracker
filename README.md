# FastAPI Currency Tracker 💱

Asynchronous API for tracking and serving currency exchange rates.

This service collects data from multiple providers (Monobank, NBU, Binance, etc.), stores historical rates in PostgreSQL, and exposes RESTful endpoints for querying real-time and past exchange rates. 

### 🔧 Features
- 🔁 Periodic background updates using Celery
- 📥 Real-time rates from public APIs
- 🕰️ Historical rates tracking
- ⚡ Fast & async FastAPI architecture
- 🧠 Smart caching with Redis
- 📊 Swagger / ReDoc documentation
- 🔒 JWT-authenticated admin routes

---

### 📚 Use cases
- Create dashboards and widgets with up-to-date currency rates
- Analyze historical currency trends
- Build your own converter service (UAH → USD → BTC, etc.)