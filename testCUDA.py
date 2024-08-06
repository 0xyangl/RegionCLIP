import torch

def check_cuda():
    print("PyTorch version:", torch.__version__)
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA version:", torch.version.cuda)
    print("cuDNN version:", torch.backends.cudnn.version())

    if torch.cuda.is_available():
        print("Number of GPUs:", torch.cuda.device_count())
        print("Current GPU device:", torch.cuda.current_device())
        print("Current GPU name:", torch.cuda.get_device_name(torch.cuda.current_device()))

if __name__ == "__main__":
    check_cuda()
