import csv
def fun1(start,end,year):
    print(year,"<br>")
    labels = []  # 塞年齡
    unmarried = []  # 未婚
    married = []  # 已婚
    divorce = []  # 離婚
    widowed = []  # 喪偶
    #plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
    #plt.rcParams['axes.unicode_minus'] = False
    with open('宜蘭婚姻比例6.csv', 'r', encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        x = 0
        for row in read:
            if x >= start and x <= end:
                if row[1] != "":
                    labels.append(row[1])
                    unmarried.append(int(row[5]))
                    married.append(int(row[8]))
                    divorce.append(int(row[11]))
                    widowed.append(int(row[14]))
                    #print(row[1], row[5], row[8], row[11], row[14],"<br>")
            x = x + 1

def funAll(start,end,year):
    print("<h1>",year,"</h1>","<br>")
    global labels # 塞年齡
    global unmarried  # 未婚
    global married  # 已婚
    global divorce # 離婚
    global widowed  # 喪偶
    #plt.rcParams['font.sans-serif'] = ['SimSun']  # 步驟一（替換sans-serif字型）
    #plt.rcParams['axes.unicode_minus'] = False
    with open('宜蘭婚姻比例6.csv', 'r', encoding="utf-8") as fin:
        read = csv.reader(fin, delimiter=',')
        x = 0
        for row in read:
            if x >= start and x <= end:
                if row[1] != "":
                    labels.append(row[1])
                    unmarried.append(int(row[5]))
                    married.append(int(row[8]))
                    divorce.append(int(row[11]))
                    widowed.append(int(row[14]))
                    #print(row[1], row[5], row[8], row[11], row[14],"<br>")
                #if x==21 or x== 42 or x==63 or x==84 or x==105 or x==126 or x== 147 or x==168 or x==189 or x==210 or x==231 or x==252 or x==273 or x==294 or x==315 or x==336 or x==357:
                    #print("<hr>")
            x = x + 1




#year="1999"
import sys

labels = []  # 塞年齡
unmarried = []  # 未婚
married = []  # 已婚
divorce = []  # 離婚
widowed = []  # 喪偶


# print('參數:', len(sys.argv))
# print('參數列表:', str(sys.argv))
year="0"

if len(sys.argv)>1:
    year=sys.argv[1]

if year=="0":
    funAll(1,377,"1999-2016年")

else:
    dic1={"1999":{"val1":1,"val2":20},
          "2000":{"val1": 22, "val2": 41},
          "2001":{"val1": 43, "val2": 62},
          "2002":{"val1": 64, "val2": 84},
          "2003":{"val1": 85, "val2": 104},
          "2004": {"val1": 106, "val2": 125},
          "2005": {"val1": 127, "val2": 146},
          "2006": {"val1": 148, "val2": 167},
          "2007": {"val1": 169, "val2": 188},
          "2008": {"val1": 190, "val2": 209},
          "2009": {"val1": 211, "val2": 230},
          "2010": {"val1": 232, "val2": 251},
          "2011": {"val1": 253, "val2": 272},
          "2012": {"val1": 274, "val2": 293},
          "2013": {"val1": 295, "val2": 314},
          "2014": {"val1": 316, "val2": 335},
          "2015": {"val1": 337, "val2": 356},
          "2016": {"val1": 358, "val2": 377},
          }
    funAll(dic1[year]["val1"],dic1[year]["val2"],year)

data_List=[sum(unmarried),sum(married),sum(divorce),sum(widowed)]
label_List = ['unmarried','married','divorce','widowed']  # 塞年齡

pie_HTML="""
<html>
<header>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.4.0/Chart.min.js"></script>
</header>
<body>

 <canvas id="example" width="400" height="200"></canvas>
  <script>
  	var ctx = document.getElementById( "example" ),
  		example = new Chart(ctx, {
  			// 參數設定[註1]
  			type: "pie", // 圖表類型
  			data: {
  				labels: [label_List], // 標題
  				datasets: [{
  					label: "婚姻狀況", // 標籤
  					data: [data_List], // 資料
  					backgroundColor: [ // 背景色
  					"#FF6666",
  					"#339966",
  					"#3399FF",
                    "#FFA500"
  					],
  					borderWidth: 1 // 外框寬度
  				}]
  			}
  		});
  </script>
</body>
</html>
"""

pie_HTML=pie_HTML.replace('[label_List]',str(label_List))
pie_HTML=pie_HTML.replace('[data_List]',str(data_List))

print(pie_HTML)