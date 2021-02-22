def main():
    #light is the travel time of light in miles per seconds
    light = 186000
    #distance is the approx. distance of Mars to the Earth at the minimum
    distance = 34000000
    #Equation to how many seconds it takes to transmit to Earth, x = seconds
    x = distance/light
    #x/60 to convert into minutes
    print("It takes", str(x/60)[0:6],
          "minutes for a photo to transmit from Mars to Earth")
main()
