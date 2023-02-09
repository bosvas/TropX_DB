import matplotlib

matplotlib.use('svg')
import matplotlib.pyplot as plt
import io
import base64

def execution_chart(execution_correctness):
    # x = []
    # y = []
    for name, executions in execution_correctness.items():
        executions.sort(key=lambda x: x[0])  # sort by execution_date
        dates, correct_rates = zip(*executions)
        plt.plot_date(dates, correct_rates, label=name, linestyle='-')

    # plt.plot_date(x, y, label=username, linestyle='solid')
    plt.gcf().autofmt_xdate()

    plt.xlabel("Date")
    plt.ylabel("Correctness Rate")
    plt.title("Correctness Rate per Exercise Specification")
    plt.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    img.seek(0)

    plot_img = base64.b64encode(img.getvalue()).decode()

    plt.cla()
    return plot_img