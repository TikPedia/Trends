from fastapi import FastAPI


from server.routes.trend import router as TrendRouter
from server.routes.commands import router as CommandRouter

app = FastAPI()

app.include_router(TrendRouter, tags=["Trends"], prefix="/trends")
app.include_router(CommandRouter, tags=["Commands"], prefix="/commands")


