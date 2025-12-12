# LogicFrame 🧠
> Your Personal Life Operating System.

LogicFrame is a modular, open-source ERP for personal life management. It integrates Financial Tracking, Habit Building, and Task Management into a single, cohesive dashboard using Atomic Design principles.

## 🚀 Features

### 💰 Finance Module (Atomic Transactions)
- Double-entry bookkeeping logic.
- Atomic Transactions: Ensuring data integrity with transaction.atomic.
- Expense & Income tracking with dynamic categories.
- Real-time Net Worth calculation.

### 🔄 Habit Module (EchoLoop)
- Daily habit tracking loop.
- Visual streaks and progress bars.
- Integration with dashboard for daily overview.

### ⚡ Tech Stack
- Backend: Django 6, Django Rest Framework (DRF)
- Frontend: Django Templates + Tailwind CSS + HTMX + Alpine.js
- Database: SQLite (Dev) / PostgreSQL (Prod)

## 🛠 Installation

1. Clone the repo:
   `bash
   git clone [https://github.com/sajadqadir01/LogicFrame.git](https://github.com/sajadqadir01/LogicFrame.git)
   cd LogicFrame
2. create virtual environment: python -m venv venv
source venv/bin/activate
On Windows: venv\Scripts\activate
3. Install Dependencies: pip install -r requirements.txt
4. Migrate & Run: python manage.py migrate
python manage.py runserver


Built with ❤️ by sajad.