# JALA-submission
For model deployment of Gradient Boosting Regression:

API Usage

The API endpoint for predictions is /predict. Send a POST request with JSON data containing the features.

Example Request:
```json
{
    "total_feed": 1000,
    "total_harvest_weight": 500,
    "initial_age": 20,
    "fasting_avg": 1.2,
    "harvest_population": 300,
    "pond_length": 50,
    "total_seed_type": 2,
    "volume_ponds": 1000,
    "pond_depth": 1.5,
    "total_live_shrimp": 250,
    "total_seed": 500,
    "pond_width": 20,
    "death_abw": 0.5,
    "target_cultivation_day": 120,
    "FCR": 1.5,
    "area": 1000,
    "death_quantity": 50
}
```

The Output Respons:
```json
{
    "abw_samples": 30,
    "adg": 0.5,
    "biomassa": 2000,
    "survival_rate": 95,
    "revenue_idr": 1500000
}

```
