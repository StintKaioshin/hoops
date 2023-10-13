current_season = 2
max_players = 1
primary_currency_start = 1000
primary_currency_max = 100000
max_weekly_earnings = 2000  # per/week
start_attribute = 0
start_badge = 0
min_attribute = 0
max_attribute = 99
min_badge = 0
max_badge = 4
min_tendency = 0
max_tendency = 100
player_weight_min = 150
player_weight_max = 270
referral_bonus = 100
# Description: For league related model fields
max_contract_season = 3
# Description: For cap space
hard_cap = 1600
min_years = 1
max_years = 3
min_salary = 100
max_salary = 600
rookie_salary = 100
free_agent_salary = 60
# Description: For height & weight limits
min_max_heights = {
    "PG": {"min": 72, "max": 79},
    "SG": {"min": 72, "max": 81},
    "SF": {"min": 72, "max": 82},
    "PF": {"min": 72, "max": 84},
    "C": {"min": 72, "max": 86},
}
min_max_weights = {
    "PG": {"min": 150, "max": 250},
    "SG": {"min": 155, "max": 255},
    "SF": {"min": 160, "max": 260},
    "PF": {"min": 165, "max": 265},
    "C": {"min": 170, "max": 300},
}
# Description: For starting attributes
position_starting_attributes = {
    "PG": {
        "Pick Roll Defensive Iq": 50,
        "Shot Contest": 50,
        "Driving Layup": 55,
        "Post Fadeaway": 45,
        "Post Hook": 45,
        "Post Moves": 45,
        "Draw Foul": 55,
        "Close Shot": 50,
        "Mid Range Shot": 60,
        "Three Point Shot": 60,
        "Free Throw": 55,
        "Ball Control": 60,
        "Passing Iq": 60,
        "Passing Accuracy": 60,
        "Offensive Rebound": 45,
        "Standing Dunk": 45,
        "Driving Dunk": 55,
        "Shot Iq": 55,
        "Passing Vision": 60,
        "Hands": 60,
        "Defensive Rebound": 45,
        "Interior Defense": 45,
        "Lateral Quickness": 55,
        "Perimeter Defense": 55,
        "Block": 45,
        "Steal": 65,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense Iq": 60,
        "Offensive Consistency": 60,
        "Acceleration": 99,
        "Strength": 30,
        "Speed": 94,
        "Speed With Ball": 94,
        "Vertical": 95,
        "Intangibles": 60,
        "Pick Roll Defensive Iq": 60,
        "Shot Contest": 60,
    },
    "SG": {
        "Driving Layup": 65,
        "Post Fadeaway": 45,
        "Post Hook": 45,
        "Post Moves": 45,
        "Draw Foul": 55,
        "Close Shot": 60,
        "Mid Range Shot": 60,
        "Three Point Shot": 60,
        "Free Throw": 55,
        "Ball Control": 60,
        "Passing Iq": 60,
        "Passing Accuracy": 60,
        "Offensive Rebound": 45,
        "Standing Dunk": 45,
        "Driving Dunk": 55,
        "Shot Iq": 55,
        "Passing Vision": 60,
        "Hands": 60,
        "Defensive Rebound": 45,
        "Interior Defense": 45,
        "Lateral Quickness": 65,
        "Perimeter Defense": 65,
        "Block": 45,
        "Steal": 65,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense Iq": 60,
        "Offensive Consistency": 60,
        "Acceleration": 95,
        "Strength": 35,
        "Speed": 92,
        "Speed With Ball": 92,
        "Vertical": 90,
        "Intangibles": 60,
        "Pick Roll Defensive Iq": 60,
        "Shot Contest": 60,
    },
    "SF": {
        "Driving Layup": 55,
        "Post Fadeaway": 55,
        "Post Hook": 55,
        "Post Moves": 55,
        "Draw Foul": 55,
        "Close Shot": 65,
        "Mid Range Shot": 65,
        "Three Point Shot": 65,
        "Free Throw": 55,
        "Ball Control": 65,
        "Passing Iq": 65,
        "Passing Accuracy": 65,
        "Offensive Rebound": 55,
        "Standing Dunk": 55,
        "Driving Dunk": 60,
        "Shot Iq": 55,
        "Passing Vision": 55,
        "Hands": 60,
        "Defensive Rebound": 55,
        "Interior Defense": 60,
        "Lateral Quickness": 60,
        "Perimeter Defense": 60,
        "Block": 60,
        "Steal": 60,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense Iq": 60,
        "Offensive Consistency": 60,
        "Acceleration": 90,
        "Strength": 40,
        "Speed": 88,
        "Speed With Ball": 88,
        "Vertical": 80,
        "Intangibles": 60,
        "Pick Roll Defensive Iq": 60,
        "Shot Contest": 60,
    },
    "PF": {
        "Driving Layup": 45,
        "Post Fadeaway": 65,
        "Post Hook": 65,
        "Post Moves": 65,
        "Draw Foul": 55,
        "Close Shot": 60,
        "Mid Range Shot": 45,
        "Three Point Shot": 45,
        "Free Throw": 55,
        "Ball Control": 45,
        "Passing Iq": 55,
        "Passing Accuracy": 55,
        "Offensive Rebound": 60,
        "Standing Dunk": 60,
        "Driving Dunk": 45,
        "Shot Iq": 55,
        "Passing Vision": 55,
        "Hands": 60,
        "Defensive Rebound": 60,
        "Interior Defense": 55,
        "Lateral Quickness": 45,
        "Perimeter Defense": 45,
        "Block": 65,
        "Steal": 45,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense Iq": 60,
        "Offensive Consistency": 60,
        "Acceleration": 85,
        "Strength": 45,
        "Speed": 78,
        "Speed With Ball": 78,
        "Vertical": 70,
        "Intangibles": 60,
        "Pick Roll Defensive Iq": 60,
        "Shot Contest": 60,
    },
    "C": {
        "Driving Layup": 45,
        "Post Fadeaway": 65,
        "Post Hook": 65,
        "Post Moves": 65,
        "Draw Foul": 55,
        "Close Shot": 55,
        "Mid Range Shot": 60,
        "Three Point Shot": 45,
        "Free Throw": 55,
        "Ball Control": 45,
        "Passing Iq": 55,
        "Passing Accuracy": 55,
        "Offensive Rebound": 60,
        "Standing Dunk": 60,
        "Driving Dunk": 45,
        "Shot Iq": 55,
        "Passing Vision": 55,
        "Hands": 60,
        "Defensive Rebound": 60,
        "Interior Defense": 65,
        "Lateral Quickness": 45,
        "Perimeter Defense": 45,
        "Block": 65,
        "Steal": 45,
        "Hustle": 60,
        "Pass Perception": 60,
        "Defensive Consistency": 60,
        "Help Defense Iq": 60,
        "Offensive Consistency": 60,
        "Acceleration": 75,
        "Strength": 49,
        "Speed": 70,
        "Speed With Ball": 70,
        "Vertical": 60,
        "Intangibles": 60,
        "Pick Roll Defensive Iq": 60,
        "Shot Contest": 60,
    },
}
# Description: For attributes & badge prices
# Work in progress!
# This is the cost to unlock hot zones
hotzone_price = 250

# This is the cost per pound to increase or decrease weight
price_per_pound = 15

# The cost to increase attributes is divided into ranges.
# For each range, there's a different cost for base, primary, and secondary attributes.
attribute_prices = {
    "0-70": {"range": range(0, 71), "base": 60, "primary": 30, "secondary": 40},
    "71-80": {"range": range(71, 81), "base": 150, "primary": 45, "secondary": 70},
    "81-86": {"range": range(81, 87), "base": 200, "primary": 70, "secondary": 130},
    "87-93": {"range": range(87, 94), "base": 400, "primary": 100, "secondary": 200},
    "94-96": {"range": range(94, 97), "base": 800, "primary": 200, "secondary": 400},
    "97-99": {"range": range(97, 100), "base": 1200, "primary": 400, "secondary": 800},
}

# The cost to unlock badges at different levels
badge_prices = {
    1: {
        "base": 250,
        "primary": 100,
        "secondary": 150,
    },
    2: {
        "base": 350,
        "primary": 150,
        "secondary": 275,
    },
    3: {
        "base": 450,
        "primary": 175,
        "secondary": 350,
    },
    4: {
        "base": 550,
        "primary": 200,
        "secondary": 425,
    },
}

# Tendencies that players are not allowed to have
banned_tendencies = ["TOUCHES_TENDENCY", "BLOCK_SHOT_TENDENCY", "ON-BALL_STEAL_TENDENCY"]

# The maximum values for certain tendencies
max_tendencies = {
    "ON-BALL_STEAL_TENDENCY": 75,
    "BLOCK_SHOT_TENDENCY": 75,
}

# Description: For player archetypes
# Description: The player is first given starting attributes of zero, thenthey are set to the starting attributes depending on position.
# Description: Then, depending on the player's chosen archetype, archetype additions are added to the starting attributes.
# The bonus values added to primary and secondary attributes
primary_attribute_bonus = 10
secondary_attribute_bonus = 5

# The bonus values added to primary and secondary badges
primary_badge_bonus = 10
secondary_badge_bonus = 5

# We no longer have a fixed set of attributes linked to specific archetypes.
# If you have a predefined set of attribute bonuses for specific primary and secondary attributes/badges,
# we would need to adjust the data structure to reflect that.

initial_statics = {
    "playstyles": {
        "playstyle1": "0",
        "playstyle2": "0",
        "playstyle3": "0",
        "playstyle4": "0",
    }
}
initial_attributes = {
    "Driving Layup": start_attribute,
    "Standing Dunk": start_attribute,
    "Driving Dunk": start_attribute,
    "Close Shot": start_attribute,
    "Mid Range Shot": start_attribute,
    "Three Point Shot": start_attribute,
    "Free Throw": start_attribute,
    "Post Hook": start_attribute,
    "Post Fadeaway": start_attribute,
    "Post Moves": start_attribute,
    "Draw Foul": start_attribute,
    "Shot Iq": start_attribute,
    "Passing Accuracy": start_attribute,
    "Ball Control": start_attribute,
    "Speed With Ball": start_attribute,
    "Hands": start_attribute,
    "Passing Iq": start_attribute,
    "Passing Vision": start_attribute,
    "Offensive Consistency": start_attribute,
    "Interior Defense": start_attribute,
    "Perimeter Defense": start_attribute,
    "Steal": start_attribute,
    "Block": start_attribute,
    "Offensive Rebound": start_attribute,
    "Defensive Rebound": start_attribute,
    "Lateral Quickness": start_attribute,
    "Help Defense Iq": start_attribute,
    "Pass Perception": start_attribute,
    "Defensive Consistency": start_attribute,
    "Pick Roll Defensive Iq": start_attribute,
    "Shot Contest": start_attribute,
    "Speed": start_attribute,
    "Acceleration": start_attribute,
    "Strength": start_attribute,
    "Vertical": start_attribute,
    "Hustle": start_attribute,
    "Intangibles": start_attribute,
}

initial_badges = {
    "Acrobat": start_badge,
    "Backdown Punisher": start_badge,
    "Consistent Finisher": start_badge,
    "Contact Finisher": start_badge,
    "Cross-Key Scorer": start_badge,
    "Deep Hooks": start_badge,
    "Dropstepper": start_badge,
    "Fancy Footwork": start_badge,
    "Fastbreak Finisher": start_badge,
    "Giant Slayer": start_badge,
    "Lob City Finisher": start_badge,
    "Pick & Roller": start_badge,
    "Pro Touch": start_badge,
    "Putback Boss": start_badge,
    "Relentless Finisher": start_badge,
    "Showtime": start_badge,
    "Slithery Finisher": start_badge,
    "Tear Dropper": start_badge,
    "Catch & Shoot": start_badge,
    "Clutch Shooter": start_badge,
    "Corner Specialist": start_badge,
    "Deadeye": start_badge,
    "Deep Fades": start_badge,
    "Difficult Shots": start_badge,
    "Green Machine": start_badge,
    "Hot Zone Hunter": start_badge,
    "Ice In Veins": start_badge,
    "Pick & Popper": start_badge,
    "Pump Fake Maestro": start_badge,
    "Quick Draw": start_badge,
    "Range Extender": start_badge,
    "Slippery Off-Ball": start_badge,
    "Steady Shooter": start_badge,
    "Volume Shooter": start_badge,
    "Box": start_badge,
    "Brick Wall": start_badge,
    "Chase  Artist": start_badge,
    "Clamps": start_badge,
    "Defensive Leader": start_badge,
    "Heart Crusher": start_badge,
    "Interceptor": start_badge,
    "Intimidator": start_badge,
    "Lightning Reflexes": start_badge,
    "Moving Truck": start_badge,
    "Off-Ball Pest": start_badge,
    "Pick Dodger": start_badge,
    "Pick Pocket": start_badge,
    "Pogo Stick": start_badge,
    "Post Move Lock": start_badge,
    "Rebound Chaser": start_badge,
    "Rim Protector": start_badge,
    "Trapper": start_badge,
    "Worm": start_badge,
    "Ankle Breaker": start_badge,
    "Bail Out": start_badge,
    "Break Starter": start_badge,
    "Dimer": start_badge,
    "Downhill": start_badge,
    "Dream Shake": start_badge,
    "Flashy Passer": start_badge,
    "Floor General": start_badge,
    "Lob City Passer": start_badge,
    "Needle Threader": start_badge,
    "Pass Fake Maestro": start_badge,
    "Post Spin Technician": start_badge,
    "Quick First Step": start_badge,
    "Space Creator": start_badge,
    "Stop & Go": start_badge,
    "Tight Handles": start_badge,
    "Unpluckable": start_badge,
}
initial_history = {
    "grade_logs": [],
    "contract_logs": [],
    "trade_logs": [],
    "used_coons": [],
}
initial_settings = {
    "test": False,
}
initial_limits = {
    "Speed": start_attribute,
    "Speed With Ball": start_attribute,
    "Acceleration": start_attribute,
    "Vertical": start_attribute,
    "Strength": start_attribute,
}
initial_hotzones = {
    "Left Corner Three": False,
    "Left Wing Three": False,
    "Middle Three": False,
    "Right Wing Three": False,
    "Right Corner Three": False,
    "Left Corner Midrange": False,
    "Left Wing Midrange": False,
    "Middle Midrange": False,
    "Right Wing Midrange": False,
    "Right Corner Midrange": False,
    "Inside Left": False,
    "Inside Middle": False,
    "Inside Right": False,
    "Inside Center": False,
}
initial_tendencies = {
    "STEP_THROUGH_SHOT_TENDENCY": 0,
    "SHOT_UNDER_BASKET_TENDENCY": 0,
    "SHOT_CLOSE_TENDENCY": 0,
    "SHOT_CLOSE_LEFT_TENDENCY": 0,
    "SHOT_CLOSE_MIDDLE_TENDENCY": 0,
    "SHOT_CLOSE_RIGHT_TENDENCY": 0,
    "SHOT_MID-RANGE_TENDENCY": 0,
    "SPOT__SHOT_MID-RANGE_TENDENCY": 0,
    "OFF_SCREEN_SHOT_MID-RANGE_TENDENCY": 0,
    "SHOT_MID_LEFT_TENDENCY": 0,
    "SHOT_MID_LEFT-CENTER_TENDENCY": 0,
    "SHOT_MID_CENTER_TENDENCY": 0,
    "SHOT_MID_RIGHT-CENTER_TENDENCY": 0,
    "SHOT_MID_RIGHT_TENDENCY": 0,
    "SHOT_THREE_TENDENCY": 0,
    "SPOT__SHOT_THREE_TENDENCY": 0,
    "OFF_SCREEN_SHOT_THREE_TENDENCY": 0,
    "SHOT_THREE_LEFT_TENDENCY": 0,
    "SHOT_THREE_LEFT-CENTER_TENDENCY": 0,
    "SHOT_THREE_CENTER_TENDENCY": 0,
    "SHOT_THREE_RIGHT-CENTER_TENDENCY": 0,
    "SHOT_THREE_RIGHT_TENDENCY": 0,
    "CONTESTED_JUMPER_THREE_TENDENCY": 0,
    "CONTESTED_JUMPER_MID-RANGE_TENDENCY": 0,
    "STEPBACK_JUMPER_THREE_TENDENCY": 0,
    "STEPBACK_JUMPER_MID-RANGE_TENDENCY": 0,
    "SPIN_JUMPER_TENDENCY": 0,
    "TRANSITION_PULL__THREE_TENDENCY": 0,
    "DRIVE_PULL__THREE_TENDENCY": 0,
    "DRIVE_PULL__MID-RANGE_TENDENCY": 0,
    "USE_GLASS_TENDENCY": 0,
    "DRIVING_LAY_TENDENCY": 0,
    "STANDING_DUNK_TENDENCY": 0,
    "DRIVING_DUNK_TENDENCY": 0,
    "FLASHY_DUNK_TENDENCY": 0,
    "ALLEY-OOP_TENDENCY": 0,
    "PUTBACK_TENDENCY": 0,
    "CRASH_TENDENCY": 0,
    "SPIN_LAY_TENDENCY": 0,
    "HOP_STEP_LAY_TENDENCY": 0,
    "EURO_STEP_LAY_TENDENCY": 0,
    "FLOATER_TENDENCY": 0,
    "TRIPLE_THREAT_PUMP_FAKE_TENDENCY": 0,
    "TRIPLE_THREAT_JAB_STEP_TENDENCY": 0,
    "TRIPLE_THREAT_IDLE_TENDENCY": 0,
    "TRIPLE_THREAT_SHOOT_TENDENCY": 0,
    "SET_WITH_SIZE_TENDENCY": 0,
    "SET_WITH_HESITATION_TENDENCY": 0,
    "NO_SET_DRIBBLE_TENDENCY": 0,
    "DRIVE_TENDENCY": 0,
    "SPOT__DRIVE_TENDENCY": 0,
    "OFF_SCREEN_DRIVE_TENDENCY": 0,
    "DRIVE_RIGHT_TENDENCY": 0,
    "DRIVE_CROSSOVER_TENDENCY": 0,
    "DRIVE_SPIN_TENDENCY": 0,
    "DRIVING_STEP_BACK_TENDENCY": 0,
    "DRIVING_HALF_SPIN_TENDENCY": 0,
    "DRIVING_DOUBLE_CROSSOVER_TENDENCY": 0,
    "DRIVING_BEHIND_THE_BACK_TENDENCY": 0,
    "DRIVING_DRIBBLE_HESITATION_TENDENCY": 0,
    "DRIVING_IN_AND_OUT_TENDENCY": 0,
    "NO_DRIVING_DRIBBLE_MOVE_TENDENCY": 0,
    "ATTACK_STRONG_ON_DRIVE_TENDENCY": 0,
    "DISH_TO_OPEN_MAN_TENDENCY": 0,
    "FLASHY_PASS_TENDENCY": 0,
    "ALLEY-OOP_PASS_TENDENCY": 0,
    "POST__TENDENCY": 0,
    "POST_SHIMMY_SHOT_TENDENCY": 0,
    "POST_FACE__TENDENCY": 0,
    "POST_BACK__TENDENCY": 0,
    "POST_AGGRESSIVE_BACK_TENDENCY": 0,
    "SHOOT_FROM_POST_TENDENCY": 0,
    "POST_HOOK_LEFT_TENDENCY": 0,
    "POST_HOOK_RIGHT_TENDENCY": 0,
    "POST_FADE_LEFT_TENDENCY": 0,
    "POST_FADE_RIGHT_TENDENCY": 0,
    "POST__AND_UNDER_TENDENCY": 0,
    "POST_HOP_SHOT_TENDENCY": 0,
    "POST_STEP_BACK_SHOT_TENDENCY": 0,
    "POST_DRIVE_TENDENCY": 0,
    "POST_SPIN_TENDENCY": 0,
    "POST_DROP_STEP_TENDENCY": 0,
    "POST_HOP_STEP_TENDENCY": 0,
    "SHOT_TENDENCY": 0,
    "TOUCHES_TENDENCY": 0,
    "ROLL_VS._POP_TENDENCY": 0,
    "TRANSITION_SPOT__TENDENCY": 0,
    "ISO_VS._ELITE_DEFENDER_TENDENCY": 0,
    "ISO_VS._GOOD_DEFENDER_TENDENCY": 0,
    "ISO_VS._AVERAGE_DEFENDER_TENDENCY": 0,
    "ISO_VS._POOR_DEFENDER_TENDENCY": 0,
    "PLAY_DISCIPLINE_TENDENCY": 0,
    "PASS_INTERCEPTION_TENDENCY": 0,
    "TAKE_CHARGE_TENDENCY": 0,
    "ON-BALL_STEAL_TENDENCY": 0,
    "CONTEST_SHOT_TENDENCY": 0,
    "BLOCK_SHOT_TENDENCY": 0,
    "FOUL_TENDENCY": 0,
    "HARD_FOUL_TENDENCY": 0,
}
initial_picks = {}
initial_styles = {}
initial_trade_offer = {}
initial_team_logo = "https://cdn.simplystamps.com/media/catalog/product/5/8/5802-n-a-stock-stamp-hcb.png"
initial_headshot = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
# Description: Choices & labels for player forms
height_choices = [
    (72, "6'0"),
    (73, "6'1"),
    (74, "6'2"),
    (75, "6'3"),
    (76, "6'4"),
    (77, "6'5"),
    (78, "6'6"),
    (79, "6'7"),
    (80, "6'8"),
    (81, "6'9"),
    (82, "6'10"),
    (83, "6'11"),
    (84, "7'0"),
    (85, "7'1"),
    (86, "7'2"),
]
position_choices = [
    ("PG", "Point Guard"),
    ("SG", "Shooting Guard"),
    ("SF", "Small Forward"),
    ("PF", "Power Forward"),
    ("C", "Center"),
]

badge_upgrade_choices = [
    (0, "Current"),
    (1, "Bronze"),
    (2, "Silver"),
    (3, "Gold"),
    (4, "Hall of Fame"),
]

transaction_type_choices = [
    ("cash_taken", "Cash Taken"),
    ("cash_given", "Cash Given"),
    ("paycheck", "Paycheck"),
]
contract_option_choices = [
    ("No Option", "No Option"),
    ("Team Option", "Team Option"),
    ("Player Option", "Player Option"),
    ("Restricted Free Agent", "Restricted Free Agent"),
]
contract_benefit_choices = [
    ("No Benefits", "No Benefits"),
    ("No Trade Clause", "No Trade Clause"),
    ("No Cut Clause", "No Cut Clause"),
    ("No Trade Clause + No Cut Clause", "No Trade Clause + No Cut Clause"),
]
award_name_choices = [
    ("MVP", "MVP"),
    ("DPOY", "DPOY"),
    ("MIP", "MIP"),
    ("ROY", "ROY"),
    ("6MOY", "6MOY"),
    ("AH1ST", "AH1ST"),
    ("AH2ND", "AH2ND"),
    ("D1ST", "D1ST"),
    ("D2ND", "D2ND"),
    ("KOTS", "KOTS"),
    ("RING", "RING"),
    ("FMVP", "FMVP"),
    ("ASG", "ASG"),
    ("ASGMVP", "ASGMVP"),
    ("3PTWIN", "3PTWIN"),
    ("DNKWIN", "DNKWIN"),
]
hotzone_choices = [
    ("0", "None"),
    ("1", "Equipped"),
]


primary_badge_max = 4
secondary_badge_max = 3
tertiary_badge_max = 2


# Description: Categories for .html pages
attribute_categories = {
    "finishing": [
        "Driving Layup",
        "Post Moves",
        "Draw Foul",
        "Close Shot",
        "Standing Dunk",
        "Driving Dunk",
    ],
    "shooting": [
        "Post Fadeaway",
        "Post Hook",
        "Mid Range Shot",
        "Three Point Shot",
        "Free Throw",
        "Shot Iq",
    ],
    "defense": [
        "Defensive Rebound",
        "Offensive Rebound",
        "Interior Defense",
        "Perimeter Defense",
        "Block",
        "Steal",
        "Defensive Consistency",
        "Help Defense Iq",
        "Pass Perception",
        "Pick Roll Defensive Iq",
        "Shot Contest",
    ],
    "playmaking": [
        "Hands",
        "Ball Control",
        "Passing Iq",
        "Passing Vision",
        "Passing Accuracy",
        "Offensive Consistency",
        "Intangibles",
    ],
    "physical": [
        "Speed",
        "Acceleration",
        "Vertical",
        "Strength",
        "Speed With Ball",
        "Lateral Quickness",      
        "Hustle",

    ],
}
badge_categories = {
    "finishing": [
        "Acrobat",
        "Backdown Punisher",
        "Consistent Finisher",
        "Contact Finisher",
        "Cross-Key Scorer",
        "Deep Hooks",
        "Dropstepper",
        "Fancy Footwork",
        "Fastbreak Finisher",
        "Giant Slayer",
        "Lob City Finisher",
        "Pick & Roller",
        "Pro Touch",
        "Putback Boss",
        "Relentless Finisher",
        "Showtime",
        "Slithery Finisher",
        "Tear Dropper",
    ],
    "shooting": [
        "Catch Shoot",
        "Clutch Shooter",
        "Corner Specialist",
        "Deadeye",
        "Deep Fades",
        "Difficult Shots",
        "Flexible Release",
        "Green Machine",
        "Hot Zone Hunter",
        "Ice In Veins",
        "Pick & Popper",
        "Pump Fake Maestro",
        "Quick Draw",
        "Range Extender",
        "Slippery Off-Ball",
        "Steady Shooter",
        "Tireless Shooter",
        "Volume Shooter",
    ],
    "defense": [
        "Box",
        "Brick Wall",
        "Chase  Artist",
        "Clamps",
        "Defensive Leader",
        "Heart Crusher",
        "Interceptor",
        "Intimidator",
        "Lightning Reflexes",
        "Moving Truck",
        "Off-Ball Pest",
        "Pick Dodger",
        "Pick Pocket",
        "Pogo Stick",
        "Post Move Lock",
        "Rebound Chaser",
        "Rim Protector",
        "Tireless Defender",
        "Trapper",
        "Worm",
    ],
    "playmaking": [
        "Ankle Breaker",
        "Bail Out",
        "Break Starter",
        "Dimer",
        "Downhill",
        "Dream Shake",
        "Flashy Passer",
        "Floor General",
        "Handles For Days",
        "Lob City Passer",
        "Needle Threader",
        "Pass Fake Maestro",
        "Post Spin Technician",
        "Quick First Step",
        "Space Creator",
        "Stop & Go",
        "Tight Handles",
        "Unpluckable",
    ],
}
# Description: Initials methods for models
playstyles = {
    "0": "None",
    "1": "Isolation",
    "2": "Isolation Point",
    "3": "Isolation Wing",
    "4": "P&R Ball Handler",
    "5": "P&R Point",
    "6": "P&R Wing",
    "7": "P&R Roll Man",
    "8": "Post  Low",
    "9": "Post  High",
    "10": "Guard Post ",
    "11": "Cutter",
    "12": "Handoff",
    "13": "Midrange",
    "14": "3PT",
}


def get_default_statics():
    return initial_statics
def get_default_attributes():
    return initial_attributes
def get_default_badges():
    return initial_badges
def get_default_history():
    return initial_history
def get_default_settings():
    return initial_settings
def get_default_limits():
    return initial_limits
def get_default_hotzones():
    return initial_hotzones
def get_default_tendencies():
    return initial_tendencies
def get_default_picks():
    return initial_picks
def get_default_trade_offer():
    return initial_trade_offer
def get_default_styles():
    return initial_styles
