from fastapi import FastAPI
from mongodb.routes import router as MongoRouter
from postgresql.routes import router as PostgresqlRouter
from neo4j_graph.routes import router as Neo4jRouter


app = FastAPI()
app.include_router(MongoRouter, tags=["mongo"], prefix="/mongo")
app.include_router(PostgresqlRouter, tags=["postgresql"], prefix="/postgresql")
app.include_router(Neo4jRouter, tags=["neo4j_graph"], prefix="/neo4j_graph")

@app.get("/")
async def root():
    return {"message": "Hello World"}
