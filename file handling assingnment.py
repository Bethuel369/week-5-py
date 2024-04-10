try:
    with open("my_file.txt", "w") as file:
        file.write("Hi there do you know humans can live upto 100 years!")
        file.write("Once a software engenieer always a software engenieer\n")
        file.write("To buy bundles just press *544# on your phone\n")
        file.write("Many people hope that by 2040 our country will be in a better place")
    print("File 'my_file.txt' created successfully.")
except PermissionError:
    print("Permission denied. Check your file permissions.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()

try:
    with open("my_file.txt", "r") as file:
        print("Contents of my_file.txt:")
        print(file.read())
except FileNotFoundError:
    print("File not found. Make sure 'my_file.txt' exists.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()

try:
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("I Iove cars.\n")
        file.write("50% of people believe saving is good.\n")
    print("Three lines appended to 'my_file.txt'.")
except PermissionError:
    print("Permission denied. Check your file permissions.")
except Exception as e:
    print("An error occurred:", e)
finally:
    print()