from src.data_preprocessing import load_data, clean_data
from src.feature_engineering import prepare_features
from src.model_training import train_model, save_model
from src.evaluation import evaluate_model


df = load_data()

df = clean_data(df)

df = prepare_features(df)

model, vectorizer, X_test, y_test = train_model(df)

accuracy = evaluate_model(
    model,
    X_test,
    y_test
)

save_model(
    model,
    vectorizer
)

print("\nModel training completed.")
print("Accuracy:", round(accuracy, 4))
print("Model saved successfully.")