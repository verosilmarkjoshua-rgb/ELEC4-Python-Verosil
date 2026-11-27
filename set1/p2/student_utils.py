# Full Name: Mark Joshua Verosil
# Section: IV-BSIT-A
# Activity: P2 - Custom Module
# Date: November 27, 2026


def get_average(list_of_scores):
    total = sum(list_of_scores)
    return total / len(list_of_scores)


def get_status(average_score):
    if average_score >= 75:
        return "PASSED"
    else:
        return "FAILED"


def get_highest(list_of_scores):
    return max(list_of_scores)


def get_lowest(list_of_scores):
    return min(list_of_scores)
