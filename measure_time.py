from datetime import datetime, timezone


if __name__ == "__main__":
    # tokyo_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # utc_time = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")

    # t_tokyo_time = datetime.strptime(tokyo_time, "%Y-%m-%d %H:%M:%S")
    # t_utc_time = datetime.strptime(utc_time, "%Y-%m-%d %H:%M:%S")

    # diff_time = t_tokyo_time - t_utc_time

    # print(f"Tokyo time: {tokyo_time}")
    # print(f"UTC time: {utc_time}")

    start_time = "2021-06-07 04:58:46"
    end_time = "2021-06-07 05:03:07"

    t_start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    t_end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    diff_time = t_end_time - t_start_time

    print(f"Diff time: {diff_time}")