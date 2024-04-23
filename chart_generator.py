from io import BytesIO

import matplotlib.pyplot as plt
import pandas as pd
import requests


def generate_chart():
    CSV_URL = "https://raw.githubusercontent.com/RamVasuthevan/city-of-toronto-toronto-island-ferry-ticket-counts/main/toronto_island_ferry_ticket_counts.csv"
    response = requests.get(CSV_URL)
    data = pd.read_csv(BytesIO(response.content))
    data["Timestamp"] = pd.to_datetime(data["Timestamp"])
    data.set_index("Timestamp", inplace=True)
    daily_redemptions = data["Redemption Count"].resample("D").sum()
    first_point_time = data.index.min().strftime("%Y-%m-%d %H:%M:%S")
    last_point_time = data.index.max().strftime("%Y-%m-%d %H:%M:%S")

    fig, ax = plt.subplots(figsize=(20, 6))
    ax.plot(daily_redemptions, color="teal")
    title = "Toronto Island Ferry Ticket Redemptions"
    subtitle = f"(Data from {first_point_time} to {last_point_time})"
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("Date")
    ax.set_ylabel("Ticket Redemptions")

    plt.figtext(0.5, 0.01, subtitle, ha="center", fontsize=10, color="gray")

    chart_output = BytesIO()
    fig.savefig(chart_output, format="svg", bbox_inches="tight")
    plt.close(fig)
    chart_output.seek(0)

    return chart_output.getvalue()
