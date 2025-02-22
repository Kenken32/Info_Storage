#Dictionary {}. pair between key and value

conversion_factors = {"distance" :{"mm":1,
                                   "cm":0.1,
                                   "m":0.001,
                                   "km":0.000001,
                                   "inch":0.03937008,
                                   "yard":0.00109361,
                                   "feet":0.00328084,
                                   "miles":6.2137E-7},
                      "weight":{"mg": 1,
                                "gr": 0.01,
                                "kg": 0.000001},
                      "time" : {"hour" : 1,
                                "minute" : 60,
                                "second" : 60*60,
                                "day" : 1/24,
                                "week" : 1/24*7,
                                "month" : 1/24*7*4,
                                "year" : 1/24*7*4*12,
                                "decade" : 1/24*7*4*12*10,
                                "century" : 1/24*7*4*12*10*10}}
#                       "speed" : {"1cm" : 1,
#                                  "cm/min" : 1*60,
#                                  "cm/h" : 1*60*60},
#                                  "m/s" : 1/100}}


        
#print(type(conversion_factors))
#print(conversion_factors.keys())
#print(conversion_factors.values())

#print(conversion_factors["m"])

input_number = 1
base_factor = conversion_factors["time"]["day"]
conver_factor = conversion_factors["time"]["year"]

converted_value = input_number / base_factor * conver_factor

print(converted_value)