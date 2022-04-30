def give_recommendation(score,target):
    if score < 16:
        return "Get onto eating proteins and doing simple workouts to get your body into shape"
    elif 16 <= score < 18.5:
        return "You need to eat more proteins and give your body more exercise"
    elif 18.5 <= score < 25:
        return "Good work in watching your health"
    elif 25 <= score < 30:
        return "Reduce your protein levels and do more exercise"
    elif score >= 30:
        return "Lower your proteins consumption \n start a workout program \n consult a health personelle for advice"


