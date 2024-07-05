# Python Syntax: Medical Insurance Project

## Overview

This project is designed to help understand how various factors contribute to medical insurance costs using a simple formula. As a medical professional or data scientist, analyzing how different variables like age, sex, BMI, number of children, and smoking status affect insurance costs can provide valuable insights.

**Note:** While insurance companies may use BMI in their calculations, it is important to recognize that BMI is not necessarily an accurate predictor of health. As data scientists, we should approach quantitative measures like BMI critically, as they often oversimplify complex phenomena.

## Project Structure

The project involves setting up variables for each factor and then using a formula to estimate the insurance costs. We will also investigate how changes in these factors impact the cost predictions.

## Factors Considered

The following variables are used in the estimation formula:

- `age`: Age of the individual in years
- `sex`: 0 for female, 1 for male*
- `bmi`: Individual’s body mass index
- `num_of_children`: Number of children the individual has
- `smoker`: 0 for a non-smoker, 1 for a smoker

## Example

For instance, at the top of `script.py`, we create variables for a 28-year-old, non-smoking woman who has three children and a BMI of 26.2:

```python
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0
```

## Formula

The insurance cost is calculated using the following formula:

```makefile
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
```

This formula provides an estimate of the yearly insurance cost for an individual based on the given factors.

## Project Goals

The main goal of this project is to:

1. Set up the variables for each factor.
2. Calculate the insurance cost using the formula.
3. Explore how changes in individual factors impact the insurance cost estimation.

## Usage

To run the project, simply execute the `script.py` file. You can modify the variables to see how changes in each factor affect the insurance cost.

## Conclusion

This project provides a basic introduction to how various factors can influence medical insurance costs. It serves as a foundation for further exploration and more advanced analyses in the field of medical data science.

## Acknowledgments

This project was completed as part of a project on the Codecademy platform.
