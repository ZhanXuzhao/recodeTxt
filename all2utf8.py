from sc.textfile import txtfile

if __name__ == '__main__':
    # 注意路径\需要手工改为\\
    yourpath = "D:\\Projects\\GHY\语料\\01先秦"
    file_ext='.txt|.csv'
    txtfile.allpath_txt_encoding_to_utf8(yourpath, file_ext)