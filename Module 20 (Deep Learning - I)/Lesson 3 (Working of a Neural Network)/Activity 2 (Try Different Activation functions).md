# Activity 2: Try Different Activation Functions

### **Dataset & Architecture Setup**
Based on the instructions for the Pima Indians diabetes dataset (Binary Classification), the neural network was configured with the following parameters:

* **Problem Type:** Classification
* **Training to Test Data Ratio:** 80%
* **Hidden Layers:** 2
    * **Hidden Layer 1:** 4 Neurons
    * **Hidden Layer 2:** 6 Neurons

---

### **Results: Testing Loss Comparison**

After running the simulation with the specified architecture, here are the testing loss results for the different activation functions:

**1) Sigmoid Activation Function**
* **Test Loss:** 0.520
* *(Note: Training loss was observed at 0.506)*

**2) Tanh Activation Function**
* **Test Loss:** 0.498
* *(Note: Tanh often converges faster than Sigmoid due to its zero-centered range of -1 to 1).*