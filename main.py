from fastapi import FastAPI

app = FastAPI(
    title="Cheking salary"
)

employees = [
    {"id": 1, "name": "Racoon",  "salary": 10000000, "salary_increase_date": "11.07.2023"},
    {"id": 2, "name": "Monkey",  "salary": 10000000, "salary_increase_date": "13.08.2023"},
    {"id": 3, "name": "Zimbruh", "salary": 5000,     "salary_increase_date": "01.01.2024"},
    {"id": 4, "name": "Duck",    "salary": 3500,     "salary_increase_date": "17.09.2025"}
]

@app.get("/empl/{empl_id}")
def get_user(user_id: int):
    return [user for user in employees if user.get("id") == user_id]

@app.get("/date_inc_salary")
def get_salary_increase_date(user_id: int):
    return [empl for empl in employees if empl.get("id") == user_id]
