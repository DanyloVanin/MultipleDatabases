from neomodel import config
from decouple import config as get_from_env_var

NEO4J_URL = get_from_env_var("NEO4J_URL")  # read environment variable

config.DATABASE_URL = NEO4J_URL #"bolt://neo4j:trilogy-scoop-helena-jason-mystic-2734@localhost:7687"
