# Activity 1: Perform Operations on Image Data

## 1. Extracted Data

**Input Image (6x6):**

$$
\begin{bmatrix}
1 & 0 & 1 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 1 & 1 \\
1 & 0 & 1 & 0 & 1 & 0 \\
1 & 0 & 1 & 1 & 1 & 0 \\
0 & 1 & 1 & 0 & 1 & 1 \\
1 & 0 & 1 & 0 & 1 & 0
\end{bmatrix}
$$

**Kernel / Filter (3x3):**

$$
\begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
$$

---

## 2. Operation 1: Convolution

To perform the convolution, we slide the $3 \times 3$ kernel over the $6 \times 6$ input image (assuming a standard stride of 1 and no padding). This calculates the dot product between the kernel and the overlapping section of the image.

The output Feature Map size is calculated as: $(N - F) / S + 1 = (6 - 3) / 1 + 1 = 4$.

**Example calculation for the first element (top-left):**
$(1\cdot1) + (0\cdot2) + (1\cdot3) + (0\cdot4) + (1\cdot5) + (1\cdot6) + (1\cdot7) + (0\cdot8) + (1\cdot9) = 1 + 0 + 3 + 0 + 5 + 6 + 7 + 0 + 9 = 31$

**Convolved Feature Map (4x4):**

$$
\begin{bmatrix}
31 & 19 & 30 & 21 \\
31 & 25 & 38 & 25 \\
31 & 28 & 35 & 28 \\
31 & 22 & 32 & 22
\end{bmatrix}
$$

---

## 3. Operation 2: Max Pooling

Using a window size of $(2, 2)$, max pooling takes the maximum value from each $2 \times 2$ section of the convolved feature map (assuming a standard stride of 2, non-overlapping).

* **Top-Left Window:** $\max(31, 19, 31, 25) = 31$
* **Top-Right Window:** $\max(30, 21, 38, 25) = 38$
* **Bottom-Left Window:** $\max(31, 28, 31, 22) = 31$
* **Bottom-Right Window:** $\max(35, 28, 32, 22) = 35$

**Pooled Feature Map (2x2):**

$$
\begin{bmatrix}
31 & 38 \\
31 & 35
\end{bmatrix}
$$

---

## 4. Operation 3: Flattening

The final step is to flatten the pooled feature map into a single, continuous 1-Dimensional array (reading row by row from left to right).

**Final Flattened Array:**

$$
\begin{bmatrix}
31 \\
38 \\
31 \\
35
\end{bmatrix}
$$

*(Or written horizontally as `[31, 38, 31, 35]`)*