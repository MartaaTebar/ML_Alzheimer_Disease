# imports
import matplotlib.pyplot as plt
import seaborn as sns

# Función para calcular la cardinalidad de una columna
def cardinalidad(col, df):
    return col.nunique(dropna = False) / len(df) * 100

def plot_grouped_boxplots_and_histograms(df, cat_col, num_col, group_size=5):

    unique_cats = df[cat_col].unique()
    num_cats = len(unique_cats)

    for i in range(0, num_cats, group_size):
        subset_cats = unique_cats[i:i+group_size]
        subset_df = df[df[cat_col].isin(subset_cats)]
        
        # Crear una figura con dos subgráficas
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))

        # Histogram
        for cat in subset_cats:
            sns.histplot(subset_df[subset_df[cat_col] == cat][num_col], 
                         kde=True, label=str(cat), ax=axes[0])
        axes[0].set_title(f'Histograms of {num_col} for {cat_col}')
        axes[0].set_xlabel(num_col)
        axes[0].set_ylabel('Frequency')
        axes[0].legend()
        
        # Boxplot
        sns.boxplot(ax=axes[1], x=cat_col, y=num_col, data=subset_df)
        axes[1].set_title(f'Boxplots of {num_col} for {cat_col}')
        axes[1].tick_params(axis='x', rotation=45)

        # Mostrar figura
        plt.tight_layout()
        plt.show()

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_grouped_boxplots_and_histograms_relative(df, cat_col, num_col, group_size=5):

    unique_cats = df[cat_col].unique()
    num_cats = len(unique_cats)

    for i in range(0, num_cats, group_size):
        subset_cats = unique_cats[i:i+group_size]
        subset_df = df[df[cat_col].isin(subset_cats)]
        
        # Crear una figura con dos subgráficas
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    
        # Histogram (datos relativos como proporción)
        for cat in subset_cats:
            subset = subset_df[subset_df[cat_col] == cat]
            total = len(subset)  # Total de elementos en la categoría
            sns.histplot(subset[num_col], kde=True, stat='probability', label=str(cat), ax=axes[0])
        
        axes[0].set_title(f'Relative Histograms of {num_col} for {cat_col}')
        axes[0].set_xlabel(num_col)
        axes[0].set_ylabel('Relative Frequency')
        axes[0].legend()
        
        # Boxplot (sin cambios, relativo aquí no aplica directamente)
        sns.boxplot(ax=axes[1], x=cat_col, y=num_col, data=subset_df)
        axes[1].set_title(f'Boxplots of {num_col} for {cat_col}')
        axes[1].tick_params(axis='x', rotation=45)


        # Mostrar figura
        plt.tight_layout()
        plt.show()


def plot_categorical_relationship(df, cat_col1, cat_col2, relative_freq=False, show_values=False, size_group = 5):
    # Prepara los datos
    count_data = df.groupby([cat_col1, cat_col2]).size().reset_index(name='count')
    total_counts = df[cat_col1].value_counts()
    
    # Convierte a frecuencias relativas si se solicita
    if relative_freq:
        count_data['count'] = count_data.apply(lambda x: x['count'] / total_counts[x[cat_col1]], axis=1)

    # Si hay más de size_group categorías en cat_col1, las divide en grupos de size_group
    unique_categories = df[cat_col1].unique()
    if len(unique_categories) > size_group:
        num_plots = int(np.ceil(len(unique_categories) / size_group))

        for i in range(num_plots):
            # Selecciona un subconjunto de categorías para cada gráfico
            categories_subset = unique_categories[i * size_group:(i + 1) * size_group]
            data_subset = count_data[count_data[cat_col1].isin(categories_subset)]

            # Crea el gráfico
            plt.figure(figsize=(6, 4))
            ax = sns.barplot(x=cat_col1, y='count', hue=cat_col2, data=data_subset, order=categories_subset)

            # Añade títulos y etiquetas
            plt.title(f'Relación entre {cat_col1} y {cat_col2} - Grupo {i + 1}')
            plt.xlabel(cat_col1)
            plt.ylabel('Frecuencia' if relative_freq else 'Conteo')
            plt.xticks(rotation=45)

            # Mostrar valores en el gráfico
            if show_values:
                for p in ax.patches:
                    ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                                ha='center', va='center', fontsize=10, color='black', xytext=(0, size_group),
                                textcoords='offset points')

            # Muestra el gráfico
            plt.show()
    else:
        # Crea el gráfico para menos de size_group categorías
        plt.figure(figsize=(6, 4))
        ax = sns.barplot(x=cat_col1, y='count', hue=cat_col2, data=count_data)

        # Añade títulos y etiquetas
        plt.title(f'Relación entre {cat_col1} y {cat_col2}')
        plt.xlabel(cat_col1)
        plt.ylabel('Frecuencia' if relative_freq else 'Conteo')
        plt.xticks(rotation=45)

        # Mostrar valores en el gráfico
        if show_values:
            for p in ax.patches:
                ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                            ha='center', va='center', fontsize=10, color='black', xytext=(0, size_group),
                            textcoords='offset points')

        # Muestra el gráfico
        plt.show()


        
def dispersion_con_correlacion(df, columna_x, columna_y, tamano_puntos=50, mostrar_correlacion=False):
 
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x=columna_x, y=columna_y, s=tamano_puntos)

    if mostrar_correlacion:
        correlacion = df[[columna_x, columna_y]].corr().iloc[0, 1]
        plt.title(f'Diagrama de Dispersión con Correlación: {correlacion:.2f}')
    else:
        plt.title('Diagrama de Dispersión')

    plt.xlabel(columna_x)
    plt.ylabel(columna_y)
    plt.grid(True)
    plt.show()
