import numpy as np

# -------------------------------------------------------------------------------------------------------------------- #
class Linear_operator(object):
    """ Abstract class for a linear operator L
    """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def __init__(self, params):

        self.norm = None

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def get_norm(self):
        """ Return the norm of operator L:
                max_{||x||_2 <= 1}( <Lx, Lx>)
        """

        if self.norm is None:
            self.norm = self._compute_norm()

        return self.norm

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def forward(self, x):
        """ Return L x
        """
        h, w = x.shape
        gradient = np.zeros((h, w, 2), x.dtype)  # Allocate gradient array
        # Horizontal direction
        gradient[:, :-1, 0] = x[:, 1:] - x[:, :-1]
        # Vertical direction
        gradient[:-1, :, 1] = x[1:, :] - x[:-1, :]
        return gradient
        #raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def backward(self, y):
        """
            Function to compute the backward divergence.
            Definition in : http://www.ipol.im/pub/art/2014/103/, p208

            :param grad: numpy array [NxMx2], array with the same dimensions as the gradient of the image to denoise.
            :return: numpy array [NxM], backward divergence L^t y
        """

        h, w = y.shape[:2]
        div = np.zeros((h, w), y.dtype)  # Allocate divergence array
        # Horizontal direction
        d_h = np.zeros((h, w), y.dtype)
        d_h[:, 0] = y[:, 0, 0]
        d_h[:, 1:-1] = y[:, 1:-1, 0] - y[:, :-2, 0]
        d_h[:, -1] = -y[:, -2:-1, 0].flatten()

        # Vertical direction
        d_v = np.zeros((h, w), y.dtype)
        d_v[0, :] = y[0, :, 1]
        d_v[1:-1, :] = y[1:-1, :, 1] - y[:-2, :, 1]
        d_v[-1, :] = -y[-2:-1, :, 1].flatten()

        # Divergence
        div = d_h + d_v
        return div

        #raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    # Helper functions
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _sanity_check(self, tol=1e-5):
        """ Verify that for random x and y we have:
            <L x, y>_Y = <x, L^t y>_X
        """

        # Create random x and apply linear operator (forward)
        x = self._random_x()
        Lx = self.forward(x)

        # Create random y and apply linear operator (backward)
        y = self._random_y(Lx.shape)
        Lty = self.backward(y)

        # Compute scalar product in each space
        scalar_product_x = np.sum(Lx ** y, axis=None)
        scalar_product_y = np.sum(x ** Lty, axis=None)

        # Check
        if abs(scalar_product_x - scalar_product_y) > tol:
            raise ValueError(
                'Fail on sanity check for linear operator: <L x, y>_Y={}, <x, L^t y>_X={}'.format(scalar_product_x,
                                                                                                  scalar_product_y))

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _random_x(self, shape=None):

        raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _random_y(self, shape=None):

        raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _compute_norm(self):

        raise NotImplementedError



# -------------------------------------------------------------------------------------------------------------------- #
class Grid_linear_opreator(Linear_operator):
    """ Abstract class for a grid based linear operator L in connectivity
    """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _random_x(self, shape=(10, 20)):
        return np.random.rand(shape)

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _random_y(self, shape=None):
        return np.random.rand(shape)

# -------------------------------------------------------------------------------------------------------------------- #
class Gradient_grid_linear_opreator(Grid_linear_opreator):
    """ Class for a gradient grid based linear operator L in connectivity
    """

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def forward(self, x):
        """ Return L x
        """
        # TODO: to implement

        raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def backward(self, y):
        """ Return L^t y
        """

        # TODO: to implement

        raise NotImplementedError

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    # Helper functions
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -#
    def _compute_norm(self):

        return 8.



