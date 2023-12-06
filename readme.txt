#：可能会与官方的安装流程有所出入，因为在官方的基础上修改了一些编译的bug，并添加了一些文件
#：新增 GraspPosePre.py 和 utils/quaternion_utils.py ，其中前者是API接口文件，后者为四元数转化函数文件

# 安装步骤
1、
cd graspnet-baseline
pip install -r requirements.txt

2、
安装本机对应的版本的pytorch和torchvision

3、
cd pointnet2
python setup.py install

4、
cd knn
python setup.py install

5、
cd graspnetAPI
pip install .

# 测试是否安装成功
6、
bash command_demo.sh 

# API调用示例：
7、
    from GraspPosePre import GraspPosePrediction
    ......
    grasp = GraspPosePrediction()
    translation, quaternion = grasp.get_grasp(point_cloud, workspace_mask)

Note: 可以根据不同的硬件参数（例如："self.camera_width"  "self.camera_high" "self.intrinsic" "self.factor_depth"）以及不同的网络需求修改GraspPosePrediction()的初始化参数