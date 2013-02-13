ReceptiveFields
===============

Receptive Fields in the primary visual pathway applied to images. 

<a href="http://nbviewer.ipython.org/urls/raw.github.com/jonasnick/ReceptiveFields/master/receptiveFields.ipynb">**Static html version**</a>

Use <a href="https://github.com/ipython/ipython">IPython Notebook</a> to open the .ipynb file or use receptiveFields.py.

Filters
---------------

    *   Gaussian
    *   Mexican hat
    *   Gabor
    *   Quadrature Pairs (edge energy)

using the scipy.signal function convolve

Theory
---------------

Mexican hat (Difference of Gaussians) receptive fields are found in retinal ganglion cells and the LGN. 
They vary with respect to their polarity (on-center vs. off-center). 
Orientation specific receptive fields (Gabor filters) are found throughout the cortex. 
Complex cells react equally well to step edges and lines. 

Reference
----------------

Introduction to Computational Neuroscience, Hanspeter Mallot, [University of Tübingen](http://www.uni-tuebingen.de/cog)
