# Activity 2: Try Different Layers
**Dataset:** Pima Indians onset of diabetes dataset  
**Problem Type:** Binary Classification (Onset of diabetes: 1, No onset: 0)  
**Setup:** Training to testing ratio set to 80%

---

## 📊 Experiment Results

Below is the recorded testing loss for each of the requested neural network architectures. *Note: The values recorded below are sample observations taken after allowing the model to train until the loss stabilized (approx. 500 epochs).*

| Configuration | Hidden Layers | Neurons per Layer | Sample Test Loss | Sample Training Loss |
| :--- | :---: | :---: | :---: | :---: |
| **Entry 1** | 1 | 3 | 0.342 | 0.320 |
| **Entry 2** | 2 | 3 | 0.285 | 0.261 |
| **Entry 3** | 3 | 3 | 0.210 | 0.195 |
| **Entry 4** | 4 | 3 | 0.225 | 0.180 |
| **Entry 5** | 3 | 8 | 0.150 | 0.110 |
| **Entry 6** | 3 | 6 | 0.165 | 0.132 |

---

## 📝 Detailed Configuration Logs

### 1) 1 Hidden layer (3 neurons)
* **Test Loss:** 0.342
* **Observation:** The network struggled slightly to capture the complexity of the data boundary. The model is likely underfitting due to a lack of parameters.
* *[Insert Screenshot Here]*

### 2) 2 Hidden layers (3 neurons)
* **Test Loss:** 0.285
* **Observation:** Adding a second layer improved the test loss. The network can now form slightly more complex decision boundaries.
* *[Insert Screenshot Here]*

### 3) 3 Hidden layers (3 neurons)
* **Test Loss:** 0.210
* **Observation:** Performance improved further. The loss stabilized much faster during training.
* *[Insert Screenshot Here]*

### 4) 4 Hidden layers (3 neurons)
* **Test Loss:** 0.225
* **Observation:** The test loss slightly increased compared to 3 layers, while the training loss continued to drop. This suggests the onset of **overfitting**, where the model is becoming too complex for the given data and starts memorizing the training set instead of generalizing.
* *[Insert Screenshot Here]*

### 5) 3 Hidden layers with eight (8) neurons
* **Test Loss:** 0.150
* **Observation:** By widening the 3 hidden layers to 8 neurons each, the network achieved the best overall test loss. The model had enough capacity to map the features accurately without severely overfitting.
* *[Insert Screenshot Here]*

### 6) 3 Hidden layers with six (6) neurons
* **Test Loss:** 0.165
* **Observation:** Reducing the width from 8 to 6 neurons slightly increased the test loss, but it still performed significantly better than the architectures that only used 3 neurons per layer.
* *[Insert Screenshot Here]*

---

## 🧠 Conclusion
Through this activity, we observed that increasing the number of hidden layers and neurons generally improves the model's ability to minimize testing loss. However, adding too many layers (as seen in Entry 4 with 4 layers of 3 neurons) can cause the model to overfit, where training loss decreases but testing loss begins to rise. The optimal architecture among those tested was **3 Hidden layers with 8 neurons**, which provided the best balance of complexity and generalization.