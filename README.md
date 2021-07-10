# Offline_speech_synthesis

## v2.0
> 优化合成性能

## 离线语音合成的简单方法
> 目前支持中文和阿拉伯数字  

## 开发环境
> ubantu18 + python3.6.7  

## 下载
```
git clone git@github.com:wxxhub/Offline_speech_synthesis.git
cd Offline_speech_synthesis
git submodule init
git submodule update
```

## 依赖安装
```shell
sudo apt-get install ffmpeg

## python3
pip3 install -r requirment.txt 
pip3 install -r speech_synthesis/requirement.txt

## python2
pip install -r requirment.txt  
pip install -r speech_synthesis/requirement.txt

## 根据实际情况使用
```

## 使用
```shell   
python3 demo.py   
```  

## 说明
> wav为处理过后的音频,更换音频可以提升合成效果。 
