# Encryption and Decryption Project - Shark Hack 2023
### This project is in collaboration with Zoey Zeballos, Anna Saunders, and Christine Felt.
Our team won Best Community Hack at Simmons University's 2023 Shark Hack Hackathon with this project. We wrote a program that randomly generates an invertible matrix to encrypt inputted messages. Messages are split into sections of length n, corresponding with the dimensions of the n x n encoding matrix (creating lists of lists). Each character is converted to its corresponding number and each section is multiplied by the encoding matrix. Encrypted messages are converted to Strings and are printed to the screen. To decrypt messages, the inverse of the encoding matrix is found through performing Gauss-Jordan elimination with helper methods that expand and halve the matrix (to add and remove the identity matrix) as well as ones that multiply and add rows. Each section of the message is multiplied by the decoding matrix and each number is converted to its corresponding character. Decrypted messages are converted to Strings and are printed to the screen.
