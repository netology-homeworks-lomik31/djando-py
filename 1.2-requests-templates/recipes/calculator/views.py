from django.shortcuts import render

DATA = {
    "omlet": {
        "яйца, шт": 2,
        "молоко, л": 0.1,
        "соль, ч.л.": 0.5,
    },
    "pasta": {
        "макароны, г": 0.3,
        "сыр, г": 0.05,
    },
    "buter": {
        "хлеб, ломтик": 1,
        "колбаса, ломтик": 1,
        "сыр, ломтик": 1,
        "помидор, ломтик": 1,
    },
}

def gen_recipe(req, dish):
    try: servings = float(req.GET.get("servings", 1))
    except: servings = 0

    context = {
        "servings": servings,
        "recipe": dict(map(lambda i: (i, round(DATA[dish][i]*servings, 3)), DATA[dish]))
    }
    return render(req, "calculator/index.html", context)
