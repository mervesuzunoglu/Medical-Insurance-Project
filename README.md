# Python Syntax, Functions, and **Control Flow**: Medical Insurance Project

## Overview

This project is designed to help understand how various factors contribute to medical insurance costs using a simple formula. As a medical professional or data scientist, analyzing how different variables like age, sex, BMI, number of children, and smoking status affect insurance costs can provide valuable insights.

**Note:** While insurance companies may use BMI in their calculations, it is important to recognize that BMI is not necessarily an accurate predictor of health. As data scientists, we should approach quantitative measures like BMI critically, as they often oversimplify complex phenomena.

## Project Structure

The project involves setting up variables for each factor and then using a formula to estimate the insurance costs. We will also investigate how changes in these factors impact the cost predictions.

## Factors Considered

The following variables are used in the estimation formula:

- **age:** Age of the individual in years
- **sex:** 0 for female, 1 for male*
- **bmi:** Individual’s body mass index
- **num_of_children:** Number of children the individual has
- **smoker:** 0 for a non-smoker, 1 for a smoker

## Example

For instance, at the top of `script.py`, we create variables for a 28-year-old, non-smoking woman who has three children and a BMI of 26.2:

```python
pythonCopy code
age = 28
sex = 0
bmi = 26.2
num_of_children = 3
smoker = 0
```

## Formula

The insurance cost is calculated using the following formula:

```python
pythonCopy code
insurance_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
```

Additionally, here is a Python function to calculate the insurance cost:

```python
pythonCopy code
def calculate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):
    estimated_cost = 250 * age - 128 * sex + 370 * bmi + 425 * num_of_children + 24000 * smoker - 12500
    print("The estimated insurance cost for " + name + " is " + str(estimated_cost) + " dollars.")
    return estimated_cost
```

This function calculates the insurance cost for an individual based on the given factors and prints the result.

## Project Goals

The main goals of this project are to:

1. Set up the variables for each factor.
2. Calculate the insurance cost using the formula.
3. Explore how changes in individual factors impact the insurance cost estimation.
4. Apply your new knowledge of Python functions to write a useful function that calculates medical insurance costs.
5. Apply the knowledge of Python control flow to write code that gives people advice on how to lower their medical insurance costs.

## Additional Contribution

To provide advice on how to lower medical insurance costs, especially regarding smoking status, the following function was created:

```python
pythonCopy code
def analyze_smoker(smoker_status):
    if smoker_status == 1:
        print("To lower your cost, you should consider quitting smoking.")
    else:
        print("Smoking is not an issue for you.")
```

In general, insurance costs are higher for smokers. This function analyzes an individual’s smoking status and provides advice on how to lower insurance costs based on whether they smoke or not.

## Usage

To run the project, simply execute the `script.py` file. You can modify the variables to see how changes in each factor affect the insurance cost.

## Regular Updates

This repository is part of the Codecademy Projects and is regularly updated. As I proceed through the course and complete additional projects, new `.py` files will be added, and required changes will be made to the README file to reflect the updates and new insights.

## Conclusion

This project provides a basic introduction to how various factors can influence medical insurance costs. It serves as a foundation for further exploration and more advanced analyses in the field of medical data science.

## Acknowledgments

This project was completed as part of a project on the Codecademy platform.
