
import Log as l

class Poseidon:

    LOG = None

    """
    Poseidon Class
        This class should be built to take in timing candlestick charts to scan for different trend templates and should
            it find one it would notify Zeus to buy and then set a constant scan and when Zeus should sell it will send a 
            signal saying it is in optimal selling rage, Zeus will ultimately make the descision but Poseidon is set to
            give the advice to the main bot and let the risk/reward function built into Zeus handle it.
    """
    def __init__(self):
        self.LOG = l.Log("[POSEIDON]", "blue")
        self.LOG.print("Initiating Poseidon...")