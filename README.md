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

Relation to Neuroscience
---------------

Mexican hat (Difference of Gaussians) receptive fields are found in retinal ganglion cells and the LGN. 
They vary with respect to their polarity (on-center vs. off-center). 
Orientation specific receptive fields (Gabor filters) are found throughout the cortex. 
Complex cells react equally well to step edges and lines. 

Reference
----------------

Introduction to Computational Neuroscience, Hanspeter Mallot, [University of Tübingen](http://www.uni-tuebingen.de/cog)

License
----------------
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:vcard="http://www.w3.org/2001/vcard-rdf/3.0#">
  <a rel="license"
       href="http://creativecommons.org/publicdomain/zero/1.0/">
           <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
             </a>
               <br />
                 To the extent possible under law,
                   <a rel="dct:publisher"
                        href="jonasnick.github.com">
                            <span property="dct:title">Jonas Nick</span></a>
                              has waived all copyright and related or neighboring rights to
                                <span property="dct:title">Visualizing Receptive Fields</span>.
                                This work is published from:
                                <span property="vcard:Country" datatype="dct:ISO3166"
                                      content="DE" about="jonasnick.github.com">
                                        Germany</span>.
                                        </p>
