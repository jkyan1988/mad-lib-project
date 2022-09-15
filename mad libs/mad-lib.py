import json
import os

class MadLibs:
    def __init__(self, word_descriptions, template): 
        self.template = template
        self.word_descriptions = word_descriptions
        self.user_input = []
        self.story = []

    @classmethod
    def from_json(cls, name, path="/home/jkyan/mad-lib-project/mad libs/templates"):
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib


#User Input
    def get_words_from_user(self):
        print("Please provide the following words: ")
        for desc in self.word_descriptions:
            ui = input(desc + " ")
            self.user_input.append(ui)
        return self.user_input




    def build_story(self):
        self.story = self.template.format(*self.user_input)
        return self.story

temp_name = "day_at_the_zoo.json"
mad_lib = MadLibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()

print(story)