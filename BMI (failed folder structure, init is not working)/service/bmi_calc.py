def bmi_score(height: float, weight: float) -> float:
    # always provide credit for the source of any calculation
    bmi = (weight/(height**2.5)) * 1.3
    return bmi

def bmi_category(bmi_score):
    if (bmi_score < 16):
        return 'extremely underweight'
    elif (bmi_score >= 16 and bmi_score < 18.5):
        return 'underweight'
    elif (bmi_score >= 18.5 and bmi_score < 25):
        return 'healthy'
    elif (bmi_score >= 25 and bmi_score < 30):
        return 'overweight'
    elif (bmi_score >= 30):
        return 'obese'

def bmi_evaluation(height, weight):
    bmi = bmi_score(height, weight)
    category = bmi_category(bmi)
    return (f'Your BMI is: {bmi} and you are: {category}')

