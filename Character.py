import json

class Character:
    skill_to_attribute = {
            "Acrobatics": "Dexterity",
            "Animal Handling": "Wisdom",
            "Arcana": "Intelligence",
            "Athletics": "Strength",
            "Deception": "Charisma",
            "History": "Intelligence",
            "Insight": "Wisdom",
            "Investigation": "Intelligence",
            "Medicine": "Wisdom",
            "Nature": "Intelligence",
            "Perception": "Wisdom",
            "Performance": "Charisma",
            "Persuasion": "Charisma",
            "Religion": "Intelligence",
            "Sleight of Hand": "Dexterity",
            "Stealth": "Dexterity",
            "Survival": "Wisdom"
        }
    
    def __init__(self):
        self.name = None
        self.background = None
        self.alignment = None
        self.race = None
        self.character_class = None
        self.level = 1
        self.experience_points = 0
        self.health_points = 10
        self.armour_class = 8
        self.proficiency_bonus = 2

        try:
            with open("races.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.races = list(data.keys())
                self.races.remove("Racial Traits")
        except FileNotFoundError:
            print("Error: 'races.json' file not found.")

        try:
            with open("classes.json", "r", encoding="utf-8") as file:
                data = json.load(file)
                self.classes = list(data.keys())
        except FileNotFoundError:
            print("Error: 'classes.json' file not found.")

        self.attributes = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
        }

        self.attribute_modifiers = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }

        self.saving_throws = {
            "Strength": 0,
            "Dexterity": 0,
            "Constitution": 0,
            "Intelligence": 0,
            "Wisdom": 0,
            "Charisma": 0
        }

        self.skills = {
            "Acrobatics": 0,
            "Animal Handling": 0,
            "Arcana": 0,
            "Athletics": 0,
            "Deception": 0,
            "History": 0,
            "Insight": 0,
            "Investigation": 0,
            "Medicine": 0,
            "Nature": 0,
            "Perception": 0,
            "Performance": 0,
            "Persuasion": 0,
            "Religion": 0,
            "Sleight of Hand": 0,
            "Stealth": 0,
            "Survival": 0
        }

        self.equiptment = []

        self.equipped = []

        self.proficient_saving_throws = set()

        self.proficient_skills = set()

    def update_attribute(self, attribute, value):
        if attribute in self.attributes:
            self.attributes[attribute] = value
            self.update_attribute_modifiers()
        else:
            print("Attribute not found")

    def update_attribute_modifiers(self):
        for attribute, value in self.attributes.items():
            self.attribute_modifiers[attribute] = (value - 10) // 2

    def add_proficient_saving_throw(self, attribute):
        if attribute in self.saving_throws:
            self.proficient_saving_throws.add(attribute)
            self.update_saving_throws()
        else:
            print(f"Attribute '{attribute}' not found.")
    
    def add_proficiency(self, skill):
        if skill in self.skills:
            self.proficient_skills.add(skill)
            self.update_skills_based_on_attributes()
        else:
            print(f"Skill '{skill}' not found.")

    def add_equipment(self):
        pass

    def remove_equipment(self):
        pass

    def equip_equipment(self):
        pass

    def unequip_equipment(self):     
        pass

    def update_proficiency_bonus(self): 
        self.proficiency_bonus = 2 + (self.level - 1) // 4

    def update_saving_throws(self):
        for attribute, value in self.attributes.items():
            self.saving_throws[attribute] = (value - 10) // 2
            if attribute in self.proficient_saving_throws:
                self.saving_throws[attribute] += self.proficiency_bonus

    def update_skills_based_on_attributes(self):
        for skill, attribute in self.skill_to_attribute.items():
            self.skills[skill] = self.attribute_modifiers[attribute]
            if skill in self.proficient_skills:
                self.skills[skill] += self.proficiency_bonus

    def update_all(self):
        self.update_attribute_modifiers()
        self.update_proficiency_bonus()
        self.update_saving_throws()
        self.update_skills_based_on_attributes()

    def save_character(self):
        pass

    def load_character(self):
        pass

    def create_character(self):
        #TODO: Finish
        self.name = input("Enter character name: ")
        self.background = input("Enter character background: ")

        alignments = [
            "Lawful Good", "Neutral Good", "Chaotic Good", 
            "Lawful Neutral", "True Neutral", "Chaotic Neutral",
            "Lawful Evil", "Neutral Evil", "Chaotic Evil"]

        print("Select an alignment:")
        for i, alignment in enumerate(alignments, 1):
            print(f"{i}. {alignment}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to the alignment: "))
                if 1 <= choice <= len(alignments):
                    self.alignment = alignments[choice - 1]
                    break
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        print("Select a race:")

        for i, race in enumerate(self.races, 1):
            print(f"{i}. {race}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to the race: "))
                if 1 <= choice <= len(self.races):
                    self.race = self.races[choice - 1]
                    break
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        print("Select a class:")
        
        for i, character_class in enumerate(self.classes, 1):
            print(f"{i}. {character_class}")

        while True:
            try:
                choice = int(input("Enter the number corresponding to the class: "))
                if 1 <= choice <= len(self.classes):
                    self.character_class = self.classes[choice - 1]
                    break
                else:
                    print("Invalid choice. Please select a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def update_character(self):
        pass

    def modify_health(self):
        pass

    def short_rest(self):
        pass

    def long_rest(self):
        pass

    def print_character_sheet(self):
        #TODO: Finish
        print(f"{'='*30}")
        print(f"Character Name: {self.name}")
        print(f"Class: {self.character_class}")
        print(f"Race: {self.race}")
        print(f"Background: {self.background}")
        print(f"Level: {self.level}  |  Alignment: {self.alignment}")
        print(f"{'='*30}\n")

        print(f"{'Ability Scores':^30}")
        for ability, score in self.attributes.items():
            mod = self.attribute_modifiers[ability]
            print(f"{ability}: {score} (Modifier: {mod:+})")
        print(f"{'-'*30}\n")

    #def level_up(self):
    #def modify_experience_points(self):