# src/config.py

# --- STRICT WHOLE FOODS DATABASE ---
# No seed oils, no additives, no processed sugars.

# --- RECIPE VAULT ---
# This database acts as the source of truth for the Precision Planner.
# 'base_cals' are approximate; the Planner mathematically scales these based on your Whoop Strain.

RECIPE_VAULT = {
    # ---------------------------------------------------------
    # BREAKFAST: LOW INSULIN / HIGH FOCUS
    # Best for: Rest days, Low Strain days, or "Break-Fast" at 10-11am.
    # ---------------------------------------------------------
    "breakfast_high_fat": [
        {
            "title": "Steak & Avocado 'Power' Omelet",
            "desc": "High satiety start. High fats keep insulin baseline low for mental clarity.",
            "base_cals": 650,
            "query": "steak avocado omelet keto paleo recipe"
        },
        {
            "title": "Smoked Salmon & Poached Eggs Benedict",
            "desc": "Omega-3 rich start. Use a portobello mushroom or tomato slice instead of bread base.",
            "base_cals": 550,
            "query": "smoked salmon poached eggs portobello keto recipe"
        },
        {
            "title": "Bison & Sweet Potato Hash (Leftovers)",
            "desc": "Nutrient dense ruminant meat with moderate fibrous carbs.",
            "base_cals": 600,
            "query": "bison sweet potato hash paleo recipe cast iron"
        },
        {
            "title": "Pastured Egg & Chorizo Frittata",
            "desc": "Choline-rich eggs with spicy pork protein. Ensure chorizo is sugar-free.",
            "base_cals": 500,
            "query": "chorizo frittata paleo whole30 recipe"
        },
        {
            "title": "Coconut & Chia 'No-Oat'meal",
            "desc": "Healthy medium-chain triglycerides (MCTs) for immediate brain fuel.",
            "base_cals": 450,
            "query": "keto chia pudding coconut milk recipe hot"
        }
    ],

    # ---------------------------------------------------------
    # BREAKFAST: HIGH GLYCOLYTIC / TRAINING
    # Best for: Days with Morning Workouts or Strain > 14.
    # ---------------------------------------------------------
    "breakfast_high_carb": [
        {
            "title": "Anabolic Pro-Oats (Egg White Volume)",
            "desc": "Oats cooked with egg whites for massive volume and protein without the fat.",
            "base_cals": 600,
            "query": "egg white oatmeal protein recipe bodybuilder"
        },
        {
            "title": "Sourdough French Toast (Honey & Berry)",
            "desc": "Fermented wheat is easier to digest. Maple syrup refills muscle glycogen.",
            "base_cals": 700,
            "query": "sourdough french toast refined sugar free recipe"
        },
        {
            "title": "Banana & Egg 'Pancakes'",
            "desc": "Simple 2-ingredient batter. Fast digesting glucose for immediate energy.",
            "base_cals": 500,
            "query": "banana egg pancakes paleo 3 ingredients"
        },
        {
            "title": "Cream of Rice with Collagen",
            "desc": "The ultimate pre-heavy-lifting fuel. pure glucose, zero digestion distress.",
            "base_cals": 550,
            "query": "cream of rice protein bowl recipe pre workout"
        }
    ],

    # ---------------------------------------------------------
    # LUNCH: LIGHT & DIGESTIBLE
    # Best for: Mid-day fueling that prevents the "2pm Crash".
    # ---------------------------------------------------------
    "lunch_light": [
        {
            "title": "Bison Burger Salad Bowl",
            "desc": "Lean ruminant meat over arugula. Arugula stimulates bile for fat digestion.",
            "base_cals": 550,
            "query": "bison burger salad bowl paleo recipe no bun"
        },
        {
            "title": "Cod & Roasted Asparagus",
            "desc": "Fast digesting white fish. High protein, very low fat. Perfect pre-afternoon training.",
            "base_cals": 450,
            "query": "baked cod asparagus lemon garlic recipe foil packet"
        },
        {
            "title": "Chicken Thigh & Kimchi Bowl",
            "desc": "Probiotic rich kimchi aids gut health. Chicken thighs provide collagen.",
            "base_cals": 600,
            "query": "chicken thigh kimchi bowl paleo recipe"
        },
        {
            "title": "Shrimp Ceviche with Plantain Chips",
            "desc": "Citrus-cured protein. Extremely light on the stomach.",
            "base_cals": 400,
            "query": "shrimp ceviche recipe traditional peruvian"
        },
        {
            "title": "Grass-Fed Beef Tartare",
            "desc": "Raw enzymes and B12. Only for the strict bio-hacker. Highest bioavailability.",
            "base_cals": 500,
            "query": "steak tartare recipe classic egg yolk"
        }
    ],

    # ---------------------------------------------------------
    # DINNER: RECOVERY & DEEP SLEEP
    # Best for: Post-workout repair and Tryptophan loading for sleep.
    # ---------------------------------------------------------
    "dinner_recovery": [
        {
            "title": "Slow Roast Lamb Shank & Mash",
            "desc": "Collagen-rich connective tissue repairs joints. Mash (white potato) helps sleep.",
            "base_cals": 850,
            "query": "slow cooked lamb shank mashed potato recipe paleo"
        },
        {
            "title": "Crispy Skin Salmon & White Rice",
            "desc": "Omega-3s lower inflammation (CRP). White rice restores glycogen for tomorrow.",
            "base_cals": 750,
            "query": "crispy skin salmon white rice bowl recipe japanese"
        },
        {
            "title": "Grass-Fed Ribeye & Honey Glazed Carrots",
            "desc": "Red meat is high in Creatine and Carnitine. Carrots help bind endotoxins in the gut.",
            "base_cals": 950,
            "query": "pan seared ribeye glazed carrots recipe cast iron"
        },
        {
            "title": "Thai Coconut Curry Chicken",
            "desc": "Coconut milk provides lauric acid (immune support). Ginger reduces inflammation.",
            "base_cals": 700,
            "query": "paleo thai green curry chicken recipe coconut milk"
        },
        {
            "title": "Venison Stew with Root Vegetables",
            "desc": "Very lean game meat. High iron. Stewed cooking makes nutrients bioavailable.",
            "base_cals": 600,
            "query": "venison stew recipe slow cooker root vegetables"
        }
    ],

    # ---------------------------------------------------------
    # SNACKS / FUNCTIONAL FUEL
    # Best for: Pre-workout ignition or bridging long gaps.
    # ---------------------------------------------------------
    "snacks": [
        {
            "title": "Raw Honey & Sea Salt Fruit Salad",
            "base_cals": 200, 
            "query": "fruit salad raw honey lime adrenal cocktail",
            "desc": "Adrenal support. Minerals + Fructose."
        },
        {
            "title": "Hard Boiled Eggs & Orange Slices",
            "base_cals": 220, 
            "query": "none",
            "desc": "Protein + Vitamin C (helps absorb iron)."
        },
        {
            "title": "Bone Broth Cup (Salted)",
            "base_cals": 60, 
            "query": "bone broth homemade recipe Instant pot",
            "desc": "Pure glycine for gut lining repair."
        },
        {
            "title": "Canned Oysters / Sardines",
            "base_cals": 180, 
            "query": "canned smoked oysters snack",
            "desc": "Zinc bomb for testosterone support."
        },
        {
            "title": "Medjool Dates & Butter",
            "base_cals": 250, 
            "query": "dates stuffed with butter snack",
            "desc": "Intense energy density. Good pre-heavy squat/deadlift."
        }
    ]
}

# --- METRIC CONSTANTS ---
THRESHOLDS = {
    "recovery_red": 33,
    "recovery_green": 67,
    "strain_high": 14.0,
    "strain_low": 8.0,
    "sleep_min": 70
}