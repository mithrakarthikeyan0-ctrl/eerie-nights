

SCENARIOS = {
    # --- LEVEL 1: THE AWAKENING ---
    '1': {
        'text': "OBSERVATION LOG 234: Subject awake. The room is cold. The smell of copper and formaldehyde is suffocating. You are naked on a steel slab. A single bulb buzzes above like a dying fly. In the corner, shadows detach themselves from the wall.",
        'choices': [
            {'text': "Grab the rusted scalpel.", 'next_id': 'lvl1_ins', 'effect': {'item': 'rusty_scalpel', 'sanity': -5}},
            {'text': "Remain motionless.", 'next_id': 'lvl1_lis', 'effect': {'sanity': -15}}
        ],
        'image': '/assets/dark_corridor.jpg' 
    },
    'lvl1_ins': {
        'text': "The tiles are cracked and weeping black fluid. A heavy iron door stands ajar. To your left, a drain gurgles with something thick and viscous. You hear wet footsteps approaching.",
        'choices': [
            {'text': "Sprint for the door.", 'next_id': 'lvl2_hall', 'effect': {'health': -5}, 'leads_to_level_up': True},
            {'text': "Hide in the drain.", 'next_id': 'lvl2_sewer', 'effect': {'sanity': -10}, 'leads_to_level_up': True}
        ],
        'image': '/assets/bloody_hallway.jpg'
    },
    'lvl1_lis': {
        'text': "The shadows have eyes. They whisper your name in a voice that sounds like tearing paper. Cold fingers brush your ankle. The light bulb explodes.",
        'choices': [
            {'text': "Kick and scream.", 'next_id': 'lvl2_hall', 'effect': {'health': -15}, 'leads_to_level_up': True},
            {'text': "Beg for mercy.", 'next_id': 'death_1', 'effect': {'sanity': -100}}
        ],
        'image': 'https://picsum.photos/seed/shadow/800/600?grayscale&blur=4'
    },

    # --- LEVEL 2: THE FACILITY ---
    'lvl2_hall': {
        'text': "A hallway of glass cells. Inside, human forms are fused with machinery, tubes replacing veins. They twitch in unison. At the end, a tall figure with scalpels for fingers turns towards you.",
        'choices': [
            {'text': "Fight the Surgeon.", 'next_id': 'lvl3_combat', 'effect': {'health': -40}},
            {'text': "Dive into an empty cell.", 'next_id': 'lvl3_hide', 'effect': {'sanity': -10}}
        ],
        'image': '/assets/bloody_hallway.jpg'
    },
    'lvl2_sewer': {
        'text': "You slide into a river of blood and offal. The smell makes you retch. Something massive moves under the surface, sending ripples of filth towards you.",
        'choices': [
            {'text': "Climb the rusted ladder.", 'next_id': 'lvl3_surface', 'effect': {'health': -10}},
            {'text': "Hold your breath and submerge.", 'next_id': 'lvl3_submerge', 'effect': {'sanity': -25, 'health': -5}}
        ],
        'image': 'https://picsum.photos/seed/sewer/800/600?grayscale&blur=3'
    },

    # --- LEVEL 3: ESCAPE ---
    'lvl3_combat': {
        'text': "You tear the Surgeon's mask off. It has no face, only a mirror reflecting your own terror. You stab it with its own finger-blade. It dissolves into black sludge.",
        'choices': [
            {'text': "Run for the Exit Sign.", 'next_id': 'lvl4_city', 'effect': {'health': -10}, 'leads_to_level_up': True}
        ],
        'image': '/assets/dark_corridor.jpg'
    },
    'lvl3_hide': {
        'text': "You hide under a cot stained with old fluids. The Surgeon passes, its footsteps sounding like knives on tile. You find a loose ventilation grate.",
        'choices': [
            {'text': "Crawl through the vent.", 'next_id': 'lvl4_city', 'effect': {'sanity': +5}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/grate/800/600?grayscale&blur=2'
    },
    'lvl3_surface': {
        'text': "You emerge from the manhole. The air burns your lungs. The sky is a bruised purple, the sun a weeping sore. You have escaped the facility, but not the nightmare.",
        'choices': [
            {'text': "Look at the city.", 'next_id': 'lvl4_city', 'effect': {'sanity': -5}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/ruinedcity/800/600?grayscale&blur=2'
    },
     'lvl3_submerge': {
        'text': "The thing passes over you, its underbelly soft and warm. You surface gasping for air. The current carries you to an outflow pipe.",
        'choices': [
            {'text': "Wash up on the banks.", 'next_id': 'lvl4_city', 'effect': {'sanity': -15}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/drown/800/600?grayscale&blur=3'
    },

    # --- LEVEL 4: THE RUINED CITY ---
    'lvl4_city': {
        'text': "The city is a architecture of bone and concrete. Buildings twist like melted wax. Packs of dogs with human faces roam the streets, howling in familiar voices.",
        'choices': [
            {'text': "Scavenge the pharmacy for meds.", 'next_id': 'lvl5_pharmacy', 'effect': {'item': 'pills', 'sanity': +20}},
            {'text': "Head to the burning Cathedral.", 'next_id': 'lvl5_cath', 'effect': {'sanity': -10}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/apocalypse/800/600?grayscale&blur=2'
    },

    # --- LEVEL 5: THE CULT ---
    'lvl5_pharmacy': {
        'text': "The pills numb the shaking. Through the window, you see a procession of robed figures dragging screaming victims towards the Cathedral. One of them stops and points at you.",
        'choices': [
            {'text': "Join the procession.", 'next_id': 'lvl6_ritual', 'effect': {'sanity': -20}},
            {'text': "Ambush the straggler.", 'next_id': 'lvl6_fight', 'effect': {'health': -10, 'item': 'ceremonial_dagger'}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/cult/800/600?grayscale&blur=1'
    },
    'lvl5_cath': {
        'text': "The Cathedral breathes. Its doors are giant ribs that open and close. Inside, a sermon is being preached in a language that makes your teeth ache.",
        'choices': [
            {'text': "Listen to the sermon.", 'next_id': 'lvl6_ritual', 'effect': {'sanity': -30, 'knowledge': +1}},
            {'text': "Sneak into the crypts.", 'next_id': 'lvl6_crypt', 'effect': {'sanity': -5}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/cathedral/800/600?grayscale&blur=2'
    },
    'lvl6_fight': {
         'text': "You slit the cultist's throat. He thanks you as he dies. You take his robes and his dagger. The crypt entrance is nearby.",
         'choices': [
             {'text': "Enter the crypts.", 'next_id': 'lvl6_crypt', 'effect': {'sanity': -5}, 'leads_to_level_up': True}
         ],
         'image': 'https://picsum.photos/seed/knife/800/600?grayscale&blur=2'
    },

    # --- LEVEL 6: THE SACRIFICE ---
    'lvl6_ritual': {
        'text': "They are throwing survivors into a pit of writhing flesh. 'FEED THE HIVE,' they chant. You are next in line. The pit calls to you.",
        'choices': [
            {'text': "Push the priest in.", 'next_id': 'lvl7_hive', 'effect': {'sanity': -15}, 'leads_to_level_up': True},
            {'text': "Jump willingly.", 'next_id': 'death_2', 'effect': {'health': -100}}
        ],
        'image': 'https://picsum.photos/seed/pit/800/600?grayscale&blur=2'
    },
    'lvl6_crypt': {
        'text': "The crypt walls turn from stone to meat. Veins pulse under the surface. You have found the root of the corruption. It is warm to the touch.",
        'choices': [
            {'text': "Cut through the membrane.", 'next_id': 'lvl7_hive', 'effect': {'health': -5, 'sanity': -10}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/flesh/800/600?grayscale&blur=3'
    },

    # --- LEVEL 7: THE HIVE ---
    'lvl7_hive': {
        'text': "You are inside the organism. The heat is stifling. The walls are made of faces—thousands of them, moaning softly. You see a copy of yourself merged into the wall.",
        'choices': [
            {'text': "Kill your copy.", 'next_id': 'lvl8_copy', 'effect': {'sanity': -25}, 'leads_to_level_up': True},
            {'text': "Ignore it and walk on.", 'next_id': 'lvl8_heart', 'effect': {'sanity': -10}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/faces/800/600?grayscale&blur=3'
    },

    # --- LEVEL 8: DOPPELGANGER ---
    'lvl8_copy': {
        'text': "Your double dies smiling. 'The Heart is hungry,' it whispers. The path splits: an artery leading up, and a vein leading down.",
        'choices': [
            {'text': "Follow the artery (Up).", 'next_id': 'lvl9_brain', 'effect': {'sanity': -10}},
            {'text': "Follow the vein (Down).", 'next_id': 'lvl9_heart', 'effect': {'health': -10}}
        ],
        'image': 'https://picsum.photos/seed/artery/800/600?grayscale&blur=2'
    },
    'lvl8_heart': {
        'text': "The beating is deafening. You enter a chamber where a massive heart hangs from chains of bone. It beats in time with yours, forcing your blood to pump painfully.",
        'choices': [
            {'text': "Stab the Heart.", 'next_id': 'ending_survive', 'effect': {'health': -60}, 'leads_to_level_up': True},
            {'text': "Touch the Heart.", 'next_id': 'lvl9_ascend', 'effect': {'sanity': -40}, 'leads_to_level_up': True}
        ],
        'image': 'https://picsum.photos/seed/heart/800/600?grayscale&blur=2'
    },

    # --- LEVEL 9: CLIMAX ---
    'lvl9_brain': {
        'text': "You reach the brain. A pulsating sack of gray matter that speaks in the voices of everyone you've ever loved. 'Join us. No more pain. Only Us.'",
        'choices': [
            {'text': "Burn it all down.", 'next_id': 'ending_survive', 'effect': {'health': -30}, 'leads_to_level_up': True},
            {'text': "Merge with the Hive.", 'next_id': 'death_3', 'effect': {'sanity': -100}}
        ],
        'image': 'https://picsum.photos/seed/brain/800/600?grayscale&blur=3'
    },
    'lvl9_ascend': {
        'text': "The heart stops. Yours continues. You feel a surge of infinite power and infinite sorrow. The Hive shudders and bows to its new master.",
        'choices': [
            {'text': "Accept Godhood.", 'next_id': 'ending_god', 'effect': {'sanity': +100}}
        ],
        'image': 'https://picsum.photos/seed/ascend/800/600?grayscale&blur=4'
    },

    # --- LEVEL 10: ENDINGS ---
    'ending_survive': {
        'text': "You wake up in a hospital bed. The doctors say you were trapped in a collapsed basement for three days. They say you're safe. But when you close your eyes, you can still hear the meat breathing.",
        'choices': [{'text': "Play Again?", 'next_id': '1'}],
        'image': 'https://picsum.photos/seed/hospitalroom/800/600?grayscale&blur=1'
    },
    'ending_god': {
        'text': "You are the Hive. You are the City. You see a thousand souls wandering your maze, terrified and delicious. You smile, and the world screams with you.",
        'choices': [{'text': "Reset the Nightmare.", 'next_id': '1'}],
        'image': 'https://picsum.photos/seed/god/800/600?grayscale&blur=4'
    },
    'death_1': {
        'text': "The darkness swallows you whole. Your screams are eaten before they leave your throat.",
        'choices': [{'text': "Restart.", 'next_id': '1'}],
        'effect': {'health': -100},
        'image': 'https://picsum.photos/seed/death/800/600?grayscale&blur=4'
    },
    'death_2': {
        'text': "You are thrown into the pit. You become part of the wall, another face moaning in the dark. Forever.",
        'choices': [{'text': "Restart.", 'next_id': '1'}],
        'effect': {'health': -100},
        'image': 'https://picsum.photos/seed/wall/800/600?grayscale&blur=4'
    },
    'death_3': {
        'text': "Your individuality dissolves like sugar in hot water. There is no you. Only Us.",
        'choices': [{'text': "Restart.", 'next_id': '1'}],
        'effect': {'health': -100},
        'image': 'https://picsum.photos/seed/void/800/600?grayscale&blur=4'
    }
}
