from random import uniform
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep
from loguru import logger
from tqdm import tqdm

logger.add(".logs/file_{time}.log", retention=3, level="DEBUG")


def main() -> None:
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = [executor.submit(test_task, i) for i in range(100)]

        for future in tqdm(
            as_completed(futures),
            desc="Processing tasks",
            unit="task",
            total=len(futures),
        ):
            try:
                future.result()  # Wait for the task to complete
            except Exception as e:
                logger.error(f"Task failed with exception: {e}")

    logger.success("Processing complete!")


def test_task(task_id: int) -> int:
    sleep(uniform(0.1, 1.0))

    return task_id


if __name__ == "__main__":
    main()
