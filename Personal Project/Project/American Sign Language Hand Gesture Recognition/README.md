# Project- American Sign Language Hand Gesture Recognition

## Project Overview & aims

While there are new and accessible technologies emerging to help those with hearing disabilities, there is still plenty of work to be done. For example, Deep learning algorithms could help the deaf and hard-of-hearing even further by offering ways to better communicate using computer vision applications. Our project aims to do just that.
We sought to create a system that is capable of identifying American Sign Language (ASL) hand gestures.

## Project Summary

## Goal:
Build a system that can correctly identify American Sign Language signs that corresponds to the hand gestures

## Method:
- The static sign language data for our project was in the form of images. We trained a Convolutional Neural Network (CNN) to identify the signs represented by each of these images.
- The dynamic sign language dataset we used was collected by a LeapMotion Controller (LMC) and was in the form of (x, y, z) coordinates of each joint of each hand collected every few milliseconds

## Applications:
- Our proposed system will help the deaf and hard-of-hearing communicate better with members of the community.
- For example, there have been incidents where those who are deaf have had trouble communicating with first responders when in need.
- Although responders may receive training on the basics of ASL, it is unrealistic to expect everyone to become fully fluent in sign language.
- Down the line, advancements like these in computer recognition could aid a first responder in understanding and helping those that are unable to communicate through speech.
- Another application is to enable the deaf and hard-of-hearing equal access to video consultations, whether in a professional context or while trying to communicate with their healthcare providers via telehealth. Instead of using basic chat, these advancements would allow the hearing-impaired access to effective video communication.

## Performance:
The proposed model for the still images is able to identify the static signs with an accuracy of 98.68%.

# Ref:
- https://keras.io/preprocessing/image/
- https://medium.com/@vijayabhaskar96/tutorial-image-classification-with-keras-flow-from-directory-and-generators-95f75ebe5720
- https://towardsdatascience.com/american-sign-language-hand-gesture-recognition-f1c4468fb177
- https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0 (Displaying curves of loss and accuracy during training)
- https://github.com/gabrielpierobon/cnnshapes/blob/master/README.md (Visualizing intermediate activation in Convolutional Neural Networks with Keras) https://www.kaggle.com/amarjeet007/visualize-cnn-with-keras
- https://towardsdatascience.com/overfitting-vs-underfitting-a-complete-example-d05dd7e19765
