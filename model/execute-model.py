"""
Program executes the stored Random Forest model and returns a prediction.

Accepted arguments from the command line are as follows:

age (int)
height (int)
weight (float)
gender (binary)
systolic blood pressure (int)
diastolic blood pressure (int)
cholesterol (int)
glucose (int)
smoking (binary)
alcohol intake (binary)
physical activity (binary)

@author: Alexander
"""

import sklearn

# We need pickle to deserialize the model
import pickle

# We need sys to read command line arguments
import sys

# CONSTANTS
MODEL_FILE = 'model/random-forest-heart-disease-model.sav' # because we call from outside the 'model' directory
FILE_NAME_INDEX = 0
FALSE_INDEX = 0
TRUE_INDEX = 1

# Deserialize the model, read-binary mode
model = pickle.load(open(MODEL_FILE, 'rb'))

# sys.argv always starts with the file name... we don't want that
features = sys.argv[FILE_NAME_INDEX + 1:]

# Now let's feed it into the model and get the prediction probabilities
# Normally we have to reshape the array, but in this case we can just wrap it
prob = model.predict_proba([features])

# Print out to the terminal and flush it
print(prob[0][TRUE_INDEX])
sys.stdout.flush()
