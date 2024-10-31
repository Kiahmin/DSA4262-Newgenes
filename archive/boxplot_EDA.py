df = pd.read_csv("studies/ProjectStorage/reference/parsed_data.csv")
# Select only numerical columns for outlier detection
numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

def detect_outliers(df):
    outlier_indices = []
    for col in numeric_cols:
        # Drop NaN values for the current column
        col_data = df[col].dropna()
        Q1 = col_data.quantile(0.25)
        Q3 = col_data.quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        # Find outlier indices
        outlier_list_col = df[(df[col] < lower_bound) | (df[col] > upper_bound)].index
        outlier_indices.extend(outlier_list_col)
    # Get unique indices (some rows may be outliers in multiple columns)
    outlier_indices = list(set(outlier_indices))
    # Return the rows with outliers
    return df.loc[outlier_indices]
# Detect outliers in the entire DataFrame
outliers_df = detect_outliers(df)# Display the rows with outliers
print("Rows with outliers detected in any numerical column:")
print(outliers_df)
for col in numeric_cols:
    sns.boxplot(data=df[col])
    plt.title(f'Boxplot of {col}')
    plt.show()


