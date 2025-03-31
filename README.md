# ML_Alzheimer_Disease

### Problem Description
Alzheimer's disease is a neurodegenerative disorder that progressively impairs memory and cognitive functions. Early detection is crucial for providing timely medical intervention. This project aims to develop a Machine Learning model to assist in diagnosing Alzheimer's disease based on clinical data, demographic details, lifestyle factors, cognitive and functional assessments and symptoms.

### Dataset
- **Source**: Kaggle. https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
- **Description**: This dataset contains extensive health information for 2,149 patients, each uniquely identified with IDs ranging from 4751 to 6900. The dataset includes demographic details, lifestyle factors, medical history, clinical measurements, cognitive and functional assessments, symptoms, and a diagnosis of Alzheimer's Disease.
- **Data Type**: The dataset includes both numerical and categorical features, with some categorical variables having 4 or fewer categories.

### Solution
The implemented solution involves:
- **Feature Selection** to remove irrelevant or redundant information.
- **Hyperparameter Optimization** using techniques such as GridSearchCV to improve model performance.
- **Model Evaluation** to compare different classifiers and select the best-performing one, LightGBM, based on F1-score and confusion matrix.

### Repository Structure
```
ML_Alzheimer_Disease/
│-- data/                # Dataset files 
│-- models/              # Saved ML models
│-- notebooks/           # Jupyter Notebooks with analysis and training
│-- results/             # Output results such as metrics, plots, and logs
│-- src/                 # Python scripts 
│-- README.md            # Project documentation 
```

---

### Descripción del Problema
El Alzheimer es una enfermedad neurodegenerativa que afecta progresivamente la memoria y las funciones cognitivas. La detección temprana es clave para ofrecer tratamientos oportunos. El objetivo de este proyecto es desarrollar un modelo de aprendizaje automático que ayude a diagnosticar la enfermedad de Alzheimer a partir de datos clínicos, detalles demográficos, factores de estilo de vida, evaluaciones cognitivas y funcionales y síntomas.

### Dataset
- **Fuente**: Kaggle. https://www.kaggle.com/datasets/rabieelkharoua/alzheimers-disease-dataset
- **Descripción**: Este conjunto de datos contiene amplia información sanitaria de 2.149 pacientes, cada uno de ellos identificado de forma única con IDs que van de 4751 a 6900. El conjunto de datos incluye detalles demográficos, factores de estilo de vida, historial médico, mediciones clínicas, evaluaciones cognitivas y funcionales, síntomas y un diagnóstico de enfermedad de Alzheimer.
- **Tipo de Datos**: Contiene variables numéricas y categóricas, algunas con 4 o menos categorías.

### Solución
La solución implementada incluye:
- **Selección de Características** para eliminar información irrelevante o redundante.
- **Optimización de Hiperparámetros** con GridSearchCV para mejorar el rendimiento del modelo.
- **Evaluación del Modelo** comparando distintos clasificadores y seleccionando el mejor, LightGBM, basado en el F1-score y la matriz de confusión.

### Estructura del Repositorio
```
ML_Alzheimer_Disease/
│-- data/                # Archivos del dataset 
│-- models/              # Modelos de ML guardados
│-- notebooks/           # Jupyter Notebooks con análisis y entrenamiento
│-- results/             # Resultados como métricas, gráficos y logs
│-- src/                 # Scripts Python
│-- README.md            # Documentación del proyecto
```

