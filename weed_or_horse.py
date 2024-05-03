import random
from os import system

system("cls")

WEED_STRAINS = [
    "Wappa",
    "Watermelon Rush",
    "Unobtanium",
    "Up All Day Jay",
    "Up the Straits",
    "Tropicana Banana",
    "Tygra",
    "The Gift",
    "Thank You Jerry",
    "Tangilope",
    "Strawnana",
    "Space Oddity",
    "Saint Jack",
    "Serious Happiness",
    "Snow Temple",
    "Rootbeer Rolex",
    "Right Mark",
    "Queen Dream",
    "Peach Cresccendo",
    "Pennywise",
    "Pink Stake",
    "Original Jamaican Lyons",
    "Mendo Breath",
    "Juneau's Gift",
    "Italian Kiss",
    "Jilly Bean",
    "Grape Lui",
    "Glitter Bomb",
    "Fibranova",
    "Durban Poison",
    "Cherry Blossom",
    "Cherry Gar-See-Ya",
    "Cheddar Head",
    "Camel Toes",
    "Carmagnola",
    "Bordello",
    "Black Beauty",
    "Agent Orange",
]

UNDEFEATED_HORSES = [
    "Ace Impact",
    "Agnes Tachyon",
    "Ajax",
    "Albany Girl",
    "Aldford",
    "Alipes",
    "American Eclipse",
    "Amianto",
    "Ardrossan",
    "Army Mule",
    "Asteroid",
    "Bahram",
    "Barcaldine",
    "Bay Middleton",
    "Black Caviar",
    "Blue Train",
    "Boniform",
    "Braque",
    "Bullets Fever",
    "Bustin Stones",
    "Candy Ride",
    "Caracalla",
    "Catchascatchcan",
    "Cavaliere d'Arpino",
    "Claude",
    "Cluster of Stars",
    "Cobweb",
    "Colin",
    "Combat",
    "Crucifix",
    "Danzig",
    "Dice",
    "Dismal",
    "Drone",
    "Eclipse",
    "El Rio Rey",
    "Emerson",
    "Fain",
    "Fasliyev",
    "Flightline",
    "Flying Childers",
    "Footstepsinthesand",
    "Frankel",
    "Fuji Kiseki",
    "Golden Fleece",
    "Goldfinder",
    "Grand Flaneur",
    "Handsomchamp",
    "Highflyer",
    "Hurry On",
    "Husson",
    "Itajara",
    "Justify",
    "Karayel",
    "Kincsem",
    "Kitano Daio",
    "Kneller",
    "Kurifuji",
    "La Cressonniere",
    "Lammtarra",
    "Landaluce",
    "Landgraf",
    "Macón",
    "Madelia",
    "Malt Queen",
    "Manantial",
    "Mannamead",
    "Maruzensky",
    "Mastery",
    "Meadowlake",
    "Melody",
    "Monarch",
    "Moscona",
    "Nadal",
    "Nearco",
    "Nereide",
    "Norfolk",
    "Ormonde",
    "Patience",
    "Payaso",
    "Peppers Pride",
    "Perdita II",
    "Perigord",
    "Personal Ensign",
    "Pharis",
    "Precocious",
    "Prestige",
    "Pronto",
    "Queen's Logic",
    "Quorto",
    "Raise a Native",
    "Rare Brick",
    "Regulus",
    "Reset",
    "Ribot",
    "Rodolph",
    "Salvator",
    "Saphir",
    "Sensations",
    "Snap",
    "Soberbo",
    "St. Simon",
    "Sweetbriar",
    "Teofilo",
    "The Tetrarch",
    "Tiffin",
    "Tokino Minoru",
    "Tolgus",
    "Tremont",
    "Tsurumaru Sunday",
    "Val de Grace",
    "Valyra",
    "Viani",
    "Vindication",
    "White Moonstone",
    "Windsor Slipper",
    "Zarkava",
]

# Initialize the user's score
score = 0

# Select 20 names from each list
selected_horse_names = random.sample(UNDEFEATED_HORSES, 20)
selected_weed_strain_names = random.sample(WEED_STRAINS, 20)

# Combine the selected names
combined_names = selected_horse_names + selected_weed_strain_names

while True:
    # Randomly select a name from the combined list
    random_name = random.choice(combined_names)

    # Remove the selected name from the combined list to avoid repeats
    combined_names.remove(random_name)

    # Ask the user to guess
    user_guess = input(
        f"Is '{random_name}' a horse name or a weed strain? (h/w): "
    ).lower()

    # Check if the guess is correct
    if (user_guess == "h" and random_name in selected_horse_names) or (
        user_guess == "w" and random_name in selected_weed_strain_names
    ):
        print("Correct! You earn a point.")
        score += 1
    else:
        print("Incorrect. Game over!")
        break

# Display the final score
print(f"Your total score: {score}")
