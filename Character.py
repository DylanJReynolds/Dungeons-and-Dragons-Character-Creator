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
    
    def __init__(self, name, race, character_class, level=1, experience_points=0, health_points=10, armour_class=8):
        self.name = name
        self.race = race
        self.character_class = character_class
        self.level = level
        self.experience_points = experience_points
        self.health_points = health_points
        self.armour_class = armour_class
        self.proficiency_bonus = 2


        self.attributes = {
            "Strength": 10,
            "Dexterity": 10,
            "Constitution": 10,
            "Intelligence": 10,
            "Wisdom": 10,
            "Charisma": 10
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

        self.proficient_saving_throws = set()

        self.proficient_skills = set()

    def update_attribute(self, attribute, value):
        if attribute in self.attributes:
            self.attributes[attribute] = value
        else:
            print("Attribute not found")

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

    def update_proficiency_bonus(self): 
        self.proficiency_bonus = 2 + (self.level - 1) // 4

    def update_saving_throws(self):
        for attribute, value in self.attributes.items():
            self.saving_throws[attribute] = (value - 10) // 2
            if attribute in self.proficient_saving_throws:
                self.saving_throws[attribute] += self.proficiency_bonus

    def update_skills_based_on_attributes(self):
        for skill, attribute in self.skill_to_attribute.items():
            self.skills[skill] = (self.attributes[attribute] - 10) // 2
            if skill in self.proficient_skills:
                self.skills[skill] += self.proficiency_bonus

    def update_all(self):
        self.update_proficiency_bonus()
        self.update_saving_throws()
        self.update_skills_based_on_attributes()

    #def level_up(self):
    #def short_rest(self):
    #def long_rest(self):
    #def create_character(self):
    #def update_character(self):
    #def print_character(self):
    #def add_equipment(self):
    #def remove_equipment(self):
    #def equip_equipment(self):
    #def unequip_equipment(self):
    #def heal(self):
    #def take_damage(self):
    


    
        


