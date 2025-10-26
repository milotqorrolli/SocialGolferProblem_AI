Social Golfers Problem Solver (AI Search Project)

This project solves the Social Golfers Problem using uninformed search techniques (Depth-First Search and Depth-Limited Search).
It includes a Streamlit web interface that allows users to define the number of players, group size, and search algorithm to find the maximum number of weeks golfers can play without any two players being grouped together more than once.

Live Demo: https://socialgolfersproblem.streamlit.app/

1. Problem Description

The Social Golfers Problem (SGP) asks:

Given n golfers, who play in groups of p each week, for how many weeks can they play so that no two golfers ever play in the same group more than once?

Formally:
n = g × p → total players
g → number of groups
p → players per group
w → maximum number of valid weeks (to be found)

This project uses Depth-First Search (DFS) and Depth-Limited Search (DLS) with backtracking to explore valid configurations of weekly groupings.

2. Project Structure
SocialGolferProblem_AI/
│
├── backend/
│   ├── __init__.py
│   ├── solver.py                # Core search logic (DFS & DLS)
│
├── frontend/
│   ├── app.py                   # Streamlit app UI
│
├── requirements.txt
└── README.md

3. Installation and Setup

Follow these steps to run the project locally.

Step 1: Clone the Repository
git clone https://github.com/milotqorrolli/SocialGolferProblem_AI.git
cd SocialGolferProblem_AI

Step 2: Create a Virtual Environment
python -m venv .venv

Step 3: Activate the Virtual Environment

On Windows:
.\.venv\Scripts\activate


On macOS / Linux:
source .venv/bin/activate

Step 4: Install Dependencies
pip install -r requirements.txt

4. Running the Application

Once dependencies are installed and the virtual environment is active, run the Streamlit app:

cd frontend
streamlit run app.py


Then open the URL shown in the terminal (usually http://localhost:8501) in your browser.

5. Usage

Open the app in your browser.

Input:

Number of Players (n) – e.g., 32
Players per Group (p) – e.g., 4
Algorithm – choose between DFS or DLS
Depth Limit – for DLS, specify the maximum search depth
Click Run Solver.
The app will display:
The maximum number of valid weeks (w)
Weekly group configurations

6. Algorithms Used
Depth-First Search (DFS) - Explores all possible weekly combinations recursively, backtracking when a constraint is violated.

Depth-Limited Search (DLS) - Same as DFS but with a maximum depth (week limit), preventing exploration beyond a certain level.

Both methods ensure that no pair of golfers ever plays together more than once.

7. Technologies

Python 3.10+
Streamlit (frontend)
Custom search logic (DFS & DLS)
itertools, random, and standard Python libraries

8. Author

Milot Qorrolli
Project for Artificial Intelligence course
University of Prishtina, 2025