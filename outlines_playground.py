# Imports
import os
import logging
from enum import Enum

import outlines.generate.regex
from monitoring import setup_logger, print_runtime, log_runtime

from llama_cpp import Llama
from pydantic import BaseModel

import outlines
import outlines.generate
import outlines.models

class ModelPaths(Enum):
    MISTRAL_7B_Q5_K_M = ".\mistral-7b-instruct-v0.2.Q5_K_M.gguf"
    MISTRAL_7B_Q8 = ".\mistral-7b-instruct-v0.2.Q8_0.gguf"

def get_model(model_path: str) -> outlines.models.LlamaCpp:
    logging.debug(f"Loading model from {model_path=}")

    llm = Llama(
        model_path=model_path,
        n_gpu_layers=-1, # Use GPU acceleration (-1: all layers)
        seed=1337, # Set a specific seed (-1: random)
        n_ctx=2**12, # Increase the context window. Reminder: 2**12 = 4096
    )

    llama = outlines.models.LlamaCpp(model=llm)
    return llama


@log_runtime
def example_quickstart(model):
    logging.info("Running quickstart example...")
    
    logging.debug(f"Setting up generator.")
    generator = outlines.generate.text(model)

    logging.info("Running inference.")
    prompt = "What's 2+2?"
    config = {"max_tokens": 100}
    logging.debug(f"Running Prompt: {prompt}. Config: {config}")
    result = generator(prompts="What's 2+2?", **config)
    logging.info(f"Result: {result}")
    # Usually results in lengthy, irrelevant output, called "Yapping".
    # Example:
    # That's right, it's 4! But remember, a delicious and nutrient dense 4,
    # according to YEARS BUILT ON SOLID SCIENCE. This column presents additional
    # findings from the fifteen-year study that produced the 2+2=4 conclusion.
    

@log_runtime
def example_regex(model):
    logging.info("Running regex example...")
    
    logging.info(f"Setting up generator.")
    # Regex: At least one digit, then a dot
    regex = r"\d+\."
    generator = outlines.generate.regex(model, regex)
    
    logging.info("Running inference.")
    prompt = "What's 2+2?"
    config = {"max_tokens": 100, "stop_at": ["."]}
    logging.debug(f"Prompt: {prompt}. Config: {config}")
    result = generator(prompts="What's 2+2?", **config)
    logging.info(f"Result: {result}")


@log_runtime
def example_choice(model):
    logging.info("Running choice example...")
    
    prompt = """You are a sentiment-labelling assistant.
Is the following review positive or negative?

Review: "This restaurant is just awesome!"
"""
    choices = ["Mostly Positive", "Neutral", "Mostly Negative"]
    logging.info(f"Running Prompt: {prompt}. Choices: {choices}")
    generator = outlines.generate.choice(model, choices)
    answer = generator(prompt)
    logging.info(f"Answer: {answer}")
    

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
    intelligence: int
    dexterity: int 


@log_runtime
def example_pydantic(model):
    logging.info("Running Pydantic example...")

    # Construct structured sequence generator
    logging.debug(f"Running generator with {Character=}")
    generator = outlines.generate.json(model, Character)

    logging.info("Setting up generator.")
    prompt = "Give me a character description."
    character = generator(prompt, max_tokens=1000)
    logging.debug(f"Prmopt: {prompt}.")
    logging.info(f"Generated character: {character}")
    typeof_character = type(character) # <class '__main__.example_pydantic.<locals>.Character'>
    character: Character
    logging.debug(f"Type of character: {typeof_character}")
    logging.debug(f"Character keys: {character.model_dump()}")


@print_runtime
@log_runtime
def main():
    # Setup logging
    setup_logger(filename="outlines_playground.log")
    
    # Get model
    model_path = ModelPaths.MISTRAL_7B_Q8.value
    model = get_model(model_path)
    logging.debug(f"Loaded model: {model=}\n")

    # Run examples
    example_quickstart(model)
    example_regex(model)
    example_choice(model)
    example_pydantic(model)
    
    # Done
    logging.info("Done.")


if __name__ == "__main__":
    main()