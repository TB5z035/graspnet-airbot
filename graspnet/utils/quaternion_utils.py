""" Rotation_matrix to Quaternion.
    Author: Hongrui-Zhu
"""

import numpy as np
from scipy.spatial.transform import Rotation

def rota_to_quat(rotation_matrix):

    # 将旋转矩阵转换为四元数
    r = Rotation.from_matrix(rotation_matrix)
    quaternion = r.as_quat()

    # 计算旋转四元数和 (1, 0, 0) 之间的差异
    target_rotation = Rotation.from_rotvec(np.pi / 2 * np.array([1, 0, 0]))
    desired_quaternion = r * target_rotation
    desired_quaternion = desired_quaternion.as_quat()
    # print(desired_quaternion)
    
    return desired_quaternion

if __name__=='__main__':
    pass