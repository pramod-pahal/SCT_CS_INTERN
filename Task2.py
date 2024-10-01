from PIL import Image
import random

def swap_pixels(image, seed):
    random.seed(seed)
    width, height = image.size
    pixels = list(image.getdata())
    pixel_count = width * height
    
    for i in range(pixel_count):
        swap_index = random.randint(0, pixel_count - 1)
        pixels[i], pixels[swap_index] = pixels[swap_index], pixels[i]
    
    image.putdata(pixels)
    return image

def add_value_to_pixels(image, value):
    pixels = list(image.getdata())
    new_pixels = []

    for pixel in pixels:
        new_pixel = tuple((p + value) % 256 for p in pixel)
        new_pixels.append(new_pixel)

    image.putdata(new_pixels)
    return image

def encrypt_image(image_path, operation, key):
    image = Image.open(image_path)
    
    if operation == 'swap':
        encrypted_image = swap_pixels(image, key)
    elif operation == 'add':
        encrypted_image = add_value_to_pixels(image, key)
    else:
        raise ValueError("Invalid operation")
    
    encrypted_image.save('encrypted_image.png')
    print("Image encrypted and saved as 'encrypted_image.png'.")

def decrypt_image(image_path, operation, key):
    image = Image.open(image_path)
    
    if operation == 'swap':
        decrypted_image = swap_pixels(image, key)  # Swapping twice with the same seed reverses the operation
    elif operation == 'add':
        decrypted_image = add_value_to_pixels(image, -key)
    else:
        raise ValueError("Invalid operation")
    
    decrypted_image.save('decrypted_image.png')
    print("Image decrypted and saved as 'decrypted_image.png'.")

def main():
    while True:
        print("Image Encryption Tool")
        print("1. Encrypt Image")
        print("2. Decrypt Image")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            image_path = input("Enter the path to the image: ")
            operation = input("Choose operation ('swap' or 'add'): ")
            key = int(input("Enter the encryption key (integer): "))
            encrypt_image(image_path, operation, key)

        elif choice == '2':
            image_path = input("Enter the path to the encrypted image: ")
            operation = input("Choose operation ('swap' or 'add'): ")
            key = int(input("Enter the decryption key (integer): "))
            decrypt_image(image_path, operation, key)

        elif choice == '3':
            break

        else:
            print("Invalid option, please choose again.\n")

if __name__ == "__main__":
    main()
