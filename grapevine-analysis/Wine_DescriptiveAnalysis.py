import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as stats
import matplotlib.pyplot as plt
from sklearn.datasets import load_wine

wine = load_wine()
df = pd.DataFrame(wine.data, columns=wine.feature_names)
df['target'] = wine.target
df['target_name'] = df['target'].map(dict(enumerate(wine.target_names)))

# Check for missing values
print(df.isnull().sum())

#### Class Distribution Visualization ####
sns.set(style='whitegrid', font_scale=1.2, rc={"figure.dpi": 150})
fig, axes = plt.subplots(4, 4, figsize=(16, 12))
axes = axes.flatten()

for i, col in enumerate(wine.feature_names):
    ax = axes[i]

    sns.boxplot(
        data=df,
        x='target_name',
        y=col,
        palette='pastel',
        linewidth=1.2,
        fliersize=3,
        ax=ax  # Axis to be plot
    )

    # Data for Kruskal-Wallis test
    groups = []
    class_names = df['target_name'].unique()

    for class_name in class_names:
        class_subset = df[df['target_name'] == class_name]
        values = class_subset[col]
        groups.append(values)

    # Kruskal-Wallis test
    stat, p_value = stats.kruskal(*groups)

    p_text = f"p = {p_value:.3e}"
    if p_value < 0.001:
        p_text = "p < 0.001"

    # p-value on the plot
    ax.annotate(
        p_text,
        xy=(0.5, 0.9),
        xycoords='axes fraction',
        ha='center',
        va='center',
        fontsize=10,
        color='black'
    )

    ax.set_title(col, fontsize=11, fontweight='semibold')
    ax.set_xlabel("")
    ax.set_ylabel("")
    sns.despine(ax=ax)

# Removing unused subplots
for j in range(len(wine.feature_names), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.savefig("wine_boxplots.png", dpi=300, bbox_inches='tight')

#### Correlation Heatmap ####
corr = df[wine.feature_names].corr()

sns.set(style='white', font_scale=1.2, rc={"figure.dpi": 150})
plt.figure(figsize=(12, 10))
sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap='coolwarm',
    square=True,
    cbar_kws={"shrink": 0.75, "label": "Correlation"},
    linewidths=0.5,
    linecolor='gray',
    annot_kws={"size": 10}
)
plt.title("Correlation Matrix of Wine Features", fontsize=14, fontweight='bold', pad=15)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.savefig("wine_feature_correlation_heatmap.png", dpi=300, bbox_inches='tight')
plt.show()
