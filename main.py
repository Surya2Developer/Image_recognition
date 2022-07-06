import cv2
import mediapipe as mp
import time
import numpy as np
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
# For static images:
decide = True
count = 0
ptime = 0
close_check = False
open_check = False

def count_open_close(open, close):
    global decide
    global count
    global ptime
    if open == True and close == False and decide == True:
        decide = False
    if open == False and close == True and decide == False:
        decide = True
        count = count + 1
        cTime = time.time()
        frequency = round(1 / (cTime - ptime), 2)
        ptime = cTime
        print(count, frequency, ":Hz")


    else:
        return 0

def open_check_by_distance(keypoints, center):
    def thumb_open_check(keypoints, center):
        d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
        d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
        if d4 > d3:
            return True
        else:
            return False
    def index_open_check(keypoints, center):
        d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
        d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
        d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
        d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
        if d8 > d7 > d6 > d5:
            return True
        else:
            return False
    def middle_open_check(keypoints, center):
        d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
        d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
        d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
        d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
        if d12 > d11 > d10 > d9:
            return True
        else:
            return False
    def ring_open_check(keypoints, center):
        d13 = np.sqrt(np.square(keypoints[13][0] - center[0]) + np.square(keypoints[13][1] - center[1]))
        d14 = np.sqrt(np.square(keypoints[14][0] - center[0]) + np.square(keypoints[14][1] - center[1]))
        d15 = np.sqrt(np.square(keypoints[15][0] - center[0]) + np.square(keypoints[15][1] - center[1]))
        d16 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[16][1] - center[1]))
        if d16 > d15 > d14 > d13:
            return True
        else:
            return False
    def pinky_open_check(keypoints, center):
        d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
        d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
        d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
        d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
        if d20 > d19 > d18 > d17:
            return True
        else:
            return False
    thumb = thumb_open_check(keypoints, center)
    index = index_open_check(keypoints, center)
    middle = middle_open_check(keypoints, center)
    ring = ring_open_check(keypoints, center)
    pinky = pinky_open_check(keypoints, center)
    if thumb == True and index == True and middle == True and ring == True and pinky == True:
        return True
    else:
        return False

def close_check_by_distance(keypoints, center): #tested OK
   d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
   d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   d5 = np.sqrt(np.square(keypoints[5][0] - keypoints[0][0]) + np.square(keypoints[5][1] - keypoints[0][1]))
   d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))

   if d8 < d5 and d12 < d9 and d16 < d13 and d20 < d17 and d4 < d3:
       return True
   else:
       return False

def peace_check_by_distance(center, keypoints):
    def index_open_check(keypoints, center):
        d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
        d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
        d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
        d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
        if d8 > d7 > d6 > d5:
            return True
        else:
            return False

    def middle_open_check(keypoints, center):
        d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
        d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
        d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
        d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
        if d12 > d11 > d10 > d9:
            return True
        else:
            return False

    d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
    d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
    d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
    d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))

    index = index_open_check(keypoints, center)
    middle = middle_open_check(keypoints, center)
    a_5_8 = get_angle(keypoints[5], keypoints[8])
    #if a_5_8 > 340:
    #    a_5_8 = 360 - a_5_8
    a_9_12 = get_angle(keypoints[9], keypoints[12])
    #if a_9_12 > 340:
    #    a_9_12 = 360 - a_9_12
    a_8_0_12 = a_5_8-a_9_12
    #print(a_8_0_12)
    if index == True and middle == True and d13 > d16 and d17 > d20 and a_8_0_12 > 10:
        return True
    else:
        return False

def take_coordinates(coordinates):#この関数は２１点のハンドランドマークを検出する関数
  #print(coordinates) 20 xyz
  if coordinates == None:
    return 0
  keypoints = []
  for data_point in coordinates:
    xyz_datapoints = data_point.landmark
    for xyz in xyz_datapoints:
      X_value = round(xyz.x*10000, 2)
      Y_value = round(xyz.y*10000, 2)
      Z_value = round(xyz.z, 3)
      xy = [X_value,Y_value, Z_value]
      keypoints.append(xy)
    #print("Depth情報:\n 手首:{} 中指先:{} 薬指先:{}".format(keypoints[0][2], keypoints[12][2], keypoints[16][2]))
  return keypoints

def centroid_palm(keypoints): #calculation not correct. Do it again
    if keypoints == 0:
        return 0
    x_bar = (keypoints[0][0] + keypoints[9][0])/2
    x_bar = round(x_bar, 2)
    y_bar = (keypoints[0][1] + keypoints[9][1])/2
    y_bar = round(y_bar, 2)
    return x_bar, y_bar

def distance_center_to_tip(keypoints, center):#手の中心からそれぞれの指先までの距離を求める。
    if keypoints == 0:
        return 0
    d1 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
    d2 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
    d3 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
    d4 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[14][1] - center[1]))
    d5 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
    return round(d1, 1), round(d2, 1), round(d3, 1), round(d4, 1), round(d5, 1)

def get_angle(keypoints, center):#この関数はふたつの点から角度を求める。引数は((x1,y1),(x2,y2)).よってθを求める
    #(x',y')=(x, max-y)
    if keypoints == 0:
        return 0

    center = list(center)
    wrist = list(keypoints)
    wrist[1] = 10000-wrist[1] # y' = max - y
    center[1] = 10000-center[1] # y' = max - y
    Y = center[1]-wrist[1]
    X = center[0]-wrist[0]
    try:
        m = Y/X
    except ZeroDivisionError:
        m = 0
    angle = np.arctan(m)*180/(np.pi)
    if X > 0 and Y < 0:
        angle = angle + 360
    elif X < 0 and Y > 0:
        angle = angle + 180
    elif X < 0 and Y < 0:
        angle = angle + 180
    return round(angle, 1)

def ok_check_by_distance( keypoints, center):
   d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[4][0]) + np.square(keypoints[8][1] - keypoints[4][1]))
   d7 = np.sqrt(np.square(keypoints[4][0] - keypoints[3][0]) + np.square(keypoints[4][1] - keypoints[3][1]))
   def middle_open_check(keypoints, center):
       d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
       d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
       d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
       d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
       if d12 > d11 > d10 > d9:
           return True
       else:
           return False
   def ring_open_check(keypoints, center):
       d13 = np.sqrt(np.square(keypoints[13][0] - center[0]) + np.square(keypoints[13][1] - center[1]))
       d14 = np.sqrt(np.square(keypoints[14][0] - center[0]) + np.square(keypoints[14][1] - center[1]))
       d15 = np.sqrt(np.square(keypoints[15][0] - center[0]) + np.square(keypoints[15][1] - center[1]))
       d16 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[16][1] - center[1]))
       if d16 > d15 > d14 > d13:
           return True
       else:
           return False
   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False
   middle = middle_open_check(keypoints, center)
   ring = ring_open_check(keypoints, center)
   pinky = pinky_open_check(keypoints, center)
   if middle == True and ring == True and pinky == True and d8 < d7:
       return True
   else:
       return False

def kitsune_check_by_distance(center, keypoints):
   def index_open_check(keypoints, center):
       d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
       d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
       d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
       d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
       if d8 > d7 > d6 > d5:
           return True
       else:
           return False
   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False

   d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   index = index_open_check(keypoints, center)
   pinky = pinky_open_check(keypoints, center)

   if index == True and pinky == True and d12 < d9 and d16 < d13:
       return True
   else:
       return False

def a_fingerspell(keypoints, center):
   d5 = np.sqrt(np.square(keypoints[5][0] - keypoints[0][0]) + np.square(keypoints[5][1] - keypoints[0][1]))
   d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
   d0_1 = np.sqrt(np.square(keypoints[0][0] - keypoints[1][0]) + np.square(keypoints[0][1] - keypoints[1][1]))
   d0_2 = np.sqrt(np.square(keypoints[0][0] - keypoints[2][0]) + np.square(keypoints[0][1] - keypoints[2][1]))
   d0_3 = np.sqrt(np.square(keypoints[0][0] - keypoints[3][0]) + np.square(keypoints[0][1] - keypoints[3][1]))
   d0_4 = np.sqrt(np.square(keypoints[0][0] - keypoints[4][0]) + np.square(keypoints[0][1] - keypoints[4][1]))
   d1_2 = np.sqrt(np.square(keypoints[1][0] - keypoints[2][0]) + np.square(keypoints[1][1] - keypoints[2][1]))
   d4_6 = np.sqrt(np.square(keypoints[4][0] - keypoints[6][0]) + np.square(keypoints[4][1] - keypoints[6][1]))
   dc_3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
   dc_4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   a_3_4 = get_angle(keypoints[3], keypoints[4])
   #print(a_3_4)
   if 100>a_3_4>80 and d0_1 < d0_2 < d0_3 < d0_4 and d1_2 > d4_6 and d5 > d8 and d9 > d12 and d13 > d16 and d17 > d20 and dc_4 > dc_3:
       return True
   else:
       return False

def b_fingerspell(keypoints, center):
   def index_open_check(keypoints, center):
       d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
       d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
       d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
       d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
       if d8 > d7 > d6 > d5:
           return True
       else:
           return False
   def middle_open_check(keypoints, center):
       d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
       d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
       d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
       d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
       if d12 > d11 > d10 > d9:
           return True
       else:
           return False
   def ring_open_check(keypoints, center):
       d13 = np.sqrt(np.square(keypoints[13][0] - center[0]) + np.square(keypoints[13][1] - center[1]))
       d14 = np.sqrt(np.square(keypoints[14][0] - center[0]) + np.square(keypoints[14][1] - center[1]))
       d15 = np.sqrt(np.square(keypoints[15][0] - center[0]) + np.square(keypoints[15][1] - center[1]))
       d16 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[16][1] - center[1]))
       if d16 > d15 > d14 > d13:
           return True
       else:
           return False
   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False
   index = index_open_check(keypoints, center)
   middle = middle_open_check(keypoints, center)
   ring = ring_open_check(keypoints, center)
   pinky = pinky_open_check(keypoints, center)

   d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
   d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   a17_20 = get_angle(keypoints[17], keypoints[20])
   a13_16 = get_angle(keypoints[13], keypoints[16])
   a9_12 = get_angle(keypoints[9], keypoints[12])
   a5_8 = get_angle(keypoints[5], keypoints[8])
   #print(a17_20, a13_16, a9_12, a5_8)
   a_max = max(a17_20, a13_16, a9_12, a5_8)
   a_min = min(a17_20, a13_16, a9_12, a5_8)
   if (a_max - a_min) <= 5 and index == True and middle == True and ring == True and pinky == True and d4 < d3:
       return True
   else:
       return False

def c_fingerspell(keypoints, center):
   global open_check
   a_2_4 = get_angle(keypoints[2], keypoints[4])
   a_7_8 = get_angle(keypoints[7], keypoints[8])
   a_11_12 = get_angle(keypoints[11], keypoints[12])
   a_15_16 = get_angle(keypoints[15], keypoints[16])
   a_19_20 = get_angle(keypoints[19], keypoints[20])

   if open_check == True and 210>a_2_4>150 and 200>a_7_8>135 and 200>a_11_12>135 and 200>a_15_16>135 and 200>a_19_20>135:
       return True
   else:
       return False

def d_fingerspell(keypoints, center):
  a_2_3 = get_angle(keypoints[2], keypoints[3])
  a_3_4 = get_angle(keypoints[3], keypoints[4])
  a_5_8 = get_angle(keypoints[5], keypoints[8])
  a_9_10 = get_angle(keypoints[9], keypoints[10])
  a_10_11 = get_angle(keypoints[10], keypoints[11])
  a_13_14 = get_angle(keypoints[13], keypoints[14])
  a_14_15 = get_angle(keypoints[14], keypoints[15])
  a_17_18 = get_angle(keypoints[17], keypoints[18])
  a_18_19 = get_angle(keypoints[18], keypoints[19])
  d_0_10 = np.sqrt(np.square(keypoints[0][0] - keypoints[10][0]) + np.square(keypoints[0][1] - keypoints[10][1]))
  d_0_11 = np.sqrt(np.square(keypoints[0][0] - keypoints[11][0]) + np.square(keypoints[0][1] - keypoints[11][1]))
  d_10_11 = np.sqrt(np.square(keypoints[10][0] - keypoints[11][0]) + np.square(keypoints[10][1] - keypoints[11][1]))
  d_4_10 = np.sqrt(np.square(keypoints[4][0] - keypoints[10][0]) + np.square(keypoints[4][1] - keypoints[10][1]))
  a_2_3_4 = a_3_4 + 180 -a_2_3
  if a_2_3_4 > 180:
      a_2_3_4 = 360 - a_2_3_4
  a_9_10_11 = a_10_11 + 180 - a_9_10
  if a_9_10_11 > 180:
      a_9_10_11 = 360 - a_9_10_11
  a_13_14_15 = a_14_15 + 180 - a_13_14
  if a_13_14_15 > 180:
      a_13_14_15 = 360 - a_13_14_15
  a_17_18_19 = a_18_19 + 180 - a_17_18
  if a_17_18_19 > 180:
      a_17_18_19 = 360 - a_17_18_19
  #print(a_17_18_19, a_13_14_15, a_9_10_11)
  if 100 > a_5_8 > 80 and d_0_10 > d_0_11 and a_9_10_11 < 110 and a_13_14_15 < 110 and a_17_18_19 < 110 and a_2_3_4 < 180 and d_10_11 > d_4_10:
      return True
  else:
      return False

def e_fingerspell(keypoints, center):
   global close_check
   dc_3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
   dc_4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   dc_8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
   dc_12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
   dc_16 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[16][1] - center[1]))
   dc_20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
   d7 = np.sqrt(np.square(keypoints[6][0] - keypoints[0][0]) + np.square(keypoints[6][1] - keypoints[0][1]))
   d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   d11 = np.sqrt(np.square(keypoints[10][0] - keypoints[0][0]) + np.square(keypoints[10][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d15 = np.sqrt(np.square(keypoints[14][0] - keypoints[0][0]) + np.square(keypoints[14][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d19 = np.sqrt(np.square(keypoints[18][0] - keypoints[0][0]) + np.square(keypoints[18][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))

   if close_check == False and  d7 > d8 and d11 > d12 and d15 > d16 and d19 > d20 and dc_4 < dc_3:
       return True
   else:
       return False

def f_fingerspell(keypoints, center):
   d0_3 = np.sqrt(np.square(keypoints[3][0] - keypoints[0][0]) + np.square(keypoints[3][1] - keypoints[0][1]))
   d0_5 = np.sqrt(np.square(keypoints[5][0] - keypoints[0][0]) + np.square(keypoints[5][1] - keypoints[0][1]))
   d0_8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   a_2_4 = get_angle(keypoints[2], keypoints[4])
   a_9_12 = get_angle(keypoints[9], keypoints[12])
   a_4_p_12 = a_2_4 - a_9_12
   def thumb_open_check(keypoints, center):
       d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
       d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
       if d4 > d3:
           return True
       else:
           return False
   def middle_open_check(keypoints, center):
       d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
       d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
       d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
       d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
       if d12 > d11 > d10 > d9:
           return True
       else:
           return False
   def ring_open_check(keypoints, center):
       d13 = np.sqrt(np.square(keypoints[13][0] - center[0]) + np.square(keypoints[13][1] - center[1]))
       d14 = np.sqrt(np.square(keypoints[14][0] - center[0]) + np.square(keypoints[14][1] - center[1]))
       d15 = np.sqrt(np.square(keypoints[15][0] - center[0]) + np.square(keypoints[15][1] - center[1]))
       d16 = np.sqrt(np.square(keypoints[16][0] - center[0]) + np.square(keypoints[16][1] - center[1]))
       if d16 > d15 > d14 > d13:
           return True
       else:
           return False
   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False
   thumb = thumb_open_check(keypoints, center)
   middle = middle_open_check(keypoints, center)
   ring = ring_open_check(keypoints, center)
   pinky = pinky_open_check(keypoints, center)

   if thumb == True and middle == True and ring == True and pinky == True and d0_8 < d0_5 and d0_8 < d0_3 and a_4_p_12 < 30:
       return True
   else:
       return False

def g_fingerspell(keypoints, center):
   def index_open_check(keypoints, center):
       d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
       d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
       d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
       d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
       if d8 > d7 > d6 > d5:
           return True
       else:
           return False
   d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
   d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
   a_5_8 = get_angle(keypoints[5], keypoints[8])
   a_0_c = get_angle(keypoints[0], center)
   index = index_open_check(keypoints, center)
   #print(a_5_8, a_0_c)
   if index == True and d12 < d9 and d16 < d13 and d20 < d17 and d4 < d3 and (20 > a_5_8 or a_5_8 > 340) and 45 > a_0_c:
       return True
   else:
       return False

def h_fingerspell(keypoints, center):
   d_14_3 = np.sqrt(np.square(keypoints[14][0] - keypoints[3][0]) + np.square(keypoints[14][1] - keypoints[3][1]))
   d_14_4 = np.sqrt(np.square(keypoints[14][0] - keypoints[4][0]) + np.square(keypoints[14][1] - keypoints[4][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
   a_5_8 = get_angle(keypoints[5], keypoints[8])
   a_9_12 = get_angle(keypoints[9], keypoints[12])
   #a_max = max(a_5_8, a_9_12)
   #a_min = min(a_5_8, a_9_12)
   #print(a_5_8, a_9_12)
   def index_open_check(keypoints, center):
       d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
       d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
       d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
       d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
       if d8 > d7 > d6 > d5:
           return True
       else:
           return False
   def middle_open_check(keypoints, center):
       d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
       d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
       d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
       d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
       if d12 > d11 > d10 > d9:
           return True
       else:
           return False
   index = index_open_check(keypoints, center)
   middle = middle_open_check(keypoints, center)
   if index == True and middle == True and (340<a_5_8 or a_5_8<20) and (340<a_9_12 or a_9_12<20) and d_14_3 > d_14_4 and d13 > d16 and d17 > d20:
       #print("h")
       return True
   else:
       return False

def i_fingerspell(keypoints, center):
   dc_4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
   dc_6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
   d0_5 = np.sqrt(np.square(keypoints[6][0] - keypoints[0][0]) + np.square(keypoints[6][1] - keypoints[0][1]))
   d0_8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   d0_9 = np.sqrt(np.square(keypoints[10][0] - keypoints[0][0]) + np.square(keypoints[10][1] - keypoints[0][1]))
   d0_12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d0_13 = np.sqrt(np.square(keypoints[14][0] - keypoints[0][0]) + np.square(keypoints[14][1] - keypoints[0][1]))
   d0_16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   a_3_4 = get_angle(keypoints[3], keypoints[4])
   a_17_20 = get_angle(keypoints[17], keypoints[20])

   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False
   pinky = pinky_open_check(keypoints, center)

   if  pinky == True and dc_4 < dc_6 and d0_8 < d0_5 and d0_12 < d0_9 and d0_16 < d0_13 and 100>a_17_20>80 and a_3_4<90:
       return True
   else:
       return False

def j_fingerspell(keypoints, center):
    def pinky_open_check(keypoints, center):
        d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
        d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
        d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
        d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
        if d20 > d19 > d18 > d17:
            return True
        else:
            return False
    def close_check_(keypoints, center):  # tested OK
        d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
        d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
        d5 = np.sqrt(np.square(keypoints[5][0] - keypoints[0][0]) + np.square(keypoints[5][1] - keypoints[0][1]))
        d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
        d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
        d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
        d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
        d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
        #d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
        #d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
        if d8 < d5 and d12 < d9 and d16 < d13 and d4 < d3:
            return True
        else:
            return False
    a_17_20 = get_angle(keypoints[17], keypoints[20])
    pinky_open = pinky_open_check(keypoints, center)
    close_check = close_check_(keypoints, center)
    p =[]
    if pinky_open == True and close_check == True and 35 < a_17_20 < 55:
        p.append(keypoints[20])
        #print(p)
        return True
    else:
        return False

def k_fingerspell(keypoints, center):
   def thumb_open_check(keypoints, center):
       d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
       d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
       if d4 > d3:
           return True
       else:
           return False
   def index_open_check(keypoints, center):
       d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
       d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
       d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
       d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
       if d8 > d7 > d6 > d5:
           return True
       else:
           return False
   def middle_open_check(keypoints, center):
       d9 = np.sqrt(np.square(keypoints[9][0] - center[0]) + np.square(keypoints[9][1] - center[1]))
       d10 = np.sqrt(np.square(keypoints[10][0] - center[0]) + np.square(keypoints[10][1] - center[1]))
       d11 = np.sqrt(np.square(keypoints[11][0] - center[0]) + np.square(keypoints[11][1] - center[1]))
       d12 = np.sqrt(np.square(keypoints[12][0] - center[0]) + np.square(keypoints[12][1] - center[1]))
       if d12 > d11 > d10 > d9:
           return True
       else:
           return False
   thumb = thumb_open_check(keypoints, center)
   index = index_open_check(keypoints, center)
   middle = middle_open_check(keypoints, center)
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
   d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
   a_9_12 = get_angle(keypoints[9], keypoints[12])
   a_5_8 = get_angle(keypoints[5], keypoints[8])
   a_2_4 = get_angle(keypoints[2], keypoints[4])
   a_0_c = get_angle(keypoints[0], center)
   a_8_p_12 = a_9_12 - a_5_8
   a_4_p_12 = a_9_12 - a_2_4
   #print(a_8_p_12)
   if thumb == True and index == True and middle == True and d16 < d13 and d20 < d17 and 70 < a_0_c < 110 and 30 < a_8_p_12 < 90\
           and 40 < a_4_p_12 < 80:
       return True
   else:
       return False

def l_fingerspell(keypoints, center):
  d10 = np.sqrt(np.square(keypoints[10][0] - keypoints[0][0]) + np.square(keypoints[10][1] - keypoints[0][1]))
  d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
  d14 = np.sqrt(np.square(keypoints[14][0] - keypoints[0][0]) + np.square(keypoints[14][1] - keypoints[0][1]))
  d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
  d18 = np.sqrt(np.square(keypoints[18][0] - keypoints[0][0]) + np.square(keypoints[18][1] - keypoints[0][1]))
  d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
  def thumb_open_check(keypoints, center):
      d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
      d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
      if d4 > d3:
          return True
      else:
          return False
  def index_open_check(keypoints, center):
      d5 = np.sqrt(np.square(keypoints[5][0] - center[0]) + np.square(keypoints[5][1] - center[1]))
      d6 = np.sqrt(np.square(keypoints[6][0] - center[0]) + np.square(keypoints[6][1] - center[1]))
      d7 = np.sqrt(np.square(keypoints[7][0] - center[0]) + np.square(keypoints[7][1] - center[1]))
      d8 = np.sqrt(np.square(keypoints[8][0] - center[0]) + np.square(keypoints[8][1] - center[1]))
      if d8 > d7 > d6 > d5:
          return True
      else:
          return False
  thumb = thumb_open_check(keypoints, center)
  index = index_open_check(keypoints, center)
  a_2_4 = get_angle(keypoints[2], keypoints[4])
  a_5_8 = get_angle(keypoints[5], keypoints[8])
  a_4_p_8 = a_2_4 - a_5_8
  #print(a_4_p_8)
  if thumb == True and index == True and d10 > d12 and d14 > d16 and d18 > d20 and 60 < a_4_p_8 < 90:
      return True
  else:
      return False

def p_fingerspell(keypoints, center):
   a_5_8 = get_angle(keypoints[5], keypoints[8])
   a_0_5 = get_angle(keypoints[0], keypoints[5])
   a_10_12 = get_angle(keypoints[10], keypoints[12])
   a_14_16 = get_angle(keypoints[14], keypoints[16])
   a_18_20 = get_angle(keypoints[18], keypoints[20])
   a_2_4 = get_angle(keypoints[2], keypoints[4])
   #print(a_10_12, a_14_16, a_18_20)
   if (350 < a_5_8 or a_5_8 < 10 ) and (350 < a_0_5 or a_0_5 < 10 ) and 240 < a_10_12 < 260 and 240 < a_14_16 < 260 \
           and 240 < a_18_20 < 260 and 285 < a_2_4 < 295 :
       return True
   else:
       return False

def t_fingetspell(keypoints, center):
    a_7_8 = get_angle(keypoints[7], keypoints[8])
    a_3_4 = get_angle(keypoints[3], keypoints[4])
    d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
    d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
    d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
    d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
    d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
    d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
    if d12 < d9 and d16 < d13 and d20 < d17 and (200 > a_7_8 > 160) and (70 < a_3_4 < 110):
        return True
    else:
        return False

def y_fingerspell(keypoints, center):
   def thumb_open_check(keypoints, center):
       d4 = np.sqrt(np.square(keypoints[4][0] - center[0]) + np.square(keypoints[4][1] - center[1]))
       d3 = np.sqrt(np.square(keypoints[3][0] - center[0]) + np.square(keypoints[3][1] - center[1]))
       if d4 > d3:
           return True
       else:
           return False
   def pinky_open_check(keypoints, center):
       d17 = np.sqrt(np.square(keypoints[17][0] - center[0]) + np.square(keypoints[17][1] - center[1]))
       d18 = np.sqrt(np.square(keypoints[18][0] - center[0]) + np.square(keypoints[18][1] - center[1]))
       d19 = np.sqrt(np.square(keypoints[19][0] - center[0]) + np.square(keypoints[19][1] - center[1]))
       d20 = np.sqrt(np.square(keypoints[20][0] - center[0]) + np.square(keypoints[20][1] - center[1]))
       if d20 > d19 > d18 > d17:
           return True
       else:
           return False
   thumb = thumb_open_check(keypoints, center)
   pinky = pinky_open_check(keypoints, center)
   d5 = np.sqrt(np.square(keypoints[5][0] - keypoints[0][0]) + np.square(keypoints[5][1] - keypoints[0][1]))
   d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))
   d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
   d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
   d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
   d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
   a_2_4 = get_angle(keypoints[2], keypoints[4])
   a_17_20 = get_angle(keypoints[17], keypoints[20])
   a_4_p_20 = a_2_4 - a_17_20
   #print(a_4_p_20)
   if thumb == True and pinky == True and d8 < d5 and d12 < d9 and d16 < d13 and 45 < a_4_p_20 < 90:
       return True
   else:
       return False

def x_fingerspell(keypoints, center):
    a_5_6 = get_angle(keypoints[5], keypoints[6])
    d9 = np.sqrt(np.square(keypoints[9][0] - keypoints[0][0]) + np.square(keypoints[9][1] - keypoints[0][1]))
    d12 = np.sqrt(np.square(keypoints[12][0] - keypoints[0][0]) + np.square(keypoints[12][1] - keypoints[0][1]))
    d13 = np.sqrt(np.square(keypoints[13][0] - keypoints[0][0]) + np.square(keypoints[13][1] - keypoints[0][1]))
    d16 = np.sqrt(np.square(keypoints[16][0] - keypoints[0][0]) + np.square(keypoints[16][1] - keypoints[0][1]))
    d17 = np.sqrt(np.square(keypoints[17][0] - keypoints[0][0]) + np.square(keypoints[17][1] - keypoints[0][1]))
    d20 = np.sqrt(np.square(keypoints[20][0] - keypoints[0][0]) + np.square(keypoints[20][1] - keypoints[0][1]))
    d10 = np.sqrt(np.square(keypoints[10][0] - keypoints[0][0]) + np.square(keypoints[10][1] - keypoints[0][1]))
    d4 = np.sqrt(np.square(keypoints[4][0] - keypoints[0][0]) + np.square(keypoints[4][1] - keypoints[0][1]))
    d6 = np.sqrt(np.square(keypoints[6][0] - keypoints[0][0]) + np.square(keypoints[6][1] - keypoints[0][1]))
    d8 = np.sqrt(np.square(keypoints[8][0] - keypoints[0][0]) + np.square(keypoints[8][1] - keypoints[0][1]))

    if d10 > d4 and d12 < d9 and d16 < d13 and d20 < d17 and d6 > d8 and (70 < a_5_6 or a_5_6 > 110):
        return True
    else:
        return False

def spell_check(keypoints, center):#この関数は指文字（アルファベット）の認識を行う。　◯_fingerspell()はアルファベットの定義した関数

    a = a_fingerspell(keypoints, center)
    b = b_fingerspell(keypoints, center)
    c = c_fingerspell(keypoints, center)
    d = d_fingerspell(keypoints, center)
    e = e_fingerspell(keypoints, center)
    f = f_fingerspell(keypoints, center)
    g = g_fingerspell(keypoints, center)
    h = h_fingerspell(keypoints, center)
    i = i_fingerspell(keypoints, center)
    k = k_fingerspell(keypoints, center)
    j = j_fingerspell(keypoints, center) #get pattern
    l = l_fingerspell(keypoints, center)
    p = p_fingerspell(keypoints, center)
    t = t_fingetspell(keypoints, center)
    y = y_fingerspell(keypoints, center)
    x = x_fingerspell(keypoints, center)
    if a == True:
        spell = "a"
    elif b == True:
        spell = "b"
    elif c == True:
        spell = "c"
    elif d == True:
        spell = "d"
    elif e == True:
        spell = "e"
    elif f == True:
        spell = "f"
    elif g == True:
        spell = "g"
    elif h == True:
        spell = "h"
    elif i == True:
        spell = "i"
    elif j == True:
        spell = "j"
    elif k == True:
        spell = "k"
    elif l == True:
        spell = "l"
    elif p == True:
        spell = "p"
    elif t == True:
        spell = "t"
    elif x == True:
        spell = "x"
    elif y == True:
        spell = "y"
    else:
        spell = " "
    cv2.putText(image, f'{spell}', (400, 500), cv2.FONT_HERSHEY_PLAIN, 6, (0, 255, 0), 3)#認識したアルファベットを画面上表示する

def pose_check(keypoints, center):#この関数は手のポーズの認識を行う
    global decide
    global close_check
    global open_check
    open_check = open_check_by_distance(keypoints, center)
    close_check = close_check_by_distance(keypoints, center)
    peace = peace_check_by_distance(center, keypoints)
    ok = ok_check_by_distance(keypoints, center)
    kitsune = kitsune_check_by_distance(center, keypoints)

    if peace == True:
        pose = "PEACE"
        if decide:
            cv2.imwrite('CaptImage/Test_{}.jpg'.format(time.localtime()), cv2.cvtColor(image, cv2.COLOR_RGB2BGR))#写真札絵を行う
            decide = False
    elif ok == True:
        pose = "OK"
        decide = True
    elif kitsune == True:
        pose = "KITSUNE"
    elif open_check:
        pose = "OPEN"
    elif close_check:
        pose = "CLOSE"
    else:
        pose = " "
    cv2.putText(image, f'{pose}', (100, 200), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)#画面上手のポーズを表示する

def calculate(keypoints):
    global decide
    global close_check
    global open_check

    if keypoints == 0:
        return 0#引数が0の場合計算しない
    center = centroid_palm(keypoints) #ひらの中心を求める
    distance_center_to_tip_all = distance_center_to_tip(keypoints, center)
    angle = get_angle(keypoints[0], center)#手の角度を求める

    #手の開閉のカウント
    if open_check == True and close_check == False:
        #pose = "OPEN"
        count_open_close(open=True, close=False)
        #print("OPEN!!")
    if open_check == False and close_check == True:
        count_open_close(open=False, close=True)
        #print("CLOSE")
        #pose = "CLOSE"

    #手のポーズと指文字の認識はそれぞれpose_check()とspell_check()関数より行う
    pose_check(keypoints, center)
    spell_check(keypoints, center)

    #print("Center:", center)
    #print('角度:',angle, '中心:', center, '中心から指先の距離', distance_center_to_tip_all)
    return angle# Test



IMAGE_FILES = []
with mp_hands.Hands(
    static_image_mode=True,
    max_num_hands=1,
    min_detection_confidence=0.5) as hands:
  for idx, file in enumerate(IMAGE_FILES):
    # Read an image, flip it around y-axis for correct handedness output (see
    # above).
    image = cv2.flip(cv2.imread(file), 1)
    # Convert the BGR image to RGB before processing.
    results = hands.process(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))

    # Print handedness and draw hand landmarks on the image.

    print('Handedness:', results.multi_handedness)
    if not results.multi_hand_landmarks:
      continue
    image_height, image_width, _ = image.shape
    annotated_image = image.copy()
    for hand_landmarks in results.multi_hand_landmarks:
      print('hand_landmarks:', hand_landmarks)
      print(
          f'Index finger tip coordinates: (',
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].x * image_width}, '
          f'{hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP].y * image_height})'
      )

      mp_drawing.draw_landmarks(
          annotated_image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imwrite(
        '/tmp/annotated_image' + str(idx) + '.png', cv2.flip(annotated_image, 1))

# For webcam input:
cap = cv2.VideoCapture(0)
fps = cap.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))
pTime = 0
with mp_hands.Hands(
    min_detection_confidence=0.8,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime


    # Flip the image horizontally for a later selfie-view display, and convert
    # the BGR image to RGB.
    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
    cv2.putText(image, f'FPS: {int(fps)}', (800, 720), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    results = hands.process(image)
    #take_coordinatesという関数がname tupleを３次元行列に２１点のランドマークを返す
    keypoints = take_coordinates(results.multi_hand_landmarks)
    if keypoints != 0:
        place = (int((keypoints[12][0]) / 10), int((keypoints[12][1]) / 15))
        #cv2.putText(image, f'{float(get_angle(keypoints[0], centroid_palm(keypoints)))}', place, cv2.FONT_HERSHEY_PLAIN,
                    #3, (255, 0, 0), 3)
    if keypoints == 0:
        place = (200, 200)
    calculate(keypoints) #この関数が全ての数値を計算してる


    #cv2.putText(image, f'{float(get_angle(keypoints, centroid_palm(keypoints)))}', place, cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

    #time.sleep(1)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    cv2.imshow('MediaPipe Hands', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()