<h2 align="center">
  <br>
  <a href="https://github.com/mrl-hsl"><img src="https://github.com/Awrsha/MRL-HSL-Humanoid-Robot-Projects/assets/89135083/be030efa-3400-432b-9e76-376f071daadf" alt="Melanoma" width="400"></a>
  <br>
  <b><h4 align="center">.:: Skin Cancer Detection using Deep Learning ::.</h4></b>
  <br>
</h2>

## Overview
This project aims to develop a deep learning model for the detection of skin cancer from dermoscopic images. The model utilizes convolutional neural networks (CNNs), specifically the ResNet50 architecture, to classify images into two classes: benign and malignant.

## Dataset
The dataset used in this project is the Skin Cancer dataset, obtained from [Kaggle](https://www.kaggle.com/amirmohammadparvizi/skin-canser-b584m584). It consists of dermoscopic images of skin lesions, categorized into benign and malignant classes.

## Project Structure
- `data/`
  - `train/`: Training images divided into benign and malignant classes.
  - `validation/`: Validation images for model evaluation.
  - `test/`: Test images for final model evaluation.
- `model_version_*_log.csv`: CSV files containing training logs for each model version.
- `model_version_*.h5`: Saved weights of each trained model version.
- `resNet50_V3.h5`: Final trained model.

## Usage
1. **Setup**: Install the necessary libraries and download the dataset from Kaggle.
2. **Preprocessing**: Balance the dataset and divide it into training, validation, and test sets.
3. **Modeling**: Train the model using the ResNet50 architecture, repeating the process 6 times to account for variability.
4. **Evaluation**: Evaluate the model on the test set and analyze performance metrics such as accuracy, precision, recall, specificity, and sensitivity.
5. **Testing**: Test the final model on unseen data.

## Results
- The final model achieved an accuracy of 74% on the test set.
- Precision: 0.76
- Recall (Sensitivity): 0.71
- Specificity: 0.75

## Future Work
- Implement techniques such as SMOTE and data augmentation to improve model performance.
- Experiment with more complex architectures and ensemble methods.
- Continuously monitor and update the model to improve its accuracy and generalization.

## Contributors
* Alphabetically:
  - [Amie Mohammad Parvizi](https://github.com/awrsha)
  - [Hossein Karimi](https://github.com/)
  - [Mohammad Hossein Hashemi](https://github.com/MHosseinHashemi)

## License
This project is licensed under the [License](https://github.com/MHosseinHashemi/Skin_Cancer#Apache-2.0-1-ov-file).
