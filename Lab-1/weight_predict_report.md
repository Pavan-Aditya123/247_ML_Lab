# Linear Regression Lab Report

## Objective
To predict the body weight of a person using linear regression based on:
- Height
- Age
- Gender

## Dataset
| Weight | Height | Age | Gender |
|--------|--------|-----|--------|
| 79     | 1.80   | 35  | Male   |
| 69     | 1.68   | 39  | Male   |
| 73     | 1.82   | 25  | Male   |
| 95     | 1.70   | 60  | Male   |
| 82     | 1.87   | 27  | Male   |
| 55     | 1.55   | 18  | Female |
| 69     | 1.50   | 89  | Female |
| 71     | 1.78   | 42  | Female |
| 64     | 1.67   | 16  | Female |
| 69     | 1.64   | 52  | Female |

## Preprocessing
- Gender was encoded as: Male = 1, Female = 0.

## Model
Used `LinearRegression` from `sklearn.linear_model`.

### Features: Height, Age, Gender  
### Target: Weight

## Results
- Intercept: `-24.41`
- Coefficients:
  - Height: `47.38`
  - Age: `0.30`
  - Gender: `8.92`

### Sample Prediction
For a person with height = 1.75 m, age = 30, gender = Male:
- **Predicted weight = 76.33 kg**

## Conclusion
The regression model was successfully trained and used to predict body weight. Height and gender had a stronger impact than age in this dataset. This simple model can be extended for larger datasets and used for health-related predictions.

