import os
from PIL import Image

# 定義來源文件夾和目標文件夾
source_folder = '/home/yangl/RegionCLIP/datasets/PhotoWithZone'
target_folder = '/home/yangl/RegionCLIP/datasets/custom_images'

# 確保目標文件夾存在，若不存在則創建
os.makedirs(target_folder, exist_ok=True)

# 遍歷來源文件夾中的所有文件
for filename in os.listdir(source_folder):
    if filename.endswith('.png') or filename.endswith('.jpg'):
        # 忽略包含 Zone.Identifier 的文件
        if 'Zone.Identifier' in filename:
            continue

        # 獲取完整的文件路徑
        image_path = os.path.join(source_folder, filename)
        # 定義目標 JPG 文件路徑（如果是 PNG 文件）
        if filename.endswith('.png'):
            jpg_image_path = os.path.join(target_folder, filename.replace('.png', '.jpg'))
            # 打開並轉換圖像
            with Image.open(image_path) as img:
                rgb_img = img.convert('RGB')
                rgb_img.save(jpg_image_path, 'JPEG')
        else:
            # 直接保存為 JPG 文件
            jpg_image_path = os.path.join(target_folder, filename)
            with Image.open(image_path) as img:
                img.save(jpg_image_path, 'JPEG')

        print(f"Processed {filename} and saved at {jpg_image_path}")

print("All image files have been processed.")
