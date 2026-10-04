# Loan Eligibility Rules

def check_age(age):
    if 21 <= age <= 60:
        return True, "Age is within the acceptable range."
    return False, "Age must be between 21 and 60 years."


def check_income(income):
    if income >= 25000:
        return True, "Monthly income meets the minimum requirement."
    return False, "Monthly income is below the minimum requirement."


def check_credit_score(credit_score):
    if credit_score >= 750:
        return "Excellent", "Credit score is excellent."
    elif credit_score >= 650:
        return "Good", "Credit score is good."
    elif credit_score >= 600:
        return "Average", "Credit score is average."
    else:
        return "Poor", "Credit score is poor."


def check_existing_loan(existing_loan):
    if existing_loan == "No":
        return True, "Applicant has no existing loan."
    return False, "Applicant has an existing loan."


def check_repayment(repayment_history):
    if repayment_history == "Good":
        return True, "Previous repayment history is good."
    elif repayment_history == "Average":
        return True, "Previous repayment history is average."
    return False, "Previous repayment history is poor."