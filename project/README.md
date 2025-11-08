#  Django Signals Project – Accuknox Trainee Task

This project demonstrates **Django Signals** behavior and a **custom Python class** implementation as part of the Accuknox Django Trainee Assessment.

---

## Features

### 1️. Django Signals Tests

#### Questions Covered

-> Q1 | Are Django signals synchronous or asynchronous? | Demonstrated via timing and thread output. 
-> Q2 | Do signals run in the same thread as the caller? | Verified using `threading.current_thread()`.
-> Q3 | Do signals run in the same database transaction as the caller? | Proven using `transaction.set_rollback(True)`.

####  Endpoints
| URL                   |      Description |

| `/create_demo/`       | Tests synchronous execution |
| `/thread_demo/`       | Tests if signals run in the same thread |
| `/transaction_demo/`  | Tests database transaction behavior |

---

### 2️. Custom Python Class

**File:** `rectangle_class.py`

Implements a `Rectangle` class that:
- Accepts `length` and `width` during initialization
- Can be iterated to yield:
  ```python
  {'length': value}
  {'width': value}

# 1. Create and activate virtual environment
python -m venv myenv
myenv\Scripts\activate   # On Windows
source myenv/bin/activate # On Mac/Linux

# 2. Install dependencies
pip install django

# 3. Run migrations
python manage.py makemigrations
python manage.py migrate

# 4. Start the server
python manage.py runserver

Then visit:

http://127.0.0.1:8000/create_demo/
http://127.0.0.1:8000/thread_demo/
http://127.0.0.1:8000/transaction_demo/
