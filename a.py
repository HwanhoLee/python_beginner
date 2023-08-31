"""
from requests import get

websites=(
  "https://naver.com",
  "https://google.com",
  "tiktok.com",
  "airbnb.com",
)

results = {}

for website in websites:
  if not website.startswith("https://"):
    website= f"https://{website}"
  response = get(website)
  if response.status_code==200:
    results[website] = "ok!"
  else:
   results[website] = "Failed"

print(results)
"""


# Juice Maker (recap)
def make_juice(fruit):
    return f"{fruit}+ 🍵"


def add_ice(ice):
    return f"{ice}+ 🧊"


def add_sugar(sugar):
    return f"{sugar}+🍭"


juice = make_juice("🍇")
iced_juice = add_ice(juice)
Perfect_juice = add_sugar(iced_juice)

print(Perfect_juice)
""""
#python casino
from random import randint


pc_choice= randint(1,100)

Players = True

while Players:
  users_choice=int(input("Choose number."))
  if pc_choice==users_choice:
    print ("You Won!")
    Players = False

  elif pc_choice>=users_choice:
    print ("Higher!")

  elif pc_choice<=users_choice:
    print ("Lower!")
    """

# list, tuple, and dictionary
player = {"name": "nico", "age": 12, "alive": True, "fav_food": ["🥩"]}
print(player.get("age"))
print(player["fav_food"])
player.pop("age")
print(player)
player["xp"] = 1500
print(player)
player["fav_food"].append("🍟")
print(player)
print(player.get("name"))
print(player["alive"])
player["fav_food"].append("🍔")
print(player)

# for...in..
websites = (
    "https://naver.com",
    "https://google.com",
    "https://daum.net",
    "tiktok.com",
    "airbnb.com",
)
for website in websites:
    if not website.startswith("https://"):
        print(f"https://{website}")

# results

from requests import get

websites = (
    "https://naver.com",
    "https://google.com",
    "tiktok.com",
    "airbnb.com",
)
results = {}
for website in websites:
    if not website.startswith("https://"):
        website = f"https://{website}"
    response = get(website)
    if response.status_code == 200:
        results[website] = "ok!"
    else:
        results[website] = "Failed"
print(results)
