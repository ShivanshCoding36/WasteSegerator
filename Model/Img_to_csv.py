import cv2
import pandas as pd
import os

# Define folder paths for classes
data_folder = r'C:\Users\Sivansh\OneDrive\Desktop\ML\waste segerator\TEST'
class_folders = {'O': 0, 'R': 1}  # Mapping class names to labels

# Initialize list to store image data and labels
data = []

# Loop through each class folder
i = 0
error_ = 0
for class_name, label in class_folders.items():
    class_folder_path = os.path.join(data_folder, class_name)
    for image_name in os.listdir(class_folder_path):
        try:
            image_path = os.path.join(class_folder_path, image_name)
            
            # Read and resize image (e.g., to 28x28 for simplicity)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            image = cv2.resize(image, (112, 112))  # Adjust size if needed
            
            # Flatten the image to a 1D array and add label at the end
            image_flatten = image.flatten()
            data.append([label] + list(image_flatten))  # Add label as the first column
        except Exception as e:
            error_+=1
            pass
        print(i)
        i+=1

print('Errors : ',error_)
# Convert to DataFrame and save to CSV
print('1')

columns = ['label'] + [f'pixel_{i}' for i in range(112*112)]
print('2')
df = pd.DataFrame(data, columns=columns)
print('3')
df.to_csv('test_data.csv', index=False)
print('4')
