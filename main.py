from fastapi import FastAPI

app = FastAPI(
    title="Cheking salary"
)

employees = [
    {"id": 1, "name": "������� �.",             "salary_increase_date": "11.07.2023"},
    {"id": 2, "name": "� �", "salary_increase_date": "13.08.2023"},
    {"id": 3, "name": "����� ���������",        "salary_increase_date": "01.01.2024"},
]

@app.get("/empl/{empl_id}")
def get_user(user_id: int):
    return [user for user in employees if user.get("id") == user_id]


@app.get("/date_inc_salary")
def get_salary_increase_date(user_id, login=0, password=0):
    return [empl for empl in employees if empl.get("id") == user_id]

