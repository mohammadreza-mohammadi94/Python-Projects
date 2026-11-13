# TODO Flask API

This repository contains a simple **TODO API** built using the **Flask framework**. The project implements a RESTful API to perform CRUD (Create, Read, Update, Delete) operations on a list of tasks, allowing you to manage a TODO list programmatically.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [API Endpoints](#api-endpoints)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **TODO Flask API** is a lightweight application designed to provide an easy way to create and manage a task list. It demonstrates the use of Flask to build RESTful services, following best practices in API development.

---

## Features

- **Add a Task**: Create new tasks with a title and description.
- **Retrieve Tasks**: Get all tasks or a specific task by ID.
- **Update a Task**: Modify the details of an existing task.
- **Delete a Task**: Remove tasks from the list.
- **In-Memory Storage**: Task data is stored in memory for simplicity.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mohammadreza-mohammadi94/TODO-Flask-API.git
   cd TODO-Flask-API
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the API at:
   ```
   http://127.0.0.1:5000/
   ```

---

## API Endpoints

### 1. **Get All Tasks**
   **Endpoint**: `GET /tasks`  
   **Description**: Retrieves the list of all tasks.

   **Response Example**:
   ```json
   [
       {"id": 1, "title": "Task 1", "description": "Description of Task 1"},
       {"id": 2, "title": "Task 2", "description": "Description of Task 2"}
   ]
   ```

### 2. **Get a Task by ID**
   **Endpoint**: `GET /tasks/<int:id>`  
   **Description**: Retrieves a specific task by its ID.

   **Response Example**:
   ```json
   {"id": 1, "title": "Task 1", "description": "Description of Task 1"}
   ```

### 3. **Add a New Task**
   **Endpoint**: `POST /tasks`  
   **Description**: Creates a new task.  
   **Request Body**:
   ```json
   {
       "title": "New Task",
       "description": "Description of the new task"
   }
   ```

   **Response Example**:
   ```json
   {"message": "Task added successfully", "task": {"id": 3, "title": "New Task", "description": "Description of the new task"}}
   ```

### 4. **Update a Task**
   **Endpoint**: `PUT /tasks/<int:id>`  
   **Description**: Updates the details of a specific task.  
   **Request Body**:
   ```json
   {
       "title": "Updated Task",
       "description": "Updated description"
   }
   ```

   **Response Example**:
   ```json
   {"message": "Task updated successfully", "task": {"id": 1, "title": "Updated Task", "description": "Updated description"}}
   ```

### 5. **Delete a Task**
   **Endpoint**: `DELETE /tasks/<int:id>`  
   **Description**: Deletes a specific task by ID.

   **Response Example**:
   ```json
   {"message": "Task deleted successfully"}
   ```

---

## Usage

- Start the Flask server using the steps outlined in the [Installation](#installation) section.
- Use tools like **Postman**, **cURL**, or **a frontend client** to interact with the API endpoints.

Example cURL command to add a new task:
```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title": "Learn Flask", "description": "Build a TODO API"}'
```

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Commit your changes: `git commit -m "Add some feature"`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute it as needed.
