# Assignment: Operations in Convolutional Neural Networks

## 1. Extracted Data

**Input Image (5x5):**
$$
\begin{bmatrix}
0 & 25 & 75 & 80 & 80 \\
0 & 75 & 80 & 80 & 80 \\
0 & 75 & 80 & 80 & 80 \\
0 & 70 & 75 & 80 & 80 \\
0 & 0 & 0 & 0 & 0
\end{bmatrix}
$$

**Kernel / Filter (3x3):**
*(This is a standard Sobel vertical edge detection filter)*
$$
\begin{bmatrix}
-1 & 0 & 1 \\
-2 & 0 & 2 \\
-1 & 0 & 1
\end{bmatrix}
$$

---

## 2. Operation 1: Convolution

To perform the convolution, we slide the $3 \times 3$ kernel over the $5 \times 5$ input image (using a standard stride of 1 and no padding). This calculates the element-wise multiplication and sum between the kernel and the overlapping section of the image.

The output Feature Map size is calculated as: $(N - F) / S + 1 = (5 - 3) / 1 + 1 = 3$.

**Example calculation for the first element (top-left window):**
$(-1\cdot0) + (0\cdot25) + (1\cdot75) + (-2\cdot0) + (0\cdot75) + (2\cdot80) + (-1\cdot0) + (0\cdot75) + (1\cdot80)$
$= 0 + 0 + 75 + 0 + 0 + 160 + 0 + 0 + 80 = 315$

Applying this across the entire matrix yields the **Convolved Feature Map (3x3):**
$$
\begin{bmatrix}
315 & 70 & 5 \\
315 & 20 & 5 \\
230 & 25 & 10
\end{bmatrix}
$$

---

## 3. Operation 2: Max Pooling

The instructions specify a window size of $(2, 2)$. Since our convolved feature map is $3 \times 3$, using a non-overlapping stride of 2 would drop data. Therefore, we assume a **stride of 1** (overlapping windows) to symmetrically capture all maximum values and yield a $2 \times 2$ matrix.

* **Top-Left Window:** $\max(315, 70, 315, 20) = 315$
* **Top-Right Window:** $\max(70, 5, 20, 5) = 70$
* **Bottom-Left Window:** $\max(315, 20, 230, 25) = 315$
* **Bottom-Right Window:** $\max(20, 5, 25, 10) = 25$

**Pooled Feature Map (2x2):**
$$
\begin{bmatrix}
315 & 70 \\
315 & 25
\end{bmatrix}
$$

---

## 4. Operation 3: Flattening

The final step is to flatten the pooled feature map into a 1-Dimensional array by reading it row by row, from left to right.

**Final Flattened Array:**
$$
\begin{bmatrix}
315 \\
70 \\
315 \\
25
\end{bmatrix}
$$
*(Or written horizontally as `[315, 70, 315, 25]`)*