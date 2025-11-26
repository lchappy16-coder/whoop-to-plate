# src/config.py

# --- RECIPE VAULT (USDA Verified Profiles) ---
# Strictly Whole Foods. No Industrial Seed Oils. No Processed Sugars.
# Base Macros are calculated for the 'Standard Serving' described.

RECIPE_VAULT = {
    # ------------------------------------------------------------------
    # BREAKFAST (Retained for System Stability)
    # ------------------------------------------------------------------
    "breakfast_high_fat": [
        {"title": "Steak & Avocado Omelet", "desc": "3 Pasture Eggs, 4oz Sirloin, 1/2 Avocado, Ghee", "base_cals": 645, "p": 48, "f": 48, "c": 5, "query": "steak avocado omelet keto recipe"},
        {"title": "Smoked Salmon Benedict", "desc": "3 Poached Eggs, 3oz Smoked Salmon, Hollandaise", "base_cals": 520, "p": 38, "f": 40, "c": 4, "query": "smoked salmon benedict keto no bread"},
        {"title": "Bison Hash", "desc": "6oz Bison, 1/2 cup Sweet Potato, Tallow", "base_cals": 580, "p": 45, "f": 30, "c": 32, "query": "bison sweet potato hash paleo"},
        {"title": "Chorizo Frittata", "desc": "3 Eggs, 3oz Pork Chorizo, Spinach", "base_cals": 510, "p": 35, "f": 38, "c": 6, "query": "chorizo frittata paleo whole30"},
        {"title": "Bulletproof Coffee & Eggs", "desc": "Coffee w/ Butter/MCT + 3 Hard Boiled Eggs", "base_cals": 450, "p": 19, "f": 40, "c": 2, "query": "bulletproof coffee recipe butter"}
    ],
    "breakfast_high_carb": [
        {"title": "Anabolic Pro-Oats", "desc": "1 cup Oats, 1 cup Egg Whites, Berries", "base_cals": 550, "p": 35, "f": 6, "c": 90, "query": "egg white oatmeal protein recipe"},
        {"title": "Sourdough French Toast", "desc": "2 slices Sourdough, 2 Eggs, Maple Syrup", "base_cals": 480, "p": 18, "f": 12, "c": 75, "query": "sourdough french toast refined sugar free"},
        {"title": "Banana Protein Pancakes", "desc": "2 Bananas, 4 Eggs, Cinnamon", "base_cals": 490, "p": 26, "f": 20, "c": 54, "query": "banana egg pancakes paleo"},
        {"title": "Cream of Rice & Whey", "desc": "1 cup Cream of Rice, 1 scoop Isolate (Clean)", "base_cals": 500, "p": 30, "f": 2, "c": 90, "query": "cream of rice protein bowl"},
        {"title": "Fruit & Honey Bowl", "desc": "Large bowl Papaya/Melon, Raw Honey, Greek Yogurt", "base_cals": 400, "p": 15, "f": 0, "c": 85, "query": "fruit salad raw honey lime"}
    ],

    # ------------------------------------------------------------------
    # LUNCH: LIGHT & DIGESTIBLE (20 Options)
    # Focus: High Protein, Moderate Fat/Carb, Low fiber density for mid-day energy
    # ------------------------------------------------------------------
    "lunch_light": [
        {"title": "Bison Burger Salad", "desc": "8oz Bison Patty, Arugula, Pickles, Olive Oil", "base_cals": 550, "p": 48, "f": 38, "c": 4, "query": "bison burger salad bowl paleo"},
        {"title": "Cod & Asparagus", "desc": "8oz Cod, 1 tbsp Butter, Lemon, Asparagus", "base_cals": 320, "p": 40, "f": 12, "c": 6, "query": "baked cod asparagus lemon butter"},
        {"title": "Shrimp Ceviche", "desc": "8oz Shrimp, Lime, Cilantro, Avocado", "base_cals": 380, "p": 46, "f": 15, "c": 12, "query": "shrimp ceviche recipe avocado"},
        {"title": "Chicken & Kimchi", "desc": "6oz Chicken Thighs, 1/2 cup Kimchi", "base_cals": 420, "p": 35, "f": 28, "c": 8, "query": "chicken thigh kimchi bowl"},
        {"title": "Beef Tartare", "desc": "6oz Raw Filet Mignon, Egg Yolk, Capers", "base_cals": 450, "p": 38, "f": 32, "c": 2, "query": "steak tartare recipe classic"},
        {"title": "Sardine Salad", "desc": "2 cans Sardines (water), Olive Oil, Lemon, Parsley", "base_cals": 420, "p": 44, "f": 26, "c": 0, "query": "sardine salad lemon olive oil"},
        {"title": "Seared Scallops", "desc": "8oz Scallops, Ghee, Cauliflower Rice", "base_cals": 350, "p": 35, "f": 20, "c": 8, "query": "seared scallops ghee cauliflower rice"},
        {"title": "Turkey & Avocado Roll-ups", "desc": "8oz Roasted Turkey Breast wrapped in Lettuce w/ Avocado", "base_cals": 400, "p": 50, "f": 20, "c": 6, "query": "turkey avocado lettuce wraps"},
        {"title": "Leftover Steak Salad", "desc": "6oz Cold Steak, Spinach, Balsamic, Walnuts", "base_cals": 500, "p": 42, "f": 34, "c": 6, "query": "steak salad balsamic vinaigrette"},
        {"title": "Tuna & Boiled Egg Bowl", "desc": "1 can Tuna (safe catch), 2 Eggs, Olive Oil", "base_cals": 480, "p": 52, "f": 28, "c": 2, "query": "tuna boiled egg salad olive oil"},
        {"title": "Venison Carpaccio", "desc": "6oz Raw Venison, Olive Oil, Parmesan (Raw)", "base_cals": 380, "p": 38, "f": 24, "c": 0, "query": "venison carpaccio recipe"},
        {"title": "Grilled Octopus", "desc": "6oz Octopus, Olive Oil, Oregano, Lemon", "base_cals": 350, "p": 50, "f": 14, "c": 4, "query": "grilled octopus greek recipe"},
        {"title": "Chicken Liver Pâté", "desc": "4oz Liver Pâté (Homemade/Butter), Cucumber Slices", "base_cals": 400, "p": 20, "f": 34, "c": 4, "query": "chicken liver pate recipe butter"},
        {"title": "Mackerel Fillet", "desc": "6oz Mackerel, Salt, Lemon wedge", "base_cals": 450, "p": 32, "f": 35, "c": 0, "query": "pan seared mackerel recipe"},
        {"title": "Ground Beef & Zucchini", "desc": "8oz Lean Beef, Sautéed Zucchini, Salt", "base_cals": 550, "p": 48, "f": 38, "c": 8, "query": "ground beef zucchini skillet"},
        {"title": "Salmon Sashimi Bowl", "desc": "6oz Raw Salmon, Seaweed, Cucumber (No Rice)", "base_cals": 350, "p": 34, "f": 22, "c": 4, "query": "salmon sashimi bowl recipe"},
        {"title": "Lamb Kofta Salad", "desc": "6oz Ground Lamb Skewers, Cucumber Mint Salad", "base_cals": 520, "p": 30, "f": 42, "c": 6, "query": "lamb kofta salad paleo"},
        {"title": "Prawn & Mango Salad", "desc": "8oz Prawns, 1/2 Mango, Chili, Lime", "base_cals": 350, "p": 46, "f": 4, "c": 30, "query": "prawn mango salad thai"},
        {"title": "Roast Beef Roll-ups", "desc": "6oz Roast Beef slices, Goat Cheese/Butter inside", "base_cals": 450, "p": 45, "f": 28, "c": 2, "query": "roast beef roll ups low carb"},
        {"title": "Egg Salad (Avocado Mayo)", "desc": "4 Eggs, Avocado Oil Mayo, Chives", "base_cals": 480, "p": 24, "f": 40, "c": 3, "query": "egg salad avocado oil mayo"}
    ],

    # ------------------------------------------------------------------
    # DINNER: RECOVERY & DEEP SLEEP (20 Options)
    # Focus: Collagen, Glycine, Tryptophan, Slower Digestion
    # ------------------------------------------------------------------
    "dinner_recovery": [
        {"title": "Slow Roast Lamb Shank", "desc": "10oz Shank, 1 cup Mashed Potato, Bone Broth", "base_cals": 750, "p": 55, "f": 40, "c": 45, "query": "slow cooked lamb shank mashed potato"},
        {"title": "Crispy Skin Salmon & Rice", "desc": "8oz Salmon, 1 cup Rice, Coconut Aminos", "base_cals": 680, "p": 50, "f": 28, "c": 50, "query": "crispy skin salmon white rice"},
        {"title": "Ribeye & Honey Carrots", "desc": "10oz Ribeye, Roasted Carrots, Honey", "base_cals": 920, "p": 60, "f": 65, "c": 25, "query": "pan seared ribeye glazed carrots"},
        {"title": "Oxtail Stew", "desc": "8oz Oxtail (slow cooked), Root Veggies, Broth", "base_cals": 800, "p": 45, "f": 60, "c": 20, "query": "oxtail stew slow cooker paleo"},
        {"title": "Duck Breast & Sweet Potato", "desc": "8oz Duck Breast, 1 cup Sweet Potato Mash", "base_cals": 700, "p": 35, "f": 50, "c": 30, "query": "pan seared duck breast sweet potato"},
        {"title": "Bison Meatloaf", "desc": "8oz Bison, Tomato Glaze (Sugar Free), Green Beans", "base_cals": 600, "p": 50, "f": 35, "c": 20, "query": "bison meatloaf paleo recipe"},
        {"title": "Thai Green Curry (Chicken)", "desc": "8oz Chicken, Coconut Milk, Bamboo Shoots, Rice", "base_cals": 750, "p": 45, "f": 45, "c": 40, "query": "paleo thai green curry chicken"},
        {"title": "Venison Stew", "desc": "8oz Venison, Potato, Carrots, Beef Stock", "base_cals": 550, "p": 50, "f": 15, "c": 45, "query": "venison stew slow cooker"},
        {"title": "Pork Chop & Apples", "desc": "8oz Pasture Pork Chop, Stewed Apples, Cinnamon", "base_cals": 600, "p": 48, "f": 30, "c": 35, "query": "pork chops and apples paleo"},
        {"title": "Shepherd's Pie", "desc": "Ground Lamb, Sweet Potato Mash Topping (No flour)", "base_cals": 650, "p": 35, "f": 35, "c": 45, "query": "paleo shepherds pie sweet potato"},
        {"title": "Beef Heart Bolognese", "desc": "6oz Ground Beef Heart/Beef blend, White Rice Pasta", "base_cals": 600, "p": 45, "f": 30, "c": 40, "query": "beef heart bolognese recipe"},
        {"title": "Halibut & Risotto", "desc": "8oz Halibut, Arborio Rice (cooked in broth), Ghee", "base_cals": 550, "p": 48, "f": 12, "c": 50, "query": "halibut risotto recipe"},
        {"title": "Stuffed Peppers", "desc": "Ground Beef & Rice stuffed Bell Peppers", "base_cals": 500, "p": 35, "f": 25, "c": 35, "query": "paleo stuffed peppers beef rice"},
        {"title": "Trout Almondine", "desc": "8oz Trout, Butter, Sliced Almonds, Green Beans", "base_cals": 580, "p": 46, "f": 40, "c": 10, "query": "trout almondine recipe"},
        {"title": "Surf & Turf", "desc": "6oz Filet Mignon, 4oz Shrimp, Asparagus", "base_cals": 650, "p": 60, "f": 40, "c": 5, "query": "surf and turf recipe butter garlic"},
        {"title": "Roast Chicken Dinner", "desc": "1/2 Roast Chicken, Roasted Potatoes, Carrots", "base_cals": 800, "p": 60, "f": 45, "c": 40, "query": "roast chicken potatoes carrots one pan"},
        {"title": "Beef Short Ribs", "desc": "8oz Braised Short Ribs, Cauliflower Mash", "base_cals": 850, "p": 45, "f": 70, "c": 12, "query": "braised short ribs paleo"},
        {"title": "Mussels & Fries (Tallow)", "desc": "1lb Mussels, White Wine, Oven Fries (Tallow)", "base_cals": 600, "p": 40, "f": 25, "c": 50, "query": "mussels white wine sauce recipe"},
        {"title": "Lamb Curry (Rogan Josh)", "desc": "8oz Lamb Shoulder, Ghee, Spices, Basmati Rice", "base_cals": 750, "p": 45, "f": 45, "c": 45, "query": "lamb rogan josh paleo recipe"},
        {"title": "Pot Roast", "desc": "8oz Chuck Roast, Carrots, Onions, Potatoes", "base_cals": 700, "p": 50, "f": 40, "c": 35, "query": "pot roast slow cooker recipe"}
    ],

    # ------------------------------------------------------------------
    # SNACKS: FUNCTIONAL FUEL (20 Options)
    # Focus: Single Ingredient or simple combinations
    # ------------------------------------------------------------------
    "snacks": [
        {"title": "Hard Boiled Eggs", "desc": "2 Eggs, Sea Salt", "base_cals": 140, "p": 12, "f": 10, "c": 1, "query": "none"},
        {"title": "Bone Broth Cup", "desc": "16oz Beef Bone Broth, Salt", "base_cals": 80, "p": 18, "f": 0, "c": 2, "query": "bone broth recipe"},
        {"title": "Canned Oysters", "desc": "1 tin Smoked Oysters (Olive Oil)", "base_cals": 200, "p": 16, "f": 12, "c": 8, "query": "smoked oysters snack"},
        {"title": "Macadamia Nuts", "desc": "1oz Raw Macadamias", "base_cals": 200, "p": 2, "f": 21, "c": 4, "query": "none"},
        {"title": "Medjool Dates & Butter", "desc": "2 Dates, 1 tsp Raw Butter inside", "base_cals": 180, "p": 1, "f": 4, "c": 36, "query": "dates stuffed with butter"},
        {"title": "Beef Jerky (Clean)", "desc": "2oz 100% Grass Fed Jerky (No Sugar)", "base_cals": 160, "p": 30, "f": 4, "c": 2, "query": "sugar free beef jerky recipe"},
        {"title": "Greek Yogurt & Honey", "desc": "1 cup Plain Yogurt, 1 tbsp Honey", "base_cals": 200, "p": 20, "f": 0, "c": 28, "query": "greek yogurt honey"},
        {"title": "Sardines", "desc": "1 tin Sardines in Water", "base_cals": 150, "p": 20, "f": 8, "c": 0, "query": "sardines snack ideas"},
        {"title": "Apple & Raw Cheese", "desc": "1 Apple, 1oz Raw Cheddar", "base_cals": 200, "p": 7, "f": 9, "c": 25, "query": "none"},
        {"title": "Avocado & Salt", "desc": "1/2 Avocado, Maldon Salt", "base_cals": 160, "p": 2, "f": 15, "c": 8, "query": "none"},
        {"title": "Frozen Grapes", "desc": "1 cup Grapes (frozen)", "base_cals": 100, "p": 1, "f": 0, "c": 27, "query": "none"},
        {"title": "Pemmican", "desc": "1 bar Beef/Tallow Pemmican", "base_cals": 400, "p": 15, "f": 35, "c": 0, "query": "pemmican recipe"},
        {"title": "Cottage Cheese", "desc": "1 cup Cottage Cheese (Full Fat)", "base_cals": 220, "p": 25, "f": 10, "c": 8, "query": "none"},
        {"title": "Raw Carrots & Guac", "desc": "2 Carrots, 1/2 cup Guacamole", "base_cals": 200, "p": 3, "f": 18, "c": 12, "query": "none"},
        {"title": "Biltong", "desc": "2oz Biltong (Cured Beef)", "base_cals": 160, "p": 32, "f": 4, "c": 0, "query": "biltong recipe"},
        {"title": "Kefir", "desc": "1 cup Plain Goat Kefir", "base_cals": 140, "p": 9, "f": 8, "c": 10, "query": "none"},
        {"title": "Banana", "desc": "1 Ripe Banana", "base_cals": 105, "p": 1, "f": 0, "c": 27, "query": "none"},
        {"title": "Coconut Chunks", "desc": "2oz Raw Coconut Meat", "base_cals": 200, "p": 2, "f": 18, "c": 8, "query": "none"},
        {"title": "Dark Chocolate", "desc": "2 squares 100% Cacao", "base_cals": 120, "p": 2, "f": 12, "c": 4, "query": "none"},
        {"title": "Orange & Gelatin", "desc": "1 Orange, 1 scoop Beef Gelatin (in water)", "base_cals": 100, "p": 10, "f": 0, "c": 15, "query": "gelatin gummies recipe"}
    ]
}
