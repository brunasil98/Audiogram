
from tensorflow.keras.models import load_model

model_rg = load_model("../Models/NN_RG.h5")
model_lf = load_model("../Models/NN_LF.h5")

def right_ear(a, b, c):
    data = [[a,b,c]]
    pred = model_rg.predict(data)
    pred = pred.reshape((4,1))
    pred = pred + (5-pred%5)
    r = [pred[0][0],pred[1][0],data[0][0],pred[2][0],data[0][1],data[0][2],pred[3][0]]
    return r

def left_ear(a, b, c):
    data = [[a,b,c]]
    pred = model_lf.predict(data)
    pred = pred.reshape((4,1))
    pred = pred + (5-pred%5)
    r = [pred[0][0],pred[1][0],data[0][0],pred[2][0],data[0][1],data[0][2],pred[3][0]]
    return r

out = True

while out == True:
    ear = input('Choose what ear left or right (l/r):')
    f2 = int(input('dB for 2K frequency:'))
    f4 = int(input('dB for 4K frequency:'))
    f6 = int(input('dB for 6K frequency:'))

    if ear == 'r':
        rs = right_ear(f2,f4,f6)
        print(f'The loss values, in dB, for respective frequncies are: 500k/{rs[0]}  1k/{rs[1]}  2k/{rs[2]}  3k/{rs[3]}  4k/{rs[4]}  6k/{rs[5]}  8k/{rs[6]}')
        

    if ear == 'l':
        rs = left_ear(f2,f4,f6)
        print(f'The loss values, in dB, for respective frequncies are: 500k/{rs[0]}  1k/{rs[1]}  2k/{rs[2]}  3k/{rs[3]}  4k/{rs[4]}  6k/{rs[5]}  8k/{rs[6]}')

    exit = input('To exit, type x, otherwhise, type c:')

    if exit == 'x':
        print('Bye, see you soon!')
        out = False
        
        