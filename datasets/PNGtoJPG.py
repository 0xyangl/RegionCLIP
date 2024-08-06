import os
from PIL import Image

# 定義來源文件夾和目標文件夾
source_folder = '/home/yangl/RegionCLIP/datasets/PngPIC'
target_folder = '/home/yangl/RegionCLIP/datasets/custom_images'

# 確保目標文件夾存在，若不存在則創建
os.makedirs(target_folder, exist_ok=True)

# 遍歷來源文件夾中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.png'):
        # 獲取完整的文件路徑
        png_image_path = os.path.join(source_folder, filename)
        # 定義目標 JPG 文件路徑
        jpg_image_path = os.path.join(target_folder, filename.replace('.png', '.jpg'))

        # 打開並轉換圖像
        with Image.open(png_image_path) as img:
            rgb_img = img.convert('RGB')
            rgb_img.save(jpg_image_path, 'JPEG')

        print(f"Converted {filename} to JPG and saved at {jpg_image_path}")

print("All PNG files have been converted to JPG.")
