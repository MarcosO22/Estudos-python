medida = float(input('uma distancia em metros: '))
cm = medida * 100
mm = medida * 1000
hm = medida / 2
dam = medida / 10
dm = medida * 10
print("a medida de {}m corresponde a {}cm, {}mm, {}hm, {}dam, {}dm.".format(medida,cm,mm, hm, dam, dm))