import json
import os
if os.path.exists('regions.json'):
    with open('regions.json', 'r') as regions:
        basejson = json.load(regions)

else:
    basejson = {'regions': []}
valid_types = ['enum', 'bits', 'text', 'signed', 'unsigned', 'percentage', 'ability']
def main():
    name = input('Input the name of the section.\n')
    type = input('Input the type of the section.\n')
    while type not in valid_types:
        print("Invalid type, please try again.")
        type = input('Input the type of the section.\n')
    if type.lower() == 'text':
        big = input('Is it big endian?')
        if big.lower() == "yes":
            big = True
        elif big.lower() == "no":
            big = False
        else:
            print('Invalid response.')
            os._exit(0)
    desc = input('Input the description of the section.\n')
    if type.lower() == 'enum':
        options = {}
        stop = False
        while stop != True:
            key = input('Input the key.\n')
            value = int(input('Input the value of the key.'))
            options[key] = value
            again = input('Add another dictionary pair? must be yes or no.\n')
            while again != 'yes' and again != 'no':
                print('Please try again.')
                again = input('Add another dictionary pair? must be yes or no.\n')
            if again == 'no':
                stop = True
            if again == 'yes':
                stop = False
    start = input("Input the start of the section.\n")
    if type.lower() == 'enum' or type.lower() == 'bits' or type.lower() == 'percentage':
        bit_start_location = int(input('Input the start of the bits in the section.\n'))
    length = int(input("Input the length of the section (in bits).\n"))
    if type.lower() == 'enum':
        return {"name": name, "type": type, "description": desc, "options": options, "start": start, "bit_start_location": bit_start_location, "length": length}
    if type.lower() == 'bits' or type.lower() == 'percentage':
        return {"name": name, "type" :type, "description": desc, "start": start, "bit_start_location": bit_start_location , "length": length}
    if type.lower() == 'text':
        return {"name": name, "type": type, "big_endian": big, "description": desc, "start": start, "length": length}
    return {"name": name, "type": type, "description": desc, "start": start, "length": length}

if __name__ == "__main__":
    stop = False
    print("Welcome to the amiibo regions maker!")
    while stop != True:
        values = main()
        basejson["regions"].append(values)
        again = input('Add another region? must be yes or no.\n')
        while again.lower() == "yes" or again.lower() == "no":
            if again.lower() == "yes":
                stop = False
                break
            elif again.lower() == "no":
                stop = True
                with open('regions.json', 'w+') as regions:
                    json.dump(obj = basejson, fp = regions, indent = 4)
                os._exit(0)
            else:
                print('Try again.')
