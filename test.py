import matplotlib.pyplot as plt
import numpy as np

import srwpy as srw

GeV = 1.
MeV = 1.e-3 

energy = 195*MeV  # MeV
lambda_u = 0.80   # meters
N_u = 6
B_0 = 0.130       # T


harm = srw.SRWLMagFldH()  # Create harmonic field structure
harm.n = 1                 # Harmonic number
harm