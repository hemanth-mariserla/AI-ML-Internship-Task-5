# AI-ML-Internship-Task-5
# Decision Trees and Random Forests – AI & ML Internship Task

## Objective

Implement and compare Decision Tree and Random Forest models for classification. Learn how to control overfitting, interpret feature importance, and evaluate models using cross-validation.

---

## Dataset

**Dataset Used:** [Heart Disease Dataset](https://www.kaggle.com/datasets/johnsmith88/heart-disease-dataset)
**Target Variable:** `target` (1 = Heart Disease, 0 = No Heart Disease)

---

## Tools & Libraries

* Python
* Pandas, NumPy
* Scikit-learn
* Matplotlib, Seaborn
* Graphviz (optional)

---

## Steps Performed

1. **Data Loading & Exploration**

   * Loaded dataset from CSV
   * Checked null values and basic statistics

2. **Data Preprocessing**

   * Defined features (`X`) and target (`y`)
   * Split data into training and testing sets

3. **Decision Tree Classifier**

   * Trained a basic Decision Tree Classifier
   * Visualized the tree using `plot_tree()`
   * Limited `max_depth` to prevent overfitting

4. **Random Forest Classifier**

   * Trained with 100 estimators
   * Compared accuracy with Decision Tree
   * Extracted and visualized feature importances

5. **Cross-Validation**

   * Evaluated Random Forest with 5-fold cross-validation

---

## 📊 Results

Decision Tree Accuracy: 0.9853658536585366
Limited Depth Accuracy: 0.8
Random Forest Accuracy: 0.9853658536585366
Random Forest CV Accuracy: 0.9970731707317073
---


## 📸 Visualizations

* Decision Tree Structure
<img width="1500" height="800" alt="Figure_1" src="https://github.com/user-attachments/assets/a1411a10-47ea-466e-987d-3733a530b084" />

* Feature Importance Bar Chart
<img width="640" height="480" alt="Figure_2" src="https://github.com/user-attachments/assets/33688d66-c9cc-4b2a-a34c-9e00d727678c" />


