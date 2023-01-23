import matplotlib

matplotlib.use('svg')
import matplotlib.pyplot as plt
import io
import base64
import datetime
import random


def injury_chart(injuries, username):
    x = []
    y = []
    # injuries_sorted = sorted(injuries, key=lambda injurie: injuries.injurie_date)
    for injury in injuries:
        start_date = injury.injurie_date
        end_date = injury.injurie_date + datetime.timedelta(days=injury.days_to_recover)
        for i in range((end_date - start_date).days + 1):
            day = start_date + datetime.timedelta(days=i)
            x.append(day)
            y.append(1)
    color = (random.random(), random.random(), random.random())

    plt.plot_date(x, y, label=username, linestyle='solid', color = color)
    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel("Injuried")
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    plot_img = base64.b64encode(img.getvalue()).decode()

    plt.cla()
    return plot_img
