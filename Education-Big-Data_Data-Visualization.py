import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 讀取用戶上傳的 CSV 檔案
file_path = r'D:\Desktop\校務\114\教育大數據\user_data_re.csv'
df = pd.read_csv(file_path)

# 檢視前幾行數據
df.head()


# 設定 Seaborn 主題
sns.set(style="whitegrid")

# 數據摘要
summary = df.describe()

# 繪製科目分數分佈圖
plt.figure(figsize=(12, 6))
for i, subject in enumerate(['chinese_score', 'math_score', 'english_score'], 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[subject], bins=10, kde=True, color=sns.color_palette("Set2")[i-1])
    plt.title(f'{subject.replace("_", " ").title()} Distribution')
    plt.xlabel('Score')
    plt.ylabel('Count')
plt.tight_layout()
plt.show()

summary
