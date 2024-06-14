# statistical_analysis.py
import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt
import seaborn as sns

def perform_statistical_analysis(csv_path):
    df = pd.read_csv(csv_path)

    # Descriptive statistics
    print(df.describe())

    # T-test comparing pre-pausal and non-pre-pausal durations
    pre_pausal = df[df['label'] == 'pre-pausal']['duration']
    non_pre_pausal = df[df['label'] == 'non-prepausal']['duration']

    t_test = sm.stats.ttest_ind(pre_pausal, non_pre_pausal)
    print(f"T-test results: {t_test}")

    # Linear regression model predicting duration based on formants and context
    model = ols('duration ~ f1 + f2 + C(label)', data=df).fit()
    print(model.summary())

    # Visualizations
    sns.boxplot(x='label', y='duration', data=df)
    plt.title('Duration of Schwa: Pre-pausal vs. Non-prepausal')
    plt.show()

    sns.scatterplot(x='f1', y='f2', hue='label', data=df)
    plt.title('Formant Frequencies of Schwa')
    plt.show()

def main():
    csv_path = 'data/results/schwa_analysis_results.csv'
    perform_statistical_analysis(csv_path)


if __name__ == "__main__":
    main()
