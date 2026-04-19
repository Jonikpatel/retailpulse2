from scipy import stats


def region_aov_ttest(df, region_a, region_b):
    a = df.loc[df["region"] == region_a, "aov"].dropna()
    b = df.loc[df["region"] == region_b, "aov"].dropna()

    stat, p_value = stats.ttest_ind(a, b, equal_var=False)
    return {"t_stat": float(stat), "p_value": float(p_value)}


def anova_revenue_by_category(df):
    groups = [g["net_revenue"].values for _, g in df.groupby("product_category")]
    stat, p_value = stats.f_oneway(*groups)
    return {"f_stat": float(stat), "p_value": float(p_value)}
