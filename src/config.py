# src/config.py

# --- RECIPE VAULT (Strictly Whole Foods / No Seed Oils) ---
# Data derived directly from 'Whoop-To-Plate Recipes.pdf'
# p = Protein (g), f = Fat (g), c = Carbs (g)

RECIPE_VAULT = {
    # ---------------------------------------------------------
    # BREAKFAST (High Fat / Low Insulin Focus)
    # ---------------------------------------------------------
    "breakfast_high_fat": [
        {
            "title": "Breakfast Migas (Tex-Mex Scramble)",
            "desc": "Eggs, Peppers, Onions, Olive Oil (No corn chips).",
            "base_cals": 389, "p": 23.8, "f": 25.3, "c": 16.2,
            "query": "paleo breakfast migas recipe no corn"
        },
        {
            "title": "Buffalo Chicken Egg Muffins",
            "desc": "Ground Chicken, Hot Sauce (Clean), Eggs, Ghee.",
            "base_cals": 268, "p": 22, "f": 20, "c": 4,
            "query": "buffalo chicken egg muffins paleo"
        },
        {
            "title": "Sausage Hash Brown Egg Muffins",
            "desc": "Whole Potato, Sausage, Eggs (Baked).",
            "base_cals": 255, "p": 14, "f": 17, "c": 10,
            "query": "sausage hash brown egg muffins paleo"
        },
        {
            "title": "Sweet Potato Breakfast Casserole",
            "desc": "Ground Pork, Sweet Potato, Spinach, Peppers.",
            "base_cals": 209, "p": 24, "f": 14, "c": 9,
            "query": "sweet potato breakfast casserole paleo pork"
        },
        {
            "title": "Cottage Cheese Egg Bites",
            "desc": "Eggs, Cottage Cheese (Full Fat), Bacon.",
            "base_cals": 146, "p": 12, "f": 9, "c": 3,
            "query": "cottage cheese egg bites starbucks copycat"
        },
        {
            "title": "Mixed Berry Protein Chia Pudding",
            "desc": "Chia Seeds, Collagen Peptides, Berries, Almond Milk.",
            "base_cals": 270, "p": 10, "f": 19, "c": 10,
            "query": "mixed berry protein chia pudding recipe"
        },
        {
            "title": "Spinach Artichoke Breakfast Casserole",
            "desc": "Eggs, Spinach, Artichoke Hearts, Ghee/Oil.",
            "base_cals": 235, "p": 11, "f": 18, "c": 4,
            "query": "spinach artichoke breakfast casserole paleo"
        },
        {
            "title": "Ham and Veggie Breakfast Casserole",
            "desc": "Diced Ham, Mixed Vegetables, Eggs.",
            "base_cals": 172, "p": 11, "f": 11, "c": 6,
            "query": "ham and veggie breakfast casserole whole30"
        },
        {
            "title": "Paleo Sausage Egg McMuffin",
            "desc": "Sausage Patty 'Buns', Egg, Avocado/Ghee.",
            "base_cals": 699, "p": 28, "f": 63, "c": 4,
            "query": "paleo sausage egg mcmuffin recipe"
        },
        {
            "title": "Sheet Pan Eggs",
            "desc": "Eggs baked on sheet pan with Peppers/Spinach.",
            "base_cals": 143, "p": 12, "f": 10, "c": 1,
            "query": "sheet pan eggs meal prep"
        },
        {
            "title": "Sweet Potato Toast with Avocado",
            "desc": "Sliced Sweet Potato (Toasted), Avocado Smash.",
            "base_cals": 268, "p": 8, "f": 14, "c": 10,
            "query": "sweet potato toast avocado recipe"
        }
    ],

    # ---------------------------------------------------------
    # BREAKFAST (High Carb / Glycolytic Fuel)
    # ---------------------------------------------------------
    "breakfast_high_carb": [
        {
            "title": "Sweet Potato Sausage Hash",
            "desc": "Pork Sausage, Sweet Potato, Apple, Onion.",
            "base_cals": 393, "p": 19, "f": 20, "c": 35,
            "query": "sweet potato sausage apple hash paleo"
        },
        {
            "title": "Pumpkin Protein Pancakes",
            "desc": "Pumpkin Puree, Whey/Collagen, Cinnamon (No Flour).",
            "base_cals": 512, "p": 34.4, "f": 15.5, "c": 60,
            "query": "pumpkin protein pancakes paleo recipe"
        },
        {
            "title": "Cottage Cheese Toast",
            "desc": "Sourdough/GF Toast, Cottage Cheese, Fruit/Savory topping.",
            "base_cals": 325, "p": 18.4, "f": 11.1, "c": 39.5,
            "query": "cottage cheese toast recipe ideas"
        },
        {
            "title": "Apple Cinnamon Baked Oatmeal",
            "desc": "Oats (Soaked), Apples, Cinnamon, Egg.",
            "base_cals": 216, "p": 7, "f": 7.5, "c": 31.4,
            "query": "apple cinnamon baked oatmeal healthy"
        },
        {
            "title": "Paleo Breakfast Fried Rice",
            "desc": "Cauliflower Rice, Bacon/Egg, Peas, Carrots.",
            "base_cals": 154, "p": 7.2, "f": 7.5, "c": 14.3,
            "query": "paleo breakfast fried rice cauliflower"
        },
        {
            "title": "Raspberry Chia Pudding Parfait",
            "desc": "Chia Pudding, Layered Whole Raspberries.",
            "base_cals": 288, "p": 6, "f": 18, "c": 24,
            "query": "raspberry chia pudding parfait recipe"
        },
        {
            "title": "Sweet Potato Waffle Sandwich",
            "desc": "Sweet Potato Waffles (Iron pressed), Egg/Bacon inside.",
            "base_cals": 329, "p": 11.9, "f": 5.6, "c": 59.1,
            "query": "sweet potato waffle breakfast sandwich paleo"
        },
        {
            "title": "Paleo Banana Bread",
            "desc": "Almond Flour, Bananas, Eggs (No Sugar).",
            "base_cals": 248, "p": 6, "f": 16, "c": 20,
            "query": "paleo banana bread recipe almond flour"
        },
        {
            "title": "Mexican Breakfast Casserole",
            "desc": "Sweet Potato Rounds, Spiced Meat, Eggs.",
            "base_cals": 397, "p": 20, "f": 24, "c": 25,
            "query": "mexican breakfast casserole paleo sweet potato"
        }
    ],

    # ---------------------------------------------------------
    # LUNCH (Light / Cognitive Focus)
    # ---------------------------------------------------------
    "lunch_light": [
        {
            "title": "Healthy Tuna Salad (No Mayo)",
            "desc": "Tuna, Olive/Avocado Oil, Celery, Apple (Optional).",
            "base_cals": 395, "p": 19, "f": 23, "c": 32,
            "query": "healthy tuna salad olive oil no mayo"
        },
        {
            "title": "Garlic Herb Chicken & Asparagus",
            "desc": "Chicken Breast, Asparagus, Ghee, Herbs.",
            "base_cals": 320, "p": 29, "f": 16, "c": 19,
            "query": "garlic herb chicken asparagus meal prep"
        },
        {
            "title": "Thai Chicken Meal Prep",
            "desc": "Chicken, Coconut Aminos, Almond/Sunflower Butter.",
            "base_cals": 254, "p": 34, "f": 7, "c": 12,
            "query": "thai chicken meal prep almond butter"
        },
        {
            "title": "Easy Sriracha Tuna Salad",
            "desc": "Tuna, Clean Sriracha, Avocado Oil Mayo/Oil.",
            "base_cals": 220, "p": 16, "f": 15, "c": 6,
            "query": "sriracha tuna salad paleo recipe"
        },
        {
            "title": "Turkey Taco Salad",
            "desc": "Ground Turkey, Greens, Salsa, Avocado.",
            "base_cals": 557, "p": 24, "f": 40, "c": 31,
            "query": "turkey taco salad meal prep paleo"
        },
        {
            "title": "Healthy Zuppa Toscana",
            "desc": "Sausage, Kale, Cauliflower, Coconut Milk.",
            "base_cals": 583, "p": 20, "f": 45, "c": 28,
            "query": "paleo zuppa toscana soup recipe"
        },
        {
            "title": "Paleo Sweet Potato Turkey Chili",
            "desc": "Ground Turkey, Sweet Potato, Spices (No Beans).",
            "base_cals": 312, "p": 24, "f": 2, "c": 52,
            "query": "paleo sweet potato turkey chili no beans"
        },
        {
            "title": "Chicken Zucchini Noodle Soup",
            "desc": "Chicken Broth, Zucchini Spirals, Chicken Meat.",
            "base_cals": 302, "p": 29, "f": 11, "c": 23,
            "query": "chicken zucchini noodle soup recipe"
        },
        {
            "title": "Asian Chicken Zucchini Soup Jar",
            "desc": "Concentrated Broth, Raw Zucchini, Pre-cooked Chicken.",
            "base_cals": 228, "p": 21.8, "f": 8.9, "c": 17.5,
            "query": "mason jar instant noodle soup chicken zucchini"
        },
        {
            "title": "Turmeric Chicken Cauliflower Soup",
            "desc": "Chicken, Turmeric Broth, Cauliflower Rice.",
            "base_cals": 254, "p": 22.5, "f": 6.7, "c": 27,
            "query": "turmeric chicken cauliflower rice soup anti inflammatory"
        },
        {
            "title": "Creamy Dairy-Free Clam Chowder",
            "desc": "Clams, Coconut Milk, Cauliflower/Potatoes.",
            "base_cals": 560, "p": 14, "f": 30, "c": 63,
            "query": "dairy free clam chowder paleo recipe"
        },
        {
            "title": "Classic Chicken Salad",
            "desc": "Chicken, Avocado Mayo, Celery, Grapes.",
            "base_cals": 375, "p": 26, "f": 26, "c": 9,
            "query": "paleo chicken salad avocado mayo grapes"
        },
        {
            "title": "Best Broccoli Salad",
            "desc": "Raw Broccoli, Bacon, Sunflower Seeds, Creamy Dressing.",
            "base_cals": 437, "p": 13, "f": 34, "c": 25,
            "query": "paleo broccoli salad bacon sunflower seeds"
        },
        {
            "title": "Chicken Shawarma Salad",
            "desc": "Spiced Chicken, Greens, Tahini Dressing.",
            "base_cals": 545, "p": 29.1, "f": 41.1, "c": 21.7,
            "query": "chicken shawarma salad paleo tahini"
        },
        {
            "title": "Curried Mango Chicken Salad",
            "desc": "Chicken, Curry Powder, Mango Chunks, Mayo/Yogurt.",
            "base_cals": 550, "p": 30, "f": 39, "c": 18,
            "query": "curried mango chicken salad paleo"
        },
        {
            "title": "Mandarin Chicken Salad",
            "desc": "Chicken, Mandarin Oranges, Sesame Dressing.",
            "base_cals": 505, "p": 24, "f": 34, "c": 33,
            "query": "mandarin chicken salad paleo sesame ginger"
        },
        {
            "title": "Strawberry Cobb Salad",
            "desc": "Chicken, Bacon, Avocado, Strawberries, Greens.",
            "base_cals": 683, "p": 35.5, "f": 50.7, "c": 26.2,
            "query": "strawberry cobb salad paleo recipe"
        },
        {
            "title": "Instant Pot Egg Roll Bowl",
            "desc": "Ground Pork, Cabbage, Ginger, Garlic (No Wrapper).",
            "base_cals": 511, "p": 26, "f": 33, "c": 29,
            "query": "instant pot egg roll in a bowl paleo"
        },
        {
            "title": "Red Curry Shrimp & Cauliflower",
            "desc": "Shrimp, Red Curry Paste, Coconut Milk, Cauliflower.",
            "base_cals": 369, "p": 30, "f": 14.3, "c": 32.4,
            "query": "red curry shrimp cauliflower rice recipe"
        },
        {
            "title": "Thai Turkey Lettuce Wraps",
            "desc": "Ground Turkey, Thai Spices, Lettuce Leaves.",
            "base_cals": 374, "p": 27.4, "f": 16.6, "c": 33.4,
            "query": "thai turkey lettuce wraps paleo"
        }
    ],

    # ---------------------------------------------------------
    # DINNER (Recovery / Sleep Support)
    # ---------------------------------------------------------
    "dinner_recovery": [
        {
            "title": "Creamy Tuscan Chicken",
            "desc": "Chicken Thighs, Coconut Milk, Spinach, Sun-dried Tomato.",
            "base_cals": 368, "p": 23, "f": 25, "c": 12,
            "query": "creamy tuscan chicken paleo dairy free"
        },
        {
            "title": "Paleo Pizza Soup",
            "desc": "Sausage, Peppers, Tomato Base, Broth.",
            "base_cals": 366, "p": 17, "f": 29, "c": 11,
            "query": "paleo pizza soup recipe"
        },
        {
            "title": "One Skillet Spinach Artichoke Salmon",
            "desc": "Salmon, Spinach, Artichokes, Creamy Sauce.",
            "base_cals": 407, "p": 37, "f": 26, "c": 6,
            "query": "creamy spinach artichoke salmon paleo"
        },
        {
            "title": "Shrimp Fried Cauliflower Rice",
            "desc": "Shrimp, Cauliflower Rice, Peas, Carrots, Egg.",
            "base_cals": 295, "p": 28, "f": 15, "c": 9,
            "query": "shrimp fried cauliflower rice recipe"
        },
        {
            "title": "Lemon Chicken Piccata",
            "desc": "Chicken Cutlets, Almond Flour, Ghee, Capers, Lemon.",
            "base_cals": 308, "p": 28, "f": 19, "c": 7,
            "query": "lemon chicken piccata paleo almond flour"
        },
        {
            "title": "Sheet Pan Mini Meatloaf",
            "desc": "Ground Beef Loaves, Roasted Veggies.",
            "base_cals": 380, "p": 29, "f": 17, "c": 32,
            "query": "sheet pan mini meatloaf paleo"
        },
        {
            "title": "Slow Cooker Chicken Chile Verde",
            "desc": "Chicken Thighs, Tomatillos, Green Chiles.",
            "base_cals": 250, "p": 26, "f": 4, "c": 26,
            "query": "slow cooker chicken chile verde paleo"
        },
        {
            "title": "Greek Orzo Skillet (Cassava)",
            "desc": "Cassava Orzo, Olives, Tomato, Spinach.",
            "base_cals": 475, "p": 27, "f": 25, "c": 30,
            "query": "greek skillet paleo cassava orzo"
        },
        {
            "title": "Beef and Broccoli Noodles",
            "desc": "Beef Strips, Broccoli, Sweet Potato Glass Noodles.",
            "base_cals": 575, "p": 33, "f": 17.6, "c": 68.3,
            "query": "paleo beef and broccoli sweet potato noodles"
        },
        {
            "title": "Taco Bowls (Ground Beef)",
            "desc": "Seasoned Beef, Cauliflower Rice, Guac, Salsa.",
            "base_cals": 602, "p": 37, "f": 21.6, "c": 65,
            "query": "paleo taco bowls cauliflower rice"
        },
        {
            "title": "Peanut (Almond) Butter Chicken",
            "desc": "Chicken, Almond Butter Sauce, Veggies.",
            "base_cals": 379, "p": 33.3, "f": 16.5, "c": 25.6,
            "query": "almond butter chicken paleo recipe"
        },
        {
            "title": "Chicken and Rice Bowls (Coconut)",
            "desc": "Chicken, Coconut Milk Rice (or Cauli), Veggies.",
            "base_cals": 631, "p": 39.1, "f": 29.2, "c": 53.2,
            "query": "coconut rice chicken bowl paleo"
        },
        {
            "title": "Greek Sheet Pan Chicken",
            "desc": "Chicken, Peppers, Onions, Olives, Oregano.",
            "base_cals": 541, "p": 40.9, "f": 23.6, "c": 41.7,
            "query": "greek sheet pan chicken paleo"
        },
        {
            "title": "Southwest Chicken Salad",
            "desc": "Chicken, Sweet Potato/Beans, Avocado, Greens.",
            "base_cals": 503, "p": 42.8, "f": 20.4, "c": 40.8,
            "query": "southwest chicken salad paleo dressing"
        },
        {
            "title": "Instant Pot White Bean Stew",
            "desc": "White Beans (Cannellini), Veggies, Broth.",
            "base_cals": 399, "p": 25, "f": 1, "c": 77,
            "query": "white bean stew instant pot recipe"
        },
        {
            "title": "Coconut Curry Lentil Soup",
            "desc": "Lentils, Coconut Milk, Curry Powder.",
            "base_cals": 275, "p": 11, "f": 11.5, "c": 34.4,
            "query": "coconut curry lentil soup recipe"
        },
        {
            "title": "Almond Butter Tofu (or Chicken) Bowls",
            "desc": "Protein Source, Almond Sauce, Rice/Cauli.",
            "base_cals": 450, "p": 20, "f": 25, "c": 30,
            "query": "almond butter tofu bowl recipe"
        },
        {
            "title": "Creamy Vegan Pasta",
            "desc": "GF Pasta, Cashew Cream Sauce, Veggies.",
            "base_cals": 491, "p": 17, "f": 19.6, "c": 63.9,
            "query": "creamy vegan pasta cashew sauce recipe"
        },
        {
            "title": "Paleo Egg Roll in a Bowl (Dinner)",
            "desc": "Large Portion: Pork, Cabbage, Sesame Oil.",
            "base_cals": 368, "p": 23, "f": 27, "c": 7,
            "query": "egg roll in a bowl recipe dinner"
        },
        {
            "title": "Tex Mex Sweet Potato Hash (Dinner)",
            "desc": "Beef, Sweet Potato, Spices, Avocado side.",
            "base_cals": 490, "p": 39, "f": 18, "c": 42,
            "query": "tex mex sweet potato hash beef"
        }
    ],

    # ---------------------------------------------------------
    # SNACKS (Metabolic Bridges)
    # ---------------------------------------------------------
    "snacks": [
        {
            "title": "Hard Boiled Egg",
            "desc": "1 Large Egg, Sea Salt.",
            "base_cals": 78, "p": 6.3, "f": 5.3, "c": 0.6,
            "query": "hard boiled egg nutrition"
        },
        {
            "title": "Almonds (1 oz)",
            "desc": "Raw or Dry Roasted Almonds (~23 nuts).",
            "base_cals": 164, "p": 6, "f": 14.2, "c": 6.1,
            "query": "almonds nutrition 1 oz"
        },
        {
            "title": "Walnuts (1 oz)",
            "desc": "Raw Walnuts Halves.",
            "base_cals": 185, "p": 4.3, "f": 18.5, "c": 3.9,
            "query": "walnuts nutrition 1 oz"
        },
        {
            "title": "Macadamia Nuts (1 oz)",
            "desc": "Raw Macadamia Nuts.",
            "base_cals": 204, "p": 2.2, "f": 21.6, "c": 3.8,
            "query": "macadamia nuts nutrition 1 oz"
        },
        {
            "title": "Pumpkin Seeds (1 oz)",
            "desc": "Raw Pepitas.",
            "base_cals": 126, "p": 5.3, "f": 5.5, "c": 15.2,
            "query": "pumpkin seeds nutrition 1 oz"
        },
        {
            "title": "Cashews (1 oz)",
            "desc": "Raw Cashews.",
            "base_cals": 157, "p": 5.2, "f": 12, "c": 8.6,
            "query": "cashews nutrition 1 oz"
        },
        {
            "title": "Pistachios (1 oz)",
            "desc": "Shelled Pistachios.",
            "base_cals": 165, "p": 5.8, "f": 13.4, "c": 7.8,
            "query": "pistachios nutrition 1 oz"
        },
        {
            "title": "Pecans (1 oz)",
            "desc": "Raw Pecan Halves.",
            "base_cals": 196, "p": 2.6, "f": 20, "c": 4,
            "query": "pecans nutrition 1 oz"
        },
        {
            "title": "Apple (Medium)",
            "desc": "Whole Apple.",
            "base_cals": 95, "p": 0.5, "f": 0.3, "c": 25,
            "query": "medium apple nutrition"
        },
        {
            "title": "Banana (Medium)",
            "desc": "Whole Banana.",
            "base_cals": 105, "p": 1.3, "f": 0.4, "c": 27,
            "query": "medium banana nutrition"
        },
        {
            "title": "Orange (Medium)",
            "desc": "Whole Orange.",
            "base_cals": 62, "p": 1, "f": 0, "c": 15,
            "query": "medium orange nutrition"
        },
        {
            "title": "Pear (Medium)",
            "desc": "Whole Pear.",
            "base_cals": 101, "p": 0.6, "f": 0.3, "c": 27,
            "query": "medium pear nutrition"
        },
        {
            "title": "Strawberries (1 cup)",
            "desc": "Whole Strawberries.",
            "base_cals": 53, "p": 1, "f": 0.5, "c": 13,
            "query": "strawberries nutrition 1 cup"
        },
        {
            "title": "Raspberries (1 cup)",
            "desc": "Whole Raspberries.",
            "base_cals": 64, "p": 1.5, "f": 0.8, "c": 15,
            "query": "raspberries nutrition 1 cup"
        },
        {
            "title": "Avocado (1/2 Fruit)",
            "desc": "Half Avocado with Salt.",
            "base_cals": 160, "p": 2, "f": 14.7, "c": 8.5,
            "query": "avocado nutrition half"
        },
        {
            "title": "Beef Jerky (1 oz)",
            "desc": "Sugar-Free Grass Fed Jerky.",
            "base_cals": 80, "p": 12, "f": 1.5, "c": 1,
            "query": "beef jerky nutrition sugar free"
        },
        {
            "title": "Sardines (1 Can)",
            "desc": "Sardines in Water/Olive Oil.",
            "base_cals": 191, "p": 23, "f": 11, "c": 0,
            "query": "sardines nutrition can"
        },
        {
            "title": "Dark Chocolate (1 oz)",
            "desc": "85% Cacao.",
            "base_cals": 170, "p": 2, "f": 14, "c": 11,
            "query": "dark chocolate 85 nutrition"
        },
        {
            "title": "Carrot Sticks (1 cup)",
            "desc": "Raw Carrots.",
            "base_cals": 50, "p": 1, "f": 0.3, "c": 12,
            "query": "carrot sticks nutrition"
        },
        {
            "title": "Protein Brownie Balls",
            "desc": "Dates, Nuts, Cocoa Powder (No Sugar).",
            "base_cals": 100, "p": 6, "f": 6, "c": 12,
            "query": "protein brownie balls dates recipe"
        }
    ]
}
