import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import sound

chessBoard = np.zeros((8,8))
chessBoard[1::2, 0::2] = 1
chessBoard[0::2, 1::2] = 1

plt.imshow(chessBoard, cmap='binary')
sound.music()
plt.show()
