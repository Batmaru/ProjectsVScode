#8.16
def sandwich(name:str, ingredients: list)->dict[str, list]:
    person_dict={
        'name': name,
        'ingredients':ingredients
    }
    print(f"gli ingredienti del panino di {person_dict['name']} sono: {person_dict['ingredients']}")


sandwich('Marco', ['Prosciutto', 'Formaggio'])
sandwich('Giulia', ['Salame', 'Mozzarella', 'Pomodoro'])
sandwich('Luca', ['Pollo', 'Insalata', 'Maionese', 'Pomodoro'])