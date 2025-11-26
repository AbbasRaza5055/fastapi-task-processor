# 🚀 FastAPI Task Processor API

A real-world **FastAPI mini project** that demonstrates:

- async/await processing  
- request & response handling  
- Pydantic models  
- path & query parameters  
- error handling  
- custom JSON  
- filtering system  
- UUID task management  
- in-memory database  

Perfect for beginners learning backend APIs or for building portfolio projects.

## 📁 Project Structure

fastapi-task-processor/
│── main.py
│── requirements.txt
│── .gitignore
└── README.md


---

## ⚙️ Installation & Running

1️⃣ Install dependencies

```bash
pip install -r requirements.txt

2️⃣ Run the FastAPI server
uvicorn main:app --reload

3️⃣ Open API Docs (Swagger)

📌 http://127.0.0.1:8000/docs

🧠 Features
✔ Create new tasks

Accepts text

Simulates async processing

Converts text to uppercase

Tracks created/updated timestamps

✔ View all tasks

Optional filter

/tasks?status=completed

/tasks?status=processing

✔ Get a single task by ID
✔ Delete a task
🛠 Endpoints
➕ POST /tasks

Body Example:

{
  "text": "abbas learning fastapi",
  "delay": 2
}

📄 GET /tasks

Optional filters:

/tasks?status=completed
/tasks?status=processing

📌 GET /tasks/{task_id}

Returns a specific task.

❌ DELETE /tasks/{task_id}

Deletes a task.

🧪 Sample Response
{
  "message": "Task processed successfully",
  "task_id": "c0491ccb-09d8-4cd6-b2c5-54a99c7f8c33",
  "input_text": "hello world",
  "processed_text": "HELLO WORLD"
}

🚀 Future Improvements

Add database support (MongoDB / PostgreSQL)

Add authentication (JWT)

Convert into full AI pipeline

Add React frontend dashboard

👨‍💻 Author

Abbas
FastAPI | Python | AI Engineer
