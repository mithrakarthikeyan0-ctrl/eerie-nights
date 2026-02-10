from scenarios import SCENARIOS

class GameState:
    def __init__(self):
        self.sanity = 100
        self.health = 100
        self.level = 1
        self.current_scenario_id = '1'
        self.inventory = []
        self.is_game_over = False

    def get_stats(self):
        return {
            'sanity': self.sanity,
            'health': self.health,
            'level': self.level,
            'inventory': self.inventory,
            'game_over': self.is_game_over
        }

    def process_choice(self, choice_index):
        if self.is_game_over:
            return {'message': 'Game Over. Refresh to restart.', 'game_over': True}

        current_scenario = SCENARIOS.get(self.current_scenario_id)
        if not current_scenario:
            return {'error': 'Scenario not found'}

        try:
            choice = current_scenario['choices'][choice_index]
        except IndexError:
            return {'error': 'Invalid choice'}

        # Apply effects
        if 'effect' in choice:
            self.apply_effect(choice['effect'])

        # Check for death/insanity
        if self.health <= 0:
            self.is_game_over = True
            return {'message': "You have succumbed to your injuries. The darkness consumes you.", 'game_over': True}
        if self.sanity <= 0:
            self.is_game_over = True
            return {'message': "Your mind shatters. You are now one with the madness.", 'game_over': True}

        # Progress to next scenario
        next_id = choice.get('next_id')
        
        # Level up logic if staying in same 'stage' or successful survival
        if choice.get('leads_to_level_up'):
            self.level += 1
        
        if next_id:
            self.current_scenario_id = next_id
            next_scenario = SCENARIOS.get(next_id)
            return {
                'message': next_scenario['text'],
                'choices': next_scenario.get('choices', []),
                'stats': self.get_stats(),
                'image': next_scenario.get('image', 'default_horror.jpg'),
                'sound': next_scenario.get('sound', 'heartbeat.mp3')
            }
        else:
            # End of content or victory
            self.is_game_over = True
            return {'message': "You survived... for now.", 'game_over': True}

    def apply_effect(self, effect):
        if 'sanity' in effect:
            self.sanity += effect['sanity']
        if 'health' in effect:
            self.health += effect['health']
        if 'item' in effect:
            self.inventory.append(effect['item'])
