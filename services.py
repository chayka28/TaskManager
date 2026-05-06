tasks_db = []
count_task = 1

def create_task(task_data: dict) -> dict:
    global count_task
    task_data["id"] = count_task
    tasks_db.append(task_data)
    count_task += 1
    
    return task_data

def get_all_tasks() -> list:
    return tasks_db

def get_task(task_id: int) -> dict | None:
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    return None
