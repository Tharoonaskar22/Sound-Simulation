#!/usr/bin/env python
# coding: utf-8

# In[5]:


import open3d as o3d
import numpy as np
import os
import sys

sys.path.append(',')


# In[32]:


pcd = o3d.io.read_point_cloud(r".xyz")
print(pcd)
print(np.asarray(pcd.points))




# In[174]:


pcd = o3d.io.read_point_cloud(r".xyz")
print(pcd)
o3d.visualization.draw_geometries([pcd])



# In[118]:


import open3d as o3d
pcd = o3d.io.read_point_cloud(r".ply")
o3d.io.write_point_cloud("sink_pointcloud.pcd", pcd)



# In[26]:


xyz = np.random.rand(100, 3)
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(xyz)
o3d.io.write_point_cloud(r".XYZ", pcd)


# In[27]:


o3d.visualization.draw_geometries([pcd])


# In[154]:


pcd = o3d.io.read_point_cloud(r".XYZ")
pcd.estimate_normals()
pcd.orient_normals_towards_camera_location(pcd.get_center())
pcd.normals = o3d.utility.Vector3dVector( - np.asarray(pcd.normals))
mesh, _ = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9)
mesh.paint_uniform_color(np.array([0.7, 0.7, 0.7]))
o3d.io.write_triangle_mesh('a.ply', mesh)


# In[15]:


o3d.io.write_point_cloud(r".XYZ",pcd)







