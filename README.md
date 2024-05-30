# JALA-submission
For model deployment of Gradient Boosting Regression:

API Usage

The API endpoint for predictions is /predict. Send a POST request with JSON data containing the features.

Example Request input:
```json
[
            {"id": 1, "FCR": 1.5, "days_difference": 10, "initial_age": 20, "limit_weight_per_area": 2.5,
             "target_size": 100, "total_seed_type": 2, "harvested_size": 90, "status": "partial",
             "morning_temperature": 28, "evening_temperature": 27, "morning_do": 5, "morning_salinity": 20,
             "morning_pH": 7.5, "transparency": 0.8, "started_at_year": 2021, "last_mortality_day": 50,
             "sampled_at_day": 120},
            {"id": 2, "FCR": 1.6, "days_difference": 12, "initial_age": 22, "limit_weight_per_area": 2.7,
             "target_size": 110, "total_seed_type": 2, "harvested_size": 95, "status": "partial",
             "morning_temperature": 27, "evening_temperature": 26, "morning_do": 4.8, "morning_salinity": 19,
             "morning_pH": 7.4, "transparency": 0.7, "started_at_year": 2021, "last_mortality_day": 55,
             "sampled_at_day": 130}
        ]
```

The Output Respons:
```json
[{"id":1,"abw_at_harvest":16.2,"adg":0.1642857143,"biomass":499218.0,"survival_rate":64.625,"revenue":10822248.0},{"id":2,"abw_at_harvest":16.2,"adg":0.1642857143,"biomass":499218.0,"survival_rate":64.625,"revenue":10822248.0}]

```

example request with curl in terminal
```bash
curl -X POST \
    -H "Content-Type: application/json" \
    -d '[
            {"id": 1, "FCR": 1.5, "days_difference": 10, "initial_age": 20, "limit_weight_per_area": 2.5,
             "target_size": 100, "total_seed_type": 2, "harvested_size": 90, "status": "partial",
             "morning_temperature": 28, "evening_temperature": 27, "morning_do": 5, "morning_salinity": 20,
             "morning_pH": 7.5, "transparency": 0.8, "started_at_year": 2021, "last_mortality_day": 50,
             "sampled_at_day": 120},
            {"id": 2, "FCR": 1.6, "days_difference": 12, "initial_age": 22, "limit_weight_per_area": 2.7,
             "target_size": 110, "total_seed_type": 2, "harvested_size": 95, "status": "partial",
             "morning_temperature": 27, "evening_temperature": 26, "morning_do": 4.8, "morning_salinity": 19,
             "morning_pH": 7.4, "transparency": 0.7, "started_at_year": 2021, "last_mortality_day": 55,
             "sampled_at_day": 130}
        ]' \
    http://localhost:5000/predict
```
