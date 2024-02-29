def determine_hand(file_name):
    from keras.models import load_model  # TensorFlow is required for Keras to work
    from PIL import Image, ImageOps  # Install pillow instead of PIL
    import numpy as np

    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open("image.jpg").convert("RGB")

    # resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    # print("Class:", class_name[2:], end="")
    # print("Confidence Score:", confidence_score)
    return class_name[2:-1] # to get the substring without the new line element
# print(determine_hand('image.jpg'))

from random import choice
# hands = ["rock", "paper", "scissor"]
# print(choice(hands))

def get_computer_hand():
  hands = ['rock', 'paper', 'scissor']
  return choice(hands)

def get_player_hand():
   # in the case where the picture taking does not work
   # hand = input('Enter hand: (rock, paper, scissor): ')
   # return determineHand(hand + ".jpg").lower()

   # To take a picture
   import cv2

   cap = cv2.VideoCapture(0)
   ret, frame = cap.read()
   cap.release()
   cv2.imwrite('image.jpg', frame)

   return determine_hand("image.jpg").lower()

def determine_who_won(computer, player):

    if computer == player:
        return "draw"
    elif (player == "rock" and computer == "scissor") or (player == "scissor" and computer == "paper") or (player == "paper" and computer == "rock"):
        return "player wins"
    else:
        return "computer wins"

computer_score = 0
player_score = 0

while True:
   print("Welcome to Rock, Paper, Scissor the game!")
   print("Computer decides on a hand...")
   print("CURRENT SCORES ")
   print("Computer: " + str(computer_score))
   print("Player: " + str(player_score))
   computer_hand = get_computer_hand()
   player_hand = get_player_hand()
   print('Computer gives ' + computer_hand)
   print('Player gives ' + player_hand)
   x = determine_who_won(computer_hand, player_hand)

   if x == "draw":
     print("it's a draw!")
   elif x == "player wins":
     print("Player wins!")
     player_score += 1
   else:
     print("Computer wins")
     computer_score += 1




