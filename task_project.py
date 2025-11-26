from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
import uuid
from datetime import datetime

app = FastAPI()

task_db = {}

class TaskInput(BaseModel):
    text : str
    delay : int  = 2

@app.post('/task')
async def create_task(task : TaskInput):
    task_id = str(uuid.uuid4())  # unique id for each task
    start_time = datetime.utcnow()

    # Save initial task info
    task_db[task_id] = {
        "text" : task.text,
        "status" : 'Processing',
        "created_at" : start_time,
        "updated_at" : start_time,
        'result' : None
    }


    #Simulate background processing
    await asyncio.sleep(task.delay)

    # Produce result

    processed_result = task.text.upper()

    # update the task info

    task_db[task_id]['status'] = 'completed'
    task_db[task_id]['updated_at'] = datetime.utcnow()
    task_db[task_id]['result'] = processed_result

    return {
        'message' : 'Task processed Successfully',
        'task_id' : task_id,
        'input_text' : task.text,
        'result' : processed_result
    }


# Get task by ID
@app.get('/tasks/{task_id}')
def get_task(task_id : str):

    if task_id not in task_db:
        raise HTTPException(status_code=404, detail= "Task not found")
    
    return task_db[task_id]

@app.get('/tasks')
def get_all_tasks(status : str | None = None):
    if status:
        filtered = {tid : data for tid, data in task_db.items() if data['status'] == status}
        return filtered
    return task_db


@app.delete('/task/{task_id}')
def delete_task(task_id : str):
    if task_id not in task_db:
        raise HTTPException(status_code= 404, detail= 'Task not found')
    
    del task_db[task_id]

    return {'message' : 'Task deleted Successfully'}