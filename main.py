import pickle
from fastapi import FastAPI, Path

app = FastAPI()

companies = pickle.load(open("companies.pkl", "rb"))
api_home = "This API returns info about several companies. Go to /docs for more complete documentation on how to use it."


@app.get("/")
def home():
    return api_home


@app.get("/get-companies/{activity}")
def get_companies(
    activity: str = Path(
        None,
        description=f"The type of industry that company works in.\
                      Can be one of the following: [texteis, couro, papel, borracha, metal]",
    )
):
    return [(company["Nome"], company["Atividade"], company["url"], company["Distrito"], company["Morada"]) for company in companies[activity]]
