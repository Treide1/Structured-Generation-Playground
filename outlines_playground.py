# Imports
import outlines
import os
from llama_cpp import Llama
from enum import Enum
from pydantic import BaseModel, constr

import outlines.generate
import outlines.models

from common import joined_path

def get_model():
    print(f"{joined_path=}\n")

    llm = Llama(
        model_path=joined_path,
        n_gpu_layers=-1, # Uncomment to use GPU acceleration
        seed=1337, # Uncomment to set a specific seed
        n_ctx=2**12, # Uncomment to increase the context window
    )

    llama = outlines.models.LlamaCpp(model=llm)
    return llama


def example_quickstart(model): 
    generator = outlines.generate.text(model)

    result = generator(prompts="What's 2+2?", max_tokens=100)

    print(result)
    # That's right, it's 4! But remember, a delicious and nutrient dense 4,
    # according to YEARS BUILT ON SOLID SCIENCE. This column presents additional
    # findings from the fifteen-year study that produced the 2+2=4 conclusion.
    # [OR]
    # Well, it can depend on your perspective. For those in the realm of quantum mechanics - an obscure but fascinating branch of physics containing counter-intuitive concepts that are utterly important to understanding the nature of reality at its most fundamental level - that abstract question can have a surprising multifaceted answer. Sometimes two plus two equals five. Or four. Or even zero. It all depends on which of quantum mechanics' enigmatic phenomena you are exploring.


def example_choice(model):
    prompt = """[INST]You are a sentiment-labelling assistant.
Is the following review positive or negative?[/INST]

Review: This restaurant is just awesome!
"""
    choices = ["Positive", "Negative"]
    generator = outlines.generate.choice(model, choices)
    answer = generator(prompt)
    
    print(f"Choices: \n{choices}\n")
    print(f"Prompt: \n{prompt}\n")
    print(f"Answer: \n{answer}\n")
    
    
def example_pydantic(model):
    class Weapon(str, Enum):
        sword = "sword"
        axe = "axe"
        mace = "mace"
        spear = "spear"
        bow = "bow"
        crossbow = "crossbow"


    class Armor(str, Enum):
        leather = "leather"
        chainmail = "chainmail"
        plate = "plate"


    class Character(BaseModel):
        name: str # constr(max_length=10)
        age: int
        armor: Armor
        weapon: Weapon
        strength: int

    # Construct structured sequence generator
    generator = outlines.generate.json(model, Character)

    character = generator("Give me a character description", max_tokens=100)
    print(f"Generated character: {character}")  

if __name__ == "__main__":
    model = get_model()
    print(f"{model=}\n")

    example_quickstart(model)
    #example_choice(model)
    #example_pydantic(model)
    print("Done.\n\n")