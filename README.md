# Offline_speech_synthesis

## version1.1
> 更新线程方式, 只用一个线程合成音频, 节省资源, 提高灵活性.  
> 添加reset, 快速重置, 重新播放音频.  
> 优化合成速度.  
> 解决多音字问题.  
> 添加频率设置, 可以变换频率, 改变声音, 值越小, 声音越浑厚, 值越大, 声音越尖锐, 10000-22050.  
> 暂时不支持小数, 因为部分场景考虑小数比较复杂.  
> 适配python2.7.  

## 离线语音合成的简单方法
> 目前支持中文和阿拉伯数字  

## 开发环境
> ubantu18 + python3.6.7  

## 依赖安装
```shell
## python3
pip3 install -r requirment.txt   

## python2
pip install -r requirment.txt  

## 根据实际情况使用
```

## 使用
```shell   
python3 demo.py   
```  

## 说明
> wav为处理过后的音频,更换音频可以提升合成效果。 
