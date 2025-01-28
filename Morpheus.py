"""
Author: Drew Bogdan

Testing suite for the code, built to test functions while not in trading day due to exclusion purposes. will download
    historical day data of different stocks to let it run analysis on.
"""
import json

import Log as l
from Poseidon import Poseidon
from Athena import Athena
from Hephaestus import Hephaestus

class Morpheus:

    LOG = None
    ATHENA = None
    POSEIDON = None
    HEPHAESTUS = None

    def __init__(self):
        self.LOG = l.Log("[MORPHEUS]", "morph")
        self.LOG.print("Initiating Morpheus...")
        self.ATHENA = Athena()
        self.HEPHAESTUS = Hephaestus(self.ATHENA)
        self.POSEIDON = Poseidon(self.ATHENA, self.HEPHAESTUS)

    def run_tests(self, symb):
        self.LOG.print("Running Tests...")
        #data = self.parse_data(symb)
        self.test_peaks(symb)
        self.test_valleys(symb)

    def parse_data(self, symb):
        f = open(f"{symb}.json")
        data = json.load(f)
        return data[symb]

    def test_peaks(self, symb):
        self.LOG.print("================= PEAKS TEST =================")
        self.LOG.print(f"Gathering Historical Data for {symb} on January 27th 2025...")
        hist = self.ATHENA.get_day_test(symb)
        self.LOG.print("Data Gathered. Testing for Peaks...")
        peaks = self.POSEIDON.identify_peaks(hist)
        self.LOG.print(f"Poseidon gathered a total of {len(peaks)} peaks from historical data chart")
    def test_valleys(self, symb):
        self.LOG.print("================= VALLEYS TEST =================")
        self.LOG.print(f"Gathering Historical Data for {symb} on January 27th 2025...")
        hist = self.ATHENA.get_day_test(symb)
        self.LOG.print("Data Gathered. Testing for Valleys...")
        peaks = self.POSEIDON.identify_valleys(hist)
        self.LOG.print(f"Poseidon gathered a total of {len(peaks)} valleys from historical data chart")