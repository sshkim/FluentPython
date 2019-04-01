from concurrent import futures

from flags import save_flag, get_flag, show, main

MAX_WORKERS = 20  # ThreadPoolExecutor에서 사용할 Worker 수


def download_one(cc):
    image = get_flag(cc)
    show(cc)
    save_flag(image, cc.lower() + '.gif')
    return cc


def download_many(cc_list):
    workers = min(MAX_WORKERS, len(cc_list))  # Worker의 최대 값은 list size
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(download_one, sorted(cc_list))  # 반환한 값을 가져올 수 있도록 반복할 수 있는 제너레이터를 반환한다. return generator

    return len(list(res))  # download_one 함수에서 에러가 발생시 여기서 발생한다. 제너레이터에서 에러 발생했을 경우를 생각해보자.


if __name__ == '__main__':
    main(download_many)
