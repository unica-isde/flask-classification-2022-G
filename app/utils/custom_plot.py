import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.colors as colors


def generate(labels, values):
    """
    Generate a plot image.
    """
    color_palette = ["olivedrab", "yellowgreen", "seagreen", "teal", "palegreen"]
    color_list = colors.to_rgba_array(color_palette)

    fig = Figure(figsize=(13, 6), dpi=150)
    axis = fig.add_subplot(1, 1, 1)
    axis.barh(labels, values, color=color_list)
    axis.set_title("CLASSIFICATION RESULTS")
    axis.set_xlabel("SCORE %")
    axis.set_ylabel("LABEL")
    axis.grid(True)
    axis.invert_yaxis()

    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return output.getvalue()
