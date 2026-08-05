#Calc for operating margin
def calculate_margin(numerator, denominator):
    return (numerator / denominator) * 100
#For performance segment - simple formula for growth calculation
def calculate_growth(current, previous):

    return ((current - previous) / previous) * 100