from kitchen.models import *
from django.utils import timezone
import datetime

monday = (timezone.now() + datetime.timedelta(days=-timezone.now().weekday(), weeks=0)).date()
week = [monday + datetime.timedelta(days=i) for i in range(0,7)]


lunch_descriptions = [
"Chicken Parmigiana\nBoneless, skinless chicken breast breaded and baked with cheese and a light marinara sauce",
"Stuffed Chicken Medallions\nBoneless chicken breast stuffed with spinach and cheese, baked then topped with a light bechamel sauce",
"Chicken Marsala\nBoneless chicken breast sauteed with mushrooms, Marsala wine, diced tomatoes and olives",
"Tuna Ahi Salad with Wasabi Sauce",
"Charbroiled Tri-ip\nMarinated in a blend of spices, charbroiled and served 'London Broil' style",
"Oriental Chicken or Beef Stir Fry\nBoneless chicken OR sirloin steak stir-fried with peppers, onions, carrots, sesame seeds and tossed with a teriyaki glaze",
"Stuffed Sole\nGrilled and stuffed with shrimp and Dungeness crab and topped with melted cheese and a light lemon butter sauce",]

grill_options = [
'American Angus Hamburgers',
'Avacado Wrap with Chicken',
'4-Meat Chili',
"Ahi-Ahi-Wahi Burger",
'Chicken Thai Curry Wrap',
'Big Boy Burger with A1 Steak Sauce',
'Pesto and Italian Meat Panini',
'Nutella Crepe | Turkey and Peach Jam Crepe']

dinner_descriptions = [
"Penne a la Vodka\nBuffalo Chicken Wings with Ranch & Blue Cheese Sauce",
"Braised Short Ribs with Red Wine Mustard Sauce\nRed Bliss Mashed Potato",
"Roast Salmon and Tilapia\nGarlic Parsley Crust | Tomatoes | Shallots | Capers",
"California Rolls, Avacado Rolls, Shrimp Sashimi, Tuna Salad",
"Herb Roasted Chicken\nOlive Oil | Rosemary | Sage | Parsley",
"Twice Cooked Beef Short Ribs\nAsian Chili Sauce | Soy Glaze | Ginger | Scallions | White Sesame Seeds",
"Baked Ziti\nCream Spinach Sauce | Parmesan Cheese",
"Butter Basted Roasted Turkey\nHomemade Gravy | Cranberry Orange Sauce",
]

plated_options = ['Baked Chicken with Rice and Beans',
"Baked Macaroni and Cheese\nCheddar | Monterey Jack Cheese | Crispy Herb Breading",
"Oven Roasted Salmon & Tilapia\nGarlic Parsley Crust | Tomatoes | Shallots | Capers"]

salads = ['Apple, Cherry, Pecan & Roasted Feta Salad',
'Cumin Scented Carrot Salad',
'Summer Squash Salad',
'Roasted Beet Salad',
'Farro Salad',
'Fingerling Potato Salad',
'Fava Beans and Pomegranate',
'Artichoke and Piquillo Salad',]


omlette = ['Feta Cheese and Ham Omlette', 'Ranchero Omlette with Chili']
meals = []
for i in range(0,5):
    a = Lunch(day=week[i], sophomore_limit = 20, description=lunch_descriptions[i], salad=salads[i], grill_special=grill_options[i])
    b = Dinner(day=week[i], sophomore_limit = 20, description=dinner_descriptions[i], salad=salads[i])

    a.save()
    b.save()

    meals.append((a,b))

for i in range(5,7):
    a = Brunch(day=week[i], sophomore_limit = 20, description=lunch_descriptions[i], omlette=omlette[i-5], grill_special=grill_options[i])
    b = Dinner(day=week[i], sophomore_limit = 20, description=dinner_descriptions[i], salad=salads[i])

    a.save()
    b.save()

    meals.append((a,b))


# Add the plated options
meals[2][1].plated_option = plated_options[0]
meals[4][1].plated_option = plated_options[1]
meals[6][1].plated_option = plated_options[2]


# Do some special stuff
meals[3][1].sophomore_limit = 0
meals[3][1].special_note = "Members only dinner"
meals[3][1].name = "Sushi Pub Night"
meals[6][0].name = "sophomore Brunch"

for i in range(5,7):
    meals[i][0].meals="Brunch"

for m in meals:
    m[0].save()
    m[1].save()

