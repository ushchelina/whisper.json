# GPU

## Настройка под Linux.

```sh
python3 -V
Python 3.8.10
sudo apt install python3.8-dev python3.8-venv 

# sudo apt update
# sudo apt upgrade
# sudo apt install software-properties-common -y
# sudo add-apt-repository ppa:deadsnakes/ppa
# sudo apt update
# sudo apt-get install build-essential python3.10 git zip unzip screen
# sudo apt install python3-pip
```

## Links

-[Could not load library libcudnn_ops_infer.so.8](https://github.com/SYSTRAN/faster-whisper/issues/516#issuecomment-1972615012)
-[Issues Installing CUDA and cuDNN on Ubuntu 24.04](https://askubuntu.com/questions/1520509/issues-installing-cuda-and-cudnn-on-ubuntu-24-04)
-[https://askubuntu.com/questions/1536271/can-i-install-cuda-11-4-in-ubuntu-24-04-if-so-how](https://askubuntu.com/questions/1536271/can-i-install-cuda-11-4-in-ubuntu-24-04-if-so-how)
-[v4.5.0 is not compatible with torch>=2.*.*+cu121](https://github.com/OpenNMT/CTranslate2/issues/1806#issue-2610861176)

```sh
sudo apt install nvidia-cuda-toolkit nvidia-utils-525 ubuntu-drivers-common unzip
sudo ubuntu-drivers autoinstall
sudo reboot now
nvcc --version
nvidia-smi
pip install nvidia-cublas-cu12 nvidia-cudnn-cu12==9.*
pip install --force-reinstall ctranslate2==4.4.0
./venv/bin/python -m pip install nvidia-cublas-cu11 nvidia-cudnn-cu11
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/home/vit/whisper.nemo/venv/lib/python3.12/site-packages/nvidia/cublas/lib/:/home/vit/whisper.nemo/venv/lib/python3.12/site-packages/nvidia/cudnn/lib/
```

```text
Unable to load any of {libcudnn_ops.so.9.1.0, libcudnn_ops.so.9.1, libcudnn_ops.so.9,

https://github.com/MahmoudAshraf97/whisper-diarization/issues/259

thanks @roboatLee @MahmoudAshraf97 for help. I found the solution.
sudo apt-get install libcudnn9-cuda-12 9.5.1.17-1 (for cuda 12)
apt-get install libcudnn9-cuda-11 9.5.1.17-1 (for cuda 11)
find / |grep libcudnn_ops
export LD_LIBRARY_PATH = $LD_LIBRARY_PATH:/path/to/you
or simply copy the libcudnn_ops.so.9 to the destination where script actually looking for it.
```

Installation Instructions:

```sh
wget https://developer.download.nvidia.com/compute/nvidia-driver/580.105.08/local_installers/nvidia-driver-local-repo-ubuntu2404-580.105.08_1.0-1_amd64.deb
sudo dpkg -i nvidia-driver-local-repo-ubuntu2404-580.105.08_1.0-1_amd64.deb
sudo cp /var/nvidia-driver-local-repo-ubuntu2404-580.105.08/nvidia-driver-*-keyring.gpg /usr/share/keyrings/
sudo apt-get update
```

NVIDIA Driver Instructions
To install the open kernel module flavor:

```sh
sudo apt-get install -y nvidia-open-580
```

To install the proprietary kernel module flavor:

```sh
sudo apt-get install -y cuda-drivers-580
```

## GPU CUDA в Ubuntu 24.04 LTS

Здравствуйте.

В Яндекс Облаке у меня имеется виртуальная машина в следующей конфигурации.

- Intel Ice Lake with NVIDIA® Tesla® T4
- Количество GPU 1
- ОС Ubuntu 24.04 LTS

Я запускаю там программу на Python с использованием библиотеки Torch.
Torch работает без использования GPU на центральном процессоре.

Я хочу запустить Torch на GPU (режим cuda) для сравнения производительности работы программы в двух режимах: с GPU и без GPU.

У меня не получается настроить Ubuntu таким образом, чтобы в системе было доступно устройство 'cuda' версии 11.
Непонятно, какие драйвера устанавливать для этого.

Нет ли у вас образа с уже настроенным устройством cuda11 ?
Или подскажите пожалуйста, куда копать для решения этой проблемы, на используемой сейчас Ubuntu 24.04 LTS.
