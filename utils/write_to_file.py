def write_to_file(img, img_type):
    with open('pet.txt', 'w') as f:
        f.write(img)
        f.write('\n'+img_type)
    
