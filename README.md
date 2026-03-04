# 🎓 School System Project

I developed this project to test and showcase my new skills! 🚀  

In this project, you can view the **class schedules** for grades **1 through 11**.  

## 📝 Registration & Login
- During registration, a student selects their class.  
- After logging in, the student can see their **own schedule**.  
- There is also a **role selection** option, where you can log in as:
  - 👨‍🎓 **Student**
  - 👩‍🏫 **Teacher**
  - 👨‍💼 **Director**

## 👩‍🏫 Teacher Role
- Teachers can only view lessons related to their subject.  
- They can also see **which class** the lesson belongs to.  
- Teachers have the ability to:
  - ⏰ Change the lesson time  
  - ❌ Delete the lesson if necessary  

## 👨‍💼 Director Role
- Directors can view **all class schedules**.  
- They also have access to the **Action Log**, where they can monitor:  
  - Which teacher made changes  
  - What kind of updates were performed  
- This provides full **control and oversight** over the system. 🔍  

## 🚀 How to Run

To run this project on your local machine, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository_github_url>
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd school_system
    ```

3.  **Create and activate a virtual environment:**
    ```bash
    # Create virtual environment
    python -m venv venv

    # Activate on Windows
    venv\Scripts\activate

    # Activate on MacOS/Linux
    source venv/bin/activate
    ```

4.  **Install the required packages (from `requirements.txt`):**
    *(To create this file, run `pip freeze > requirements.txt` in the project directory)*
    ```bash
    pip install -r requirements.txt
    ```

5.  **Apply database migrations and create a superuser:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

6.  **Start the development server:**
    ```bash
    python manage.py runserver
    ```
    You can now access the project in your browser at `http://127.0.0.1:8000/`.

---

✨ This project reflects my journey of learning and applying new abilities in backend and web development.
