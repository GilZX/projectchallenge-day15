MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffe":18
        },
        "cost":1.5,
        "avaible":True
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffe":24
        },
        "cost":2.5,
        "avaible":True
    },
    "Cappuccino":{
        "ingredients":{
            "water":250,
            "coffe":24,
            "milk":100
        },
        "cost":3.00,
        "avaible":True
    }
}
options=['espresso','latte','Cappuccino']

INPUTS=[
    {"water": 300, "availability": True},
    {"milk": 200, "availability": True},
    {"coffe": 100, "availability": True},
    {"money": 0}
]

def desscount_ingredients(variety,inputs,menu):
    if variety=='espresso':
        inputs[variety]["water"]-menu['espresso']['ingredients']['water']




for item in options:
    if MENU[item]["avaible"]==True:
        print(item)


input_flavours = input(f"What would you like ? {options} :")


def check_avaible_taste(input,inputs):
    water_nesesary= MENU[input]["ingredients"]["water"]
    milk_nesesary=MENU[input]["ingredients"]["milk"]
    coffe_nesesary=MENU[input]["ingredients"]["coffe"]

    if (inputs[0]["water"] - water_nesesary < 0) or (inputs[1]["milk"] - milk_nesesary < 0) or (inputs[2]["coffe"] - coffe_nesesary < 0):
        return False
    else:
        return True






def coffe_machine(option):
    off_state=False







