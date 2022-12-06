def wave_length_visible():
    wavelength = int(input())
    if wavelength >=380 and wavelength <= 750:
        if wavelength >= 380 and wavelength< 450:
            print("Violet")
        elif wavelength >= 450 and wavelength< 495:
            print("Blue")
        elif  wavelength >= 495 and wavelength< 570:
            print("Green")
        elif  wavelength >= 570 and wavelength< 590:
            print("Yellow")
        elif  wavelength >= 590 and wavelength< 620:
            print("Orange")
        else:
            print("Red")
    else:
        print("The wavelength entered is out of visible spectrum")



wave_length_visible()