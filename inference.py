# Inference Engine
# Forward Chaining + Backward Chaining

from rules import (
    check_age,
    check_income,
    check_credit_score,
    check_existing_loan,
    check_repayment
)


# ---------------- FORWARD CHAINING ----------------

def forward_chaining(applicant):

    results = []
    eligible = True

    age_result, age_reason = check_age(applicant["age"])
    results.append(age_reason)

    if not age_result:
        eligible = False

    income_result, income_reason = check_income(applicant["income"])
    results.append(income_reason)

    if not income_result:
        eligible = False

    credit_rating, credit_reason = check_credit_score(
        applicant["credit_score"]
    )
    results.append(credit_reason)

    if credit_rating == "Poor":
        eligible = False

    loan_result, loan_reason = check_existing_loan(
        applicant["existing_loan"]
    )
    results.append(loan_reason)

    repayment_result, repayment_reason = check_repayment(
        applicant["repayment_history"]
    )
    results.append(repayment_reason)

    if not repayment_result:
        eligible = False

    if eligible:
        decision = "ELIGIBLE"
    else:
        decision = "NOT ELIGIBLE"

    return decision, results


# ---------------- BACKWARD CHAINING ----------------

def backward_chaining(applicant):

    reasons = []

    # Goal: Prove that applicant is eligible

    age_result, age_reason = check_age(applicant["age"])

    if not age_result:
        reasons.append(age_reason)
        return "NOT ELIGIBLE", reasons

    reasons.append(age_reason)

    income_result, income_reason = check_income(applicant["income"])

    if not income_result:
        reasons.append(income_reason)
        return "NOT ELIGIBLE", reasons

    reasons.append(income_reason)

    credit_rating, credit_reason = check_credit_score(
        applicant["credit_score"]
    )

    if credit_rating == "Poor":
        reasons.append(credit_reason)
        return "NOT ELIGIBLE", reasons

    reasons.append(credit_reason)

    loan_result, loan_reason = check_existing_loan(
        applicant["existing_loan"]
    )

    if not loan_result:
        reasons.append(loan_reason)
        return "NOT ELIGIBLE", reasons

    reasons.append(loan_reason)

    repayment_result, repayment_reason = check_repayment(
        applicant["repayment_history"]
    )

    if not repayment_result:
        reasons.append(repayment_reason)
        return "NOT ELIGIBLE", reasons

    reasons.append(repayment_reason)

    return "ELIGIBLE", reasons