import altair as alt
import numpy as np
import pandas as pd


def plot_histogram(values, index, bins=20, bar_size=15, height=200, n_digits=0):
    hist, bin_edges = np.histogram(values, bins=bins)
    source = (
        pd.DataFrame(hist, index=bin_edges[:-1], columns=["count"])
        .reset_index()
        .rename(columns={index: "count", "index": index})
    )
    stats = pd.DataFrame(
        {
            "mean": [round(values.mean(), 2)],
            "median": [round(np.quantile(values, 0.5), 2)],
        }
    )
    eps = 0.02

    bars = (
        alt.Chart(source)
        .transform_joinaggregate(total_count="sum(count)")
        .transform_calculate(pecent_of_total="datum.count / datum.total_count")
        .mark_bar(size=bar_size)
        .encode(
            x=alt.X(
                f"{index}:Q",
                axis=alt.Axis(title=None, format=f".{n_digits}f"),
                scale=alt.Scale(
                    domain=[bin_edges[0] - eps, bin_edges[-1] + eps], nice=False
                ),
            ),
            y=alt.Y("pecent_of_total:Q", axis=alt.Axis(title=None, format=".0%")),
            tooltip=[
                alt.Tooltip(f"{index}:Q", format=f".{n_digits}f"),
                alt.Tooltip("count:Q", format=".0f"),
            ],
        )
    )
    rule_mean = (
        alt.Chart(stats)
        .mark_rule(color="#ff7f0e", size=1.5, strokeDash=[3, 2])
        .encode(x="mean:Q", tooltip=["mean", "mean:Q"])
    )
    rule_median = (
        alt.Chart(stats)
        .mark_rule(color="#2ca02c", size=1.5, strokeDash=[3, 2])
        .encode(x="median:Q", tooltip=["median", "median:Q"])
    )
    return (bars + rule_mean + rule_median).properties(
        title=f"Histogram of '{index}'", height=height
    )
