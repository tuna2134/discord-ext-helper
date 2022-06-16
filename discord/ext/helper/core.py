from discord.ext import commands
from yaml import load


class HelperCore:
    def __init__(self, path: str):
        self.path = path
        
    def loads(self, category: Category):
        with open(f"{self.path}/{category.name}.yml", "r") as f:
            data = load(f)
        category.description = {}
        category.commands = []
        for description_lang in data["description"]:
            category.description[description_lang] = data["description"][description_lang]
        for command_lang in data["commands"]:
            category.commands.append({command_lang: data["commands"]})
