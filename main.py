import pandas as pd
import os
# 輸入於環境變數設置之密碼

# 載入習慣
file_path = 'habit.csv'
df = pd.read_csv(file_path)
df.columns = df.columns.str.replace(' ', '')  # trim
desired_columns = ['代號', '習慣']
subset_df = df[desired_columns]

# 顯示習慣
print(subset_df)

# 詢問習慣
print('你今天做了那些習慣？')
user_ans = input('請輸入：')

# 檢查輸入

# 異動result.csv
result_path = 'result.csv'
result = pd.read_csv(result_path)
result.columns = result.columns.str.replace(' ', '')  # trim

# 讀取使用者輸入
user_arr = list(user_ans)

for i in range(0, len(user_arr)):
  result.loc[result['代號'] == user_arr[i], '積分'] += 1

output_file_path = 'result.csv'
result.to_csv(output_file_path, index=False)
# 習慣天數+1
day_txt_path = 'day.txt'
if os.path.isfile(day_txt_path):
  f = open(day_txt_path, 'r+')
  day_count_str = f.read()
  last_day_count = int(day_count_str) + 1
  f.seek(0)
  f.write(str(last_day_count))
  f.truncate()
  f.close()
else:
  f = open(day_txt_path, 'w+')
  last_day_count = 1
  f.write(str(last_day_count))
  f.close()
print('=====')
print('總覽')
# 合併兩份csv
merged_df = pd.merge(df, result, on='代號')
desired_columns = ['習慣', '積分']
subset_merged_df = merged_df[desired_columns]
print(subset_merged_df)
# 解讀（用merged_df而非顯示用subset_merged_df）
print('======')
# 開始記錄習慣的天數
print('開始記錄習慣天數：' + str(last_day_count))

# 好寶寶指數perfect_sore=習慣天數*習慣數目
perfect_sore = last_day_count * len(merged_df)

# 所有積分總和
score = merged_df['積分'].sum()
print('所有積分總和：' + str(score))

# 所有積分總和/好寶寶指數=好寶寶百分比
print('好寶寶百分比：' + str(round(score / perfect_sore, 2) * 100) + '%')
