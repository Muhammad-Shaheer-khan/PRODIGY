import time
import numpy as np
from PIL import Image

def encrypt_image(input_image_path, output_image_path, user_number):

    start_time = time.time()

    try:
        image = Image.open(input_image_path).convert("RGB")
        width, height = image.size
        pixels = np.array(image)

        user_number = user_number % 256

        encrypted_img_array = (pixels + user_number) % 256

        encrypted_img = Image.fromarray(encrypted_img_array.astype(np.uint8))
        encrypted_img.save(output_image_path)

        end_time = time.time()
        print(f"Image encrypted successfully and saved to: {output_image_path}")
        print(f"Encryption time: {end_time - start_time:.2f} seconds")

    except FileNotFoundError:
        print(f"Error: Input image file not found at: {input_image_path}")


def decrypt_image(encrypted_image_path, output_image_path, user_number):

    start_time = time.time()

    try:
        encrypted_img = Image.open(encrypted_image_path)
        width, height = encrypted_img.size
        pixels = np.array(encrypted_img)

        user_number = user_number % 256

        decrypted_img_array = (pixels - user_number) % 256

        decrypted_img = Image.fromarray(decrypted_img_array.astype(np.uint8))
        decrypted_img.save(output_image_path)

        end_time = time.time()
        print(f"Image decrypted successfully and saved to: {output_image_path}")
        print(f"Decryption time: {end_time - start_time:.2f} seconds")

    except FileNotFoundError:
        print(f"Error: Encrypted image file not found at: {encrypted_image_path}")


input_image_path = "t2.png"  
output_encrypted_path = "encrypted_image.png"
output_decrypted_path = "decrypted_image.png"

user_number = int(input("Enter a random number: "))  

encrypt_image(input_image_path, output_encrypted_path, user_number)
decrypt_image(output_encrypted_path, output_decrypted_path, user_number)
