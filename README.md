# Sound-Simulation
This project aims to explore noise reduction and create noiseless cities by leveraging computational methods and noise manipulation using point data.
_____________________
---------------------
Requirements
Unity 3D 
Microsoft visuals 2022
Python 3.11.0

______________________
----------------------
Method  1
1.	read AudioPeer.cs
2.	Read FastNoise.cs
3.	Read NoiseFlowfield.cs
4.	Add Audio (.wav) to Noise flow field
5.	Read AudioFlowfield.cs
6.	Input obj file into scenes and input audio file into Noise flow field source.
7.	Particle simulation depends upon intensity of the sound and depth of the form.

_____________________
---------------------
Method 2
1.	Read python code to access Numerical data from Audio source
2.	Convert the point cloud data to .csv (.xyzrgb)
3.	Read .CSV with original data (X, Y, Z, R, G, B) & Sound data (S1)
4.	Python tool (Pandas Data frame) - To manipulate data
5.	Pandas - create new data sets (X, Y, Z, R, G, B )
6.	Input the data into C# 
7.	Read readPC2.cs
8.	Visualize the output in the form of point data (spheres) 
or
9.	Read .ply in open 3d (python)



