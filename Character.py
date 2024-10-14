class Character:
    def __init__(self, name, race, character_class, level=1, experience_points=0, health_points=10, armour_class=10):
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

    def update_attribute(self, attribute, value):
        if attribute in self.attributes:
            self.attributes[attribute] = value
        else:
            print("Attribute not found")

    def update_skills_based_on_attributes(self):
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

        for skill, attribute in skill_to_attribute.items():
            self.skills[skill] = (self.attributes[attribute] - 10) // 2
            if skill in self.proficient_skills:
                self.skills[skill] += self.proficiency_bonus

        


