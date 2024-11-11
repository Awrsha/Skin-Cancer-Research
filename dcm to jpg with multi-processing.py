import os
import pydicom
from PIL import Image
import numpy as np
from multiprocessing import Pool, cpu_count

def convert_dcm_to_jpg(dcm_path):
    try:
        ds = pydicom.dcmread(dcm_path)
        image_array = ds.pixel_array
        
        image_array = (image_array / image_array.max()) * 255.0
        image_array = image_array.astype(np.uint8)
        
        image = Image.fromarray(image_array)
        
        jpg_path = dcm_path.replace('.dcm', '.jpg')
        image.save(jpg_path, 'JPEG')
        
        os.remove(dcm_path)
        
        return jpg_path
    except Exception as e:
        print(f"Error converting {dcm_path}: {e}")
        return None

def process_folder(folder_path):
    dcm_files = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.dcm')]
    for dcm_file in dcm_files:
        convert_dcm_to_jpg(dcm_file)

def main():
    base_folder = r"C:\Users\pc\Desktop\iaaa-mri-train\data"
    subfolders = [os.path.join(base_folder, f) for f in os.listdir(base_folder) if os.path.isdir(os.path.join(base_folder, f))]
    
    pool = Pool(cpu_count() - 1)
    pool.map(process_folder, subfolders)
    
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()