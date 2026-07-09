import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()


def get_secret(key):
    value = os.getenv(key)
    if value:
        return value
    return st.secrets[key]


API_KEY = get_secret("AVIATIONSTACK_API_KEY")


def search_flights(query):

    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }

    response = requests.get(url, params=params)

    data = response.json()

    flights = []

    if "data" in data:

        for flight in data["data"][:5]:

            airline = flight.get("airline", {}).get("name", "Unknown")
            departure = flight.get("departure", {}).get("airport", "Unknown")
            arrival = flight.get("arrival", {}).get("airport", "Unknown")
            status = flight.get("flight_status", "Unknown")

            flights.append(
                f"""
Airline: {airline}
Departure: {departure}
Arrival: {arrival}
Status: {status}
"""
            )

    return "\n".join(flights)
