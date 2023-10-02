class Store:
    def __init__(self):
        self.items = {
            'power_ups': {
                'skip_question': 100,
                'show_hint': 50,
                'free_travel': 100,
                'random_powerup': 150
            },
            'plant_trees': {
                'plant_10_trees': 30,
                'plant_20_trees': 50,
                'plant_30_trees': 65
            }
        }
        self.player_inventory = {}

    def display_store_options(self):
        print("Welcome to the store! Here are the available items:")
        for category, items in self.items.items():
            print(f"\n{category.upper()}:")
            for item, price in items.items():
                print(f"  {item.capitalize()}: {price}€")

    def purchase_item(self, player, category):
        if category in self.items:
            self.display_store_options()

            print("Choose an item:")
            for i, (item, price) in enumerate(self.items[category].items(), start=1):
                print(f"{i}. {item.capitalize()}: {price}€")

            try:
                item_choice = int(input("Enter the number of your choice: "))
                item = list(self.items[category].keys())[item_choice - 1]

                self.process_purchase(category, item, player)
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid selection.")
        else:
            print("Invalid category choice.")

    def purchase_power_up(self, player):
        # Implementation for purchasing power-ups
        pass

    def purchase_plant_trees(self, player):
        print("Choose a tree planting option:")
        for i, (item, price) in enumerate(self.items['plant_trees'].items(), start=1):
            print(f"{i}. {item.capitalize()}: {price}€")

        try:
            item_choice = int(input("Enter the number of your choice: "))
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
            price = self.items['plant_trees'][item]
            if player.budget >= price:
                player.budget -= price

                # Apply CO2 reduction
                player.reduce_co2_emission(co2_reduction)


                print(f"You've successfully purchased {item} for {price}€.")
            else:
                print("Insufficient funds. Cannot purchase the item.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a valid selection.")
