import random

# List of diseases
diseases = ["Healthy", "Leaf Blight", "Rust", "Mildew"]

# Simulate AI prediction
predicted_disease = random.choice(diseases)

print("Detected Disease:", predicted_disease)

# Advisory system
if predicted_disease == "Leaf Blight":
    print("Treatment: Copper fungicide")
    print("Prevention: Avoid water logging")

elif predicted_disease == "Rust":
    print("Treatment: Sulfur spray")
    print("Prevention: Crop rotation")

elif predicted_disease == "Mildew":
    print("Treatment: Neem oil")
    print("Prevention: Proper air circulation")

else:
    print("Crop is healthy. No action required.")