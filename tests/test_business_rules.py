from business_rules import calculate_job_total, calculate_print_cost, format_job_line, get_volume_discount, largest_job, needs_overnight_run, requires_proof, total_invoiced

def test_print_cost_is_price_times_copies():
    assert round(calculate_print_cost(0.25, 100), 2) == 25.00

def test_discount_199_copies_is_none():
    assert get_volume_discount(199) == 0.0

def test_discount_200_copies_is_8_percent():
    assert get_volume_discount(200) == 0.08

def test_discount_999_copies_is_8_percent():
    assert get_volume_discount(999) == 0.08

def test_discount_1000_copies_is_15_percent():
    assert get_volume_discount(1000) == 0.15

def test_student_org_discount_200_copies_is_13_percent():
    assert round(get_volume_discount(200, True), 2) == 0.13

def test_student_org_discount_1000_copies_is_20_percent():
    assert round(get_volume_discount(1000, True), 2) == 0.20

def test_students_org_changes_job_total():
    assert round(calculate_job_total(0.50, 300), 2) == 138.00
    assert round(calculate_job_total(0.50, 300, True), 2) == 130.50

def test_setup_fee_below_40():
    assert round(calculate_job_total(39.99, 1), 2) == 54.99

def test_no_setup_fee_at_40():
    assert round (calculate_job_total(40.00, 1), 2) == 40.00

def test_proof_not_required_at_300():
    assert requires_proof(300.00) is False

def test_proof_required_over_300():
    assert requires_proof(300.01) is True 

def test_overnight_not_needed_at_500_copies():
    assert needs_overnight_run(500, 100.00) is False

def test_overnight_needed_over_500_copies():
    assert needs_overnight_run(501, 100.00) is True

def test_overnight_not_needed_at_400():
    assert needs_overnight_run(100, 400.00) is False

def test_overnight_needed_over_400():
    assert needs_overnight_run(100, 400.01) is True

def test_total_invoiced_adds_two_jobs():
    jobs = [
        {"title": "Stickers", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Flags", "copy_price": 2.00, "copies": 100, "student_org": False},
    ]
    assert round(total_invoiced(jobs), 2) == 300.00

def test_largest_job_returns_biggest_title():
    jobs = [
        {"title": "Stickers", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Flags", "copy_price": 2.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(jobs) == "Flags"

def test_the_same_largest_job_returns_first():
    jobs = [
        {"title": "First", "copy_price": 1.00, "copies": 100, "student_org": False},
        {"title": "Second", "copy_price": 1.00, "copies": 100, "student_org": False},
    ]
    assert largest_job(jobs) == "First"

def test_largest_job_empty_list_returns_empty_string():
    assert largest_job([]) == ""

def test_format_job_line_shows_yes_and_no():
    line = format_job_line("Programs", 348, True, False)
    assert line == "Programs: $348.00 | proof: yes | overnight run: no"





