import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def add_logo(ax, logo='logo', corner='upper right', zoom=0.1):
    """
    Add an AXO logo to the corner of a Matplotlib plot.

    Parameters:
    - logo: str, 'logo' is cute AXO face only, 'title' adds the full AXO name.
    - ax: Matplotlib axis, the axis to which the logo will be added.
    - corner: str, 'upper right' or 'upper left', specifies which corner to place the logo.
    - zoom: float, scale factor for the logo size.

    Example:
    import matplotlib.pyplot as plt
    from add_logo_plot import add_logo

    fig, ax = plt.subplots()
    ax.plot([0, 1], [0, 1])  # Simple plot for demonstration

    # Add logo to the upper right corner
    add_logo(ax, logo='title', corner='upper right', zoom=0.2)

    plt.show()

    """
    logo_path = 'add_axo_logo/logos/AXOL1TL_Logo.png'
    if logo=='title':
        logo_path = 'add_axo_logo/logos/AXOL1TL_Title.png'

    # Read the logo image
    img = mpimg.imread(logo_path)
    imagebox = OffsetImage(img, zoom=zoom)
    
    # Determine the position
    if corner == 'upper right':
        x, y = 1, 1
        loc = 'upper right'
    elif corner == 'upper left':
        x, y = 0, 1
        loc = 'upper left'
    else:
        raise ValueError("corner must be 'upper right' or 'upper left'")
    
    # Add the logo image to the plot
    ab = AnnotationBbox(imagebox, (x, y), frameon=False, xycoords='axes fraction', boxcoords="axes fraction", pad=0, box_alignment=(x,y))
    ax.add_artist(ab)
