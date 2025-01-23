from tensorflow.keras.models import load_model

# Load the model
model = load_model('bio_nonbio4.h5')

# Check the model summary to confirm it loaded correctly
model.summary()

# Example usage: Make a prediction
# Assuming you have an input prepared as `input_data` in the correct shape
# prediction = model.predict(input_data)
