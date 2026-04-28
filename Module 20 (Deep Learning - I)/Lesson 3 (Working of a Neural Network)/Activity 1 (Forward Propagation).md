# Activity 1: Forward Propagation Calculation

Here are the step-by-step forward propagation calculations based on the provided neural network architecture and values.

### **Given Values**
* **Inputs:** $X_1 = 20, X_2 = 30, X_3 = 12$
* **Weights (Hidden Layer):** $W_1 = 0.6, W_2 = 0.6, W_3 = 0.3$
* **Weight (Output Layer):** $W_4 = 0.7$
* **Bias:** $0$ (Assumed)

---

### **Step 1: Calculate the value at the Hidden Layer**
We first calculate the weighted sum of the inputs and their corresponding weights entering the hidden layer node.

$$Z_{hidden} = (X_1 \cdot W_1) + (X_2 \cdot W_2) + (X_3 \cdot W_3)$$

**Substituting the values:**
$$Z_{hidden} = (20 \cdot 0.6) + (30 \cdot 0.6) + (12 \cdot 0.3)$$
$$Z_{hidden} = 12 + 18 + 3.6$$
**$Z_{hidden} = 33.6$**

*(Note: If using ReLU activation at the hidden layer, $ReLU(33.6) = 33.6$ because the value is positive).*

---

### **Step 2: Calculate the value at the Output Layer**
Next, we multiply the hidden layer's output by the final weight ($W_4$) to reach the output node.

$$Z_{output} = Z_{hidden} \cdot W_4$$

**Substituting the values:**
$$Z_{output} = 33.6 \cdot 0.7$$
**$Z_{output} = 23.52$**

---

### **Step 3: Apply the Classification Activation Function**
Since this is a **Classification problem**, we use the **Sigmoid activation function** to map the result to a probability between 0 and 1.

**Sigmoid Formula:**
$$Output = \frac{1}{1 + e^{-z}}$$

**Applying the calculation:**
$$Output = \frac{1}{1 + e^{-23.52}}$$

Because $e^{-23.52}$ is an extremely small number (approaching 0), the equation simplifies to:
$$Output \approx \frac{1}{1 + 0}$$
**$Final \ Output \approx 1.0$**

---

### **Final Answer Summary**
Based on the forward propagation calculation for this classification problem, the final output value is **1**.