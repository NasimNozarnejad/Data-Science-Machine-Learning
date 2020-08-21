import numpy as np
import sys
filename=sys.argv[1]
Data=np.load(filename)
X=Data[:,0]
Y=Data[:,1]
y=lambda a, b : (a*np.sin(X))+b
Q_obs=Y
A=[]
A.append(((max(Q_obs)-min(Q_obs))/2)/2)
A.append(-((max(Q_obs)-min(Q_obs))/2)/2)
L=np.matrix([max(Q_obs),min(Q_obs)])
B=(L.mean())/2
n=0
y0_theory=y(A[0],B)
y1_theory=y(A[1],B)
bestfit=[]
for j in range(2):
    B=(L.mean())/2
    dA=A[j]/2
    dB=B/2
    n=0
    y_theory=y(A[j],B)
    loss=np.sum((y_theory-Q_obs)**2)
    for i in range(10000):
        y_theory1=y(A[j]+dA,B)
        loss1=np.sum((y_theory-Q_obs)**2)
        
        y_theory2=y(A[j],B+dB)
        loss2=np.sum((y_theory2-Q_obs)**2)
        
        y_theory3=y(A[j]+dA,B+dB)
        loss3=np.sum((y_theory3-Q_obs)**2)
        
        INFO=np.matrix([[loss1, loss2, loss3], [A[j]+dA, A[j], A[j]+dA], [B, B+dB, B+dB]])
        MIN_loss=INFO[0].argmin()
        best_loss=INFO[:,MIN_loss]
        
        
        if best_loss[0,0] < loss:
            loss = best_loss[0,0]
            A[j] = best_loss[1,0]
            B = best_loss[2,0]
        else:
            n+=1
        if n > 1:
            dA = dA/5
            dB = dB/5
            n=0
    bestfit.append(loss)

Abest=A[np.matrix(bestfit).argmin()]
print('a is: ' + str(Abest))
print('b is: ' + str(B))
