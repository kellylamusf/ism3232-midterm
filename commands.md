# Terminal Record: Brightline Print Shop

## 1. Building the Project
mkdir, 
cd, 
ls, 
.gitignore, 
pip freeze, 
git remote add origin, 
git push, 
python3 -m venv .venv, 
source .venv/bin/activate, 
python3, 
clear

## 2. The virtual environment
/home/klam9/ism3232_midterm/.venv/bin/python3

## 3. The project structure
├── README.md
├── __pycache__
├── business_rules.py
├── commands.md
├── main.py
├── requirements.txt
└── tests
    ├── __init__.py
    ├── __pycache__
    └── test_business_rules.py

## 4. Every function and test
tests/test_business_rules.py
3:def test_print_cost_is_price_times_copies():
6:def test_discount_199_copies_is_none():
9:def test_discount_200_copies_is_8_percent():
12:def test_discount_999_copies_is_8_percent():
15:def test_discount_1000_copies_is_15_percent():
18:def test_student_org_discount_200_copies_is_13_percent():
21:def test_student_org_discount_1000_copies_is_20_percent():
24:def test_students_org_changes_job_total():
28:def test_setup_fee_below_40():
31:def test_no_setup_fee_at_40():
34:def test_proof_not_required_at_300():
37:def test_proof_required_over_300():
40:def test_overnight_not_needed_at_500_copies():
43:def test_overnight_needed_over_500_copies():
46:def test_overnight_not_needed_at_400():
49:def test_overnight_needed_over_400():
52:def test_total_invoiced_adds_two_jobs():
59:def test_largest_job_returns_biggest_title():
66:def test_largest_job_tie_returns_first():
73:def test_largest_job_empty_list_returns_empty_string():
76:def test_format_job_line_shows_yes_and_no():
business_rules.py
18:def calculate_print_cost(copy_price: float, copies: int) -> float:
22:def get_volume_discount(copies: int, student_org: bool = False) -> float:
34:def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
43:def requires_proof(total: float) -> bool:
47:def needs_overnight_run(copies: int, total: float) -> bool:
51:def total_invoiced(jobs: list) -> float:
59:def largest_job(jobs: list) -> str:
74:def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str:

## 5. Which files print 
main.py
commands.md
tests/test_business_rules.py
business_rules.py

## 6. The commit history 
b53e1c2 (HEAD -> main, origin/main) added a README for people who wants to be able to run the project
8c33d15 added 11 more pytests to test out each function in business_rules.py
92a3b59 imported business rules and added 11 tests for my functions
41da318 had to fix my get_volume_discount function, it was not applying the student discount so some of the outputs in main.py was wrong.
40e5453 imported my functions from businesss_rules and added the printed line for each job and the summary of the total invoiced, average job total, largest job total, proofs required, and overnight runs.
3bfe5d5 added return statements to each defined functions in business_rules.py as well as the Brightline Print Shop pricing and discount
008c6b2 ism3232 midterm: added the jobs table lists into main.py
ca9ee22 ism3232 midterm: added functions and stated what each functions does in business_rules.py