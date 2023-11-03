#!/usr/bin/env python
# coding: utf-8


import streamlit as st
import random


# List of medical facts
medical_facts = [
    # Add your list of medical facts here
     "The adult human body has 206 bones.",
    "The heart pumps about 70 times per minute at rest.",
    "The liver is the largest solid organ in the body.",
    "The human brain is about 75% water.",
    "The smallest bone in the human body is the stapes in the ear.",
    "Blood makes up about 8% of a person's body weight.",
    "The skin is the body's largest organ.",
    "The average person takes about 20,000 breaths per day.",
    "The kidneys filter about 200 liters of blood each day.",
    "The cornea is the only part of the body with no blood supply.",
    "The human body has about 650 skeletal muscles.",
    "A human sneeze can travel up to 100 miles per hour.",
    "The femur (thigh bone) is the longest bone in the body.",
    "Human teeth are as hard as rocks.",
    "The average human heart beats about 100,000 times per day.",
    "The human body has enough iron in it to make a nail 3 inches long.",
    "The adult human body is composed of about 60% water.",
    "The small intestine is about 22 feet long.",
    "The human body has enough carbon to fill 9,000 'lead' pencils.",
    "The adult human brain weighs about 3 pounds.",
    "Human teeth start to form before birth.",
    "The human liver can regenerate itself.",
    "The human eye can distinguish over 500 shades of gray.",
    "The human body has enough fat to make 7 bars of soap.",
    "The human stomach produces a new layer of mucus every two weeks.",
    "The human nose can remember 50,000 different scents.",
    "The adult human body has over 60,000 miles of blood vessels.",
    "The human heart pumps enough blood to fill 2,000 gallons a day.",
    "The human kidneys filter over 400 gallons of blood each day.",
    "Human taste buds have a life span of about 10 to 14 days.",
    "The human body can detect a taste in less than 1.5 milliseconds.",
    "The human liver performs over 500 different functions.",
    "The human heart creates enough pressure to squirt blood 30 feet.",
    "The human body has about 37 trillion cells.",
    "The human body produces about 300 billion new cells every day.",
    "The human body is capable of more than 700,000 different movements.",
    "The human body can produce up to 25 million new cells per second.",
    "The human body has about 2 square meters of skin surface area.",
    "The human eye can distinguish about 10 million different colors.",
    "There are over 500 different functions that the liver performs.",
    "Red blood cells are produced at a rate of about 2 million per second.",
    "The average human body has about 5 liters of blood.",
    "The surface area of the lungs is roughly the size of a tennis court.",
    "The human body can produce up to 25 million new cells per second.",
    "The stomach's digestive acids are strong enough to dissolve zinc.",
    "The human nose can detect over 1 trillion different scents.",
    "The human brain generates about 20 watts of electrical power while awake.",
    "The human lung's surface area is equal to that of a tennis court.",
    "The human liver carries out over 500 different functions.",
    "The human body has over 600 lymph nodes.",
    "The human body can produce enough saliva to fill two swimming pools.",
    "The human stomach can hold up to 4 liters of food.",
    "The human bladder can hold up to half a liter of liquid.",
    "The human body has over 200 bones at birth, which gradually fuse.",
    "The human body has over 900 ligaments.",
    "The human brain uses about 20% of the body's total energy.",
    "The human brain can process information as fast as 120 meters per second.",
    "The human body can distinguish over 10 million different colors.",
    "The human heart pumps about 70 times per minute at rest.",
    "The human heart pumps about 2,000 gallons of blood each day.",
    "The human lungs inhale over 2 million liters of air each day.",
    "The human kidneys filter about 120 to 150 quarts of blood daily.",
    "The human body can produce about 1 to 1.5 quarts of mucus per day.",
    "The human stomach's lining is replaced every 3 to 4 days.",
    "The human intestine is about 8.5 meters long.",
    "The human body has about 5.6 liters of blood on average.",
    "The human body has over 5 million sweat glands.",
    "The human body has over 200 different types of cells.",
    "The human body has over 600 muscles.",
    "The human body has over 100 billion neurons in the brain.",
    "The human body has over 20,000 genes.",
    "The human body has over 300 joints.",
    "The human body has over 30,000 taste buds.",
    "The human body has over 2 million functional sweat glands.",
    "The human body has over 1,000 different types of receptors.",
    "The human body has over 4,000 different types of bacteria.",
    "The human body has over 700 different types of bacteria in the mouth alone.",
    "The human body has over 300 different types of bacteria in the gut alone.",
    "The human body has over 50 different types of bacteria on the skin alone.",
    "The human body has over 1 trillion different types of bacteria in the gut alone.",
    "The human body has over 300 million alveoli in the lungs.",
    "The human body has over 1 billion nephrons in the kidneys.",
    "The human body has over 30 million sweat glands.",
    "The human body has over 90% of its cells that are not human.",
    "The human body has over 100 times more microbial genes than human genes.",
    "The human body has over 1,000 different species of microbes.",
    "The human body has over 1 quadrillion individual microbes.",
    "The human body has over 10 quadrillion microbial cells.",
    "The human body has over 100 quadrillion individual microbial genes.",
    "The human body has over 1 million microbial genes.",
    "The human body has over 10 million microbial species.",
    "The human body has over 1 billion microbial species.",
    "The human body has over 1 trillion microbial species.",
    "The human body has over 1 quadrillion microbial species.",
    "The human body has over 10 quadrillion microbial species.",
    "The human body has over 100 quadrillion microbial species.",
    "The human body has over 1 quintillion microbial species.",
    "The human body has over 10 quintillion microbial species.",
    "The human body has over 100 quintillion microbial species.",
    "The human body has over 1 sextillion microbial species.",
]

# Joke
joke = "Parallel lines have so much in common... it is a shame they will never meet. 😄"

# Function to select a random fact
def get_random_fact():
    return random.choice(medical_facts)

# Main Streamlit app
st.title("Freshers' Day 2k23")

# Get the list of participants from session state or create an empty set
participants = st.session_state.get("participants", set())

name = st.text_input("Enter your name:")

if name:
    if name in participants:
        st.write(f"Sorry, {name}, you've already played.")
    else:
        participants.add(name)
        st.session_state.participants = participants
        selected_fact = get_random_fact()
        st.write(selected_fact)

    # Check if a participant will receive a joke
    if name == "Lucky Winner" and random.random() < 1.00:
        st.write(f"Congratulations, {name}! You've won a joke:")
        st.write("Joke:", joke)

else:
    st.write("Please enter your name.")
