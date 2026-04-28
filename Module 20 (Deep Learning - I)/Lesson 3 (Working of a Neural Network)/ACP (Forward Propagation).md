# Assignment: Forward Propagation

Here are the step-by-step forward propagation calculations based on the provided neural network architecture and given values.

### **Given Values**
* **Inputs:** $a = 20, b = 30, c = 15$
* **Weights:** * $w_1 = 0.6$
  * $w_2 = 0.3$
  * $w_3 = 0.6$
  * $w_4 = 0.3$
* **Problem Type:** Regression (Requires a Linear Activation Function at the output).

---

### **Step 1: Calculate the values at the Hidden Layer**

Based on the diagram, we have two hidden nodes. Let's call the top hidden node $H_1$ and the bottom hidden node $H_2$. We calculate the weighted sum (dot product) of the inputs going into each node.

**For Top Hidden Node ($H_1$):**
The diagram shows connections coming from $a$ (weight $w_1$), $b$ (weight $w_1$), and $c$ (weight $w_2$).
$$H_1 = (a \cdot w_1) + (b \cdot w_1) + (c \cdot w_2)$$
$$H_1 = (20 \cdot 0.6) + (30 \cdot 0.6) + (15 \cdot 0.3)$$
$$H_1 = 12 + 18 + 4.5$$
**$H_1 = 34.5$**

**For Bottom Hidden Node ($H_2$):**
The diagram shows connections coming from $a$ (weight $w_2$), $b$ (weight $w_2$), and $c$ (weight $w_1$).
$$H_2 = (a \cdot w_2) + (b \cdot w_2) + (c \cdot w_1)$$
$$H_2 = (20 \cdot 0.3) + (30 \cdot 0.3) + (15 \cdot 0.6)$$
$$H_2 = 6 + 9 + 9$$
**$H_2 = 24$**

---

### **Step 2: Calculate the pre-activation value at the Output Layer**

Now we take the values from our hidden nodes ($H_1$ and $H_2$) and multiply them by their respective weights ($w_3$ and $w_4$) connecting to the final output node ($y$).

$$Z_{y} = (H_1 \cdot w_3) + (H_2 \cdot w_4)$$
$$Z_{y} = (34.5 \cdot 0.6) + (24 \cdot 0.3)$$
$$Z_{y} = 20.7 + 7.2$$
**$Z_{y} = 27.9$**

---

### **Step 3: Apply the Regression Activation Function**

The assignment states: *"Consider that this is a Regression problem, and use the activation function accordingly."* For regression problems, we need continuous numerical output, so the standard activation function used at the output layer is the **Linear Activation Function**. 
A linear activation function simply outputs the exact value it receives ($f(x) = x$). Therefore, no mathematical transformation is needed for our $Z_y$ value.

$$y = Z_{y}$$
**$y = 27.9$**

---

### **Final Answer Summary**
Based on the forward propagation calculation for this regression network, the final output value for **$y$** is **27.9**.