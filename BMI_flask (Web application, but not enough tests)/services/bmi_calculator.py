def bmi_score(height: float, weight: float) -> float:
    # always provide credit for the source of any calculation
    # https://www.cdc.gov/nccdphp/dnpao/growthcharts/training/bmiage/page5_1.html
    # https://www.medicalnewstoday.com/articles/255712
    # Formula: weight (lb) / [height (in)]2 x 5734

    return round((weight / (height ** 2.5) * 5734), 2)


def bmi_category(score):
    if score < 16:
        return 'extremely underweight'
    elif 16 <= score < 18.5:
        return 'underweight'
    elif 18.5 <= score < 25:
        return 'healthy'
    elif 25 <= score < 30:
        return 'overweight'
    elif score >= 30:
        return 'obese'


def bmi_evaluation(height, weight):
    bmi = bmi_score(height, weight)
    category = bmi_category(bmi)
    return f'Your BMI is: {bmi} and you are: {category}'
