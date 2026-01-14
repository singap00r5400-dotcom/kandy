from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

diseases = ["Healthy", "Leaf Blight", "Rust", "Mildew"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    treatment = None
    prevention = None

    if request.method == "POST":
        # Get uploaded file
        file = request.files.get("leaf_image")

        if file:
            prediction = np.random.choice(diseases)
            result = prediction

            if prediction == "Leaf Blight":
                treatment = "Use copper-based fungicide"
                prevention = "Avoid water logging"

            elif prediction == "Rust":
                treatment = "Apply sulfur spray"
                prevention = "Practice crop rotation"

            elif prediction == "Mildew":
                treatment = "Use neem oil (organic)"
                prevention = "Ensure proper air circulation"

            else:
                treatment = "No treatment needed"
                prevention = "Maintain good crop care"

    return render_template(
        "index.html",
        result=result,
        treatment=treatment,
        prevention=prevention
    )

if __name__ == "__main__":
    app.run(debug=True)