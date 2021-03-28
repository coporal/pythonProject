import errno
import os

def folderdh():
    try:
        if not (os.path.isdir({"1_다운로드 링크"})):
            os.makedirs(os.path.join({"1_다운로드 링크"}))

        if not (os.path.isdir({"2_유투브 영상"})):
            os.makedirs(os.path.join({"유투브 영상"}))

        if not (os.path.isdir({"3_사용자 메뉴얼"})):
            os.makedirs(os.path.join({"3_사용자 메뉴얼"}))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("파일생성실패")
            raise


if __name__ == '__main__':
    folderdh()


