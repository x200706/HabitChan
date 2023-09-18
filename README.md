# 習慣醬！v1.0.0
一個於Python環境執行的習慣紀錄程式，推薦您使用Replit fork本專案讓它可以在手機APP跟電腦瀏覽器都能運行，方便您隨時可以完成一天的習慣檢視

***
## 注意事項
1. 最近太忙還沒寫輸入檢查，不乖乖輸入正確代號或輸入重複代號，程式或結果都會壞掉喔QQ
2. Replit環境變數上鎖功能還沒製作

***
## 運行環境
- Python 3
- Pandas 2.1.0，沒有的話在程式目錄使用Windows命令列或Linux終端機執行：
  ```shell
  pip install -r requirements.txt
  ```

***
## 使用教學
1. 先準備`habit.csv`放到與`main.py`同層，格式如下：
```
代號, 習慣
A, 健康飲食
B, 打掃房間
C, 打球
```
2. 準備另個檔案`result.csv`放到與`main.py`同層，格式如下：
```
代號,積分
A,0
B,0
C,0
```
代號就是對應`habit.csv`的習慣，之後會做為關聯鍵，所以要保持一致
>有點土炮，會這麼設計是想說之後匯入舊有資料方便^^"

3. 在Windows命令列或Linux終端機cd到本專案目錄輸入：
```shell
python main.py
```
如果是fork到Replit按`Run`就可以運行了

4. 每天照著指示輸入有達成習慣的代號即可，目前功能有：
    - 計算總積分（公式為`所有習慣積分加總`）
    - 計算好寶寶百分比（公式為`所有習慣積分加總/好寶寶指數`，好寶寶指數公式為`開始計算習慣天數*習慣總數`）