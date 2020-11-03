import pyaudio
import numpy as np
from scipy import fftpack
import wave

CHUNK = 1024  # 块大小
FORMAT = pyaudio.paInt16  # 每次采集的位数
CHANNELS = 1  # 声道数
RATE = 16000  # 采样率：每秒采集数据的次数
# RECORD_SECONDS = time  # 录音时间
# WAVE_OUTPUT_FILENAME = filename  # 文件存放位置


def recording(path_name, sampling_time, media_id, threshold=7000):
    """
    :param media_id: 文件名
    :param path_name: 文件路径
    :param sampling_time: 录音时间,如果指定时间，按时间来录音，默认为自动识别是否结束录音
    :param threshold: 判断录音结束的阈值
    :return:
    """

    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    print("* 录音中...")
    frames = []
    if sampling_time > 0:
        for i in range(0, int(RATE / CHUNK * sampling_time)):
            data = stream.read(CHUNK)
            frames.append(data)
    else:
        stop_flag = 0
        stop_flag2 = 0
        while True:
            data = stream.read(CHUNK)
            rt_data = np.frombuffer(data, np.dtype('<i2'))
            # print(rt_data*10)
            # 傅里叶变换
            fft_temp_data = fftpack.fft(rt_data, rt_data.size, overwrite_x=True)
            fft_data = np.abs(fft_temp_data)[0:fft_temp_data.size // 2 + 1]

            # 测试阈值，输出值用来判断阈值
            print(sum(fft_data) // len(fft_data))

            # 判断麦克风是否停止，判断说话是否结束，# 麦克风阈值，默认7000
            if sum(fft_data) // len(fft_data) > threshold:
                stop_flag += 1
            else:
                stop_flag2 += 1
            one_second = int(RATE / CHUNK)
            if stop_flag2 + stop_flag > one_second:
                if stop_flag2 > one_second // 3 * 2:
                    break
                else:
                    stop_flag2 = 0
                    stop_flag = 0
            frames.append(data)
    print("* 录音结束")
    stream.stop_stream()
    stream.close()
    p.terminate()
    with wave.open(f"{path_name}\\Media\\UploadAudio\\{media_id}", 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
