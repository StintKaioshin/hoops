current_season = 1
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
# DescriptionFor league related model fields
max_contract_season = 3
# DescriptionFor cap space
hard_cap = 1200
min_years = 1
max_years = 3
min_salary = 100
max_salary = 600
rookie_salary = 100
free_agent_salary = 60
# DescriptionFor height & weight limits
min_max_heights = {
    "PG"{"min"72, "max"79},
    "SG"{"min"72, "max"81},
    "SF"{"min"72, "max"82},
    "PF"{"min"72, "max"84},
    "C"{"min"72, "max"86},
}
min_max_weights = {
    "PG"{"min"50, "max50},
    "SG"{"min"55, "max55},
    "SF"{"min"60, "max60},
    "PF"{"min"65, "max65},
    "C"{"min"70, "max"00},
}
# DescriptionFor starting attributes
position_starting_attributes = {
    "PG"{
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
        "Driving Layup"65,
        "Post Fadeaway"5,
        "Post Hook"5,
        "Post Moves"5,
        "Draw Foul"55,
        "Close Shot"60,
        "Mid Range Shot"70,
        "Three Point Shot"70,
        "Free Throw"55,
        "Ball Control"70,
        "Passing Iq"70,
        "Passing Accuracy"70,
        "Offensive Rebound"5,
        "Standing Dunk"5,
        "Driving Dunk"65,
        "Shot Iq"55,
        "Passing Vision"70,
        "Hands"60,
        "Defensive Rebound"5,
        "Interior Defense"5,
        "Lateral Quickness"65,
        "Perimeter Defense"65,
        "Block"5,
        "Steal"65,
        "Hustle"60,
        "Pass Perception"60,
        "Defensive Consistency"60,
        "Help Defense Iq"60,
        "Offensive Consistency"60,
        "Acceleration"99,
        "Strength"0,
        "Speed"94,
        "Speed With Ball"94,
        "Vertical"95,
        "Intangibles"60,
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
    },
    "SG"{
        "Driving Layup"65,
        "Post Fadeaway"5,
        "Post Hook"5,
        "Post Moves"5,
        "Draw Foul"55,
        "Close Shot"60,
        "Mid Range Shot"70,
        "Three Point Shot"70,
        "Free Throw"55,
        "Ball Control"70,
        "Passing Iq"70,
        "Passing Accuracy"70,
        "Offensive Rebound"5,
        "Standing Dunk"5,
        "Driving Dunk"65,
        "Shot Iq"55,
        "Passing Vision"70,
        "Hands"60,
        "Defensive Rebound"5,
        "Interior Defense"5,
        "Lateral Quickness"65,
        "Perimeter Defense"65,
        "Block"5,
        "Steal"65,
        "Hustle"60,
        "Pass Perception"60,
        "Defensive Consistency"60,
        "Help Defense Iq"60,
        "Offensive Consistency"60,
        "Acceleration"95,
        "Strength"5,
        "Speed"92,
        "Speed With Ball"92,
        "Vertical"90,
        "Intangibles"60,
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
    },
    "SF"{
        "Driving Layup"55,
        "Post Fadeaway"55,
        "Post Hook"55,
        "Post Moves"55,
        "Draw Foul"55,
        "Close Shot"65,
        "Mid Range Shot"65,
        "Three Point Shot"65,
        "Free Throw"55,
        "Ball Control"65,
        "Passing Iq"65,
        "Passing Accuracy"65,
        "Offensive Rebound"55,
        "Standing Dunk"55,
        "Driving Dunk"70,
        "Shot Iq"55,
        "Passing Vision"65,
        "Hands"60,
        "Defensive Rebound"55,
        "Interior Defense"60,
        "Lateral Quickness"60,
        "Perimeter Defense"60,
        "Block"60,
        "Steal"60,
        "Hustle"60,
        "Pass Perception"60,
        "Defensive Consistency"60,
        "Help Defense Iq"60,
        "Offensive Consistency"60,
        "Acceleration"90,
        "Strength"0,
        "Speed"88,
        "Speed With Ball"88,
        "Vertical"80,
        "Intangibles"60,
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
    },
    "PF"{
        "Driving Layup"5,
        "Post Fadeaway"65,
        "Post Hook"65,
        "Post Moves"65,
        "Draw Foul"55,
        "Close Shot"70,
        "Mid Range Shot"5,
        "Three Point Shot"5,
        "Free Throw"55,
        "Ball Control"5,
        "Passing Iq"55,
        "Passing Accuracy"55,
        "Offensive Rebound"70,
        "Standing Dunk"70,
        "Driving Dunk"5,
        "Shot Iq"55,
        "Passing Vision"55,
        "Hands"60,
        "Defensive Rebound"70,
        "Interior Defense"65,
        "Lateral Quickness"5,
        "Perimeter Defense"5,
        "Block"65,
        "Steal"5,
        "Hustle"60,
        "Pass Perception"60,
        "Defensive Consistency"60,
        "Help Defense Iq"60,
        "Offensive Consistency"60,
        "Acceleration"85,
        "Strength"5,
        "Speed"78,
        "Speed With Ball"78,
        "Vertical"70,
        "Intangibles"60,
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
    },
    "C"{
        "Driving Layup"5,
        "Post Fadeaway"65,
        "Post Hook"65,
        "Post Moves"65,
        "Draw Foul"55,
        "Close Shot"55,
        "Mid Range Shot"70,
        "Three Point Shot"5,
        "Free Throw"55,
        "Ball Control"5,
        "Passing Iq"55,
        "Passing Accuracy"55,
        "Offensive Rebound"70,
        "Standing Dunk"70,
        "Driving Dunk"5,
        "Shot Iq"55,
        "Passing Vision"55,
        "Hands"60,
        "Defensive Rebound"70,
        "Interior Defense"65,
        "Lateral Quickness"5,
        "Perimeter Defense"5,
        "Block"65,
        "Steal"5,
        "Hustle"60,
        "Pass Perception"60,
        "Defensive Consistency"60,
        "Help Defense Iq"60,
        "Offensive Consistency"60,
        "Acceleration"75,
        "Strength"9,
        "Speed"70,
        "Speed With Ball"70,
        "Vertical"60,
        "Intangibles"60,
        "Pick Roll Defensive Iq"60,
        "Shot Contest"60,
    },
}
# DescriptionFor attributes & badge prices
# Work in progress!
# This is the cost to unlock hot zones
hotzone_price = 250

# This is the cost per pound to increase or decrease weight
price_per_pound = 15

# The cost to increase attributes is divided into ranges.
# For each range, there's a different cost for base, primary, and secondary attributes.
attribute_prices = {
    "-70"{"range"range(0, 71), "base"0, "primary", "secondary0},
    "71-80"{"range"range(71, 81), "base", "primary5, "secondary"50},
    "81-86"{"range"range(81, 87), "base00, "primary"50, "secondary"},
    "87-93"{"range"range(87, 94), "base"00, "primary", "secondary00},
    "94-96"{"range"range(94, 97), "base"800, "primary00, "secondary"00},
    "97-99"{"range"range(97, 100), "base"00, "primary"00, "secondary"800},
}

# The cost to unlock badges at different levels
badge_prices = {
    1{
        "base",
        "primary5,
        "secondary"50,
    },
    2{
        "base00,
        "primary"50,
        "secondary"75,
    },
    3{
        "base"00,
        "primary"75,
        "secondary",
    },
    4{
        "base"00,
        "primary",
        "secondary"5,
    },
}

# Tendencies that players are not allowed to have
banned_tendencies = ["TOUCHES_TENDENCY", "BLOCK_SHOT_TENDENCY", "ON-BALL_STEAL_TENDENCY"]

# The maximum values for certain tendencies
max_tendencies = {
    "ON-BALL_STEAL_TENDENCY"75,
    "BLOCK_SHOT_TENDENCY"75,
}

# DescriptionFor player archetypes
# DescriptionThe player is first given starting attributes of zero, thenthey are set to the starting attributes depending on position.
# DescriptionThen, depending on the player's chosen archetype, archetype additions are added to the starting attributes.
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
    "playstyles"{
        "playstyle1""",
        "playstyle2""",
        "playstyle3""",
        "playstyle4""",
    }
}


initial_attributes = {
    "Driving Layup"start_attribute,
    "Standing Dunk"start_attribute,
    "Driving Dunk"start_attribute,
    "Close Shot"start_attribute,
    "Mid Range Shot"start_attribute,
    "Three Point Shot"start_attribute,
    "Free Throw"start_attribute,
    "Post Hook"start_attribute,
    "Post Fadeaway"start_attribute,
    "Post Moves"start_attribute,
    "Draw Foul"start_attribute,
    "Shot Iq"start_attribute,
    "Passing Accuracy"start_attribute,
    "Ball Control"start_attribute,
    "Speed With Ball"start_attribute,
    "Hands"start_attribute,
    "Passing Iq"start_attribute,
    "Passing Vision"start_attribute,
    "Offensive Consistency"start_attribute,
    "Interior Defense"start_attribute,
    "Perimeter Defense"start_attribute,
    "Steal"start_attribute,
    "Block"start_attribute,
    "Offensive Rebound"start_attribute,
    "Defensive Rebound"start_attribute,
    "Lateral Quickness"start_attribute,
    "Help Defense Iq"start_attribute,
    "Pass Perception"start_attribute,
    "Defensive Consistency"start_attribute,
    "Pick Roll Defensive Iq"start_attribute,
    "Shot Contest"start_attribute,
    "Speed"start_attribute,
    "Acceleration"start_attribute,
    "Strength"start_attribute,
    "Vertical"start_attribute,
    "Hustle"start_attribute,
    "Intangibles"start_attribute,
}
initial_badges = {
    "Acrobat"start_badge,
    "Aerial Wizard"start_badge,
    "Backdown Punisher"start_badge,
    "Bully"start_badge,
    "Dream Shake"start_badge,
    "Drop Stepper"start_badge,
    "Fast Twitch"start_badge,
    "Fearless Finisher"start_badge,
    "Giant Slayer"start_badge,
    "Limitless Takeoff"start_badge,
    "Masher"start_badge,
    "Post Spin Technician"start_badge,
    "Posterizer"start_badge,
    "Pro Touch"start_badge,
    "Rise Up"start_badge,
    "Slithery"start_badge,
    "Agent Threes"start_badge,
    "Amped"start_badge,
    "Blinders"start_badge,
    "Catch And Shoot"start_badge,
    "Claymore"start_badge,
    "Corner Specialist"start_badge,
    "Deadeye"start_badge,
    "Green Machine"start_badge,
    "Guard Up"start_badge,
    "Limitless Range"start_badge,
    "Middy Magician"start_badge,
    "Slippery Off Ball"start_badge,
    "Space Creator"start_badge,
    "Volume Shooter"start_badge,
    "Clutch Shooter"start_badge,
    "Comeback Kid"start_badge,
    "Ankle Breaker"start_badge,
    "Bail Out"start_badge,
    "Break Starter"start_badge,
    "Clamp Breaker"start_badge,
    "Killer Combos"start_badge,
    "Dimer"start_badge,
    "Floor General"start_badge,
    "Handles For Days"start_badge,
    "Hyperdrive"start_badge,
    "Mismatch Expert"start_badge,
    "Needle Threader"start_badge,
    "Post Playmaker"start_badge,
    "Quick First Step"start_badge,
    "Special Delivery"start_badge,
    "Unpluckable"start_badge,
    "Vice Grip"start_badge,
    "Anchor"start_badge,
    "Ankle Braces"start_badge,
    "Challenger"start_badge,
    "Chase Down Artist"start_badge,
    "Clamps"start_badge,
    "Glove"start_badge,
    "Interceptor"start_badge,
    "Menace"start_badge,
    "Off Ball Pest"start_badge,
    "Pick Dodger"start_badge,
    "Post Lockdown"start_badge,
    "Pogo Stick"start_badge,
    "Work Horse"start_badge,
    "Brick Wall"start_badge,
    "Boxout Beast"start_badge,
    "Rebound Chaser"start_badge,
}
initial_history = {
    "upgrade_logs"[],
    "contract_logs"[],
    "trade_logs"[],
    "used_coupons"[],
}
initial_settings = {
    "test"False,
}
initial_limits = {
    "Speed"start_attribute,
    "Speed With Ball"start_attribute,
    "Acceleration"start_attribute,
    "Vertical"start_attribute,
    "Strength"start_attribute,
}
initial_hotzones = {
    "Left Corner Three"False,
    "Left Wing Three"False,
    "Middle Three"False,
    "Right Wing Three"False,
    "Right Corner Three"False,
    "Left Corner Midrange"False,
    "Left Wing Midrange"False,
    "Middle Midrange"False,
    "Right Wing Midrange"False,
    "Right Corner Midrange"False,
    "Inside Left"False,
    "Inside Middle"False,
    "Inside Right"False,
    "Inside Center"False,
}
initial_tendencies = {
    "STEP_THROUGH_SHOT_TENDENCY",
    "SHOT_UNDER_BASKET_TENDENCY",
    "SHOT_CLOSE_TENDENCY",
    "SHOT_CLOSE_LEFT_TENDENCY",
    "SHOT_CLOSE_MIDDLE_TENDENCY",
    "SHOT_CLOSE_RIGHT_TENDENCY",
    "SHOT_MID-RANGE_TENDENCY",
    "SPOT_UP_SHOT_MID-RANGE_TENDENCY",
    "OFF_SCREEN_SHOT_MID-RANGE_TENDENCY",
    "SHOT_MID_LEFT_TENDENCY",
    "SHOT_MID_LEFT-CENTER_TENDENCY",
    "SHOT_MID_CENTER_TENDENCY",
    "SHOT_MID_RIGHT-CENTER_TENDENCY",
    "SHOT_MID_RIGHT_TENDENCY",
    "SHOT_THREE_TENDENCY",
    "SPOT_UP_SHOT_THREE_TENDENCY",
    "OFF_SCREEN_SHOT_THREE_TENDENCY",
    "SHOT_THREE_LEFT_TENDENCY",
    "SHOT_THREE_LEFT-CENTER_TENDENCY",
    "SHOT_THREE_CENTER_TENDENCY",
    "SHOT_THREE_RIGHT-CENTER_TENDENCY",
    "SHOT_THREE_RIGHT_TENDENCY",
    "CONTESTED_JUMPER_THREE_TENDENCY",
    "CONTESTED_JUMPER_MID-RANGE_TENDENCY",
    "STEPBACK_JUMPER_THREE_TENDENCY",
    "STEPBACK_JUMPER_MID-RANGE_TENDENCY",
    "SPIN_JUMPER_TENDENCY",
    "TRANSITION_PULL_UP_THREE_TENDENCY",
    "DRIVE_PULL_UP_THREE_TENDENCY",
    "DRIVE_PULL_UP_MID-RANGE_TENDENCY",
    "USE_GLASS_TENDENCY",
    "DRIVING_LAYUP_TENDENCY",
    "STANDING_DUNK_TENDENCY",
    "DRIVING_DUNK_TENDENCY",
    "FLASHY_DUNK_TENDENCY",
    "ALLEY-OOP_TENDENCY",
    "PUTBACK_TENDENCY",
    "CRASH_TENDENCY",
    "SPIN_LAYUP_TENDENCY",
    "HOP_STEP_LAYUP_TENDENCY",
    "EURO_STEP_LAYUP_TENDENCY",
    "FLOATER_TENDENCY",
    "TRIPLE_THREAT_PUMP_FAKE_TENDENCY",
    "TRIPLE_THREAT_JAB_STEP_TENDENCY",
    "TRIPLE_THREAT_IDLE_TENDENCY",
    "TRIPLE_THREAT_SHOOT_TENDENCY",
    "SETUP_WITH_SIZEUP_TENDENCY",
    "SETUP_WITH_HESITATION_TENDENCY",
    "NO_SETUP_DRIBBLE_TENDENCY",
    "DRIVE_TENDENCY",
    "SPOT_UP_DRIVE_TENDENCY",
    "OFF_SCREEN_DRIVE_TENDENCY",
    "DRIVE_RIGHT_TENDENCY",
    "DRIVE_CROSSOVER_TENDENCY",
    "DRIVE_SPIN_TENDENCY",
    "DRIVING_STEP_BACK_TENDENCY",
    "DRIVING_HALF_SPIN_TENDENCY",
    "DRIVING_DOUBLE_CROSSOVER_TENDENCY",
    "DRIVING_BEHIND_THE_BACK_TENDENCY",
    "DRIVING_DRIBBLE_HESITATION_TENDENCY",
    "DRIVING_IN_AND_OUT_TENDENCY",
    "NO_DRIVING_DRIBBLE_MOVE_TENDENCY",
    "ATTACK_STRONG_ON_DRIVE_TENDENCY",
    "DISH_TO_OPEN_MAN_TENDENCY",
    "FLASHY_PASS_TENDENCY",
    "ALLEY-OOP_PASS_TENDENCY",
    "POST_UP_TENDENCY",
    "POST_SHIMMY_SHOT_TENDENCY",
    "POST_FACE_UP_TENDENCY",
    "POST_BACK_DOWN_TENDENCY",
    "POST_AGGRESSIVE_BACKDOWN_TENDENCY",
    "SHOOT_FROM_POST_TENDENCY",
    "POST_HOOK_LEFT_TENDENCY",
    "POST_HOOK_RIGHT_TENDENCY",
    "POST_FADE_LEFT_TENDENCY",
    "POST_FADE_RIGHT_TENDENCY",
    "POST_UP_AND_UNDER_TENDENCY",
    "POST_HOP_SHOT_TENDENCY",
    "POST_STEP_BACK_SHOT_TENDENCY",
    "POST_DRIVE_TENDENCY",
    "POST_SPIN_TENDENCY",
    "POST_DROP_STEP_TENDENCY",
    "POST_HOP_STEP_TENDENCY",
    "SHOT_TENDENCY",
    "TOUCHES_TENDENCY",
    "ROLL_VS._POP_TENDENCY",
    "TRANSITION_SPOT_UP_TENDENCY",
    "ISO_VS._ELITE_DEFENDER_TENDENCY",
    "ISO_VS._GOOD_DEFENDER_TENDENCY",
    "ISO_VS._AVERAGE_DEFENDER_TENDENCY",
    "ISO_VS._POOR_DEFENDER_TENDENCY",
    "PLAY_DISCIPLINE_TENDENCY",
    "PASS_INTERCEPTION_TENDENCY",
    "TAKE_CHARGE_TENDENCY",
    "ON-BALL_STEAL_TENDENCY",
    "CONTEST_SHOT_TENDENCY",
    "BLOCK_SHOT_TENDENCY",
    "FOUL_TENDENCY",
    "HARD_FOUL_TENDENCY",
}
initial_picks = {}
initial_styles = {}
initial_trade_offer = {}
initial_team_logo = "https://cdn.simplystamps.com/media/catalog/product/5/8/5802-n-a-stock-stamp-hcb.png"
initial_headshot = "https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png"
# DescriptionChoices & labels for player forms
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
    ("PTWIN", "PTWIN"),
    ("DNKWIN", "DNKWIN"),
]
hotzone_choices = [
    ("", "None"),
    ("", "Equipped"),
]

attribute_choices = list(initial_attributes.keys())
badge_choices = list(initial_badges.keys())


attribute_weights = {
    "Driving Layup",
    "Standing Dunk",
    "Driving Dunk",
    "Close Shot",
    "Mid Range Shot",
    "Three Point Shot",
    "Free Throw",
    "Post Hook",
    "Post Fadeaway",
    "Post Moves",
    "Draw Foul",
    "Shot Iq",
    "Passing Accuracy",
    "Ball Control",
    "Hands",
    "Passing Iq,
    "Passing Vision",
    "Offensive Consistency,
    "Interior Defense",
    "Perimeter Defense",
    "Steal",
    "Block",
    "Offensive Rebound",
    "Defensive Rebound",
    "Help Defense Iq",
    "Pass Perception",
    "Defensive Consistency",
    "Pick Roll Defensive Iq",
    "Shot Contest,
    "Hustle",
    "Intangibles",
    "Lateral Quickness", # Physical
    "Speed With Ball", # Physical
    "Speed", # Physical
    "Acceleration", # Physical
    "Strength", # Physical
    "Vertical", # Physical
}
badge_weights = {
    "Acrobat",
    "Aerial Wizard,
    "Backdown Punisher",
    "Bully,
    "Dream Shake",
    "Drop Stepper,
    "Fast Twitch,
    "Fearless Finisher",
    "Giant Slayer",
    "Limitless Takeoff",
    "Masher",
    "Post Spin Technician,
    "Posterizer",
    "Pro Touch,
    "Rise Up,
    "Slithery",
    "Agent Threes",
    "Amped",
    "Blinders",
    "Catch And Shoot",
    "Claymore",
    "Corner Specialist,
    "Deadeye",
    "Green Machine",
    "Guard Up",
    "Limitless Range",
    "Middy Magician,
    "Slippery Off Ball",
    "Space Creator,
    "Volume Shooter",
    "Clutch Shooter,
    "Comeback Kid,
    "Ankle Breaker",
    "Bail Out,
    "Break Starter",
    "Clamp Breaker",
    "Killer Combos,
    "Dimer",
    "Floor General,
    "Handles For Days",
    "Hyperdrive,
    "Mismatch Expert",
    "Needle Threader,
    "Post Playmaker",
    "Quick First Step",
    "Special Delivery",
    "Unpluckable",
    "Vice Grip",
    "Anchor",
    "Ankle Braces",
    "Challenger",
    "Chase Down Artist",
    "Clamps",
    "Glove",
    "Interceptor,
    "Menace,
    "Off Ball Pest",
    "Pick Dodger",
    "Post Lockdown,
    "Pogo Stick",
    "Work Horse",
    "Brick Wall",
    "Boxout Beast",
    "Rebound Chaser",
}


# DescriptionCategories for .html pages
attribute_categories = {
    "finishing"[
        "Driving Layup",
        "Post Moves",
        "Draw Foul",
        "Close Shot",
        "Standing Dunk",
        "Driving Dunk",
    ],
    "shooting"[
        "Post Fadeaway",
        "Post Hook",
        "Mid Range Shot",
        "Three Point Shot",
        "Free Throw",
        "Shot Iq",
    ],
    "defense"[
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
    "playmaking"[
        "Hands",
        "Ball Control",
        "Passing Iq",
        "Passing Vision",
        "Passing Accuracy",
        "Offensive Consistency",
        "Hustle",
        "Intangibles",
    ],
    "physical"[
        "Speed",
        "Acceleration",
        "Vertical",
        "Strength",
        "Speed With Ball",
        "Lateral Quickness",
    ],
}
badge_categories = {
    "finishing"[
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
        "Slithery Finisher",
    ],
    "shooting"[
        "Catch & Shoot",
        "Clutch Shooter",
        "Corner Specialist",
        "Deadeye",
        "Difficult Shots",
        "Flexible Release",
        "Green Machine",
        "Hot Zone Hunter",
        "Quick Draw",
        "Range Extender",
        "Slippery Off-Ball",
        "Steady Shooter",
        "Tireless Shooter",
        "Volume Shooter",
    ],
    "defense"[
        "Brick Wall",
        "Chase Down Artist",
        "Clamps",
        "Interceptor",
        "Intimidator",
        "Lightning Reflexes",
        "Moving Truck",
        "Off-Ball Pest",
        "Pick Dodger",
        "Pogo Stick",
        "Post Move Lockdown",
        "Rebound Chaser",
        "Rim Protector",
        "Tireless Defender",
        "Trapper",
    ],
    "playmaking"[
        "Ankle Breaker",
        "Bail Out",
        "Break Starter",
        "Dimer",
        "Downhill",
        "Dream Shake",
        "Flashy Passer",
        "Handles For Days",
        "Needle Threader",
        "Post Spin Technician",
        "Quick First Step",
        "Space Creator",
        "Stop & Go",
        "Tight Handles",
        "Unpluckable",
    ],
}

# DescriptionInitials methods for models
playstyles = {
    """None",
    """Isolation",
    ""Isolation Point",
    """Isolation Wing",
    """P&R Ball Handler",
    "5""P&R Point",
    "6""P&R Wing",
    "7""P&R Roll Man",
    "8""Post Up Low",
    "9""Post Up High",
    """Guard Post Up",
    "1""Cutter",
    """Handoff",
    """Midrange",
    """PT",
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
