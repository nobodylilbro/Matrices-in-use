import numpy as np

# Step 1: Define historical datasets (matrix/table format)
bad_clients = np.array([
    [1, 4, 1],
    [2, 4, 2],
    [2, 1, 2]
])

good_clients = np.array([
    [4, 4, 4],
    [5, 4, 5],
    [4, 1, 4]
])

# Step 2: Calculate the geometric centers (centroids) for both groups
center_bad = np.mean(bad_clients, axis=0)
center_good = np.mean(good_clients, axis=0)

# Step 3: Create the grading vector (w) by connecting the two centers
w = center_good - center_bad

# Step 4: Find the spatial equilibrium midpoint and calculate the threshold (b)
midpoint = (center_good + center_bad) / 2
b = np.dot(w, midpoint)

# Step 5: Evaluate a new applicant
new_client = np.array([5, 3, 4])
client_score = np.dot(w, new_client)

if client_score >= b:
    print("Decision: APPROVED")
else:
    print("Decision: REJECTED")