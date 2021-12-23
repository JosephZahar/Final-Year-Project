import matplotlib.pyplot as plt
import pandas as pd

Random_motion = pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/Random Motion Cancer/Random Motion Cancer.xlsx')
wiggle_move = pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/wiggle + move Cancer /wiggle  +  move.xlsx')
Flock_motion = pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/Flock Cancer cells /Flock Motion.xlsx')
move = pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/move Cancer cells /Search Dominated Motion of 50 Nanobots.xlsx')
floor = pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/Floor/Floor.xlsx')
floor_speed =pd.read_excel(r'/Users/macbookpro/Desktop/DEN318 -            Third Year Project (Beng:Meng) - 2020:21/Algorithms Plots/Floor/Floor 2.xlsx')

fonttype = {'fontname': 'Times New Roman'}
fig = plt.figure()
ax1 = plt.axes()
ax1.plot(Random_motion['x 50'], Random_motion['y 50'], color='crimson')
ax1.plot(Random_motion['x 100'], Random_motion['y 100'], color='mediumblue')
ax1.plot(Random_motion['x 150'], Random_motion['y 150'], color='yellowgreen')
ax1.plot(Random_motion['x 200'], Random_motion['y 200'], color='darkgoldenrod')
plt.rcParams['figure.dpi'] = 360
ax1.set_xlim([0, 1250])
ax1.set_title('Random Motion of Nanobots', fontsize=13, **fonttype, weight="bold")
ax1.set_ylabel('Cancer Cells', fontsize=13, **fonttype)
ax1.set_xlabel('Time', fontsize=13, **fonttype)
ax1.legend(['50 Nanobots', '100 Nanobots', '150 Nanobots', '200 Nanobots'],
           loc='upper right', borderaxespad=0., prop={"size": 10, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
#plt.show()

fig = plt.figure()
ax1 = plt.axes()
ax1.plot(floor['x 10'], floor['y 10'])
ax1.plot(floor['x 20'], floor['y 20'])
ax1.plot(floor['x 30'], floor['y 30'])
ax1.plot(floor['x 40'], floor['y 40'])
ax1.plot(floor['x 50'], floor['y 50'])
plt.rcParams['figure.dpi'] = 360
ax1.set_xlim([0, 700])
ax1.set_ylabel('Area of Contaminated Floor', fontsize=13, **fonttype)
ax1.set_xlabel('Time', fontsize=13, **fonttype)
ax1.legend(['10 robots', '20 robots', '30 robots', '40 robots','50 robots'],
           loc='upper right', borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax1.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax1.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.savefig('Floor Decontamination Algorithm.png')

fig = plt.figure()
ax2 = plt.axes()
ax2.plot(floor_speed['x 0.2'], floor_speed['y 0.2'])
ax2.plot(floor_speed['x 0.3'], floor_speed['y 0.4'])
ax2.plot(floor_speed['x 0.5'], floor_speed['y 0.6'])
ax2.plot(floor_speed['x 0.8'], floor_speed['y 0.8'])
ax2.plot(floor_speed['x 1'], floor_speed['y 1'])
plt.rcParams['figure.dpi'] = 360
ax2.set_xlim([0, 850])
ax2.set_ylabel('Area of Contaminated Floor', fontsize=13, **fonttype)
ax2.set_xlabel('Time', fontsize=13, **fonttype)
ax2.legend([ '0.2 robot-speed', '0.3 robot-speed', '0.5 robot-speed', '0.8 robot-speed', '1 robot-speed'],
           loc='upper right', borderaxespad=0., prop={"size": 12, "family": 'Times New Roman'})
for tick in ax2.get_xticklabels():
    tick.set_fontname("Times New Roman")
for tick in ax2.get_yticklabels():
    tick.set_fontname("Times New Roman")
plt.savefig('Floor speed.png')


def Cancerplots(n, t1, t2, t3, t4):
    fig = plt.figure(figsize=([35,8]))
    ax1 = plt.subplot(141)
    ax1.plot(wiggle_move['x ' + n + ' 100 100'], wiggle_move['y ' + n + ' 100 100'], color='crimson')
    ax1.plot(wiggle_move['x ' + n + ' 10 100'], wiggle_move['y ' + n + ' 10 100'], color='mediumblue')
    ax1.plot(wiggle_move['x ' + n + ' 10 30'], wiggle_move['y ' + n + ' 10 30'], color='limegreen')
    ax1.plot(wiggle_move['x ' + n + ' 100 30'], wiggle_move['y ' + n + ' 100 30'], color='gold')
    plt.rcParams['figure.dpi'] = 360
    ax1.set_xlim([0, t1])
    ax1.set_title('Flock Dominated Motion of ' + n + ' Nanobots', fontsize=13, **fonttype, weight="bold")
    ax1.set_ylabel('Cancer Cells', fontsize=13, **fonttype)
    ax1.set_xlabel('Time', fontsize=13, **fonttype)
    for tick in ax1.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax1.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax2 = plt.subplot(142)
    ax2.plot(Flock_motion['x ' + n + ' 100 100'], Flock_motion['y ' + n + ' 100 100'], color='crimson')
    ax2.plot(Flock_motion['x ' + n + ' 10 100'], Flock_motion['y ' + n + ' 10 100'], color='mediumblue')
    ax2.plot(Flock_motion['x ' + n + ' 10 30'], Flock_motion['y ' + n + ' 10 30'], color='limegreen')
    ax2.plot(Flock_motion['x ' + n + ' 100 30'], Flock_motion['y ' + n + ' 100 30'], color='gold')
    plt.rcParams['figure.dpi'] = 360
    ax2.set_xlim([0, t2])
    ax2.set_title('Flock Motion of ' + n + ' Nanobots', fontsize=13, **fonttype, weight="bold")
    ax2.set_ylabel('Cancer Cells', fontsize=13, **fonttype)
    ax2.set_xlabel('Time', fontsize=13, **fonttype)
    for tick in ax2.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax2.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax3 = plt.subplot(143)
    ax3.plot(move['x ' + n + ' 100 100'], move['y ' + n + ' 100 100'], color='crimson')
    ax3.plot(move['x ' + n + ' 10 100'], move['y ' + n + ' 10 100'], color='mediumblue')
    ax3.plot(move['x ' + n + ' 10 30'], move['y ' + n + ' 10 30'], color='limegreen')
    ax3.plot(move['x ' + n + ' 100 30'], move['y ' + n + ' 100 30'], color='gold')
    plt.rcParams['figure.dpi'] = 360
    ax3.set_xlim([0, t3])
    ax3.set_title('Search Dominated Motion of ' + n + ' Nanobots ', fontsize=13, **fonttype, weight="bold")
    ax3.set_ylabel('Cancer Cells', fontsize=13, **fonttype)
    ax3.set_xlabel('Time', fontsize=13, **fonttype)
    ax3.legend(['100 Nano-vision 100 align-turn', '10 Nano-vision 100 align-turn', '10 Nano-vision 30 align-turn',
                '100 Nano-vision 30 align-turn'],
               loc='upper right', borderaxespad=0., prop={"size": 10, "family": 'Times New Roman'})
    for tick in ax3.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax3.get_yticklabels():
        tick.set_fontname("Times New Roman")

    ax4 = plt.subplot(144)
    ax4.plot(wiggle_move['x ' + n + ' 10 100'], wiggle_move['y ' + n + ' 10 100'], color='steelblue')
    ax4.plot(Flock_motion['x ' + n + ' 10 30'], Flock_motion['y ' + n + ' 10 30'], color='blue')
    ax4.plot(Random_motion['x ' + n], Random_motion['y ' + n], color='dodgerblue')
    ax4.plot(move['x ' + n + ' 10 30'], move['y ' + n + ' 10 30'], color='black')
    plt.rcParams['figure.dpi'] = 360
    ax4.set_xlim([0, t4])
    ax4.set_title('Control Algorithms of ' + n + ' Nanobots ', fontsize=13, **fonttype, weight="bold")
    ax4.set_ylabel('Cancer Cells', fontsize=13, **fonttype)
    ax4.set_xlabel('Time', fontsize=13, **fonttype)
    ax4.legend(['Flock Dominated Motion', 'Flock Motion', 'Random Motion', 'Search Dominated Motion'],
               loc='upper right', borderaxespad=0., prop={"size": 10, "family": 'Times New Roman'})
    for tick in ax4.get_xticklabels():
        tick.set_fontname("Times New Roman")
    for tick in ax4.get_yticklabels():
        tick.set_fontname("Times New Roman")

    plt.tight_layout(pad=10)
    plt.savefig('Control Algorithms of ' + n + ' Nanobots.png')

####Cancerplots('50',3000,1500,500,2000)
###Cancerplots('100',1800,1200,350,1300)
##Cancerplots('150',1400,1000,350,800)
#Cancerplots('200',800,900,300,800)
