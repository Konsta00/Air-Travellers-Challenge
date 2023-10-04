class Store:
    def __init__(self):
        self.items = {
            'power_ups': {
                'skip_question': ('Skip question', 100),
                'show_hint': ('Show hint', 50),
                'free_travel': ('Free travel', 50),
                'random_powerup': ('Random powerup', 150),
            },
            'plant_trees': {
                'plant_10_trees': ('Plant 10 trees', 30),
                'plant_20_trees': ('Plant 20 trees', 50),
                'plant_30_trees': ('Plant 30 trees', 65),
            }
        }
        self.player_inventory = {}

    def display_store_options(self):
        print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")
        print("Welcome to the store! Here are the available items:")
        for category, items in self.items.items():
            print(f"\n{'1. Power ups: ' if category == 'power_ups' else '2. Plant trees:'}")
            for item  in items.items():
                print(f"  {item[1][0]}: {item[1][1]}€")

    def purchase_item(self, player, category, input_number):
        if category in self.items:
            try:
                item_choice = input_number
                item = list(self.items[category].keys())[item_choice - 1]

                if category == 'power_ups':
                    print("Choose an item:")
                    for i, (item) in enumerate(self.items[category].items(), start=1):
                        print(f"{i}.{item[1][0]}: {item[1][1] }€")
                        self.process_purchase(category, item, player)
                elif category == 'plant_trees':
                    self.purchase_plant_trees(player)
                
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid selection.")
        else:
            print("-------------[Invalid category choice.]-------------")

    def purchase_power_up(self, player):
        # Implementation for purchasing power-ups
        pass

    def purchase_plant_trees(self, player):
        print("\n╔══════════════════════════╗\n  Air Travellers Challenge\n╚══════════════════════════╝\n")
        print("Choose a tree planting option:")
        for i, item in enumerate(self.items['plant_trees'].items(), start=1):
            print(f"{i}. {item[1][0]}: {item[1][1]}€")

        try:
            item_choice = int(input("\nEnter the number of your choice: "))
            item = list(self.items['plant_trees'].keys())[item_choice - 1]

            # Calculate CO2 reduction based on the chosen option
            if item == 'plant_10_trees':
                co2_reduction = 1.5
            elif item == 'plant_20_trees':
                co2_reduction = 3.5
            elif item == 'plant_30_trees':
                co2_reduction = 6.5
            else:
                print("Invalid item choice.")
                return

            # Deduct the price from the player's budget
            price = self.items['plant_trees'][item][1]
            if player.budget >= price:
                player.budget -= price

                # Apply CO2 reduction
                player.update_co2_emissions(co2_reduction)


                print(f"You've successfully purchased {item} for {price}€.")
            else:
                print("Insufficient funds. Cannot purchase the item.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid selection.")

    def process_purchase(self, category, item, player):
        p = self.items[category]

        if category == 'power_ups':
            # p = self.items[category]
            pass
            # player.budget -= p[item]
            # print(p[item][0])
            # player.powerups += (item,)


        


