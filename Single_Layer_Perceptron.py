import numpy as np
import csv  # for data load
import time

# Hyper Parameters
RND_MEAN = 0  # 정규분포 난수값의 평균
RND_STD = 0.0030  # 정규분포 난수값의 표준편차


# main function
def exec(epoch_count=10, mb_size=10, report=1):
    # epoch_count = 학습횟수
    # mb_size = 미니 배치 크기
    # report = ;
    load_dataset()
    init_model()
    train_and_test(epoch_count, mb_size, report)


def load_dataset():
    with open("./DataSet/abalone.csv") as csvfile:
        csvreader = csv.reader(csvfile)
        next(csvreader, None)
        rows = []
        for row in csvreader:
            rows.append[row]
    None


def init_model():
    None


def train_and_test():
    None
