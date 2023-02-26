# Sound-Simulation
This project aims to explore noise reduction and create noiseless cities by leveraging computational methods and noise manipulation using point data.
_____________________
---------------------
Requirements:
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

__________________________
--------------------------
METHODOLOGY:

1.Camera - To gather data
2.Reality Capture - Data Visualization
3.Noise Dosimetry - To collect Audio data
4.Read .CSV with original data (X, Y, Z, R, G, B) & Sound data (S1)
5.Python tool (Pandas Data frame) - To manipulate data
6.Pandas - create new data sets (X, Y, Z, R, G, B) 
7.Export - .CSV file from Pandaas
8.Input the data into C# 
9.C# -To create spheres with input & Unity 3D - to visualize output 
10.Point cloud data (.PLY file)  into Open 3D to see the output
11.Simulating data as Flow Field Direction in Unity 3D
12.To assign the colours to generated spheres
13.Collision of a particle to the Building 



