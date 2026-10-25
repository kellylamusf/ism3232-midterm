# ISM3232 Midterm: Brightline Print Shop

- **Name:** Kelly Lam
- **Version:** 
- **Date:** 10/25/2026

## What this program does 
This program works for the Brightline Print Shop and prints out the pricing for the shop. For each job that is performed it prints out discounted job total, apply a setup fee when approriate, and decides whether a job needs a printed proof or an overnight press run. It also prints out a summary for the total invoiced, average job total, largest job total, proofs required, and overnight runs. 

## Business Rules
1. The print cost is the price per copy times the number of copies
2. The discount depends on the number of copies. Fewer than 200 copies: no discount. 200-999 Copies: 8%, 1000+ Copies: 15%
3. A registered student organization gets an extra 5% discount only on jobs of 200 copies or more. For them, 8% becomes 13%, and 15% becomes 20%. 
4. A setup fee is added when the discounted cost is below $40 
5. A job total of more than $300 requires a printed proof
6. A job that needs an overnight press run when it has more than 500 copies or its job total is over $400.  

## How to Run 
1. Access the repository, then run cd ism3232_midterm
2. Activate the virtual environment, python3 -m venv .venv, source .venv/bin/activate 
3. Install the requirements, pip install pytest ruff && pip freeze > requirements.txt
4. Run the program, python3 main.py

## How to Test
In order to run the test you must run pytest -v. All 21 tests should be passed. 

## Files in This Repository
- 'business_rules.py': it has the rules and pricing functions 
- 'main.py': prints out the job lists and the six summary lines 
- 'commands.md': what commands were used to create the program
- 'README.md': a file that has what the program does, business rules, how to run the program, how to test it, the and the files in the repository.
- 'requirements.txt': what packages you need to run the program 
- '.gitignore': ignores .venv/, __pycache__/, and *.pyc
- 'tests/test_business_rules.py': the pytests for every function 
- 'tests/__init__.py': test folder

## AI Use Statement
I did not use AI on this exam 