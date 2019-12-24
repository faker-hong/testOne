import numpy as np
import matplotlib.pyplot as plt


# Creates matrix t (right side of the augmented matrix).
t = np.array([4, 11])

# Creates matrix vw (left side of the augmented matrix).
vw = np.array([[1, 2], [3, 5]])


def check_vector_span(set_of_vectors, vector_to_check):
    # Creates an empty vector of correct size
    vector_of_scalars = np.asarray([None] * set_of_vectors.shape[0])

    # Solves for the scalars that make the equation true if vector is within the span
    try:
        # TODO: Use np.linalg.solve() function here to solve for vector_of_scalars
        vector_of_scalars = np.linalg.solve(set_of_vectors, vector_to_check)
        if not (vector_of_scalars is None):
            print("\nVector is within span.\nScalars in s:", vector_of_scalars)
    # Handles the cases when the vector is NOT within the span
    except Exception as exception_type:
        if str(exception_type) == "Singular matrix":
            print("\nNo single solution\nVector is NOT within span")
        else:
            print("\nUnexpected Exception Error:", exception_type)
    return vector_of_scalars


check_vector_span(vw, t)

vw2 = np.array([[1, 2], [2, 4]])
t2 = np.array([6, 12])

vw3 = np.array([[1, 2], [1, 2]])
t3 = np.array([6, 10])

check_vector_span(vw2, t2)
check_vector_span(vw3, t3)