# 🌿 Air Quality Plant Recommendation Model

This project uses a machine learning model to recommend suitable indoor plants based on specific air pollutant levels. It's designed to help users choose plants that can best help filter the air in their environment, given a set of air quality measurements.

The model is a `RandomForestClassifier` trained on historical air quality data to predict one or more appropriate plants for a given set of pollutant values.

## ⚙️ How It Works

The model is built as a **multi-label classification** system. This is because a single set of air quality readings can be associated with *multiple* recommended plants (e.g., both "Areca Palm" and "Peace Lily").

The pipeline is as follows:
1.  **Load Data:** The model is trained on the `updated_aqi_dataset_with_plants_filled.csv` dataset.
2.  **Feature Selection:** The model uses the following 6 pollutants as features:
    * `PM2.5`
    * `PM10`
    * `NO`
    * `NO2`
    * `O3`
    * `SO2`
3.  **Label Encoding:** The `Recommended_Plants` column (which contains text like "Areca Palm, Spider Plant") is encoded using `MultiLabelBinarizer`. This converts each plant name into a separate binary column, allowing the model to predict multiple plants at once.
4.  **Model Training:** A `RandomForestClassifier` is trained on the feature data (X) and the binarized labels (y).
5.  **Serialization:** The trained model (`model.pkl`) and the label binarizer (`mlb.pkl`) are saved using `pickle` so they can be easily loaded for future predictions.

## 📂 Files in This Repository

* **`model1.ipynb`**: The Jupyter Notebook containing all the code for data preprocessing, model training, and evaluation.
* **`model.pkl`**: The serialized, pre-trained `RandomForestClassifier` object.
* **`mlb.pkl`**: The serialized `MultiLabelBinarizer` object. This is **essential** for converting the model's numeric output back into human-readable plant names.
* **`updated_aqi_dataset_with_plants_filled.csv`**: The dataset used to train the model.

## 🚀 Getting Started: How to Use the Model

To use the pre-trained model for your own predictions, you'll need to have Python and the `scikit-learn` and `pandas` libraries installed.

```bash
pip install scikit-learn pandas
