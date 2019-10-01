import sys
import datetime
import time
import serial
import datetime
import os
import csv
import time
import matplotlib.patches as mpatches
# from getmac import get_mac_address
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from mintsXU4 import mintsVisual as mV
from mintsXU4 import mintsDefinitions as mD
from matplotlib import style
import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


dataFolder = mD.dataFolder
macAddress = mD.macAddress

plt.style.use('ggplot')

my_dpi=96
fig = plt.figure(figsize=(800/my_dpi, 450/my_dpi), dpi=my_dpi)
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)


def main():
    ani = animation.FuncAnimation(fig, animateOPCN3, interval=500)
    manager = plt.get_current_fig_manager()
    manager.window.showMaximized()
    plt.show()


def animateOPCN3(i):
    # try:
        SensorName ="OPCN3"
        OPCN3  ,validOPCN3     = mV.readJSONLatestAll("OPCN3")
        binCountsIn = []
        #
        # BME280 ,validBME280    = mV.readJSONLatestAll("BME280")
        # print(BME280)

        if(validOPCN3):
            dateTimeOPCN3  = OPCN3['dateTime']
            binCountsIn = [ float(OPCN3['binCount0']), \
                                  float(OPCN3['binCount1']), \
                                  float(OPCN3['binCount2']), \
                                  float(OPCN3['binCount3']), \
                                  float(OPCN3['binCount4']), \
                                  float(OPCN3['binCount5']), \
                                  float(OPCN3['binCount6']), \
                                  float(OPCN3['binCount7']), \
                                  float(OPCN3['binCount8']), \
                                  float(OPCN3['binCount9']), \
                                  float(OPCN3['binCount10']), \
                                  float(OPCN3['binCount11']), \
                                  float(OPCN3['binCount12']), \
                                  float(OPCN3['binCount13']), \
                                  float(OPCN3['binCount14']), \
                                  float(OPCN3['binCount15']), \
                                  float(OPCN3['binCount16']), \
                                  float(OPCN3['binCount17']), \
                                  float(OPCN3['binCount18']), \
                                  float(OPCN3['binCount19']), \
                                  float(OPCN3['binCount20']), \
                                  float(OPCN3['binCount21']), \
                                  float(OPCN3['binCount22']), \
                                  float(OPCN3['binCount23']), \
                                  ]
            pm1In   = str(OPCN3['pm1']).rjust(7," ")
            pm2_5In = str(OPCN3['pm2_5']).rjust(7," ")
            pm10In  = str(OPCN3['pm10']).rjust(7," ")

            # dateTimeBME280  = BME280['dateTime']
            #
            # temperature = str(BME280['temperature']).rjust(7," ")
            # pressure    = str(BME280['pressure']).rjust(7," ")
            # humidity    = str(BME280['humidity']).rjust(7," ")

            dateTimePatchOPCN3 = mpatches.Patch(color='black',label="Update Time(OPCN3): " + str(dateTimeOPCN3))

            pm1Patch    = mpatches.Patch(color='blue', label="OPCN3 PM1    :"+ str(pm1In))
            pm2_5Patch   = mpatches.Patch(color='blue', label="OPCN3 PM2.5 :"+ str(pm2_5In))
            pm10Patch     = mpatches.Patch(color='blue', label="OPCN3 PM10  :"+ str(pm10In))
            bluePatch    = mpatches.Patch(color='blue', label="OPCN3 PM1    :"+ str(pm1In))
            #
            # dateTimePatchBME280 = mpatches.Patch(color='black',label="Update Time(BME280): " + str(dateTimeBME280))
            # temperaturePatch    = mpatches.Patch(color='blue',label="BME280 temperature :"+ str(temperature))
            # humidityPatch       = mpatches.Patch(color='blue',label="BME280 pressure  :"+ str(pressure))
            # pressurPatch        = mpatches.Patch(color='blue',label="BME280 humidity:"+ str(humidity))

            legendsIn     = [dateTimePatchOPCN3,pm1Patch,pm2_5Patch,pm10Patch]

            print("----------------------")
            print("dateTime OPCN3: " + str(dateTimeOPCN3))
            print("pm1:   " + str(pm1In))
            print("pm2_5: " + str(pm2_5In))
            print("pm10:  " + str(pm10In))
            #
            # print("dateTime BME280: " + str(dateTimeBME280))
            # print("temperature: " + str(humidity))
            # print("pressure: " + str(pressure))
            # print("humidty:  " + str(humidity))
            # print("----------------------")
            #
            boundriesIn =  [0.35,0.46,0.66,1.0,1.3,1.7,2.3,3.0,4.0,5.2,\
                                6.5,8.0,10.0,12.0,14.0,16.0,18.0,20.0,22.0,25.0,\
                                28.0,31.0,34.0,37.0,40]

            diametorsInPre = boundriesIn[:-1] + np.diff(boundriesIn)/2
            diametorsInPre2= []
            for x in diametorsInPre:
                diametorsInPre2.append(round(x,2))


            diametorsIn = tuple(diametorsInPre2)

            xData  = np.linspace(1,24,24)
            ax1.clear()
            ax1.bar(xData, binCountsIn, align='center', alpha=0.8,color="blue")
            ax1.set_xticks(xData)
            ax1.set_xticklabels(diametorsIn,rotation='vertical')
            ax1.set_yscale('log')
            ax1.set_ylabel("Bin Counts ")
            ax1.set_xlabel("Particle Diametors (" +u"\u03bcm"+")")
            ax1.set_title("Particle Distribution Data(OPCN3)" )
            ax1.legend(handles=legendsIn)
    #
            ax2.clear()
            ax2.bar(xData, binCountsIn, align='center', alpha=0.8,color="blue")
            ax2.set_xticks(xData)
            ax2.set_xticklabels(diametorsIn,rotation='vertical')
            ax2.set_yscale('log')
            ax2.set_ylabel("Bin Counts ")
            ax2.set_xlabel("Particle Diametors (" +u"\u03bcm"+")")
            ax2.set_title("Particle Distribution Data(OPCN3)" )
            ax2.legend(handles=legendsIn)

    # except KeyboardInterrupt:
    #     print("-- MINTS QUITING --")
    #     ax1.close()
    # except:
    #     pass

if __name__ == '__main__':
  main()
