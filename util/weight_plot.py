import matplotlib

matplotlib.use('svg')
import matplotlib.pyplot as plt
import io
import base64

def weight_histogram_chart(weights, username):
    x = []
    y = []
    weights_sorted = sorted(weights, key=lambda weight: weight.weight_date)
    for weight in weights_sorted:
        x.append(weight.weight_date)
        y.append(weight.weight)

    plt.plot_date(x, y, label=username, linestyle='solid')
    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel("Weight")
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    plot_img = base64.b64encode(img.getvalue()).decode()

    plt.cla()
    return plot_img
