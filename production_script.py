import os
def main():
    os.system("python \"train.py\" --dataroot=\"E:/Image Transfer - Patches/\" --num_threads=12 --batch_size=512 --preprocess=crop --crop_size=32 --continue_train")
    # os.system("python \"test.py\" --dataroot=\"E:/Image Transfer - Patches/\" --num_threads=12 --batch_size=512 --netG=resnet_9blocks --dataset_mode=unaligned")
if __name__ == "__main__":
    main()