# Start FROM Nvidia PyTorch image https://ngc.nvidia.com/catalog/containers/nvidia:pytorch
FROM nvcr.io/nvidia/pytorch:21.10-py3


# Install linux packages
RUN apt update && apt install -y zip htop screen libgl1-mesa-glx

RUN apt install libgl1-mesa-glx
RUN apt-get install libglib2.0-0

# Install python dependencies
COPY requirements.txt .
RUN python -m pip install --upgrade pip
RUN pip uninstall -y nvidia-tensorboard nvidia-tensorboard-plugin-dlprof
RUN pip install --no-cache -r requirements.txt albumentations coremltools onnx gsutil notebook numpy Pillow wandb>=0.12.2
RUN pip install --no-cache torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html


# Copy contents
COPY . .

#RUN pwd
RUN python3 detect.py --weights runs/train/exp_15_epoch_points_pre-entraines/weights/best.pt --source 0