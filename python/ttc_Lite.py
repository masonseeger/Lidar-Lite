from lidar_lite import Lidar_Lite
from time import time as timer
lidar = Lidar_Lite()
connected = lidar.connect(1)

class Lite_TTC():

    def init(self):
        self.lidar = Lidar_Lite()
        if connected < -1:
            print ("Not Connected")

    def main():

        start_time = timer()
        current_distance = lidar.getDistance()/100
        while True:
            previous_distance = current_distance
            prev_time = start_time
            start_time = timer()
            current_distance = lidar.getDistance()/100
            ttc(prev_time, start_time, current_distance, previous_distance)


        def ttc(prev_t, start_t, current_d, prev_d):
            elapsed_time = start_t-prev_t
            #print(elapsed_time)
            distance_moved = prev_d-current_d
            #print(distance_moved)
            if(distance_moved>.035 or distance_moved<-.035):
                velocity = distance_moved/elapsed_time
                if (velocity>0):
                    current_ttc = current_d/velocity
                    print("Current ttc is %d seconds; speed is %d mps..." % (current_ttc, velocity))
            else:
                print("there is no current ttc available: Object is not moving or is moving away...")

if __name__ == '__main__':
    main()
