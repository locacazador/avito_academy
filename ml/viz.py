import datetime
from typing import Tuple, Union, List

import matplotlib.pyplot as plt
import numpy as np


def plot_normal_graph(center: Tuple[Union[int, float], ...],
                      name: str,
                      cov_matrix: List[List[Union[float, int]]],
                      color: str,
                      ax: plt.Axes
                      ) -> None:
    """
    Функция строит для переданной оси график первого задания
    args:
        :center: - центр распределения. Ожидается кортеж размера (N,)
        :name: - подпись, заголовок для графика 
        :cov_matrix: - матрица ковариации для генерации нормального
                       распределения
        :color: - цвет краев точек
        :ax: - ось, на которой это будет отрисовано
    """
    # генерим нормальное распредление и распаковываем
    multi_norm_distr = np.random.multivariate_normal(mean=center,
                                                     cov=cov_matrix,
                                                     size=1500)
    x, y = multi_norm_distr.T
    ax.scatter(x, y, edgecolors=color)
    ax.set_title(name)


def plot_hist_graph(name: str,
                    ax: plt.Axes,
                    color: str) -> None:
    """
    Строит геометрическое распределение
    args:
        :name: - подпись, заголовок для графика 
        :ax: - ось, на которой это будет отрисовано
        :color: - цвет графика
    """
    # генерим геометрическое распредление
    data_hist = np.random.geometric(p=0.1, size=3000)
    ax.hist(data_hist, bins=40, color=color)
    ax.set_title(name)


def plot_logs_graph(name: str,
                    ax: plt.Axes,
                    colors: Tuple[str, ...]) -> None:
    """
    Строит log(x) и log(2x)
    args:
        :name: - подпись, заголовок для графика 
        :ax: - ось, на которой это будет отрисовано
        :color: - tuple цветов, ожидается размер (2,)
    """
    x = np.linspace(0.01, 6, 1000)
    log_y = np.log(x)
    log_2y = np.log(2 * x)

    color1, color2 = colors

    ax.plot(x, log_y, label='log(x)', color=color1)
    ax.plot(x, log_2y, label='log(2x)', color=color2)
    ax.legend()
    ax.set_title(name)


def plot_bar_graph(name: str,
                   dates: List[datetime.date],
                   center: Union[int, float],
                   ax: plt.Axes) -> None:
    """
    Строит log(x) и log(2x)
    args:
        :name: - подпись, заголовок для графика 
        :dates: - список дат, для которых будет отрисовка
                  Ожидается объектов datetime.date внутри
        :center: - среднее значение для генерации нормального
                 распределения
        :ax: - ось, на которой это будет отрисовано
    """
    normal_data = np.random.normal(loc=center, size=len(dates))
    dates_copy = dates  # no inplace operations
    dates_copy.sort()
    ax.bar(dates_copy, normal_data)
    ax.xaxis.set_ticks(dates_copy)
    ax.tick_params(axis='x', labelrotation=90)
    ax.set_title(name)


if __name__ == '__main__':
    fig, axes = plt.subplots(2, 2, figsize=(17, 10))
    fig.suptitle('Plot examples', fontsize=20)
    plot_config = {
        1: {
            'function': plot_normal_graph,
            'params': {
                'center': (20, 10),
                'name': 'Scatter plot example',
                'cov_matrix': [[1, 0.7], [0.7, 1]],
                'color': 'black'
            }
        },
        2: {
            'function': plot_hist_graph,
            'params': {
                'name': 'Hist plot example',
                'color': 'red'
            }
        },
        3: {
            'function': plot_logs_graph,
            'params': {
                'name': 'Line plot example',
                'colors': ('k', 'r')

            }
        },
        4: {
            'function': plot_bar_graph,
            'params': {
                'name': 'Bar plot example',
                'dates': [datetime.date(year=2021, month=1, day=1)
                          + datetime.timedelta(days=i) for i in range(0, 14)],
                'center': 5
            }
        }
    }

    for idx, axis in enumerate(axes.flatten()):
        # гарантируем, что есть такой ключ
        func, params = plot_config[idx + 1].values()
        params['ax'] = axis
        func(**params)
    plt.show()
