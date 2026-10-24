# business_rules.py
# Author: Kelly Lam

"""Brightline Print Shop Pricing"""

TIER_ONE_COPIES = 200
TIER_TWO_COPIES = 1000
NO_DISCOUNT = 0.0
DISCOUNT_ONE = 0.08
DISCOUNT_TWO = 0.15
STUDENT_ORG_DISCOUNT = 0.05
SETUP_FEE = 15.0
SETUP_FEE_LIMIT = 40.0
PROOF = 300.0 
OVERNIGHT_COPIES_LIMIT = 500
OVERNIGHT_TOTAL_LIMIT = 400.0

def calculate_print_cost(copy_price: float, copies: int) -> float:
    """Return the print cost before any discount (rule 1)."""
    return copy_price * copies

def get_volume_discount(copies: int, student_org: bool = False) -> float:
    """Return the discount rate as a decimal, so 8%, is 0.08 (rules 2 and 3)."""
    if copies >= TIER_TWO_COPIES:
        rate = DISCOUNT_TWO
    elif copies >= TIER_ONE_COPIES:
        rate = DISCOUNT_ONE
    else:
        return NO_DISCOUNT
    if student_org:
        rate += STUDENT_ORG_DISCOUNT
    return rate

def calculate_job_total(copy_price: float, copies: int, student_org: bool = False) -> float:
    """Returns the job total for one job: the discounted cost, plus the setup fee when it applies (rule 4). 
    it must call your first two functions."""
    cost = calculate_print_cost(copy_price, copies)
    discounted = cost * (1 - get_volume_discount(copies, student_org))
    if discounted < SETUP_FEE_LIMIT:
        discounted += SETUP_FEE
    return discounted

def requires_proof(total: float) -> bool:
    """Returns True when the job total requires a printed proof (rule 5), otherwise False."""
    return total > PROOF

def needs_overnight_run(copies: int, total: float) -> bool:
    """Returns True when the job needs an overnight press run (rule 6), otherise False.""" 
    return copies > OVERNIGHT_COPIES_LIMIT or total > OVERNIGHT_TOTAL_LIMIT

def total_invoiced(jobs: list) -> float:
    """Returns the sum of the job totals for every job in the list. It must use a for loop that calls
    calculate_job_total."""
    total = 0.0
    for job in jobs:
        total += calculate_job_total(job["copy_price"], job["copies"], job["student_org"])
    return total

def largest_job(jobs: list) -> str:
    """Returns the title of the job with the largest job total. If two are tied for largest, it returns the one
    that comes first in the list. An empty list returns an empty string, "". It must use a for loop that calls 
    calculate_job_total."""
    best_title = ""
    best_total = 0.0
    first = True
    for job in jobs:
        total = calculate_job_total(job["copy_price"], job["copies"], job["student_org"])
        if first or total > best_total:
            best_title = job["title"]
            best_total = total
            first = False
    return best_title

def format_job_line(title: str, total: float, proof: bool, overnight_run: bool) -> str: 
    """Return one line of the report, such as Flyers: $40.00 | proof: no | overnight run: no. Each True/False 
    value is shown as yes or no, and the amount alaways has two decimal places.""" 
    proof_text = "yes" if proof else "no"
    overnight_text = "yes" if overnight_run else "no"
    return f"{title}: ${total:.2f} | proof: {proof_text} | overnight run: {overnight_text}"



