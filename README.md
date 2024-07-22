# Add cute AXO logo to all your plots


![Logo Example](https://github.com/thaarres/add_axo_logo/blob/4bbec00f093b9f0d3f7a5a7ef8284f4b82a69595/add_axo_logo/logos/AXOL1TL_Logo.png)

## Installation

You can install the package using pip:

```sh
pip install git+https://github.com/thaarres/add_axo_logo.git

```

And then use it the following way
```python
import matplotlib.pyplot as plt
from add_axo_logo import add_logo

fig, ax = plt.subplots()
ax.plot([0, 1], [0, 1])  # Simple plot for demonstration

# Add logo to the upper right corner
add_logo(ax, logo='title', corner='upper right', zoom=0.2)
#add_logo(ax, logo='logo', corner='upper right', zoom=0.2)

plt.show()

![Logo Example](https://github.com/thaarres/add_axo_logo/blob/4bbec00f093b9f0d3f7a5a7ef8284f4b82a69595/add_axo_logo/logos/add_logo_example.png)




