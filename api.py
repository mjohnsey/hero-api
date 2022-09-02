from uuid import UUID

from fastapi import FastAPI

from fastapi_example.schemas import HealthResponse
from fastapi_example.server.routers.hero import SuperheroRouter
from fastapi_example.stores.hero import HeroStore, Superhero

store = HeroStore(
    heroes={
        UUID("00000000-0000-0000-0000-000000000001"): Superhero(
            id=UUID("00000000-0000-0000-0000-000000000001"),
            name="Superman",
            super_power="flight",
        ),
        UUID("00000000-0000-0000-0000-000000000002"): Superhero(
            id=UUID("00000000-0000-0000-0000-000000000002"),
            name="Flash",
            super_power="super-speed",
        ),
    }
)

app = FastAPI()

hero_router = SuperheroRouter(store)

app.include_router(hero_router.router, tags=["Heroes"])


@app.get("/health", response_model=HealthResponse)
async def health():
    return {"status": "ok"}


@app.get("/", response_model=dict[str, str])
async def root():
    return {"msg": "Hello World"}