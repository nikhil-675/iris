from flask import Blueprint, request, Response
import joblib
import orjson
from src.utils.config import Config

main_bp = Blueprint('main_bp', __name__)

# Load pipeline once (lazy loading optional)
pipeline = joblib.load(Config.MODEL_PATH)

def orjson_response(payload, status=200):
    return Response(
        response=orjson.dumps(payload),
        status=status,
        mimetype='application/json'
    )

@main_bp.route('/health', methods=['GET'])
def health_check():
    return orjson_response({"status": "API is live!"})

@main_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    if not data or 'features' not in data:
        return orjson_response({"error": "Invalid input. Expecting 'features'."}, status=400)

    features = data['features']  # Example: [[5.1, 3.5, 1.4, 0.2]]

    try:
        prediction = pipeline.predict(features).tolist()
        return orjson_response({"prediction": prediction})
    except Exception as e:
        return orjson_response({"error": str(e)}, status=500)
