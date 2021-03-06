# :mountain_snow: mountainplot 
mountainplot provides an easy to API to plot a chart showing triangles "mountains" representing the fulfilement of goals.
It  is meant as an enhancement for the famous matplotlib. 

For example if you have climbed 5678m (64.2%) of the Mount Everest :mountain_snow: and you would like to plot your gain on a pretty chart.
(and possible other mountains of the seven summits)

## Usage
Basically two things are relevant for the usage of mountainplot, namely: 
* `Mountain` (a named tuple providing parameter for the mountain plot)
* `mountainplot` (function taking an axes.Axes matplotlib object and a list of mountains)

### Seven Summits Example
![Seven Summits](img/seven_summits.png "Seven Summits")

Code for the upper plot.
```python
import matplotlib.pyplot as plt
from mountainplot import Mountain, mountainplot

SEVEN_SUMMITS = [
    Mountain(name='Everest', height=8848 , level=0.642, color='lime', text_color='white'),
    ...
]

plt.style.use('dark_background')
fig, ax = plt.subplots()

ax.axes.get_xaxis().set_visible(False)
mountainplot(ax, SEVEN_SUMMITS)

plt.box(False)
plt.show()
```
