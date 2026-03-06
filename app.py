from fastapi import FastAPI, Query, Request
from fastapi.responses import PlainTextResponse, JSONResponse
import time

app = FastAPI()

# ===== Simple In-Memory Rate Limit =====
RATE_LIMIT_SECONDS = 0
ip_last_request = {}

@app.middleware("http")
async def rate_limit(request: Request, call_next):
    ip = request.client.host
    now = time.time()

    last_time = ip_last_request.get(ip)
    if last_time and (now - last_time) < RATE_LIMIT_SECONDS:
        return JSONResponse(
            status_code=429,
            content={"error": "Slow down bro"}
        )

    ip_last_request[ip] = now
    return await call_next(request)

# ===== API =====
@app.get("/")
async def lookup(key: str = Query(None), number: str = Query(None)):

    if key != "IntelX":
        return JSONResponse(
            status_code=403,
            content={"error": "Unauthorized: Invalid Key"}
        )

    return PlainTextResponse(
"""Free mai kya lifetime ke liye loge abbb
Free Trial Over

DM FOR Paid Access
@Cyber_XSupport

For Free APIs join channel:
https://t.me/+qsKh2hpGj0IwM2Q1
"""
                     )
