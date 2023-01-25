"""
Shanti Kandel
Data Analytics Fundamentals
January 22, 2023
Doamin: Shoes 
The goal is to duplicate the PyBuddy class and extend PyBuddy to answer couple of questions 
about my domain. Here, I want to practice different skills on object 
oriented programming, creating custom classes, and writing custom functions.
"""
#import helpful modules to make our job easier

import datetime
from enum import Enum


class Species(Enum):
    DOG = 1
    CAT = 2
    ELF = 3
    ORC = 4

# Add the @dataclass decorator to let Python do more of the work
# Notice what changes.


@dataclass
class PyBuddy:
    """PyBuddy data class for creating a study buddy."""

    # With a data class, we just name each field and provide the type.
    # Include a default value in case something is not provied.
    name: str = "Unknown"
    species: Species = 1
    num_legs: int = 4
    weight_kgs: float = 9.999999999
    is_available: bool = True
    skill_list: list = field(default_factory=list)
    create_date = datetime.datetime.now()

    def get_age_string(self):
        """Return a string with our age."""
        return str(datetime.datetime.now() - self.create_date)

    def get_availability_string(self):
        """Return a message based on availability."""
        if self.is_available:
            return "I'm available for tutoring."
        else:
            return "I'm already helping others learn Python."

    def get_skills_string(self):
        """Return a nicely formatted string of skills."""
        # use concise list comprehension syntax
        return "".join([str(f"  - {elem}\n") for elem in self.skill_list])

    def display_welcome(self):
        """Display a welcome message from this instance."""

        print(
            f"""
Welcome, I'm a new PyBuddy.
{self.to_string()}
You'll need curiousity, the ability to search the web, 
and the tenacity and resourcefulness
to solve all kinds of challenges.
Let's get started! 

        """
        )

    def to_string(self):
        """Return a custom string describing this instance"""

        # Use an f-string (aka 'formatted string literal')
        # Use curly braces to switch into code that will be executed."
        # Wrap it all in parentheses so we can move the left side.
        return f"""
I'm {self.name}.
I'm a {self.species} with {self.num_legs} legs.
I weigh {self.weight_kgs:.2f} kgs.
I've been alive for {self.get_age_string()}.
I know:
{self.get_skills_string()}
"""
# PyBuddy Examples:
"""Creating new codes in PyBuddy using the statistics module"""
import statistics

shoe_sizes = [7, 7.5, 8, 8.5, 8, 10.5, 9, 8, 8, 9, 12, 14, 7, 7]

mean_size = statistics.mean(shoe_sizes)
print("The mean shoe size is:", mean_size)

median_size = statistics.median(shoe_sizes)
print("The median shoe size is:", median_size)

try:
    mode_size = statistics.mode(shoe_sizes)
    print("The mode shoe size is:", mode_size)
except statistics.StatisticsError:
    print("No unique mode found.")

stdev_size = statistics.stdev(shoe_sizes)
print("The standard deviation of shoe sizes is:", stdev_size)

# Practice 2
class ShoeSizeAnalyzer:
    def __init__(self, shoe_sizes):
        self.shoe_sizes = shoe_sizes

    def get_mean(self):
        return statistics.mean(self.shoe_sizes)

    def get_mode(self):
        try:
            return statistics.mode(self.shoe_sizes)
        except statistics.StatisticsError:
            return "No unique mode found."

    def double_weight(self):
        return [size*2 for size in self.shoe_sizes]

    def get_cube_root_of_weight(self):
        return [size**(1/3) for size in self.shoe_sizes]


# creating an instance of PyBuddy:
class PyBuddy:
    def __init__(self):
        self.greeting = "Hi, Good morning! Which shoe size do you need?"

    def execute(self, sentence):
        return self.greeting

bot = PyBuddy()
print(bot.execute(""))






