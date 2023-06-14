import pandas as pd
import matplotlib as plt

#各人の予定リスト,0が欠席1が出席可
#リストは[[月～金の10:00のコマ],[月～金の13:00のコマ],[月～金の15:00のコマ]]
#B4
p11=[[0,0,0,1,1],[0,0,0,1,1],[0,0,1,1,1]]
p12=[[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
p13=[[1,1,1,1,0],[1,1,1,1,0],[1,1,1,1,0]]
p14=[[0,0,0,0,0],[1,1,1,1,1],[1,1,1,1,1]]

#M1
p22=[[0,0,0,0,0],[1,0,1,1,1],[1,0,1,1,1]]
p21=[[0,0,0,0,0],[1,0,1,1,1],[1,0,1,1,1]]
p23=[[0,0,0,0,0],[1,0,1,1,1],[1,0,1,1,1]]
p24=[[0,0,0,0,0],[0,0,1,1,1],[1,0,1,1,0]]
p25=[[0,0,0,0,0],[1,0,1,1,1],[1,0,1,1,1]]

#M2
p31=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
p32=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
p33=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

p44=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
p41=[[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]

#Pro
p91=[[1,1,1,1,1],[1,0,0,1,1],[1,0,0,1,1]]
p92=[[1,1,1,1,1],[1,0,0,1,0],[1,0,0,1,0]]
p93=[[0,1,1,1,1],[0,1,1,1,1],[0,1,1,0,0]]

#各人のリストを格納
PL=[p11,p12,p13,p14,p21,p22,p23,p24,p25,p31,p32,p33,p44,p41,p91,p92,p93]
#人のリスト（名簿）実際に名前にすると良いかと
P=['P11','P12','P13','P14','P21','P22','P23','P24','P25','P31','P32','P33','P44','P41','P91','P92','P93']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#各ゼミの参加者リスト（上のリストと表記を合わせる）
c1=['P11','P12','P13','P14','P93']#B4Gross
c2=['P21','P22','P23','P24','P91']#M1Peskin
c3=['P11','P12','P13','P14','P21','P24','P92']#cosmology
c4=['P11','P12','P13','P14','P21','P22','P23','P24','P25','P31','P32','P33','P44','P41','P91','P92']

#各ゼミのリストを格納
CL=[c1,c2,c3,c4]
#各ゼミのリスト（名簿）最終的な日程表に記載されるゼミの名前
C=['c1','c2','c3','c4']
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#来れる人を追加する各日のリスト
d11=[]#月曜10~12
d21=[]#月曜13~15
d31=[]#月曜15~17

d12=[]#火曜10~12
d22=[]#火曜13~15
d32=[]#火曜15~17

d13=[]#水曜10~12
d23=[]#水曜13~15
d33=[]#水曜15~17

d14=[]#木曜10~12
d24=[]#木曜13~15
d34=[]#木曜15~17

d15=[]#金曜10~12
d25=[]#金曜13~15
d35=[]#金曜15~17

#カレンダー
cal=[[d11,d12,d13,d14,d15],[d21,d22,d23,d24,d25],[d31,d32,d33,d34,d35]]

#可能なゼミを追加する各日のリスト
D11=['0']#月曜10~12
D21=['0']#月曜13~15
D31=['0']#月曜15~17

D12=['0']#火曜10~12
D22=['0']#火曜13~15
D32=['0']#火曜15~17

D13=['0']#水曜10~12
D23=['0']#水曜13~15
D33=['0']#水曜15~17

D14=['0']#木曜10~12
D24=['0']#木曜13~15
D34=['0']#木曜15~17

D15=['0']#金曜10~12
D25=['0']#金曜13~15
D35=['0']#金曜15~17

#カレンダー
CAL=[[D11,D12,D13,D14,D15],[D21,D22,D23,D24,D25],[D31,D32,D33,D34,D35]]
#候補カレンダー
cancal=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#各関数定義

#1人について空き時間をリストに追加
def epad(a):
    for i in range(5):
        for j in range(3):
            if(PL[a][j][i]==1):
                cal[j][i].append(P[a])
                
#epadを全員で回す
def roopepad():
    for a in range(len(P)):
        epad(a)
        
#リスト包含精査
def list_check1(list1, list2):
    count = 0
    for element in list1:
        if element in list2:
            count += 1
        if len(list1) == count:
            return True
    return False

#1つのゼミについてカレンダーの可能な日程に追加    
def ecad(a):
    for i in range(5):
        for j in range(3):
            if(list_check1(CL[a],cal[j][i])):
                CAL[j][i].append(C[a])

#ecadを全ゼミで回す
def roopecad():
    for a in range(len(CL)):
        ecad(a)
    
roopepad()
roopecad()
#ここまでの実行で各コマで可能なゼミのカレンダー
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#各日程候補の表を出力
def prifig():
    can1=[cancal[0],cancal[1],cancal[2],cancal[3],cancal[4]]
    can2=[cancal[5],cancal[6],cancal[7],cancal[8],cancal[9]]
    can3=[cancal[10],cancal[11],cancal[12],cancal[13],cancal[14]]

    df=pd.DataFrame([can1,can2,can3],index=['10~12','13~15','15~17'],columns=['Mo','Tu','We','Th','Fr']) 
    df
    print(df)

#各日程で開講可能なゼミ全て入れた表を出力
def prifig2():
    df=pd.DataFrame(CAL,index=['10~12','13~15','15~17'],columns=['Mo','Tu','We','Th','Fr'])
    df
    print(df)
    
#matplotlibを用いた表の出力（うまくいかない）
def pritable():
    fig=plt.figure()
    ax1=fig.add_subplot(111)
    can1=['10~12',cancal[0],cancal[1],cancal[2],cancal[3],cancal[4]]
    can2=['13~15',cancal[5],cancal[6],cancal[7],cancal[8],cancal[9]]
    can3=['15~17',cancal[10],cancal[11],cancal[12],cancal[13],cancal[14]]
    can=[can1,can2,can3]
    col=["候補","Mon","Tues","Wed","Thurs","Fri"]
    ax1.axis('off')
    ax1.table(cellText=can,colLabels=col)
    fig.tight_layout()
    plt.show()
    
def pritable2():
        fig=plt.figure()
        ax1=fig.add_subplot(111)
        col=["Mon","Tues","Wed","Thurs","Fri"]
        ax1.axis('off')
        ax1.table(cellText=CAL,colLabels=col)
        fig.tight_layout()
        plt.show()
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#カレンダーの候補を作成、表示
def mkcal():
    tnc=0
    for a in range(len(CAL[0][0])):
        cancal[0]=CAL[0][0][a]
        for b in range(len(CAL[0][1])):
            cancal[1]=CAL[0][1][b]
            for c in range(len(CAL[0][2])):
                cancal[2]=CAL[0][2][c]
                for d in range(len(CAL[0][3])):
                    cancal[3]=CAL[0][3][d]
                    for e in range(len(CAL[0][4])):
                        cancal[4]=CAL[0][4][e]
                        for f in range(len(CAL[1][0])):
                            cancal[5]=CAL[1][0][f]
                            for g in range(len(CAL[1][1])):
                                cancal[6]=CAL[1][1][g]
                                for h in range(len(CAL[1][2])):
                                    cancal[7]=CAL[1][2][h]
                                    for i in range(len(CAL[1][3])):
                                        cancal[8]=CAL[1][3][i]
                                        for j in range(len(CAL[1][4])):
                                            cancal[9]=CAL[1][4][j]
                                            for k in range(len(CAL[2][0])):
                                                cancal[10]=CAL[2][0][k]
                                                for l in range(len(CAL[2][1])):
                                                    cancal[11]=CAL[2][1][l]
                                                    for m in range(len(CAL[2][2])):
                                                        cancal[12]=CAL[2][2][m]
                                                        for n in range(len(CAL[2][3])):
                                                            cancal[13]=CAL[2][3][n]
                                                            for o in range(len(CAL[2][4])):
                                                                cancal[14]=CAL[2][4][o]
                                                                if(list_check1(C,cancal)):  #全ゼミが開催できるもののみ
                                                                    for z in C:
                                                                        nc=cancal.count(z)
                                                                        tnc=tnc+nc
                                                                    if(tnc==len(C)):  #各ゼミが1回ずつ開催するもののみ
                                                                        prifig()
                                                                    else:
                                                                        pass
                                                                    tnc=0
                                                                else:
                                                                    pass
            
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ 
mkcal()
prifig2()



#問題点
#今までと同じコマに開講できそうなゼミを優先して同じコマに入れる思考は難しい
#毎回ファイルに各人の予定を記入しなければならず、一人の人がそれを行う必要がある
#表が見ずらい

#改善
#ファイルへの書き込みはGithubを用いればいけそう、より実用的にするにはwebやappの開発が必要
#ゼミが開講出来ない場合は開講できないゼミを列挙したうえで、その他のゼミの予定表を描くようにする
#➡185のifの分岐で194のelseのパートに書き足せばよい
#表はmatplotlibで作る（画像ファイルが何個も作られる恐れあり）