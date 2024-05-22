def extract_info(path_file):
    epochs = []
    accuracy_train = []
    loss_train = []
    accuracy_val = []
    loss_val = []
    count = 0
    for line in open(path_file, encoding='utf-8'):
        line_string = str(line)
        if count % 2 == 0:
            epochs.append(line_string[6:len(line_string)-])

extract_info('DeepLearning-DrowsinessDetection/info/slice1.txt')