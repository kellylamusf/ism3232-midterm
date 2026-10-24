# business_rules.py
# Author: Kelly Lam


def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before any discount (rule 1)."""

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the discount rate as a decimal, so 8%, is 0.08 (rules 2 and 3)."""

def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Returns the job total for one job: the discounted cost, plus the setup fee when it applies (rule 4). 
    it must call your first two functions."""


def requires_proof(total: float) -> bool:
    """Returns True when the job total requires a printed proof (rule 5), otherwise False."""

def needs_overnight_run(copies: int, total: float) -> bool:
    """Returns True when the job needs an overnight press run (rule 6), otherise False.""" 

def total_invoiced(jobs: list) -> float:
    """Returns the sum of the job totals for every job in the list. It must use a for loop that calls
    calculate_job_total."""

def largest_job(jobs: list) -> str:
    """Returns the title of the job with the largest job total. If two are tied for largest, it returns the one
    that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls 
    calculate_job_total."""

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str: 
    """Return one line of the report, such as Flyers: $40.00 | proof: no | overnight run: no. Each True/False 
    value is shown as yes or no, and the amount alaways has two decimal places.""" 


